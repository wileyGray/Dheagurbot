import discord
import os
import discord.ext
import time
import SongQueue
from discord.ext import commands
import download
from mutagen.mp3 import MP3


client = commands.Bot(command_prefix=";")
q = SongQueue.SongQueue

@client.command()
async def hi(ctx):
    await ctx.send("fuck you")


@client.command()
async def play(ctx, url: str):
    voiceChannel = ctx.message.author.voice.channel
    try:
        await voiceChannel.connect()
    finally:
        pass
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    file_name = download.download_song(url)
    print(file_name)
    voice.play(discord.FFmpegPCMAudio(file_name))


@client.command()
async def leave(ctx):
    try:
        os.remove("song.mp3")
    except:
        print("continuing")
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")


@client.command()
async def pause(ctx):
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
client.run(token);



