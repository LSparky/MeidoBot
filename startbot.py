import discord
import asyncio
import json
from discord.ext import commands

startup_extensions = [
"cogs.events",
"cogs.no_erp",
"cogs.clever",
"cogs.reddit"
]

client = discord.Client()

with open('token.json') as token_file:
	data = json.load(token_file)
token = data['token']


client = commands.Bot(command_prefix=('$','maid.'),
					pm_help=True,
					case_insensitive=True,
					owner_id=115895386606010376)

client.remove_command('help')
client.load_extension("jishaku")

async def background_loop():
	while True:
		await client.wait_until_ready()
		online = []
		x = client.get_all_members()
		for member in x:
			if member.status == discord.Status.online:
				online.append(member)
			elif member.status == discord.Status.idle:
				online.append(member)
			elif member.status == discord.Status.dnd:
				online.append(member)
		onlinemaid = "{0} maids!".format(str(len(set(online)) -1))

		await client.change_presence(activity=discord.Activity(name=onlinemaid, type=3))
		print("updated maid count, now " + str(len(set(online))))
		await asyncio.sleep(120)

if __name__ == "__main__":
	for extension in startup_extensions:
		try:
			client.load_extension(extension)
		except Exception as e:
			exc = '{}: {}'.format(type(e).__name__, e)
			print('Failed to load extension {}\n{}'.format(extension, exc))

client.loop.create_task(background_loop())
client.run(token, bot=True, reconnect=True)
