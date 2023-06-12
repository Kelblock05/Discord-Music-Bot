
# Hype Haven Discord Bot
A simple and easy to use discord bot made in python for any discord server =D

## Authors

- [@Brosnank10101](https://github.com/Brosnank10101)

## How To Use My Discord Music Bot

My Music bot has pretty simple easy to use commands with the command prefix: b!

- b!play search term - example: b!play never gonna give you up<br />
  searches for music on youtube and plays the music without you needing to find a youtube link
  
- b!play youtube link - example: b!play https://www.youtube.com/watch?v=w1PXnF8fR9U<br />
  uses the youtube link provided and plays that song
  
- b!pause - pauses your music

- b!resume - resumes your music

- b!skip - skips the current playing song

- b!leave - Discord Bot leaves the voice call

- b!help_music - shows you a list of the music commands


## Requirements
- [The latest version of python](https://www.python.org/downloads/)<br />Python 3.10 is best however Python 3.8 or higher should work fine anything lower you will run into problems. 

- [A Discord Account](https://discord.com/register) and a discord bot 
  [application](https://discord.com/developers/docs/game-sdk/applications) is required.
  
- [FFmpeg](https://ffmpeg.org/) is a MUST requirement or else my discord music bot can't stream audio to discord.<br />    FFmpeg is a cross-platform solution to record, convert and stream audio and video.



## How to Setup a Discord Bot

![](https://i.imgur.com/evQaq2W.png)
- Go to the discord developer portal go to [applacations](https://discord.com/developers/applications) and either sign in with your discord account or register a new discord account. 

![](https://i.imgur.com/fJGJi0A.png)
- Create a new applacation, name your applacation and click confirm to the terms and conditions.

![](https://i.imgur.com/EByG0G3.png)
- Got to bot.

![](https://i.imgur.com/ih1wtnJ.png)
- create a new bot and click yes create a bot

![](https://i.imgur.com/PS82HSs.png)

- Reset the token and copy it and keep it somewhere safe.
  Using this token copy it and paste into the token variable
![](https://i.imgur.com/1AwhrGa.png)

![](https://i.imgur.com/glJqwY4.png)

- Under Bot enable all the gateway intents like I have here.

![](https://i.imgur.com/7AcPs3M.png)

- Go to OAuth2 and go to url editor select the scopes and bot perms that I have selected. Copy the URL and paste it into a new tab and add it to your discord server.<br /><br />If your confuesed on how to make a discord server here is a quick tutorial I found on youtube:<br />https://www.youtube.com/watch?v=VZUIvADKuu4&ab_channel=TechInsider

## How to install FFmpeg For Windows

- For windows users download the three exe files from [here](https://drive.google.com/drive/folders/1Az47gObzlVSqKD9L-UT0dSJbPFPo2fju?usp=sharing) put these files into a folder and name that folder FFmpeg then save the folder into your local disk that has windows on it and save the folder here C:\Users\YOUR_USER\ffmpeg

- Search up edit the system environment variables in windows search and open it up
![](https://i.imgur.com/8CWLrsU.png)

![](https://i.imgur.com/HsCGIqb.png)
- Go to advanced then environment variables

![](https://i.imgur.com/wuEGDLM.png)

- select path and edit

![](https://i.imgur.com/yt5ZLJw.png)

- Go new and the paste in the file path of the folder location C:Users\YOUR_USER\ffmpeg

## How to install FFmpeg on Linux

- Linux users you have things nice and simple compared windows all you need to do is paste the following command into your terminal: sudo apt install ffmpeg

## Download all the python modules in the requirements.txt file

 - There you go your discord bot is all setup you just need to run it enjoy.

 MAKE SURE YOU DOWNLOAD DISCORD.PY 1.7.3 NOT THE LATEST VERSION OF DISCORD.PY
