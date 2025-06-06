# Documentação do Projeto: Jojo e o Campus do Caos

## 1. Visão Geral

#### Tecnologia Utilizada: Python 3.10+ + Pygame 2.5+

#### Descrição: Jojo e o Campus do Caos é um jogo 2D em estilo pixel art desenvolvido com Pygame. O jogador assume o papel de Jojo, um professor de informática do IFRN – Campus Caicó, em uma jornada cheia de obstáculos para sair da sala dos servidores e chegar à sua sala de aula no menor tempo possível.

#### Objetivo: Desenvolver um jogo com narrativa cômica e interativa que combine exploração, minigames e tomada de decisão. A estrutura do código é modular, com possibilidade de expansão para novos níveis, minigames e eventos.

## 2. Descrição Detalhada do Projeto

### Jojo e o Campus do Caos?

Jojo e o Campus do Caos é um jogo eletrônico 2D em estilo pixel art, ambientado no IFRN – Campus Caicó. Inspirado no cotidiano de um professor da área de informática, o jogador assume o papel de Jojo, um docente que precisa cumprir sua missão diária: sair da sala dos servidores e chegar até sua sala de aula o mais rápido possível. No entanto, sua jornada é constantemente interrompida por diversos desafios que retratam, de forma cômica e interativa, situações comuns do ambiente escolar.

O jogo mistura elementos de aventura, minigames e tomada de decisão, transformando o caminho do professor em uma verdadeira missão cheia de imprevistos.

Referência real: O projeto utiliza como base referências locais do IFRN e elementos caricatos da vivência escolar, criando uma experiência imersiva e divertida tanto para estudantes quanto para servidores.

### 2.1 Funcionalidades Principais

+ #### Motor do Jogo:
  + Início do cronômetro assim que o jogador sai da sala dos servidores.
  + Sistema de movimentação em um mapa com múltiplos caminhos.
  + Detecção de colisões com NPCs e obstáculos interativos.
  + Gatilhos de eventos personalizados (minigames, diálogos, escolhas).
  + Sistema de decisões com impacto direto no tempo total.


+ #### Obstáculos e Dinâmicas de Jogo:
  + Colegas de Trabalho:
    + Não causam penalidades diretas no tempo.
    + Ao colidir ou interagir, iniciam longos diálogos que atrasam o progresso do jogador.
    + Após o diálogo, o jogador retoma o movimento normalmente.

  + Alunos Pedindo Revisão de Prova:
    + Acionam um minigame no qual o jogador precisa analisar uma "prova digital".
    + O desafio consiste em somar as notas, avaliar os argumentos e julgar se a revisão é válida.
    + Respostas erradas ou demoradas adicionam segundos ao cronômetro.


  + Problemas de Conduta:
    + Eventos aleatórios nos quais o jogador deve tomar uma decisão rápida (ex.: advertir ou ignorar).
    + As escolhas influenciam o tempo.


  + Manifestações Estudantis (GESS):
    + Grupos de alunos bloqueando corredores, impossibilitando a passagem.
    + O jogador precisa encontrar rotas alternativas para continuar sua jornada.

+ #### Interface Gráfica:
  + Visual inspirado em pixel art com elementos estilizados do IFRN.
  + HUD com cronômetro em tempo real, indicadores de tempo perdido e status dos eventos.
  + Telas de início, pausa e fim de jogo com menus interativos.
  + Sistema de diálogos com múltiplas linhas por personagem.

+ #### Extras:
  + Trilha sonora ambiente leve e envolvente, mantendo o ritmo descontraído da narrativa.
  + Efeitos sonoros únicos para interações com NPCs, conclusão de minigames e eventos especiais.
  + Modularidade para criação de novos obstáculos, desafios e rotas alternativas em atualizações futuras.
  + Possível integração com sistema de high score para competições de tempo entre jogadores.

 + ### 2.2 Arquitetura do Código
   ```plaintext
jojo-campus-do-caos/
├── assets/                 # Recursos visuais e sonoros do jogo
│   ├── images/             # Imagens e sprites em pixel art
│   │   ├── player/         # Sprites do personagem Jojo
│   │   ├── npcs/           # Sprites dos NPCs (colegas, alunos, GESS)
│   │   ├── tilesets/       # Tilesets para construção do mapa/corredores
│   │   └── ui/             # Elementos gráficos da interface (HUD, menus)
│   └── sounds/             # Sons e músicas
│       ├── bgm/            # Trilha sonora ambiente
│       └── sfx/            # Efeitos sonoros (interações, minigames)
│
├── data/                   # Dados estruturados para o jogo
│   ├── levels/             # Arquivos de configuração dos níveis e mapas
│   └── dialogs/            # Diálogos dos NPCs e textos do jogo em JSON ou TXT
│
├── core/                   # Núcleo do jogo e lógica principal
│   ├── main.py             # Ponto de entrada e inicialização do jogo
│   ├── settings.py         # Configurações globais (resolução, FPS, cores)
│   ├── game.py             # Loop principal e controle de estados do jogo
│   └── state_manager.py    # Gerenciamento das transições entre telas e estados
│
├── engine/                 # Sistemas básicos que suportam o funcionamento
│   ├── map_loader.py       # Carregamento e renderização do mapa e cenário
│   ├── event_trigger.py    # Detecção e ativação de eventos e minigames
│   ├── timer.py            # Cronômetro do jogo e controle de penalidades
│   ├── collision.py        # Detecção de colisões entre personagem e objetos
│   └── dialogue_box.py     # Sistema de diálogos multilinha com NPCs
│
├── entities/               # Definição e comportamento dos personagens e objetos
│   ├── player.py           # Classe do Jojo (movimentação, interação)
│   ├── npc.py              # Lógica dos NPCs (colegas, alunos, GESS)
│   ├── obstacle.py         # Obstáculos no mapa (fixos ou móveis)
│   └── minigame_manager.py # Gerencia minigames ativados durante o jogo
│
├── minigames/              # Módulos de minigames específicos
│   ├── prova_revisao.py    # Minigame de revisão de prova
│   ├── conduta_aluno.py    # Minigame de decisão sobre condutas
│   └── manifestacao_gess.py# Minigame das manifestações estudantis (bloqueios)
│
├── ui/                     # Interface gráfica e gerenciamento de telas
│   ├── hud.py              # HUD: cronômetro, status e indicadores
│   ├── menu.py             # Menus principais, pause e opções
│   └── screens.py          # Telas de início, pausa e fim de jogo
│
├── utils/                  # Utilitários e funções auxiliares
│   ├── helpers.py          # Funções genéricas (carregar assets, formatação)
│   └── constants.py        # Constantes globais (cores, caminhos, teclas)
```

