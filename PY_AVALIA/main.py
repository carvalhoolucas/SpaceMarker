import pygame
from tkinter import Tk, simpledialog
import json
pygame.init()
fundo = pygame.image.load("space.png")
tamanho = 1100, 700
tela = pygame.display.set_mode((tamanho))
pygame.display.set_caption("Space Marker")
fundo = pygame.image.load("space.png")
def obter_nome_estrela(posicao_mouse):
    tela = Tk()
    tela.withdraw()
    NameStar = simpledialog.askstring("Nome da Estrela", "Digite o nome da estrela:")
    tela.destroy()
    return NameStar
def SaveTags():
    try:
        with open("tags.json", "w") as arquivo:
            json.dump(estrelas_marcadas, arquivo)
        print("Tags successfully saved!")
    except Exception as e:
        print("Error saving tags!", str(e))
def carregar_marcacoes():
    global estrelas_marcadas
    try:
        with open("tags.json", "r") as arquivo:
            estrelas_marcadas = json.load(arquivo)
    except FileNotFoundError:
        estrelas_marcadas = []
    except Exception as e:
        print("Erro ao carregar as marcações:", str(e))
def excluir_marcacoes():
    global estrelas_marcadas
    estrelas_marcadas = []
estrelas_marcadas = []
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            SaveTags() 
            rodando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1: 
                posicao_mouse = pygame.mouse.get_pos()
                nome_estrela = obter_nome_estrela(posicao_mouse)
                estrela = (nome_estrela if nome_estrela else "Desconhecido", posicao_mouse)
                estrelas_marcadas.append(estrela)
                print("Nome da estrela:", estrela[0])
                print("Posição do clique:", estrela[1])
    tela.fill((0, 0, 0))  
    tela.blit(fundo, (0, 0))
    for i, estrela in enumerate(estrelas_marcadas):
        pygame.draw.circle(tela, (255,255,255), estrela[1], 2)  
        texto = f"{estrela[0]} ({estrela[1][0]}, {estrela[1][1]})" 
        fonte = pygame.font.SysFont(None, 20)
        texto_renderizado = fonte.render(texto, True, (255, 255, 255))
        tela.blit(texto_renderizado, (estrela[1][0], estrela[1][1] + 25))
        if i > 0:
            pygame.draw.line(tela, (255, 255, 255), estrelas_marcadas[i-1][1], estrela[1], 1)
        if i > 0:
            estrela_anterior = estrelas_marcadas[i-1]
            pygame.draw.line(tela, (255, 255, 255), estrela_anterior[1], estrela[1], 1)
            distancia_x = abs(estrela_anterior[1][0] - estrela[1][0])
            distancia_y = abs(estrela_anterior[1][1] - estrela[1][1])
            soma_distancias = distancia_x + distancia_y
            texto_distancia = f"{soma_distancias}"
            texto_distancia_renderizado = fonte.render(texto_distancia, True, (255, 255, 255))
            tela.blit(texto_distancia_renderizado, ((estrela_anterior[1][0] + estrela[1][0]) // 2, (estrela_anterior[1][1] + estrela[1][1]) // 2))        
    for estrela in estrelas_marcadas:
        pygame.draw.circle(tela, (255,255,255), estrela[1], 2) 
        texto = estrela[0]
        fonte = pygame.font.SysFont(None, 20)
        texto_renderizado = fonte.render(texto, True, (255, 255, 255))
    teclas_pressionadas = pygame.key.get_pressed()
    if teclas_pressionadas[pygame.K_F10]:
        SaveTags()
        print("Saved Tags.")
    if teclas_pressionadas[pygame.K_F11]:
        carregar_marcacoes()
        print("Load Tags.")

    pygame.display.flip()

pygame.quit()