def solution(A):
    A.sort()
    min = 1
    for a in A:
        if a>0 :
            if a==min:
                min += 1
    return min

def main():
    A = [1, 3, 6, 4, 1, 2]
    print("A: ", A," \tsmallest positive missing integer: ", solution(A))

if __name__ == "__main__":
    main()
