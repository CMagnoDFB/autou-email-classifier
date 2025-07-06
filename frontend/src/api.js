import axios from "axios";

// usa a variável do .env ou fallback para localhost
const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || "http://localhost:5000",
});

export const classifyEmail = (text) =>
  api.post("/classify", { text }).then((r) => r.data);

export const extractFileText = (file) => {
  const form = new FormData();
  form.append("file", file);

  return api
    .post("/extract-text", form, {
      headers: { "Content-Type": "multipart/form-data" },
    })
    .then((r) => r.data.text); // devolve só o texto
};
