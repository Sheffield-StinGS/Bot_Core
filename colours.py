import discord

path = r"Bot_Core\Brand\colours.scss"

colours_file = open(path, "r")

colour_list = {}


for line in colours_file:
    if line[0] == "$":
        colour_start = line.find("(") + 1
        colour_end = line.find(")")
        full_colour_data = line[colour_start:colour_end]
        colour_name_end = line.find(":")
        colour_data = full_colour_data.split(",")
        colour_name = line[1:colour_name_end]
        colour = discord.Colour.from_rgb(int(colour_data[0]), int(colour_data[1]), int(colour_data[2]))
        colour_list.update({colour_name : colour})

colours_file.close()