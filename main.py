#Returns top search on YouTube for the provided song name
#For best result, make sure to spell correctly, add lyrics to end of title
#pip install youtube-search-python

import discord
import os
from youtubesearchpython import SearchVideos
from replit import db
import random
from keep_up import keep_up


client = discord.Client()

def add_song(song_name):
  if "randomsongs" in db.keys():
    randomsongs = db["randomsongs"]
    randomsongs.append(song_name)
    db["randomsongs"] = randomsongs
  else:
    db["randomsongs"] = [song_name]

def delete_song(index):
  randomsongs = db["randomsongs"]
  if len(randomsongs) > index:
    del randomsongs[index]
    db["randomsongs"] = randomsongs

@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  #convert from dict to list to dict
  if message.content.startswith('$go'):
    userInput = message.content[3:]
    videosSearch = SearchVideos(userInput, offset = 1, mode = "dict", max_results=1)
    listy = videosSearch.result()['search_result']
    diction = listy[0]
    link = diction["link"]
    await message.channel.send(link)

  if message.content.startswith('$random'):
    await message.channel.send(random.choice(db["randomsongs"]))
    
  
  if message.content.startswith('$add'):
    userInput = message.content[4:]
    videosSearch = SearchVideos(userInput, offset = 1, mode = "dict", max_results=1)
    listy = videosSearch.result()['search_result']
    diction = listy[0]
    link = diction["link"]
    add_song(link)
    await message.channel.send("Added song to random list.")

  if message.content.startswith('$delete'):
    userInput = message.content[7:]
    randomsongs = []
    if "randomsongs" in db.keys():
      index = int(userInput)
      delete_song(index)
      randomsongs = db["randomsongs"]

keep_up()
client.run(os.getenv('TOKEN'))