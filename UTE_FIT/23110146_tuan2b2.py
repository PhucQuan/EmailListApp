# 1. Tính tổng các phần tử
def bai1():
    n = int(input("Nhập số phần tử n: "))
    lst = []
    for i in range(n):
        x = float(input(f"Nhập phần tử thứ {i+1}: "))
        lst.append(x)
    print("Tổng các phần tử:", sum(lst))

# 2. Tính trung bình cộng
def bai2():
    n = int(input("Nhập số phần tử n: "))
    lst = []
    for i in range(n):
        x = float(input(f"Nhập phần tử thứ {i+1}: "))
        lst.append(x)
    if n > 0:
        print("Trung bình cộng:", sum(lst)/n)
    else:
        print("Danh sách rỗng.")

# 3. Vị trí phần tử âm đầu tiên
def bai3():
    n = int(input("Nhập số phần tử n: "))
    lst = []
    for i in range(n):
        x = float(input(f"Nhập phần tử thứ {i+1}: "))
        lst.append(x)
    found = False
    for i in range(n):
        if lst[i] < 0:
            print("Vị trí phần tử âm đầu tiên:", i)
            found = True
            break
    if not found:
        print("Không có phần tử âm.")

# 4. Vị trí phần tử âm thứ k
def bai4():
    n = int(input("Nhập số phần tử n: "))
    k = int(input("Nhập giá trị k (nguyên dương): "))
    lst = []
    for i in range(n):
        x = float(input(f"Nhập phần tử thứ {i+1}: "))
        lst.append(x)
    count = 0
    found = False
    for i in range(n):
        if lst[i] < 0:
            count += 1
            if count == k:
                print("Vị trí phần tử âm thứ", k, "là:", i)
                found = True
                break
    if not found:
        print("Không có đủ phần tử âm.")

# 5. In ra danh sách các số chẵn/lẻ
def bai5():
    n = int(input("Nhập số phần tử n: "))
    lst = []
    chan = []
    le = []
    for i in range(n):
        x = int(input(f"Nhập phần tử thứ {i+1}: "))
        lst.append(x)
        if x % 2 == 0:
            chan.append(x)
        else:
            le.append(x)
    print("Các số chẵn:", chan)
    print("Các số lẻ:", le)

# 6. In ra danh sách các số nguyên tố
def bai6(): 
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5)+1):
            if x % i == 0:
                return False
        return True
    n = int(input("Nhập số phần tử n: "))
    lst = []
    primes = []
    for i in range(n):
        x = int(input(f"Nhập phần tử thứ {i+1}: "))
        lst.append(x)
        if is_prime(x):
            primes.append(x)
    print("Các số nguyên tố:", primes)

# 7. Xóa tất cả phần tử có giá trị k
def bai7():
    n = int(input("Nhập số phần tử n: "))
    lst = []
    for i in range(n):
        x = input(f"Nhập phần tử thứ {i+1}: ")
        lst.append(x)
    k = input("Nhập giá trị k: ")
    if k in lst:
        lst = [x for x in lst if x != k]
        print("Danh sách sau khi xóa tất cả phần tử có giá trị k:", lst)
    else:
        print("Không tồn tại giá trị k trong danh sách.")

# 8. Xuất ra danh sách các phần tử không trùng lặp
def bai8():
    n = int(input("Nhập số phần tử n: "))
    lst = []
    for i in range(n):
        x = input(f"Nhập phần tử thứ {i+1}: ")
        lst.append(x)
    result = [x for x in lst if lst.count(x) == 1]
    print("Các phần tử không trùng lặp:", result)

# 9. Sắp xếp list tăng dần
def bai9():
    n = int(input("Nhập số phần tử n: "))
    lst = []
    for i in range(n):
        x = float(input(f"Nhập phần tử thứ {i+1}: "))
        lst.append(x)
    lst.sort()
    print("List tăng dần:", lst)

# 10. Sắp xếp phần tử âm giảm dần
def bai10():
    n = int(input("Nhập số phần tử n: "))
    lst = []
    am = []
    for i in range(n):
        x = float(input(f"Nhập phần tử thứ {i+1}: "))
        lst.append(x)
        if x < 0:
            am.append(x)
    am.sort(reverse=True)
    print("Các phần tử âm giảm dần:", am)

# 11. Sắp xếp phần tử âm tăng dần, dương giảm dần
def bai11():
    n = int(input("Nhập số phần tử n: "))
    lst = []
    am = []
    duong = []
    for i in range(n):
        x = float(input(f"Nhập phần tử thứ {i+1}: "))
        lst.append(x)
        if x < 0:
            am.append(x)
        elif x > 0:
            duong.append(x)
    am.sort()
    duong.sort(reverse=True)
    print("Âm tăng dần:", am)
    print("Dương giảm dần:", duong)

# 12. Sắp xếp phần tử lẻ giảm dần, chẵn tăng dần
def bai12():
    n = int(input("Nhập số phần tử n: "))
    lst = []
    chan = []
    le = []
    for i in range(n):
        x = int(input(f"Nhập phần tử thứ {i+1}: "))
        lst.append(x)
        if x % 2 == 0:
            chan.append(x)
        else:
            le.append(x)
    chan.sort()
    le.sort(reverse=True)
    print("Chẵn tăng dần:", chan)
    print("Lẻ giảm dần:", le)

