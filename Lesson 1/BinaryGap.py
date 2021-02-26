def solution(N):
    A = []
    max = 0
    counter =0
    while N > 0:
        A.append(N%2)
        N = N//2
    for i in range(len(A)-2,-1,-1):
        if A[i] == 0:
            counter += 1
        elif A[i] == 1:
            if counter > max:
                max = counter
            counter = 0
    return max

def main():
    A = [5,32,9,1041,529]
    for i in A:
        print("Number: ",i," \tbinary gap: ", solution(i))

if __name__ == "__main__":
    main()
