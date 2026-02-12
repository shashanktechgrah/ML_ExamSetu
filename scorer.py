from rules import apply_rules
from similarity import semantic_similarity

def evaluate_answer(correct: str, student: str) -> float:
    # 1️⃣ Rule-based scoring
    rule_score = apply_rules(correct, student)
    if rule_score is not None:
        return rule_score

    # 3️⃣ Semantic similarity fallback
    return semantic_similarity(correct, student)

