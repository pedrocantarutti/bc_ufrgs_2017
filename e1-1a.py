# 1 a)
def p_1a():
    with open('sequence.fasta', 'r') as f:
        seq = f.read().strip()
        seq = seq.replace('\n', '')
        seq = seq.replace('N', '')

        print(seq.find('ACCTGGTGTTCCCA'))



if __name__=='__main__':
    p_1a()