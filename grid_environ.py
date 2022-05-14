import os
import tkinter as tk
import tkinter.ttk as ttk

# メインフォーム
form = tk.Tk()
form.title("タイトル")
form.geometry("800x600")

# ツリービュー(表)
grid = ttk.Treeview(form, show="headings")

# 列ID
grid["columns"] = ("番号","変数","値")

# 列幅
grid.column("番号", width=30)
grid.column("変数", width=150)
grid.column("値", width=500)

# タイトル
grid.heading("番号", text="№")
grid.heading("変数", text="変数")
grid.heading("値", text="値")

# データ
i = 0
for k, v in os.environ.items():
    i = i + 1
    grid.insert("","end",values=(i,f"{k}", f"{v}"))

# 位置指定して作成
grid.place(x=20, y=40, height=500)

# スクロールバーを同期させて form に配置
vsb = ttk.Scrollbar(form, orient="vertical", command=grid.yview)
vsb.place(x=20+680+3, y=40+3, height=500)
grid.configure(yscrollcommand=vsb.set)


form.mainloop()