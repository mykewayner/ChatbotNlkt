pairs = [
    # Cumprimentos e despedidas
    [r"(oi|olá|ei)", ["Olá, Pronto pra explorar o mundo de Terraria?"]],
    [r"sair|tchau|até logo", ["Boa sorte nas suas aventuras!"]],
    
    # Início do jogo
    [r"como começar( o jogo)?", ["Comece cortando madeira, crie uma casa e equipe-se antes que a noite chegue!"]],
    [r"como faço uma casa", ["Construa uma estrutura com paredes, fundo e uma porta. Coloque uma tocha, mesa e cadeira!"]],
    [r"o que fazer no começo", ["Explore, colete recursos, e construa abrigo antes da noite. Depois, procure minérios!"]],
    
    # Equipamentos
    [r"qual melhor armadura( para iniciantes)?", ["A armadura de Cobre ou de Madeira serve pra começar. Depois, busque a de Tungstênio ou Ouro."]],
    [r"qual a melhor arma( para começar)?", ["O arco de madeira com flechas flamejantes é uma boa. Depois procure a Espada de Tungstênio!"]],
    [r"como fazer uma espada de (.*)", [r"Você pode fazer uma espada de %1 usando uma forja e os minérios correspondentes."]],

    # Biomas
    [r"quais biomas existem", ["Existem vários: Floresta, Deserto, Corruption, Crimson, Selva, Hallow, Inferno e mais."]],
    [r"como sobreviver no bioma (.*)", [r"No bioma %1, leve boas armas, armadura e poções. E prepare-se para inimigos específicos."]],
    
    # Bosses
    [r"como invocar o olho de cthulhu", ["Use uma 'Lente' para criar um 'Olho Suspeito' no Altar Demoníaco à noite."]],
    [r"como invocar o rei slime", ["Derrote 150 slimes durante uma Slime Rain ou use uma Coroa de Slime."]],
    [r"qual o primeiro boss", ["Normalmente o primeiro boss é o Olho de Cthulhu. Mas você pode tentar o Rei Slime antes."]],
    [r"qual boss vem depois do (.*)", [r"Depois do %1, os próximos são geralmente o Cérebro de Cthulhu ou o Devorador de Mundos."]],
    [r"qual o boss mais difícil", ["O Moon Lord é geralmente considerado o boss mais difícil do Terraria vanilla."]],
    [r"como invocar o cérebro de cthulhu", ["Quebre 3 Corações Carmesins no bioma Crimson ou use uma Espinha Sangrenta no Altar Carmesim."]],
    [r"como invocar o devorador de mundos", ["Quebre 3 Orbes das Sombras no bioma Corruption ou use uma Isca de Verme no Altar Demoníaco."]],
    [r"como invocar a abelha rainha", ["Quebre uma Colmeia de Abelha na Selva ou use uma Abelha Larval."]],
    [r"como invocar o esqueletron", ["Fale com o NPC Velho na Dungeon à noite e aceite a maldição."]],
    [r"como invocar a Parede de carne", ["Jogue uma Boneca Vodu do Guia na lava no bioma Inferno."]],
    [r"como invocar os gêmeos", ["Use um Olho Mecânico à noite."]],
    [r"como invocar o destruidor", ["Use um Verme Mecânico à noite."]],
    [r"como invocar o esqueletron prime", ["Use uma Caveira Mecânica à noite."]],
    [r"como invocar o plantera", ["Quebre uma Bulbo de Plantera encontrada na Selva subterrânea após derrotar os bosses mecânicos."]],
    [r"como invocar o golem", ["Use uma Lihzahrd Power Cell no Altar de Lihzahrd no Templo da Selva."]],
    [r"como invocar o duque fishron", ["Pesque com uma Trufa de Minhoca no bioma Oceano."]],
    [r"como invocar o imperador da luz", ["Ataque uma Borboleta Prismática no bioma Hallow durante o dia."]],
    [r"como invocar o moon lord", ["Derrote o Cultista Lunático e complete os eventos dos Pilares Celestiais."]],
    
    # NPCs
    [r"como conseguir o npc (.*)", [r"Para conseguir o NPC %1, você precisa cumprir certas condições. Consulte a wiki ou me diga mais sobre ele."]],
    [r"quantos npcs existem", ["Existem mais de 25 NPCs, incluindo vendedores, curandeiros e até o Papai Noel!"]],
    
    # Modo Expert / Master
    [r"diferença entre modo normal e expert", ["O modo Expert tem inimigos mais fortes, itens exclusivos e mais desafios."]],
    [r"o que muda no master mode", ["No Master Mode, os inimigos são ainda mais fortes e os drops são melhores. Só para os corajosos!"]],
    
    # Eventos e Progressão
    [r"como ativar o hardmode", ["Derrote o boss 'Wall of Flesh' no Inferno para ativar o Hardmode."]],
    [r"o que é hardmode", ["É uma nova fase do jogo com biomas corrompidos, inimigos mais fortes e novos bosses."]],
    [r"como invocar a parede de carne", ["Jogue uma boneca vudu do guia na lava no Inferno para invocar a Wall of Flesh."]],

    # Diversos
    [r"tem modo multiplayer?", ["Sim! Você pode jogar com amigos online ou em LAN, e explorar juntos."]],
    [r"o que são asas", ["As asas te permitem voar por um tempo e evitam dano de queda. Elas são essenciais no Hardmode."]],
    [r"como conseguir asas", ["Derrote bosses no Hardmode, use almas de voo e combine com materiais especiais."]],
    [r"qual melhor asa", ["As melhores são as Solar Wings, Fishron Wings ou Nebula Wings — depende da sua classe."]],
    
    # Genérico
    [r"(.*)", ["Legal! E o que mais você quer saber sobre Terraria?"]],

    # Minérios e crafting
    [r"para que serve o minério de (.*)", [r"O minério de %1 é usado para criar armas, armaduras e ferramentas melhores."]],
    [r"como eu faço uma espada de cobre", ["Para criar uma Espada Curta de Cobre, você precisa de 5 Barras de Cobre. Use uma bigorna de ferro ou chumbo para forjá-la."]],
    [r"como eu faço uma espada de estanho", ["Para criar uma Espada Curta de Estanho, você precisa de 5 Barras de Estanho. Use uma bigorna de ferro ou chumbo para forjá-la."]],
    [r"como eu faço uma espada de madeira", ["Para criar uma Espada de Madeira, você precisa de 7 madeiras. Use uma bancada de trabalho para forjá-la."]],
    [r"como eu faço uma espada de ferro", ["Para criar uma Espada Curta de Ferro, você precisa de 6 Barras de Ferro. Use uma bigorna de ferro ou chumbo para forjá-la."]],
    [r"como eu faço uma espada de prata", ["Para criar uma Espada Curta de Prata, você precisa de 6 Barras de Prata. Use uma bigorna de ferro ou chumbo para forjá-la."]],
    [r"como eu faço uma espada de chumbo", ["Para criar uma Espada Curta de Chumbo, você precisa de 6 Barras de Chumbo. Use uma bigorna de ferro ou chumbo para forjá-la."]],
    [r"como eu faço uma espada de tungstênio", ["Para criar uma Espada Curta de Tungstênio, você precisa de 6 Barras de Tungstênio. Use uma bigorna de ferro ou chumbo para forjá-la."]],
    [r"como eu faço uma espada de ouro", ["Para criar uma Espada Curta de Ouro, você precisa de 6 Barras de Ouro. Use uma bigorna de ferro ou chumbo para forjá-la."]],
    [r"como eu faço uma espada de platina", ["Para criar uma Espada Curta de Platina, você precisa de 6 Barras de Platina. Use uma bigorna de ferro ou chumbo para forjá-la."]],

    [r"como eu faço um arco de madeira", ["Para criar um Arco de Madeira, você precisa de 10 madeiras. Use uma bancada de trabalho para forjá-lo."]],
    [r"como eu faço um arco de cobre", ["Para criar um Arco de Cobre, você precisa de 7 Barras de Cobre. Use uma bigorna de ferro ou chumbo para forjá-lo."]],
    [r"como eu faço um arco de estanho", ["Para criar um Arco de Estanho, você precisa de 7 Barras de Estanho. Use uma bigorna de ferro ou chumbo para forjá-lo."]],
    [r"como eu faço um arco de ferro", ["Para criar um Arco de Ferro, você precisa de 7 Barras de Ferro. Use uma bigorna de ferro ou chumbo para forjá-lo."]],
    [r"como eu faço um arco de prata", ["Para criar um Arco de Prata, você precisa de 7 Barras de Prata. Use uma bigorna de ferro ou chumbo para forjá-lo."]],
    [r"como eu faço um arco de chumbo", ["Para criar um Arco de Chumbo, você precisa de 7 Barras de Chumbo. Use uma bigorna de ferro ou chumbo para forjá-lo."]],
    [r"como eu faço um arco de tungstênio", ["Para criar um Arco de Tungstênio, você precisa de 7 Barras de Tungstênio. Use uma bigorna de ferro ou chumbo para forjá-lo."]],
    [r"como eu faço um arco de ouro", ["Para criar um Arco de Ouro, você precisa de 7 Barras de Ouro. Use uma bigorna de ferro ou chumbo para forjá-lo."]],
    [r"como eu faço um arco de platina", ["Para criar um Arco de Platina, você precisa de 7 Barras de Platina. Use uma bigorna de ferro ou chumbo para forjá-lo."]],

    # Varinhas do Pre-Hardmode
    [r"como conseguir a varinha de faísca", ["A Varinha de Faísca pode ser encontrada em baús de superfície ou em baús dourados no subsolo."]],
    [r"como conseguir a varinha de safira", ["A Varinha de Safira pode ser criada com 10 barras de Prata e 8 Safiras em uma bigorna."]],
    [r"como conseguir a varinha de rubi", ["A Varinha de Rubi pode ser criada com 10 barras de Ouro e 8 Rubis em uma bigorna."]],
    [r"como conseguir a varinha de topázio", ["A Varinha de Topázio pode ser criada com 10 barras de Estanho e 8 Topázios em uma bigorna."]],
    [r"como conseguir a varinha de ametista", ["A Varinha de Ametista pode ser criada com 10 barras de Cobre e 8 Ametistas em uma bigorna."]],
    [r"como conseguir a varinha de esmeralda", ["A Varinha de Esmeralda pode ser criada com 10 barras de Tungstênio e 8 Esmeraldas em uma bigorna."]],
    [r"como conseguir a varinha de diamante", ["A Varinha de Diamante pode ser criada com 10 barras de Platina e 8 Diamantes em uma bigorna."]],

    # Armas de Fogo do Pré-Hardmode
    [r"como conseguir a pistola", ["A Pistola pode ser obtida ao abrir os Baus dourados na Dungeon após derrotar o Esqueletron."]],
    [r"como conseguir o mosquete", ["O Mosquete pode ser encontrado ao quebrar um Orbe das Sombras no bioma Corruption."]],
    [r"como conseguir o minishark", ["O Minishark pode ser comprado do NPC Armeiro por 35 moedas de ouro."]],
    [r"como conseguir a phoenix blaster", ["A Phoenix Blaster pode ser criada ao combinar uma Pistola e 10 Barras de Pedra Infernal em uma Bigorna."]],
    [r"como conseguir o space gun", ["A Space Gun pode ser criada com 20 Meteoritos em uma Bigorna."]],

    # Armas de Invocador do Pré-Hardmode
    [r"como conseguir o cajado da vespa", ["O Cajado da vespa pode ser criado com 14 Cera de Abelhas em uma Bigorna."]],
    [r"como conseguir o cajado de slime", ["O Cajado de Slime tem uma chance muito baixa de ser dropado por Slimes comuns."]],
    [r"como conseguir o cajado do sapo vampiro", ["O Cajado do Sapo Vampiro pode ser obtido ao derrotar Zombie Mermen e Wandering Eye Fish na Lua de Sangue."]],
]   