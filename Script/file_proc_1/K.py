from math import exp
from math import pi, e, cos, sin

# def fft(x, inv=False):
#     n = size(x)
#     j = 0
#     for i in range(n):
#         if (i < j): x[i], x[j] = x[j], x[i]
#         m = n >> 1
#         while (1 <= m and m <= j):
#             j -= m
#             m >>= 1
#         j += m
#     mx = 1
#     while(mx < n):
#         wp = exp(complex(0, (-1 if inv else 1) *  pi / mx))
#         w = 1
#         for
#
#
#         mx <<= 1


def fft(array, n, inv=False):
    if n == 1:
        return
    theta = (pi * 2) / n
    if inv:
        Wn = pow(e, (-2 * pi * 1j) / n)
    else:
        Wn = pow(e, (2 * pi * 1j) / n)

    W = 1

    a = [0] * (n // 2)
    b = [0] * (n // 2)

    for i in range(n):
        if (i & 1):
            b[i // 2] = array[i]
        else:
            a[i // 2] = array[i]

    fft(a, n // 2, inv)
    fft(b, n // 2, inv)

    for i in range(n // 2):
        array[i] = a[i] + W * b[i]
        array[i + n // 2] = a[i] - W * b[i]
        W *= Wn

def encode(n):
    map_dir = {}
    map_dir['n'] = 0
    map_dir['w'] = 1
    map_dir['e'] = 2
    map_dir['s'] = 3
    te = [0 for _ in range(n)]

    for i in range(n):
        s = input()
        if s == '?':
            continue
        dir, step = s.split()
        te[i] = int(step) * 4 + map_dir[dir]
    return te


n, m = map(int, input().split())
a, b = encode(n), encode(m)
size = 2 * n + 1
while (size & (size - 1)): size += 1
bits = [i for i in range(5)]
match = [True for _ in range(n - m + 1)]

for bit in bits:
    A = [complex(0,0) for _ in range(size)]
    B = [complex(0,0) for _ in range(size)]
    F = [0 for _ in range(n - m + 1)]
    G = [0 for _ in range(n - m + 1)]

    for i in range(n): A[n-i-1] = complex(0 if (a[i] == 0) else 1 if (a[i] & (1 << bit)) else -1, 0)
    for i in range(m): B[i] = complex(0 if (b[i] == 0) else 1 if (b[i] & (1 << bit)) else -1, 0)

    fft(A, size)
    fft(B, size)
    for i in range(size): A[i] *= B[i]
    fft(A, size, inv=True)
    for i in range(n - m + 1): F[i] = int(round(A[n-i-1].real))
    #print(F)

    A = [complex(0, 0) for _ in range(size)]
    B = [complex(0, 0) for _ in range(size)]
    for i in range(n): A[n - i - 1] = complex(0 if (a[i] == 0) else 1, 0)
    for i in range(m): B[i] = complex(0 if (b[i] == 0) else 1, 0)
    fft(A, size)
    fft(B, size)
    for i in range(size): A[i] *= B[i]
    fft(A, size, inv=True)
    for i in range(n - m + 1): G[i] = int(round(A[n - i - 1].real))
    #print(G)

    for i in range(n - m + 1): match[i] = match[i] and (F[i] == G[i])

print(sum(match))