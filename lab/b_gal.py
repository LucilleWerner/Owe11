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

# amino acid of interest (G)
print(codon_table[codons[794]])

region = ''

region += codons[79]+' '
region += codons[794]+' '
region += codons[795]+' '
region += codons[796]

print(region)

"""
Gly795
Asperagine for palindrome with pos - 1
Tyrosine for palindrome with  pos + 1
(both polar like Glycine)

"""