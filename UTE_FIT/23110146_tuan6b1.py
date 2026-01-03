import math
#bai 1
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2

    def show_info(self):
        print(f"Hình tròn bán kính = {self.radius}")
        print(f"Chu vi = {self.perimeter():.2f}")
        print(f"Diện tích = {self.area():.2f}")

#bai2
class Triangle:
    def __init__(self, a, b, c, color="Không màu"):
        self.a = a
        self.b = b
        self.c = c
        self.color = color

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def triangle_type(self):
        a, b, c = self.a, self.b, self.c
        # Sắp xếp để kiểm tra tam giác vuông
        sides = sorted([a, b, c])
        x, y, z = sides  # x^2 + y^2 ?= z^2
        is_right = math.isclose(x**2 + y**2, z**2)

        if a == b == c:
            return "Tam giác đều"
        elif a == b or b == c or a == c:
            if is_right:
                return "Tam giác vuông cân"
            return "Tam giác cân"
        elif is_right:
            return "Tam giác vuông"
        else:
            return "Tam giác thường"

    def show_info(self):
        print(f"Tam giác cạnh ({self.a}, {self.b}, {self.c}), màu sắc: {self.color}")
        print(f"Chu vi = {self.perimeter():.2f}")
        print(f"Diện tích = {self.area():.2f}")
        print(f"Loại: {self.triangle_type()}")


#bai3 

class ToanHoc:
    def __init__(self, *nso):
        self.numbers = nso

    def TinhTong(self):
        return sum(self.numbers)

    def TinhTrungBinh(self):
        return sum(self.numbers) / len(self.numbers) if self.numbers else 0

    def TimMax(self):
        return max(self.numbers)

    def TimMin(self):
        return min(self.numbers)

    def HienThi(self):
        print("Các số:", self.numbers)
        print("Tổng =", self.TinhTong())
        print("Trung bình =", self.TinhTrungBinh())
        print("Max =", self.TimMax())
        print("Min =", self.TimMin())



#bai4
import json

class MonHoc:
    def __init__(self, ma_mon, ten_mon, so_tiet):
        self.ma_mon = ma_mon
        self.ten_mon = ten_mon
        self.so_tiet = so_tiet

    def to_dict(self):
        return {
            "ma_mon": self.ma_mon,
            "ten_mon": self.ten_mon,
            "so_tiet": self.so_tiet
        }

class HocVien:
    def __init__(self, so_dinh_danh, ho_ten, nam_sinh, ds_mon):
        self.so_dinh_danh = so_dinh_danh
        self.ho_ten = ho_ten
        self.nam_sinh = nam_sinh
        self.ds_mon = ds_mon  # danh sách MonHoc

    def to_dict(self):
        return {
            "so_dinh_danh": self.so_dinh_danh,
            "ho_ten": self.ho_ten,
            "nam_sinh": self.nam_sinh,
            "ds_mon": [mon.to_dict() for mon in self.ds_mon]
        }

