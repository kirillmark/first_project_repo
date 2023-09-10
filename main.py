import discord
from discord.ext import commands
from flip_a_coin import random_coin
from random_smile import rand_smile
from toss import toss_dice

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def bye(ctx):
    await ctx.send(f'Пока! Это был бот {bot.user}!')

@bot.command()
async def flip_a_coin(ctx):
    await ctx.send(random_coin())
  
@bot.command()
async def toss_the_dice(ctx):
    await ctx.send(toss_dice())

@bot.command()
async def random_smile(ctx):
    await ctx.send(rand_smile())

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run("ВАШ ТОКИН")

        
