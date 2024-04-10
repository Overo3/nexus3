import discord
from pytube import YouTube
import os

TOKEN = os.environ["DISCORD_TOKEN"]
eventsDB = {"test":"dataTesting"}

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$nexus load'):
        try:
            await message.channel.send(eventsDB[message.content[12:len(message.content)]])
        except KeyError:
            await message.channel.send("EventsDB entry not found.")
    if message.content.startswith('$nexus mp3'):
        try:
            vidLink = message.content[11:len(message.content)]
            yt = YouTube(vidLink)
            stream = yt.streams.filter(only_audio=True).first()
            stream.download(filename=f'mp3files/"{yt.title}".mp3')
            with open(f'mp3files/"{yt.title}".mp3') as file:
                await message.channel.send(file=file)
client.run(TOKEN)
