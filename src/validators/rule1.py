class Rule1Validator:
    """
    Checks if nouns/noun clusters are preceded by an article (the, a, an) or demonstrative (this, these, that, those).
    """
    
    def __init__(self, nlp):
        self.allowed_determiners = {"a", "an", "the", "this", "these", "that", "those"}
        self.nlp = nlp
    
    def validate(self, sentence: str) -> bool:
        """
        Identifies violations of Rule 1 in a sentence.
        
        Args:
            str: Input sentence
            
        Returns:
            bool: Validation flag
        """
        doc = self.nlp(sentence)
        
        for chunk in doc.noun_chunks:
            # Check if the noun chunk starts with a valid determiner
            first_token = chunk.root.head if chunk.root.dep_ == "det" else chunk[0]
            if first_token.text.lower() not in self.allowed_determiners:
                return True
        
        return False