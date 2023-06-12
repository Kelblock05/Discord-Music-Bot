#importing all required modules and extention modules
from http import client
import discord
from discord.ext import commands
import urllib.request
import re
from pytube import YouTube
import os
import threading
import time

#defining global variables
global if_skipped
global paused
paused = False
if_skipped = False

#checking if there is a previous song still in the file directory and deletes it if one is found
if os.path.isfile('vibes.mp3'):
  os.remove('vibes.mp3')

#Checking if there is a previous MP4 file that may have not been converted into a MP3 and deletes it if one is found
MP4_to_delete = os.listdir()
for item in MP4_to_delete:
    if item.endswith(".mp4"):
        os.remove(os.path.join(item))

#function that gets run as a thread that continuously checks if the current song file (vibes.mp3) can be deleted and when it can the mp3 file gets deleted and breaks out of the while loop and the thread dies.
def auto_delete():
  while True:
    try:
      if if_skipped == True:
        break
      if paused == True:
        pass
      else:
        if os.path.isfile('vibes.mp3'):
          os.remove('vibes.mp3')
        else:
          break
    except:
      pass

#The main class and cog that allows me to organize my collection of commands and objects into one place
class Music(commands.Cog):
  async def main(self,client):
    self.client = client

  #Removing discords default help command so I can create my own
  client = commands.Bot(command_prefix=['b!','B!'], case_insensitive=True)
  client.remove_command('help')
  
  #allows the user to pause their music at any given time
  @commands.command()
  async def pause(self,ctx):
    global paused
    if paused == True:
      embed = discord.Embed(title = f"Your vibes are already paused no need to pause them twice!?",color = discord.Colour.red())
      await ctx.send(embed = embed)
    else:
      if os.path.isfile('vibes.mp3'):
        #the global variable paused lets other functions like auto_delete know the music has been paused so the users music won't get deleted when their music is paused
        paused = True
        vc1 = ctx.voice_client
        vc1.pause()
        #sends an embed message to discord imforming the user about what has happened
        embed = discord.Embed(title = f"Your vibes Have Been Paused ⏸️",color = discord.Colour.blurple())
        await ctx.send(embed = embed)
      else:
        #making sure an error doesn't happen if the user pauses music when there is no music to be paused
        embed = discord.Embed(title = f"There are no songs to be paused",color = discord.Colour.red())
        await ctx.send(embed = embed)



  @commands.command()
  #allows the user to resume their music after pausing their tunes
  async def resume(self,ctx):
    #stops errors from happening if music is resumed when music is playing already
    if ctx.voice_client.is_playing():
      embed = discord.Embed(title = f"You can't resume music when it's already playing",color = discord.Colour.red())
      await ctx.send(embed = embed)
    else:
      if os.path.isfile('vibes.mp3'):
        global paused
        paused = False
        vc1 = ctx.voice_client
        vc1.resume()
        embed = discord.Embed(title = f"Your vibes Have Been Resumed ⏯️",color = discord.Colour.blurple())
        await ctx.send(embed = embed)
      else:
        embed = discord.Embed(title = f"There are no songs to be resumed",color = discord.Colour.red())
        await ctx.send(embed = embed)

  @commands.command()
  #allows the user to disconnect the bot from their voice call
  async def leave(self,ctx):
    vc1 = ctx.voice_client
    vc1.pause()
    await ctx.voice_client.disconnect()
    embed = discord.Embed(title = f"Cyaaaaa",color = discord.Colour.blurple())
    await ctx.send(embed = embed)

  @commands.command()
  
  async def skip(self,ctx):
    #allows the user to skip the current playing song
    if os.path.isfile('vibes.mp3'):
      #gets the current songs title from youtube so it can be used in the embed message
      yt_skip = YouTube(current_url)
      name_skip = yt_skip.title
      vc1 = ctx.voice_client
      vc1.stop()
      embed = discord.Embed(title = f"Skipped {name_skip} ⏭️",color = discord.Colour.blurple())
      await ctx.send(embed = embed)
      global if_skipped
      if_skipped = True
      if os.path.isfile('vibes.mp3'):
        os.remove('vibes.mp3')
    else:
      #avoids errors by checking if there is a song to be skipped
      embed = discord.Embed(title = f"You can't skip a vibe if there are no vibes to skip",color = discord.Colour.red())
      await ctx.send(embed = embed)

  
  @commands.command()
  #the music help command allows confuesed users to know what to do
  async def help_music(self,ctx):
    embed = discord.Embed(title = f"Music Command Help",description = f"- Play Commands:\nㅤㅤb!play[youtube_link]\n\nㅤor\n\nㅤㅤb!play[search keywords]\n\n- Music Control Commands:\nㅤㅤb!pause , b!resume , b!skip,\nㅤㅤb!leave",color = discord.Colour.blurple())
    await ctx.send(embed = embed)

  @commands.command()
  #The play command allows users to search youtube for songs (while allowing the video to still gaining views/revenue) and then downloading them and playing them though discord
  async def play(self,ctx):
    #global variable for the current playing songs url
    global current_url

    #checks if the user is connect to a voice channel and joins it if the user is found in one if not asks the user to join a voice call
    if ctx.author.voice is None:
      embed = discord.Embed(title = f"Your currently not in a vc please join a vc and try again....",color = discord.Colour.red())
      await ctx.send(embed = embed)
    else:
      vc = ctx.author.voice.channel
      if ctx.voice_client is None:
        await vc.connect()
      else:
        await ctx.voice_client.move_to(vc)
      

      #stops errors from happening if the user trys to play two songs at once
      if os.path.isfile('vibes.mp3'):
        embed = discord.Embed(title = f"There seems to a song playing.\n\nEither skip the current song or wait until the current song has finished",color = discord.Colour.red())
        await ctx.send(embed = embed)

      else:
        embed = discord.Embed(title = f"For Music Command help use: b!help_music\n\nSearching and Downloading your vibes give me a bit...",color = discord.Colour.blurple())
        await ctx.send(embed = embed)
        yt_link = str('https://www.youtube.com/watch?v=')
        if_link_found = False
        bypass = True
        #gets the user message and filters it for search keywords or filters a youtube link if one is found in the message

        search_keyword = str(ctx.message.content)
        if yt_link in search_keyword:
          url = (re.search("(?P<url>https?://[^\s]+)", search_keyword).group("url"))
          if_link_found = True
          #if a youtube link is found in the user message it skips finding it on youtube and downloads the video

        search_keyword = str(search_keyword).lower()
        search_keyword = search_keyword.replace("b!play", "")
        if yt_link not in search_keyword:
          search_keyword = search_keyword.replace(" ", "_")
          #using the search keyword in the users message, it searches youtube and gets the url of the most relevant video from the search keyword
          youtube_url = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
          #youtube_ids is a list of all found youtube video ids found under the users search word
          youtube_ids = re.findall(r"watch\?v=(\S{11})", youtube_url.read().decode())
          #[0] selects the item in the list which will be the most relevant found youtube video
          url = ("https://www.youtube.com/watch?v=" + youtube_ids[0])
      if ctx.voice_client.is_playing():
        pass
      else:
        #using the gathered url it downloads the video from youtube and converts it into a MP3 file (THE YOUTUBE VIDEO STILL GAINS VIEWS/REVENUE THE DOWNLOADED FILE IS DELETED AFTER IT'S SINGLE USE)
        yt = YouTube(url)
        video_title = yt.title
        #checking if the video is within the limits of one hour to keep file sizes down and so the bot doesn't timeout while converting the song MP4 file to an MP4 file
        video_length = yt.length
        video_length = int(video_length)
        if video_length > 3600:
          if if_link_found == True:
            embed = discord.Embed(title = f"WOAH!!! Calm Down... Those vibes are longer than an hour.\n\nHow about find some vibes that are less than an hour long.",color = discord.Colour.red())
            await ctx.send(embed = embed)
            bypass = False
          else:
            #if the video that the bot has found though the users search term is longer than an hour it will cycle though to find a song that's under an hour long
            embed = discord.Embed(title = f"The found Song is longer than one hour long.\n\nCycling though found Youtube Videos to find a song under an hour",color = discord.Colour.red())
            await ctx.send(embed = embed)
            while True:
              url = ("https://www.youtube.com/watch?v=" + youtube_ids.pop())
              yt = YouTube(url)
              video_length = yt.length
              video_length = int(video_length)
              if video_length > 3600:
                pass
              else:
                yt = YouTube(url)
                bypass = True
                break
        if bypass == True:
          video = yt.streams.filter(only_audio=True).first()
          output_file = video.download()
          base, ext = os.path.splitext(output_file)
          new_file = base + '.mp3'
          os.rename(output_file, new_file)
          play_file = new_file

          #*************** CHANGE F:\Hyped Haven\ TO YOUR FILE DIRECTORY**** (REMEMBER TO ADD ANOTHER BACKSLASH TO USE A SINGLE BACKSLASH IN THE STRING)***************
          play_file = play_file.replace("F:\Hyped Haven\\", "")
          os.rename(play_file, 'vibes.mp3')

          #plays the MP3 though discord and double checks that the bot is still in the voice channel to avoid errors
          vc = ctx.voice_client
          vc_join = ctx.author.voice.channel
          if ctx.voice_client is None:
            await vc.connect()
          else:
            await ctx.voice_client.move_to(vc_join)
          vc.play(await discord.FFmpegOpusAudio.from_probe('vibes.mp3'))
          
          #if a youtube link is found in the orginal user message it will send the video title instead of the embed url message so the users discord channel is tidy
          if if_link_found == True:
            embed = discord.Embed(title = f"Now Playing Your Requested Vibes:\n{video_title}",color = discord.Colour.blurple())
            await ctx.send(embed = embed)
            if_link_found = False

          elif if_link_found == False:
            embed = discord.Embed(title = f"Now Playing Your Requested Vibes:",color = discord.Colour.blurple())
            await ctx.send(embed = embed)
            await ctx.send(f'{url}')
          url = str(url)
          current_url = url

          #creating and starting up the auto_delete thread so the song to be deleted straight after it has finished. This happens for two reasons: maintaining low storage use, and so the content/music doesn't extend it's allowed usage period which is once since the youtube video only gains REVENUE/views when downloaded the first time therefore the music can not be used multiple times and must be deleted.
          auto_del = threading.Thread(target=auto_delete)
          auto_del.start()

#setting up the main cog
async def setup(client):
  client.add_cog(Music(client))