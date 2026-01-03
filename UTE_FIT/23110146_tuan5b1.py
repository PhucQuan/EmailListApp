#bai 1 
gia_co_so = 4.0
gia_cong_them = 0.25

def tinh_tientaxi(km):
    if km <= 0:
        return 0
    tongtien = gia_co_so + gia_cong_them * int(km/0.14)
    return tongtien


#bai 2 : viet chuong trinh tinh trung vi cua 3 diem,hay dinh nghia mot ham nhan
#  3 tham so ngo vao va tra ve ket qua la so trung vi cac diem da nhan

def trung_vi(a,b,c):
    if (a <= b <= c) or (c <= b <= a):
        return b    
    elif (b <= a <= c) or (c <= a <= b):
        return a
    else:
        return c
print("trung vi cua 3 diem la: ", trung_vi(3,1,2))

# bai 3 : kiem tra so nguyen to 
def kt_snt(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False    
    return True
print("kiem tra so nguyen to: ", kt_snt(11))


#bai 4 : 
n = int(input("nhap so n: "))
def in_snt(n):
    k = n + 1
    while True:
        if kt_snt(k):
            return k
        k += 1


#bai 5
def is_strong_password(pw: str) -> bool:
    return (len(pw) >= 8
            and any(c.islower() for c in pw)
            and any(c.isupper() for c in pw)
            and any(c.isdigit() for c in pw))

def main():
    pw = input("Nhập mật khẩu: ")
    if is_strong_password(pw):
        print("Mật khẩu mạnh")
    else:
        print("Mật khẩu yếu")

if __name__ == "__main__":
    main()



#bai 6
def to_decimal(num_str, base):
    try:
        return int(num_str, base)
    except ValueError:
        return None

def from_decimal(num, base):
    if base == 2:
        return bin(num)[2:]
    elif base == 16:
        return hex(num)[2:]
    elif base == 10:
        return str(num)
    else:
        return None

def main():
    num_str = input("Nhập số: ")
    base_from = int(input("Nhập hệ gốc (2, 10, 16): "))
    base_to = int(input("Nhập hệ muốn đổi (2, 10, 16): "))

    dec = to_decimal(num_str, base_from)
    if dec is None:
        print("Số không hợp lệ trong hệ", base_from)
    else:
        result = from_decimal(dec, base_to)
        if result is None:
            print("Không hỗ trợ hệ", base_to)
        else:
            print("Kết quả:", result)

if __name__ == "__main__":
    main()


#bai 7
def kiemtra_tietkiem(dien):
    if dien < 10:
        print("Thiết bị tiết kiệm điện")
    else:
        print("Thiết bị không tiết kiệm điện")

kiemtra_tietkiem(8)
kiemtra_tietkiem(15)

#bai 8
def so_sao(dien):
    if dien < 10: return 5
    elif dien < 20: return 4
    elif dien < 30: return 3
    elif dien < 40: return 2
    else: return 1

print(so_sao(8))   # 5
print(so_sao(25))  # 3

#bai 9
def kiemtra_tietkiem_dien(dien):
    stars = so_sao(dien)
    if stars < 3:
        print("Thiết bị không tiết kiệm điện")
    else:
        print("Thiết bị tiết kiệm điện")

kiemtra_tietkiem_dien(35)



def filter_speeds(speeds, min_val):
    result = [(i, v) for i, v in enumerate(speeds) if v < min_val]
    return result

print(filter_speeds([100, 200, 50, 300, 80], 150))
# 👉 [(0, 100), (2, 50), (4, 80)]


#bai 11

import math

def solve_quadratic(a, b, c):
    if a == 0:  # bậc 1
        return [] if b == 0 else [-c/b]
    delta = b*b - 4*a*c
    if delta < 0:
        return []
    elif delta == 0:
        return [-b/(2*a)]
    else:
        sqrt_d = math.sqrt(delta)
        return [(-b+sqrt_d)/(2*a), (-b-sqrt_d)/(2*a)]

print(solve_quadratic(1, -3, 2))  # [2.0, 1.0]

#bai 12
import math

def cos_taylor(x, epsilon=1e-6):
    n = 0
    term = 1.0  # số hạng đầu
    result = 0.0
    while abs(term) > epsilon:
        term = ((-1)**n) * (x**(2*n)) / math.factorial(2*n)
        result += term
        n += 1
    return result

print(cos_taylor(math.pi/3))   # ~0.5
print(math.cos(math.pi/3))     # 0.5


#bai 13
def capitalize_words(s: str) -> str:
    return " ".join(word.capitalize() for word in s.split())

print(capitalize_words("nGuyeN hiEu NGhiA"))  # "Nguyen Hieu Nghia"
