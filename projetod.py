import pyautogui as auto
import os

auto.useImageNotFoundException()

CAMINHO_IMAGENS = '.\\modulo2\\projetodino\\img'
caminho_dino = ".\\modulo2\\projetodino\\dino.png"     

lista_imagens = os.listdir(CAMINHO_IMAGENS)  
      

while True:
    #Pecorre as imagens da pasta img
    for imagem_cacto in lista_imagens:
        #Pega o caminho dessas imagens uma a uma
        caminho_imagem_cacto = os.path.join(CAMINHO_IMAGENS,imagem_cacto)
        #Se a imagem não é encontrada na tela, o pyautogui emite um erro
        #Por isso utilizamos o bloco try
        try:
            posicao_dino = auto.locateOnScreen(caminho_dino, confidence=0.6)     
            posicao_cacto = auto.locateOnScreen(caminho_imagem_cacto, confidence=0.8)
        except auto.ImageNotFoundException:
            posicao_cacto = None
            posicao_dino = None 
        #Se não houve erro (uma das imagens foi encontrada)
        #Falamos qual imagem foi encontrada e apertamos a tecla espaço.
        else:
            px_dino =  posicao_dino.left
            px_cacto = posicao_cacto.left

            print(imagem_cacto)

            print(px_cacto-px_dino)

            if px_cacto - px_dino >= 300:
                auto.keyDown('space')
            elif px_cacto - px_dino <= 100:
                auto.keyDown('space')

#TO DO:
# - Identificar piterodactilo
# - Identificar mapa a noite