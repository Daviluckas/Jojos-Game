# Jojo e o Campus do Caos

## 1. Resumo e Proposta do Jogo

**Jojo e o Campus do Caos** é um jogo de luta 2D faseado, desenvolvido com Python e Pygame, onde o protagonista, Jojo, é o único funcionário do IFRN que escapou de um controle mental imposto pela reitoria. Com o objetivo de maximizar a produtividade do campus, a reitoria implementou um sistema de manipulação mental que transformou professores e colegas em oponentes agressivos e robotizados.

Ao longo do jogo, Jojo enfrentará cada um desses colegas e professores em batalhas individuais. Ao derrotá-los, os adversários recobram a consciência e passam a se unir a ele, podendo substituí-lo em batalhas futuras ou lutar ao seu lado como aliados controlados pela IA. Cada fase representa um setor ou servidor diferente, trazendo diversidade de estilo de luta e ambientações específicas inspiradas no cotidiano do IFRN.

## 2. Descrição do Projeto

O projeto tem como foco principal o desenvolvimento de um jogo de luta em que o jogador enfrenta inimigos um a um em fases distintas, desbloqueando aliados conforme avança. A narrativa gira em torno de Jojo, que precisa libertar o campus do caos instaurado pela reitoria.

### 2.1 Principais Funcionalidades

* Sistema de combate 1v1 com movimentação lateral.
* Aliados desbloqueáveis que podem ser usados nas fases seguintes.
* IA básica para inimigos e aliados.
* HUD com informações de vida e personagem ativo.
* Transições entre fases com diálogos e ambientações distintas.
* Sistema de substituição de personagem (troca entre Jojo e aliados).
* Sons e sprites personalizados baseados no universo do IFRN.

### 2.2 Estrutura de Pastas Simplificada

```bash
jojo-campus-do-caos/
├── assets/             # Imagens, sprites e sons
│   ├── images/         # Sprites dos personagens e cenários
│   └── sounds/         # Efeitos sonoros e trilhas
│
├── data/               # Fases e diálogos
│   ├── stages/         # Configuração de cada fase
│   └── dialogs/        # Diálogos dos personagens
│
├── src/                # Código-fonte do jogo
│   ├── main.py         # Inicialização e loop principal
│   ├── config.py       # Configurações gerais
│   ├── game.py         # Controle das fases e lógica geral
│   ├── player.py       # Comportamento do Jojo
│   ├── character.py    # Comportamento de aliados e inimigos
│   ├── battle.py       # Lógica de combate
│   └── ui.py           # Interface do usuário (menus, HUD)
│
├── utils/              # Funções auxiliares
│   └── helpers.py      # Carregamento de assets, etc.
```

### 2.3 Enredo Completo

No universo de **Jojo e o Campus do Caos**, o IFRN foi dominado por uma iniciativa autoritária da reitoria, que implantou um sistema de controle mental em todos os servidores com a promessa de atingir “eficiência absoluta” e “engajamento total”. A medida, porém, transformou os professores e técnicos administrativos em versões robotizadas e hostis, incapazes de pensar por si mesmos, obedecendo cegamente às ordens superiores.

Jojo, o único que escapou dessa dominação graças a uma falha no sistema de sincronização neural, torna-se a última esperança do campus. Ao perceber o que ocorreu com seus colegas, ele decide enfrentá-los — não por ódio, mas com o desejo sincero de libertá-los.

Sua jornada o leva por diversos setores do IFRN, onde cada fase representa um ambiente específico (sala de aula, biblioteca, laboratório, setor administrativo, etc.) e coloca Jojo contra um servidor sob controle. A cada vitória, o inimigo derrotado recobra a consciência, reconhece a manipulação e junta-se à resistência ao lado de Jojo.

Esses aliados podem ser usados nas próximas fases, permitindo ao jogador alternar entre personagens ou delegar combates a eles. Isso cria uma progressão estratégica e emocional, pois cada conquista representa uma mente liberta.

O objetivo final é chegar até o núcleo do sistema — a reitoria — e enfrentar os responsáveis diretos pela manipulação. Somente ao derrotá-los Jojo poderá destruir a fonte do controle mental e libertar definitivamente o IFRN do caos, devolvendo a autonomia e a consciência a toda a comunidade escolar.

## 3. Etapas de Entrega (Cronograma Detalhado)

### Etapa 1: Protótipo Inicial (Semanas 1–4)

* Configuração do ambiente (Python 3.10+, Pygame 2.5+).
* Estrutura básica do projeto (pasta `src`, `assets`, `data`, etc).
* Loop principal de jogo funcionando.
* Tela inicial com opção "Iniciar Jogo".

### Etapa 2: Sistema de Combate (Semanas 5–8)

* Implementação da movimentação do personagem.
* Implementação básica do sistema de batalha (ataques simples, barras de vida).
* Colisões entre personagens.
* IA simples de oponente com comportamento fixo.

### Etapa 3: Fases e Progressão (Semanas 9–12)

* Adição de múltiplas fases com transições.
* Implementação da lógica de desbloqueio de aliados.
* Sistema de troca de personagens (aliado substituindo Jojo).
* HUD mostrando nome do inimigo, vida, personagem ativo.

### Etapa 4: Polimento Visual e Sonoro (Semanas 13–16)

* Inserção de sprites próprios para personagens, cenários e ataques.
* Efeitos sonoros e trilhas para batalhas e menus.
* Tela de vitória e tela de game over.
* Diálogos iniciais e finais para cada fase.

### Etapa 5: Testes e Entrega Final (Semanas 17–18)

* Testes com jogadores (colegas de classe).
* Correções de bugs e ajustes de equilíbrio.
* Documentação final (README + comentários de código).

## 4. Requisitos Técnicos

### 4.1 Linguagem e Bibliotecas

* **Python 3.10+**
* **Pygame 2.5+**

### 4.2 Arquivo de dependências (requirements.txt)

```txt
pygame==2.5.2
```

### 4.3 Plataforma de execução

* Compatível com Windows, Linux e MacOS com Python instalado.

### 4.4 Recursos audiovisuais

* **Sprites**: desenvolvidos em pixel art pela própria equipe.
* **Cenários**: inspirados nas salas e ambientes do IFRN.
* **Trilha sonora**: composta ou selecionada com base em temas escolares e eletrônicos.
