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
import time
from cfg import *

s = open_socket()
join_room(s)
readbuffer = ""
commands = ["!songrequest", "!song", "!mods"]
elapsed_time = int(time.time())

while True:
	readbuffer = readbuffer + s.recv(1024).decode("UTF-8")
	temp = str.split(readbuffer, "\n")
	#test_line = input("Enter test line: ")
	#line = ":resinplays!:" + test_line
	readbuffer = temp.pop()
	songlist = open("songlist.txt", "r+")

	for line in temp:
		print("Line: " + line)
		user = get_user(line)
		message = get_message(line)
		print ("Message: " + message)
		print ("User: " + user)

		if message == "PING " and user == tmi.twitch.tv:
			print("PONG send attempt")
			s.send(bytes("PONG :tmi.twitch.tv\r\n".encode("UTF-8")))
			print("PONG sent successfully")

		elif message == "!commands":
			print("Commands if statement")
			send_message(s, "These are channel commands: " + commands)

		elif message == "!test":
			print("Does this work?")

		else:
			print("You Fail")

		time.sleep(30)

	#blurb that plays every 30 minutes
	if int(time.time()) - elapsed_time >= 1800:
		#print("Welcome to the stream! Feel free to ask questions or chat, I promise I'm watching!")
		send_message(s, "Welcome to the stream! Feel free to ask questions or chat, I promise I'm watching!")
		elapsed_time = time.time()
