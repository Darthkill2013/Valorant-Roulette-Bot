# Discord.py Erweiterung für Commands importieren
# 'commands' erlaubt es dir, Bot-Commands zu definieren, z.B. !agent oder /roulette
from discord.ext import commands

# Logging Modul importieren
# Damit kann der Bot dir in der Konsole Infos, Warnungen oder Fehler anzeigen
import logging

# dotenv Modul importieren
# Damit kannst du sensible Daten (z.B. Token) aus einer .env Datei laden
from dotenv import load_dotenv

# OS Modul importieren
# Wird benötigt, um Umgebungsvariablen aus dem Betriebssystem abzufragen
import os

# Lädt alle Variablen aus der Datei .env in die Umgebung
# Du kannst in der .env z.B. DISCORD_TOKEN=DeinBotToken schreiben
load_dotenv()

# Speichert den Bot-Token aus der Umgebungsvariable in die Variable 'token'
# Wichtig: Der Token ist geheim – NICHT in Code posten!
token = os.getenv('DISCORD_TOKEN')