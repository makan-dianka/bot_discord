from discord.ext import commands
import discord
import config
import time
import os

TOKEN = os.environ.get('discord_token')

class MyClient(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="$", intents=discord.Intents.all())

    async def on_ready(self):
        print('\nTout est prêt !')
        print(f'Je m\'appelle [{self.user.name}] et mon id est [{self.user.id}]')


    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        if message.content in ['hello', 'yo', 'ça va', 'salut', 'cv']:
            await message.channel.send('Hello {0.author.mention} quoi de neuf ?'.format(message))  
            print(message.content) 
            time.sleep(5) 
            await message.channel.send('Je suis dans ma version Beta. Je ne pourrais peut être pas répondre à toutes tes questions pour le moment.'.format(message)) 
            time.sleep(3) 
            await message.channel.send('À très bientôt !'.format(message))        
       
client = MyClient()
client.run(TOKEN)