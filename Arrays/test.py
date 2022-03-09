def countMinMoves(A, B):
    if A == B:
        return 0
    if A-B==-1:
        return 1 + countMinMoves(A + 1, B)
    if A-B==1:
        return 1 + countMinMoves(A , B+1)
    if A | (B - A) < B:
        print(A,B)
        return 1 + countMinMoves(A | (B - A), B)



t = int(input())
for _ in range(t):
    A, B = map(int, input().split())
    print(countMinMoves(A, B))