import socket

# Define the broadcast address and port
broadcast_address = '255.255.255.255'  # This is the broadcast address for the local network
broadcast_port = 12345

# Create a UDP socket for broadcasting
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

def get_local_ip():
    try:
        # Create a socket and connect to an external host
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  # Connect to Google's public DNS server
        local_ip = s.getsockname()[0]  # Get the local IP address
        s.close()
        return local_ip
    except socket.error:
        return "Unable to determine local IP address"

def broadcast_my_ip():
    try:
        local_ip = get_local_ip()
        message = f"Device IP: {local_ip}"

        seen_devices = set()

        while True:
            udp_socket.sendto(message.encode(), (broadcast_address, broadcast_port))
            # You can add a delay here to control how often you broadcast

            try:
                data, addr = udp_socket.recvfrom(1024)
                message = data.decode()
                if message not in seen_devices:
                    seen_devices.add(message)
                    print(f"New device found: {message} from {addr}")
            except socket.timeout:
                pass

    except socket.error as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    udp_socket.settimeout(1)  # Set a timeout for receiving broadcasts
    broadcast_my_ip()  # Start broadcasting your IP address
