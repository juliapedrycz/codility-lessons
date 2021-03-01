
def solution(X, A):
    x = ((X+1) * X)//2
    B = [0]*X
    sum = 0
    j=0
    for i in A:
        if B[i-1] == 0:
            B[i-1] = i
            sum += i
        if sum == x:
            return j
        j+=1
    return -1


def main():
    A = [1,3,1,4,2,3,5,4]
    X = 5
    print("A: ", A," \tX: ",X,"\tearliest time when the frog can jump to the other side of the river:", solution(X,A))

if __name__ == "__main__":
    main()
