# shift_jis の３列の csv フォーマットのデータを Treeview に表示する
#
from builld_grid import *

with open('cp932.txt', encoding='cp932') as fp:
    for line_buffer in fp:
        # 行末の改行を削除する
        line_buffer = line_buffer.rstrip("\n")
        print(line_buffer)
        # カンマで分割
        csv = line_buffer.split(",")
        print(csv)
        # Treeview にセット
        grid.insert("","end",values=(f"{csv[0]}",f"{csv[1]}", f"{csv[2]}"))

# ウインドウ開始
form.mainloop()