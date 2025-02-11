import customtkinter as ctk
import random
import threading
import time
from PIL import Image, ImageTk

# Configuração dos botões
tamanho_sim = 40
tamanho_nao = 35
tamanho_max = 120
incremento_sim = 26

# Configuração da janela
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")
janela = ctk.CTk()
janela.attributes('-fullscreen', True)
janela.title("Proposta de Namoro")

# Texto principal
titulo = ctk.CTkLabel(janela, text="Quer namorar comigo? ❤️", font=("Arial", 72))
titulo.place(relx=0.5, rely=0.2, anchor="center")

# Função para aumentar o botão "Sim" e mover o "Não"
def mover_botao_nao():
    global tamanho_sim
    if tamanho_sim < tamanho_max:
        tamanho_sim += incremento_sim
        botao_sim.configure(font=("Arial", tamanho_sim))
    nova_x = random.uniform(0.3, 0.7)
    nova_y = random.uniform(0.5, 0.7)
    botao_nao.place(relx=nova_x, rely=nova_y, anchor="center")

# Função ao clicar no botão "Sim"
def aceitar():
    titulo.configure(text="Agora a gente namora! 💖", font=("Arial", 72))
    botao_nao.place_forget()
    botao_sim.place_forget()
    texto_escolha.place_forget()
    exibir_gif()

# Exibir GIF
def exibir_gif():
    gif_path = "Projetos\Proposta-de-namoro-interativa/amor-happy-valentines-day.gif"
    try:
        gif = Image.open(gif_path)
        gif_label = ctk.CTkLabel(janela, text="")
        gif_label.place(relx=0.5, rely=0.5, anchor="center")

        def animar_gif():
            while True:
                for frame in range(gif.n_frames):
                    gif.seek(frame)
                    img = ImageTk.PhotoImage(gif)
                    gif_label.configure(image=img)
                    gif_label.image = img
                    time.sleep(0.1)

        threading.Thread(target=animar_gif, daemon=True).start()
    except Exception as e:
        titulo.configure(text="Erro ao carregar GIF 💔")

# Criar corações espalhados sem sobrepor os elementos principais
def criar_coracoes():
    areas_proibidas = [
        (0.3, 0.7, 0.1, 0.3),  # Área do título
        (0.35, 0.65, 0.4, 0.5), # Área do texto de escolha
        (0.3, 0.7, 0.55, 0.75)  # Área dos botões
    ]
    
    for _ in range(10):  # Número de corações
        while True:
            x = random.uniform(0.05, 0.95)
            y = random.uniform(0.05, 0.95)
            sobrepoe = any(x1 <= x <= x2 and y1 <= y <= y2 for x1, x2, y1, y2 in areas_proibidas)
            if not sobrepoe:
                break

        coracao = ctk.CTkLabel(janela, text="❤️", font=("Arial", random.randint(20, 50)))
        coracao.place(relx=x, rely=y, anchor="center")

# Texto de escolha
texto_escolha = ctk.CTkLabel(janela, text="Escolha uma das opções abaixo:", font=("Arial", 44))
texto_escolha.place(relx=0.5, rely=0.45, anchor="center")

# Botão "Sim"
botao_sim = ctk.CTkButton(
    janela, text="Sim", fg_color="green", hover_color="darkgreen",
    font=("Arial", tamanho_sim), command=aceitar
)
botao_sim.place(relx=0.4, rely=0.6, anchor="center")

# Botão "Não"
botao_nao = ctk.CTkButton(
    janela, text="Não", fg_color="red", hover_color="darkred",
    font=("Arial", tamanho_nao), command=mover_botao_nao
)
botao_nao.place(relx=0.6, rely=0.6, anchor="center")

# Criar os corações na tela
criar_coracoes()

# Executa a interface
janela.mainloop()
