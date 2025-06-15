"""
jia.py
甲方操作脚本
- 取密钥、明文、IV等参数。
- 用乙方公钥加密SM4密钥。
- 用SM4密钥和IV加密明文。
- 计算明文哈希SM3(Message)。
- 用甲方私钥对哈希SM2签名。
"""
import binascii

from tongsuopy.crypto.ciphers import Cipher, algorithms, modes
from tongsuopy.crypto import serialization
from tongsuopy.crypto.asymciphers import ec
from gmssl import sm2, func
from cryptography.hazmat.primitives import serialization as crypto_serialization

key = ""
iv = "5072656E7469636548616C6C496E632E" # 实践项目指定的IV
plaintext = "" # 读取Message(课程实践3-待选论文).zip文件内容
ciphertext = ""
with open('./jia_knowledge/Message(课程实践3-待选论文).zip',"rb") as f:
    plaintext = f.read()
    # print(plaintext)

yi_public_key = ""
with open('./jia_knowledge/yi_public_key.pem', 'rb') as f:
    yi_public_key = f.read()
    # print(yi_public_key)

with open('./jia_knowledge/sm4_key.bin', 'rb') as f:
    key = f.read()
# 加载PEM格式公钥为对象
# !!!tongsuo1.0.2才支持PEM格式的SM2公钥加载，到2025/6/14为止，还没有支持。换用gmssl。
pubkey_obj = crypto_serialization.load_pem_public_key(yi_public_key)
# 因为gmssl库的SM2加密接口要求公钥必须是64字节的十六进制字符串，格式为X坐标+Y坐标，而不是PEM格式或对象。
# 导出为数字（点坐标），再转hex字符串
# public_numbers = pubkey_obj.public_numbers()
# x = format(public_numbers.x, '064x')
# y = format(public_numbers.y, '064x')
# yi_public_key_hex = x + y  # 64字节hex字符串

# sm2加密sm4_key
sm2_crypt = sm2.CryptSM2(public_key=yi_public_key_hex, private_key=None)
sm4_key_ciphertext = sm2_crypt.encrypt(key)

# 放入乙方文件夹=>加密后的SM4密钥网络通信传递给乙方 
with open('./jia_knowledge/sm4_key_ciphertext.bin', 'wb') as f:
    f.write(sm4_key_ciphertext)

