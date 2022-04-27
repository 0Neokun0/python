#モジュール読込
import requests
import tkinter as tk
base = tk.Tk()

# 関数定義(function)
def push() :
    print('押された')
    url = "https://roboticsandautomationnews.com/wp-content/uploads/2020/04/web-scraping-2.png"
    response = requests.get(url)
    file = open("downloads\downloads.jpg","wb")
    #iter_content()メソッドでWebファイルのデータを渡す
    for chunk in response.iter_content(100000):
        #ファイル書込
        file.write(chunk)
    
    #ファイルを閉じる
    file.close()
    print('完了')

button = tk.Button(base,text='ボタン', command=push).pack()
base.mainloop()
