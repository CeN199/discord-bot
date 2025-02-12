import discord
from os import environ
from discord.ext import commands
from time import sleep
from keep_alive import keep_alive
keep_alive()

TOKEN = file.read(environ.get('token'))

intents = discord.Intents.default()

intents.members = True
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(name='кэпчут', aliases=[])
async def кэпчут(ctx):
    await ctx.send(f"Вы что-то хотели господин {ctx.author}?")
    
@bot.command(name='царство-теней')
async def ct(ctx):
    with open("images/цс.png", "rb") as f:
        await ctx.send("Вот ваша картинка:", file=discord.File(f))

def get_user(username: str):
    for guild in bot.guilds:
        user = discord.utils.find(lambda u: u.name == username, guild.members)
        if user:
            return user
        else:
        	return None

def check_roles(user: str):
    return [role.name for role in user.roles]

@bot.command(name="send")
async def send(ctx, username: str, message_count: str, message_sleep: str, *, message: str):    
    if username is None:
        await ctx.send("Пользователь не найден!")
        return
    user = get_user(username)
    if 'сооснователь olf empire' not in check_roles(ctx.author):
        await ctx.send("Недостачно прав!")
        return
    if not message_count.isdigit() and not message_sleep.isdigit():
        await ctx.send("Ошибка!")
        return
    for _ in range(int(message_count)):
        await user.send(message)
        sleep(int(message_sleep))
    await ctx.send(f"{ctx.author} твоё задание выполнено!")

@bot.command(name='гудим')
async def gudim(ctx):
    with open("images/гудим.png", "rb") as f:
        await ctx.send(file=discord.File(f))

@bot.command(name='sd')
async def shutdown(ctx):
    if 'сооснователь olf empire' not in check_roles(ctx.author):
        await ctx.send("Недостачно прав!")
        return
    await ctx.send("Завершаю работу")
    await bot.close()

bot.run(TOKEN)
