def main():
    tc = int(input())
    r = []
    for _ in range(tc):
        n, m = map(int, input().split())
        pairs = [map(int, input().split()) for _ in range(m)]
        r.append(n-1)
    for v in r: print(v)

if __name__=="__main__": main()