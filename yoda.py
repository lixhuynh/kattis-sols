def main():
    n = input()
    m = input()
    i = len(n)-1; j = len(m)-1
    while i >= 0 and j >= 0:
        if int(n[i]) > int(m[j]): m = m[:j] + m[j+1:]
        elif int(n[i]) < int(m[j]): n = n[:i] + n[i+1:]
        i -= 1; j -= 1
    print(int(n) if n != "" else "YODA")
    print(int(m) if m != "" else "YODA")    
            
if __name__ == "__main__": main()