class QuanLyHocVien:
    FILE_NAME = "dssv.txt"

    def __init__(self):
        self.danh_sach = []

    def nhap_hoc_vien(self):
        so_dinh_danh = input("Nhập số CMND/CCCD/GKS: ")
        ho_ten = input("Nhập họ tên: ")
        nam_sinh = input("Nhập năm sinh: ")

        ds_mon = []
        n = int(input("Số môn học đăng ký: "))
        for i in range(n):
            print(f"--- Môn học {i+1} ---")
            ma_mon = input("Mã môn: ")
            ten_mon = input("Tên môn: ")
            so_tiet = int(input("Số tiết: "))
            ds_mon.append(MonHoc(ma_mon, ten_mon, so_tiet))

        hv = HocVien(so_dinh_danh, ho_ten, nam_sinh, ds_mon)
        self.danh_sach.append(hv)
        self.ghi_file()
        print("✅ Đã thêm học viên và lưu file!")

    def ghi_file(self):
        with open(self.FILE_NAME, "w", encoding="utf-8") as f:
            json.dump([hv.to_dict() for hv in self.danh_sach], f, ensure_ascii=False, indent=4)

    def doc_file(self):
        try:
            with open(self.FILE_NAME, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.danh_sach = []
                for hv in data:
                    ds_mon = [MonHoc(m["ma_mon"], m["ten_mon"], m["so_tiet"]) for m in hv["ds_mon"]]
                    self.danh_sach.append(HocVien(hv["so_dinh_danh"], hv["ho_ten"], hv["nam_sinh"], ds_mon))
        except FileNotFoundError:
            self.danh_sach = []

    def hien_thi_hoc_vien(self):
        self.doc_file()
        print("\n=== DANH SÁCH HỌC VIÊN ===")
        for hv in self.danh_sach:
            print(f"ID: {hv.so_dinh_danh}, Họ tên: {hv.ho_ten}, Năm sinh: {hv.nam_sinh}")
            for mon in hv.ds_mon:
                print(f"   -> {mon.ma_mon} - {mon.ten_mon} ({mon.so_tiet} tiết)")

    def hoc_vien_it_nhat_hai_mon(self):
        self.doc_file()
        print("\n=== HỌC VIÊN ĐĂNG KÝ ≥ 2 MÔN ===")
        for hv in self.danh_sach:
            if len(hv.ds_mon) >= 2:
                print(f"{hv.ho_ten} ({hv.so_dinh_danh}) - Số môn: {len(hv.ds_mon)}")

    def mon_hoc_duoc_dang_ky_nhieu_nhat(self):
        self.doc_file()
        dem_mon = {}
        for hv in self.danh_sach:
            for mon in hv.ds_mon:
                dem_mon[mon.ten_mon] = dem_mon.get(mon.ten_mon, 0) + 1
        if dem_mon:
            max_mon = max(dem_mon, key=dem_mon.get)
            print(f"\n📌 Môn học được nhiều học viên đăng ký nhất: {max_mon} ({dem_mon[max_mon]} HV)")

    def thong_ke_hoc_vien_theo_mon(self):
        self.doc_file()
        dem_mon = {}
        for hv in self.danh_sach:
            for mon in hv.ds_mon:
                dem_mon[mon.ten_mon] = dem_mon.get(mon.ten_mon, 0) + 1
        print("\n=== THỐNG KÊ HỌC VIÊN TRÊN MỖI MÔN ===")
        for mon, so_hv in dem_mon.items():
            print(f"{mon}: {so_hv} học viên")


# ========================
# CHƯƠNG TRÌNH CHÍNH
# ========================
if __name__ == "__main__":
    ql = QuanLyHocVien()
    while True:
        print("\n===== MENU =====")
        print("1. Nhập học viên")
        print("2. Hiển thị danh sách học viên")
        print("3. Hiển thị học viên đăng ký ≥ 2 môn")
        print("4. Môn học nhiều học viên đăng ký nhất")
        print("5. Thống kê học viên/môn")
        print("0. Thoát")
        chon = input("Chọn: ")

        if chon == "1":
            ql.nhap_hoc_vien()
        elif chon == "2":
            ql.hien_thi_hoc_vien()
        elif chon == "3":
            ql.hoc_vien_it_nhat_hai_mon()
        elif chon == "4":
            ql.mon_hoc_duoc_dang_ky_nhieu_nhat()
        elif chon == "5":
            ql.thong_ke_hoc_vien_theo_mon()
        elif chon == "0":
            break
        else:
            print("❌ Lựa chọn không hợp lệ!")



from abc import ABC, abstractmethod
import math

# Lớp trừu tượng
class Hinh(ABC):
    @abstractmethod
    def tinh_chu_vi(self):
        pass

    @abstractmethod
    def tinh_dien_tich(self):
        pass


class HinhTron(Hinh):
    def __init__(self, ban_kinh):
        self.r = ban_kinh

    def tinh_chu_vi(self):
        return 2 * math.pi * self.r

    def tinh_dien_tich(self):
        return math.pi * self.r**2


class HinhChuNhat(Hinh):
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong

    def tinh_chu_vi(self):
        return 2 * (self.dai + self.rong)

    def tinh_dien_tich(self):
        return self.dai * self.rong


class HinhTamGiac(Hinh):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def tinh_chu_vi(self):
        return self.a + self.b + self.c

    def tinh_dien_tich(self):
        p = self.tinh_chu_vi() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))


# Test
ds_hinh = [
    HinhTron(5),
    HinhChuNhat(4, 6),
    HinhTamGiac(3, 4, 5)
]

for h in ds_hinh:
    print(f"{h.__class__.__name__}: Chu vi = {h.tinh_chu_vi():.2f}, Diện tích = {h.tinh_dien_tich():.2f}")



#bai6
import json

class MonHoc:
    def __init__(self, ma_mon, ten_mon, so_tiet):
        self.ma_mon = ma_mon
        self.ten_mon = ten_mon
        self.so_tiet = so_tiet

    def __repr__(self):
        return f"{self.ma_mon}-{self.ten_mon} ({self.so_tiet} tiết)"


