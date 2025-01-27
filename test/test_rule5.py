from src.validators.rule5 import Rule5Validator

def test_rule5_validator():
    validator = Rule5Validator()
    
    # Valid: 5 words
    assert validator.validate("This is a short sentence.") == False
    
    # Violation: 21 words
    long_sentence = " ".join(["word"] * 21)
    assert validator.validate(long_sentence) == True
    
    # Edge case: 20 words
    edge_sentence = " ".join(["word"] * 20)
    assert validator.validate(edge_sentence) == False
    
    # Test punctuation and hyphenated words
    assert validator.validate("State-of-the-art device—developed in 2020—supports 10+ users.") == False