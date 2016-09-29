from __future__ import absolute_import, division, print_function, unicode_literals

import os
import base64
import credsmash.aes_ctr
import credsmash.aes_gcm


class DummyKeyService(object):
    def generate_key_data(self, number_of_bytes):
        key = os.urandom(int(number_of_bytes))
        return key, base64.b64encode(key)

    def decrypt(self, encoded_key):
        return base64.b64decode(encoded_key)


def test_aes_ctr_legacy():
    """
    Basic test to ensure `cryptography` is installed/working
    """
    key_service = DummyKeyService()

    plaintext = b'abcdefghi'
    material = credsmash.aes_ctr.seal_aes_ctr_legacy(
        key_service,
        plaintext
    )
    recovered_plaintext = credsmash.aes_ctr.open_aes_ctr_legacy(
        key_service, material
    )
    assert plaintext == recovered_plaintext


def test_aes_ctr():
    key_service = DummyKeyService()

    plaintext = b'abcdefghi'
    material = credsmash.aes_ctr.seal_aes_ctr(
        key_service,
        plaintext
    )
    recovered_plaintext = credsmash.aes_ctr.open_aes_ctr(
        key_service, material
    )
    assert plaintext == recovered_plaintext


def test_aes_gcm():
    key_service = DummyKeyService()

    plaintext = b'abcdefghi'
    material = credsmash.aes_gcm.seal_aes_gcm(
        key_service,
        plaintext
    )
    recovered_plaintext = credsmash.aes_gcm.open_aes_gcm(
        key_service, material
    )
    assert plaintext == recovered_plaintext

