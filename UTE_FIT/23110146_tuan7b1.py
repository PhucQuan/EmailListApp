import numpy as np

# ===============================================
# 1. Tạo mảng numpy 2x4 toàn giá trị 0
# ===============================================
def bai1():
    arr = np.zeros((2, 4))
    print("Bài 1 - Mảng 2x4 toàn 0:\n", arr)
    return arr


# ===============================================
# 2. Lọc các giá trị nguyên dương trong mảng 1D ngẫu nhiên
# ===============================================
def bai2():
    arr = np.random.randint(-10, 10, size=10)
    positive = arr[arr > 0]
    print("Bài 2 - Mảng gốc:", arr)
    print("Các giá trị nguyên dương:", positive)
    return positive


# ===============================================
# 3. Dùng argmax tìm chỉ mục phần tử lớn nhất trong mảng 1D
# ===============================================
def bai3():
    arr = np.random.randint(0, 100, size=10)
    index = np.argmax(arr)
    print("Bài 3 - Mảng:", arr)
    print("Chỉ mục phần tử lớn nhất:", index, "Giá trị:", arr[index])
    return index


# ===============================================
# 4. Mảng chứa các số lẻ từ 1 đến N
# ===============================================
def bai4():
    N = int(input("Nhập N: "))
    arr = np.arange(1, N + 1, 2)
    print("Bài 4 - Các số lẻ từ 1 đến", N, "là:", arr)
    return arr


# ===============================================
# 5. Mảng gồm 20 số thực cách đều trong khoảng (a, b)
# ===============================================
def bai5():
    a = float(input("Nhập a: "))
    b = float(input("Nhập b: "))
    arr = np.linspace(a, b, 20)
    print("Bài 5 - 20 số thực cách đều trong khoảng (a, b):\n", arr)
    return arr


# ===============================================
# 6. Mảng gồm 10 số thực ngẫu nhiên trong khoảng (a, b)
# ===============================================
def bai6():
    a = float(input("Nhập a: "))
    b = float(input("Nhập b: "))
    arr = a + (b - a) * np.random.rand(10)
    print("Bài 6 - 10 số thực ngẫu nhiên trong khoảng (a, b):\n", arr)
    return arr


# ===============================================
# 7. Thống kê bán hàng 2 buổi trong tuần (2x7)
# ===============================================
def bai7():
    sales = np.random.randint(10, 100, size=(2, 7))
    print("Bài 7 - Dữ liệu bán hàng (2 buổi x 7 ngày):\n", sales)

    # a. Ngày bán nhiều nhất
    total_per_day = sales.sum(axis=0)
    day_max = np.argmax(total_per_day)
    print("Ngày bán nhiều nhất (theo tổng 2 buổi): Thứ", day_max + 1)

    # b. Buổi & ngày bán nhiều nhất
    i, j = np.unravel_index(np.argmax(sales), sales.shape)
    print("Thời điểm bán nhiều nhất: Buổi", "sáng" if i == 0 else "chiều", ", Ngày", j + 1)

    # c. Buổi nào bán nhiều hơn
    morning_better = 0
    afternoon_better = 0
    equal_days = 0
    for d in range(7):
        if sales[0, d] > sales[1, d]:
            morning_better += 1
        elif sales[0, d] < sales[1, d]:
            afternoon_better += 1
        else:
            equal_days += 1

    if morning_better > afternoon_better:
        result = "Buổi sáng bán nhiều hơn"
    elif afternoon_better > morning_better:
        result = "Buổi chiều bán nhiều hơn"
    else:
        result = "Hai buổi như nhau"
    print(result)
    return sales


# ===============================================
# 8. Chọn thí sinh từ hai phòng thi
# ===============================================
def combine_rooms(room_1, room_2):
    result = []
    for a, b in zip(room_1, room_2):
        if a > 0:
            result.append(a)
        elif b > 0:
            result.append(b)
        else:
            result.append(None)
    return result


def bai8():
    room_1 = np.array([1, 2, -3, 4, 5, 6, -7])
    room_2 = np.array([8, 9, 10, 11, 12, -13, -14])
    result = combine_rooms(room_1, room_2)
    print("Bài 8 - Danh sách thí sinh cuối cùng:", result)
    return result


# ===============================================
# 9. Mô phỏng broadcast vector thành ma trận
# ===============================================
def broadcast(vec, n):
    return np.tile(vec.reshape(-1, 1), (1, n))


def bai9():
    vec = np.array([6, 7])
    n = 3
    result = broadcast(vec, n)
    print("Bài 9 - Broadcast vector:\n", result)
    return result


# ===============================================
# 10. Ma trận chuyển vị
# ===============================================
def transpose(mat):
    return mat.T


def bai10():
    mat = np.array([[1, 2], [3, 4], [5, 6]])
    result = transpose(mat)
    print("Bài 10 - Ma trận chuyển vị:\n", result)
    return result


# ===============================================
# 11. Tích ma trận & tích Hadamard
# ===============================================
def product(mat_a, mat_b):
    try:
        matmul_res = np.matmul(mat_a, mat_b)
        print("Tích ma trận:\n", matmul_res)
    except ValueError:
        print("Không có tích ma trận")

    try:
        hadamard_res = mat_a * mat_b
        print("Tích Hadamard:\n", hadamard_res)
    except ValueError:
        print("Không có tích Hadamard")


def bai11():
    A = np.array([[1, 2, 3], [4, 5, 6]])
    B = np.array([[7, 8], [9, 10], [11, 12]])
    print("Bài 11:")
    product(A, B)
    return


# ===============================================
# 12. Thay giá trị cột thành 1
# ===============================================
def replace_col(mat, col_ind):
    mat[:, col_ind] = 1
    return mat


def bai12():
    mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    col = int(input("Nhập chỉ số cột cần thay (0-index): "))
    result = replace_col(mat, col)
    print("Bài 12 - Ma trận sau khi thay cột", col, "thành 1:\n", result)
    return result


# ===============================================
# MAIN TEST
# ===============================================
if __name__ == "__main__":
    print("=== CHƯƠNG TRÌNH BÀI TẬP NUMPY ===")
    bai1()
    bai2()
    bai3()
    # Các bài có nhập từ bàn phím bạn có thể gọi thủ công:
    # bai4()
    # bai5()
    # bai6()
    bai7()
    bai8()
    bai9()
    bai10()
    bai11()
    # bai12()  # Gọi khi muốn nhập cột cần thay
