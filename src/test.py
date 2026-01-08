from device import get_device
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
model = AutoModelForSequenceClassification.from_pretrained(
    "distilbert-base-uncased-finetuned-sst-2-english"
).to(get_device)

text = "Testing the GPU setup on Windows."
inputs = tokenizer(text, return_tensors="pt").to(get_device)

with torch.no_grad():
    outputs = model(**inputs)

pred = outputs.logits.argmax(dim=-1).item()
label = model.config.id2label[pred]
print("Prediction:", label)
