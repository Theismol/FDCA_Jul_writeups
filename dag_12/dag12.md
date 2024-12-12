# Opgave
I en skjult dal i Asgård har jætterne udviklet en algoritme, som de hævder er uigennemtrængelig. Vi har fået adgang til nogle filer på tilforladelige måder. Herunder det output, der var på skærmen, da jætterne krypterede en vigtig besked.

Vi har desværre ikke nogen der er kyndige i jættekode. Måske du kan cracke deres kryptering?

Vedhæftet fil: filedump.zip

---

# Løsning

Zip filen indeholder følgende filer: **cipher.bin**, **encryption_output.txt**, **iv.bin**, **jaette_random_tools.py**, **encrypt.py**

**encrypt.py** indeholder denne kode:

```python
import getpass
import hashlib

from jaette_random_tools import JaetteAES, ThorLCG

# Initialize the LCG with exposed parameters
a = 1664525
c = 1013904223
m = 2**32
password = getpass.getpass("Secret jætte-key: ")
seed = int(hashlib.sha256(password.encode()).hexdigest(), 16) % m
rng = ThorLCG(seed, a=a, c=c, m=m)

# Post signature jætte laugh, but make it random to make it more scary
laughparts = [
    "Haaaha",
    "Heehhe",
    "Hiiha",
    "Ha",
    "Huihuhe",
    "Hae",
    "Huoo",
    "Hohhao",
    "Hua",
    "Hyu",
]

print("De kommer aldrig igennem vores avancerede krypteringsalgoritme")

laugh_seed = rng.next()
print("".join([laughparts[int(l)] for l in str(laugh_seed)]))

# Generate a secret key
key = bytes([rng.get_random_byte() for _ in range(16)])  # 128-bit key

# Check that an iv.bin file is present, otherwise make one
try:
    with open("iv.bin", "rb") as iv_file:
        iv = iv_file.read()
except FileNotFoundError:
    print("iv.bin not found, creating a default one")
    # Create a default
    iv = bytes(rng.get_random_byte() for _ in range(16))
    with open("iv.bin", "wb") as iv_file:
        iv_file.write(iv)

# Encrypt a super secret message using the secret key
with open("message.txt", "r") as message_input_file:
    payload = message_input_file.read()
cipher = JaetteAES(key)
ciphertext = cipher.encrypt(payload)

# Save the ciphertext to a file to be shared with jætte receivers
with open("cipher.bin", "wb") as cipher_file:
    cipher_file.write(ciphertext)

print("\nEncryption complete and written to 'cipher.bin'")
```

**jaette_random_tools.py** indeholder følgende relevante kode:

```python
class ThorLCG:
    """
    Thor's Linear Congruent Generator for generating thunderous random numbers.
    Harness the power of Mjölnir.
    """

    def __init__(self, seed, a, c, m):
        self.state = seed
        self.a = a
        self.c = c
        self.m = m

    def next(self):
        self.state = (self.a * self.state + self.c) % self.m
        return self.state

    def get_random_byte(self):
        """Return a random byte (0-255)"""
        return self.next() % 256

class JaetteAES:
    def __init__(self, key: bytes):
        # Check if an iv.bin is in the folder, otherwise fail hard and ask for the file
        try:
            with open("iv.bin", "rb") as iv_file:
                self.iv = iv_file.read()
        except FileNotFoundError:
            print("iv.bin not found, please add the file to the folder")

        self.key = key

    def encrypt(self, plaintext: str):
        cipher = AES.new(self.key, AES.MODE_CBC, iv=self.iv)
        return cipher.encrypt(pad(plaintext.encode(), AES.block_size))

    def decrypt(self, ciphertext: bytes):
        cipher = AES.new(self.key, AES.MODE_CBC, iv=self.iv)
        return unpad(cipher.decrypt(ciphertext), AES.block_size).decode()
```

**encryption_output.txt** indeholder dette: 
`Secret jætte-key: 
De kommer aldrig igennem vores avancerede krypteringsalgoritme
HuihuheHiihaHeehheHiihaHaeHaaahaHiihaHohhaoHuooHyu
iv.bin not found, creating a default one

Encryption complete and written to 'cipher.bin'`


Da vi egentlig bare skal finde passcode for at kunne decrypte ciphertexten tænkte jeg først jeg kunne prøve at bruteforce den.

Jeg prøvede at bruteforce med alfanumeriske tegn og fandt hurtigt at passcoden er **m** som giver flaget: **FDCA{YOU_BROKE_THE_RNG}**

Jeg er rimelig sikker på det her ikke var den tænkte løsning og at man skulle bruge laugh_seed ud fra **encryption_output.txt** til at reverse ThorLCG for at finde seed og derfra genskabe keyen til at decrypte flaget.


---
