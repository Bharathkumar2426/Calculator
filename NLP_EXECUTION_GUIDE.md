# Execution Guide for NLP & HMM POS Tagging

This guide outlines the theoretical concepts, prerequisites, setup instructions, and step-by-step execution details for [`nlp.py`](file:///d:/DL/nlp.py) and [`nlpHMM.py`](file:///d:/DL/nlpHMM.py).

---

## 1. Project Overview

Both scripts perform **Part-of-Speech (POS) Tagging** using **Hidden Markov Models (HMM)** and the **Viterbi Algorithm**, comparing an explicit mathematical implementation with a corpus-trained supervised model:

| Script | Implementation Type | POS Tagset | Training Source | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| [`nlp.py`](file:///d:/DL/nlp.py) | **Manual From-Scratch Viterbi** | Simplified (`DET`, `NOUN`, `VERB`) | Hand-crafted probability matrices (Start, Transition, Emission) | Python Standard Library (`math`) |
| [`nlpHMM.py`](file:///d:/DL/nlpHMM.py) | **NLTK Supervised HMM** | Penn Treebank tagset (`DT`, `NN`, `VBD`, `PRP`, etc.) | NLTK Penn Treebank corpus (300 tagged sentences) | `nltk` |

---

## 2. Prerequisites & Environment Setup

### Step 2.1: Python Environment
Python 3.9+ is recommended. Check your active Python version:
```powershell
python --version
```

### Step 2.2: Activate the Virtual Environment
A virtual environment (`.venv`) is already configured in the workspace directory.

- **PowerShell**:
  ```powershell
  .\.venv\Scripts\Activate.ps1
  ```
  *(If execution is blocked by PowerShell policy, run: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` and then run the script).*

- **Command Prompt (CMD)**:
  ```cmd
  .\.venv\Scripts\activate.bat
  ```

- **Direct Path Execution (without activating)**:
  You can execute scripts directly with the virtual environment interpreter:
  ```powershell
  .\.venv\Scripts\python.exe <script_name>.py
  ```

### Step 2.3: Install Required Dependencies
- For [`nlp.py`](file:///d:/DL/nlp.py): No third-party packages required (uses built-in `math`).
- For [`nlpHMM.py`](file:///d:/DL/nlpHMM.py): Install `nltk`:
  ```powershell
  pip install nltk
  ```

---

## 3. Script 1: `nlp.py` (From-Scratch Viterbi Algorithm)

### How It Works
1. **Hidden States (POS Tags)**: `['DET', 'NOUN', 'VERB']`.
2. **Initial Probabilities ($\pi$)**: Defines the prior probability of a sentence starting with a tag.
3. **Transition Probabilities ($A$)**: Probability of transitioning from tag $t_{i-1}$ to tag $t_i$.
4. **Emission Probabilities ($B$)**: Probability of a tag emitting an observed word.
5. **Log-Space Computation**: Uses `math.log()` to prevent floating-point underflow when multiplying small probabilities.
6. **Dynamic Programming Matrix & Backpointers**: Tracks the best score for each state at each time step and records backpointers for optimal sequence traceback.

### Execution Command
```powershell
python nlp.py
```
*(Or `.\.venv\Scripts\python.exe nlp.py`)*

### Input Sentence
```python
sentence = "the dog barks"
```

### Expected Output
```text
Input Sentence: the dog barks
POS Tags:
the -> DET
dog -> NOUN
barks -> VERB
```

---

## 4. Script 2: `nlpHMM.py` (NLTK Supervised HMM on Penn Treebank)

### How It Works
1. **Corpus Download**: Downloads the NLTK Penn Treebank dataset using `nltk.download('treebank', quiet=True)`.
2. **Training Data**: Loads the first 300 tagged sentences from the Wall Street Journal section of the Penn Treebank.
3. **Model Training**: Initializes `nltk.tag.hmm.HiddenMarkovModelTrainer` and trains a supervised HMM (`train_supervised`).
4. **Inference**: Predicts POS tags for a test sentence using the Viterbi decoder built into NLTK.

### Execution Command
```powershell
python nlpHMM.py
```
*(Or `.\.venv\Scripts\python.exe nlpHMM.py`)*

### Input Sentence
```python
sentence = "The company said it expects a profit ."
```

### Expected Output
```text
Input Sentence: The company said it expects a profit .
POS Tags: [('The', 'DT'), ('company', 'NN'), ('said', 'VBD'), ('it', 'PRP'), ('expects', 'VBZ'), ('a', 'DT'), ('profit', 'NN'), ('.', '.')]
```

> **Note on NLTK Runtime Warning:**
> You may see warnings like `RuntimeWarning: overflow encountered in cast` from `nltk/tag/hmm.py`. This occurs when zero-probabilities are mapped to $-\infty$ in log-space and cast to numpy float arrays. This is standard behavior within NLTK and does not affect the correctness of the predicted tags.

---

## 5. Tagset Reference (Penn Treebank)

Common tags encountered in [`nlpHMM.py`](file:///d:/DL/nlpHMM.py):

| Tag | Category | Example |
| :--- | :--- | :--- |
| `DT` | Determiner | *The, a, an* |
| `NN` | Noun, singular or mass | *company, profit* |
| `VBD` | Verb, past tense | *said, went* |
| `PRP` | Personal pronoun | *it, he, they* |
| `VBZ` | Verb, 3rd person singular present | *expects, is* |
| `.` | Sentence-final punctuation | *.* |

---

## 6. Troubleshooting & FAQs

- **`Python was not found` error in Windows PowerShell:**
  Use the full path to the virtual environment Python interpreter:
  ```powershell
  .\.venv\Scripts\python.exe nlp.py
  .\.venv\Scripts\python.exe nlpHMM.py
  ```
- **NLTK Download Fails Behind a Proxy or Offline:**
  Ensure internet connectivity on first run so NLTK can fetch the `treebank` corpus into `~/nltk_data`. Alternatively, download manually via Python:
  ```powershell
  python -c "import nltk; nltk.download('treebank')"
  ```
- **Customizing Sentences:**
  - In [`nlp.py`](file:///d:/DL/nlp.py), modify line 29: `sentence = "the dog barks".lower().split()`. Ensure all words are present in `emit_prob`.
  - In [`nlpHMM.py`](file:///d:/DL/nlpHMM.py), modify line 17: `sentence = "Your sentence here .".split()`.
