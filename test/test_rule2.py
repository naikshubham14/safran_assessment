from src.validators.rule2 import Rule2Validator

def test_rule2_validator():
    validator = Rule2Validator()
    
    # Valid: Active voice
    assert validator.validate("The manufacturer supplies the safety procedures.") == False
    
    # Violation: Passive voice
    assert validator.validate("The safety procedures are supplied by the manufacturer.") == True
    
    # Violation: Passive voice without "by"
    assert validator.validate("The report was submitted.") == True
    
    # Edge case: Adjective mistaken for passive (spaCy may misclassify)
    assert validator.validate("The door is closed.") == True # Flagged as per problem statement
    
    # Valid: Active voice with imperative
    assert validator.validate("Connect the circuits using a relay.") == False