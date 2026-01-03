#ma tran xoan oc
def xoanoc(n):
    matrix = [[0] * n for _ in range(n)]
    num = 1
    top, bottom, left, right = 0, n - 1, 0, n - 1

    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 2
        top += 1

        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 2
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 2
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 2
            left += 1

    return matrix
# tổng các phần tử trên đường chéo phu
def tong_duong_cheo_chinh(matrix):
    n = len(matrix)
    tong = 0
    for i in range(n):
        tong += matrix[i][n-i-1]
    return tong

x = int(input("Nhập kích thước ma trận vuông n x n: "))
matrix = xoanoc(x)
for row in matrix:
    print(row)  
print("Tổng các phần tử trên đường chéo chính:", tong_duong_cheo_chinh(matrix)) 

#======================================================================================
n = int(input("Nhập kích thước ma trận vuông n x n: "))

#  duong cheo song song voi duong cheo chinh,cach deu k don vi 
def duong_cheo_song_song(matrix,k):
    n = len(matrix)
    duong_cheo = []
    for i in range(n):
        duong_cheo.append(matrix[i][n-i-1+k])
    return duong_cheo
k = int(input("Nhập k (k > 0): "))
print("Đường chéo song song với đường chéo chính cách đều k đơn vị:", duong_cheo_song_song(matrix, k))

#======================================================================================

#to o vuong trai sang phai , phai sang trai giam dan tu n -> n-i + 1
N, c = map(int, input().split())

count = 0
for i in range(1, N+1):   # duyệt từng dòng
    if i % 2 == 1:  # dòng lẻ
        if c <= N - i + 1:
            count += 1
    else:           # dòng chẵn
        if c >= i:
            count += 1

print(count)
#======================================================================================
#xoan oc so : mot luoi vo han co o vuong trai tren chua so 1
R, C = map(int, input().split())

# hoán đổi theo công thức
r = C
c = R

if r <= c:
    if c % 2 == 0:
        ans = c*c - r + 1
    else:
        ans = (c-1)*(c-1) + r
else:
    if r % 2 == 0:
        ans = (r-1)*(r-1) + c
    else:
        ans = r*r - c + 1

print(ans)
#======================================================================================
a = int(input())
b = int(input())
c = int(input())
d = int(input())
solonnhat = max(a,b,c,d)
hvt1 = max - a
hvt2 = max - b
hvt3 = max - c
hvt4 = max - d
dapan = 2*(hvt1 + hvt2 + hvt3 + hvt4)
dapan1 = 2*dapan


