from discord.ext import commands

bot = commands.Bot(command_prefix='?')

bot.lava_nodes = [
    {
        'host': 'lava.link',
        'port': 80,
        'rest_uri': f'http://lava.link:80',
        'identifier': 'MAIN',
        'password': 'anything',
        'region': 'malaysia'
    }
]

@bot.event
async def on_ready():
    print('The bot is ready t play music! Have fun!')
    bot.load_extension('dismusic')
    bot.load_extension('dch')
    


bot.run("token")