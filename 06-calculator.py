import tkinter as tk

# RGB 색상 값을 프로그래머가 직접 지정
# 예: 연한 노란색
rgb_color = (255, 150, 224)  # Light yellow


# RGB를 16진수 색상 코드로 변환하는 함수
def rgb_to_hex(rgb):
    return "#%02x%02x%02x" % rgb

# 지정된 RGB 색상을 16진수 코드로 변환
color_code = rgb_to_hex(rgb_color)


def on_click(button_text):
    # 버튼 클릭 이벤트 처리, 이벤트 객체 대신 문자열을 받음
    if button_text == "C":
        entry.delete(0, tk.END)
    elif button_text == "=":
        try:
            entry_text = entry.get()
            result = str(eval(entry_text))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, button_text)



# 메인 윈도우 설정
root = tk.Tk()
root.title("Calculator")
root.configure(bg=color_code)  # 메인 윈도우의 배경색 변경

# 입력 필드 생성
entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# 버튼 생성
buttons = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', '*',
    'C', '0', '=', '/'
]

for i, button in enumerate(buttons):
    tk.Button(root, text=button, width=9, height=4, bg=color_code, command=lambda button=button: on_click(button)).grid(row=(i//4)+1, column=i%4)

root.bind("<Return>", on_click)

root.mainloop()
