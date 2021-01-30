N = int(input())

AC = 0
WA = 0
TLE = 0
RE = 0

for i in range(N):
    C = input()
    if C == 'AC':
        AC += 1
    elif C == 'WA':
        WA += 1
    elif C == 'TLE':
        TLE += 1
    else:
        RE += 1

print('AC × ' + str(AC))
print('WA × ' + str(WA))
print('TLE × ' + str(TLE))
print('RE × ' + str(RE))
