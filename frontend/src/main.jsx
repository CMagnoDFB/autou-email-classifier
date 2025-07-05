import { useState } from "react";
import { classifyEmail } from "./api";

export default function App() {
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

  return (
    <div className="container">
      <h1>Insira aqui o e-mail a ser classificado:</h1>
      <form onSubmit={handleSubmit}>
        <textarea
          value={texto}
          onChange={(e) => setTexto(e.target.value)}
          rows={8}
          style={{ width: "100%" }}
        />
        <button disabled={loading}>Classificar</button>
      </form>

      {resp && (
        <div>
          <h2>Categoria: {resp.categoria}</h2>
          <p>Confiança: {resp.score}</p>
          <textarea
            readOnly
            value={resp.resposta}
            rows={4}
            style={{ width: "100%" }}
          />
          <button onClick={() => navigator.clipboard.writeText(resp.resposta)}>
            Copiar resposta
          </button>
        </div>
      )}
    </div>
  );
}
