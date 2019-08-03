all_words = ''
bit_data = []


def translator(s):
    global all_words
    global bit_data
    raw_number = 0
    b = ''
    d = ''
    translate = {
        'a': '00',
        't': '01',
        'g': '10',
        'c': '11'
    }
    for x in range(15):
        for y in range(4):
            b += s[(x*4+y)]
        all_words += b + " "
        for c in b:
            d += translate.get(c,"00")
            raw_number = int(d, 2)
        bit_data.append(raw_number)
        b = ''
        d = ''


def main():
    lines = []
    output = "OUTPUT:\n"

    with open('fulldata.txt', 'rt') as data:
        for line in data:
            words = line.split()
            lines.append(words)

    for l in lines:
        output += l[0] + '\t\t'
        l.pop(0)
        ul = ''
        for w in l:
            output += w + ' '
            ul += w
        translator(ul)
        output += '\n'
    print(output)
    print(all_words)
    print(bit_data)
    decoded = open("output.txt", "w+")
    decoded.write(output)
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


"""""


