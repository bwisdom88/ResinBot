'''
Ideas:
!songrequest
!song
!mods
Follower notification in chat
Sub notification in chat

'''

import string
from socket_cfg import *
from initialize import join_room
from read import *

s = open_socket()
join_room(s)
readbuffer = ""
temp_list = ""
commands = ["!songrequest", "!song", "!mods"]

while True:
	readbuffer = readbuffer + s.recv(1024).decode("UTF-8")
	temp = str.split(readbuffer, "\n")
	readbuffer = temp.pop()

	for line in temp:
		print(line)
		user = get_user(line)
		message = get_message(line)
		print(user + " typed :" + message)
		if "You Suck" in message:
			send_message(s, "No, you suck")
		if "!commands" in message:
			for command in commands:
				temp_list += str(command) + ", "
			send_message(s, "These are channel commands: " + temp_list)
