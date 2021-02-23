from tkinter import *
import os
import tkinter.messagebox as msgbox

root = Tk()
root.title("제목 없음 - Windows 메모장")
root.geometry("640x480")
root.resizable(True, True)

filename = "C:\JB\Coding\Python\Practice\inflearn_lecture\gui_basic\퀴즈 예제.txt"

# 동작 함수
def openfile():
    if os.path.isfile(filename):    # 파일 있으면 True, 없으면 False
        with open(filename, "r", encoding="utf8") as file:
            text.delete("1.0", END)         # 텍스트 위젯 본문 삭제
            text.insert(END, file.read())   # 파일 내용을 본문에 입력

    else:
        msgbox.showerror("오류", "파일이 없습니다.")

def savefile():
    with open(filename, "w", encoding="utf8") as file:
        file.write(text.get("1.0", END))              # 모든 내용을 가져와서 저장
    
    msgbox.showinfo("알림", "저장이 완료되었습니다.")

menu = Menu(root)

# 파일 메뉴
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=openfile)
menu_file.add_command(label="저장", command=savefile)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=root.quit)
menu.add_cascade(label="파일", menu=menu_file)

# 편집, 서식, 보기, 도움말 메뉴
menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")

root.config(menu=menu)

# 본문
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

text = Text(root, yscrollcommand=scrollbar.set)
text.pack(fill="both", expand=True)

scrollbar.config(command=text.yview)

root.mainloop()