import argparse
from jamal import *

parser = argparse.ArgumentParser(description='Cli tool for taher el-gamal')
parser.add_argument('type', help='type of operation')
parser.add_argument('-m', '--message', help='message to encrypt or decrypt')
parser.add_argument('-f', '--file', help='file to encrypt or decrypt')
parser.add_argument('-o', '--output', help='output file')
parser.add_argument('-k', '--key', help='private key for decryption')
args =parser.parse_args()

if args.type == "encrypt":
    if args.file:
        encrypted_message, output = encrypt_file(PUBLIC_KEY, args.file, args.output)
        print(encrypted_message)
    elif args.message:
        encrypted_message = encrypt_message(PUBLIC_KEY, args.message, args.output)
        print(encrypted_message)
    print(f"encryption done you can decrypt it with this key {PRIVATE_KEY} keep it to yourself")
elif args.type == "decrypt":
    if args.key:
        key = eval(args.key)
        if args.file:
            decrypted_message, output = decrypt_file(key, args.file, args.output)
            print(f"decoded =\n{decrypted_message}")
        elif args.message:
            decrypted_message = decrypt_message(key, eval(args.message), args.output)
            print(f"decoded =\n{decrypted_message}")
    else:
        print("please provide a key")   