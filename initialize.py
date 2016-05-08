import string
from socket_cfg import send_message

def join_room(s):
	readbuffer = ""
	loading = True
	while loading:
		readbuffer = readbuffer + s.recv(1024)
		temp = string.split(readbuffer, "\n")
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
