import numpy as np
import matplotlib.pyplot as plt

# Dữ liệu
x = np.linspace(-10, 10, 400)
y = 3*x**5 + 20*x**4 - 10*x**3 - 240*x**2 - 250*x + 200

# Vẽ đồ thị
plt.figure(figsize=(8,6))
plt.plot(x, y, color='darkblue', linewidth=2.5, linestyle='-', label=r'$y = 3x^5 + 20x^4 - 10x^3 - 240x^2 - 250x + 200$')

# Trang trí
plt.xlabel('Trục hoành Ox', fontsize=12)
plt.ylabel('Trục tung Oy', fontsize=12)
plt.title('Đồ thị hàm bậc 5', fontsize=14, fontweight='bold')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

# Giới hạn trục và tỷ lệ
plt.axis('equal')
plt.xlim(-10, 10)
plt.ylim(-10000, 10000)

plt.show()


#bai 2
import matplotlib.pyplot as plt

# Dữ liệu
categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 12, 36, 27]

# Vẽ biểu đồ cột
plt.figure(figsize=(7,5))
plt.bar(categories, values, color='skyblue', edgecolor='black')

plt.title('Biểu đồ cột minh họa', fontsize=14, fontweight='bold')
plt.xlabel('Danh mục')
plt.ylabel('Giá trị')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()

#bai 3
import matplotlib.pyplot as plt

# Dữ liệu
categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 12, 36, 27]

# Vẽ biểu đồ cột
plt.figure(figsize=(7,5))
plt.bar(categories, values, color='skyblue', edgecolor='black')

plt.title('Biểu đồ cột minh họa', fontsize=14, fontweight='bold')
plt.xlabel('Danh mục')
plt.ylabel('Giá trị')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()

#bai 4

import numpy as np
import matplotlib.pyplot as plt

# Sinh dữ liệu ngẫu nhiên
data = np.random.normal(loc=50, scale=10, size=500)

plt.figure(figsize=(7,5))
plt.hist(data, bins=15, color='orange', edgecolor='black', alpha=0.8)

plt.title('Histogram dữ liệu ngẫu nhiên', fontsize=14, fontweight='bold')
plt.xlabel('Giá trị')
plt.ylabel('Tần suất')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()


#bai 5

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Tạo lưới điểm
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z1 = np.sqrt(1 + 0.3*X**2 + 0.3*Y**2)
Z2 = -np.sqrt(1 + 0.3*X**2 + 0.3*Y**2)

# Vẽ bề mặt
fig = plt.figure(figsize=(9,7))
ax = fig.add_subplot(111, projection='3d')

surf1 = ax.plot_surface(X, Y, Z1, cmap='jet', vmin=-5, vmax=5)
surf2 = ax.plot_surface(X, Y, Z2, cmap='jet', vmin=-5, vmax=5)

ax.set_title('Hyperboloid: $-0.3x^2 - 0.3y^2 + z^2 = 1$', fontsize=14, fontweight='bold')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
