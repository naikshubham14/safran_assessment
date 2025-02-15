# Rule Checker Module

## Overview
This project checks if technical writing adheres to 5 predefined rules:
1. Use articles/demonstratives before nouns.
2. Use active voice in procedural writing.
3. Write one instruction per sentence (unless simultaneous).
4. Use imperative (command) form.
5. Keep sentences under 20 words.

It uses **spaCy** for NLP tasks and **Gemini** (optional) for contextual analysis.

---

### Prerequisites
- Python 3.8+
- Libraries: `spaCy`, `streamlit`, `google-generativeai` (optional).


## Setup & Usage
### Prerequisites
- Python 3.8+
- Libraries: `spaCy`, `streamlit`, `google-generativeai` (optional).

### Installation
```bash
python -m venv venv
Windows: venv\Scripts\activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
git clone https://github.com/yourusername/rule-checker.git
cd rule-checker
```

### Deployment

Deployed using streamlit cloud 

[Click Here](https://safran-rule-checker.streamlit.app/)