import discord
from discord import app_commands
from discord.ext import commands
import requests

# ----- Configuration -----
API_BASE_URL = "https://yourapi.com"  # Replace with your actual API base URL
BOT_TOKEN = "YOUR_DISCORD_BOT_TOKEN"  # Replace with your actual bot token

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s).")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

# ----- /list Command -----
@bot.tree.command(name="list", description="List all currently running Minecraft servers")
async def list_servers(interaction: discord.Interaction):
    response = requests.get(f"{API_BASE_URL}/servers/list")
    
    if response.status_code == 200:
        await interaction.response.send_message(response.text)  # Directly send API response
    else:
        await interaction.response.send_message("Failed to retrieve server list.", ephemeral=True)

# ----- /inspect {SERVER_ID} Command -----
@bot.tree.command(name="inspect", description="Get details of a specific Minecraft server")
@app_commands.describe(server_id="The ID of the server to inspect")
async def inspect_server(interaction: discord.Interaction, server_id: str):
    response = requests.get(f"{API_BASE_URL}/servers/inspect/{server_id}")
    
    if response.status_code == 200:
        await interaction.response.send_message(response.text)  # Directly send API response
    else:
        await interaction.response.send_message("Server not found or failed to fetch details.", ephemeral=True)

# ----- /logs {SERVER_ID} Command -----
@bot.tree.command(name="logs", description="Retrieve the last 50 logs of a Minecraft server")
@app_commands.describe(server_id="The ID of the server to fetch logs for")
async def get_logs(interaction: discord.Interaction, server_id: str):
    response = requests.get(f"{API_BASE_URL}/servers/logs/{server_id}")
    
    if response.status_code == 200:
        await interaction.response.send_message(f"```{response.text}```")  # Directly send logs
    else:
        await interaction.response.send_message("Failed to retrieve logs.", ephemeral=True)

# Run the bot
bot.run(BOT_TOKEN)
