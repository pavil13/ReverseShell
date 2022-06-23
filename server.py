import socket

s = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
s.bind(('0.0.0.0', 8888))
s.listen(5)
client, addr = s.accept()

while True:
    command = imput("[-] Enter your command: ")

    if command.lower() == 'exit':
        client.close()
        s.close()
        print("[-] Соединение с клиентом '{}' прервано".format(addr))
        break
    else:
        client.send(command.decode())        
        print('[-] Команда отправлена')
client.close()
s.close()
