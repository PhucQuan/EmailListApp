#tong cac phan tu tren duong cheo trinh ma tran vuong
n = int(input("nhap n: "))
a = []
for i in range(n):
    
    row = list(map(int, input().split()))
    a.append(row)

tong = 0
for i in range(n):
    tong += a[i][i]
print(tong)

# Bài 2: Sắp xếp ma trận theo tổng từng hàng

def sort_matrix_by_row_sum(matrix):
    # Tạo danh sách cặp (tổng hàng, hàng)
    row_with_sum = [(sum(row), row) for row in matrix]
    
    # Sắp xếp theo tổng hàng
    sorted_rows = sorted(row_with_sum, key=lambda x: x[0])
    
    # Lấy lại ma trận sau khi sắp xếp
    sorted_matrix = [row for (_, row) in sorted_rows]
    
    return sorted_matrix


# Ví dụ sử dụng
matrix = [
    [4, 2, 7],
    [1, 5, 6],
    [3, 8, 2]
]

print("Ma trận gốc:")
for row in matrix:
    print(row)

sorted_matrix = sort_matrix_by_row_sum(matrix)

print("\nMa trận sau khi sắp xếp:")
for row in sorted_matrix:
    print(row)

# Bài 3: Tính toán giá trị hàng tồn kho

def inventory_summary(inventory):
    # 1. Tổng số lượng hàng
    total_quantity = sum(item[1] for item in inventory)

    # 2. Giá trị từng sản phẩm
    product_values = [(item[0], item[1] * item[2]) for item in inventory]

    # 3. Tổng giá trị tồn kho
    total_value = sum(value for _, value in product_values)

    return total_quantity, product_values, total_value


# Ví dụ
inventory = [
    ["Sản phẩm 1", 10, 5.0],
    ["Sản phẩm 2", 5, 2.5],
    ["Sản phẩm 3", 3, 8.0]
]

total_qty, product_vals, total_val = inventory_summary(inventory)

print("Tổng số lượng hàng tồn kho:", total_qty)

print("\nGiá trị từng sản phẩm:")
for name, val in product_vals:
    print(f"- {name}: {val}")

print("\nTổng giá trị toàn bộ hàng tồn kho:", total_val)

def find_max(list_3d):
    max_value = list_3d[0][0][0]  # giả sử phần tử đầu tiên là lớn nhất
    for matrix in list_3d:          # duyệt từng "ma trận 2D"
        for row in matrix:          # duyệt từng hàng
            for value in row:       # duyệt từng phần tử
                if value > max_value:
                    max_value = value
    return max_value


# Ví dụ
list_3d = [
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
]

print("Giá trị lớn nhất:", find_max(list_3d))  # 12



# bai 4

def flatten_3d_list(list_3d):
    flat_list = []
    for matrix in list_3d:       # duyệt từng ma trận 2D
        for row in matrix:       # duyệt từng hàng
            for value in row:    # duyệt từng phần tử
                flat_list.append(value)
    return flat_list
list_3d = [
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
]


# Test
print(flatten_3d_list(list_3d))


def rotate_3d_clockwise(list_3d):
    depth = len(list_3d)        # số lớp
    rows = len(list_3d[0])      # số hàng trong 1 lớp
    cols = len(list_3d[0][0])   # số cột trong 1 lớp

    
    rotated = []
    for r in range(rows):
        new_layer = []
        for d in range(depth):
            new_layer.append(list_3d[d][r])
        rotated.append(new_layer)
    return rotated



list_3d = [
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]]
]

result = rotate_3d_clockwise(list_3d)
print(result)
#=========================================== 1D array ============================

# Bài 1: Tạo 1D array và in ra màn hình

arr = [1, 2, 3, 4, 5]

print("1D array vừa tạo là:", arr)

#bai 2 : tổng các phần tử trong 1 arr
total = sum(arr)
print("Tổng các phần tử trong 1D array là:", total)

