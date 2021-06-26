def proteins(strand):
            codons = [strand[x:x+3] for x in range(0,9,3)
