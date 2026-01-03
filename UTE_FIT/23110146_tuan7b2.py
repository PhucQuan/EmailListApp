import pandas as pd
import matplotlib.pyplot as plt

#bai1 a
# Đọc dữ liệu
df = pd.read_csv("Churn_Modelling.csv", header=0, index_col="RowNumber")

# Xem 5 dòng đầu
print(df.head())
print(df.describe())              # thống kê cột số
print(df.describe(include="all")) # thống kê cả số + phân loại
#c)
mean_credit = df.groupby("Geography")["CreditScore"].mean()
print(mean_credit)

#d  
df["AgeGroup"] = pd.qcut(df["Age"], q=5, labels=["G1","G2","G3","G4","G5"])
print(df["AgeGroup"].value_counts())

#e
df["AgeGroup"].value_counts().sort_index().plot.bar(color="skyblue")

plt.title("Số lượng khách hàng theo nhóm độ tuổi")
plt.xlabel("Nhóm tuổi")
plt.ylabel("Số lượng khách hàng")
plt.show()

#bai2
# chipotle_analysis.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# a) đọc dữ liệu (giả sử file là 'chipotle.tsv', phân tách bằng '\t')
df = pd.read_csv('chipotle.tsv', sep='\t')

# Hiện vài dòng để kiểm tra
print("Head of chipotle data:")
print(df.head())

# Một số xử lý cơ bản: nếu cột price tên khác, in tên cột:
print("\nColumns:", df.columns.tolist())

# Trong dataset chipotle classic có các cột: order_id, quantity, item_name, choice_description, item_price
# b) Liệt kê những sản phẩm có giá hơn 10$ (lược bỏ dòng trùng tên sản phẩm)
# Trước hết chuẩn hóa cột item_price (xóa '$' và chuyển thành float)
def price_to_float(s):
    try:
        return float(str(s).replace('$','').strip())
    except:
        return np.nan

if 'item_price' in df.columns:
    df['item_price_float'] = df['item_price'].apply(price_to_float)
else:
    # nếu dữ liệu lưu giá ở cột khác, in thông báo
    raise KeyError("Không tìm thấy cột 'item_price' trong file. Kiểm tra tên cột.")

# Lọc sản phẩm có price > 10, lược bỏ trùng tên sản phẩm (item_name)
products_over_10 = df[df['item_price_float'] > 10]['item_name'].drop_duplicates().reset_index(drop=True)
print("\nProducts with price > $10 (unique names):")
print(products_over_10.to_list())

# c) Sắp xếp các sản phẩm theo tên
products_sorted = products_over_10.sort_values().reset_index(drop=True)
print("\nProducts > $10 sorted by name:")
print(products_sorted.to_list())

# d) Tìm sản phẩm có giá cao nhất trong danh sách
max_price = df['item_price_float'].max()
# Có thể có nhiều dòng có giá max (cùng item_name hoặc khác). Lấy tên sản phẩm tương ứng
most_expensive_items = df[df['item_price_float'] == max_price]['item_name'].unique()
print(f"\nMax price = ${max_price:.2f}. Items with this price: {most_expensive_items.tolist()}")

# e) Sản phẩm "Veggie Salad Bowl" xuất hiện trong bao nhiêu đơn hàng và tổng số lượng được đặt
target = "Veggie Salad Bowl"
if 'item_name' in df.columns:
    veggie_rows = df[df['item_name'] == target]
    order_count = veggie_rows['order_id'].nunique()
    total_quantity = veggie_rows['quantity'].sum()
    print(f"\n'{target}' appears in {order_count} orders with total quantity = {total_quantity}")
else:
    print("Không tìm thấy cột 'item_name'.")

# f) Vẽ histogram cho 5 sản phẩm được mua nhiều nhất với tần suất mua
# Tần suất mua: tổng quantity theo item_name
quantity_by_item = df.groupby('item_name')['quantity'].sum().sort_values(ascending=False)
top5 = quantity_by_item.head(5)
print("\nTop 5 most purchased items (by total quantity):")
print(top5)

# Plot histogram (bar chart) cho top5
plt.figure(figsize=(8,5))
top5.plot(kind='bar')
plt.title('Top 5 sản phẩm được mua nhiều nhất (tổng quantity)')
plt.xlabel('Item')
plt.ylabel('Total quantity purchased')
plt.tight_layout()
plt.show()

# g) Vẽ scatter: số lượng mặt hàng được đặt trên mỗi đơn hàng
# Cần tổng số mặt hàng (sum quantity) theo order_id
items_per_order = df.groupby('order_id')['quantity'].sum().reset_index()
# Scatter: x = order_id (hoặc chỉ index), y = total quantity
plt.figure(figsize=(8,5))
plt.scatter(items_per_order['order_id'], items_per_order['quantity'])
plt.title('Số lượng mặt hàng (tổng quantity) trên mỗi order')
plt.xlabel('Order ID')
plt.ylabel('Total items in order')
plt.tight_layout()
plt.show()

#bai 3
# user_analysis.py
import pandas as pd
import numpy as np

# a) đọc dữ liệu
cols = ['user_id','age','gender','occupation','zip_code']
users = pd.read_csv('u.user', sep='|', names=cols, engine='python')

print("Head of u.user:")
print(users.head())

# b) độ tuổi trung bình của mỗi nghề nghiệp
age_mean_by_occ = users.groupby('occupation')['age'].mean().sort_index()
print("\nAverage age by occupation:")
print(age_mean_by_occ)

