from .colours import colour_list #Imports the defined stings colours in python form
from .imports import * #Imports all of the required libraries

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
    global bot_config #Sets the variable to be accessable from anywhere in the code
    bot_config = config[name] #Loads the specific block of config that is unique to the named bot
    DISCORD_TOKEN = bot_config["Token"] #Sets the discord token variable to be the one specific to the bot
    command_prefix = commands.when_mentioned_or(bot_config["Command_Prefix"]) #Sets the command prefix to be either when the bot is tagged or the specific value from the config file
    global bot # Makes the bot object accesable from anywhere in the code
    bot = commands.Bot(command_prefix=command_prefix, case_insensitive=True, intents=intents) #Creates the bot using the previously declared intents and command prefix. Also sets it to not care about case for commands
    bot.remove_command("help") #Removes the inbuilt help command to be replaced with our custom one
    return DISCORD_TOKEN

#Prints a message to the output with the time added
def printLog(message):
    time = datetime.now().strftime(time_format) #Creates the time stamp in the specified format 
    print(f'[{time}] {message}') #Prints the message to the log with the time stamp added

#Prints a message to the output whenever a command is triggered
def logCommand(context):
    command = context.invoked_with #Gets the command that was used
    author = context.author #Gets the person who used the command
    printLog(f'Command: \'{command}\' was triggered by \'{author}\'') #Sends the message to the logging function to format and then print

def main():
    @bot.event
    async def on_ready():
        printLog(f'{bot.user.name} has connected to Discord!') #Logs a message when the bot connects to discord
    
    @bot.command(name="Git", help="This provides a link to the Github Repository that contains all the code that makes me work")
    async def git(ctx):
        logCommand(ctx) #Logs that the command has been triggered
        git_link = bot_config["Git_Repo"] #Loads the link from the config file data
        message = "Here's the Git Repo that contains all of my code. Feel free to take a look around and see how I work \n" + git_link
        await ctx.send(message) #Sends a message that contains the git link to discord

    @bot.command(name="Help", help="Shows this help menu")
    async def help(ctx):
        logCommand(ctx) #Logs that the command has been triggered
        help_menu = discord.Embed(title=bot_config["Name"], url=bot_config["Git_Repo"], description=bot_config["Description"], colour=colour_list["stings_light_gold"]) #Creates the help menu object and loads the data from the config file and the colour from the list
        help_menu.set_thumbnail(url="https://ssago.org/img/clubs/logos/23.png") #Adds the club logo from the ssago website to the help menu
        for command in bot.commands:
            help_menu.add_field(name=command.name, value=command.help, inline=False) #Adds each command to the help menu with a description of what it does
        help_menu.set_footer(text="Any Problems, please contact Oscar Lodge (@ShadowedLord05) or the StinGS Webmaster (webmaster@stings.ssago.org)") #Adds a message to the bottom of the menu
        await ctx.send(embed=help_menu)