import discord
import time
from mail_discord import mmsend
from givevars import give_vars
from storinglog import save
from discord.ext import commands

token = os.getenv('token_feggie')
mclient = commands.Bot(command_prefix = '!')

@mclient.event
async def on_ready():
	print('ready')

@mclient.command(aliases = ['send'])
async def msend(ctx,*,str_given):
	gvars = give_vars(str_given)
	print(gvars)
	#******check this save thing
	print(save(gvars))
	#******************print

	while not(gvars[0] == 0):
		subject = 'form bot'
		print(gvars[0])
		gvars[0]-=1
		mmsend(gvars[1],subject,gvars[2])
		time.sleep(gvars[3])

mclient.run(token)
