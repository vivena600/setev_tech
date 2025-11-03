import socket

HOST = "task.miminet.ru"
PORT = 8011

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((HOST, PORT))

parts = {}
while len(parts) < 7:
    try:
        s.send(b"")
        data = s.recv(1005)
    except:
        continue
    parts[len(data)] = data

last_part, *sorted_parts = sorted(parts.values(), key=len)

with open("image/udp_ex_3.png", "wb") as img:
    for data in sorted_parts:
        img.write(data)
    img.write(last_part)