# 13. Tìm ước số và bội số của k
def bai13():
    n = int(input("Nhập số phần tử n: "))
    k = int(input("Nhập giá trị k (k>=0): "))
    lst = []
    uoc = []
    boi = []
    for i in range(n):
        x = int(input(f"Nhập phần tử thứ {i+1}: "))
        lst.append(x)
        if k > 0 and x % k == 0:
            boi.append(x)
        if k > 0 and k % x == 0:
            uoc.append(x)
    print("Các ước số của k:", uoc)
    print("Các bội số của k:", boi)

# 14. Nhiệt độ 7 ngày, tính trung bình, đếm số ngày lớn hơn trung bình
def bai14():
    temps = []
    for i in range(7):
        t = float(input(f"Nhập nhiệt độ ngày thứ {i+1}: "))
        temps.append(t)
    tb = sum(temps)/7
    dem = sum(1 for x in temps if x > tb)
    print("Nhiệt độ trung bình tuần:", tb)
    print("Số ngày nhiệt độ lớn hơn trung bình:", dem)

# 15. Tìm ước số và bội số của k trong list
def bai15():
    n = int(input("Nhập số phần tử n: "))
    k = int(input("Nhập giá trị k (k>=0): "))
    lst = []
    uoc = []
    boi = []
    for i in range(n):
        x = int(input(f"Nhập phần tử thứ {i+1}: "))
        lst.append(x)
        if k > 0 and x % k == 0:
            boi.append(x)
        if k > 0 and k % x == 0:
            uoc.append(x)
    print("Các ước số của k:", uoc)
    print("Các bội số của k:", boi)


def bai17():
    n = int(input("nhap so phan tu n"))
    lst =[]
    for i in range(n):
        x = int(input("nhap phan tu thu i + 1 :"))
        lst.append(x)

    if n == 0 :
        print("khong co gia tri max,min")
    else:
        max_val = lst[0]
        min_val = lst[0]

        for num in lst:
            if num > max_val:
                max_val = num
            if num < min_val:
                min_val = num
        print(max_val)
        print(min_val)

def bai18():
    n = int(input("Nhập n: "))

    list_numbers = [i for i in range(n+1)]
    list_squares = [i**2 for i in range(n)]

    print("Danh sách số tự nhiên từ 0 → n:", list_numbers)
    print("Danh sách bình phương từ 0 → n-1:", list_squares)


def bai19():
    def count_ways(coins, m, n):
    # dp[i] = số cách để tạo ra số i
        dp = [0] * (n + 1)
        dp[0] = 1  # Có 1 cách để đổi ra 0 (không dùng đồng nào)

        for i in range(m):
            for j in range(coins[i], n + 1):
                dp[j] += dp[j - coins[i]]
        return dp[n]

# Ví dụ
    coins = [1, 2, 3]
    N = 4
    print(f"Số cách đổi {N} xu:", count_ways(coins, len(coins), N))

    coins = [2, 5, 3, 6]
    N = 10
    print(f"Số cách đổi {N} xu:", count_ways(coins, len(coins), N))









# Menu chọn bài
while True:
    print("\n--- MENU ---")
    print("1. Tính tổng các phần tử")
    print("2. Tính trung bình cộng")
    print("3. Vị trí phần tử âm đầu tiên")
    print("4. Vị trí phần tử âm thứ k")
    print("5. In ra danh sách các số chẵn/lẻ")
    print("6. In ra danh sách các số nguyên tố")
    print("7. Xóa tất cả phần tử có giá trị k")
    print("8. Xuất ra danh sách các phần tử không trùng lặp")
    print("9. Sắp xếp list tăng dần")
    print("10. Sắp xếp phần tử âm giảm dần")
    print("11. Sắp xếp phần tử âm tăng dần, dương giảm dần")
    print("12. Sắp xếp phần tử lẻ giảm dần, chẵn tăng dần")
    print("13. Tìm ước số và bội số của k")
    print("14. Nhiệt độ 7 ngày, tính trung bình, đếm số ngày lớn hơn trung bình")
    print("15. Tìm ước số và bội số của k trong list")
    print("17")
    print("18")
    print("19")
    print("0. Thoát")
    choice = input("Chọn bài (0-15): ")
    if choice == "1":
        bai1()
    elif choice == "2":
        bai2()
    elif choice == "3":
        bai3()
    elif choice == "4":
        bai4()
    elif choice == "5":
        bai5()
    elif choice == "6":
        bai6()
    elif choice == "7":
        bai7()
    elif choice == "8":
        bai8()
    elif choice == "9":
        bai9()
    elif choice == "10":
        bai10()
    elif choice == "11":
        bai11()
    elif choice == "12":
        bai12()
    elif choice == "13":
        bai13()
    elif choice == "14":
        bai14()
    elif choice == "15":
        bai15()
    elif choice == "17":
        bai17()
    elif choice == "18":
        bai18()
    elif choice == "19":
        bai19()
    elif choice == "0":
        print("Kết thúc chương trình.")
        break
    else:
        print("Chọn không hợp lệ, vui lòng chọn lại.")