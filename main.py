'''
Developer: Rajjya Rohan Paudyal
File Name: main.py
Date: 5/20/2021
Description: 
    This file contains main code for True Viking Discord BOT
    Additional file keep_alive.py has been used as a support to this file         
    This file is cleaned and cleared for github push
'''

# Importing Discord Package
import discord

# Importing Additional Package
import time

# Importing os deletion
import os

# Discord functionality message
from discord import message

# time() used in the program 

# Date time library 
import datetime

from discord.gateway import DiscordClientWebSocketResponse

# Client
client = discord.Client()

# Global Variables 
global allow_checkin
allow_checkin = False

# Global List 
authorList = []

# Importing keep_alive for ping
from keep_alive import keep_alive


@client.event # assumes an event
async def on_ready(): # function runs after the BOT's online
                      # async when ever you can run this function
    # Instructions

    # general_channel = client.get_channel(836241294288093259) # finds the channel
    # await general_channel.send("Let's go get some!") # sends the message 

    print("Logged in as")
    print(client.user.id)
    print(client.user.name)
    print("-----")

# # # # # # # # # # # # # # # # # # # # # # # # # 
@client.event
async def on_message(message):
  # When somesort of message is entered on the channel
  general_channel = client.get_channel(836241294288093259) # finds the channel
  if(message.content == "Noikay!"):
    general_channel = client.get_channel(836241294288093259) # finds the channel
    await general_channel.send("Good Jobes :sweat_smile: !") # sends the message 

  elif((message.content == "!startcheckin") & (message.channel.id==attendance_channel_ID)):
        # Function call 
        await Allow_checkin(message) 

  elif((message.content == "!stopcheckin") & (message.channel.id==attendance_channel_ID)):
        # Function call 
        await End_checkin()

  elif(message.content == "!version"):
        # Sending Version Information 
        await Version_Info(message)

  elif(message.content == "go vikings"):
        # Easter Egg 1 
        general_channel = client.get_channel(836241294288093259) # finds the channel
        await general_channel.send("https://media.giphy.com/media/SEEeoQclOShsA/giphy.gif")


        

    # # # # # # # # # # # # # # # # # # # # # # # # #   

    # Sending DM's to user 
  general_channel_ID = 836241294288093259
  if((message.content.startswith("!checkin")) & (message.channel.id==general_channel_ID)):
      # Checking if it allow_checkin is on?
      if(allow_checkin):

          # Adding Authors to List 
          await Record_Author(message)

      else:
          # Checkin Not Allowed 
          await Send_error_dm_to_members(message)

  # Displaying Status 
  if((message.content == "!status") & (message.channel.id==attendance_channel_ID)):
      # Sending the Checkin Status
      attendance_channel = client.get_channel(attendance_channel_ID)
      if(allow_checkin):
          myEmbed = discord.Embed(title="Allow_Checkin is Online :white_check_mark: ", description="BOT is ready to take attendance", color=0xffff00)
          myEmbed.add_field(name="Stop Checkin Command", value="use the command `!stopcheckin` to stop checkin and you will recieve an attendance list", inline=False)
          myEmbed.set_footer(text=("Command by → " + message.author.name))
        
      else: 
          # When offline 
          myEmbed = discord.Embed(title="Status", description="Allow_Checkin is Offline :x: BOT is not ready to take attendance", color=0xff0000)
          myEmbed.add_field(name="Start Checkin Command", value="use the command `!startcheckin` to start checkin and other members will be able to check in", inline=False)           
          myEmbed.set_footer(text=("Command by → " + message.author.name))
            
      # Sending Embeded Message 
      await attendance_channel.send(embed=myEmbed)

  
        
