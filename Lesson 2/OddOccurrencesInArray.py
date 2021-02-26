def solution(A):
    A.sort()
    sum1 = 0
    sum2 = 0
    for i in range(0,len(A),2):
        sum1 += A[i]
        if (i + 1) < len(A):
            sum2 += A[i+1]
    return abs(sum1-sum2)

def main():
    A = [7,5,8,5,5,7,5]
    print("A: ", A)
    print("odd occurency ", solution(A))

if __name__ == "__main__":
    main()
