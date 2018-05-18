# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py
import discord

TOKEN = 'NDQ2NDQxNDc4NzI2ODc3MTg1.DeB0NA.DJ_Q_CuBTtYYD6kWA5CsHexlGB8'

client = discord.Client()

@client.event
async def on_message(message):
	# we do not want the bot to reply to itself
	if message.author == client.user:
		return	


	if message.content.lower().startswith('!hello'):
		msg = 'Hello {0.author.mention}'.format(message)
		await client.send_message(message.channel, msg)

	if message.content.lower().startswith("i'm "):
		msg = "Hello " + message.content[4:] + ", I'm Dad"
		await client.send_message(message.channel, msg)
	
	if "admin" in [y.name.lower() for y in message.author.roles]:
		if message.content == "!Kill":
			await client.send_message(message.channel, "Logging off...")
			await client.logout()


	

@client.event
async def on_ready():
	channel = [channel for channel in client.get_all_channels() if channel.name == 'dev-test'][0]
	await client.send_message(channel, "Systems Online...")
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

client.run(TOKEN)
