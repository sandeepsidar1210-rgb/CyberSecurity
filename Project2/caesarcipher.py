def crypt(txt, k , mode ="enc"):
    res =""
    for c in txt:
        if c.isalpha():
            # b = base ASCII value (65 for A-Z, 97 for a-z)
            b = 65 if c.isupper() else 97

            # s = shift direction (forward for lock, backward for unlock)
            s = k if mode == "enc" else -k

            # The mathematical shift logic
            res += chr((ord(c) - b + s) % 26 + b)

        else:
            # Handle edge cases (spaces, symbols, numbers)
            res += c 


    return res

def main():
    print("---Symmetric Cryptograhic Engine---")

    # IPO Cycle: Input [cite: 635] 
    msg = input("Enter text to secure:")
    k = int (input("Enter numerical shift key (e.g., 3)"))

    # IPO Cycle: Process & Output for Encryption [cite: 635, 638]
    enc = crypt (msg , k , "enc")
    print(f"\n[LOCKED] Ciphertext: {enc}")

    # What it does: It calls our crypt function, hands it the message and the key, and asks it to encrypt ("enc"). It saves the result in enc and prints it to the screen.

    # IPO Cycle: Process & Output for Decryption [cite: 635, 638]
    dec = crypt(enc , k , "dec")
    print(f"[UNLOCKED] Plaintext: {dec}")



if __name__ == "__main__":
    main()
