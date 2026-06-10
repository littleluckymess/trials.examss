from itertools import product

for pos, val in enumerate(product(sorted('СТРОКА'), repeat=5), start=1):
    val = ''.join(val)
    if val[0] not in 'АСТ' and val.count('О') == 2:
        if pos % 2 == 0:
            print(pos)


