import socket
from cfg import HOST, PORT, PASS, NICK, CHAN

def open_socket():
	s = socket.socket()
	s.connect((HOST, PORT))
	s.send("PASS " + PASS + "\r\n")
	s.send("NICK " + NICK + "\r\n")
	s.send("JOIN #" + CHAN + "\r\n")
	return s

def send_message(s, message):
	message_temp = "PRIVMSG #" + CHAN + " :" + message
	s.send(message_temp + "\r\n")
	print("Sent: " + message_temp)
