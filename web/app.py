#!/usr/bin/env python3
import json
import os
import signal
import subprocess
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEB_ROOT = os.path.dirname(os.path.abspath(__file__))
SERVER_SCRIPT = os.path.join(ROOT, 'minecraft')
PID_FILE = os.path.join(ROOT, 'minecraft-server', 'server', 'server.pid')
process_lock = threading.Lock()


def load_pid():
    try:
        with open(PID_FILE, 'r') as f:
            return int(f.read().strip())
    except Exception:
        return None


def save_pid(pid: int):
    os.makedirs(os.path.dirname(PID_FILE), exist_ok=True)
    with open(PID_FILE, 'w') as f:
        f.write(str(pid))


def is_running(pid: int) -> bool:
    if pid is None:
        return False
    try:
        os.kill(pid, 0)
        return True
    except OSError:
        return False


def init_minecraft():
    server_folder = os.path.join(ROOT, 'minecraft-server', 'server')
    if os.path.exists(os.path.join(server_folder, 'start.sh')) and os.path.exists(os.path.join(server_folder, 'paper-1.20.1.jar')):
        return

    proc = subprocess.run([
        SERVER_SCRIPT,
        'init'
    ], cwd=WEB_ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or 'Error al inicializar el servidor')


def start_minecraft():
    with process_lock:
        existing = load_pid()
        if existing and is_running(existing):
            return existing

        init_minecraft()

        proc = subprocess.Popen([
            SERVER_SCRIPT,
            'start'
        ], cwd=WEB_ROOT, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL, start_new_session=True)
        save_pid(proc.pid)
        return proc.pid


class RequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == '/index.html' or self.path == '/iniciar' or self.path == '/iniciar.html':
            self.path = '/iniciar.html'
            return super().do_GET()
        if self.path == '/status':
            pid = load_pid()
            running = pid is not None and is_running(pid)
            message = 'Servidor en ejecución (PID ' + str(pid) + ')' if running else 'Servidor detenido'
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(json.dumps({'running': running, 'message': message}).encode('utf-8'))
            return
        return super().do_GET()

    def do_POST(self):
        if self.path == '/start':
            try:
                pid = start_minecraft()
                running = pid is not None and is_running(pid)
                message = 'Servidor iniciado (PID ' + str(pid) + ')' if running else 'No se pudo iniciar el servidor'
                self.send_response(200)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.end_headers()
                self.wfile.write(json.dumps({'running': running, 'message': message}).encode('utf-8'))
            except Exception as exc:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.end_headers()
                self.wfile.write(json.dumps({'running': False, 'message': str(exc)}).encode('utf-8'))
            return
        self.send_error(404, 'Not found')

    def log_message(self, format, *args):
        return


def main():
    os.chdir(WEB_ROOT)
    server = HTTPServer(('0.0.0.0', 8080), RequestHandler)
    print('Servidor web iniciado en http://localhost:8080')
    server.serve_forever()


if __name__ == '__main__':
    main()
