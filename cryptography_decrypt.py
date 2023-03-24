import time
from datetime import datetime
import random 

def decrypt(ciphertext, key):
    #alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plaintext = ""
    for i in range(0,len(ciphertext),key+1):
        plaintext = plaintext + ciphertext[i]
    return plaintext

def decrypt_time(ciphertext, key):
    start_time = datetime.now()
    print("Starting decryption at:", start_time.strftime("%Y-%m-%d %H:%M:%S.%f"))  # printing the start time

    time.sleep(3)  # sleep time before decrypting. 

    plaintext = decrypt(ciphertext, key)  # decrypt fucntion being called
    end_time = datetime.now()
    print("Decryption finished at:", end_time.strftime("%Y-%m-%d %H:%M:%S.%f")) # printing the end time
    decryption_time = (end_time - start_time).total_seconds() - 3 # subtracting the sleep time of 3 seconds
    # Time conversion into minutes and seconds
    if decryption_time >= 60:
        minutes = int(decryption_time // 60)
        seconds = int(decryption_time % 60)
        print("Decryption took", minutes, "minute(s)", seconds, "second(s)")
    else:
        print("Decryption took", round(decryption_time, 6), "second(s)") # rounding the seconds to 6 milliseconds
    print("Plaintext:", plaintext)
    
# while loop to handle multiple cypher decryption until 'exit'
while True:
    ciphertext = input("Enter ciphertext (or type 'exit' to stop): ")
    if ciphertext == 'exit':
        print("Exiting program...")
        break
    key = int(input("Input a key as a number between 1 and 10: "))
    while not (key >= 1 and key <= 10):
        print("Invalid key, try again!")
        key = int(input("Input a key as a number between 1 and 10: "))
    print("...")
    time.sleep(2)
    print("Decrypting cyphertext...")
    time.sleep(2)
    print("...")
    time.sleep(1)
    decrypt_time(ciphertext, key)
    print("...")
    
