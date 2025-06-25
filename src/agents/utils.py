# utils.py
# Shared helper functions for agents

def clean_code(code):
    return code.strip()

def detect_division_by_zero(code):
    return "0" in code and "/ 0" in code
