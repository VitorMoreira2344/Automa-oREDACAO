import customtkinter as ctk

# ----- Configuração global -----
ctk.set_appearance_mode('dark')

# Variável para guardar os dados digitados
dados_login = {}

def validar_login(usuario_entry, senha_entry, app):
    usuario = usuario_entry.get().strip()
    senha = senha_entry.get().strip()

    # Divide RA e dígito (ex: 1234567-8)
    if "-" in usuario:
        ra, digito = usuario.split("-")
    else:
        ra, digito = usuario[:-1], usuario[-1]  # último dígito separado

    # Salva os valores
    dados_login["ra"] = ra
    dados_login["digito"] = digito
    dados_login["senha"] = senha

    app.destroy()  # fecha a janela

def criar_janela():
    app = ctk.CTk()
    app.title('Login Automático')
    app.geometry('320x250')

    # Título
    label_titulo = ctk.CTkLabel(app, text='Login Sala do Futuro',
                                font=('default', 15, 'bold'))
    label_titulo.pack(pady=(10, 17))

    # Entrada usuário
    entrada_usuario = ctk.CTkEntry(app,
                                   placeholder_text='RA com dígito (ex: 1234567-8)',
                                   width=280)
    entrada_usuario.pack(pady=(0, 22))

    # Entrada senha
    entrada_senha = ctk.CTkEntry(app,
                                 placeholder_text='Digite sua senha',
                                 show="*",
                                 width=280)
    entrada_senha.pack()

    # Botão login
    botao_login = ctk.CTkButton(
        app,
        text='Logar',
        command=lambda: validar_login(entrada_usuario, entrada_senha, app),
        border_width=2, border_color='#005180',
        width=280
    )
    botao_login.pack(pady=20)

    app.mainloop()
    return dados_login  # retorna pro Playwright
