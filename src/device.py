import torch

def get_device():
    if torch.cuda.is_available():
        device_name = torch.cuda.get_device_name(0)
        print(f"Using NVIDIA GPU: {device_name}")
        return torch.device("cuda")
    
    if torch.backends.mps.is_available():
        print("Using Apple Silicon (MPS)")
        return torch.device("mps")
    
    print("GPU not found, using CPU")
    return torch.device("cpu")


def main():
    get_device()


if __name__ == "__main__":
    main()