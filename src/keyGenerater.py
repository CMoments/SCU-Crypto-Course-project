"""
KeyGenerator.py
- 生成甲、乙双方的SM2公钥和私钥
- 生成SM4密钥
"""
from tongsuopy.crypto import serialization
from tongsuopy.crypto.asymciphers import ec
import os

# 生成甲方SM2密钥对
jia_key = ec.generate_private_key(ec.SM2())
jia_public_key = jia_key.public_key()
jia_pem = jia_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)
jia_pem_pub = jia_public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# 生成乙方SM2密钥对
yi_key = ec.generate_private_key(ec.SM2())
yi_public_key = yi_key.public_key()
yi_pem = yi_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)
yi_pem_pub = yi_public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# 保存甲方密钥
os.makedirs("./jia_knowledge", exist_ok=True)
with open("./jia_knowledge/sm2_private_key.pem", "wb") as f:
    f.write(jia_pem)
with open("./jia_knowledge/sm2_public_key.pem", "wb") as f:
    f.write(jia_pem_pub)

# 保存乙方密钥
os.makedirs("./yi_knowledge", exist_ok=True)
with open("./yi_knowledge/sm2_private_key.pem", "wb") as f:
    f.write(yi_pem)
with open("./yi_knowledge/sm2_public_key.pem", "wb") as f:
    f.write(yi_pem_pub)

# 互相保存对方公钥（可选）
with open("./jia_knowledge/yi_public_key.pem", "wb") as f:
    f.write(yi_pem_pub)
with open("./yi_knowledge/jia_public_key.pem", "wb") as f:
    f.write(jia_pem_pub)

# 生成SM4密钥
sm4_key = os.urandom(16)
with open("./jia_knowledge/sm4_key.bin", "wb") as f:
    f.write(sm4_key)


