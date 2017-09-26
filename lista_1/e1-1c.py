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


if __name__=='__main__':
    p_1c()