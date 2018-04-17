import simplejson as json


"""
http://www.uniprot.org/uniprot/P00722
https://www.ebi.ac.uk/ena/data/view/AAB18068

"""

codon_json = open('/home/sevvy/PycharmProjects/owe11/lab/codon_table.json', 'r')

aacharc_json = open('/home/sevvy/PycharmProjects/owe11/lab/aa_characs.json', 'r')

bgal_fasta = open('/home/sevvy/PycharmProjects/owe11/lab/ecoli_bgal.fasta', 'r')

# read the sequence, split from header
bgal_split = bgal_fasta.read().split('\n')[1:]
seq = ''.join(bgal_split)

# make triplets (codons)
codons = [seq[x:x+3] for x in range(0,len(seq),3)]

# read codon table as dict
codon_table = json.load(codon_json)

# regions of interest -1 and + 1
region_dna = ''
region_aa = ''
for i in range(792,806):
    region_dna += codons[i]+' '
    region_aa += codon_table[codons[i]] +' '

print(region_dna)
print(region_aa)

comp = {'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'}

aa_charc = json.load(aacharc_json, 'r')

alts = []

# loop over the region of interest
# find possible palindromes looking at the
# previous codon and the next codon
for i in range(794,804):
    cur = codons[i]
    cur_aa = codon_table[cur]

    prev = codons[i-1]
    prev_com = [comp[c] for c in prev]
    prev_rev = ''.join(prev_com)[::-1]
    prev_aa = codon_table[prev_rev]

    nex = codons[i + 1]
    nex_com = [comp[c] for c in nex]
    nex_rev = ''.join(nex_com)[::-1]
    nex_aa = codon_table[nex_rev]

    cur_charc = aa_charc[cur_aa]
    prev_charc = aa_charc[prev_aa]
    nex_charc = aa_charc[nex_aa]

    # if old amino acid and new amino acid have
    # different characteristics, add to the list
    if cur_charc != prev_charc:
        alts.append([cur_aa+str(i), prev_aa])
    if cur_charc != nex_charc:
        alts.append([cur_aa+str(i), nex_aa])

print(alts)

