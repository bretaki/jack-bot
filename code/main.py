# author: Bret Mathyer
# lang: EN
# for: discord bot

#imports
import discord
import os
import requests
import random
import string


#main
client = discord.Client()
categories = ['jack', 'game', 'currency', 'autoreply']
command_list = {
	'jack': ['picknum', 'flip', 'math'],
	'game': [],
	'currency': [],
	'autoreply': []
}


@client.event
async def on_ready():
  print('Logged in as {bot.user}'.format(client))

	
# commands
@client.event
async def on_message(message):
	# variables
  msg = message.content
  def msgsend(reply):
    await message.channel.send(reply)
    
  # no-reply self
  if message.author == client.user:
    return
  
  # sends how-to on jackbot
  if msg.startswith('/help'):
		
    # sends command list help
    if (msg == '/help') | (msg == '/help ')
      msgsend("Please specify what category you need help with:" +'\n' + categories)
     else:
      index = msg.split(' ')
			if (lower(index[1]) == 'jack') | (lower(index[1]) == 'jackbot')
				msgsend("Here is help with general commands: ")
			if (lower(index[1]) == 'game') | (lower(index[1]) == 'games')
				msgsend("Here is help with game commands: ")
			if (lower(index[1]) == 'cur') | (lower(index[1]) == 'currency' | (lower(index[1]) == 'economy')
				msgsend("Here is help with currency commands: ")
			if (lower(index[1]) == 'autoreply') | (lower(index[1]) == 'auto')
				msgsend("Here is help with autoreply commands: ")
	
	# general commands
	if msg.startswith('/jack'):
		index = msg.split(' ')
		
		# pick a random number between x and y
		if index[1] == 'picknum':
			x = int(index[2])
			y = int(index[3])
			msgsend(random.randint(x, y) + ' was picked!')
		
		# flipping a coin
		if index[1] == 'flip':
			coin = random.randint(0, 2)
			if coin == 1:
					msgsend('The coin landed on Heads')
			else:
					msgsend('The coin landed on Tails')
		
		# solve a simple math problem, maintains system health
		if index[1] == 'math':
			equation = index[2]
			if not set(equation).intersection(string.ascii_letters + '{}[]_;\n'):
				msgsend("The answer is: ", eval(equation))
			else:
				msgsend("illegal character(s)")
				return None
	
	# autoreply
	if any(words in msg for words in autoreply_list):
		word = lower(word)
		if (word == "will smith") | (word == "willsmith"):
			msgsend('Keep my name, out of your *bleep* mouth!')
		if word == "":
			msgsend('')


# link token
client.run(os.getenv('TOKEN'))
