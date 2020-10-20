def solution(X, A):
    if X < 1 or len(A) < 1:
        return -1
    try:
        found = max([ A.index(element) for element in range(1, X + 1) ])
    except ValueError:
        return -1
    return  found
