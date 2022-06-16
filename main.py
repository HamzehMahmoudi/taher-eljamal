from jamal import *

msg = "mamad"

# with open("file.txt", "r") as f:
#     msg = f.read()
# encrypted_message = encrypt_message(PUBLIC_KEY, msg)
# decrypted_message = decrypt_message(PRIVATE_KEY, encrypted_message)
# with open("enc.txt", "w") as f:
#     f.write(str(encrypted_message))
# print(f"encoded= {encrypted_message},\n decoded = \n{decrypted_message}\n\n\n")

# with open("enc.txt", "r") as f:

# decrypted_message = decrypt_message(PRIVATE_KEY, encrypted_message)
encrypted, encode_file =encrypt_file(PUBLIC_KEY, "file.txt", "enc.txt")
decrypted, decode_file = decrypt_file(PRIVATE_KEY, "enc.txt", "dec.txt")
print(f"encoded= {encrypted},\n decoded = \n{decrypted}\n\n\n")
print(f"message decryped from file: \n{decrypted}")