import sys
import io

# Force stdin a ser UTF-8 no Windows
if sys.stdin.encoding.lower() != 'utf-8':
    sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')


from src.classifier import classify

if __name__ == "__main__":
    email_text = sys.stdin.read() if not sys.argv[1:] else " ".join(sys.argv[1:])
    resultado = classify(email_text)
    print(resultado)