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
├── Assets/                 # Pasta principal de assets do Unity
│   ├── Scenes/             # Cenas do jogo (fases, menus)
│   ├── Scripts/            # Scripts em C# (lógica do jogo)
│   │   ├── Main.cs         # Inicialização e loop principal
│   │   ├── Config.cs       # Configurações gerais
│   │   ├── Game.cs         # Controle das fases e lógica geral
│   │   ├── Player.cs       # Comportamento do Jojo
│   │   ├── Character.cs    # Comportamento de aliados e inimigos
│   │   ├── Battle.cs       # Lógica de combate
│   │   └── UI.cs           # Interface do usuário (menus, HUD)
│   ├── Sprites/            # Sprites dos personagens e cenários
│   ├── Audio/              # Efeitos sonoros e trilhas
│   └── Prefabs/            # Prefabs de personagens, inimigos e objetos
│
├── ProjectSettings/        # Configurações do projeto Unity (não editar manualmente)
├── Packages/               # Pacotes e dependências do Unity
│
├── Data/                   # Dados do jogo (fases e diálogos)
│   ├── Stages/             # Configuração de cada fase (JSON, ScriptableObjects, etc.)
│   └── Dialogs/            # Diálogos dos personagens
│
├── Utils/                  # Funções auxiliares
│   └── Helpers.cs          # Carregamento de assets, utilitários, etc.
│
├── .gitignore              # Ignora Library, Temp, Build e arquivos do VS
└── README.md               # Documentação do projeto

```

### 2.3 Enredo Completo

No universo de **Jojo e o Campus do Caos**, o IFRN foi dominado por uma iniciativa autoritária da reitoria, que implantou um sistema de controle mental em todos os servidores com a promessa de atingir “eficiência absoluta” e “engajamento total”. A medida, porém, transformou os professores e técnicos administrativos em versões robotizadas e hostis, incapazes de pensar por si mesmos, obedecendo cegamente às ordens superiores.

Jojo, o único que escapou dessa dominação graças a uma falha no sistema de sincronização neural, torna-se a última esperança do campus. Ao perceber o que ocorreu com seus colegas, ele decide enfrentá-los — não por ódio, mas com o desejo sincero de libertá-los.

Sua jornada o leva por diversos setores do IFRN, onde cada fase representa um ambiente específico (sala de aula, biblioteca, laboratório, setor administrativo, etc.) e coloca Jojo contra um servidor sob controle. A cada vitória, o inimigo derrotado recobra a consciência, reconhece a manipulação e junta-se à resistência ao lado de Jojo.

Esses aliados podem ser usados nas próximas fases, permitindo ao jogador alternar entre personagens ou delegar combates a eles. Isso cria uma progressão estratégica e emocional, pois cada conquista representa uma mente liberta.

O objetivo final é chegar até o núcleo do sistema — a reitoria — e enfrentar os responsáveis diretos pela manipulação. Somente ao derrotá-los Jojo poderá destruir a fonte do controle mental e libertar definitivamente o IFRN do caos, devolvendo a autonomia e a consciência a toda a comunidade escolar.

3. Etapas de Entrega (Cronograma Detalhado)

Etapa 1: Protótipo Inicial (Semanas 1–4)
Configuração do ambiente (Unity 2022.3 LTS+, Visual Studio com suporte a C#).
Estrutura básica do projeto (pastas Assets, Data, Scripts, Utils, etc).
Cena inicial com menu e opção "Iniciar Jogo".
Sistema de build básico funcionando (modo Play no Unity).

Etapa 2: Sistema de Combate (Semanas 5–8)
Implementação da movimentação do personagem principal.
Implementação básica do sistema de batalha (ataques simples, barras de vida).
Colisões entre personagens usando Unity Colliders.
IA simples de oponente com comportamento fixo.

Etapa 3: Fases e Progressão (Semanas 9–12)
Adição de múltiplas cenas/fases com transições utilizando SceneManager.
Implementação da lógica de desbloqueio de aliados.
Sistema de troca de personagens (aliado substituindo Jojo).
HUD mostrando nome do inimigo, vida, personagem ativo, usando UI Canvas do Unity.

Etapa 4: Polimento Visual e Sonoro (Semanas 13–16)
Inserção de sprites próprios para personagens, cenários e ataques.
Efeitos sonoros e trilhas para batalhas e menus, usando AudioSource e AudioClip.
Tela de vitória e tela de game over implementadas como cenas ou overlays de UI.
Diálogos iniciais e finais para cada fase.

Etapa 5: Testes e Entrega Final (Semanas 17–18)
Testes com jogadores (colegas de classe).
Correções de bugs e ajustes de equilíbrio.
Documentação final (README + comentários de código nos scripts C#).

4. Requisitos Técnicos

4.1 Linguagem e Ferramentas
Unity 2022.3 LTS+
C# 10+ (via Visual Studio ou VS Code com suporte a Unity)

4.2 Pacotes e dependências
Unity Package Manager: 2D, Input System, UI Toolkit

4.3 Plataforma de execução
Compatível com Windows, Linux e MacOS via build do Unity.

4.4 Recursos audiovisuais

Sprites: desenvolvidos em pixel art pela própria equipe.
Cenários: inspirados nas salas e ambientes do IFRN.
Trilha sonora e efeitos sonoros: adicionados como AudioClip e gerenciados via AudioSourc
