inp_sentences = []

with open ('input.txt') as inp:
    n_words = int(inp.readline().strip())
    for i in range(n_words):
        inp_sentences.append(inp.readline().strip())

set_words = set()
dict_edges = {}

for sentence in inp_sentences:
    for i in range(len(sentence) - 2):
        set_words.add(sentence[i : i+3])

for sentence in inp_sentences:
    for i in range(len(sentence) - 3):
        word1 = sentence[i : i+3]
        word2 = sentence[i+1 : i+4]
        dict_edges[(word1, word2)] = dict_edges.get((word1, word2), 0) + 1

print (len(set_words))
print (len(dict_edges))

for (word1, word2), num in dict_edges.items():
    print (word1, word2, num)
