
import nltk
from nltk.corpus import treebank
from nltk.tag import hmm

# Step 1: Download dataset
nltk.download('treebank', quiet=True)

# Step 2: Load training data
train_data = treebank.tagged_sents()[:300]

# Step 3: Create and train HMM
trainer = hmm.HiddenMarkovModelTrainer()
model = trainer.train_supervised(train_data)

# Step 4: Input sentence
sentence = "The company said it expects a profit .".split()

# Step 5: Apply HMM POS tagging
result = model.tag(sentence)

# Step 6: Display output
print("Input Sentence:", " ".join(sentence))
print("POS Tags:", result)