#bai 3: tìm phần tử lớn nhất,nhỏ nhất trong 1 arr
max_value = max(arr)
min_value = min(arr)
print("Phần tử lớn nhất trong 1D array là:", max_value)
print("Phần tử nhỏ nhất trong 1D array là:", min_value)

#bai 4 : chuong trinh tinh trung binh cong 
average = total / len(arr)
print("Trung bình cộng của các phần tử trong 1D array là:", average)

#bai 5 : sap xep theo chieu tang hoac giam dan
sorted_arr_asc = sorted(arr)
sorted_arr_desc = sorted(arr, reverse=True)
print("1D array sau khi sắp xếp tăng dần:", sorted_arr_asc)
print("1D array sau khi sắp xếp giảm dần:", sorted_arr_desc)

#bai 6 : tong cac phan tu tren cac vi tri  chan va le
sum_even_index = sum(arr[i] for i in range(0, len(arr), 2))
qum_odd_index = sum(arr[i] for i in range(1, len(arr), 2))
print("Tổng các phần tử ở vị trí chẵn:", sum_even_index)
print("Tổng các phần tử ở vị trí lẻ:", qum_odd_index)

#bai 7 : tim cac so chan trong array va tinh tong cua chung
even_numbers = [x for x in arr if x % 2 == 0]
sum_even_numbers = sum(even_numbers)
print("Các số chẵn trong 1D array:", even_numbers)
print("Tổng các số chẵn trong 1D array:", sum_even_numbers)

#bai 8 : tong cac so nguyen to trong array 
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
prime_numbers = [x for x in arr if is_prime(x)]
sum_prime_numbers = sum(prime_numbers)
print("Các số nguyên tố trong 1D array:", prime_numbers)
print("Tổng các số nguyên tố trong 1D array:", sum_prime_numbers)

#bai 9 : tong cac so duong va tich cac so am trong array
positive_numbers = [x for x in arr if x > 0]
negative_numbers = [x for x in arr if x < 0]
sum_positive = sum(positive_numbers)
product_negative = 1
for num in negative_numbers:
    product_negative *= num
print("Tổng các số dương trong 1D array:", sum_positive)
print("Tích các số âm trong 1D array:", product_negative if negative_numbers else 0)

#bai 10 : tong cac so trong array sau khi loai bo cac so trung nhau
unique_numbers = set(arr)
sum_unique = sum(unique_numbers)
print("Các số duy nhất trong 1D array:", unique_numbers)
print("Tổng các số duy nhất trong 1D array:", sum_unique)


#=========================================== 2D array ============================
#bai 1 : tong cac phan tu trong array 2D
input =     [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
total_2d = sum(sum(row) for row in input)
print("Tổng các phần tử trong 2D array là:", total_2d)

#bai 2 : tim gia tri lon nhat va nho nhat trong array 2D
max_2d = max(max(row) for row in input)
min_2d = min(min(row) for row in input)
print("Phần tử lớn nhất trong 2D array là:", max_2d)
print("Phần tử nhỏ nhất trong 2D array là:", min_2d)

#bai 3 : tinh trung binh cong cac phan tu trong array 2D
num_elements_2d = sum(len(row) for row in input)
average_2d = total_2d / num_elements_2d
#bai 4 : sap xep 2D array theo chieu tang dan hoac giam dan
def sort_2d_array(matrix, ascending=True):
    flat_list = [item for sublist in matrix for item in sublist]
    flat_list.sort(reverse=not ascending)
    
    sorted_matrix = []
    index = 0
    for row in matrix:
        row_length = len(row)
        sorted_matrix.append(flat_list[index:index + row_length])
        index += row_length
    
    return sorted_matrix

#bai 5 : tổng các phần tử trong mỗi hàng và tính tổng  mỗi hàng
def sum_of_rows(matrix):
    return [sum(row) for row in matrix]
row_sums = sum_of_rows(input)
print("Tổng các phần tử trong mỗi hàng:", row_sums)
print("tổng của mỗi hàng là",sum(row_sums))

