import customtkinter as ctk

ctk.set_appearance_mode('dark')
dados_login = {}

def validar_login(usuario_entry, senha_entry, redacao_textbox, app):
    usuario = usuario_entry.get().strip()
    senha = senha_entry.get().strip()
    redacao = redacao_textbox.get("1.0", "end-1c").strip()  # pega todo o texto da redação

    if "-" in usuario:
        ra, digito = usuario.split("-")
    else:
        ra, digito = usuario[:-1], usuario[-1]

    dados_login["ra"] = ra
    dados_login["digito"] = digito
    dados_login["senha"] = senha
    dados_login["redacao"] = redacao  # armazena a redação

    app.destroy()

def criar_janela():
    app = ctk.CTk()
    app.title('Login Automático')
    app.geometry('400x500')

    # Título
    ctk.CTkLabel(app, text='Login Sala do Futuro', font=('default', 15, 'bold')).pack(pady=(10, 17))

    # RA + dígito
    entrada_usuario = ctk.CTkEntry(app, placeholder_text='RA com dígito (ex: 1234567-8)', width=280)
    entrada_usuario.pack(pady=(0, 10))

    # Senha
    entrada_senha = ctk.CTkEntry(app, placeholder_text='Digite sua senha', show="*", width=280)
    entrada_senha.pack(pady=(0, 20))

    # Redação
    ctk.CTkLabel(app, text='Digite sua Redação:', font=('default', 12, 'bold')).pack(pady=(0,5))
    redacao_textbox = ctk.CTkTextbox(app, width=350, height=200)
    redacao_textbox.pack(pady=(0, 20))

    # Botão login
    ctk.CTkButton(app, text='Entrar',
                  command=lambda: validar_login(entrada_usuario, entrada_senha, redacao_textbox, app),
                  border_width=2, border_color='#005180', width=280).pack()

    app.mainloop()
    return dados_login
