import sys

import discord
import os
import discord.ext
import time
import SongQueue
from discord.ext import commands
import download
from mutagen.mp3 import MP3
import Wiki

client = commands.Bot(command_prefix=";")
q = SongQueue.SongQueue()


@client.command()
async def hi(ctx):
    await ctx.send("fuck you", tts=True)


@client.command()
async def play(ctx, url: str):

    song_path = download.download_song(url)

    mp3 = MP3(song_path)
    song_info = mp3.info
    playtime = int(song_info.length)

    song_entry = SongQueue.Entry(song_path, url, ctx.message.author, playtime)
    q.enqueue(song_entry)

    if q.has_one_song():

        try:
            voice_channel = ctx.message.author.voice.channel
            await voice_channel.connect()
        except:
            pass

        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

        song_entry = q.pop_song()
        sleep_time = song_entry.get_runtime() + 1
        song_path = song_entry.path
        try:
            voice.play(discord.FFmpegPCMAudio(song_path))
            print(sleep_time)

            if q.isEmpty():
                return
        except:
            print(sys.exc_info()[0], " ", sys.exc_info()[1])


@client.command()
async def leave(ctx):
    q.clear()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")


@client.command()
async def pause(ctx):
    print("attempting to pause")
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing.")


@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not paused.")


@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()


@client.command()
async def cum(ctx):
    voiceChannel = ctx.message.author.voice.channel

    try:
        await voiceChannel.connect()
    except:
        pass #probably should do something here to handle stuff

    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio("quin/quin.mp3"))

@client.command()
async def bruh(ctx):
    voiceChannel = ctx.message.author.voice.channel

    try:
        await voiceChannel.connect()
    except:
        pass  # probably should do something here to handle stuff

    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio("songs/Bruh - Sound Effect (HD).mp3"))

async def hollup():
    time.sleep(5)

@client.command()
async def wiki(ctx, url: str):
    wikiText = Wiki.Wiki(url)
    final_text = ""
    text_arr = [final_text]
    for text in wikiText.pTagsToText: ##this is to condense the messages so it sends 2 instead of 20
        text = text.strip()
        if text != '':
            current_concat = text_arr[len(text_arr) - 1]
            if len((current_concat + " " + text)) < 2000: #length 2000 and above is not allowed in tts
                text_arr[len(text_arr) - 1] += " " + text
            else:
                text_arr.append(text)

    for texts in text_arr:
        await ctx.send(texts, tts=True)




def contains_command(string):
    possible_command = string.split(' ')[0][1:]
    if possible_command in commands:
        return possible_command
    return 0


####################
#past this everything is kinda deprecated, it's only use is the complaint channel filerting
####################
# these are commands XD
commands = {
    "play",
    "pause",
    "stop",
    "leave",
    "cum",
    "shutup",
    "test",
    "bruh"
    "wiki"
}


def parse_author(message):
    return str(message.author).split("#")[0]

async def add_complaints(complaint):
    file = open("complaints.txt", "a")
    file.write("\n" + parse_author(complaint) + " said:  " + complaint.content)
    file.close()

@client.event
async def on_ready():
    print("Dheagurbot is logged in: as {0.user}. Welcome to the rice fields mfs".format(client))

@client.event
async def on_message(message):
    await client.process_commands(message)
    if message.author == client.user:
        # Matthew Quinn will blow up the white house
        return
    if str(message.channel) == "complaints":
        await message.delete()
        await message.channel.send(parse_author(message) + " has absolutely no complaints")
        await add_complaints(message)
        return
    if not message.content.startswith(";"):
        return
    command = contains_command(message.content)
    if command == 0:
        return
    elif command == "cum":
        await message.channel.send('matthew recycles cum')
        return


token_file = open("../token.txt", "r")
token = token_file.read()
token_file.close()
client.run(token)



