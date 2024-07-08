from .colours import colour_list #Imports the defined stings colours in python form
from .imports import *

#Loads the General config file and sets the core config variable
config_file = open("config.json")
config = json.load(config_file)
core_config = config["core_data"]

#Sets the permissions for the bot to be everything
intents = discord.Intents.all()

#String that specifies the time format, it has the day, month and year as a 2 digit number and the time as a 24 hour clock with hours minutes and seconds
time_format = '%d/%m/%y %H:%M:%S'

#Creates the bot object with a command prefix of either tagging it or the specified value from the JSON config file
#Also declares the intents and that the case doesn't matter when using commands
def createBot(name):
    global bot_config
    bot_config = config[name]
    DISCORD_TOKEN = bot_config["Token"]
    global bot
    bot = commands.Bot(command_prefix=commands.when_mentioned_or(bot_config["Command_Prefix"]), case_insensitive=True, intents=intents)
    bot.remove_command("help")
    return DISCORD_TOKEN

#Prints a message to the output with the time added
def printLog(message):
    time = datetime.now().strftime(time_format)
    print(f'[{time}] {message}')

#Prints a message to the output whenever a command is triggered
def logCommand(context):
    command = context.invoked_with
    author = context.author
    printLog(f'Command: \'{command}\' was triggered by \'{author}\'')

def main():
    @bot.event
    async def on_ready():
        printLog(f'{bot.user.name} has connected to Discord!') #Logs a message when the bot connects to discord
    
    @bot.command(name="Git", help="This provides a link to the Github Repository that contains all the code that makes me work")
    async def git(ctx):
        logCommand(ctx)
        git_link = bot_config["Git_Repo"]
        message = "Here's the Git Repo that contains all of my code. Feel free to take a look around and see how I work \n" + git_link
        await ctx.send(message)

    @bot.command(name="Help", help="Shows this help menu")
    async def help(ctx):
        logCommand(ctx)
        help_menu = discord.Embed(title=bot_config["Name"], url=bot_config["Git_Repo"], description=bot_config["Description"], colour=colour_list["stings_light_gold"])
        help_menu.set_thumbnail(url="https://ssago.org/img/clubs/logos/23.png")
        for command in bot.commands:
            help_menu.add_field(name=command.name, value=command.help, inline=False)
        help_menu.set_footer(text="Any Problems, please contact Oscar Lodge (@ShadowedLord05) or the StinGS Webmaster (webmaster@stings.ssago.org)")
        await ctx.send(embed=help_menu)