H = int(input())
M = int(input())
S = int(input())
T = int(input())

if T < 60:
    S += T
    if S == 60:
        S = 0
        M += 1
        if M == 60:
            M = 0
            H += 1
elif T >= 60 and T <= 3600:
    if T == 60:
        M += 1
    else:
        Tm = T // 60
        Ts = T % 60
        M += Tm
        S += Ts
elif T >= 3600:
    if T == 3600:
        H += 1
    else:
        H += T // 3600
        M += T // 3600 + (H - 24)
        if H > 23:
            H -= 24
        S += T % 60

print(H)
print(M)
print(S)