import discord, random, os
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Бот {bot.user} запущен!')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот который хочет помочь вас научить оберегать природу')

@bot.command()
async def bye(ctx):
    await ctx.send(f'Пока, пока!')

@bot.command()
async def help_sea(ctx):
    await ctx.send(f'https://unsdg.un.org/ru/latest/stories/tri-deystvennykh-sposoba-pomoch-sokhranit-nashi-okeany')

@bot.command()
async def help_lit(ctx):
    await ctx.send(f'https://ria.ru/20220829/utilizatsiya-1812880941.html')

@bot.command()
async def help_defor(ctx):
    await ctx.send(f'https://news.un.org/ru/story/2020/05/1378752')

@bot.command()
async def help1(ctx):
    await ctx.send(f'Наш бот будет пытаться помочь людям сохранить природу,'
                   f'Для того чтобы мир был без мусора, мы сами должны сделать шаг к этому,'
                   f'Вот для чего используется наш бот,'
                   f'Вот все команды которые у нас есть:'
                   f'Команда $help_sea - помощь по сохранению океанов, $help_lit - помощь по утилизациии мусора, $help_defor - вред вырубки деревьев, $hello - приветствие, $bye - прощание'
                   )

@bot.command()
async def mem_world(ctx):
    image_name = random.choice(os.listdir('mem_world'))
    with open(f'mem_world/{image_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


bot.run("ВАШ ТОКИН ТУТ")