# HELPER FUNCTIONS # 
# Send_dm_to_members
# Pre-Condition: 1) The attendance master should change `allow_checkin = true`
#                2) Author should `!checkin` on the channel #general
#                3) The message should start with `!checkin` 
# Post-Condition: 1) Records the time author was checked 
#                 2) Sends a confirmation message to the author
async def Send_dm_to_members(message, duplication):
    # Checking if the master has allowed authors to check in 
    dm_author = message.author # finds the author 
    if(duplication == False):
        await dm_author.send(":clap: You are checked in! :raised_hands: ")
        print("DM send to Author")

    else:
        # When Duplication Detected
        await dm_author.send("Your already checked in! ")
        # Sending Saun the sheep thumps up GIF!
        await dm_author.send("https://tenor.com/view/thumbs-up-double-thumbs-up-like-agreed-yup-gif-11663223")


    # deleting the command
    await message.channel.purge(limit=1) # only 1 message


# Send_error_dm_to_members
# Pre-Condition: 1) None 
# Post-Condition: 1) Returs error message to author
async def Send_error_dm_to_members(message):
    # Sending Error Message to Author
    dm_author = message.author # finds the author
    await dm_author.send(":hand_splayed: Checkin's not allowed! Wait for Attendance Masters! :timer: ") 


# Allow_checkin
# Pre-Condition: 1) The admins use the command `startcheckin` 
#                2) `allow_checkin` value should be false else it will return an error
# Post-Condition: 1) Allows authors to check in using the `!checkin`
#                 2) Once the admins end checkin session, BOT will send the .txt file with all details 
attendance_channel_ID = 846416711141425152
async def Allow_checkin(message):
    # Testing Pre-Conditions
    
    global allow_checkin # chaning the global variable
    if(allow_checkin == True):
        # When True
        print('inside Allow_checkin')
        attendance_channel = client.get_channel(attendance_channel_ID)

        # Creating Embedded Message 
        myEmbed = discord.Embed(title="Allow_Checkin still online :green_circle:", description="BOT is waiting for new members to checkin", color=0x0000ff)
        myEmbed.add_field(name="Stop Checkin Command", value="use the command `!stopcheckin` to stop checkin and you will recieve an attendance list", inline=False)
        myEmbed.set_footer(text=("Command by → " + message.author.name))

        # Sending Embeded Message 
        await attendance_channel.send(embed=myEmbed)

        
        await attendance_channel.send("allow_checkin is still online")
        await attendance_channel.send("to end allow_checkin use the command !stopcheckin")

    else: 
        # When False 
        
        # Switching the value of data
        allow_checkin = True

        # Adding Authors to the list
        # await Record_Author(message)
        
        # Returning Conformation
        attendance_channel = client.get_channel(attendance_channel_ID)

        myEmbed = discord.Embed(title="Allow_Checkin Online :white_check_mark:", description="Now members can do their attendance procedure", color=0x00ff00)
        myEmbed.add_field(name="Stop Checkin Command", value="use the command `!stopcheckin` to stop checkin and you will recieve an attendance list", inline=False)
        myEmbed.set_footer(text=("Command by → " + message.author.name))

        await attendance_channel.send(embed=myEmbed)

    
# Stop_checkin
# Pre-Condition: 1) allow_checkin should be true
# Post-Condition: 1) turns off allow_checkin
async def End_checkin():
    global authorList
    global allow_checkin
    attendance_channel = client.get_channel(attendance_channel_ID)
    if(allow_checkin):
        # Changing the value to false 
        allow_checkin = False

        # Sending Information about the authors 
        # await Send_Author_List()

        # Sending Information about the authors using File IO
        # Function Call to File_IO
        if(len(authorList) != 0):
            # When someone checked in
            await File_IO()
        else:
            # When no one checked 
            myEmbed = discord.Embed(title="No one checked in", description="Looks like no one checked in :man_shrugging: ", color=0xffffff)
            await attendance_channel.send(embed=myEmbed)
            await attendance_channel.send("https://tenor.com/view/spongebob-nickelodeon-shrug-spongebob-squarepants-nothing-gif-5752969")

        # Erasing authorList
        authorList.clear()

        # Sending Confirmation to the Masters 
        await attendance_channel.send("allow_checkin successfully turned off :white_check_mark:")
    
    else:
        # Returning Error Message 
        await attendance_channel.send("allow_checkin is already off")
        await attendance_channel.send("To enable allow_checkin use `!startcheckin`")


