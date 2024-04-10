import discord
import os

TOKEN = MTIyNjM1NjUyNTI5NjI1OTE1NA.GrqA79.IWQv_n-4iXJdSEqeOGKMiXXgzqAPAk2Axtw9_k
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
        print(member.)
        return

    if message.content.startswith('$nexus load'):
        try:
            await message.channel.send(eventsDB[message.content[12:len(message.content)]])
        except KeyError:
            await message.channel.send("EventsDB entry not found.")

client.run(TOKEN)