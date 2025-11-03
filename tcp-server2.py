import socket
import threading

HOST = 'localhost'
PORT = 30001
data_payload = 2048
backlog = 5

def client_handler(client, address):
    print(f"Client connected from {address}")

    try:
        while True:
            data = client.recv(data_payload)

            if not data:
                break

            print(f"Data from {address}: {data.decode('utf-8')}")
            s = client.send(data)
            print(f"Sent {s} bytes back to {address}")

    except Exception as e:
        print(f"Error with client {address}: {e}")
    finally:
        client.close()
        print(f"Connection with {address} closed")


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

print(f"Starting up echo server on {HOST} port {PORT}")
sock.bind((HOST, PORT))

sock.listen(backlog)

print("Server is listening for connections...")

try:
    while True:
        print("Waiting to receive message from client")
        client, address = sock.accept()

        client_thread = threading.Thread(
            target=client_handler,
            args=(client, address)
        )
        client_thread.daemon = True
        client_thread.start()
        print(f"Started thread for client {address}")

except KeyboardInterrupt:
    print("\nServer is shutting down...")
finally:
    sock.close()