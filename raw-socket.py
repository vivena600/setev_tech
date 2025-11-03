import socket
import sys


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
except socket.error as msg:
    print("Socket could not be created. Error Code : " + str(msg))
    sys.exit(-1)

try:
    while True:

        # Читаем пакет (максимальный размер 65565 байт)
        packet = s.recvfrom(65535)

        # Первый элемент кортежа - данные пакета
        packet_data = packet[0]

        # Второй элемент - адрес отправителя
        address = packet[1]

        print(f"Захвачен пакет длиной {len(packet_data)} байт от {address}")
        print(packet_data)

except KeyboardInterrupt:
    print("\nОстановка захвата пакетов")
    s.close()