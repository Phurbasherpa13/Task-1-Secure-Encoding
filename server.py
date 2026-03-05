import socket
import base64

def start_server():
    host = '127.0.0.1'  # Localhost
    port = 65432        # Port to listen on

    # Create a TCP/IP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"[*] Server listening on {host}:{port}...")
        print("[*] Waiting for client to send data...\n")

        conn, addr = s.accept()
        with conn:
            print(f"[+] Connected by {addr}")
            
            # 1. Receive Raw Data from TCP
            # We receive up to 1024 bytes. This is what is actually traveling the wire.
            raw_tcp_data = conn.recv(1024)
            
            if not raw_tcp_data:
                return

            print(f"--- DATA RECEIVED OVER TCP ---")
            # Display the raw bytes as they look on the network (Base64)
            print(f"Raw Payload (Encoded): {raw_tcp_data.decode('utf-8')}")
            
            # 2. Decoding Process
            try:
                # The server knows the protocol is Base64, so it decodes
                decoded_message = base64.b64decode(raw_tcp_data).decode('utf-8')
                print(f"Decoded Message:       {decoded_message}")
            except Exception as e:
                print(f"Error decoding: {e}")

            # Send confirmation back
            conn.sendall(b"Message received and decoded successfully.")

if __name__ == "__main__":
    start_server()