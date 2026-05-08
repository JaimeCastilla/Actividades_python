package com.example.daylength;

import org.bukkit.Bukkit;
import org.bukkit.World;
import org.bukkit.plugin.java.JavaPlugin;
import org.bukkit.scheduler.BukkitRunnable;

public final class DayLengthPlugin extends JavaPlugin {
    private static final long TICK_INCREMENT = 1L;
    private static final long TICK_DELAY = 9L;

    @Override
    public void onEnable() {
        getLogger().info("DayLengthPlugin activado: el día durará 3 horas reales.");

        for (World world : Bukkit.getWorlds()) {
            world.setGameRule(org.bukkit.GameRule.DO_DAYLIGHT_CYCLE, false);
        }

        new BukkitRunnable() {
            private long counter = 0;

            @Override
            public void run() {
                counter++;
                if (counter < TICK_DELAY) {
                    return;
                }
                counter = 0;
                for (World world : Bukkit.getWorlds()) {
                    long time = world.getTime() + TICK_INCREMENT;
                    if (time >= 24000L) {
                        time -= 24000L;
                    }
                    world.setTime(time);
                }
            }
        }.runTaskTimer(this, 0L, 1L);
    }

    @Override
    public void onDisable() {
        getLogger().info("DayLengthPlugin desactivado.");
    }
}
