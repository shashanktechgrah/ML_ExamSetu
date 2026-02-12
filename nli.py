from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

MODEL_NAME = "cross-encoder/nli-deberta-v3-base"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

LABELS = ["CONTRADICTION", "NEUTRAL", "ENTAILMENT"]

def nli_inference(premise: str, hypothesis: str):
    inputs = tokenizer(
        premise,
        hypothesis,
        return_tensors="pt",
        truncation=True,
        padding=True
    )

    with torch.no_grad():
        logits = model(**inputs).logits

    prediction = torch.argmax(logits, dim=1).item()
    return LABELS[prediction]
