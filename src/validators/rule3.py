import google.generativeai as genai
from typing import List

class Rule3Validator:
    """
    Checks for multiple instructions in a single sentence, using Gemini for contextual simultaneity checks.
    """
    
    def __init__(self, gemini_api_key: str, nlp):
        self.nlp = nlp
        self.conjunctions = {"and", "or", "then"}
        self.simultaneous_keywords = {"at the same time", "simultaneously", "while"}
        
        # Configure Gemini
        genai.configure(api_key=gemini_api_key)
        self.llm = genai.GenerativeModel("gemini-1.5-flash-latest")
    
    def validate(self, sentence: str) -> bool:
        """
        Identifies multiple instructions unless simultaneous (using Gemini for ambiguity).
        Args:
            str: Input sentence
            
        Returns:
            bool: Validation flag
        """
        doc = self.nlp(sentence)
        
        # Allow explicit keywords
        if any(keyword in sentence.lower() for keyword in self.simultaneous_keywords):
            return False
        
        # Check for multiple root verbs
        root_verbs = [token for token in doc if token.dep_ == "ROOT" and token.pos_ == "VERB"]
        if len(root_verbs) < 2:
            return False
        
        # Use Gemini to check for implicit simultaneity
        if self._are_actions_simultaneous(sentence):
            return False
        else:
            return True
    
    def _are_actions_simultaneous(self, sentence: str) -> bool:
        """
        Queries Gemini to check if actions in the sentence occur simultaneously.
        Returns True (allow) or False (violation).
        """
        prompt = f"""
        Analyze this sentence from a technical manual:
        "{sentence}"

        Do the actions in this sentence occur at the same time? 
        Answer ONLY with YES or NO. Do NOT explain.
        """
        
        try:
            response = self.llm.generate_content(prompt)
            return response.text.strip().upper() == "YES"
        except Exception as e:
            print(f"Gemini API error: {e}")
            return False  # Fallback to default behavior