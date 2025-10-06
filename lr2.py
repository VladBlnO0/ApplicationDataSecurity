a = 5
b = 7
m = 4096
y = 4003
n = 8

def rnd_init():
    global y
    y = 4003

def rnd():
    global y
    t = []
    for _ in range(n):
        y = (a * y + b) % m
        t.append(y % 256)
    return t

# === ENCODING/DECODING ===
def en_de_crypt(fin, fout):
    rnd_init()
    with open(fin, "rb") as fin:
        with open(fout, "wb") as fout:
            while True:
                data = fin.read(n)
                if not data:
                    break
                gamma = rnd()
                arr = []
                for i in range(len(data)):
                    arr.append(data[i] ^ gamma[i])
                fout.write(bytes(arr))

en_de_crypt("Source.txt", "Coded.txt")
en_de_crypt("Coded.txt", "DeCoded.txt")

print("Encryption and decryption complete")