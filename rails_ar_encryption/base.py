from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Hash import SHA1
from Crypto.Protocol.KDF import PBKDF2


def decrypt(message, key):
    """
    Decrypt message just like it's done on Rails side, see:
    https://github.com/rails/rails/blob/main/activerecord/lib/active_record/encryption/cipher/aes256_gcm.rb
    """
    headers = message["h"]

    ciphertext = b64decode(message["p"])
    nonce = b64decode(headers["iv"])
    tag = b64decode(headers["at"])

    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)

    return cipher.decrypt_and_verify(ciphertext, tag).decode()


def derive_key(password, salt):
    """
    Derive the key just like it's done on Rails side, see:
    https://github.com/rails/rails/blob/main/activesupport/lib/active_support/key_generator.rb#L39
    """
    return PBKDF2(password, salt, 32, count=2**16, hmac_hash_module=SHA1)