class HocVien:
    def __init__(self, cmnd, ho_ten, nam_sinh, ds_mon):
        self.cmnd = cmnd
        self.ho_ten = ho_ten
        self.nam_sinh = nam_sinh
        self.ds_mon = ds_mon

    def to_dict(self):
        return {
            "cmnd": self.cmnd,
            "ho_ten": self.ho_ten,
            "nam_sinh": self.nam_sinh,
            "ds_mon": [mon.__dict__ for mon in self.ds_mon]
        }

    def __repr__(self):
        return f"{self.ho_ten} ({self.nam_sinh}), Môn: {self.ds_mon}"


class QuanLyHocVien:
    def __init__(self, filename="dssv.txt"):
        self.filename = filename
        self.ds_hv = []

    def nhap_hoc_vien(self, hv):
        self.ds_hv.append(hv)
        self.luu_file()

    def luu_file(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump([hv.to_dict() for hv in self.ds_hv], f, ensure_ascii=False, indent=4)

    def doc_file(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.ds_hv = [HocVien(d["cmnd"], d["ho_ten"], d["nam_sinh"],
                                      [MonHoc(**m) for m in d["ds_mon"]]) for d in data]
        except FileNotFoundError:
            self.ds_hv = []

    def hien_thi(self):
        for hv in self.ds_hv:
            print(hv)

    def hv_it_nhat_2_mon(self):
        for hv in self.ds_hv:
            if len(hv.ds_mon) >= 2:
                print(hv)

    def mon_duoc_dk_nhieu_nhat(self):
        dem = {}
        for hv in self.ds_hv:
            for mon in hv.ds_mon:
                dem[mon.ten_mon] = dem.get(mon.ten_mon, 0) + 1
        max_mon = max(dem, key=dem.get)
        print(f"Môn được đăng ký nhiều nhất: {max_mon} ({dem[max_mon]} học viên)")

    def thong_ke(self):
        dem = {}
        for hv in self.ds_hv:
            for mon in hv.ds_mon:
                dem[mon.ten_mon] = dem.get(mon.ten_mon, 0) + 1
        print("Thống kê số học viên trên mỗi môn:")
        for ten_mon, so_hv in dem.items():
            print(f"- {ten_mon}: {so_hv}")


#bai7
from abc import ABC, abstractmethod

class GiaoDich(ABC):
    def __init__(self, ma_gd, ngay, don_gia, so_luong):
        self.ma_gd = ma_gd
        self.ngay = ngay
        self.don_gia = don_gia
        self.so_luong = so_luong

    @abstractmethod
    def thanh_tien(self):
        pass


class GiaoDichVang(GiaoDich):
    def __init__(self, ma_gd, ngay, don_gia, so_luong, loai_vang):
        super().__init__(ma_gd, ngay, don_gia, so_luong)
        self.loai_vang = loai_vang

    def thanh_tien(self):
        return self.so_luong * self.don_gia

    def __repr__(self):
        return f"[Vàng] {self.ma_gd} - {self.loai_vang} - {self.thanh_tien()}"


class GiaoDichTienTe(GiaoDich):
    def __init__(self, ma_gd, ngay, ti_gia, so_luong, loai_tien, loai_gd):
        super().__init__(ma_gd, ngay, ti_gia, so_luong)
        self.loai_tien = loai_tien
        self.loai_gd = loai_gd.lower()

    def thanh_tien(self):
        if self.loai_gd == "mua":
            return self.so_luong * self.don_gia
        elif self.loai_gd == "bán":
            return (self.so_luong * self.don_gia) * 1.05
        return 0

    def __repr__(self):
        return f"[Tiền tệ] {self.ma_gd} - {self.loai_tien} - {self.loai_gd} - {self.thanh_tien()}"


# Quản lý giao dịch
class QuanLyGiaoDich:
    def __init__(self):
        self.ds_gd = []

    def them_gd(self, gd):
        self.ds_gd.append(gd)

    def hien_thi(self):
        for gd in self.ds_gd:
            print(gd)

    def tong_sl_theo_loai(self):
        dem = {}
        for gd in self.ds_gd:
            loai = gd.__class__.__name__
            dem[loai] = dem.get(loai, 0) + gd.so_luong
        return dem

    def tong_tt_theo_loai(self):
        dem = {}
        for gd in self.ds_gd:
            loai = gd.__class__.__name__
            dem[loai] = dem.get(loai, 0) + gd.thanh_tien()
        return dem
