import spacy
from typing import Optional

class Rule4Validator:
    """
    Checks if a sentence is written in the imperative form (Rule 4).
    """
    
    def __init__(self, nlp):
        self.nlp = nlp
    
    def validate(self, sentence: str) -> bool:
        """
        Identifies non-imperative sentences.
        
        Args:
            str: Input sentence
            
        Returns:
            bool: Validation flag
        """
        doc = self.nlp(sentence)
        root = self._get_root_verb(doc)
        
        if not root:
            return False
        
        # Check if root verb is in base form (VB) and lacks a nominal subject
        if root.tag_ != "VB":
            return True
        else:
            # Check for explicit subject
            for child in root.children:
                if child.dep_ == "nsubj":
                    return True
        
        return False
    
    def _get_root_verb(self, doc) -> Optional[spacy.tokens.Token]:
        """Extracts the root verb token from a parsed sentence."""
        for token in doc:
            if token.dep_ == "ROOT" and token.pos_ == "VERB":
                return token
        return None