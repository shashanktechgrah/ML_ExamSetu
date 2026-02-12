from fastapi import FastAPI
from pydantic import BaseModel
from scorer import evaluate_answer

app = FastAPI(title="Advanced Subjective Evaluation Service")

class EvaluateRequest(BaseModel):
    correct_answer: str
    student_answer: str
    max_marks: float

@app.get("/")
def health():
    return {"status": "ML service running"}

@app.post("/evaluate")
def evaluate(req: EvaluateRequest):
    similarity = evaluate_answer(
        req.correct_answer,
        req.student_answer
    )

    marks = round(similarity * req.max_marks, 2)

    return {
        "similarity_score": similarity,
        "marks_obtained": marks
    }
