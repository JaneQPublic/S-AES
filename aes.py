import re
import random

S_BOX =[[0x9, 0x4, 0xA, 0xB],
        [0xD, 0x1, 0x8, 0x5],
        [0x6, 0x2, 0x0, 0x3],
        [0xC, 0xE, 0xF, 0x7]]
S_BOX_t =[[0xA, 0x5, 0x9, 0xB],
        [0x1, 0x7, 0x8, 0xF],
        [0x6, 0x0, 0x2, 0x3],
        [0xC, 0x4, 0xD, 0xE]]
gf16_add = [[0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0xA, 0xB, 0xC, 0xD, 0xE, 0xF],
            [0x1, 0x0, 0x3, 0x2, 0x5, 0x4, 0x7, 0x6, 0x9, 0x8, 0xB, 0xA, 0xD, 0xC, 0xF, 0xE],
            [0x2, 0x3, 0x0, 0x1, 0x6, 0x7, 0x4, 0x5, 0xA, 0xB, 0x8, 0x9, 0xE, 0xF, 0xC, 0xD],
            [0x3, 0x2, 0x1, 0x0, 0x7, 0x6, 0x5, 0x4, 0xB, 0xA, 0x9, 0x8, 0xF, 0xE, 0xD, 0xC],
            [0x4, 0x5, 0x6, 0x7, 0x0, 0x1, 0x2, 0x3, 0xC, 0xD, 0xE, 0xF, 0x8, 0x9, 0xA, 0xB],
            [0x5, 0x4, 0x7, 0x6, 0x1, 0x0, 0x3, 0x2, 0xD, 0xC, 0xF, 0xE, 0x9, 0x8, 0xB, 0xA],
            [0x6, 0x7, 0x4, 0x5, 0x2, 0x3, 0x0, 0x1, 0xE, 0xF, 0xC, 0xD, 0xA, 0xB, 0x8, 0x9],
            [0x7, 0x6, 0x5, 0x4, 0x3, 0x2, 0x1, 0x0, 0xF, 0xE, 0xD, 0xC, 0xB, 0xA, 0x9, 0x8],
            [0x8, 0x9, 0xA, 0xB, 0xC, 0xD, 0xE, 0xF, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7],
            [0x9, 0x8, 0xB, 0xA, 0xD, 0xC, 0xF, 0xE, 0x1, 0x0, 0x3, 0x2, 0x5, 0x4, 0x7, 0x6],
            [0xA, 0xB, 0x8, 0x9, 0xE, 0xF, 0xC, 0xD, 0x2, 0x3, 0x0, 0x1, 0x6, 0x7, 0x4, 0x5],
            [0xB, 0xA, 0x9, 0x8, 0xF, 0xE, 0xD, 0xC, 0x3, 0x2, 0x1, 0x0, 0x7, 0x6, 0x5, 0x4],
            [0xC, 0xD, 0xE, 0xF, 0x8, 0x9, 0xA, 0xB, 0x4, 0x5, 0x6, 0x7, 0x0, 0x1, 0x2, 0x3],
            [0xD, 0xC, 0xF, 0xE, 0x9, 0x8, 0xB, 0xA, 0x5, 0x4, 0x7, 0x6, 0x1, 0x0, 0x3, 0x2],
            [0xE, 0xF, 0xC, 0xD, 0xA, 0xB, 0x8, 0x9, 0x6, 0x7, 0x4, 0x5, 0x2, 0x3, 0x0, 0x1],
            [0xF, 0xE, 0xD, 0xC, 0xB, 0xA, 0x9, 0x8, 0x7, 0x6, 0x5, 0x4, 0x3, 0x2, 0x1, 0x0]]
