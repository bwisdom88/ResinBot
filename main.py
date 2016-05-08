import string
from socket_cfg import open_socket
from initialize import join_room

s = open_socket()
join_room(s)
readbuffer = ""

while True:
	readbuffer = readbuffer + s.recv(1024)
	temp = string.split(readbuffer, "\n")
	readbuffer = temp.pop()

	for line in temp:
		print(line)
		
