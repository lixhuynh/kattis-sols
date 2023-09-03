def main():
    n, m = map(int, input().split())
    braces = pow(2, n+1, m) # 2^{n+1} % m
    if n <= 1: commas = 0 # no commas for 0, 1
    else: commas = pow(2, n-1, m)-1 # 2^{n-1} % m
    print((braces+commas)%m)

if __name__ == "__main__": main()