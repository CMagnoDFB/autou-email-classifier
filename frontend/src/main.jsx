import { useState } from "react";
import { classifyEmail, extractFileText } from "./api";
import { BeatLoader } from "react-spinners";
import Textarea from "@mui/joy/Textarea";
import { MdContentCopy } from "react-icons/md";
import { MdOutlineSettings } from "react-icons/md";

export default function App() {
  const [file, setFile] = useState(null);
  const [hideManual, setHideManual] = useState(false);
  const [texto, setTexto] = useState("");
  const [resp, setResp] = useState(null);
  const [loading, setLoad] = useState(false);

  // modelo selecionado: "reglog" | "zeroshot"
  const [model, setModel] = useState("reglog");

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoad(true);
    const data = await classifyEmail(texto, model);
    setResp(data);
    setLoad(false);
  };

  const handleFileSelect = async (e) => {
    const selectedFile = e.target.files[0];
    if (!selectedFile) return;

    setFile(selectedFile);
    setHideManual(true); // some a área “cole o texto”
    setLoad(true);

    try {
      const extracted = await extractFileText(selectedFile);
      setTexto(extracted); // mostra o texto extraído
    } finally {
      setLoad(false);
    }
  };

  const handleFileSubmit = async () => {
    if (!texto.trim()) return; // já temos o texto extraído
    setLoad(true);
    const data = await classifyEmail(texto, model);
    setResp(data);
    setLoad(false);
  };

  return (
    <>
      <h2 className="title-classificador">Classificador AutoU</h2>
      <p className="subtitle-classificador">
        Classifique e responda e-mails de forma automática e inteligente!
      </p>
      <p className="subtitle-classificador">
        O e-mail será classificado como <strong>"Produtivo"</strong> ou{" "}
        <strong>"Improdutivo"</strong>.
      </p>

      <div className="container">
        <h3>Envie um arquivo (.txt ou .pdf)</h3>
        <input type="file" accept=".txt,.pdf" onChange={handleFileSelect} />

        {file && texto && (
          <>
            <h4>Texto extraído do arquivo:</h4>
            <Textarea
              readOnly
              value={texto}
              variant="soft"
              size="md"
              color="neutral"
              rows={8}
              style={{ width: "100%", marginTop: "1rem" }}
            />
            <button
              style={{ marginTop: "1rem" }}
              onClick={handleFileSubmit}
              disabled={loading}
            >
              {loading ? <BeatLoader size={16} /> : "Classificar arquivo"}
            </button>
          </>
        )}

        {!hideManual && (
          <>
            <hr />
            <h3>Ou cole o texto:</h3>
            <form onSubmit={handleSubmit}>
              <Textarea
                value={texto}
                onChange={(e) => setTexto(e.target.value)}
                minRows={8}
                variant="soft"
                size="md"
                color="neutral"
                placeholder="Insira o texto aqui"
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

            <Textarea
              readOnly
              value={resp.resposta}
              variant="soft"
              size="md"
              color="neutral"
              rows={4}
              style={{ width: "100%" }}
            />
            <div className="response">
              <button
                className="copy-button"
                onClick={() => navigator.clipboard.writeText(resp.resposta)}
              >
                <MdContentCopy /> Copiar
              </button>
            </div>
          </div>
        )}
      </div>
      <div className="settings-card">
        <div className="settings-header">
          <MdOutlineSettings size={24} />
          <h4>Selecionar modelo de classificação</h4>
        </div>

        <label className="radio-line">
          <input
            type="radio"
            name="model"
            value="reglog"
            checked={model === "reglog"}
            onChange={(e) => {
              setModel(e.target.value);
            }}
          />
          Regressão Logística
        </label>

        <label className="radio-line">
          <input
            type="radio"
            name="model"
            value="zeroshot"
            checked={model === "zeroshot"}
            onChange={(e) => {
              setModel(e.target.value);
            }}
          />
          Zero‑Shot (mDeBERTa)
        </label>
      </div>
    </>
  );
}
