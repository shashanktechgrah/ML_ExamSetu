from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-mpnet-base-v2")

def semantic_similarity(correct: str, student: str) -> float:
    emb1 = model.encode(correct, convert_to_tensor=True)
    emb2 = model.encode(student, convert_to_tensor=True)
    score = util.cos_sim(emb1, emb2).item()
    return round(score, 2)
