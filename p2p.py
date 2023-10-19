import socket
import uuid
import threading

# Define the broadcast address and port
broadcast_address = '255.255.255.255'  # This is the broadcast address for the local network
broadcast_port = 12345

# Create a UDP socket for broadcasting
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# Generate a unique identifier based on the MAC address
def get_unique_identifier():
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    print(mac)
    return mac

# Retrieve your local IP address
def get_local_ip():
    try:
        # Create a socket and connect to an external host
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  # Connect to Google's public DNS server
        local_ip = s.getsockname()[0]  # Get the local IP address
        s.close()
        print(local_ip)
        return local_ip
    except socket.error:
        return "Unable to determine local IP address"

def broadcast_my_ip():
    local_ip = get_local_ip()
    unique_identifier = get_unique_identifier()
    message = f"Broadcasting IP: {local_ip}, MAC: {unique_identifier}"

    seen_devices = set()
    found_devices = []

    while True:
        udp_socket.sendto(message.encode(), (broadcast_address, broadcast_port))
        # You can add a delay here to control how often you broadcast

        for device in seen_devices:
            if device not in found_devices:
                found_devices.append(device)

        if len(found_devices) > 0:
            print(f"IP: {local_ip}, MAC: {unique_identifier}")
            print("Found Devices:")
            for i, device in enumerate(found_devices, start=1):
                print(f"{i}. {device}")

    return(found_devices)

def listen_for_broadcasts():
    udp_socket.settimeout(1)  # Set a timeout for receiving broadcasts

    while True:
        try:
            data, addr = udp_socket.recvfrom(1024)
            message = data.decode()
            if message.startswith("Broadcasting IP:"):
                parts = message.split(", ")
                if len(parts) >= 2:
                    unique_identifier = parts[1].split(": ")[1]
                    if unique_identifier not in seen_devices:
                        seen_devices.add(unique_identifier)
                        print(f"New device found: {message} from {addr}")
        except socket.timeout:
            pass

if __name__ == "__main__":
    seen_devices = set()

    # Start broadcasting in a separate thread
    broadcast_thread = threading.Thread(target=broadcast_my_ip)
    broadcast_thread.daemon = True
    broadcast_thread.start()

    # Start listening for broadcasts in the main thread
    listen_for_broadcasts()
