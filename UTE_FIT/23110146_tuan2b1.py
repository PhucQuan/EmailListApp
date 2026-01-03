#bai1 Nhap so nguyen duong n với n [10000,99999]. N vừa nhập có bao nhiêu chữ số chẵn, 

import math
n = int(input("nhap so nguyen duong n: "))
if n < 10000 or n > 99999:
    print("so khong hop le")
else:
    dem_chan = 0
    dem_le = 0
    for (so) in str(n):
        if int(so) % 2 == 0:
            dem_chan += 1
        else:
            dem_le += 1
    print("so chu so chan:", dem_chan)
    print("so chu so le:", dem_le)

 #bai2 kiem tra so chinh phuong
x = int(input("nhap so nguyen n:"))
i = 0

if x < 0:
    print("so khong hop le")
while(i*i <= x):
    if(i*i == x):
        print(x, "la so chinh phuong")
        break
    i += 1
print((i-1)*(i-1), "la so gan nhat lon hon", x)

#bai3
n = int(input("nhap so nguyen n: "))

while(n < 0):
    print("yeu cau nhap lai ")
    n = int(input("nhap so nguyen n: "))

print("so nhap dung la " ,n)



## bai 4 Yêu cầu 1: Nhập điểm lý thuyết, thực hành, kiểm tra hợp lệ, xuất điểm trung bình
while True:
    diem_lt = float(input("Nhập điểm lý thuyết [0..10]: "))
    if 0 <= diem_lt <= 10:
        break
    print("Điểm không hợp lệ, nhập lại!")

while True:
    diem_th = float(input("Nhập điểm thực hành [0..10]: "))
    if 0 <= diem_th <= 10:
        break
    print("Điểm không hợp lệ, nhập lại!")

dtb = (diem_lt + diem_th) / 2
print("Điểm trung bình cộng:", dtb)

# bai5
n = int(input("Nhập một số nguyên dương: "))
for i in range(1, n + 1):
    print(i, end=' ')
#bai 6

thang = int(input("nhap thang: "))
while True:
    if 1<= thang <= 12:
        break
    print("thang khong hop le, nhap lai")
if thang in [12,1,2]:
    print("mua dong")
elif thang in [3,4,5]:
    print("mua xuan")
elif thang in [6,7,8]:
    print("mua ha") 
elif thang in [9,10,11]:
    print("mua thu")


#bai7

thu_trong_tuan = int(input("nhap thu trong tuan (1-7): "))
if thu_trong_tuan < 1 or thu_trong_tuan > 7:
    print("thu khong hop le")
else:
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    print(days[thu_trong_tuan - 1])

#bai8 
max_val = 0
while True:
    n = int(input("Nhap so nguyen duong (nhap 0 de ket thuc): "))
    if n == 0:
        break
    if n > 0 and n > max_val:
        max_val = n
print("So lon nhat la:", max_val)

#bai 9
while True:
    tu = int(input("nhap tu: "))
    mau = int(input("nhap mau: "))
    thuong = float (tu) / mau
    if(tu == 0 or mau == 0):
        print("chuong trinh ket thuc")
        break
    else:
        print("thuong =", thuong)
        if(thuong != 0):
            tu = int(input("nhap tu: "))
            mau = int(input("nhap mau: "))
## bai10
while True:
    n = int(input("Nhập số nguyên dương: "))
    if n > 0:
        break
    print("Số không hợp lệ, nhập lại!")

sum = 0
for so in str(n):
    sum += int(so)
print("Tổng các chữ số là:", sum)


# bai 11
tong_duong = 0
while True:
    n = int(input("Nhập số (nhập 0 để kết thúc): "))
    if n == 0:
        break
    if n > 0:
        tong_duong += n
print("Tổng các số dương là:", tong_duong)

# bai 12
dem_am = 0
while True:
    n = int(input("Nhập số (nhập 0 để kết thúc): "))
    if n == 0:
        break
    if n < 0:
        dem_am += 1
print(f"Có {dem_am} số âm")

# bai 13
n = int(input("Nhập số nguyên dương: "))
dem_7 = 0
for so in str(n):
    if so == '7':
        dem_7 += 1
print(f"Có {dem_7} số 7")

#bai 16

n = int(input("Nhập số nguyên dương n: "))
i = 1
sum = 0
ketqua = 0
while i <= n:
    sum += i
    ketqua += 1/sum
    i += 1
print("Kết quả là:", ketqua)

n = int(input("Nhập số nguyên dương n: "))
i = 1
s = 0
while i <= n:
    s += 1/(i*(i+1))
    i += 1
print("Kết quả S2 =", s)




n = int(input("Nhập số nguyên dương n: "))
i = 1
s = 0
while i <= n:
    s += i/(i+1)
    i += 1
print("Kết quả S3 =", s)

n = int(input("Nhập số nguyên dương n: "))
i = 0
s = 0
while i <= n:
    s += (2*i+1)/(2*i+2)
    i += 1
print("Kết quả S4 =", s)

