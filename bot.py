import sys

import discord
import os
import discord.ext
import time
import SongQueue
from discord.ext import commands
import download
from mutagen.mp3 import MP3


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

    if q.has_one_song() or q.is_paused():

        if q.is_paused():
            #some logic
            q.unpause()
        else:
            song_entry = q.pop_song()
            sleep_time\
                = song_entry.get_runtime() + 1
            song_path = song_entry.path

        try:
            voice_channel = ctx.message.author.voice.channel
            await voice_channel.connect()
        except:
            pass

        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        loopcounter = 0
        while not q.is_paused():
            loopcounter += 1
            print("looped " + str(loopcounter) + " times")
            try:
                voice.play(discord.FFmpegPCMAudio(song_path))
                time.sleep(1)
                if q.isEmpty():
                    return
                song_entry = q.pop_song()
                sleep_time = song_entry.runtime + 1
                song_path = song_entry.path
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

@client.command()
async def wiki(ctx, url: str):
    wikiText = Wiki(url)
    channel = client.get_channel(888263334258958336)
    for text in wikiText.pTagsToText:
        channel.send(text, tts=True)



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



