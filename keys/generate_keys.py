import rsa


def generate_key_pair():
    """Generate a public/private key pair"""
    return rsa.newkeys(2048, poolsize=2)


def save_key_pair(pubkey, privkey, filename):
    """Saves the public/private key pair to a file"""
    with open(filename, "wb") as f:
        f.write(pubkey.save_pkcs1())
        f.write(privkey.save_pkcs1())
        # f.write(privkey.save_pkcs1(passphrase="my_passphrase"))
    filename_pub = filename.replace(".", "_public.")
    with open(filename_pub, "wb") as fpub:
        fpub.write(pubkey.save_pkcs1())


def main():
    """Generates and saves a public/private key pair"""
    (pubkey, privkey) = generate_key_pair()
    save_key_pair(pubkey, privkey, "my_key_pair.pem")


if __name__ == "__main__":
    main()
