'''
\_\_del__ 刪除函數<br>
當刪除時調用<br>
但變量超過一定量，python intepreter會自動執行篩除的函數功能<br><br>
這裡容易產生誤會<br>
不是由__del__定義 del的行為<br>
而是執行del 動作時，而且引用數記數為零時，調用__del__函數<br>
'''

import sys

class Display_del_cls():
    def __del__(self):
        print("I am deleted!!")

cls = Display_del_cls()
print(sys.getrefcount(cls)) #getrefcount 本身也是一次調用
del cls #觸發__del__

cls = Display_del_cls()
cls = None #觸發__del__

cls = Display_del_cls()
cls1 = cls
print(sys.getrefcount(cls))
del cls1 #不會觸發__del__
print(sys.getrefcount(cls))
del cls #觸發__del__