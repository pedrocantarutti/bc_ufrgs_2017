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


if __name__=='__main__':
    p_1d()