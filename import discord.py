import discord
from discord import app_commands
from discord.ext import commands
from config import TOKEN

bot = commands.bot(command_prefix="!", intents = discord.Intents.all())

TOKEN.run("MTA1OTE0MDg2MjMyMTM2OTEyOQ.GPZKmX.WLF4uy0G8OKP8jhGkRkBBKcOEojezrjxZ0C1V0")

@bot.event
async def on_ready():
    print("Bot is Up and Ready")
    try:    
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.tree.command(name="hello")
async def hello(interaction: discord.interaction):
    await interaction.response.send_message (f"Hey {interaction.user.mention}! this is a slash command!", ephemeral=True)

    @bot.tree.command(name="say")
    @app_commands.describe(thing_to_say = "What should I say?")
    async def say(interaction: discord.Interaction, thing_to_say: str):
        await interaction.response.send_message(f"{interaction.user.name} said: `{thing_to_say}` ")

bot.run(TOKEN) 
