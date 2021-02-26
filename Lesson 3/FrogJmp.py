def solution(X, Y, D):
    if (Y-X) % D == 0:
        return (Y-X)//D
    else:
        return ((Y-X)//D) + 1


def main():
    X = 10
    Y = 85
    Z = 30
    print("X = ", X, "\tY = ", Y,"\tZ = ", Z,"\tminimal number of jumps  = ", solution(X,Y,Z))

if __name__ == "__main__":
    main()
