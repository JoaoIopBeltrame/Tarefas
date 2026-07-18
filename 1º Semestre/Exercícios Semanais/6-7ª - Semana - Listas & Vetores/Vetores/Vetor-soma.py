A = [1, 0, 5, -2, -5, 7]
print(A)
soma = A[0] + A[1] + A[5]
print(f'{A[0]} + {A[1]} + {A[5]} = {soma}')
A[4] = 100
for i in A:
    print(i, end=' ')
