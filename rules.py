BOOLEAN_MAP = {
    "true": True,
    "false": False,
    "yes": True,
    "no": False
}

def apply_rules(correct: str, student: str):
    if not correct or not student:
        return None

    c = correct.lower().strip()
    s = student.lower().strip()

    # 1️⃣ Boolean rule (true/false, yes/no)
    if c in BOOLEAN_MAP and s in BOOLEAN_MAP:
        return 1.0 if BOOLEAN_MAP[c] == BOOLEAN_MAP[s] else 0.0

    # 2️⃣ STRICT exact match rule (VERY IMPORTANT)
    # Apply ONLY if both are short AND exactly equal
    if len(c.split()) <= 2 and len(s.split()) <= 2:
        if c == s:
            return 1.0
        else:
            return 0.0

    # 3️⃣ Otherwise, rules do NOT apply
    return None
