with open("binary.bin", "wb") as binary:
    binary.write(b"54678890kf")
with open("binary.bin", "ab") as binary:
    binary.write(b"54678890kf")
with open("binary.bin", "rb") as binary:
    readd = binary.read()
    print(readd)

with open("binary.bin", "wb+") as binary:
    binary.write(b"54678890kf")
with open("binary.bin", "rb+") as binary:
    readd = binary.read()
    print(readd)