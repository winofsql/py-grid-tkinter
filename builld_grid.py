import tkinter as tk
import tkinter.ttk as ttk

# メインフォーム
form = tk.Tk()
form.title("タイトル")
form.geometry("800x600")

# ツリービュー(表)
grid = ttk.Treeview(form, show="headings")

# 列ID
grid["columns"] = ("A","B","C")

# 列幅
grid.column("A", width=150)
grid.column("B", width=150)
grid.column("C", width=150)

# タイトル
grid.heading("A", text="A")
grid.heading("B", text="B")
grid.heading("C", text="C")

# 位置指定して作成
grid.place(x=20, y=40, height=500)

# スクロールバーを同期させて form に配置
vsb = ttk.Scrollbar(form, orient="vertical", command=grid.yview)
vsb.place(x=20+450+3, y=40+3, height=500)
grid.configure(yscrollcommand=vsb.set)

form.mainloop()
