def main():
    n = int(input())
    bytes = [input() for _ in range(n)]
    i = 0
    counts = [0, 0, 0, 0]
    while i < n:
        if bytes[i][0] == "0": # Type 1
            counts[0] += 1
        elif bytes[i][:3] == "110" \
            and i < n-1 and bytes[i+1][:2] == "10": # Type 2
            counts[1] += 1
            i += 1
        elif bytes[i][:4] == "1110" \
            and i < n-2 and bytes[i+1][:2] == "10" and bytes[i+2][:2] == "10": # Type 3
            counts[2] += 1
            i += 2
        elif bytes[i][:5] == "11110" \
            and i < n-3 and bytes[i+1][:2] == "10" and bytes[i+2][:2] == "10" and bytes[i+3][:2] == "10": # Type 4
                counts[3] += 1
                i += 3
        else:
            print('invalid')
            return
        i += 1
    for c in counts:
        print(c)
            
if __name__ == "__main__": main()