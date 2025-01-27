from src.validators.rule4 import Rule4Validator

def test_rule4_validator():
    validator = Rule4Validator()
    
    # Valid: Imperative form
    assert validator.validate("Continue the test.") == False
    assert validator.validate("Remove oil and grease.") == False
    assert validator.validate("Do not touch the screen.") == False
    
    # Violation: Non-imperative (passive)
    assert validator.validate("The test can be continued.") == True
    
    # Violation: Explicit subject ("You")
    assert validator.validate("You must press the button.") == True
    # Edge case: Gerund as root
    assert validator.validate("Removing the panel...") == True