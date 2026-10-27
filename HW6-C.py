# 讀取每日目標 G 與七天的步數列表
G = int(input())
steps = list(map(int, input().split()))

# 1. 計算總步數
total_steps = sum(steps)
print(total_steps)

# 2. 計算達標天數
achieved_count = 0
achieved_flags = []  # 記錄每一天是否達標的列表

for s in steps:
    if s >= G:
        achieved_count += 1
        achieved_flags.append(True)
    else:
        achieved_flags.append(False)

print(achieved_count)

# 3. 找出最高步數出現的所有日期（由小到大排列）[cite: 3]
max_val = max(steps)
max_days = []
for i in range(7):
    if steps[i] == max_val:
        max_days.append(str(i + 1))  # 日期從第 1 天到第 7 天

print(" ".join(max_days))

# 4. 計算最長連續達標天數（不跨週循環）[cite: 3]
max_consecutive = 0
current_consecutive = 0

for flag in achieved_flags:
    if flag:
        current_consecutive += 1
        if current_consecutive > max_consecutive:
            max_consecutive = current_consecutive
    else:
        current_consecutive = 0

print(max_consecutive)