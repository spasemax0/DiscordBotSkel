#Author: spasemax0
#this is the main bot file where you deal with client events and commands, customize as needed
import random
import discord
import googletrans
from discord.ext import commands
from discord.ext.commands import bot
from googletrans import Translator

import responses


async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = 'DISCORD BOT TOKEN GOES HERE'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    bot = commands.Bot(command_prefix='$', intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is runnin')

    @bot.command(aliases=["8ball", "eightball", "eight ball", "8 ball"])
    async def magic_eightball(ctx, *, question):
        with open("pissBot/responses.py", "r") as f:
            random_responses = f.readlines()
            response = random.choice(random_responses)

        await ctx.send(response)


    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)


    client.run(TOKEN)
