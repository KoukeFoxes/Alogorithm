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
    index = 0
    for i in range(3, sys.maxsize):
        index += 1 if isPrime(i) else 0
        if index == goal:
            print(i)
            break

if __name__ == "__main__":
    main()        