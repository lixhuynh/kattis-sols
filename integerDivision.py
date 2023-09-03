def main():
    d = int(input().split()[1])
    hash = {}
    for x in map(int, input().split()):
        hash[x//d] = hash.get(x//d, 0)
    ans = sum((x*(x-1))//2 for x in hash.values()) # nCr(x,2) for each val
    print(ans)

if __name__ == "__main__": main()