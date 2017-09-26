# The core of this implementation was based on: https://github.com/alevchuk/pairwise-alignment-in-python.git
# I've ported to Python3 and made some improvments to the base algorithmn


# Globals
MATCH_AWARD      = 5
MISMATCH_PENALTY = -3
GAP_PENALTY      = -4


# zeros() was origianlly from NumPy.
# This version is implemented by alevchuk 2011-04-10
def zeros(shape):
    retval = []
    for x in range(shape[0]):
        retval.append([])
        [retval[-1].append(0) for y in range(shape[1])]
    return retval

def match_score(alpha, beta):
    if alpha == beta:
        return MATCH_AWARD
    elif alpha == '-' or beta == '-':
        return GAP_PENALTY
    else:
        return MISMATCH_PENALTY

def finalize(align1, align2):
    align1 = align1[::-1]    #reverse sequence 1
    align2 = align2[::-1]    #reverse sequence 2
    
    i,j = 0,0
    
    #calcuate identity, score and aligned sequeces
    symbol = ''
    score = 0
    identity = 0
    for i in range(len(align1)):
        # if two AAs are the same, then output the letter
        if align1[i] == align2[i]:                
            symbol = symbol + align1[i]
            identity = identity + 1
            score += match_score(align1[i], align2[i])
    
        # if they are not identical and none of them is gap
        elif align1[i] != align2[i] and align1[i] != '-' and align2[i] != '-': 
            score += match_score(align1[i], align2[i])
            symbol += ' '

        #if one of them is a gap, output a space
        elif align1[i] == '-' or align2[i] == '-':          
            symbol += ' '
            score += GAP_PENALTY
    
    identity = float(identity) / len(align1) * 100
    
    print('Identidade =', "%3.3f" % identity, 'percent')
    print('Score =', score)
    print(align1)
    print(symbol)
    print(align2)


def needle(seq1, seq2):
    m, n = len(seq1), len(seq2)  # length of two sequences
    
    # Generate DP table and traceback path pointer matrix
    score = zeros((m+1, n+1))      # the DP table
   
    # Calculate DP table
    for i in range(m + 1):
        score[i][0] = GAP_PENALTY * i

    for j in range(n + 1):
        score[0][j] = GAP_PENALTY * j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            match = score[i - 1][j - 1] + match_score(seq1[i-1], seq2[j-1])
            delete = score[i - 1][j] + GAP_PENALTY
            insert = score[i][j - 1] + GAP_PENALTY
            score[i][j] = max(match, delete, insert)

    # Traceback and compute the alignment
    align1, align2 = '', ''
    i,j = m,n # start from the bottom right cell
    while i > 0 and j > 0: # end toching the top or the left edge
        score_current = score[i][j]
        score_diagonal = score[i-1][j-1]
        score_up = score[i][j-1]
        score_left = score[i-1][j]

        if score_current == score_diagonal + match_score(seq1[i-1], seq2[j-1]):
            align1 += seq1[i-1]
            align2 += seq2[j-1]
            i -= 1
            j -= 1
        elif score_current == score_left + GAP_PENALTY:
            align1 += seq1[i-1]
            align2 += '-'
            i -= 1
        elif score_current == score_up + GAP_PENALTY:
            align1 += '-'
            align2 += seq2[j-1]
            j -= 1

    # Finish tracing up to the top left cell
    while i > 0:
        align1 += seq1[i-1]
        align2 += '-'
        i -= 1
    while j > 0:
        align1 += '-'
        align2 += seq2[j-1]
        j -= 1

    finalize(align1, align2)
