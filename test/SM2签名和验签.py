from tongsuopy.crypto import hashes, serialization
from tongsuopy.crypto.asymciphers import ec

msg = b"hello"
key = ec.generate_private_key(ec.SM2())

pem = key.public_key().public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo,
)
pubkey = serialization.load_pem_public_key(pem)

signature = key.sign(msg, ec.ECDSA(hashes.SM3()))
pubkey.verify(signature, msg, ec.ECDSA(hashes.SM3()))