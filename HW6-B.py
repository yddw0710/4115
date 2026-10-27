import sys

# 讀取一行原始帳號（完整讀取，保留可能的尾端空白）
line = sys.stdin.readline()
s = line.rstrip('\r\n') if line else ''

# 1. 把英文字母轉成小寫
s = s.lower()

# 2. 移除頭尾的半形空白
s = s.strip(' ')

# 3. 將中間每一段連續半形空白改成一個底線
parts = s.split()
s = '_'.join(parts)

# 輸出第一行：整理後的帳號（若為空字串則輸出空白行）
print(s)

# 檢查是否合法
# 合法條件：
# 1. 長度為 6 至 16
# 2. 每個字元只能是 a 至 z、0 至 9 或底線 _
valid_chars = 'abcdefghijklmnopqrstuvwxyz0123456789_'
is_valid = True

if not (6 <= len(s) <= 16):
    is_valid = False
else:
    for ch in s:
        if ch not in valid_chars:
            is_valid = False
            break

# 輸出第二行：合法輸出 VALID，否則輸出 INVALID
if is_valid:
    print("VALID")
else:
    print("INVALID")