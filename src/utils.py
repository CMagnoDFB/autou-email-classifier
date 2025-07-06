import io, magic
from pypdf import PdfReader

def extract_text(file_storage):
    """
    Recebe um werkzeug FileStorage e devolve o texto bruto.
    """
    buf = file_storage.read()
    mime = magic.from_buffer(buf, mime=True)

    if mime == "text/plain":
        return buf.decode("utf-8", errors="ignore")

    if mime == "application/pdf":
        reader = PdfReader(io.BytesIO(buf))
        return "\n".join(page.extract_text() or "" for page in reader.pages)

    raise ValueError("Formato não suportado")