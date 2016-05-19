#cfg.py
import string
import socket

HOST = "irc.twitch.tv"
PORT = 6667
NICK = "resinbot"
PASS = "oauth:jgt7f9oa7laa6321o98innxwetwkzo"
CHAN = "resinplays"

def open_socket():
	s = socket.socket()
	s.connect((HOST, PORT))
	s.send(bytes("PASS " + PASS + "\r\n", "UTF-8"))
	s.send(bytes("NICK " + NICK + "\r\n", "UTF-8"))
	s.send(bytes("JOIN #" + CHAN + "\r\n", "UTF-8"))
	return s

def join_room(s):
	readbuffer = ""
	loading = True
	while loading:
		readbuffer = readbuffer + s.recv(1024).decode("UTF-8")
		temp = str.split(readbuffer, "\n")
		readbuffer = temp.pop()

		for line in temp:
			print(line)
			loading = loading_complete(line)
	send_message(s, "Successfully joined chat")


def loading_complete(line):
	if("End of /NAMES list" in line):
		return False
	else:
		return True

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

def send_message(s, message):
	message_temp = "PRIVMSG #" + CHAN + " :" + message
	s.send(bytes(message_temp + "\r\n", "UTF-8"))
	print("Sent: " + message_temp)
