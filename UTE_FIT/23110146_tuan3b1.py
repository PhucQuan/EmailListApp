
#bai1
s = input("nhap cac so cach nhau boi dau phay ")
lst = s.split(",")
tupple1 = tuple(lst)
print(lst)
print(tupple1)

#----------------------------------------------------------------------
#bai2
data = []
print("Nhập dữ liệu (dạng name,age,score)")
while True:
    s = input()
    if not s:  # nếu người dùng nhập dòng trống thì dừng
        break
    parts = s.split(",")
    if len(parts) != 3:
        print("Sai định dạng, hãy nhập lại theo dạng name,age,score")
        continue
    name, age, score = parts[0].strip(), int(parts[1].strip()), int(parts[2].strip())
    data.append((name, age, score))

    # Sắp xếp theo name -> age -> score
sorted_data = sorted(data, key=lambda x: (x[0], x[1], x[2]))

print(sorted_data)
#==================================================================================
#bai 3
lst = [1,2,3]
tuple1 = (4,5,6)
lst2 = list(tuple1)
lst += lst2
lst1 = [1,2,3]


tuple2 = list(tuple1)
tuple2 += lst1
tuple2.sort()
tuple3 = tuple(tuple2)

print("outputList = ",lst)
print("outputTuple",tuple3)
#bai4===================================================================================

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(len(it_companies)) 
it_companies.add('Twitter')
it_companies.update(['Netflix', 'Tesla', 'Intel'])
it_companies.remove('Google')   # nếu không tồn tại sẽ báo lỗi
# hoặc:
it_companies.discard('Google') # không báo lỗi nếu không tồn tại
print(A.union(B))
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.union(B))
print(B.union(A))   
print(A.symmetric_difference(B))
#12
del A
del B
age_set = set(age)
#13
print("Độ dài list:", len(age))
#13
print("Độ dài set:", len(age_set))

#====================================================================================
#Dictionary 
#bai 1
dict1 = { 'x' : 10, 'y' : 8 }
dict2 = { 'a' : 6, 'b' : 4 }
dict3 = {**dict1, **dict2}
print(dict3)

#bai 2
d = { 'a' : 100, 'b' : 200, 'c' : 300 }
print(sum(d.values()))

#bai 3
n = int(input("Nhập n: "))
mydict = {i: i**2 for i in range(1, n+1)}
print(mydict)

#bai 4
a = input("Nhập list a (cách nhau dấu cách): ").split()
b = input("Nhập list b (cách nhau dấu cách): ").split()
mydict = dict(zip(a, b))
print(mydict)

#bai 5
mydict = {}
n = int(input("Nhập số học sinh: "))
for _ in range(n):
    name = input("Tên học sinh: ")
    score = int(input("Điểm: "))
    mydict[name] = score

# Thống kê theo từng mốc điểm
count = {}
for score in mydict.values():
    count[score] = count.get(score, 0) + 1

print("Thống kê điểm:", count)

#bai 6
s = input("Nhập chuỗi: ")
letters = sum(c.isalpha() for c in s)
digits = sum(c.isdigit() for c in s)
print(f"Số ký tự chữ: {letters}, số ký tự số: {digits}")


#===========================================================================================


#bai 1

# Từ điển ánh xạ ký tự sang mã Morse
morse_code = {
    'A': '.-',     'B': '-...',   'C': '-.-.', 
    'D': '-..',    'E': '.',      'F': '..-.',
    'G': '--.',    'H': '....',   'I': '..',
    'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',
    'S': '...',    'T': '-',      'U': '..-',
    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',
    '0': '-----',  '1': '.----',  '2': '..---',
    '3': '...--',  '4': '....-',  '5': '.....',
    '6': '-....',  '7': '--...',  '8': '---..',
    '9': '----.'
}

# Nhập chuỗi từ người dùng
text = input("Nhập chuỗi cần mã hóa Morse: ")

# Chuyển chuỗi sang chữ hoa để ánh xạ dễ dàng
text = text.upper()

# Mã hóa sang Morse (bỏ qua ký tự không có trong từ điển)
morse_result = []
for ch in text:
    if ch in morse_code:
        morse_result.append(morse_code[ch])

# Nối các ký tự Morse bằng khoảng trắng
print("Chuỗi Morse là:")
print(" ".join(morse_result))
#===========================================================================================
#bai 2:
text = "An eye for an eye makes the whole world blind. – Mahatma Gandhi"

# Bỏ dấu câu đơn giản
for ch in ".–,":
    text = text.replace(ch, "")

# Đếm bằng dictionary
counts = {}
for ch in text:
    if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):   # chỉ lấy chữ cái
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1

# In ra kết quả
for k in counts:
    print(k, ":", counts[k])

#bai 3===================================================================================
# Quản lý thời gian trong ngày
activities = {
    "Học": 0,
    "Ngủ": 0,
    "Thể dục": 0,
    "Chơi": 0,
    "Di chuyển": 0
}

while True:
    print("\n--- Menu ---")
    print("1. Nhập thêm thời gian")
    print("2. Thống kê thời gian (theo giờ)")
    print("3. Hoạt động nhiều/ít nhất")
    print("0. Thoát")

    choice = input("Chọn chức năng: ")

    if choice == "1":
        act = input("Nhập hoạt động: ")
        minutes = int(input("Nhập số phút: "))
        # Nếu hoạt động chưa có thì thêm mới
        if act not in activities:
            activities[act] = 0
        activities[act] += minutes

    elif choice == "2":
        print("\n--- Thống kê theo giờ ---")
        for act, minutes in activities.items():
            hours = round(minutes / 60, 1)
            print(f"{act}: {hours} giờ")

    elif choice == "3":
        if len(activities) < 2:
            print("Chưa đủ dữ liệu để so sánh!")
        else:
            # Sắp xếp theo số phút giảm dần
            sorted_act = sorted(activities.items(), key=lambda x: x[1], reverse=True)
            print("\nHoạt động nhiều nhất:")
            for act, minutes in sorted_act[:2]:
                print(f"{act}: {minutes} phút")
            print("\nHoạt động ít nhất:")
            for act, minutes in sorted_act[-2:]:
                print(f"{act}: {minutes} phút")

    elif choice == "0":
        print("Kết thúc chương trình.")
        break

    else:
        print("Lựa chọn không hợp lệ!")
