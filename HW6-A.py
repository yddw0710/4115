# 讀取一行輸入，依序為：原餐費 B、人數 N、服務費百分比 C、折價券金額 R
line = input().split()
B = int(line[0])
N = int(line[1])
C_percent = int(line[2])
R = int(line[3])

# 服務費為原餐費乘以服務費百分比，不足 1 元的部分捨去（使用整數除法）
service_fee = (B * C_percent) // 100

# 應付總額 = 原餐費 + 服務費 - 折價券金額；若小於 0，改為 0
total = B + service_fee - R
if total < 0:
    total = 0

# 計算每人基礎應付金額 q 與餘數 remainder
q = total // N
remainder = total % N

# a 人各付 q 元，b 人各付 q+1 元
a = N - remainder
b = remainder

# 輸出結果
print(total)
print(f"{q} {a}")
print(f"{q + 1} {b}")