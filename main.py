import discord
from discord import app_commands
import json
import random
from dotenv import load_dotenv
import os
import logging

# ----------------------------
# Load environment variables
# ----------------------------
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Logging
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

# Intents
intents = discord.Intents.default()

# ----------------------------
# Discord Client mit Slash Commands
# ----------------------------
class MyClient(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        # Synchronisiere Slash Commands
        await self.tree.sync()
        print("✅ Slash Commands synchronisiert")

client = MyClient()

# ----------------------------
# CHAR ROULETTE
# ----------------------------
@client.tree.command(name="char_roulette", description="Zufällige Valorant Agents auswählen")
@app_commands.describe(anzahl="Anzahl der Spieler (1–5)")
async def char_roulette(interaction: discord.Interaction, anzahl: int):

    if not 1 <= anzahl <= 5:
        await interaction.response.send_message(
            "❌ Bitte eine Zahl zwischen 1 und 5 angeben!",
            ephemeral=True
        )
        return

    try:
        with open("agents.json", "r", encoding="utf-8") as f:
            agents = json.load(f)
    except FileNotFoundError:
        await interaction.response.send_message("❌ agents.json nicht gefunden!", ephemeral=True)
        return

    if len(agents) < anzahl:
        await interaction.response.send_message("❌ Nicht genug Agents in der Liste!", ephemeral=True)
        return

    auswahl = random.sample(agents, anzahl)

    nachricht = "🎲 **Character Roulette Ergebnisse:**\n"
    for i, char in enumerate(auswahl, start=1):
        nachricht += f"Spieler {i}: {char['role']} {char['name']} {char['emoji']}\n"

    await interaction.response.send_message(nachricht)

# ----------------------------
# WEAPON ROULETTE
# ----------------------------
@client.tree.command(name="weapon_roulette", description="Zufällige Waffe nach Budget auswählen")
@app_commands.describe(budget="Dein verfügbares Geld")
async def weapon_roulette(interaction: discord.Interaction, budget: int):

    try:
        with open("weapons.json", "r", encoding="utf-8") as f:
            weapons = json.load(f)
    except FileNotFoundError:
        await interaction.response.send_message("❌ weapons.json nicht gefunden!", ephemeral=True)
        return

    affordable = [w for w in weapons if w["cost"] <= budget]

    if not affordable:
        await interaction.response.send_message(
            "❌ Keine Waffe in deinem Budget 😭",
            ephemeral=True
        )
        return

    weapon = random.choice(affordable)

    await interaction.response.send_message(
        f"🔫 **Deine Waffe:** {weapon['name']}\n"
        f"Viel Erfolg {interaction.user.mention}!"
    )

# ----------------------------
# BOT START
# ----------------------------
client.run(TOKEN, log_handler=handler, log_level=logging.DEBUG)
