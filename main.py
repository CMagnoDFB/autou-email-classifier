import sys
from src.classifier import classify

if __name__ == "__main__":
    email_text = sys.stdin.read() if not sys.argv[1:] else " ".join(sys.argv[1:])
    resultado = classify(email_text)
    print(resultado)