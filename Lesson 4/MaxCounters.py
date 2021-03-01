def solution(N, A):
    B = [0]*N
    max = 0
    for i in range(0,len(A)):
        if not (A[i-1] == N+1 and A[i] == N+1):
            if A[i] < N+1:
                B[A[i]-1] += 1
                if B[A[i]-1] > max:
                    max = B[A[i]-1]
            if A[i] == N+1:
                B = [max] * N
    return B

def main():
    A = [3,4,4,6,1,4,4]
    N = 5
    print("A: ", A," \tN: ",N,"\tsequence of integers representing the values of the counters:", solution(N,A))

if __name__ == "__main__":
    main()
