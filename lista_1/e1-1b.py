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
    p_1b()