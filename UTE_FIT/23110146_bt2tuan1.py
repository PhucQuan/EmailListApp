#bai 
import math
import numpy as np

# ---------------- Các bài ----------------
def bai1():# Bảng ánh xạ điểm chữ sang điểm số
    bang_diem = {
        'A': 4.0,
        'B': 3.0,
        'C': 2.0,
        'D': 1.0,
        'F': 0.0
    }

    while True:
        ky_tu = input("Nhập ký tự điểm (A, B, C, D, F): ").upper()
        if ky_tu in bang_diem:
            print("Điểm số tương ứng:", bang_diem[ky_tu])
            break
        else:
            print("Yêu cầu nhập lại!")
    

def bai2():
        while True:
            n = float(input("Nhập giá trị đánh giá hiệu quả làm việc (0.0, 0.4, 0.6 hoặc lớn hơn): "))
            if n == 0.0:
                print("Hiệu quả làm việc: unacceptable")
                print("Tiền thưởng: $", 2400 * n)
                break
            elif n == 0.4:
                print("Hiệu quả làm việc: acceptable")
                print("Tiền thưởng: $", 2400 * n)
                break
            elif n >= 0.6:
                print("Hiệu quả làm việc: meritorious")
                print("Tiền thưởng: $", 2400 * n)
                break
            else:
                print("Vui lòng nhập lại")

def bai3():
    year = int(input("nhap so nam "))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 :
        print(year,"la nam nhuan")
    else:
        print(year,"khong phai nam nhuan")


def bai4():
    a = float(input("nhap so thuc a: "))
    b = float(input("nhap so thuc b: "))
    c = float(input("nhap so thuc c: "))
    if a == 0:
        if b == 0:
            if c == 0:
                print("phuong trinh co vo so nghiem")
            else:
                print("phuong trinh vo nghiem")
        else:
            x = -c / b
            print("phuong trinh co nghiem x =", x)
    else:   
        delta = b**2 - 4*a*c
        if delta < 0:
            print("phuong trinh vo nghiem")
        elif delta == 0:
            x = -b/(2*a)
            print("phuong trinh co nghiem kep x =", x)
        else:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            print("phuong trinh co 2 nghiem: x1 =", x1, ", x2 =", x2)



def bai5():
    a = float(input("nhap so thuc a: "))
    b = float(input("nhap so thuc b: "))
    c = float(input("nhap so thuc c: "))
    if(abs(a) < 10) :
        print("gia tri tuyet doi cua a nho hon 10",a)
    if(abs(b) < 10) :   
        print("gia tri tuyet doi cua b nho hon 10",b)
    if(abs(c) < 10) :
        print("gia tri tuyet doi cua c nho hon 10",c)


def bai6():
    numbers = []
    for i in range(5):
        num = float(input(f"Nhập số thực thứ {i+1}: "))
        numbers.append(num)

    print("Số lớn nhất là:", max(numbers))
    print("Số nhỏ nhất là:", min(numbers))

def bai7():
    year = int(input("Nhập năm: "))
    day_of_the_week = (year + math.floor((year - 1) / 4) - math.floor((year - 1) / 100) + math.floor((year - 1) / 400)) % 7

# Mapping số sang tên thứ
    thu_map = {
        0: "Chủ nhật",
        1: "Thứ hai",
        2: "Thứ ba",
        3: "Thứ tư",
        4: "Thứ năm",
        5: "Thứ sáu",
        6: "Thứ bảy"
}

    print(f"Ngày 1 tháng 1 năm {year} là {thu_map[day_of_the_week]}")

def bai8():
    n = int(input("nhap gia tri của tháng"))
    if n < 1 or n > 12:
        print("thang khong hop le")
    else:
        print("thang hop le")
    


def bai9():
    x = float(input("Nhập số thực x: "))
    if x > 0:
        fx = x**2 + 3*x + 5
    else:
        fx = -x**2 - 3*x - 5
    print("f(x) =", fx)

def bai10():
   
   
    nums = []
    dem_am = 0
    dem_duong = 0
    dem_0 = 0
    for i in range(5):
        num = float(input(f"Nhập số thứ {i+1}: "))
        nums.append(num)
        if num < 0:
            dem_am += 1
        elif num > 0:
            dem_duong += 1
        else:
            dem_0 += 1
    print("Số âm:", dem_am)
    print("Số dương:", dem_duong)
    print("Số bằng 0:", dem_0)

def bai11():
    a = int(input("Nhập số nguyên dương a: "))
    b= int(input("Nhập số nguyên dương b: "))
    if a % 2 == 0 and b % 2 == 0:
        print("a và b là 2 số chẵn")
    elif (a % 2 == 0 and b % 2 != 0) or (a % 2 != 0 and b % 2 == 0):
        print("chỉ có một số chẵn")
    else:
        print("a, b là hai số lẻ")



def bai12():
    
    a = int(input("Nhập số nguyên a: "))
    b = int(input("Nhập số nguyên b: "))
    if b == 0:
        print("Không thể kiểm tra vì b = 0.")
    elif a % b == 0:
        print(f"{a} là bội của {b}")
    else:
        print(f"{a} không phải là bội của {b}")



def bai13():
   a = int(input("Nhập số nguyên dương a: "))
   b = int(input("Nhập số nguyên dương b: "))
   c = int(input("Nhập số nguyên dương c: "))
   duong =[]
   if a > 0:
       duong.append(a)
   if b > 0:
        duong.append(b)
   if c>0:
        duong.append(c)
   if len(duong) == 0:
        print("khong co so duong")
   else:
        print("so duong lon nhat la:", min(duong))


def bai14():
   a = int(input("Nhập số nguyên dương a: "))
   b = int(input("Nhập số nguyên dương b: "))
   c = int(input("Nhập số nguyên dương c: "))
   sochan =[]
   if a % 2 == 0:
       sochan.append(a)
   if b % 2 == 0:
        sochan.append(b)
   if c % 2 == 0:
        sochan.append(c)
   if len(sochan) > 0:
        print("so chan lon nhat la:", max(sochan))
   else:
        print("khong co so chan")
    
def bai15():
    a = int(input("Nhập số nguyên a: "))
    b = int(input("Nhập số nguyên b: "))
    c = int(input("Nhập số nguyên c: "))
    nums = [a, b, c]
    nums.sort()
    print("Số lớn nhì là:", nums[1])


# ---------------- Menu chọn ----------------
while True:
    print("\n--- MENU ---")
    print("1. Bài 1")
    print("2. Bài 2")
    print("3. Bài 3")
    print("4. Bài 4")
    print("5. Bài 5")
    print("6. Bài 6")
    print("7. Bài 7")
    print("9. Bài 9")
    print("10. Bài 10")
    print("11. Bài 11")
    print("12. Bài 12")
    print("13. Bài 13")
    print("14. Bài 14")
    print
    print("0. Thoát")

    choice = int(input("Chọn bài muốn chạy: "))

    if choice == 0:
        print("Thoát chương trình.")
        break
    elif choice == 1: bai1()
    elif choice == 2: bai2()
    elif choice == 3: bai3()
    elif choice == 4: bai4()
    elif choice == 5: bai5()
    elif choice == 6: bai6()
    elif choice == 7: bai7()
    elif choice == 9: bai9()
    elif choice == 10: bai10()
    elif choice == 11: bai11()
    elif choice == 12: bai12()
    elif choice == 13: bai13()
    elif choice == 14: bai14()
    elif choice == 15: bai15()
    else:
        print("Không có bài này, vui lòng chọn lại!")

