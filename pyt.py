start = input()
end = input()
start = start.split()
end = end.split()
start = [int(i) for i in start]
end = [int(i) for i in end]

A = start[0]-end[0]
def A_to_B_and_V(A):
    start[0] -= A
    start[1] += A
    start[2] += A

def B_to_V_and_G(B):
    start[1] -= B
    start[2] += B
    start[3] += B
def V_to_G(V):
    start[2] -= V
    start[3] += V

if A > 0:
    A_to_B_and_V(A)
    B = start[1]-end[1]
    if B > 0:
        B_to_V_and_G(B)
        V = start[2]-end[2]
        if V > 0:
            V_to_G(V)
            if start[3] >= end[3]:
                print('YES')
            else: print('NO')
else:print('NO')