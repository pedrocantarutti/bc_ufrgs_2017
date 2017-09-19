
# 2A)
with open('sequence.fasta', 'r') as f:
    seq = f.read().strip()
    chunks, chunk_size = len(seq), 9
    a = [seq[i:i + int(chunk_size)] for i in range(0, chunks, int(chunk_size))]
    print('CHUNK', a)
    # for line in lines:
    #     if 'ACCTGGTGTTCCCA' in line:
    #         print('LINHA:', line)



# 1A)
# with open('sequence.fasta', 'r') as f:
#     lines = f.readlines()
#     for line in lines:
#         if 'ACCTGGTGTTCCCA' in line:
#             print('LINHA:', line)
