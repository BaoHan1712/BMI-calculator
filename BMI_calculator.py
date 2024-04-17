import tkinter as tk
# Rạo hàm tính BMI
def calculate_bmi():
    # Bắt lỗi 
    try:
        height = float(height_entry.get())
        weight = float(weight_entry.get())
        bmi = weight / (height * height)
        bmi_label.config(text=f"BMI của bạn: {bmi:.2f}")
        
        if bmi < 18.5:
            status_label.config(text="Tình trạng của bạn: Gầy")
            risk_label.config(text="Nguy cơ phát triển bệnh: Thấp")
        elif 18.5 <= bmi <= 24.9:
            status_label.config(text="Tình trạng của bạn: Bình thường")
            risk_label.config(text="Nguy cơ phát triển bệnh: Trung bình")
        elif 25 <= bmi <= 29.9:
            status_label.config(text="Tình trạng của bạn: Hơi béo")
            risk_label.config(text="Nguy cơ phát triển bệnh: Cao")
        else:
            status_label.config(text="Tình trạng của bạn: Béo phì")
            risk_label.config(text="Nguy cơ phát triển bệnh: Rất cao")
# nếu xảy ra lỗi thì chạy đoạn code này 
    except ValueError:
        bmi_label.config(text="Vui lòng nhập chiều cao và cân nặng hợp lệ.")
# tạo cửa sổ chính
root = tk.Tk()
# tiêu đề
root.title("BMI Calculator")
# Size bảng xét
root.geometry("250x300") 
# Cửa sổ chiều cao
tk.Label(root,height= 2,text="Nhập chiều cao (m):").pack()
# tạo ô trống để nhập vào
height_entry = tk.Entry(root)
height_entry.pack()
# Cửa sổ cân nặng
tk.Label(root, height= 2,text="Nhập cân nặng (kg):").pack()
# tạo ô trống để nhập vào
weight_entry = tk.Entry(root)
weight_entry.pack()
# Nút BMI
calculate_button = tk.Button(root,bd = 2,text='Tính BMI', command=calculate_bmi)
calculate_button.pack(padx=10, pady=20)
# Hiển thị số BMI
bmi_label = tk.Label(root, text="")
bmi_label.pack()
# Hiển thị trạng thái
status_label = tk.Label(root, text="")
status_label.pack()
# Hiển thị độ nguy hiểm 
risk_label = tk.Label(root, text="")
risk_label.pack()
# phá hủy cửa sổ
exit_button = tk.Button(root,text='Thoát', command=root.destroy)
exit_button.pack()
# Chạy vòng lặp
root.mainloop()