# This program is to generate Chinese number from 0 to 9999 9999 9999 to verity if any bug in CN_num_convert.py

from CN_num_convert import cn_num2num
from CN_num_generate import num2cn_num

# ==============main================
choice = input("需要进行的操作：\n1.输出0~9999 9999 9999的汉字数字\n2.校验CN_num_convert.py")
if choice == "1":
    for i in range(0, 1000000000000):
        print(num2cn_num(i))

elif choice == "2":
    for i in range(0, 1000000000000):
        pass
        # if_equal =