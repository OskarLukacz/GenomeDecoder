output = "OUTPUT:\n"
raw_genome = ''
all_words = ''
bit_data = []
all_protein = ''

table = {
        'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
        'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
        'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
        'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
        'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
        'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
        'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
        'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
        'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
        'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
        'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_',
        'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W'
    }

def bit_translator(s):
    global all_words
    global bit_data

    translate = {
        'a': '00',
        't': '01',
        'g': '10',
        'c': '11'
    }

    while True:
        try:
            raw_bits = ''
            word = s[0] + s[1] + s[2] + s[3]
            all_words += word + " "
            for c in word:
                raw_bits += translate.get(c, "00")
            bit_data.append(int(raw_bits, 2))
            s = s[4:]
        except IndexError:
            return


def polychain_finder(s):

    while True:
        try:
            codon = s[0] + s[1] + s[2]
            print('tried:', codon)
            if codon == 'ATG':
                print('success')
                s = protein_translator(s)
            else:
                s = s[1:]
        except IndexError:
            return


def protein_translator(s):
    global all_protein

    while True:
        try:
            protein = ''
            codon = s[0] + s[1] + s[2]
            protein += table[codon]
            s = s[3:]
            if protein == '_':
                all_protein += '\n\n'
                print('break')
                break
            else:
                all_protein += protein
                print('protein:', protein)
        except IndexError:
            return
    return s


def main():
    global raw_genome
    lines = []

    with open('fulldata.txt', 'rt') as data:
        for line in data:
            words = line.split()
            lines.append(words)

    for l in lines:
        l.pop(0)
        ul = ''
        for w in l:
            ul += w
        raw_genome += ul

    bit_translator(raw_genome)
    #protein_translator(raw_genome.upper())
    polychain_finder(raw_genome.upper())

    """
    for l in lines:
        output += l[0] + '\t\t'
        l.pop(0)
        ul = ''
        for w in l:
            output += w + ' '
            ul += w
        translator(ul)
        output += '\n'
    """
    print("Raw genome:", raw_genome)
    print("Number of words: ", len(all_words.split()))
    print(all_words)
    print("Number of bits: ", len(bit_data))
    print(bit_data)
    print(all_protein)
    print(output)

    decoded = open("output.txt", "w+")
    decoded.write(output)
    decoded.write(all_protein)
    decoded.close()


main()


"""""

TRANSLATION CODE

The default set of expressions describes the standard genetic code. Slashes mark the boundary of the pattern to match,
while the equal sign and letter specify the amino acid described by the pattern. Within the pattern square brackets 
surround possible bases present at a single position. The vertical bar separates two distinct patterns that represent 
the same amino acid. Each expression is followed by a comma, except for the last expression. 

https://www.bioinformatics.org/sms/show_trans.html

/gc[agtcn]/=A,
/tg[ct]/=C,
/ga[tc]/=D,
/ga[ag]/=E,
/tt[tc]/=F,
/gg[agctn]/=G,
/ca[tc]/=H,
/at[atc]/=I,
/aa[ag]/=K,
/ct[agtcn]|tt[ag]/=L,
/atg/=M,
/aa[tc]/=N,
/cc[atgcn]/=P,
/ca[ag]/=Q,
/cg[agctn]|ag[ag]/=R,
/tc[agctn]|ag[ct]/=S,
/ac[agctn]/=T,
/gt[agctn]/=V,
/tgg/=W,
/ta[tc]/=Y,
/ta[ga]|tga/=*


    def take_four(s):
    while True:
        try:
            a = s[0]
            b = s[1]
            s = s[2:]
        except IndexError:
            return
        yield a, b


    for a, b in take_four(s):
        print(a, b, "check")
        all_words += a + b


   
    for x in range(2):
        for y in range(4):
            b += s[(x*4+y)]
        all_words += b + " "
        for c in b:
            d += translate.get(c, "00")
            raw_number = int(d, 2)
        bit_data.append(raw_number)
        b = ''
        d = ''
"""""


