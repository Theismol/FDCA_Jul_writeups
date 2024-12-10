with open("flag.txt.ragnarok", "rb") as file:
    file_data = bytearray(file.read())

jotunheim_bytearray = bytearray(b"Jotunheim")

key_length = len(jotunheim_bytearray)
decrypted_flag = bytearray(
    (byte - jotunheim_bytearray[i % key_length]) % 256
    for i, byte in enumerate(file_data)
)

# Save the reversed data to a new file
print(decrypted_flag.decode("utf-8"))