gf16_mix = [[0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0],
            [0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0xA, 0xB, 0xC, 0xD, 0xE, 0xF],
            [0x0, 0x2, 0x4, 0x6, 0x8, 0xA, 0xC, 0xE, 0x3, 0x1, 0x7, 0x5, 0xB, 0x9, 0xF, 0xD],
            [0x0, 0x3, 0x6, 0x5, 0xC, 0xF, 0xA, 0x9, 0xB, 0x8, 0xD, 0xE, 0x7, 0x4, 0x1, 0x2],
            [0x0, 0x4, 0x8, 0xC, 0x3, 0x7, 0xB, 0xF, 0x6, 0x2, 0xE, 0xA, 0x5, 0x1, 0xD, 0x9],
            [0x0, 0x5, 0xA, 0xF, 0x7, 0x2, 0xD, 0x8, 0xE, 0xB, 0x4, 0x1, 0x9, 0xC, 0x3, 0x6],
            [0x0, 0x6, 0xC, 0xA, 0xB, 0xD, 0x7, 0x1, 0x5, 0x3, 0x9, 0xF, 0xE, 0x8, 0x2, 0x4],
            [0x0, 0x7, 0xE, 0x9, 0xF, 0x8, 0x1, 0x6, 0xD, 0xA, 0x3, 0x4, 0x2, 0x5, 0xC, 0xB],
            [0x0, 0x8, 0x3, 0xB, 0x6, 0xE, 0x5, 0xD, 0xC, 0x4, 0xF, 0x7, 0xA, 0x2, 0x9, 0x1],
            [0x0, 0x9, 0x1, 0x8, 0x2, 0xB, 0x3, 0xA, 0x4, 0xD, 0x5, 0xC, 0x6, 0xF, 0x7, 0xE],
            [0x0, 0xA, 0x7, 0xD, 0xE, 0x4, 0x9, 0x3, 0xF, 0x5, 0x8, 0x2, 0x1, 0xB, 0x6, 0xC],
            [0x0, 0xB, 0x5, 0xE, 0xA, 0x1, 0xF, 0x4, 0x7, 0xC, 0x2, 0x9, 0xD, 0x6, 0x8, 0x3],
            [0x0, 0xC, 0xB, 0x7, 0x5, 0x9, 0xE, 0x2, 0xA, 0x6, 0x1, 0xD, 0xF, 0x3, 0x4, 0x8],
            [0x0, 0xD, 0x9, 0x4, 0x1, 0xC, 0x8, 0x5, 0x2, 0xF, 0xB, 0x6, 0x3, 0xE, 0xA, 0x7],
            [0x0, 0xE, 0xF, 0x1, 0xD, 0x3, 0x2, 0xC, 0x9, 0x7, 0x6, 0x8, 0x4, 0xA, 0xB, 0x5],
            [0x0, 0xF, 0xD, 0x2, 0x9, 0x6, 0x4, 0xB, 0x1, 0xE, 0xC, 0x3, 0x8, 0x7, 0x5, 0xA]]

# 二进制转状态矩阵
def binary_to_hex_matrix(binary):
    # 将二进制数按照4位进行分组
    groups = [binary[i:i+4] for i in range(0, len(binary), 4)]
    # 将每个分组转换为十六进制表示
    hex_matrixs = [hex(int(group, 2))[2:] for group in groups]

    # 创建状态矩阵
    matrix = [[0 for i in range(2)] for j in range(2)]
    matrix[0][0] = hex_matrixs[0]
    matrix[1][0] = hex_matrixs[1]
    matrix[0][1] = hex_matrixs[2]
    matrix[1][1] = hex_matrixs[3]
    return matrix

# 状态矩阵转二进制
def hex_matrix_to_binary(hex_matrix):
    num = ""
    for i in range(2):
        for j in range(2):
            bin_num = bin(hex_matrix[j][i])
            num += bin_num[2:].zfill(4)
    return num

# 整数转换为n位二进制
def int_to_bin(key, n):
    return bin(int(key))[2:].rjust(n, '0')

# 二进制转换为整数
def bin_to_int(binary):
    return int(binary, 2)

# 将每个ASCII字符转换为对应的n位二进制字符，并添加到列表中
def ascii_to_bin_groups(ascii_string,n):
    binary_groups = []  # 用于存储n位二进制字符的列表
    for char in ascii_string:
        ascii_char = ord(char)
        binary_char = bin(ascii_char)[2:].rjust(n, '0')
        binary_groups.append(binary_char)
    return binary_groups

# 将n位二进制字符串转换为对应的ASCII字符
def bin_to_ascii(binary_string,n):
   # 将二进制字符串分割为长度为8的子字符串
   binary_list = [binary_string[i:i + n] for i in range(0, len(binary_string), n)]
   # 将每个子字符串转换为十进制数，并将其转换为对应的ASCII字符
   ascii_string = ''.join(chr(int(binary, 2)) for binary in binary_list)
   return ascii_string

