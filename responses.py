#Author: spasemax0
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

    if message == '$translate':
        return str(result = translator.translate(input))

    if p_message == '!buy puffer fish':
        return '`no u broke`'
    if p_message == '!8ball':
        return 'magic_eightball'
