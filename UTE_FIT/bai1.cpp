#include <iostream>
#include <chrono>
using namespace std;
using namespace std::chrono;

const int N = 1000;

int main() {
    int a[N][N];
     int b[N][N];
     long long c[N][N]; // dùng long long để tránh tràn số nếu lớn

    // Khởi tạo ma trận toàn 1
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            a[i][j] = 1;
            b[i][j] = 1;
            c[i][j] = 0;
        }
    }

    auto start = high_resolution_clock::now();

    // Nhân ma trận
    for (int i = 0; i < N; i++) {
        for (int k = 0; k < N; k++) {
            for (int j = 0; j < N; j++) {
                c[i][j] += (long long)a[i][k] * b[k][j];
            }
        }
    }

    auto end = high_resolution_clock::now();
    auto duration = duration_cast<milliseconds>(end - start);

    cout << "Kich thuoc ket qua c: " << N << " x " << N << endl;
    cout << "Gia tri phan tu dau tien c[0][0]: " << c[0][0] << endl;
    cout << "Thoi gian chay: " << duration.count() << " ms" << endl;

    return 0;
}
