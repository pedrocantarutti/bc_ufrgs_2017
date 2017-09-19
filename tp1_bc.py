
# 1 d)
# Resposta: %, sim
def p_1d():
    with open('sequence.fasta', 'r') as f:
        seq = f.read().strip()

        if '\n' in seq:
            seq = seq.replace('\n', '')


# 1 c)
def p_1c():
    with open('sequence.fasta', 'r') as f:
        seq = f.read().strip()

        if '\n' in seq:
            seq = seq.replace('\n', '')


# 1 b)
# Resposta: 986
def p_1b():
    with open('sequence.fasta', 'r') as f:
        seq = f.read().strip()

        if '\n' in seq:
            seq = seq.replace('\n', '')

        chunks, chunk_size = len(seq), 9
        a = [seq[i:i + int(chunk_size)] for i in range(0, chunks, int(chunk_size))]

        pal = []
        for s in a:
            if s == s[::-1]:
                if s not in pal and 'N' not in s:
                    pal.append(s)

        print(len(pal))


# 1 a)
def p_1a():
    with open('sequence.fasta', 'r') as f:
        lines = f.readlines()

        for line in lines:
            if '\n' in line:
                line = line.replace('\n', '')
            if 'ACCTGGTGTTCCCA' in line:
                print('LINHA:', line)



if __name__=='__main__':
    p_1b()
