import { useState } from "react";
import { classifyEmail, classifyFile } from "./api";
import { BeatLoader } from "react-spinners";

export default function App() {
  const [file, setFile] = useState(null);
  const [hideManual, setHideManual] = useState(false);
  const [texto, setTexto] = useState("");
  const [resp, setResp] = useState(null);
  const [loading, setLoad] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoad(true);
    const data = await classifyEmail(texto);
    setResp(data);
    setLoad(false);
  };

  const handleFileSelect = (e) => {
    const selectedFile = e.target.files[0];
    if (!selectedFile) return;
    setFile(selectedFile);
  };

  const handleFileSubmit = async () => {
    if (!file) return;
    setHideManual(true);
    setLoad(true);
    const data = await classifyFile(file);
    setResp(data);
    setLoad(false);
  };

  return (
    <>
      <h2 className="title-classificador">Classificador AutoU</h2>
      <p className="subtitle-classificador">
        Classifique e responda e-mails de forma automática e inteligente!
      </p>

      <div className="container">
        <h3>Envie um arquivo (.txt ou .pdf)</h3>
        <input type="file" accept=".txt,.pdf" onChange={handleFileSelect} />

        {file && (
          <button
            style={{ marginTop: "1rem" }}
            onClick={handleFileSubmit}
            disabled={loading}
          >
            {loading ? <BeatLoader size={16} /> : "Classificar arquivo"}
          </button>
        )}

        {!hideManual && (
          <>
            <hr />
            <h3>Ou cole o texto:</h3>
            <form onSubmit={handleSubmit}>
              <textarea
                value={texto}
                onChange={(e) => setTexto(e.target.value)}
                rows={8}
                style={{ width: "100%" }}
              />
              <button disabled={loading}>
                {loading ? (
                  <BeatLoader size={15} color="white" />
                ) : (
                  "Classificar texto"
                )}
              </button>
            </form>
          </>
        )}

        {resp && (
          <div>
            <h2>Categoria: {resp.categoria}</h2>

            <textarea
              readOnly
              value={resp.resposta}
              rows={4}
              style={{ width: "100%" }}
            />
            <button
              onClick={() => navigator.clipboard.writeText(resp.resposta)}
            >
              Copiar resposta
            </button>
          </div>
        )}
      </div>
    </>
  );
}