# 判断输入的明/密文是否为二进制字符，若不是则转换为二进制
def is_bin_string(key):
    # 定义正则表达式模式，表示只包含0和1的字符串
    a_bin = r'^[01]+$'
    # 使用re.match()来匹配字符串
    match = re.match(a_bin, key)
    # 如果匹配成功，说明是二进制字符串，返回True；否则返回False
    if match:
        # print("输入的是二进制字符串")
        return True
    else:
        # print("输入的是ASCII字符串")
        return False
    
# 按位异或,输入二进制数
def xor(a, b):
    xor_result = ''
    for i, j in zip(a, b):
        if int(i) == int(j):
            xor_result += '0'
        else:
            xor_result += '1'
    return xor_result

# 密钥加，逆函数为本身
def add_key(x, key):
    out = xor(x, key)
    return out

# 半字节替代，index判断调用S盒或逆S盒, x为半字节二进制字符串
def s_box(x, index):
    a = int(x[0:2], 2)
    b = int(x[2:4], 2)
    if index == 0:  # S盒
        y = S_BOX[a][b]
    elif index == 1:  # 逆S盒
        y = S_BOX_t[a][b]
    return y

# 行移位，逆函数为本身
def shift_rows(x):
    temp = x[1][0]
    x[1][0] = x[1][1]
    x[1][1] = temp
    return x

# G（16）加法
def add_gef16(a, b):
    if type(a) == str:
        a = int(a, 16)
    if type(b) == str:
        b = int(b, 16)
    result = gf16_add[a][b]
    return result

# G（16）乘法
def mix_gef16(a, b):
    if type(a) == str:
        a = int(a, 16)
    if type(b) == str:
        b = int(b, 16)
    result = gf16_mix[a][b]
    return result

# 列混淆
def mix_columns(matrix):
    new_matrix = [[0 for i in range(2)] for j in range(2)]
    new_matrix[0][0] = add_gef16(matrix[0][0], mix_gef16(4, matrix[1][0]))
    new_matrix[0][1] = add_gef16(matrix[0][1], mix_gef16(4, matrix[1][1]))
    new_matrix[1][0] = add_gef16(mix_gef16(4, matrix[0][0]), matrix[1][0])
    new_matrix[1][1] = add_gef16(mix_gef16(4, matrix[0][1]), matrix[1][1])
    return new_matrix

# 逆列混淆
def n_mix_columns(matrix):
    new_matrix = [[0 for i in range(2)] for j in range(2)]
    new_matrix[0][0] = add_gef16(mix_gef16(9, matrix[0][0]), mix_gef16(2, matrix[1][0]))
    new_matrix[0][1] = add_gef16(mix_gef16(9, matrix[0][1]), mix_gef16(2, matrix[1][1]))
    new_matrix[1][0] = add_gef16(mix_gef16(2, matrix[0][0]), mix_gef16(9, matrix[1][0]))
    new_matrix[1][1] = add_gef16(mix_gef16(2, matrix[0][1]), mix_gef16(9, matrix[1][1]))
    return new_matrix

# 密钥扩展
def get_keys(key):
    w0 = key[0:8]
    w1 = key[8:16]

    w2 = xor(xor(w0, "10000000"), g(w1))
    w3 = xor(w2, w1)
    w4 = xor(xor(w2, "00110000"), g(w3))
    w5 = xor(w4, w3)
    return w0, w1, w2, w3, w4, w5

# 密钥扩展中g函数
def g(w):
    w0 = w[0:4]
    w1 = w[4:8]
    w0 = bin(s_box(w0, 0))[2:].zfill(4)
    w1 = bin(s_box(w1, 0))[2:].zfill(4)
    new_g = w1 + w0
    return new_g

