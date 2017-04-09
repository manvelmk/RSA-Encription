import random


"""Calculates Greatest Common Denominator"""
def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


"""Returns the multiplicative inverse of two numbers e and z"""
def mult_inverse(e, z):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_z = z

    while e > 0:
        temp1 = temp_z / e
        temp2 = temp_z - temp1 * e
        temp_z = e
        e = temp2
        x = x2 - temp1 * x1
        y = d - temp1 * y1
        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_z == 1:
        return d + z


"""Checks if the argument num is a prime number"""
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in xrange(3, int(num**0.5) + 2, 2):
        if num % n == 0:
            return False
    return True


"""Generates a key pair from the two prime numbers provided"""
def generate_keypair(p, q):
    n = p * q
    z = (p - 1) * (q - 1)
    e = random.randrange(1, z)

    # Check if the numbers are coprime
    g = find_gcd(e, z)
    while g != 1:
        e = random.randrange(1, z)
        g = find_gcd(e, z)

    d = mult_inverse(e, z)
    # Public key (e, n) and private key (d, n)
    return ((e, n), (d, n))


"""RSA Encryption"""
def encrypt(pk, plaintext):
    # Unpack the key into it's components
    key, n = pk
    # Apply RSA algorithm to each character's ASCII value of the plaintext
    cipher = [(ord(char) ** key) % n for char in plaintext]
    # Return the array of bytes (ciphertext)
    return cipher


"""RSA Decryption"""
def decrypt(pk, ciphertext):
    # Unpack the key into it's components
    key, n = pk
    # Reconstruct the plaintext from the ciphertext
    plain = [chr((char ** key) % n) for char in ciphertext]
    # Combine the characters into a string and return
    return ''.join(plain)


if __name__ == '__main__':
    print "RSA ENCRYPTION"
    menu = {}
    menu['1'] = "Test RSA"
    menu['2'] = "Encrypt"
    menu['3'] = "Decrypt"
    menu['4'] = "Exit"
    while True:
        options = menu.keys()
        options.sort()
        for entry in options:
            print entry, menu[entry]

        selection = raw_input("Please Select:")
        if selection == '1':
            p = int(raw_input("Enter first prime: "))
            if not is_prime(p):
                while not is_prime(p):
                    print "", p, " is not prime"
                    p = int(raw_input("Enter first prime: "))
            q = int(raw_input("Enter second prime: "))
            if not is_prime(q):
                while not is_prime(q):
                    print "", q, " is not prime"
                    q = int(raw_input("Enter second prime: "))
            print "Generating key pairs"
            public, private = generate_keypair(p, q)
            print "Public key: ", public, " Private key: ", private
            message = raw_input("Enter message to be encrypted: ")
            encrypted_msg = encrypt(private, message)
            print "ENCRYPTED: "
            print ''.join(map(lambda x: str(x), encrypted_msg))
            print "Decrypting with public key ", public
            print "DECRYPTED:"
            print decrypt(public, encrypted_msg)
        elif selection == '2':
            p = int(raw_input("Enter first prime: "))
            if not is_prime(p):
                while not is_prime(p):
                    print "", p, " is not prime"
                    p = int(raw_input("Enter first prime: "))
            q = int(raw_input("Enter second prime: "))
            if not is_prime(q):
                while not is_prime(q):
                    print "", q, " is not prime"
                    q = int(raw_input("Enter second prime: "))
            print "Generating key pairs"
            public, private = generate_keypair(p, q)
            print "Public key: ", public, " Private key: ", private
            message = raw_input("Enter message to be encrypted: ")
            encrypted_msg = encrypt(private, message)
            print "ENCRYPTED: "
            print ''.join(map(lambda x: str(x), encrypted_msg))
        elif selection == '3':
            ciphertxt = raw_input("Enter message to be decrypted: ")
            print "Enter the public keys: "
            public = map(int, input())
            public = tuple(public)
            print "Decrypting with public key ", public
            print "DECRYPTED:"
            print decrypt(public, ciphertxt)
        elif selection == '4':
            break
        else:
            print "Unknown Option Selected!"
