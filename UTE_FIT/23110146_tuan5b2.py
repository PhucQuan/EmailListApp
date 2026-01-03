#in ra tất cả các kí tự trong 1 xâu kí tự
s = input("nhap ki tu bat ky: ")
for i in s:
    print(i)    
#bai 2 dao nguoc 1 xau ki tu
s = input("nhap ki tu bat ky: " )
s_dao =  ''.join(reversed(s))
print(s_dao)

#bai 3  tim so lan xuat hien cua mot chuoi con trong 1 xau ki tu
s = input("nhap ki tu bat ky: ")
sub = input("nhap chuoi con can dem: ")
print(s.count(sub))

#bai4 :kiem tra chuoi doi xung

def kiemtradoixung(s):
    s = s.lower().replace()
    return s == s[::-1]
k = input("nhap ki tu bat ky: ")
if kiemtradoixung(k):
    print("chuoi doi xung")

#bai 5 : loai bo cac ki tu trung nhau trong 1 xau ki tu
s = input("nhap ki tu bat ky: ")
kq = ""
for i in s:
    if i not in kq:
        kq += i
print(kq)

#bai 6 : chuyen doi ki tu hoa thanh ki tu thuong va nguoc lai
s = input("nhap ki tu bat ky: ")
kq = ""
for i in s:
    if i.islower():
        kq += i.upper()
    else:
        kq += i.lower()
print(kq)

#bai 7 : viet chuogn trinh tim do dai cua xau ki tu
s = input("nhap ki tu bat ky: ")
print("do dai cua xau ki tu la: ", len(s))
#bai 8 : sap xep mot xau ki tu theo thu tu tang dan
s = input("nhap ki tu bat ky: ")
kq = ''.join(sorted(s, reverse = False))
#bai 9 tim xau con dai nhat khong chua cac ki tu trung lap
s = input("nhap ki tu bat ky: ")
kq = ""
for i in s:
    if i not in kq:
        kq += i
print(kq)
#bai 10 : tim ki tu xuat hien nhieu nhat trong xau ki tu
s = input("nhap ki tu bat ky: ")
max_kytu = ''
max_soluong = 0
for i in s:
    soluong = s.count(i)
    if soluong > max_soluong:
        max_soluong = soluong
        max_kytu = i
print("ky tu xuat hien nhieu nhat la: ", max_kytu, "voi so lan xuat hien la: ", max_soluong)
#baii 12 : dem so tu trong xau ki tu
s = input("nhap ki tu bat ky: ")
words = s.split()   
print("so tu trong xau ki tu la: ", len(words))

#bai 13 : kiem tra mot xau ki tu co phai la dao nguoc cua xau ki tu khac hay khong
s1 = input("nhap ki tu bat ky: ")
s2 = input("nhap ki tu bat ky: ")
def kiemtra_dao_nguoc(s1, s2):
    return s1 == s2[::-1]
if kiemtra_dao_nguoc(s1, s2):
    print("s1 la dao nguoc cua s2")
else:
    print("s1 khong phai la dao nguoc cua s2")
#bai 14 : tao mot xau ki tu moi bang cach thay the cac ki tu trong mot xau ki tu bang mot ki tu khac
s = input("nhap ki tu bat ky: ")
old_char = input("nhap ki tu can thay the: ")
new_char = input("nhap ki tu thay the: ")
kq = s.replace(old_char, new_char)
print(kq)
#bai 15 : tim tat ca xau con co do dai lon hon hoac bang gia tri cho truoc
s = input("nhap ki tu bat ky: ")
n = int(input("nhap do dai can tim: "))
words = s.split()
kq = [word for word in words if len(word) >= n]
print("cac xau con co do dai lon hon hoac bang", n, "la: ", kq)
#bai 16 : tim xau con dai nhat chua tat cac cac ki tu trong xau ki tu 
s = input("nhap ki tu bat ky: ")
words = s.split()
max_word = max(words, key=len)
print("xau con dai nhat la: ", max_word)
#bai 17 : tim tat cac cac xau con khac nhau trong xau ki tu
s = input("nhap ki tu bat ky: ")
words = s.split()
kq = set(words)
print("cac xau con khac nhau la: ", kq)
#bai 19 : chuyển đổi xâu kí tự thành mã ASCII
s = input("nhap ki tu bat ky: ")
kq = [ord(i) for i in s]
print("ma ASCII cua xau ki tu la: ", kq)