# Record_Author
# Pre-Condition: 1) All prerequisites are satisfied
# Post-Condition: 1) The BOT records the time and name of the author in a list
async def Record_Author(message):
    # Add Authors to List 
    global authorList
    global time
    localTime = time.asctime( time.localtime(time.time()) )

    # Preventing Duplication 
    authorExists = False # initial value False 


    for i in range(len(authorList)):
        if(message.author == authorList[i][0]):
            print("Duplication Detected!")
            authorExists = True


    if(authorExists == False):
      # Adding Author 
        authorList.append([message.author, localTime])

        # Sending Conformation Message to Author 
        await Send_dm_to_members(message, False)

    else:
        # When duplication occurs 
        # Sending Duplication message
        await Send_dm_to_members(message, True)
        

# Send_Author_List 
# Pre-Condition: 1) The admins must end check in 
# Post-Condition: 2) The admins get the list of people who checked in
async def Send_Author_List():
    # Sending an Embeded Message
    attendance_channel = client.get_channel(attendance_channel_ID)
    if(len(authorList) == 0):
        # When no one checked in 
        attendance_channel.send("Looks like no one checked in :cold_sweat: ")
    else:
        # Atleast someone checked in 
        count = 1
        for i in range(len(authorList)):
            helpVariable = str(str(count) + ". " + str(authorList[i][0]) + " checked in at " + str(authorList[i][1]))
            await attendance_channel.send(helpVariable)
        

# File_IO
# Pre-Condition: 1) Prerequisites must be met 
# Post-Condition: 1) Creates a new .txt file and sends it to the admin 
#                 2) Deletes the .txt file after sending it to the admin
async def File_IO():

    # Finding what day is today and using it as fileName
    week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    week_num = datetime.datetime.today().weekday()
    todays_day = week_days[week_num]

    fileName = str(todays_day) + ".txt"
    print(fileName)

    # Opening the .txt file
    f = open(fileName,"w+") # w+ → tells to create and write a file if DND

    # Writing on .txt file
    for i in range(len(authorList)):
        f.write(str(i+1) + ". " + str(authorList[i][0]) + " --------> " + str(authorList[i][1]) + "\n")

    # Closing File
    f.close()


    # Sending the .txt file to the admins
    attendance_channel = client.get_channel(attendance_channel_ID)
    await attendance_channel.send("Attendance List : ")
    await attendance_channel.send(file=discord.File(fileName))


    # Deleting the created file
    os.remove(fileName)
    

# Version_Info() 
# Pre-Condition: 1) Someone calls the command 
# Pre-Condition: 1) Sends the embeded version information as a DM
async def Version_Info(message):
    # Finding Author 
    dm_author = message.author 

    # Sending Embeded Message 
    versionEmbed = discord.Embed(title="Developer Information", color=0x800080)
    versionEmbed.add_field(name="Version 1.5", value="Fifth Beta Version converted to Final version", inline=False) 
    versionEmbed.add_field(name="Developer's", value="Hardik Paudyal\nRajjya Rohan Paudyal", inline=False)
    versionEmbed.add_field(name="Release Date", value="May 28, 2021 Friday", inline=False)
    
    # Sending Embeded Message
    await dm_author.send(embed=versionEmbed)



# Calling keep_alive to keep the server running 24/7
keep_alive() # function call from the next file


# Running the client on the server(makes bot online)
my_secret1 = os.environ['CHABI'] # importing the password from .env's alternative
                                 # name CHABI means key in Nepali language 
                                 # CHABI is discord BOT's key (top secrect)
client.run(my_secret1) # Connects to the BOT 








