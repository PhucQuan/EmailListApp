#bai2

class Address:
    def __init__(self, so_nha, duong, quan, thanh_pho):
        self.so_nha = so_nha
        self.duong = duong
        self.quan = quan
        self.thanh_pho = thanh_pho

    def __str__(self):
        return f"{self.so_nha}, {self.duong}, {self.quan}, {self.thanh_pho}"


class NhanVien:
    def __init__(self, ho_ten, ngay_sinh, dia_chi: Address):
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.dia_chi = dia_chi

    def tinhLuong(self):
        pass

    def inThongTin(self):
        print(f"Name: {self.ho_ten}, DOB: {self.ngay_sinh}, Address: {self.dia_chi}, Salary: {self.tinhLuong()}")


class NhanVienSanXuat(NhanVien):
    def __init__(self, ho_ten, ngay_sinh, dia_chi, luong_cb, so_san_pham):
        super().__init__(ho_ten, ngay_sinh, dia_chi)
        self.luong_cb = luong_cb
        self.so_san_pham = so_san_pham

    def tinhLuong(self):
        return self.luong_cb + self.so_san_pham * 5000


class NhanVienVanPhong(NhanVien):
    def __init__(self, ho_ten, ngay_sinh, dia_chi, so_ngay_lam):
        super().__init__(ho_ten, ngay_sinh, dia_chi)
        self.so_ngay_lam = so_ngay_lam

    def tinhLuong(self):
        return self.so_ngay_lam * 100000


# Demo
nv_sx_list = [
    NhanVienSanXuat("A", "01/01/1990", Address("12", "Nguyen Trai", "Q1", "HCM"), 3000000, 200),
    NhanVienSanXuat("B", "02/02/1992", Address("45", "Le Loi", "Q3", "HCM"), 2800000, 150)
]

nv_vp_list = [
    NhanVienVanPhong("C", "03/03/1995", Address("78", "Hai Ba Trung", "Q1", "HCM"), 22),
    NhanVienVanPhong("D", "04/04/1998", Address("99", "Ly Thuong Kiet", "Q10", "HCM"), 25)
]

print("=== Nhân viên sản xuất ===")
for nv in nv_sx_list:
    nv.inThongTin()

print("\n=== Nhân viên văn phòng ===")
for nv in nv_vp_list:
    nv.inThongTin()