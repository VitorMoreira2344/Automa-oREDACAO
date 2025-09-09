# Automação de Login - Sala do Futuro (Playwright)

Este projeto automatiza o login no site [Sala do Futuro](https://saladofuturo.educacao.sp.gov.br) usando [Playwright para Python](https://playwright.dev/python/).  
Inclui um guia para transformar o script em um executável `.exe` portátil com **auto-py-to-exe**.

---

## 📌 Funcionalidades
- Acessa a página de escolha de perfil.
- Seleciona **Estudante**.
- Preenche RA, dígito e senha.
- Clica no botão **Acessar**.
- Mantém a página aberta para verificação.

---

## ✅ Pré-requisitos
- **Python 3.10+**
- **pip**
- **Google Chrome não é necessário** (o Playwright instala seu próprio Chromium).

---

## 🔧 Instalação e execução pelo Python
Clone ou baixe este repositório. Depois, no terminal:

```bash
# Crie um ambiente virtual
python -m venv .venv
.venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Instale navegadores do Playwright (apenas 1x)
playwright install chromium

# Rode o script
python main.py
