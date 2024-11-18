import discord
from discord import app_commands
from discord.ext import commands
import requests

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Logged in as {bot.user}!")

# Command 1: Generate Loadstring
@bot.tree.command(name="generate_loadstring")
async def generate_loadstring(interaction: discord.Interaction, script: str):
    try:
        url = "http://127.0.0.1:5000/generate_loadstring"  # Replace with your server URL if hosted elsewhere
        response = requests.post(url, json={"script": script})
        response_data = response.json()

        if "loadstring" in response_data:
            await interaction.response.send_message(f"Generated Loadstring: `{response_data['loadstring']}`")
        else:
            await interaction.response.send_message(f"Error: {response_data.get('error', 'Unknown error')}", ephemeral=True)
    except Exception as e:
        await interaction.response.send_message(f"An error occurred: {str(e)}", ephemeral=True)

# Command 2: Hold Search
@bot.tree.command(name="hold_search")
async def hold_search(interaction: discord.Interaction):
    await interaction.response.send_message("Hold search initiated. Please wait...")
    # Add your hold search logic here

bot.run("MTMwNzg2MTY0MTU4NDcwOTcyMw.GyMFcW.GEOuQLg1H1rhltGIy1EVGh9LO4ZVzBwc7aCHuY")
