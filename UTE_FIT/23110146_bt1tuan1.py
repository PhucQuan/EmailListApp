import math
import numpy as np

# ---------------- Các bài ----------------
def bai1():
    x = int(input("nhap don gia: "))
    y = int(input("nhap so luong: "))
    z = x*y
    print("tong tien truoc thue la", z)
    print("tong tien thue la", z*0.1)
    print("tong tien sau thue la", z*1.1)

def bai2():
    x, y, z = 5, 10, 9
    a, b, c = 3, 9, 8
    print("gia tri trung binh la", (x+y+z)/3)
    print("gia tri trung binh la", (a+b+c)/3)

def bai3():
    n = int(input("nhap so nguyen co 3 chu so: "))
    tram = n // 100
    chuc = (n % 100) // 10
    donvi = n % 10
    print("gia tri trung binh cong 3 chu so la", (tram + chuc + donvi) / 3)

def bai4():
    n = int(input("nhap so nguyen duong: "))
    dem = 0
    while n != 0:
        n //= 10
        dem += 1
    print("so chu so cua so nguyen duong la", dem)

def bai5():
    a = int(input("nhap so nguyen a: "))
    b = int(input("nhap so nguyen b: "))
    print("trc khi hoan doi, a =", a, ", b =", b)
    a, b = b, a
    print("sau khi hoan doi, a =", a, ", b =", b)

def bai6():
    a = int(input("nhap so nguyen a: "))
    b = int(input("nhap so nguyen b: "))
    c = int(input("nhap so nguyen c: "))
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

def bai7():
    x = int(input("nhap so nguyen bat ki: "))
    kq = x**8 - 5 + abs(x)
    print("ket qua =", kq)

def bai9():
    x = float(input("nhap so thuc: "))
    print("phan nguyen cua so thuc la", int(x))

def bai10():
    x = input("nhap ki tu bat ki: ")
    print("ki tu do la", x)

def bai11():
    x = int(input("nhap so nguyen n: "))
    for i in range(1, 11):
        print(x, "x", i, "=", x*i)

def bai12():
    dai = 10
    cao = 6
    dientich = (dai * cao) / 2
    print("dien tich tam giac la", dientich, "cm^2")

def bai13():
    x1 = math.pi
    x2 = math.pi / 2
    x3 = 4 * math.pi / 3

    #kiem tra bieu thuc sin^2(x) + cos^2(x) voi cac gia tri x co dung khong ( true/false)
    print("voi x =", x1, ", bieu thuc sin^2(x) + cos^2(x) =", (math.sin(x1))**2 + (math.cos(x1))**2)
    print("voi x =", x2, ", bieu thuc sin^2(x) + cos^2(x) =", (math.sin(x2))**2 + (math.cos(x2))**2)
    print("voi x =", x3, ", bieu thuc sin^2(x) + cos^2(x) =", (math.sin(x3))**2 + (math.cos(x3))**2)
    if (math.sin(x1))**2 + (math.cos(x1))**2 == 1:
        print("voi x =", x1, ", bieu thuc sin^2(x) + cos^2(x) dung")
    else:
        print("voi x =", x1, ", bieu thuc sin^2(x) + cos^2(x) sai")
    if (math.sin(x2))**2 + (math.cos(x2))**2 == 1:
        print("voi x =", x2, ", bieu thuc sin^2(x) + cos^2(x) dung")
    else:
        print("voi x =", x2, ", bieu thuc sin^2(x) + cos^2(x) sai")
    if (math.sin(x3))**2 + (math.cos(x3))**2 == 1:  
        print("voi x =", x3, ", bieu thuc sin^2(x) + cos^2(x) dung")
    else:
        print("voi x =", x3, ", bieu thuc sin^2(x) + cos^2(x) sai")
        
  



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
    else:
        print("Không có bài này, vui lòng chọn lại!")
