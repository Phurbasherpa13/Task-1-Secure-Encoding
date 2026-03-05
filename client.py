import socket
import base64

def start_client():
    host = '127.0.0.1'
    port = 65432

    # Create a TCP/IP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        
        # Get user input
        message = input("Enter message to send securely over TCP: ")
        
        # 1. Encoding Process
        # Before sending, we encode the string to Base64 bytes
        # This simulates preparing data for a text-based protocol
        encoded_bytes = base64.b64encode(message.encode('utf-8'))
        
        print(f"\n--- SENDING DATA ---")
        print(f"Original: {message}")
        print(f"Sending over TCP as: {encoded_bytes.decode('utf-8')}\n")

        # 2. Transmission
        # We send the encoded bytes
        s.sendall(encoded_bytes)
        
        # Wait for server response
        data = s.recv(1024)
        print(f"\n[Server Reply]: {data.decode('utf-8')}")

if __name__ == "__main__":
    start_client()
