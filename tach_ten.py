# Nhập họ và tên từ bàn phím
'Nguyễn Phúc Thiên Bảo' 

# Tách họ và tên
['Nguyễn','Phúc','Thiên','Bảo'] 

# Kiểm tra xem có đủ phần để tách không
if len(['Nguyễn','Phúc','Thiên','Bảo'] ) >= 2:
    last_name = ['Nguyễn','Phúc','Thiên','Bảo'] [0]  # Họ
    first_name = " ".join(['Nguyễn','Phúc','Thiên','Bảo'] [1:])  # Tên
    print(f"Họ: {last_name}")
    print(f"Tên: {first_name}")
else:
    print("Nguyễn Phúc Thiên Bảo")
