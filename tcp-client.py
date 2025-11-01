import socket
import select

HOST = "task.miminet.ru"
PORT = 8010
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

try:
    s.connect((HOST, PORT))
    print("Connected to server")

    all_data = b""
    while True:
        data = s.recv(4096)
        if not data:
            break
        all_data += data

    png_data = all_data[::-1]

    with open("received_image.png", "wb") as f:
        f.write(png_data)

    print(png_data)

except Exception as e:
    print("Socket error: "+str(e))
finally:
    s.close()