#bai 17 
while True:
    # Nhập N hợp lệ
    while True:
        N = int(input("Nhập số nguyên dương N: "))
        if N > 0:
            break
        print("N không hợp lệ, nhập lại!")

    max_le = None
    for i in range(N):
        x = int(input(f"Nhập số nguyên thứ {i+1}: "))
        if x % 2 != 0:
            if max_le is None or x > max_le:
                max_le = x
    if max_le is None:
        print("Không có số lẻ nào trong các số đã nhập.")
    else:
        print("Số lẻ lớn nhất là:", max_le)

    tiep_tuc = input("Bạn có muốn tiếp tục không? (nhấn 'c' để tiếp tục, phím khác để thoát): ")
    if tiep_tuc.lower() != 'c':
        break
#bai 18
N = int(input("Nhập số nguyên N: "))
print("Các ước số của", N, "là:")
for i in range(1, abs(N)+1):
    if N % i == 0:
        print(i, end=' ')
print()

#bai 20
#a
sum1 = 0
n = int(input("Nhập số nguyên dương n: "))
for i in range(1, n):
    sum1 += 1/i*(i+1)
print("Kết quả là:", sum1)
#b
sum2 = 0
a = int(input("Nhập số nguyên dương n: "))
for i in range(1, a):
    sum2 += (2*i+1)/(2*i+2)
print("Kết quả là:", sum2)


#bai 21
lst = []
max_div_5 = None
n = int(input("Nhập số phần tử của danh sách: "))
for i in range(n):
    num = int(input("Nhập phần tử : "))
    lst.append(num)
for x in lst:
    if x % 5 == 0:
        if max_div_5 is None or x > max_div_5:
            max_div_5 = x
if max_div_5 is None:
    print("Không có số nào chia hết cho 5 trong danh sách.")

#bai 22
lst = [12, 45, 23, 10, 55, 37, 90, 7]
A = float(input("Nhập số thực A: "))

new_lst = []
for x in lst:
    if x <= A:
        new_lst.append(x)

print("Danh sách sau khi xóa:", new_lst)

#bai 23
# List đã được sắp tăng dần sẵn
lst = [2, 5, 10, 15, 20, 30]

B = float(input("Nhập số thực B: "))

inserted = False
for i in range(len(lst)):
    if lst[i] > B:
        lst.insert(i, B)  # chèn vào vị trí i
        inserted = True
        break

if not inserted:
    lst.append(B)  # nếu B lớn hơn tất cả thì thêm vào cuối

print("Danh sách sau khi chèn:", lst)


#bai 24

N = int(input("Nhập N (số lượng số nguyên tố cần tìm): "))

primes = []   # danh sách chứa các số nguyên tố
num = 2       # bắt đầu kiểm tra từ 2

while len(primes) < N:   # lặp đến khi đủ N số nguyên tố
    is_prime = True
    # kiểm tra num có phải số nguyên tố không
    for i in range(2, int(num**0.5) + 1):   # chỉ cần đến căn bậc 2
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        primes.append(num)
    num += 1

print(f"{N} số nguyên tố đầu tiên là:", primes)

#bai 25
import math
x = int(input("Nhập số nguyên dương x: "))
guess = x/2
while True:
    new_guess = (guess + x/guess) / 2
    if abs(new_guess**2 - x) <= 1e-12:  # kiểm tra độ chính xác
        break
    guess = new_guess
print("Căn bậc hai của", x, "là:", new_guess)
print("Kiểm tra bằng hàm sqrt:", math.sqrt(x))


#bai 26
binary_str = input("nhap so nhi phan ")
decimal = 0
power = 0
for k in reversed(binary_str):
    if k == 1:
        decimal += 2 ** power
    power +=1

print(decimal)

#bai 14
import math

pts = []   # lưu các điểm
cv = 0.0   # chu vi
print("Nhập tọa độ (x,y). Bỏ trống x để dừng:")

truoc = None
while True:
    x = input("x = ")
    if x.strip() == "":
        if len(pts) > 2:
            # nối điểm cuối về điểm đầu
            cv += math.dist(pts[-1], pts[0])
        break

    y = input("y = ")
    x, y = float(x), float(y)
    pts.append((x,y))

    if truoc != None:
        cv += math.dist(truoc,(x,y))
    truoc = (x,y)

print("\nDanh sách điểm đã nhập:")
for p in pts:
    print(p)

print("Chu vi =", cv)
#bai16 
n = int(input("Nhập số nguyên thập phân: "))
result = ""

q = n
while q > 0:
    r = q % 2
    result = str(r) + result   # thêm vào đầu chuỗi
    q = q // 2

print(f"Số {n} ở dạng nhị phân là: {result}")

#bai 15 
# Bài: tính parity bit cho chuỗi nhị phân 8 bit
# mình làm đơn giản thôi

while True:
    s = input("Nhập chuỗi nhị phân 8 bit (Enter để thoát): ")
    if s == "":   # thoát vòng lặp khi người dùng nhấn Enter
        break

    # kiểm tra có đúng 8 kí tự không
    if len(s) != 8:
        print("Chuỗi phải đủ 8 bit!!!")
        continue

    # đếm số bit 1
    so1 = 0
    for c in s:
        if c == "1":
            so1 += 1

    loai = input("Chọn parity (even/odd): ")

    if loai == "even":
        if so1 % 2 == 0:
            parity = "0"
        else:
            parity = "1"
    else:  # odd
        if so1 % 2 == 0:
            parity = "1"
        else:
            parity = "0"

    print("Chuỗi kèm parity:", s + parity)






