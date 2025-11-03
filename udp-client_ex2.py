import socket

HOST = "task.miminet.ru"
PORT = 8010

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.settimeout(5)

try:
    message = b""

    client.sendto(message, (HOST, PORT))
    data, address = client.recvfrom(1024)

    print(f"Response data: {data.decode('utf-8')}")
except socket.timeout:
    print("Timeout: No response received")
except Exception as e:
    print("Socket error: " + str(e))