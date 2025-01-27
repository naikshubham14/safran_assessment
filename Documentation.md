# Documentation

## Overview
This module checks if input text complies with 5 predefined technical writing rules. It uses NLP libraries (spaCy) and optional GenAI (Gemini) for contextual analysis.

## Workflow
1. **Input Handling**:
   - Accepts text input as Text String or file via Streamlit UI.
   - No preprocessing (preserves original formatting).

2. **Sentence Splitting**:
   - Splits text into sentences using spaCy’s `sentencizer`.

3. **Rule Validation**:
   - Applies rules sequentially per sentence:
     1. **Rule 1**: Articles/demonstratives before nouns.
     2. **Rule 2**: Active voice detection.
     3. **Rule 3**: Single instruction/sentence (Gemini resolves ambiguity).
     4. **Rule 4**: Imperative form.
     5. **Rule 5**: Sentence length ≤20 words.

4. **Output**:
   - Returns violations with boolean flags and messages.
   - Streamlit UI displays results in a user-friendly format.

---

## Architectural Decisions
1. **NLP Library**:  
   - **spaCy** over NLTK/StanfordNLP for efficiency in dependency parsing and noun chunk detection.

2. **Modular Validators**:  
   - Each rule has a separate validator class to simplify testing and maintenance.

3. **Hybrid Approach (Rule 3)**:  
   - Uses **spaCy** for basic checks + **Gemini** for nuanced simultaneity detection.

4. **Streamlit UI**:  
   - Prioritized simplicity over Flask/Django for rapid prototyping.

5. **Boolean Flags**:  
   - Validators return `True/False` for violations to decouple logic from messaging.

---

## Assumptions
1. **No Preprocessing**:  
   - Original casing/punctuation preserved to avoid altering context.

2. **Rule 1**:  
   - Articles/demonstratives must directly precede noun chunks (ignores edge cases like possessives).

3. **Rule 2**:  
   - Passive voice detected via `auxpass` dependency + past participles.

4. **Rule 4**:  
   - Imperative = root verb in base form (`VB` tag) with no explicit subject.

5. **Rule 3**:  
   - Gemini resolves ambiguous simultaneity (assumes API availability).

6. **Sentence Segmentation**:  
   - Relies on spaCy’s `sentencizer` (may fail on abbreviations like "Dr.").

---

## I/O Fromats
## Input
- Input can be provided as either a text string in text box or as a .txt file upload 
- The Input format can be selected from the toggle option in sidebar

## Output
- In case of text input, output will displayed on the same screen with each sentence annotated with identification number of all the rules the sentence violates
- In case of file input output will be a downloadable docx file with the orginal text with each sentence annotated with identification number of all the rules the sentence violates

## Setup & Usage
### Prerequisites
- Python 3.8+
- Libraries: `spaCy`, `streamlit`, `google-generativeai` (optional).

### Installation
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm