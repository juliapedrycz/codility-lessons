def solution(A):
    sumA = 0
    s1 = 0
    s2 = 0
    for i in A:
        sumA += i
    for P in range(1,len(A)):
        s1 += A[P-1]
        s2 = sumA - s1
        if P == 1:
            min = abs(s1-s2)
        elif abs(s1-s2) < min:
            min = abs(s1-s2)
    return min

def main():
    A = [3,1,2,4,3]
    print("A: ", A," \tminimal difference: ", solution(A))

if __name__ == "__main__":
    main()
