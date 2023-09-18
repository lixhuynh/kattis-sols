from collections import defaultdict

def findMostFreq(line): # find k = most freq bag dimension
    k = 0; hist = defaultdict(list)
    for x in line:
        hist[x].append(x)
        k = max(k, len(hist[x]))
    return k

def placeBags(line, k): # fit bags based on loop placement
    groups = [[] for _ in range(k)]; i = 0
    for val in line:
        groups[i].append(str(val))
        i = (i+1)%k
    return groups

def main():
    lines = []
    while True: # read the input
        n = int(input())
        if n == 0: break
        else: lines.append([int(x) for x in input().split()])
    for line in lines:
        line.sort()
        k = findMostFreq(line)
        groups = placeBags(line, k)
        print(k)
        for group in groups: print(' '.join(group))
        if line != lines[-1]: print()

if __name__ == "__main__": main()