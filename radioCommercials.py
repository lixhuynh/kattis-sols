def main():
    n, p = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    i = 0
    while c[i] < p: # Find the first profitable time
        i += 1
        if i == n: print(0); return
    j = i+1; maxsum = cursum = c[i]-p
    while j < n: # Sliding window
        while cursum < 0:
            cursum -= c[i]-p
            i += 1
        cursum += c[j]-p
        maxsum = max(maxsum, cursum)
        j += 1
    print(max(maxsum, cursum))
            
if __name__ == "__main__": main()