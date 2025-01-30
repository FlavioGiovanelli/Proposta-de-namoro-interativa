import customtkinter as ctk
import random  # Para movimentar o botão "Não" aleatoriamente

# Configuração inicial do tema
ctk.set_appearance_mode("Dark")  # Modos disponíveis: "Light", "Dark", "System"
ctk.set_default_color_theme("blue")  # Define a paleta de cores da interface

# Criação da janela principal
janela = ctk.CTk()
janela.geometry("600x400")  # Define o tamanho da janela
janela.title("Proposta de Namoro")  # Define o título da aplicação

# Texto principal da interface
texto_principal = ctk.CTkLabel(janela, text="Quer namorar comigo? ❤️", font=("Arial", 24))
texto_principal.pack(pady=30)  # Adiciona espaçamento ao redor do texto

# Função chamada ao clicar no botão "Sim"
def aceitar():
    texto_principal.configure(text="Agora a gente namora!")  # Atualiza a mensagem
    botao_nao.place_forget()  # Remove o botão "Não" da tela
    botao_sim.place(relx=0.5, rely=0.7, anchor="center")  # Reposiciona o botão "Sim" ao centro

# Função que move o botão "Não" para uma posição aleatória
def mover_botao_nao(event):
    nova_x = random.randint(10, 500)
    nova_y = random.randint(10, 300)
    botao_nao.place(x=nova_x, y=nova_y)  # Atualiza a posição do botão

# Botão "Sim"
botao_sim = ctk.CTkButton(
    janela, text="Sim", fg_color="green", hover_color="darkgreen",
    font=("Arial", 18), command=aceitar
)
botao_sim.place(relx=0.3, rely=0.6, anchor="center")

# Botão "Não"
botao_nao = ctk.CTkButton(
    janela, text="Não", fg_color="red", hover_color="darkred", font=("Arial", 18)
)
botao_nao.place(relx=0.7, rely=0.6, anchor="center")

# Quando o mouse passa sobre o botão "Não", ele se move
botao_nao.bind("<Enter>", mover_botao_nao)

# Mantém a interface em execução
janela.mainloop()