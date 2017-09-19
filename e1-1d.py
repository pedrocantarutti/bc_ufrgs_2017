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

        total = sum(perc.values())

        print("{0:.2f}".format((perc['A'] * 100) / total),
              "{0:.2f}".format((perc['T'] * 100) / total),
              "{0:.2f}".format((perc['C'] * 100) / total),
              "{0:.2f}".format((perc['G'] * 100) / total))


if __name__=='__main__':
    p_1d()