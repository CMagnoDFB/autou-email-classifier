import icon from "./assets/autou.png";

export default function Header() {
  return (
    <header>
      <img src={icon} alt="AutoU Classificador de E-mails" />
      <div className="header-text">
        <h1>AutoU - Classificador de E-mails</h1>
        <p>Classifique e responda e-mails de forma automática e inteligente</p>
      </div>
    </header>
  );
}
