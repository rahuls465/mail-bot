import discord
import random
import os

token = os.environ.get('token_feggie')
from discord.ext import commands

client = commands.Bot(command_prefix= '.')

@client.event
async def on_ready():
	print("bot is on_ready")

@client.command()
async def ping(ctx):
	await ctx.send(f'! {round(client.latency * 1000)}ms !')


ans = [ 'It is certain.',
'It is decidedly so.',
'Without a doubt.',
'Yes - definitely.',
'You may rely on it.',
'As I see it, yes.',
'Most likely.',
'Outlook good.',
'Yes.',
'Signs point to yes.',
'Reply hazy, try again.',
'Ask again later.',
'Better not tell you now.',
'Cannot predict now.',
'Concentrate and ask again.',
"Don't count on it.",
'My reply is no.',
'My sources say no.',
'Outlook not so good.',
'Very doubtful.']



@client.command(aliases=['8ball','test','question'])
async def _8ball(ctx, *, question):
	await ctx.send(f'question: {question}\nanswer: {random.choice(ans)}')



@client.command()
async def rules(ctx):
	await ctx.send('''```Rule #1: Be respectful toward other people. No harassing or personally attacking others.\nRule #2: No text spamming in the text channels, no mic spamming in the voice channels.
Rule #3: No pornographic or disturbing content.\nRule #4: No meme/joke songs in the #project-chanel text channel, keep them to the #memes-and-garbage channel. The #music channel is for real discussion and sharing of music that you like.\nRule #5: IMPORTANT Don't be asshole```''')
client.run(token)