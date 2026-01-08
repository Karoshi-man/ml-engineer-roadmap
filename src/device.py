import torch

if torch.backends.mps.is_available():
    device = torch.device("mps")      # Mac M1/M2
elif torch.cuda.is_available():
    device = torch.device("cuda")     # Windows / Linux GPU
else:
    device = torch.device("cpu")      # fallback

print("Using device:", device)
