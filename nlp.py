
import math

# Step 1: Define POS tags (hidden states)
tags = ["DET", "NOUN", "VERB"]

# Step 2: Initial probabilities
start_prob = {
    "DET": 0.6,
    "NOUN": 0.3,
    "VERB": 0.1
}

# Step 3: Transition probabilities
trans_prob = {
    "DET":  {"DET": 0.1, "NOUN": 0.8, "VERB": 0.1},
    "NOUN": {"DET": 0.1, "NOUN": 0.2, "VERB": 0.7},
    "VERB": {"DET": 0.2, "NOUN": 0.3, "VERB": 0.5}
}

# Step 4: Emission probabilities
emit_prob = {
    "the":   {"DET": 0.9, "NOUN": 0.01, "VERB": 0.01},
    "dog":   {"DET": 0.01, "NOUN": 0.8, "VERB": 0.01},
    "barks": {"DET": 0.01, "NOUN": 0.02, "VERB": 0.8}
}

# Step 5: Input sentence
sentence = "the dog barks".lower().split()

# Step 6: Initialize Viterbi table
viterbi = [{}]
backpointer = [{}]

for tag in tags:
    viterbi[0][tag] = (
        math.log(start_prob[tag])
        + math.log(emit_prob[sentence[0]][tag])
    )
    backpointer[0][tag] = None

# Step 7: Calculate probabilities for remaining words
for t in range(1, len(sentence)):
    viterbi.append({})
    backpointer.append({})

    word = sentence[t]

    for current_tag in tags:
        candidates = [
            (
                viterbi[t - 1][previous_tag]
                + math.log(trans_prob[previous_tag][current_tag])
                + math.log(emit_prob[word][current_tag]),
                previous_tag
            )
            for previous_tag in tags
        ]

        best_score, best_previous = max(candidates)

        viterbi[t][current_tag] = best_score
        backpointer[t][current_tag] = best_previous

# Step 8: Find the best final tag
last_tag = max(viterbi[-1], key=viterbi[-1].get)

# Step 9: Trace back the best tag sequence
best_tags = [last_tag]

for t in range(len(sentence) - 1, 0, -1):
    best_tags.insert(0, backpointer[t][best_tags[0]])

# Step 10: Display the result
print("Input Sentence:", " ".join(sentence))
print("POS Tags:")

for word, tag in zip(sentence, best_tags):
    print(word, "->", tag)
