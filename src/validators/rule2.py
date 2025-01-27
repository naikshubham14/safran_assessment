class Rule2Validator:
    """
    Checks if a sentence uses passive voice.
    """
    
    def __init__(self, nlp):
        self.nlp = nlp
    
    def validate(self, sentence: str) -> bool:
        """
        Identifies passive voice in a sentence.
        
        Args:
            str: Input sentence
            
        Returns:
            bool: Validation flag
        """
        doc = self.nlp(sentence)
        
        # Check for passive voice: "auxpass" dependency + past participle (VBN)
        for token in doc:
            if token.tag_ == "VBN":
                for child in token.children:
                    if child.dep_ == "auxpass":
                        return True
        
        return False