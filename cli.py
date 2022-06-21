import argparse
from jamal import generate_key, encrypt_file, encrypt_message, decrypt_file, decrypt_message

class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

parser = argparse.ArgumentParser(description='Cli tool for taher el-gamal')
parser.add_argument('type', help='type of operation')
parser.add_argument('-m', '--message', help='message to encrypt or decrypt')
parser.add_argument('-f', '--file', help='file to encrypt or decrypt')
parser.add_argument('-o', '--output', help='output file')
parser.add_argument('-k', '--key', help='private key for decryption')
args =parser.parse_args()
PRIVATE_KEY, PUBLIC_KEY = generate_key()
if args.type == "encrypt":
    if args.message and args.file:
        print("\n")
        print(f"{Bcolors.BOLD}{Bcolors.FAIL}Error: You can't encrypt a file and a message at the same time i'm too lazy to handle this{Bcolors.ENDC}\n")
        exit(1)
    elif args.file:
        encrypted_message, output = encrypt_file(PUBLIC_KEY, args.file, args.output)
    elif args.message:
        encrypted_message, output = encrypt_message(PUBLIC_KEY, args.message, args.output)
    else:
        print("\n")
        print(f"{Bcolors.BOLD}{Bcolors.FAIL}Error: You must provide a message or file to decrypt{Bcolors.ENDC}\n")
        exit(1)
    print("\n")
    print(f"{Bcolors.BOLD}{Bcolors.OKGREEN}Done: Encryption finished successfully!{Bcolors.ENDC}")
    print(f"{Bcolors.BOLD}{Bcolors.WARNING} *** You need private key to decrypt ***{Bcolors.ENDC}")
    print(f"{Bcolors.BOLD}{Bcolors.HEADER}         Private key : {PRIVATE_KEY}{Bcolors.ENDC}")
    print(f"{Bcolors.BOLD}{Bcolors.WARNING} *** this key its just yours keep it secret ***{Bcolors.ENDC}")
    if output is not None:
        print(f"{Bcolors.BOLD}{Bcolors.OKBLUE}Output file : {output}{Bcolors.ENDC}")
    print(f"{Bcolors.BOLD}Encrypted message:\n{encrypted_message}{Bcolors.ENDC} \n")

elif args.type == "decrypt":
    if args.key:
        key = eval(args.key)
        if args.message and args.file:
            print("\n")
            print(f"{Bcolors.BOLD}{Bcolors.FAIL}Error: You can't decrypt a file and a message at the same time i'm too lazy to handle this{Bcolors.ENDC} \n")
            exit(1)
        elif args.file:
            decrypted_message, output = decrypt_file(key, args.file, args.output)
        elif args.message:
            decrypted_message, output = decrypt_message(key, eval(args.message), args.output)
        else:
            print("\n")
            print(f"{Bcolors.BOLD}{Bcolors.FAIL}Error: You must provide a message or file to decrypt{Bcolors.ENDC}\n")
            exit(1)
        print("\n")
        print(f"{Bcolors.BOLD}{Bcolors.OKGREEN}Done: Decryption finished successfully!{Bcolors.ENDC}")
        if output is not None:
            print(f"{Bcolors.BOLD}{Bcolors.OKBLUE}Output file : {output}{Bcolors.ENDC}")
        print(f"{Bcolors.BOLD}Message:\n{decrypted_message}{Bcolors.ENDC}\n")
    else:
        print("\n")
        print(f"{Bcolors.FAIL} FAILED {Bcolors.ENDC}: {Bcolors.WARNING}Private key required{Bcolors.ENDC} \n")   