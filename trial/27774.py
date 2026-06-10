def f(x, y, s):
    if x + y >= 207: return s % 2 == 0
    if s == 0: return False
    h = [
        f(x + 1, y,  s - 1),
        f(x, y + 1, s - 1),
        f(x * 2, y, s - 1),
        f(x, y * 2, s - 1)
    ]
    return any(h) if (s - 1) % 2 == 0 else all(h)

print('19)', [s for s in range(2, 189) if f(s, 17, 2)])
print('19)', [s for s in range(2, 189) if f(s, 17, 3) and not f(s, 17, 1)])
print('19)', [s for s in range(2, 189) if f(s, 17, 4) and not f(s, 17, 2)])
