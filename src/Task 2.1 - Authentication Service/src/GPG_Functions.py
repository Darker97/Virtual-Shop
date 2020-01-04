import gpg

class GPG_Functions:
    # Generates the keys we need
    def createKeys(self):

        print("Creating Keys")

        input_data = gpg.gen_key_input(key_type="RSA", key_length=1024)
        key = gpg.gen_key(input_data)

        
        # Public key
        # gpg.export_keys(key)

        #Private Key
        # gpg.export_keys(key, True)

        return key

# ------------------------------------------
    def Encryptor(self, key, data):
        encrypted_data = gpg.encrypt(data, key)
        return str(encrypted_data)

    def Decryptor(self, key, data):
        decrypted_data = gpg.decrypt(data, key)
        return str(decrypted_data)

    def sign(self, key, data):
        signed_data = gpg.sign(data, key)
        return str(signed_data)

    def verify(self, key, data):
        verified = gpg.verify(data, key)
        return verified