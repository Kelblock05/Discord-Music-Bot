#the main file the starts the Music file, authorizes accsess to the discord bot, starts the discord bot up and sets up the cogs
import discord
from discord.ext import commands
import Music
cogs = [Music]
#authorization key
token = '***REPLACE WITH YOUR OWN DISCORD BOT TOKEN'

#the command prefix the users use to use the music commands
client = commands.Bot(command_prefix=['b!','B!'], intents = discord.Intents.all(), case_insensitive=True)
#setting up the cogs
async def main():
  for egg in range(len(cogs)):
    await cogs[egg].setup(client)

#looping the main async function
client.loop.create_task(main())

#starting up the discord bot
client.run(token)
