import string
from socket_cfg import *

def get_user(line):
	separate = line.split(":", 2)
	user = separate[1].split("!", 1)[0]
	return user

def get_message(line):
	separate = line.split(":", 2)
	if separate[0] == "PING ":
		s.send(bytes("PONG :tmi.twitch.tv\r\n".encode("UTF-8")))
	else:
		message = separate[2]
	return message
