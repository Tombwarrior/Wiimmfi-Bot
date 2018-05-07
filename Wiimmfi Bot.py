import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
        print("Bot is ready!")
        await client.change_presence(game=discord.Game(name='Wiimmfi'))

@client.event
async def on_message(message):
    if message.content == "!wiimmfi":
        await client.send_message(message.channel, "Wiimmfi Main Page: https://wiimmfi.de")
    elif message.content == "!status":
        await client.send_message(message.channel, "Wiimmfi Status: https://wiimmfi.de/stat?m=8")
    elif message.content == "!mkw":
        await client.send_message(message.channel, "Wiimmfi MKW Status: https://wiimmfi.de/mkw")
    elif message.content == "!wiimmfibans":
        await client.send_message(message.channel, "Wiimmfi Bans: https://wiimmfi.de/show-bans")
    elif message.content == "!regions":
        await client.send_message(message.channel, "Wiimmfi Regions: https://wiimmfi.de/reg-list")
    elif message.content == "!comp":
        await client.send_message(message.channel, "Wiimmfi Competitions: https://competitions.wiimmfi.de")
    elif message.content == "!invite":
        await client.send_message(message.channel, "Awww, you want to invite me to your server, here is the link https://discordapp.com/api/oauth2/authorize?client_id=443078805502951424&permissions=0&scope=bot%22")
    elif message.content == "!help":
        await client.send_message(message.channel, "https://pastebin.com/VUmnZLC0")
client.run ("NDQzMDc4ODA1NTAyOTUxNDI0.DdIJ9w.Cc93PL1i9_7g4vjTwbMtmrd1g30")
