import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Бот {bot.user} запущен!')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def mem(ctx):
    image_name = random.choice(os.listdir('images'))
    with open(f'images/{image_name}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

@bot.command()
async def an_mem(ctx):
    image_name = random.choice(os.listdir('images_animals'))
    with open(f'images_animals/{image_name}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

@bot.command()
async def bye(ctx):
    await ctx.send(f'Пока! Это был бот {bot.user}!')


bot.run('ТУТ ТОКИН ОТ БОТА')
