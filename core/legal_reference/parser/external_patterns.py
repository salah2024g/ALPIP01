import re


LAW_PATTERN = re.compile(
    r"القانون\s+رقم\s+([0-9٠-٩]+)\s+لسنة\s+([0-9٠-٩]+)"
)


DECISION_PATTERN = re.compile(
    r"قرار\s+(?:الوزير|رئيس\s+مجلس\s+الوزراء|رئيس\s+الجمهورية)\s+رقم\s+([0-9٠-٩]+)\s+لسنة\s+([0-9٠-٩]+)"
)


REGULATION_PATTERN = re.compile(
    r"اللائحة\s+التنفيذية"
)
