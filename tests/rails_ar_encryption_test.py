import pytest
from rails_ar_encryption.base import derive_key, decrypt


def test_derive_key_is_32_bits():
    key = derive_key("primary key", "key derivation salt")
    assert len(key) == 32


def test_decrypt_success():
    password = "ptJvigCRrrlKX29kU4bx80FUmxmjUej0"
    salt = "dMoxVXAxoRrnOutfiPyeYqtfMiFICTva"
    message = {
        "p": "SY0Ky7wFH3i6s73Bi7LL2cI=",
        "h": {"iv": "mr7kZJHH2DOYZDM6", "at": "qlrSLDRNH0qpB9/ATlHbQg=="},
    }

    key = derive_key(password, salt)

    assert decrypt(message, key) == "my_secret_message"


def test_decrypt_bad_tag_error():
    password = "ptJvigCRrrlKX29kU4bx80FUmxmjUej0"
    salt = "dMoxVXAxoRrnOutfiPyeYqtfMiFICTva"
    message = {
        "p": "SY0Ky7wFH3i6s73Bi7LL2cI=",
        "h": {"iv": "mr7kZJHH2DOYZDM6", "at": "d3JvbmcgdGFn"},
    }

    key = derive_key(password, salt)

    with pytest.raises(ValueError, match="MAC check failed"):
        decrypt(message, key)
