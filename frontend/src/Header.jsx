import icon from "./assets/autou.png";

export default function Header() {
  return (
    <header>
      <img src={icon} alt="AutoU Classificador de E-mails" />
      <div className="header-text">
        <h1>Classificador de E-mails</h1>
        <p>Case prático de Desenvolvimento</p>
      </div>
    </header>
  );
}
