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
Baixe este repositório. Depois, no terminal:

```bash

# Instale o Playwright (apenas 1x)
pip install playwright

# Instale o Customtkinter (apenas 1x)
playwright install customtkinter

# Rode o script
python main.py
