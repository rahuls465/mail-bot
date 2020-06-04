import discord
import random
import os
import time
from mail_discord import mmsend
from givevars import give_vars
from givevars import give_vars2
from storinglog import save
token = os.environ.get('token_feggie')

from discord.ext import commands

client = commands.Bot(command_prefix= '!')

@client.event
async def on_ready():
	print("bot is on_ready")

@client.command()
async def ping(ctx):
	await ctx.send(f'! {round(client.latency * 1000)}ms !')



@client.command(aliases = ['send'])
async def msend(ctx,*,str_given):
	gvars = give_vars(str_given)
	print(gvars)

	while not(gvars[0] == 0):
		subject = 'form bot'
		print(gvars[0])
		gvars[0]-=1
		mmsend(gvars[1],subject,gvars[2])
		time.sleep(gvars[3])

@client.command()
async def mail (ctx,*,str_given):
	gvars = give_vars2(str_given)
	subject = 'from bot'
	mmsend(gvars[0],subject,gvars[1])

client.run(token)