# 加密
def en(plain, key, index):
    if index == 1:
        # print("基础加密")
        w0, w1, w2, w3, w4, w5 = get_keys(key)
        xor_result = xor(plain, key)  # 异或
        # 第一轮加密
        matrix = binary_to_hex_matrix(xor_result)
        for i in range(2):
            for j in range(2):
                if type(matrix[i][j]) == str:
                    matrix[i][j] = int(matrix[i][j], 16)
                matrix[i][j] = s_box(bin(matrix[i][j])[2:].zfill(4), 0)  # S盒替换
        matrix = shift_rows(matrix)  # 行位移
        matrix = mix_columns(matrix)  # 列混淆
        result = xor(hex_matrix_to_binary(matrix), w2 + w3)
        matrix = binary_to_hex_matrix(result)

        # 第二轮加密
        for i in range(2):
            for j in range(2):
                if type(matrix[i][j]) == str:
                    matrix[i][j] = int(matrix[i][j], 16)
                matrix[i][j] = s_box(bin(matrix[i][j])[2:].zfill(4), 0)  # S盒替换
        matrix = shift_rows(matrix)  # 行位移
        x = hex_matrix_to_binary(matrix)
        result = xor(x, w4 + w5)  # 异或
        return result
    
    elif index == 2:  # 双重加密
        # print("双重加密")
        key1 = key[0:16]
        key2 = key[16:32]
        temp = en(plain, key1, 1)
        return en(temp, key2, 1)
    
    elif index == 3:  # 三重加密
        # print("三重加密")
        key1 = key[0:16]
        key2 = key[16:32]
        key3 = key[32:48]
        temp = en(plain, key1, 1)
        temp = en(temp, key2, 1)
        return en(temp, key3, 1)
    
def encrypt(plain0, key, index):
    results = []
    
    if not is_bin_string(plain0):
        if type(plain0) == int:
            plain = [int_to_bin(plain0, 16)]
        else:
            plain_group = ascii_to_bin_groups(plain0,16)

        for item in plain_group:
            result = en(item, key, index)
            result = result if is_bin_string(plain0) else bin_to_ascii(result,16)
            results.append(result)
    else:
        plain = plain0
        result = en(plain, key, index)
        result = result if is_bin_string(plain0) else bin_to_ascii(result,16)
        results.append(result)
    out = ''
    for item in results:
        out += item
    # print("转换后的加密为:",out)
    return out

def de(cipher, key, index):
    if index == 1:
        w0, w1, w2, w3, w4, w5 = get_keys(key)
        xor_result = xor(cipher, w4 + w5)  # 异或
        # 第一轮解密
        matrix = binary_to_hex_matrix(xor_result)
        matrix = shift_rows(matrix)  # 逆行移位
        for i in range(2):
            for j in range(2):
                if type(matrix[i][j]) == str:
                    matrix[i][j] = int(matrix[i][j], 16)
                matrix[i][j] = s_box(bin(matrix[i][j])[2:].zfill(4), 1)  # 逆S盒替换
        matrix = xor(hex_matrix_to_binary(matrix), w2 + w3)
        matrix = binary_to_hex_matrix(matrix)
        matrix = n_mix_columns(matrix)  # 逆列混淆

        # 第二轮解密
        matrix = shift_rows(matrix)  # 逆行移位
        for i in range(2):
            for j in range(2):
                if type(matrix[i][j]) == str:
                    matrix[i][j] = int(matrix[i][j], 16)
                matrix[i][j] = s_box(bin(matrix[i][j])[2:].zfill(4), 1)  # 逆S盒替换
        x = hex_matrix_to_binary(matrix)
        result = xor(x, w0 + w1)  # 异或
        return result
    
    elif index == 2:  # 双重解密
        # print("双重解密")
        key1 = key[0:16]
        key2 = key[16:32]
        temp = de(cipher, key2, 1)
        return de(temp, key1, 1)
    
    elif index == 3:  # 三重解密
        # print("三重解密")
        key1 = key[0:16]
        key2 = key[16:32]
        key3 = key[32:48]
        temp = de(cipher, key3, 1)
        temp = de(temp, key2, 1)
        return de(temp, key1, 1)
    
def decrypt(cipher, key, index):
    results = []
    if not is_bin_string(cipher):
        if type(cipher) == int:
            cipher = [int_to_bin(cipher, 16)]
        else:
            cipher_group = ascii_to_bin_groups(cipher,16)

        for item in cipher_group:
            result = de(item, key, index)
            result = result if is_bin_string(cipher) else bin_to_ascii(result,16)
            results.append(result)
    else:
        result = de(cipher, key, index)
        result = result if is_bin_string(cipher) else bin_to_ascii(result,16)
        results.append(result)
    out = ''
    for item in results:
        out += item
    # print("密文的原文为:",out)
    return out

