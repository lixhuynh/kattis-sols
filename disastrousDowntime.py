from math import ceil

def main():
    n,k = [int(x) for x in input().split()]
    reqs = [int(input()) for _ in range(n)]
    mx = 1
    i = 0; j = 1
    while j < n:
        while j < n and reqs[j] - reqs[i] < 1000:
            j += 1
        mx = max(j-i, mx)
        i += 1
        if i == j: j += 1
    print(ceil(mx / k))

if __name__ == "__main__": main()