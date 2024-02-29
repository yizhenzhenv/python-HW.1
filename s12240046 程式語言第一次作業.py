# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import cmath  # 使用複數數學庫，以處理虛數解

def quadratic_solver(a, b, c):
    # 計算判別式
    discriminant = cmath.sqrt(b**2 - 4*a*c)

    # 計算兩個解
    root1 = (-b + discriminant) / (2*a)
    root2 = (-b - discriminant) / (2*a)

    return root1, root2

# 使用者輸入係數
a = float(input("輸入 a: "))
b = float(input("輸入 b: "))
c = float(input("輸入 c: "))

# 解一元二次方程式
roots = quadratic_solver(a, b, c)

# 顯示解
print("解為:", roots)
