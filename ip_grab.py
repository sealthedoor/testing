import socket

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

if __name__ == "__main__":
    your_local_ip = get_local_ip()
    print(f"Your Local IP Address: {your_local_ip}")
