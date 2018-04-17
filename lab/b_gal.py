import simplejson as json


"""
http://www.uniprot.org/uniprot/P00722
https://www.ebi.ac.uk/ena/data/view/AAB18068

"""

codon_json = open('/home/sevvy/PycharmProjects/owe11/lab/codon_table.json', 'r')

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
for i in range(793,805):
    region_dna += codons[i]+' '
    region_aa += codon_table[codons[i]] +' '

print(region_dna)
print(region_aa)

"""
Gly795
Asperagine for palindrome with pos - 1
Tyrosine for palindrome with  pos + 1
(both polar like Glycine)

"""