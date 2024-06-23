'''
This is the solution for the GoogleCTF 2024 for the problem DESFUNCTIONAL

Solution explained:
- Given the code of the running service we observe that the server decrypts any plaintext we provide but the key they use for the DES decryption is XORED with a mask
- The server randomly picks a few bits from the 16 byte - long mask that haven't been fliped and flips them.
- The idea for the solution is that at some point all the bits of the mask are flipped i.e. the mask is 0xffffffffffffffffffffffffffffffff
- If we provide 0x00000000000000000000000000000000 until we find a repeated decrypted output it means that the key used to decrypt these two outputs is the same.
- Since the original key is not changed then it means that with high probability the MASK is now 0xffffffffffffffffffffffffffffffff. 
- Therefore we can compute the IV by xoring the first 8 bytes of the decrypted output provided by the service with 0xffffffff.
- Now that we found IV we repeat the same procedure and provide the encrypted plaintext(self.challenge) XORED with the mask continually until we detect a circle.
NOTE: It's important to know the MASK since the key that will be used by the service to decrypt our key will be key ^ MASK at all times.
      Therefore if we ask the the service to decrypt the our plaintext we need to make sure that it will use the same key as when it will decrypt the solution we provide
- Therefore we provide self.challenge ^  (128 * "f") until we detect a circle, and then XOR the answer again thus obtaining our plaintext
'''

from pwn import *
import binascii
import warnings
from Crypto.Cipher import DES3

# Connect to the remote service
host = 'desfunctional.2024.ctfcompetition.com'
port = 1337
#run locally usig processes
# connection = process('./run.sh', shell=True)
connection = remote(host, port)

# Function to get the challenge
def get_challenge():
    connection.sendline(b'1')
    print(f"(1) Requesting Challenge...")
    response = connection.recvline().strip()
    return bytes.fromhex(response.decode())

# Function to decrypt a given ciphertext
def decrypt(ciphertext):
    connection.sendline(b'2')
    # print(f"(2) Attempt to decrypt {ciphertext.hex()}...")

    connection.recvuntil(": ")
    connection.sendline(ciphertext.hex())
    response = connection.recvline().strip()
    return bytes.fromhex(response.decode())

# Function to get the flag with a given plaintext
def get_flag(plaintext):
    connection.sendline(b'3')
    # print(f"(3) Attempt to get the flag with {plaintext.hex()}...")
    connection.recvuntil(": ")
    connection.sendline(plaintext.hex())
    response = connection.recvline().strip()
    return response

def detect_cycle(to_decrypt):
    decrypts = set()
    decrypted_with_f = "0"
    for i in range(100):
        # print("iteration: ", i)
        # Decrypt the challenge
        decrypted_text = decrypt(bytes.fromhex(to_decrypt))
        decrypted_with_f = decrypted_text
        if decrypted_text in decrypts:
            # print(f"[-] Full key iteration circuit detected. Ready to exploit...")
            # print(f"[-] Received Decrypted Text: {decrypted_text.hex()}")
            break
        decrypts.add(decrypted_text)
        # print(f"[-] Received Decrypted Text: {decrypted_text.hex()}")
    return decrypted_with_f

# Main interaction loop
def main():

    #Receive prompt

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        prompt = connection.recvuntil("flag\n")
        print(prompt.decode())
    
        # Get the challenge
        challenge = get_challenge()
        print(f"[-] Received Challenge: {challenge.hex()}")

        #Receive prompt
        prompt = connection.recvuntil("flag\n")
        print(prompt.decode())

        decrypted_with_f = detect_cycle("000000000000000000000000000000000000000000000000")
        #xor the first 8 bytes of the decrypted text with the last 8 bytes of the challenge
        iv = bytes(i ^ j for i, j in zip(decrypted_with_f[:8], decrypted_with_f[-8:]))
        print(f"[-] Calculated IV: {iv.hex()}")

        print("\n============= Repeat with masked challenge... ====================\n")
        trying = "f"*128
        masked_challenge = bytes(i ^ j for i, j in zip(bytes.fromhex(trying),challenge))
        decrypted_with_f = detect_cycle(masked_challenge.hex())
        # Unmask with 128*"f"
        unmask_plaintext1 = bytes(i ^ j for i, j in zip(decrypted_with_f, bytes.fromhex(128*"f")))[:8]
        
        plaintext = unmask_plaintext1.hex()+decrypted_with_f[8:].hex()

        print(f"\nSummary:")
        print(f"[-] Calculated Plaintext: {plaintext}")
        print(f"[-] Calculated IV: {iv.hex()}")
        print("\n============= Getting the flag... ====================\n")

        # Get the flag using the decrypted text
        flag_response = get_flag(bytes.fromhex(plaintext))
        print(f"[-] Received Flag Response: {flag_response.decode()}")

if __name__ == "__main__":
    main()
