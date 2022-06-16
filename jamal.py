
import random
from math import gcd

# generate large prime number
def generate_prime():
    while(1):
        p = random.randint(128, 512)
        if p % 2 == 0:
            p = p + 1
        if is_prime(p):
            return p   

def is_prime(num):
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5)+1, 2):
        if num % i == 0:
            return False
    return True

# get generator of a list of numbers
def get_generator(p):
    zp = set(num for num in range (1, p) if gcd(num, p) == 1)
    for g in range(1, p):
        z = set(pow(g, powers) % p for powers in range (1, p))
        if zp == z:
            return g
            
p = generate_prime()
g = get_generator(p)
alpha = random.randint(1, p-2)
# p = 7
# g = 3
# alpha = 3
betha = pow(g, alpha, p)
PRIVATE_KEY = (p, g, alpha)
PUBLIC_KEY = (p, g, betha)

def encrypt(public_key:tuple, data_block):
    p, g, betha = public_key
    k = random.randint(1, p-2)
    gamma = pow(g, k, p)
    delta = pow(betha, k, p) * data_block % p
    return gamma, delta

def decrypt(private_key:tuple, cipher:tuple):
    p, g, alpha = private_key
    gamma, delta = cipher
    m = pow(gamma, p-1-alpha, p) * delta % p
    return m

def encrypt_message(public_key:tuple, message:str, output=None)->list:
    blocks = []
    for c in message:
        data=ord(c)
        e = encrypt(public_key, data)
        blocks.append(e)
    if output is not None:
        with open(output, "w") as f:
            f.write(str(blocks))
    return blocks

def decrypt_message(private_key:tuple, blocks:list, output=None)->str:
    plain = ""
    for c in blocks:
        d = decrypt(private_key, c)
        p = chr(d)
        plain += p
    if output is not None:
        with open(output, "w") as f:
            f.write(plain)
    return plain

def decrypt_file(private_key:tuple, file:str, output=None)->str:
    with open(file, "r") as f:
        blocks = eval(f.read())
    decrypted = decrypt_message(private_key, blocks)
    if output is not None:
        with open(output, "w") as f:
            f.write(decrypted)
    return decrypted , output       

def encrypt_file(public_key:tuple, input_file:str, output_file=None):
    with open(input_file, "r") as f:
        msg = f.read()
    blocks = encrypt_message(public_key, msg)
    if output_file is not None:
        with open(output_file, "w") as f:
            f.write(str(blocks))
    return blocks, output_file