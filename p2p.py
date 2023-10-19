import socket
import threading
import sys

debug = 1

def broadcast_message_to_network(message, target_ip='127.0.0.1', port=12345):
    # Create a UDP socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    # Define the broadcast address
    broadcast_address = (target_ip, port)

    # Broadcast the message
    udp_socket.sendto(message.encode(), broadcast_address)

    # Close the socket
    udp_socket.close()

def listen_for_broadcast(port=12345):
    # Create a UDP socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the specified port and the wildcard address
    udp_socket.bind(('0.0.0.0', port))

    print(f"Listening for broadcasts on port {port}...")

    while True:
        try:
            data, addr = udp_socket.recvfrom(1024)
            print(f"Received a broadcast from {addr}: {data.decode()}")
        except KeyboardInterrupt:
            print("Ctrl+C pressed. Exiting.")
            sys.exit()

if __name__ == "__main__":
    message = "Hello, world!"
    target_ip = input("Enter the target IP address (default is 127.0.0.1): ") or '127.0.0.1'
    broadcast_message_to_network(message, target_ip)

if __name__ == "__main__":
    listen_for_broadcast()
