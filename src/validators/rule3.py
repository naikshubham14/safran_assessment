import spacy
import google.generativeai as genai
from typing import List, Optional


class Rule3Validator:
    """
    Checks for multiple instructions in a single sentence, using Gemini for contextual simultaneity checks.
    """
    
    def __init__(self, gemini_api_key: str, nlp):
        self.nlp = nlp
        self.conjunctions = {"and", "or", "then"}
        self.simultaneous_keywords = {
            "at the same time",
            "simultaneously",
            "while",
            "concurrently",
            "in parallel"
        }
        
        # Configure Gemini
        genai.configure(api_key=gemini_api_key)
        self.llm = genai.GenerativeModel("gemini-1.5-flash-latest")
    
    def validate(self, sentence: str) -> bool:
        """
        Identifies multiple instructions unless simultaneous (using Gemini for ambiguity).
        
        Args:
            sentence (str): Input sentence.
            
        Returns:
            bool: True if the sentence violates Rule 3 (multiple instructions without simultaneity).
        """
        doc = self.nlp(sentence)
        
        # Check for explicit simultaneity keywords
        if self._has_simultaneous_keywords(sentence):
            return False
        
        # Check for multiple actions via root verbs and subordinate clauses
        if self._has_multiple_actions(doc):
            # Use Gemini to check for implicit simultaneity
            if not self._are_actions_simultaneous(sentence):
                return True
        
        return False
    
    def _has_simultaneous_keywords(self, sentence: str) -> bool:
        """
        Checks if the sentence explicitly indicates simultaneous actions.
        """
        return any(keyword in sentence.lower() for keyword in self.simultaneous_keywords)
    
    def _has_multiple_actions(self, doc) -> bool:
        """
        Checks for multiple actions by counting root verbs and analyzing conjunctions.
        """
        # Identify root verbs
        root_verbs = [token for token in doc if token.dep_ == "ROOT" and token.pos_ == "VERB"]
        
        # Identify subordinate clauses or conjunction-based splits
        conjunctions = [token for token in doc if token.text.lower() in self.conjunctions]
        
        # Multiple actions are present if there are multiple root verbs or key conjunctions
        return len(root_verbs) > 1 or len(conjunctions) > 0
    
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
            # Fallback: assume actions are not simultaneous if the API fails
            return False
