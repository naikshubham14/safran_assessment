from src.validators.rule1 import Rule1Validator

def test_rule1_validator():
    validator = Rule1Validator()
    
    # Valid: Contains "the"
    assert validator.validate("Turn the shaft assembly.") == False
    
    # Violation: Missing determiner
    assert validator.validate("Turn shaft assembly.") == True
    
    # Valid: Contains "this"
    assert validator.validate("This data module explains the process.") == False
    
    # Violation: Proper noun without determiner
    assert validator.validate("John manual is missing.") == True
    
    # Edge case: Determiner in the middle (should still flag)
    assert validator.validate("Assembly the shaft.") == True