from Crypto import Random
from Crypto.PublicKey import RSA
import base64

class GPG_Functions:
    # Generates the keys we need
    def createKeys():
        # RSA modulus length must be a multiple of 256 and >= 1024
        modulus_length = 256*4 # use larger value in production
        privatekey = RSA.generate(modulus_length, Random.new().read)
        publickey = privatekey.publickey()
        return privatekey, publickey

# ------------------------------------------
    def Encryptor(key, data):
        encrypted_msg = key.encrypt(data, 32)[0]
        message = base64.b64encode(encrypted_msg) # base64 encoded strings are database friendly
        return message

    def Decryptor(key, data):
        message = base64.b64decode(data)
        message = key.decrypt(message)
        return message

    def sign(key, data):
        signed_data = gpg.sign(data, key)
        return str(signed_data)

    def verify(key, data):
        verified = gpg.verify(data, key)
        return verified