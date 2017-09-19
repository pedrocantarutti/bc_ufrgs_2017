
# 1 d)
# Resposta: %, sim
def p_1d():
    perc = {
        'A': 0,
        'G': 0,
        'C': 0,
        'T': 0
    }

    with open('sequence.fasta', 'r') as f:
        seq = f.read().strip()

        seq = seq.replace('\n', '')
        seq = seq.replace('N', '')

        for c in seq:
            if c in perc:
                perc[str(c)] += 1

        print(perc)


# 1 c)
# Resposta: 1050079
def p_1c():
    with open('sequence.fasta', 'r') as f:
        seq = f.read().strip()

        seq = seq.replace('\n', '')

        chunks, chunk_size = len(seq), 37
        a = [seq[i:i + int(chunk_size)] for i in range(0, chunks, int(chunk_size))]

        lst = set()
        for s in a:
            if len(s) == 37 and 'N' not in s:
                lst.add(s)
        print(len(lst))



# 1 b)
# Resposta: 986
def p_1b():
    with open('sequence.fasta', 'r') as f:
        seq = f.read().strip()

        seq = seq.replace('\n', '')

        chunks, chunk_size = len(seq), 9
        a = [seq[i:i + int(chunk_size)] for i in range(0, chunks, int(chunk_size))]

        pal = set()
        for s in a:
            if s == s[::-1]:
                if 'N' not in s:
                    pal.add(s)

        print(len(pal))


if __name__=='__main__':
    # p_1b()
    # p_1c()
    p_1d()