def main():
    n,k = [int(x) for x in input().split()]
    seq = [0,1]
    for _ in range(2,n-1): seq.append(seq[-1]+seq[-2]) # Fibonacci sequence up to (n-2)th number
    while n > 2:
        if k > seq[n-2]:
            k -= seq[n-2]
            n -= 1
        else: n -= 2
    if n == 1: print("N")
    else: print("A")

if __name__ == "__main__": main()