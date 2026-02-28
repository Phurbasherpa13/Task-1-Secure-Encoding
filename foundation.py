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

