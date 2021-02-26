def solution(A, K):
    if len(A) > 1:
        B = []
        if K < len(A):
            for i in range(0,len(A)):
                B.append(A[i-K])
        else:
            K = K%len(A)
            for i in range(0,len(A)):
                B.append(A[i-K])
        return B
    else:
        return A

def main():
    A = [1,2,3,4,5]
    K = [1,2,3,4,5,6,7,8,9,10,11]
    for i in K:
        print("A: ", A ,"\tK: ", i, "\trotated A: ", solution(A, i))

if __name__ == "__main__":
    main()