# 扩展：
# 中间相遇攻击
def middle_attack(plain, cipher):
    possible_keys = []

    for k1 in range(2**16):
        key1 = int_to_bin(k1, 16)
        # 对明文进行加密
        cipher1 = encrypt(plain, key1, 1)
        possible_keys.append((key1, cipher1))

    # 对密文进行排序
    possible_keys.sort(key=lambda x: x[1])
    for k2 in range(2**16):
        key2 = int_to_bin(k2, 16)
        # 对密文进行解密
        cipher2 = decrypt(cipher, key2, 1)
        
        # 在加密结果中搜索解密结果
        for key1, cipher1 in possible_keys:
            if cipher2 == cipher1:
                return key1 +" "+ key2
    return None



#密码分组链(CBC)模式：
def CBC_encrypt(plain, key,index):
    iv = ""
    for _ in range(16):
        iv += str(random.randint(0, 1))

    cipher = ""
    previous_cipher = iv
    for i in range(0, len(plain), 16):
        block = plain[i:i+16] #每16个一组进行加密
        xored_block = xor(block, previous_cipher)
        encrypted_block = en(xored_block, key, index)
        cipher += encrypted_block
        previous_cipher = encrypted_block
        
    return iv + cipher #更新向量

def CBC_decrypt(cipher, key, index):
    iv = cipher[:16]
    cipher = cipher[16:]
    plain = ""
    previous_cipher = iv

    for i in range(0, len(cipher), 16):
        block = cipher[i:i+16] 
        decrypted_block = de(block, key,index)
        plain += xor(decrypted_block, previous_cipher)
        previous_cipher = block

    return plain

# 对密文分组进行篡改
def tamper_cipher(cipher, index, new_block):
    cipher = list(cipher)
    cipher[index:index+16] = new_block
    return "".join(cipher)


if __name__ == '__main__' :
    # plain='1100110011001100'
    plain='hello'
    cipher = '0111111111111000'
    key1='1010101010101010'
    key2='0000000000000000'
    key3='1111111111111111'

    print("------------基础加密------------")
    cipher1=encrypt(plain, key1, 1)
    plain1=decrypt(cipher1, key1, 1)
    print("加密为",cipher1,"\n解密为",plain1)

    print("------------双重加密------------")
    cipher2=encrypt(plain1, key1+key2, 2)
    plain2=decrypt(cipher2, key1+key2, 2)
    print("加密为",cipher2,"\n解密为",plain2)

    print("------------中间相遇攻击------------")
    key = middle_attack(plain2, cipher2)
    print("找到的密钥为:", key)

    print("------------三重加密------------")
    cipher3=encrypt(plain2, key1+key2+key3, 3)
    plain3=decrypt(cipher3,  key1+key2+key3, 3)
    print("加密为",cipher3,"\n解密为",plain3)
    

    plain='000000000000000011111111111111111010101010101010' #明长文
    cipher='1101111111010010000000100110100101010111101100111100100001010110'
    print("------------CBC基础加密------------")
    cipher1=CBC_encrypt(plain, key1, 1)
    plain1=CBC_decrypt(cipher1, key1, 1)
    print("加密为",cipher1,"\n解密为",plain1)
    print("------------CBC双重加密------------")
    cipher2=CBC_encrypt(plain1, key1+key2, 2)
    plain2=CBC_decrypt(cipher2, key1+key2, 2)
    print("加密为",cipher2,"\n解密为",plain2)
    print("------------CBC三重加密------------")
    cipher3=CBC_encrypt(plain2, key1+key2+key3, 3)
    plain3=CBC_decrypt(cipher3,  key1+key2+key3, 3)
    print("加密为",cipher3,"\n解密为",plain3)

    print("------------篡改密文分组------------")
    new_block='0101010101010101'
    cipher_distort=tamper_cipher(cipher, 2, new_block)
    plain_distort=CBC_decrypt(cipher_distort, key1+key2+key3, 3)
    print("篡改前解密为",plain3,"\n篡改后解密为",plain_distort)