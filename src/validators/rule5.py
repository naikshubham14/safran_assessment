class Rule5Validator:
    """
    Checks if a sentence exceeds 20 words (Rule 5: "Write short sentences").
    """
    
    def __init__(self, nlp):
        self.nlp = nlp
    
    def validate(self, sentence: str) -> bool:
        """
        Checks if the sentence has more than 20 words (excluding punctuation and spaces).
        
        Args:
            str: Input sentence
            
        Returns:
            bool: Validation flag
        """
        doc = self.nlp(sentence)
        word_count = sum(
            1 for token in doc 
            if not token.is_punct and not token.is_space
        )
        return True if word_count > 20 else False