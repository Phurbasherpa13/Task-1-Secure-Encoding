import base64
import urllib.parse
import zlib
import json

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
        Visualizes how a malicious payload looks in different formats:
        1. Raw ASCII (The threat)
        2. Hex (The underlying bytes)
        3. URL Encoded (The safe transport)
        4. Base64 (Another transport format)
        """
        print("\n--- Example 2: Injection Prevention Analysis ---")
        
        # 1. Raw Input
        print(f"1. Raw ASCII String: {user_input}")

        # 2. Hex Representation
        # We convert the string to bytes and then to Hexadecimal.
        # This reveals the 'dangerous' byte values like 0x3C (<) and 0x3E (>).
        hex_bytes = user_input.encode('utf-8').hex()
        # Format with spaces for readability (e.g., "3c 73 63...")
        formatted_hex = ' '.join([hex_bytes[i:i+2] for i in range(0, len(hex_bytes), 2)])
        print(f"2. Hex Representation:  {formatted_hex}")

        # 3. URL Encoding
        # Replaces unsafe characters with % followed by two hex digits.
        url_encoded = urllib.parse.quote(user_input, safe='')
        print(f"3. URL Encoded:        {url_encoded}")

        # 4. Base64 Encoding
        # Maps binary to ASCII characters. Note that '<' becomes 'PH' in Base64.
        b64_encoded = base64.b64encode(user_input.encode('utf-8')).decode('utf-8')
        print(f"4. Base64 Encoded:     {b64_encoded}")
        print("-" * 60)

# --- Real World Example Scenarios ---

# Example 1: Secure Token Transmission (OAuth style)
print("--- Example 1: Secure Token (Base64URL) ---")
auth_header = {"alg": "HS256", "typ": "JWT", "user": "admin", "exp": 1715620000}
exchange = SecureDataExchange()
token_part = exchange.encode_base64url_safe(auth_header)
print(f"Generated Token Header: {token_part}\n")

# Example 2: Injection Prevention (Updated with ASCII, Hex, URL, Base64)
malicious_input = "<script>alert('XSS')</script>"
secure_handler = SecureDataExchange()
secure_handler.analyze_encoding_security(malicious_input)

# Example 3: Efficiency Optimization
print("--- Example 3: Efficiency (Compression + Encoding) ---")
long_text = "Repetitive data string used to demonstrate GZIP compression efficiency. " * 50
optimized_exchange = SecureDataExchange(long_text)
optimized_exchange.compress_and_encode()