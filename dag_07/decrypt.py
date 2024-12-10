import struct
import base64
def decrypt(encrypted_string):
    encoded_array = base64.b64decode(encrypted_string)
    
    decoded_array = bytearray(32)
    
    for index in range(8):
        encoded_four_bytes = encoded_array[index*4:index*4+4]
        
        encoded_four_bytes_integer = struct.unpack('<i', bytes(encoded_four_bytes))[0]
        
        original_number = -encoded_four_bytes_integer 
        
        decoded_four_bytes = struct.pack('<i', original_number)
        decoded_array[index*4:index*4+4] = decoded_four_bytes
    
    return decoded_array.decode('utf-8').rstrip('\x00')

# Example usage
decrypted_string = decrypt("uru8voW7zNK0zpi4zY3SltOSqsqQzLOXzc6yggAAAAA=")
print(decrypted_string)