# c) tỷ lệ (count) theo nghề (và sắp xếp từ cao xuống thấp)
occ_counts = users['occupation'].value_counts().sort_values(ascending=False)
occ_percentage = (occ_counts / len(users)) * 100
print("\nCounts by occupation (desc):")
print(occ_counts)
print("\nPercentage by occupation (desc):")
print(occ_percentage)

# d) với mỗi nghề nghiệp, độ tuổi nhỏ nhất và lớn nhất
age_min_max = users.groupby('occupation')['age'].agg(['min','max'])
print("\nMin and max age by occupation:")
print(age_min_max)

# e) với mỗi tổ hợp nghề nghiệp - giới tính, tính tuổi trung bình
mean_age_occ_gender = users.groupby(['occupation','gender'])['age'].mean().unstack(fill_value=np.nan)
print("\nAverage age by occupation and gender:")
print(mean_age_occ_gender)

# f) với mỗi nghề nghiệp, tỷ lệ phần trăm nam - nữ
occ_gender_counts = users.groupby(['occupation','gender'])['user_id'].count().unstack(fill_value=0)
occ_gender_percent = occ_gender_counts.div(occ_gender_counts.sum(axis=1), axis=0) * 100
print("\nPercentage male/female by occupation:")
print(occ_gender_percent)
# ===============================================

#bai 4 
# wind_analysis.py
import pandas as pd
import numpy as np

# a) đọc dữ liệu
# Thử đọc với delim_whitespace; nếu file có header, pd.read_table sẽ tự parse. 
wind = pd.read_csv('wind.data', delim_whitespace=True, header=0)
print("Head of wind.data:")
print(wind.head())

# b) Hợp nhất ba cột đầu tiên thành 'Yr_Mo_Dy' theo định dạng yyyy-MM-dd
# Tạo cột datetime
wind['Yr_Mo_Dy'] = pd.to_datetime(wind[['Yr','Mo','Dy']])
# convert to string format yyyy-MM-dd
wind['Yr_Mo_Dy'] = wind['Yr_Mo_Dy'].dt.strftime('%Y-%m-%d')
print("\nSample Yr_Mo_Dy:")
print(wind['Yr_Mo_Dy'].head())

# c) Đặt cột mới làm chỉ mục
wind2 = wind.set_index('Yr_Mo_Dy')
print("\nIndex set to Yr_Mo_Dy; head:")
print(wind2.head())

# d) Số lượng giá trị hiện có và còn thiếu ở các cột từ RPT → MAL
# Giả sử cột RPT là thứ 4 và MAL là cột cuối cùng; chọn các cột theo tên nếu tồn tại
cols = list(wind.columns)
try:
    start_idx = cols.index('RPT')
    end_idx = cols.index('MAL')
    selected_cols = cols[start_idx:end_idx+1]
except ValueError:
    # nếu không tìm thấy tên RPT/MAL, thử lấy từ cột thứ 3 đến hết
    selected_cols = cols[3:]
print("\nSelected columns for missingness check:", selected_cols)

presence = pd.DataFrame({
    'non_na_count': wind2[selected_cols].count(),
    'na_count': wind2[selected_cols].isna().sum()
})
print("\nNon-missing and missing counts for selected columns:")
print(presence)

# e) Tính tốc độ giá trung bình của toàn bộ dữ liệu (mọi nơi và mọi thời điểm)
# Giả sử các cột vị trí đều numeric; flatten tất cả giá trị vị trí sang một mảng
all_values = wind2[selected_cols].values.flatten()
mean_speed = np.nanmean(all_values)
print(f"\nOverall mean wind speed (all places, all times): {mean_speed:.4f}")

# f) Tạo DataFrame loc_stats: min, max, mean, std của mỗi vị trí
loc_stats = wind2[selected_cols].agg(['min','max','mean','std']).transpose()
loc_stats = loc_stats.rename(columns={'min':'min_speed','max':'max_speed','mean':'mean_speed','std':'std_speed'})
print("\nloc_stats (min, max, mean, std) for each location:")
print(loc_stats)

# g) Tìm tốc độ gió trung bình trong tháng 1 ở mỗi nơi
# index hiện là 'Yr_Mo_Dy' string; chuyển lại thành DatetimeIndex để filter tháng
wind_dt = wind.copy()
wind_dt['date'] = pd.to_datetime(wind_dt[['Yr','Mo','Dy']])
wind_dt = wind_dt.set_index('date')
jan_means = wind_dt[wind_dt.index.month == 1][selected_cols].mean()
print("\nMean wind speed in January for each location:")
print(jan_means)

# h) Giảm dữ liệu: thống kê theo từng năm, theo month-year, theo tuần-month-year
# convert index to datetime if not
wind_dt = wind_dt.copy()
# By year
by_year = wind_dt[selected_cols].groupby(wind_dt.index.year).agg(['mean','min','max','std'])
print("\nStatistics by year (sample):")
print(by_year.head())

# By month-year
by_month_year = wind_dt[selected_cols].groupby([wind_dt.index.year, wind_dt.index.month]).agg(['mean','min','max','std'])
print("\nStatistics by month-year (sample):")
print(by_month_year.head())

# By week-year-month: sử dụng year, month, week number
by_week = wind_dt[selected_cols].groupby([wind_dt.index.year, wind_dt.index.month, wind_dt.index.isocalendar().week]).agg(['mean','min','max','std'])
print("\nStatistics by year-month-week (sample):")
print(by_week.head())

