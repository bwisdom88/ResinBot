'''
Ideas:
!songrequest
!song
!mods
Follower notification in chat
Sub notification in chat
Find a way to make commands only work for subs
'''

import string
from cfg import *

#s = open_socket()
#join_room(s)
readbuffer = ""
commands = ["!songrequest", "!song", "!mods"]

while True:
	test_input = input("Test line:")
	readbuffer = ":resinplays:" + test_input
	#readbuffer = readbuffer + s.recv(1024).decode("UTF-8")
	temp = str.split(readbuffer, "\n")
	#readbuffer = temp.pop()
	#for line in temp:
		#print("But this one works")
	#change temp[0] to line for prod
	#for line in temp:
	#print(line)
	user = get_user(temp[0])
	message = get_message(temp[0])
	#analysis = message.split(" ")
	print ("Message: " + message)
	print ("User: " + user)

	if message == "PING ":
		print("PONG send attempt")
		#s.send(bytes("PONG :tmi.twitch.tv\r\n".encode("UTF-8")))
		print("PONG sent successfully")

	if message == "!commands":
		print("Commands if statement")
		#send_message(s, "These are channel commands: " + commands)

	if message == "!test":
		print("Does this work?")

		#This is a feature that will be revisted later
#		elif analysis[0] == "!addcomm" and user == CHAN:
#			breakdown = message.split(" +")
#			added_commands.extend[breakdown[1]]
#			added_commands_text.extend[breakdown[2]]

		#elif analysis[0] == "!songrequest":
			#breakdown = message.split(" ")
			#print(breakdown[1])
			#songlist.write(breakdown[1] + "\r\n")
			#take URL and add it to a list for playback
			#2 part list split by space
			#once played remove from list
			#blacklist? How?
			#guard against evil requests
			#https://www.youtube.com/watch?v=PajEshrnGdY

		#if "!song" in message:
		#elif analysis[0] == "!song":

		#elif analysis[0] == "!pausebot" and user == CHAN:
			#put bot to sleep
			#if we do this how do we restart it?

		#elif analysis[0] == "!startbot" and user == CHAN:
	#playing songs
	#status blurb every 30 minutes
