
def main():
    num_array1 = [
        12, 33, 36, 9, 26, 22, 41, 22, 29, 13,
        107, 9, 19, 74, 8, 29, 44, 76, 17, 61,
        1, 15
    ]
    xor_key = "JegHarGemtFlagetBagXor"
    flag = "".join(chr(num_array1[i] ^ ord(xor_key[i])) for i in range(len(num_array1)))
    print("Flag:", flag)

if __name__ == "__main__":
    main()

