import sys

def main():
    # 讀取第一行並轉為整數 K
    line1 = sys.stdin.readline()
    if not line1:
        return
    K = int(line1.strip())
    
    # 讀取第二行原始訊息 S，精確去除結尾換行符號，同時完整保留頭尾及連續空白
    S = sys.stdin.readline()
    if S.endswith('\n'):
        S = S[:-1]
    if S.endswith('\r'):
        S = S[:-1]
        
    result = []
    for ch in S:
        code = ord(ch)
        if 65 <= code <= 90:  # 大寫字母 'A' ~ 'Z' (ASCII 65-90)
            new_code = (code - 65 + K) % 26 + 65
            result.append(chr(new_code))
        elif 97 <= code <= 122:  # 小寫字母 'a' ~ 'z' (ASCII 97-122)
            new_code = (code - 97 + K) % 26 + 97
            result.append(chr(new_code))
        else:  # 數字、空白與標點符號保持原樣
            result.append(ch)
            
    # 輸出加密後的完整訊息並加上換行
    print("".join(result))

if __name__ == '__main__':
    main()