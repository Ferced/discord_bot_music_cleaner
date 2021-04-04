# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


commands_not_accepted = ['-p','-skip','-stop','-pause','-leave','-n','-next',';;p',';;skip',';;stop',';;pause',';;leave',';;next',';;n','/p','/skip','/stop','/pause','/leave','/n','/next']
authors_not_accepted = ["Seba Dictador#5132","FredBoat♪♪#7284","Groovy#7254","Rythm#3722"]

def get_channel_by_name(name,server):
	for server in client.guilds:
		for text_channel in server.text_channels:
			if text_channel.name == "general":
					channel = text_channel
	return channel
def custom_message(author):
    return {
        'burguer': 'que boludo que sos burger ya te lo explicamos mil veces, los comandos de musica van en #musically',
        'Eriq': 'Erik dolape le re puta que te pario, la musica va en #musically',
        'Sebame#9960': 'Que haceeeeeeeeeeeeeees king sebaking sebarey',
        'frxnk#4504':'Fran estas re duracell, la musica va en el canal #musica',
        'augustijas#2996':'Agustito te voy a buscar a tu casa con un ak47 si seguis poniendo musica en #general',
        'Joaco#4913':'Bestia total',
    }.get(str(author),str(author) + ' te borre el mensaje, los comandos de musica van en el canal #musically la re concha bien de tu hermana')

@client.event
async def on_ready():
	
	channel = get_channel_by_name("general",client)
	print(f'{client.user.name} se acaba de prender, se acabo la joda.')
	def check_msg(msg):
		if len(msg.content) > 1 and any(msg.content.startswith(item) for item in commands_not_accepted):
			return True
		if str(msg.author)  in authors_not_accepted:
			return True
		return False
	await channel.send('Borrando mensajes al pedo... ',delete_after=5)
	deleted = await channel.purge(limit=100, check=check_msg)
@client.event
async def on_message(message):
	channel = message.channel

	if any(message.content.startswith(item) for item in commands_not_accepted) and str(channel) == "general":

		await channel.send(custom_message(message.author),delete_after=60)
		await message.delete()
		msg = await client.wait_for('message')

client.run(TOKEN)