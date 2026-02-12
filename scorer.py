from rules import apply_rules
from nli import nli_inference
from similarity import semantic_similarity

def evaluate_answer(correct: str, student: str) -> float:
    # 1️⃣ Rule-based scoring
    rule_score = apply_rules(correct, student)
    if rule_score is not None:
        return rule_score

    # 2️⃣ NLI-based reasoning
    nli_result = nli_inference(correct, student)

    if nli_result == "CONTRADICTION":
        return 0.0
    elif nli_result == "ENTAILMENT":
        return 1.0

    # 3️⃣ Semantic similarity fallback
    return semantic_similarity(correct, student)
