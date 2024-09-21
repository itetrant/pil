# Nhập số a từ bàn phím
a = float(input("Nhập số a: "))

# Nhập số b từ bàn phím
b = float(input("Nhập số b: "))

# Kiểm tra nếu b khác 0 để tránh chia cho 0
if b != 0:
    result = a / b
    print(f"Kết quả của {a} / {b} là: {result}")
else:
    print("Lỗi: Không thể chia cho 0!")



