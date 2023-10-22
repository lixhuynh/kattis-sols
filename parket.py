def main():
    r, b = [int(x) for x in input().split()]
    blocks = r + b
    for w in range(2, blocks):
        if blocks % w == 0:
            l = blocks // w
            if r == 2*l + 2*w - 4:
                print(l, w)
                return

if __name__=="__main__": main()