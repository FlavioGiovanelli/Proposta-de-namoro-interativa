import customtkinter as ctk 
import random  # Importa a biblioteca para movimentar o botão "Não" aleatoriamente

# ---------------------------- Configuração do Tema ----------------------------
# Definir o modo de aparência da janela (escuro, claro ou modo do sistema)
ctk.set_appearance_mode("Dark")  # Opções: "Light", "Dark", "System"

# Definir o tema de cores (padrão em azul)
ctk.set_default_color_theme("blue")  # Define o tema de cores

# ---------------------------- Criação da Janela Principal ----------------------------
# Criar a janela principal da aplicação
janela = ctk.CTk()
janela.geometry("600x400")  # Define as dimensões da janela
janela.title("Proposta de Namoro")  # Define o título da janela

# ---------------------------- Elementos Visuais ----------------------------
# Label de texto principal que será exibido na janela
texto_principal = ctk.CTkLabel(
    janela, text="Quer namorar comigo? ❤️", font=("Arial", 24)
)
texto_principal.pack(pady=30)  # Adiciona o texto com espaçamento

# ---------------------------- Funções de Ação ----------------------------

# Função chamada quando o usuário clica no botão "Sim"
def aceitar():
    texto_principal.configure(text="Agora a gente namora!")  # Atualiza o texto da label
    botao_nao.place_forget()  # Remove o botão "Não" da tela
    botao_sim.place(relx=0.5, rely=0.7, anchor="center")  # Centraliza o botão "Sim"

# Função que move o botão "Não" aleatoriamente dentro da janela
def mover_botao_nao(event):
    nova_x = random.randint(10, 500)  # Define uma nova posição X aleatória
    nova_y = random.randint(10, 300)  # Define uma nova posição Y aleatória
    botao_nao.place(x=nova_x, y=nova_y)  # Mover o botão para a nova posição

# ---------------------------- Botões ----------------------------

# Botão "Sim" que será exibido na janela
botao_sim = ctk.CTkButton(
    janela,
    text="Sim",  # Texto do botão
    fg_color="green",  # Cor de fundo do botão
    hover_color="darkgreen",  # Cor de fundo ao passar o mouse sobre o botão
    font=("Arial", 18),  # Fonte do texto no botão
    command=aceitar,  # Ação associada ao botão (chama a função "aceitar")
)
botao_sim.place(relx=0.3, rely=0.6, anchor="center")  # Posição inicial do botão "Sim"

# Botão "Não" que será exibido na janela
botao_nao = ctk.CTkButton(
    janela,
    text="Não",  # Texto do botão
    fg_color="red",  # Cor de fundo do botão
    hover_color="darkred",  # Cor de fundo ao passar o mouse sobre o botão
    font=("Arial", 18),  # Fonte do texto no botão
)
botao_nao.place(relx=0.7, rely=0.6, anchor="center")  # Posição inicial do botão "Não"

# Adiciona um evento para mover o botão "Não" aleatoriamente quando o mouse passar sobre ele
botao_nao.bind("<Enter>", mover_botao_nao)

# ---------------------------- Execução da Janela ----------------------------
# Inicia a interface gráfica e mantém a janela aberta
janela.mainloop()
