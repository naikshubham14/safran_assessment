from typing import List, Dict
import spacy
from preprocessors.sentence_splitter import SentenceSplitter
from validators.rule1 import Rule1Validator
from validators.rule2 import Rule2Validator
from validators.rule3 import Rule3Validator
from validators.rule4 import Rule4Validator
from validators.rule5 import Rule5Validator

class RuleChecker:
    """
    Orchestrates the entire rule-checking workflow.
    Processes input text, splits sentences, and checks all rules.
    """
    
    def __init__(self, gemini_api_key: str = None):
        # Initialize modules
        nlp = spacy.load("en_core_web_sm")
        self.splitter = SentenceSplitter()
        self.rule1 = Rule1Validator(nlp)
        self.rule2 = Rule2Validator(nlp)
        self.rule3 = Rule3Validator(gemini_api_key, nlp) if gemini_api_key else None
        self.rule4 = Rule4Validator(nlp)
        self.rule5 = Rule5Validator(nlp)
    
    def check_rules(self, text: str) -> List[Dict]:
        """
        Processes input text and checks all rules.
        
        Args:
            text (str): Input text
            
        Returns:
            List[Dict]: List of results per sentence
        """
        results = []
        sentences = self.splitter.split_sentences(text)
        
        for sentence in sentences:
            violations = []
            
            # Check Rule 1
            violations.append(self.rule1.validate(sentence))
            
            # Check Rule 2
            violations.append(self.rule2.validate(sentence))
            
            # Check Rule 3 (if Gemini is enabled)
            violations.append(self.rule3.validate(sentence))
            
            # Check Rule 4
            violations.append(self.rule4.validate(sentence))
            
            # Check Rule 5
            violations.append(self.rule5.validate(sentence))
            
            results.append({
                "sentence": sentence,
                "violations": violations
            })
        
        return results