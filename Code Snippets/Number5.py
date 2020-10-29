# k-mer generator program

def kmers_amount(dna, k):
    count = {}
    kmers = len(dna) - k + 1
    for items in range(kmers):
        kmer = dna[items: items + k]
        if kmer not in count:
            count[kmer] = 0
        count[kmer] += 1
    return count

print(kmers_amount('ACGTCG', 3))


