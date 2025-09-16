P=2
Q=11
e=7
d=3
alphabet="1234567890"
N=P*Q
euler_function=(P-1)*(Q-1)

def en_de_crypt(text, exp):
    ed_list = []
    for i in range(text.__len__()):
        ed_list.append(str((int(text[i]) ** exp) % N))
    return ed_list

def check_txt(org_txt, dec_txt):
    if org_txt == dec_txt:
        print('Good Code\n')
    else:
        print('Bad Code\n')

print(alphabet)
print(" ".join(en_de_crypt(alphabet, e)))
res = "".join(en_de_crypt(en_de_crypt(alphabet, e), d))
print(res)

check_txt(alphabet, res)

alphabet = "12022005"
print(alphabet)
print(" ".join(en_de_crypt(alphabet, e)))
res = "".join(en_de_crypt(en_de_crypt(alphabet, e), d))
print(res)

check_txt(alphabet, res)
