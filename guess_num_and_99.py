#!/usr/bin/env python3
#coding:utf-8
'''print("**********九九乘法口诀表**********")
for i in range(1,10):
    for j in range(1,i+1):
        print(j,"×",i,"=",i * j,end = "\t")
    print()

#方法二：用递归
def cal(num):
    while num <= 9:
        for i in range(1,num + 1):
            print( i,"×",num,"=", i * num,end= "   ")
        print()
        return cal(num + 1)
cal(1)
'''
import random
print("**********猜字游戏**********")
sys_num = random.randint(100,500)
usr_answer = None
guess_time = 0
while usr_answer != "n" and usr_answer != "N":
    usr_num = int(input("请输入一个100-500之间的整数：\n"))
    guess_time += 1
    if usr_num > sys_num:
        print("猜大了，再输入小一些！\n你已经猜了",guess_time,"次。\n------------------------------")
    elif usr_num < sys_num:
        print("猜小了，再输入大一些！\n你已经猜了",guess_time,"次。\n------------------------------")
    else:
        print("恭喜你猜对啦！\n你共猜了",guess_time,"次。\n------------------------------")
        while True:
            usr_answer = input("是否继续游戏？（继续：Y/n，退出：N/n）\n")
            if usr_answer == "Y" or usr_answer == "y":
                sys_num = random.randint(100, 500)
                guess_time = 0
                break
            elif usr_answer == "N" or usr_answer == "n":
                break
            else:
                print("!!!输入无效，请重新输入!!!\n------------------------------")
