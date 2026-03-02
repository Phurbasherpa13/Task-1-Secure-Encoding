import base64
import urllib.parse
import zlib
import json
import sys

class SecureDataExchange:
    def __init__(self, data=None):
        self.raw_data = data

    def encode_base64url_safe(self, data_dict):
        """Simulates creating a JWT-like payload (Base64URL)."""
        json_str = json.dumps(data_dict, separators=(',', ':'))
        b64_bytes = base64.b64encode(json_str.encode('utf-8'))
        return b64_bytes.decode('utf-8').replace('+', '-').replace('/', '_').rstrip('=')

    def compress_and_encode(self):
        """Efficiency Demo: Compress then Encode."""
        if isinstance(self.raw_data, str):
            self.raw_data = self.raw_data.encode('utf-8')
        compressed = zlib.compress(self.raw_data)
        encoded = base64.b64encode(compressed).decode('utf-8')
        print(f"Original Size: {len(self.raw_data)} bytes")
        print(f"Final Size: {len(encoded)} bytes")
        return encoded

    def analyze_encoding_security(self, user_input):
        """
        Example 2: Injection Prevention Analysis
        Visualizes how a malicious payload looks in different formats.
        """
        print("\n--- Example 2: Injection Prevention Analysis ---")
        print(f"1. Raw ASCII String: {user_input}")
        
        hex_bytes = user_input.encode('utf-8').hex()
        formatted_hex = ' '.join([hex_bytes[i:i+2] for i in range(0, len(hex_bytes), 2)])
        print(f"2. Hex Representation:  {formatted_hex}")

        url_encoded = urllib.parse.quote(user_input, safe='')
        print(f"3. URL Encoded:        {url_encoded}")

        b64_encoded = base64.b64encode(user_input.encode('utf-8')).decode('utf-8')
        print(f"4. Base64 Encoded:     {b64_encoded}")
        print("-" * 60)

def interactive_translator():
    """
    Example 4: Interactive Encoder/Decoder Tool
    Allows user to input text to get URL/Base64 encodings, or input 
    encodings to get the raw text back.
    """
    print("\n" + "="*60)
    print("     INTERACTIVE ENCODER/DECODER TOOL")
    print("="*60)
    print("Instructions:")
    print("1. Type any text to see it Encoded.")
    print("2. Paste a URL-encoded string (e.g., %20) to see it Decoded.")
    print("3. Paste a Base64 string to see it Decoded.")
    print("4. Type 'exit' or 'quit' to stop.")
    print("-" * 60)

    while True:
        user_input = input("\nInput: ")
        
        if user_input.lower() in ['exit', 'quit']:
            print("Exiting tool...")
            break

        # --- URL Operations ---
        print("\n[URL Encoding Operations]")
        # 1. URL Encode (Convert unsafe chars to %xx)
        url_encoded_output = urllib.parse.quote(user_input, safe='')
        print(f" -> URL Encoded:  {url_encoded_output}")
        
        # 2. URL Decode (Convert %xx back to char)
        url_decoded_output = urllib.parse.unquote(user_input)
        if url_decoded_output != user_input:
            print(f" -> URL Decoded:  {url_decoded_output}")
        else:
            print(f" -> URL Decoded:  (No change - input was not URL encoded)")

        # --- Base64 Operations ---
        print("\n[Base64 Encoding Operations]")
        try:
            # 1. Base64 Encode
            # We must convert string to bytes first
            b64_encoded_output = base64.b64encode(user_input.encode('utf-8')).decode('utf-8')
            print(f" -> Base64 Encoded: {b64_encoded_output}")

            # 2. Base64 Decode
            try:
                b64_decoded_output = base64.b64decode(user_input).decode('utf-8')
                print(f" -> Base64 Decoded: {b64_decoded_output}")
            except Exception:
                print(f" -> Base64 Decoded: (Invalid Base64 string)")
                
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    # Example 1: Secure Token
    print("--- Example 1: Secure Token (Base64URL) ---")
    auth_header = {"alg": "HS256", "typ": "JWT", "user": "admin"}
    exchange = SecureDataExchange()
    token_part = exchange.encode_base64url_safe(auth_header)
    print(f"Token: {token_part}\n")

    # Example 2: Injection Analysis
    malicious_input = "<script>alert('XSS')</script>"
    secure_handler = SecureDataExchange()
    secure_handler.analyze_encoding_security(malicious_input)

    # Example 3: Compression
    print("--- Example 3: Efficiency (Compression + Encoding) ---")
    long_text = "Data " * 100
    optimized_exchange = SecureDataExchange(long_text)
    optimized_exchange.compress_and_encode()

    # Example 4: Interactive Tool (Requested Feature)
    # Run the interactive loop so you can type and encode/decode
    interactive_translator()