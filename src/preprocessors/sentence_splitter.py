import spacy

class SentenceSplitter:
    """
    Splits input text into sentences using spaCy sentence segmentation.
    Preserves original formatting (no lowercase, no stopword removal, etc.).
    """
    
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        # Explicitly add sentencizer to pipeline (disables parser for efficiency)
        self.nlp.add_pipe("sentencizer")
    
    def split_sentences(self, text: str) -> list[str]:
        """
        Split raw text into sentences.
        
        Args:
            text (str): Input text corpus 
        Returns:
            list[str]: List of sentences
        """
        doc = self.nlp(text)
        return [sent.text.strip() for sent in doc.sents]