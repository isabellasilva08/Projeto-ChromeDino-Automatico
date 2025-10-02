# Projeto-ChromeDino-Automatico
echo "# Projeto Dino - Bot para Jogo do Dinossauro do Chrome

Este projeto é um bot simples para o jogo do dinossauro do Google Chrome, que usa \`pyautogui\` para detectar obstáculos na tela e simular a tecla espaço para pular.

## Funcionalidades

- Detecta diferentes obstáculos (cactos) na tela.
- Pressiona a tecla espaço para pular quando um obstáculo está próximo.
- Usa reconhecimento de imagens para encontrar o dinossauro e os obstáculos.

## Estrutura do Projeto

\`\`\`
modulo2/
├── projetodino/
│   ├── dino.png          # Imagem do dinossauro para reconhecimento
│   ├── img/              # Pasta com imagens dos obstáculos (cactos)
│   └── main.py           # Script principal do bot
\`\`\`

## Como usar

1. Instale as dependências:

\`\`\`bash
pip install pyautogui opencv-python
\`\`\`

2. Ajuste as imagens na pasta \`img\` com os obstáculos que deseja detectar.

3. Execute o script:

\`\`\`bash
python main.py
\`\`\`

## Próximos passos (TODO)

- Identificar pterodáctilo (novo tipo de obstáculo).
- Detectar o modo noturno do jogo (alteração do fundo).
- Melhorar a lógica de detecção para evitar falsos positivos.
- Criar documentação detalhada.

## Observações

- O script usa \`try/except\` para lidar com imagens que não são encontradas na tela.
- Ajuste a confiança do \`locateOnScreen\` conforme sua resolução e qualidade das imagens.
" > README.md
