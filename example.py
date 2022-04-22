from rails_ar_encryption.base import derive_key, decrypt

# RUN TEST
password = "ptJvigCRrrlKX29kU4bx80FUmxmjUej0"
salt = "dMoxVXAxoRrnOutfiPyeYqtfMiFICTva"
message = {"p":"SY0Ky7wFH3i6s73Bi7LL2cI=","h":{"iv":"mr7kZJHH2DOYZDM6","at":"qlrSLDRNH0qpB9/ATlHbQg=="}}

key = derive_key(password, salt)
clear_text = decrypt(message, key)

print("Decrypted data is => {}".format(clear_text))
