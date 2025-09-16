P = 2
Q = 11
e=7
d=3
alphabet="1234567890"
N = P*Q
euler_function=(P-1)*(Q-1)

def encrypt(text):
    c_list = []
    for i in range(text.__len__()):
        c_list.append(str((int(text[i]) ** e) % N))
    return c_list

def decrypt(enc_text):
    m_list = []
    for i in range(enc_text.__len__()):
        m_list.append(str((int(enc_text[i]) ** d) % N))
    return m_list

def check_txt(org_txt, dec_txt):
    if org_txt == dec_txt:
        print('Good Code\n')
    else:
        print('Bad Code\n')

print(alphabet)
print(" ".join(encrypt(alphabet)))
res = "".join(decrypt(encrypt(alphabet)))
print(res)

check_txt(alphabet, res)

alphabet = "12022005"
print(alphabet)
print(" ".join(encrypt(alphabet)))
res = "".join(decrypt(encrypt(alphabet)))
print(res)

check_txt(alphabet, res)
