import signal
import os
import random
import sys
from Crypto.Cipher import DES3

class Desfunctional:
    def __init__(self):
        self.key = bytes.fromhex("5f84bbf8258121beec24a5078ab3e36f194858a23e484cc3")#os.urandom(24)
        self.iv = bytes.fromhex("c0e39ecbda9c191d")#os.urandom(8)
        self.flipped_bits = set(range(0, 192, 8))
        self.challenge = bytes.fromhex("7663d0e45349fa713fe226efe50466f4eb490b7cd4f7fed80e6fca078e2f74fd09dff137d8838621802f8cedba05d4fa4cb790dada76f4a33746dca8f4de5345")#os.urandom(64)
        self.counter = 128
        self.tt = 0

    def get_flag(self, plain):
        if plain == self.challenge:
            # with open("flag.txt", "rb") as f:
            #     FLAG = f.read()
            return "CTF{THIS_IS_NOT_THE_FLAG}"
        raise Exception("Not quite right")

    def get_challenge(self):
        #print(f"Encryption_key: {self.key.hex()}")
        #print(f"")
        cipher = DES3.new(self.key, mode=DES3.MODE_CBC, iv=self.iv)
        return cipher.encrypt(self.challenge)
        
    def corruption(self):
        if len(self.flipped_bits) == 192:
            self.flipped_bits = set(range(0, 192, 8))
        remaining = list(set(range(192)) - self.flipped_bits)
        num_flips = random.randint(1, len(remaining))
        self.tt = self.tt+1
        # if len(remaining)==0:
            #print(f"REPS: {tt}")
        smth = random.choices(remaining, k=num_flips)
        self.flipped_bits = self.flipped_bits.union(
            smth
            )
        # print(f"To flip: {smth}")
        mask = int.to_bytes(sum(2**i for i in self.flipped_bits), 24)
        # print(f"MASK:{mask.hex()}<<")
        return bytes(i ^ j for i, j in zip(self.key, mask))

    def decrypt(self, text: bytes):
        self.counter -= 1
        # if self.counter < 0:
        #     raise Exception("Out of balance")
        key = self.corruption()
        # print(f"Corrupted key:{key.hex()}")
        if len(text) % 8 != 0:
            return b''
        cipher = DES3.new(key, mode=DES3.MODE_CBC, iv=self.iv)
        return cipher.decrypt(text)


if __name__ == "__main__":
    chall = Desfunctional()
    PROMPT = ("Choose an API option\n"
              "1. Get challenge\n"
              "2. Decrypt\n"
              "3. Get the flag\n")
    signal.alarm(128)
    while True:
        try:
            option = int(input(PROMPT))
            if option == 1:
                print(chall.get_challenge().hex())
            elif option == 2:
                ct = bytes.fromhex(input("(hex) ct: "))
                print(chall.decrypt(ct).hex())
            elif option == 3:
                #print(f"Challenge:{chall.challenge.hex()}")
                pt = bytes.fromhex(input("(hex) pt: "))
                print(chall.get_flag(pt))
                sys.exit(0)
        except Exception as e:
            print(e)
            sys.exit(1)