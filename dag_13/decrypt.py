from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

with open("suspicious_signal.bin", "rb") as input_file:
    data = input_file.read()
    while True:
        key = data[:69]
        print(key)
        rest = data[69:]
        key = key[4:-1]
        key = bytes.fromhex(key.decode("utf-8"))
        cipher = AES.new(key, AES.MODE_ECB)
        data = cipher.decrypt(rest)
        #        padding_length = data[-1]
        #        data = data[:-padding_length]
        data = unpad(data, AES.block_size)
        print(len(data))
