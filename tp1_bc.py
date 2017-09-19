
# 2A)
# Resposta: 1127
with open('sequence.fasta', 'r') as f:
    seq = f.read().strip()

    chunks, chunk_size = len(seq), 9
    a = [seq[i:i + int(chunk_size)] for i in range(0, chunks, int(chunk_size))]

    pal = []
    for s in a:
        if s == s[::-1]:
            if '\n' in s:
                s = s.replace('\n', '')
            if s not in pal:
                pal.append(s)

    print(len(pal))


# 1A)
# with open('sequence.fasta', 'r') as f:
#     lines = f.readlines()
#     for line in lines:
#         if 'ACCTGGTGTTCCCA' in line:
#             print('LINHA:', line)
