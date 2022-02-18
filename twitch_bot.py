# bot.py
import os  # for importing env vars for the bot to use
from twitchio.ext import commands
import random
import sys

chatters = []
bot = commands.Bot(
    # set up the bot
    irc_token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']],
    api_token=os.environ['ACCESS_TOKEN'],
)


@bot.event
async def event_ready():
    """Called once when the bot goes online."""
    print(f"{os.environ['BOT_NICK']} is online!")
    ws = bot._ws  # this is only needed to send messages within event_ready
    await ws.send_privmsg(os.environ['CHANNEL'], f"/me Bot is launched!")


@bot.event
async def event_message(ctx):
    """Runs every time a message is sent in chat."""
    # make sure the bot ignores itself and the streamer
    global chatters
    if ctx.author.name.lower() == os.environ['BOT_NICK'].lower():
        return
    await bot.handle_commands(ctx)
    # await bot.pubsub_subscribe(os.environ['ACCESS_TOKEN'], 'channel-points-channel-v1.26083851')
    if 'привет' in ctx.content.lower():
        if str(ctx.author.name) not in chatters:
            await ctx.channel.send(random.choice(
                [f"Привет, @{ctx.author.name}! HeyGuys", f"Хэллоу биба @{ctx.author.name} HeyGuys",
                 f"Шалом @{ctx.author.name} HeyGuys"]))
            chatters.append(ctx.author.name)  # Adds new chatter to list of chatters
            print(chatters)
        else:
            await ctx.channel.send(f"Я с тобой уже здоровался @{ctx.author.name}! Kappa")
    elif ctx.content.lower() == "бб":
        await ctx.channel.send(f"Пока, @{ctx.author.name}! Keepo")
    elif "боты + в чат" in ctx.content.lower():
        await ctx.channel.send(f"- Kappa")
    elif ctx.content.lower() == "пока @ps1hbot":
        await ctx.channel.send(f"Пока-пока, мой сладкий @{ctx.author.name}! Keepo")
    elif "ахаха" in ctx.content.lower():
        await ctx.channel.send(
            random.choice([f"ааахаххахахахахахахах LUL LUL LUL", "xDDDDDDDDDD", "ору", "абсыкаюсь LUL"]))
    elif ctx.content.lower() == "+":
        await ctx.channel.send(f"+++++")
    elif "дота" in ctx.content.lower():
        await ctx.channel.send(f"Дота? кто сказал дота? дота это хороооошо, доту я уважаю Kappa")
    elif "бунд" in ctx.content.lower() or "бунт" in ctx.content.lower():
        await ctx.channel.send("""⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣠⣴⣶⣶⣿⣿⣿⣶⣶⣤⣄⡀⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢠⣾⣿⣯⢿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣦⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢠⣿⣿⣯⣽⣶⣶⣾⣕⣝⣧⣣⢫⡋⡿⠿⣇⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣾⣿⣿⣿⣿⢖⢬⣍⠻⣿⣿⡜⢧⠑⣴⣿⣿⣦⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣾⣿⣿⣿⣿⢖⢬⣍⠻⣿⣿⡜⢧⠑⣴⣿⣿⣦⠄⠄
⠄⠄⠄⠈⠻⣿⣿⠁⠄⣶⣿⣿⣿⣿⣿⣏⣚⣏⣴⢟⣟⠁⣰⠄⡇⣄⣽⣿⡄⠄
⠄⠄⠄⠄⠄⠈⢿⣶⡾⠿⢻⣿⣿⡛⠋⠁⣠⢏⣵⣿⣿⣿⣿⣷⣿⡘⡜⡿⠃⠄
⠄⠄⠄⠄⠄⠄⠄⠙⠿⣿⡿⣿⢻⡧⢀⡞⣡⣿⣿⣿⣿⣿⣿⣿⡿⣷⢁⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣾⡿⣼⣳⢿⣾⣿⣿⣿⣶⣶⣶⣶⡶⠶⣶⣍⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⢷⣿⣿⣿⡿⢋⠄⢶⠂⠶⠄⠄⠄⡤⣤⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⣿⠈⣿⣿⠟⠄⣰⡇⢀⡀⠄⠠⠄⠄⠄⠉⣤⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⣿⣿⣿⡇⠼⠷⢿⣇⢸⣷⡀⣾⡆⣾⣷⠠⡿⠆⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠸⣿⣽⣿⣷⣿⡿⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣶⣷⣦⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⠛⠛⣿⣿⣿⣶⣤⣤⣈⡉⠉⠉⠉⠉⠉⠉⠉⠁⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠻⣯⣭⣯⣭⣤⣶⣶⣶⣶⣦⣤⡈⠁⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠛⠛⠿⠛⠛⠁⠈⠉⠙⠛⠁⠄⠄⠄""")

    # elif "custom-reward-id=96153d86-a6ce-4eaf-90e5-67786d0d394f" in ctx.raw_data:
    #    print(ctx.raw_data)
    #    await ctx.channel.send("бунд удался")


# @bot.event
# async def event_raw_pubsub(data):
#   print(data)


@bot.command(name='заклипай')
async def clip(ctx):
    clip_url = await bot.create_clip(os.environ["ACCESS_TOKEN"], '26083851')
    await ctx.send(f"Заклипал Kappa {clip_url[0]['edit_url']}")


@bot.command(name='санитары')
async def clip(ctx):
    users = await bot.get_chatters('ps1honya')
    print(users[1])
    await ctx.channel.send(f'@{ctx.author.name} сдал санитарам бедного @{random.choice(users[1])} TPFufun TPFufun')


@bot.command(name='users')
async def get_id():
    users = await bot.get_users('xorus777')
    print(users)


@bot.command(name='kill')
async def kill():
    sys.exit(0)


if __name__ == "__main__":
    bot.run()