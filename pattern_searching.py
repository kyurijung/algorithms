def naiveAlgorithm(txt,pat):
    # src: https://www.geeksforgeeks.org/naive-algorithm-for-pattern-searching/
    # O(n*m) and O(1)
    for i in range(len(txt)-len(pat)+1):
        j = 0
        while j < len(pat):
            if txt[i+j] != pat[j]:
                break
            j += 1
        if j == len(pat):
            print(i)

def main():
    txt = "AABAACAADAABAAABAA"
    pat = "AABA"

    naiveAlgorithm(txt,pat)

if __name__ == "__main__":
    main()
