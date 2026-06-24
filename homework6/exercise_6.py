sentence = "milk bread milk eggs milk"

split_sentence = sentence.split()

counts ={}

for word in split_sentence:
    counts[word]= counts.get(word, 0) + 1

for i, item in counts.items():
    print(f"{i}: {item}")

