import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk

# Definindo o tema escuro globalmente
ctk.set_appearance_mode("dark")  # Tema escuro
ctk.set_default_color_theme("dark-blue")  # Definindo um esquema de cores

# Dicionário de usuários e senhas
usuarios = {
    "admin": "senha123",
    "usuario1": "senha456",
    "teste": "teste123"
}

# Função de verificação de login
def verificar_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    # Verificar se o usuário e senha estão no dicionário
    if usuario in usuarios and usuarios[usuario] == senha:
        messagebox.showinfo("Login Bem-sucedido", f"Bem-vindo, {usuario}!")
        abrir_menu(usuario)  # Abre o menu após login bem-sucedido
        root.destroy()  # Fecha a janela de login
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos!")

# Função para abrir o menu de opções
def abrir_menu(usuario):
    menu_window = ctk.CTk()
    menu_window.title(f"Menu - {usuario}")
    menu_window.geometry("350x210")
    menu_window.resizable(width= False, height= False) ## Limitação para o usuário não expandir a tela do aplicativo

    # Função para exibir o dashboard de receitas
    def mostrar_dados_financeiros(tipo):
        if tipo == "receitas":
            messagebox.showinfo("Dashboard de Receitas", "Aqui você pode visualizar suas receitas.")
        elif tipo == "despesas":
            messagebox.showinfo("Dashboard de Despesas", "Aqui você pode visualizar suas despesas.")
        elif tipo == "geral":
            messagebox.showinfo("Dashboard Geral", "Aqui você pode ver o controle geral de finanças.")
    
    # Adicionando o menu
    welcome_label = ctk.CTkLabel(menu_window, text=f"Bem-vindo ao sistema de controle financeiro, {usuario}!", font=("Arial", 14))
    welcome_label.pack(pady=10)

    # Botões para os dashboards
    btn_receitas = ctk.CTkButton(menu_window, text="Dashboard de Receitas", width=200, command=lambda: mostrar_dados_financeiros("receitas"))
    btn_receitas.pack(pady=10)

    btn_despesas = ctk.CTkButton(menu_window, text="Dashboard de Despesas", width=200, command=lambda: mostrar_dados_financeiros("despesas"))
    btn_despesas.pack(pady=10)

    btn_geral = ctk.CTkButton(menu_window, text="Dashboard Geral", width=200, command=lambda: mostrar_dados_financeiros("geral"))
    btn_geral.pack(pady=10)

    menu_window.mainloop()

# Criar a janela principal de login
root = ctk.CTk()
root.title("Tela de login")
root.geometry("300x220")
root.resizable(width= False, height= False) ## Limitação para o usuário não expandir a tela do aplicativo

# Adicionar os elementos da interface de login
label_usuario = ctk.CTkLabel(root, text="Usuário:")
label_usuario.pack(pady=5)

entry_usuario = ctk.CTkEntry(root)
entry_usuario.pack(pady=5)

label_senha = ctk.CTkLabel(root, text="Senha:")
label_senha.pack(pady=5)

entry_senha = ctk.CTkEntry(root, show="*")
entry_senha.pack(pady=5)

# Botão de login
btn_login = ctk.CTkButton(root, text="Login", command=verificar_login)
btn_login.pack(pady=20)

# Iniciar o loop principal
root.mainloop()