import sys

def main():
    # 1. 讀取菜單筆數 M
    line1 = sys.stdin.readline()
    if not line1.strip():
        return
    M = int(line1.strip())

    drinks = []
    prices = []
    total_cups = []

    # 讀取 M 行菜單[cite: 6]
    for _ in range(M):
        parts = sys.stdin.readline().split()
        if not parts:
            continue
        drinks.append(parts[0])
        prices.append(int(parts[1]))
        total_cups.append(0)  # 初始化總杯數為 0

    # 2. 讀取訂單筆數 N
    line2 = sys.stdin.readline()
    if not line2.strip():
        return
    N = int(line2.strip())

    order_students = []
    order_drinks = []
    order_quantities = []
    student_names = []

    # 讀取 N 行訂單[cite: 6]
    for _ in range(N):
        parts = sys.stdin.readline().split()
        if not parts:
            continue
        student = parts[0]
        drink = parts[1]
        qty = int(parts[2])
        
        order_students.append(student)
        order_drinks.append(drink)
        order_quantities.append(qty)
        
        # 記錄學生首次出現的順序（不使用集合與字典）
        if student not in student_names:
            student_names.append(student)
            
        # 累計各飲料總杯數
        drink_idx = drinks.index(drink)
        total_cups[drink_idx] += qty

    # 計算每種飲料的最終單價（總杯數達 10 杯含以上，單價皆減 5 元）[cite: 6]
    final_prices = []
    for i in range(M):
        if total_cups[i] >= 10:
            final_prices.append(prices[i] - 5)
        else:
            final_prices.append(prices[i])

    # 3. 輸出 M 行：DRINK 飲料名稱 總杯數（依菜單順序）[cite: 6]
    for i in range(M):
        print(f"DRINK {drinks[i]} {total_cups[i]}")

    # 計算每位同學的應付金額
    student_totals = [0] * len(student_names)

    for i in range(N):
        s = order_students[i]
        d = order_drinks[i]
        qty = order_quantities[i]
        
        s_idx = student_names.index(s)
        d_idx = drinks.index(d)
        
        cost = qty * final_prices[d_idx]
        student_totals[s_idx] += cost

    # 4. 輸出每個不同學生：STUDENT 姓名 應付金額（依首次出現順序）[cite: 6]
    for i in range(len(student_names)):
        print(f"STUDENT {student_names[i]} {student_totals[i]}")

    # 5. 輸出 TOTAL 全班總額[cite: 6]
    total_sum = sum(student_totals)
    print(f"TOTAL {total_sum}")

if __name__ == '__main__':
    main()