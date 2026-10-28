
import nltk
from nltk.corpus import treebank
from nltk.tag import hmm

# Step 1: Download the dataset
nltk.download('treebank', quiet=True)

# Step 2: Load training data
train_data = treebank.tagged_sents()[:500]

# Step 3: Create HMM trainer
trainer = hmm.HiddenMarkovModelTrainer()

# Step 4: Train the HMM model
model = trainer.train_supervised(train_data)

# Step 5: Get input sentence
sentence = "The company said it expects a profit .".split()

print("Input Sentence:", " ".join(sentence))

# Step 6: Perform POS tagging using HMM
tagged_words = model.tag(sentence)

# Step 7: Display POS tags
print("\nWord\t\tPOS Tag")
print("-------------------------")

for word, tag in tagged_words:
    print(f"{word}\t\t{tag}")

# Step 8: Display the total number of words
print("\nTotal words:", len(tagged_words))
