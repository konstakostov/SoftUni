match_01 = input()
match_02 = input()
match_03 = input()

wins = 0
losses = 0
draws = 0

m01_t1 = int(match_01[0])
m01_t2 = int(match_01[2])

m02_t1 = int(match_02[0])
m02_t2 = int(match_02[2])

m03_t1 = int(match_03[0])
m03_t2 = int(match_03[2])

if m01_t1 > m01_t2:
    wins += 1
elif m01_t1 == m01_t2:
    draws += 1
elif m01_t1 < m01_t2:
    losses += 1

if m02_t1 > m02_t2:
    wins += 1
elif m02_t1 == m02_t2:
    draws += 1
elif m02_t1 < m02_t2:
    losses += 1

if m03_t1 > m03_t2:
    wins += 1
elif m03_t1 == m03_t2:
    draws += 1
elif m03_t1 < m03_t2:
    losses += 1

print(f"Team won {wins} games.")
print(f"Team lost {losses} games.")
print(f" Drawn games: {draws}")
