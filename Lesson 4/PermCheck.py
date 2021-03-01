def solution(A):
    A.sort()
    for i in range(0,len(A)):
        if A[i] != i+1:
            return 0
    return 1

def main():
    A = [1,2,3,4]
    print("A: ",A," \tis permutation: ", solution(A))
    A = [4,1,3]
    print("A: ",A," \tis permutation: ", solution(A))

if __name__ == "__main__":
    main()
