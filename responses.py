#Author: spasemax0
#this is a responses page used to call the bot and its events
import random
import randfacts
import googletrans
from discord.app_commands import translator
from googletrans import Translator


def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == '$funfact':
        return str(randfacts.get_fact())

    if message == '$roll':
        return str(random.randint(1, 6))

    if p_message == '!buy puffer fish':
        return '`no you have no money`'
    
    if p_message == '!8ball':
        return 'magic_eightball'
