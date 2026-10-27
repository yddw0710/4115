# 讀取商品種類數 N
N = int(input())

# 使用平行串列分別儲存商品名稱與小計
names = []
subtotals = []

for _ in range(N):
    line = input().split()
    name = line[0]
    price = int(line[1])
    qty = int(line[2])
    
    # 計算優惠：每買滿 3 件其中 1 件免費（輸入數量包含免費件數），未滿 3 件不優惠
    free_count = qty // 3
    paid_count = qty - free_count
    subtotal = paid_count * price
    
    names.append(name)
    subtotals.append(subtotal)

# 1. 輸出每種商品的優惠後小計（順序與輸入相同）[cite: 5]
for i in range(N):
    print(f"{names[i]} {subtotals[i]}")

# 2. 計算總小計[cite: 5]
total_sum = sum(subtotals)

# 3. 合計滿 1000 元折 100 元，整張帳單限折一次[cite: 5]
if total_sum >= 1000:
    final_total = total_sum - 100
else:
    final_total = total_sum

print(f"TOTAL {final_total}")

# 4. 找出花費最多的商品（若同額則取輸入較早者）[cite: 5]
max_idx = 0
for i in range(1, N):
    if subtotals[i] > subtotals[max_idx]:
        max_idx = i

print(f"TOP {names[max_idx]}")