#bai 20
s = input("Nhập xâu ký tự: ")

so = hoa = thuong = dacbiet = 0

for ch in s:
    if ch.isdigit():
        so += 1
    elif ch.isupper():
        hoa += 1
    elif ch.islower():
        thuong += 1
    else:
        dacbiet += 1

print("Số:", so)
print("Chữ in hoa:", hoa)
print("Chữ thường:", thuong)
print("Ký tự đặc biệt:", dacbiet)

#bai 21 : dao nguoc xau ki tu
s = input("Nhập chuỗi: ")
print("Chuỗi đảo ngược:", s[::-1])

#bai 22
s = input("Nhập số CCCD: ")

if s.isdigit() and len(s) == 12:
    print("CCCD hợp lệ")
    matinh = s[:3]
    gioitinh = s[3]
    namsinh = s[4:6]
    dinhdanh = s[6:]

    print("Mã tỉnh:", matinh)
    print("Giới tính:", "Nam" if int(gioitinh) % 2 == 0 else "Nữ")
    print("Năm sinh (2 số cuối):", namsinh)
    print("Định danh:", dinhdanh)
else:
    print("CCCD không hợp lệ")


#bai 23
email = input("Nhập email: ")

if email.count('@') == 1:
    a, b = email.split('@')
    if '.' in b:
        ten, mien = b.split('.', 1)
        if a and ten and mien:
            print("Email hợp lệ")
        else:
            print("Email không hợp lệ")
    else:
        print("Email không hợp lệ")
else:
    print("Email không hợp lệ")


#bai 24
s = "An eye for an eye makes the whole world blind – Mahatma Gandhi"
words = s.lower().split()
freq = {}

for w in words:
    w = w.strip("–.,!?")  # bỏ dấu câu
    freq[w] = freq.get(w, 0) + 1

print(freq)


#bai 25
import string

pw = input("Nhập password: ")

if (len(pw) >= 8 
    and any(c.islower() for c in pw)
    and any(c.isupper() for c in pw)
    and any(c.isdigit() for c in pw)
    and any(c in string.punctuation for c in pw)):
    print("Password mạnh")
else:
    print("Password yếu")


#bai 26
import random, string

def strong_password(length=10):
    chars = string.ascii_letters + string.digits + string.punctuation
    while True:
        pw = ''.join(random.choice(chars) for _ in range(length))
        if (any(c.islower() for c in pw)
            and any(c.isupper() for c in pw)
            and any(c.isdigit() for c in pw)
            and any(c in string.punctuation for c in pw)):
            return pw

print("Password ngẫu nhiên:", strong_password())


#bai 27

s = "hello world"
print(s.title())   # "Hello World"

# translate: thay thế ký tự
bang = str.maketrans("abc", "123")  # a→1, b→2, c→3
print("abcxyz".translate(bang))     # "123xyz"

#bai 28
s = input("Nhập chuỗi: ")
n = len(s)
mid = n // 2
if n % 2 == 0:
    first, second = s[:mid], s[mid:]
else:
    first, second = s[:mid], s[mid+1:]

if first == second:
    print("Symmetrical")
else:
    print("Không symmetrical")


#bai 29
s = input("Nhập chuỗi: ")
words = s.split()
print(" ".join(words))
#bai 30
import re

def NegativeNumberInStrings(st):
    return re.findall(r'-\d+', st)

s = "abc-5xyz-12k9l--p"
print(NegativeNumberInStrings(s))  # ['-5', '-12']

#bai 31
s = input("Nhập chuỗi: ")
s = " ".join(s.split())
print(s.title())
#bai 32
import os

path = "D:\\music\\muabui.mp3"

filename = os.path.basename(path)       # muabui.mp3
name, ext = os.path.splitext(filename)  # muabui, .mp3

print("File:", filename)
print("Tên không đuôi:", name)


