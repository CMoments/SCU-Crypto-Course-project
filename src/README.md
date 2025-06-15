# 实践项目流程

### 密钥传递阶段

![示意图](C:\Users\ASUS\Desktop\SCU-Crypto\README.assets\示意图.png)

### 消息传递阶段

![Snipaste_2025-06-12_10-19-03](C:\Users\ASUS\Desktop\SCU-Crypto\README.assets\Snipaste_2025-06-12_10-19-03.png)

---

## 1. key_generater.py
**功能**：生成SM2密钥对、SM4密钥和IV，并保存到文件。  
**主要内容**：

- 使用 tongsuopy 生成SM2密钥对（甲、乙各一对）。
- 生成16字节SM4密钥和16字节IV
- Base64编码后写入对应txt文件。

---

## 2. jia.py
**功能**：甲方操作。  
**主要内容**：
- 读取SM4密钥、IV、明文、甲方私钥、乙方公钥。
- 用乙方公钥SM2加密SM4密钥，保存到文件。
- 用SM4密钥和IV加密明文，保存密文到文件。
- 用SM3对明文哈希，用甲方私钥SM2签名，保存签名到文件。

---

## 3. yi.py
**功能**：乙方操作。  
**主要内容**：
- 读取SM2加密的SM4密钥、密文、IV、签名、乙方私钥、甲方公钥。
- 用乙方私钥SM2解密SM4密钥。
- 用SM4密钥和IV解密密文，得到明文。
- 用SM3对明文哈希，用甲方公钥SM2验签。
- 校验明文一致性。

---

## 4. utils/sm2_util.py
**功能**：SM2相关操作的封装。  
**主要内容**：
- 密钥生成、保存、加载。
- 加解密、签名、验签等接口，底层调用tongsuopy。

---

## 5. utils/sm4_util.py
**功能**：SM4相关操作的封装。  
**主要内容**：
- 加密、解密接口，底层调用tongsuopy。

---

## 6. utils/sm3_util.py
**功能**：SM3哈希操作的封装。  
**主要内容**：
- 哈希计算接口，底层调用tongsuopy。

---

## 7. 其它
- `plain.txt`：明文
- `crypto.txt`：密文
- `sm4_key_encrypto.txt`：SM2加密后的SM4密钥
- `sm4_key_decrypto.txt`：SM2解密后的SM4密钥
- `sign.txt`：签名
- `message.txt`：解密得到的明文
- `iv.txt`：IV
- Pri_jia.txt/Pub_jia.txt/Pri_yi.txt/Pub_yi.txt：密钥

---

### 代码实现建议

- 每个utils文件只负责算法调用和数据转换，主流程文件负责参数解析和文件读写。
- tongsuopy的SM2/SM3/SM4接口用法可参考其官方文档或示例。
- 文件读写、Base64编码/解码、异常处理等可参考你原有项目。

---

**总结结构示例：**
```
project/
│
├─ key_generater.py      # 生成密钥和IV
├─ jia.py                # 甲方流程
├─ yi.py                 # 乙方流程
├─ utils/
│    ├─ sm2_util.py      # SM2工具
│    ├─ sm3_util.py      # SM3工具
│    └─ sm4_util.py      # SM4工具
├─ plain.txt
├─ crypto.txt
├─ sm4_key_encrypto.txt
├─ sm4_key_decrypto.txt
├─ sign.txt
├─ message.txt
├─ iv.txt
├─ Pri_jia.txt
├─ Pub_jia.txt
├─ Pri_yi.txt
└─ Pub_yi.txt
```

如需具体每个文件的代码模板或tongsuopy的调用示例，请告知！**