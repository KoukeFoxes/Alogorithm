"""
    前6個質數分別是2, 3, 5, 7, 11, 16, 請問排在所有質數中的第1001個質數是？
    
    需求說明：
    1. 使用Python 3設計程式解題
    2. 程式請放至Google Colab，檔名設為prime_xxxxxxxx.ipynb (其中xxxxxxxx請用自己的學號)，再將分享連結上傳至本作業。
    
"""

import sys

def main() -> None:
    
    def isPrime(n: int) -> bool:
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5)+1, 2):
            if n % i == 0:
                return False
        return True

    goal = int(input())
    index = 1
    for i in range(3, sys.maxsize):
        index += 1 if isPrime(i) else 0
        if index == goal:
            print(i)
            break

if __name__ == "__main__":
    main()        