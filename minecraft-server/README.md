# Servidor Minecraft 1.20.1 con plugin de día de 3 horas

Esta carpeta contiene todo lo necesario para descargar, crear y ejecutar un servidor
Paper 1.20.1 con un plugin que regula el tiempo del día para durar 3 horas reales.

## Uso

1. Entra en la carpeta:
   ```bash
   cd minecraft-server
   ```

2. Inicializa el servidor:
   ```bash
   ./minecraft init
   ```

3. Inicia el servidor:
   ```bash
   ./minecraft start
   ```

4. Comprueba el estado:
   ```bash
   ./minecraft status
   ```

## Qué hace

- Descarga un JDK local en `minecraft-server/jdk`
- Descarga Paper 1.20.1 en `minecraft-server/server`
- Descarga ECJ para compilar el plugin
- Compila y coloca el plugin en `minecraft-server/server/plugins`
- Genera la configuración básica de servidor

## Advertencias

- Este script necesita `curl`, `wget` o `python3` para descargar archivos.
- También requiere `tar` para extraer el JDK.

