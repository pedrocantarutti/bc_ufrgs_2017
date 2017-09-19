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
    p_1a()