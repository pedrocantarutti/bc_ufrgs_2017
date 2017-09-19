
# 1 d)
# Resposta: %, sim
def p_1d():
    with open('sequence.fasta', 'r') as f:
        seq = f.read().strip()

        if '\n' in seq:
            seq = seq.replace('\n', '')


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
    p_1c()
