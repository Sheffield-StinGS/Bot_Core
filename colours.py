from .imports import discord

path = r"Bot_Core\Brand\colours.scss" #Path where the colour codes are located

colours_file = open(path, "r") #Loads the colout file in read only mode

colour_list = {}

#Loads the colours from the general branding file and sets them to Discord readable values
for line in colours_file:
    if line[0] == "$": #Checks that the line is a colour value
        colour_start = line.find("(") + 1 #Finds the position where the colour information starts
        colour_end = line.find(")") #Finds the position where the colour value ends
        full_colour_data = line[colour_start:colour_end] #Gets the RGBA values from the file as a single string
        colour_data = full_colour_data.split(",") #Splits the RGBA values into individual values
        colour_name_end = line.find(":") #Finds where the colour name ends
        colour_name = line[1:colour_name_end] #Gets the substring of the colour name
        colour = discord.Colour.from_rgb(int(colour_data[0]), int(colour_data[1]), int(colour_data[2])) #Creates the colour as a discord object from the data, ignores the alpha value as it is not supported
        colour_list.update({colour_name : colour}) #Adds the Colour object to the dictionary with the name as the key

colours_file.close() #Closes the file