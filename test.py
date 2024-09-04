import base64

# Original string
original_string = "Onyedikachi1"

# Encode the string into bytes, then encode those bytes into Base64
encoded_bytes = base64.b64encode(b"Onyedikachi1")

# Convert Base64 bytes back to a string
encoded_string = encoded_bytes.decode("utf-8")

print(encoded_string)  # Output: SGVsbG8sIFdvcmxkIQ==
print(encoded_bytes)


