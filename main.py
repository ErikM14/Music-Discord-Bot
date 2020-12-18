#Returns top search on YouTube for the provided song name
#For best result, make sure to spell correctly, add lyrics to end of title

import discord
import os
from youtubesearchpython import SearchVideos


client = discord.Client()

@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$go'):
    userInput = message.content[3:]
    videosSearch = SearchVideos(userInput, offset = 1, mode = "dict", max_results=1)
    listy = videosSearch.result()['search_result']
    diction = listy[0]
    link = diction["link"]
    await message.channel.send(link)

client.run(os.getenv('TOKEN'))