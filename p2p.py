#nessery python libs
import socket
import threading
print("imports done!")
#varables
debung = 1

print("var done!")
#the sause
def broadcast_message_to_network(message, port=12345):
    # Create a UDP socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    # Define the broadcast address (255.255.255.255 means all devices on the local network)
    broadcast_address = ('<broadcast>', port)

    # Broadcast the message
    udp_socket.sendto(message.encode(), broadcast_address)

    # Close the socket
    udp_socket.close()

import socket

def listen_for_broadcast(port=12345):
    # Create a UDP socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the specified port
    udp_socket.bind(('', port))

    print(f"Listening for broadcasts on port {port}...")

    while True:
        data, addr = udp_socket.recvfrom(1024)
        print(f"Received a broadcast from {addr}: {data.decode()}")




if __name__ == "__main__":
    message = "Hello, world!"
    broadcast_message_to_network(message)

if __name__ == "__main__":
    listen_for_broadcast()
print("def done!")





