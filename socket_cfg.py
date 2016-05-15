import string
import socket
from cfg import HOST, PORT, PASS, NICK, CHAN

def open_socket():
	s = socket.socket()
	s.connect((HOST, PORT))
	s.send(bytes("PASS " + PASS + "\r\n", "UTF-8"))
	s.send(bytes("NICK " + NICK + "\r\n", "UTF-8"))
	s.send(bytes("JOIN #" + CHAN + "\r\n", "UTF-8"))
	return s

def send_message(s, message):
	message_temp = "PRIVMSG #" + CHAN + " :" + message
	s.send(bytes(message_temp + "\r\n", "UTF-8"))
	print("Sent: " + message_temp)
