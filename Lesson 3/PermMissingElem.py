def solution(A):
    sumA = 0
    x = 0
    for i in range(0,len(A)):
        sumA += A[i]
        x += i+1
    return len(A) + 1 - (sumA-x)


def main():
    A = [3,4,5,1]
    print("A: ", A," \tmissing element: ", solution(A))

if __name__ == "__main__":
    main()
