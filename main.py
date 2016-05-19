'''
Ideas:
!songrequest
!song
!mods
Follower notification in chat
Sub notification in chat

'''

import string
from cfg import *

s = open_socket()
join_room(s)
readbuffer = ""
temp_list = ""
commands = ["!songrequest", "!song", "!mods"]
added_commands = []
added_commands_text = []

while True:
	readbuffer = readbuffer + s.recv(1024).decode("UTF-8")
	temp = str.split(readbuffer, "\n")
	readbuffer = temp.pop()

	for line in temp:
		print(line)
		user = get_user(line)
		message = get_message(line)
		analysis = message.split(" ")
		#print(user + " typed :" + message)

		#if "!commands" in message:
		if analysis[0] == "!commands":
			merged_lists = commands + added_commands
			for command in merged_lists:
				temp_list += str(command) + ", "
			send_message(s, "These are channel commands: " + temp_list)

		#if "!addcomm" in message && user == CHAN:
		elif analysis[0] == "!addcomm" && user == CHAN:
			breakdown = message.split(" +")
			added_commands.extend[breakdown[1]]
			added_commands_text.extend[breakdown[2]]

		#if "!songrequest" in message:
		elif analysis[0] == "!songrequest":
			#take URL and add it to a list for playback
			#2 part list split by space
			#once played remove from list
			#blacklist? How?
			#guard against evil requests

		#if "!song" in message:
		elif analysis[0] == "!song":

		elif analysis[0] == "!pausebot" && user == CHAN:
			#put bot to sleep
			#if we do this how do we restart it?

		elif analysis[0] == "!startbot" && user == CHAN:
