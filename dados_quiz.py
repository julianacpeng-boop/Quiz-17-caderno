# -*- coding: utf-8 -*-
# Juh Quiz 17 — lote novo com 15 temas e 45 perguntas.
# Legendas de vídeo: campo legenda em cada questão e dicionário LEGENDAS.
# Imagens transparentes: pasta imagens_perguntas, arquivo temaNN_perguntaNN.png.

QUIZZES = {
    "Português: ortografia e uso de G, J, S, SS e Ç": [
        {
            "pergunta": "Qual palavra está escrita corretamente?",
            "alternativas": [
                "girafa",
                "jirafa",
                "girrafa"
            ],
            "correta": 0,
            "imagem": "tema01_pergunta01.png",
            "imagem_path": "imagens_perguntas/tema01_pergunta01.png",
            "legenda": "CAPA_SEGUNDOS=2\nTeste sua atenção neste desafio de ortografia!\n#JuhQuiz #Português #Ortografia #Quiz"
        },
        {
            "pergunta": "Qual palavra está escrita corretamente?",
            "alternativas": [
                "excessão",
                "exceção",
                "esceção"
            ],
            "correta": 1,
            "imagem": "tema01_pergunta02.png",
            "imagem_path": "imagens_perguntas/tema01_pergunta02.png",
            "legenda": "CAPA_SEGUNDOS=2\nTeste sua atenção neste desafio de ortografia!\n#JuhQuiz #Português #Ortografia #Quiz"
        },
        {
            "pergunta": "Qual palavra está escrita corretamente para indicar precipitação de água das nuvens?",
            "alternativas": [
                "xuva",
                "chubva",
                "chuva"
            ],
            "correta": 2,
            "imagem": "tema01_pergunta03.png",
            "imagem_path": "imagens_perguntas/tema01_pergunta03.png",
            "legenda": "CAPA_SEGUNDOS=2\nTeste sua atenção neste desafio de ortografia!\n#JuhQuiz #Português #Ortografia #Quiz"
        }
    ],
    "Matemática: equações do primeiro grau": [
        {
            "pergunta": "Na equação 3x + 5 = 20, qual é o valor de x?",
            "alternativas": [
                "5",
                "6",
                "7"
            ],
            "correta": 0,
            "imagem": "tema02_pergunta01.png",
            "imagem_path": "imagens_perguntas/tema02_pergunta01.png",
            "legenda": "CAPA_SEGUNDOS=2\nResolva três equações do primeiro grau no Juh Quiz!\n#JuhQuiz #Matemática #Equações #Quiz"
        },
        {
            "pergunta": "Qual valor de x resolve 2(x − 3) = 10?",
            "alternativas": [
                "6",
                "8",
                "10"
            ],
            "correta": 1,
            "imagem": "tema02_pergunta02.png",
            "imagem_path": "imagens_perguntas/tema02_pergunta02.png",
            "legenda": "CAPA_SEGUNDOS=2\nResolva três equações do primeiro grau no Juh Quiz!\n#JuhQuiz #Matemática #Equações #Quiz"
        },
        {
            "pergunta": "Se 5x = 35, quanto vale x?",
            "alternativas": [
                "5",
                "6",
                "7"
            ],
            "correta": 2,
            "imagem": "tema02_pergunta03.png",
            "imagem_path": "imagens_perguntas/tema02_pergunta03.png",
            "legenda": "CAPA_SEGUNDOS=2\nResolva três equações do primeiro grau no Juh Quiz!\n#JuhQuiz #Matemática #Equações #Quiz"
        }
    ],
    "Biologia: microrganismos e suas funções": [
        {
            "pergunta": "Qual microrganismo é usado para ajudar a massa do pão a crescer?",
            "alternativas": [
                "Levedura",
                "Vírus da gripe",
                "Protozoário da malária"
            ],
            "correta": 0,
            "imagem": "tema03_pergunta01.png",
            "imagem_path": "imagens_perguntas/tema03_pergunta01.png",
            "legenda": "CAPA_SEGUNDOS=2\nDescubra o que você sabe sobre microrganismos!\n#JuhQuiz #Biologia #Microrganismos #Quiz"
        },
        {
            "pergunta": "Qual grupo inclui muitos seres que decompõem matéria orgânica no ambiente?",
            "alternativas": [
                "Borboletas",
                "Bactérias",
                "Peixes"
            ],
            "correta": 1,
            "imagem": "tema03_pergunta02.png",
            "imagem_path": "imagens_perguntas/tema03_pergunta02.png",
            "legenda": "CAPA_SEGUNDOS=2\nDescubra o que você sabe sobre microrganismos!\n#JuhQuiz #Biologia #Microrganismos #Quiz"
        },
        {
            "pergunta": "Os vírus precisam de que condição para se multiplicar?",
            "alternativas": [
                "De luz do Sol diretamente",
                "De água parada",
                "De uma célula hospedeira"
            ],
            "correta": 2,
            "imagem": "tema03_pergunta03.png",
            "imagem_path": "imagens_perguntas/tema03_pergunta03.png",
            "legenda": "CAPA_SEGUNDOS=2\nDescubra o que você sabe sobre microrganismos!\n#JuhQuiz #Biologia #Microrganismos #Quiz"
        }
    ],
    "Química: ácidos, bases e escala de pH": [
        {
            "pergunta": "Em uma escala de pH, uma solução ácida geralmente apresenta valor:",
            "alternativas": [
                "Menor que 7",
                "Igual a 7",
                "Maior que 7"
            ],
            "correta": 0,
            "imagem": "tema04_pergunta01.png",
            "imagem_path": "imagens_perguntas/tema04_pergunta01.png",
            "legenda": "CAPA_SEGUNDOS=2\nDesafio rápido de química: ácidos, bases e pH.\n#JuhQuiz #Química #pH #Quiz"
        },
        {
            "pergunta": "Em condições comuns, qual valor representa uma solução neutra na escala de pH?",
            "alternativas": [
                "5",
                "7",
                "9"
            ],
            "correta": 1,
            "imagem": "tema04_pergunta02.png",
            "imagem_path": "imagens_perguntas/tema04_pergunta02.png",
            "legenda": "CAPA_SEGUNDOS=2\nDesafio rápido de química: ácidos, bases e pH.\n#JuhQuiz #Química #pH #Quiz"
        },
        {
            "pergunta": "Uma solução básica geralmente apresenta pH:",
            "alternativas": [
                "Abaixo de 7",
                "Igual a 7",
                "Acima de 7"
            ],
            "correta": 2,
            "imagem": "tema04_pergunta03.png",
            "imagem_path": "imagens_perguntas/tema04_pergunta03.png",
            "legenda": "CAPA_SEGUNDOS=2\nDesafio rápido de química: ácidos, bases e pH.\n#JuhQuiz #Química #pH #Quiz"
        }
    ],
    "Física: força e leis de Newton": [
        {
            "pergunta": "Qual lei de Newton explica a tendência de um corpo manter seu estado de repouso ou movimento?",
            "alternativas": [
                "Primeira lei",
                "Segunda lei",
                "Terceira lei"
            ],
            "correta": 0,
            "imagem": "tema05_pergunta01.png",
            "imagem_path": "imagens_perguntas/tema05_pergunta01.png",
            "legenda": "CAPA_SEGUNDOS=2\nMostre seus conhecimentos sobre força e as leis de Newton!\n#JuhQuiz #Física #LeisDeNewton #Quiz"
        },
        {
            "pergunta": "A relação entre força resultante, massa e aceleração é expressa por qual lei de Newton?",
            "alternativas": [
                "Primeira lei",
                "Segunda lei",
                "Terceira lei"
            ],
            "correta": 1,
            "imagem": "tema05_pergunta02.png",
            "imagem_path": "imagens_perguntas/tema05_pergunta02.png",
            "legenda": "CAPA_SEGUNDOS=2\nMostre seus conhecimentos sobre força e as leis de Newton!\n#JuhQuiz #Física #LeisDeNewton #Quiz"
        },
        {
            "pergunta": "Quando um corpo exerce uma força sobre outro, surge uma força de mesma intensidade e sentido oposto. Isso corresponde à:",
            "alternativas": [
                "Primeira lei",
                "Segunda lei",
                "Terceira lei"
            ],
            "correta": 2,
            "imagem": "tema05_pergunta03.png",
            "imagem_path": "imagens_perguntas/tema05_pergunta03.png",
            "legenda": "CAPA_SEGUNDOS=2\nMostre seus conhecimentos sobre força e as leis de Newton!\n#JuhQuiz #Física #LeisDeNewton #Quiz"
        }
    ],
    "História: Independência do Brasil e Período Regencial": [
        {
            "pergunta": "Em que ano foi proclamada a Independência do Brasil?",
            "alternativas": [
                "1822",
                "1824",
                "1831"
            ],
            "correta": 0,
            "imagem": "tema06_pergunta01.png",
            "imagem_path": "imagens_perguntas/tema06_pergunta01.png",
            "legenda": "CAPA_SEGUNDOS=2\nRevise a Independência do Brasil e o Período Regencial.\n#JuhQuiz #História #Brasil #Quiz"
        },
        {
            "pergunta": "Qual personagem histórico proclamou a Independência do Brasil?",
            "alternativas": [
                "Dom João VI",
                "Dom Pedro I",
                "José Bonifácio"
            ],
            "correta": 1,
            "imagem": "tema06_pergunta02.png",
            "imagem_path": "imagens_perguntas/tema06_pergunta02.png",
            "legenda": "CAPA_SEGUNDOS=2\nRevise a Independência do Brasil e o Período Regencial.\n#JuhQuiz #História #Brasil #Quiz"
        },
        {
            "pergunta": "O Período Regencial começou após qual acontecimento, em 1831?",
            "alternativas": [
                "A chegada da corte portuguesa",
                "A Proclamação da República",
                "A abdicação de Dom Pedro I"
            ],
            "correta": 2,
            "imagem": "tema06_pergunta03.png",
            "imagem_path": "imagens_perguntas/tema06_pergunta03.png",
            "legenda": "CAPA_SEGUNDOS=2\nRevise a Independência do Brasil e o Período Regencial.\n#JuhQuiz #História #Brasil #Quiz"
        }
    ],
    "Geografia: população, migrações e urbanização": [
        {
            "pergunta": "Como se chama o crescimento da proporção de pessoas que vivem nas cidades?",
            "alternativas": [
                "Urbanização",
                "Erosão",
                "Industrialização rural"
            ],
            "correta": 0,
            "imagem": "tema07_pergunta01.png",
            "imagem_path": "imagens_perguntas/tema07_pergunta01.png",
            "legenda": "CAPA_SEGUNDOS=2\nTrês perguntas sobre população, migrações e cidades.\n#JuhQuiz #Geografia #População #Quiz"
        },
        {
            "pergunta": "A mudança de pessoas de uma região para outra, para morar, é chamada de:",
            "alternativas": [
                "Urbanização",
                "Migração",
                "Vegetação"
            ],
            "correta": 1,
            "imagem": "tema07_pergunta02.png",
            "imagem_path": "imagens_perguntas/tema07_pergunta02.png",
            "legenda": "CAPA_SEGUNDOS=2\nTrês perguntas sobre população, migrações e cidades.\n#JuhQuiz #Geografia #População #Quiz"
        },
        {
            "pergunta": "O crescimento natural da população resulta principalmente da diferença entre:",
            "alternativas": [
                "Imigração e emigração",
                "Área rural e área urbana",
                "Nascimentos e mortes"
            ],
            "correta": 2,
            "imagem": "tema07_pergunta03.png",
            "imagem_path": "imagens_perguntas/tema07_pergunta03.png",
            "legenda": "CAPA_SEGUNDOS=2\nTrês perguntas sobre população, migrações e cidades.\n#JuhQuiz #Geografia #População #Quiz"
        }
    ],
    "Ciências: efeito estufa e mudanças climáticas": [
        {
            "pergunta": "Qual é o papel natural do efeito estufa na atmosfera da Terra?",
            "alternativas": [
                "Reter parte do calor e manter o planeta aquecido",
                "Impedir toda a luz solar de chegar ao solo",
                "Eliminar completamente as nuvens"
            ],
            "correta": 0,
            "imagem": "tema08_pergunta01.png",
            "imagem_path": "imagens_perguntas/tema08_pergunta01.png",
            "legenda": "CAPA_SEGUNDOS=2\nTeste seus conhecimentos sobre efeito estufa e clima.\n#JuhQuiz #Ciências #Clima #Quiz"
        },
        {
            "pergunta": "Qual ação humana contribui para aumentar a concentração de gases de efeito estufa?",
            "alternativas": [
                "Plantar árvores nativas",
                "Queimar combustíveis fósseis",
                "Usar bicicleta em trajetos curtos"
            ],
            "correta": 1,
            "imagem": "tema08_pergunta02.png",
            "imagem_path": "imagens_perguntas/tema08_pergunta02.png",
            "legenda": "CAPA_SEGUNDOS=2\nTeste seus conhecimentos sobre efeito estufa e clima.\n#JuhQuiz #Ciências #Clima #Quiz"
        },
        {
            "pergunta": "Mudanças climáticas se referem a alterações de longo prazo em padrões do:",
            "alternativas": [
                "Relevo de uma rua",
                "Ciclo de vida de uma planta",
                "Clima"
            ],
            "correta": 2,
            "imagem": "tema08_pergunta03.png",
            "imagem_path": "imagens_perguntas/tema08_pergunta03.png",
            "legenda": "CAPA_SEGUNDOS=2\nTeste seus conhecimentos sobre efeito estufa e clima.\n#JuhQuiz #Ciências #Clima #Quiz"
        }
    ],
    "Literatura: narrador, personagens e enredo": [
        {
            "pergunta": "Em uma narrativa, quem conta os acontecimentos é chamado de:",
            "alternativas": [
                "Narrador",
                "Leitor",
                "Ilustrador"
            ],
            "correta": 0,
            "imagem": "tema09_pergunta01.png",
            "imagem_path": "imagens_perguntas/tema09_pergunta01.png",
            "legenda": "CAPA_SEGUNDOS=2\nEntre na narrativa: quem conta, quem vive e o que acontece?\n#JuhQuiz #Literatura #Narrativa #Quiz"
        },
        {
            "pergunta": "Como se chama a personagem que ocupa o papel central de uma história?",
            "alternativas": [
                "Figurante",
                "Protagonista",
                "Autor"
            ],
            "correta": 1,
            "imagem": "tema09_pergunta02.png",
            "imagem_path": "imagens_perguntas/tema09_pergunta02.png",
            "legenda": "CAPA_SEGUNDOS=2\nEntre na narrativa: quem conta, quem vive e o que acontece?\n#JuhQuiz #Literatura #Narrativa #Quiz"
        },
        {
            "pergunta": "A sequência de acontecimentos que compõe uma narrativa forma o:",
            "alternativas": [
                "Vocabulário",
                "Cenário",
                "Enredo"
            ],
            "correta": 2,
            "imagem": "tema09_pergunta03.png",
            "imagem_path": "imagens_perguntas/tema09_pergunta03.png",
            "legenda": "CAPA_SEGUNDOS=2\nEntre na narrativa: quem conta, quem vive e o que acontece?\n#JuhQuiz #Literatura #Narrativa #Quiz"
        }
    ],
    "Inglês: dias da semana, meses e horas": [
        {
            "pergunta": "Qual dia da semana vem depois de Tuesday?",
            "alternativas": [
                "Wednesday",
                "Monday",
                "Friday"
            ],
            "correta": 0,
            "imagem": "tema10_pergunta01.png",
            "imagem_path": "imagens_perguntas/tema10_pergunta01.png",
            "legenda": "CAPA_SEGUNDOS=2\nPratique dias, meses e horas em inglês!\n#JuhQuiz #Inglês #Vocabulário #Quiz"
        },
        {
            "pergunta": "Qual palavra em inglês significa “janeiro”?",
            "alternativas": [
                "June",
                "January",
                "July"
            ],
            "correta": 1,
            "imagem": "tema10_pergunta02.png",
            "imagem_path": "imagens_perguntas/tema10_pergunta02.png",
            "legenda": "CAPA_SEGUNDOS=2\nPratique dias, meses e horas em inglês!\n#JuhQuiz #Inglês #Vocabulário #Quiz"
        },
        {
            "pergunta": "Qual pergunta em inglês é usada para perguntar as horas?",
            "alternativas": [
                "How are you?",
                "Where do you live?",
                "What time is it?"
            ],
            "correta": 2,
            "imagem": "tema10_pergunta03.png",
            "imagem_path": "imagens_perguntas/tema10_pergunta03.png",
            "legenda": "CAPA_SEGUNDOS=2\nPratique dias, meses e horas em inglês!\n#JuhQuiz #Inglês #Vocabulário #Quiz"
        }
    ],
    "Artes: escultura e formas tridimensionais": [
        {
            "pergunta": "Qual característica distingue uma escultura de um desenho plano?",
            "alternativas": [
                "Ela ocupa espaço em três dimensões",
                "Ela precisa sempre ser feita de papel",
                "Ela só pode usar uma cor"
            ],
            "correta": 0,
            "imagem": "tema11_pergunta01.png",
            "imagem_path": "imagens_perguntas/tema11_pergunta01.png",
            "legenda": "CAPA_SEGUNDOS=2\nExplore escultura e formas tridimensionais neste desafio!\n#JuhQuiz #Artes #Escultura #Quiz"
        },
        {
            "pergunta": "Qual técnica consiste em dar forma a um material maleável, como argila?",
            "alternativas": [
                "Gravura",
                "Modelagem",
                "Colagem digital"
            ],
            "correta": 1,
            "imagem": "tema11_pergunta02.png",
            "imagem_path": "imagens_perguntas/tema11_pergunta02.png",
            "legenda": "CAPA_SEGUNDOS=2\nExplore escultura e formas tridimensionais neste desafio!\n#JuhQuiz #Artes #Escultura #Quiz"
        },
        {
            "pergunta": "Uma escultura pode ser observada por diferentes ângulos porque possui:",
            "alternativas": [
                "Somente comprimento",
                "Apenas uma superfície plana",
                "Volume"
            ],
            "correta": 2,
            "imagem": "tema11_pergunta03.png",
            "imagem_path": "imagens_perguntas/tema11_pergunta03.png",
            "legenda": "CAPA_SEGUNDOS=2\nExplore escultura e formas tridimensionais neste desafio!\n#JuhQuiz #Artes #Escultura #Quiz"
        }
    ],
    "Educação Física: danças brasileiras e expressão corporal": [
        {
            "pergunta": "Qual dança brasileira é tradicionalmente associada ao frevo e às festas de Pernambuco?",
            "alternativas": [
                "Frevo",
                "Tango",
                "Flamenco"
            ],
            "correta": 0,
            "imagem": "tema12_pergunta01.png",
            "imagem_path": "imagens_perguntas/tema12_pergunta01.png",
            "legenda": "CAPA_SEGUNDOS=2\nConheça ritmos e expressões das danças brasileiras!\n#JuhQuiz #EducaçãoFísica #Dança #Quiz"
        },
        {
            "pergunta": "O maracatu é uma manifestação cultural e musical tradicionalmente ligada a qual estado?",
            "alternativas": [
                "Amazonas",
                "Pernambuco",
                "Mato Grosso"
            ],
            "correta": 1,
            "imagem": "tema12_pergunta02.png",
            "imagem_path": "imagens_perguntas/tema12_pergunta02.png",
            "legenda": "CAPA_SEGUNDOS=2\nConheça ritmos e expressões das danças brasileiras!\n#JuhQuiz #EducaçãoFísica #Dança #Quiz"
        },
        {
            "pergunta": "Na dança, movimentos e gestos do corpo também podem comunicar ideias e sentimentos. Isso é chamado de:",
            "alternativas": [
                "Arbitragem",
                "Resistência muscular",
                "Expressão corporal"
            ],
            "correta": 2,
            "imagem": "tema12_pergunta03.png",
            "imagem_path": "imagens_perguntas/tema12_pergunta03.png",
            "legenda": "CAPA_SEGUNDOS=2\nConheça ritmos e expressões das danças brasileiras!\n#JuhQuiz #EducaçãoFísica #Dança #Quiz"
        }
    ],
    "Filosofia: Sócrates, Platão e Aristóteles": [
        {
            "pergunta": "Qual filósofo grego ficou conhecido por ensinar por meio de perguntas e diálogos?",
            "alternativas": [
                "Sócrates",
                "Aristóteles",
                "Epicuro"
            ],
            "correta": 0,
            "imagem": "tema13_pergunta01.png",
            "imagem_path": "imagens_perguntas/tema13_pergunta01.png",
            "legenda": "CAPA_SEGUNDOS=2\nUm desafio sobre Sócrates, Platão e Aristóteles.\n#JuhQuiz #Filosofia #Filósofos #Quiz"
        },
        {
            "pergunta": "Qual filósofo foi aluno de Sócrates e fundou a Academia em Atenas?",
            "alternativas": [
                "Aristóteles",
                "Platão",
                "Heráclito"
            ],
            "correta": 1,
            "imagem": "tema13_pergunta02.png",
            "imagem_path": "imagens_perguntas/tema13_pergunta02.png",
            "legenda": "CAPA_SEGUNDOS=2\nUm desafio sobre Sócrates, Platão e Aristóteles.\n#JuhQuiz #Filosofia #Filósofos #Quiz"
        },
        {
            "pergunta": "Qual filósofo grego foi aluno de Platão e associado à escola chamada Liceu?",
            "alternativas": [
                "Sócrates",
                "Pitágoras",
                "Aristóteles"
            ],
            "correta": 2,
            "imagem": "tema13_pergunta03.png",
            "imagem_path": "imagens_perguntas/tema13_pergunta03.png",
            "legenda": "CAPA_SEGUNDOS=2\nUm desafio sobre Sócrates, Platão e Aristóteles.\n#JuhQuiz #Filosofia #Filósofos #Quiz"
        }
    ],
    "Sociologia: socialização e instituições sociais": [
        {
            "pergunta": "Qual grupo costuma participar das primeiras experiências de socialização de uma criança?",
            "alternativas": [
                "Família",
                "Equipe esportiva profissional",
                "Empresa"
            ],
            "correta": 0,
            "imagem": "tema14_pergunta01.png",
            "imagem_path": "imagens_perguntas/tema14_pergunta01.png",
            "legenda": "CAPA_SEGUNDOS=2\nComo aprendemos a conviver em sociedade? Teste seus conhecimentos!\n#JuhQuiz #Sociologia #Sociedade #Quiz"
        },
        {
            "pergunta": "Qual instituição social tem papel importante na educação formal?",
            "alternativas": [
                "Estádio",
                "Escola",
                "Shopping center"
            ],
            "correta": 1,
            "imagem": "tema14_pergunta02.png",
            "imagem_path": "imagens_perguntas/tema14_pergunta02.png",
            "legenda": "CAPA_SEGUNDOS=2\nComo aprendemos a conviver em sociedade? Teste seus conhecimentos!\n#JuhQuiz #Sociologia #Sociedade #Quiz"
        },
        {
            "pergunta": "O processo pelo qual aprendemos normas e modos de convivência em sociedade é chamado de:",
            "alternativas": [
                "Urbanização",
                "Industrialização",
                "Socialização"
            ],
            "correta": 2,
            "imagem": "tema14_pergunta03.png",
            "imagem_path": "imagens_perguntas/tema14_pergunta03.png",
            "legenda": "CAPA_SEGUNDOS=2\nComo aprendemos a conviver em sociedade? Teste seus conhecimentos!\n#JuhQuiz #Sociologia #Sociedade #Quiz"
        }
    ],
    "Informática: planilhas, fórmulas e gráficos": [
        {
            "pergunta": "Em uma planilha, como se chama o espaço formado pelo encontro de uma linha com uma coluna?",
            "alternativas": [
                "Célula",
                "Página",
                "Janela"
            ],
            "correta": 0,
            "imagem": "tema15_pergunta01.png",
            "imagem_path": "imagens_perguntas/tema15_pergunta01.png",
            "legenda": "CAPA_SEGUNDOS=2\nTeste sua lógica com planilhas, fórmulas e gráficos!\n#JuhQuiz #Informática #Planilhas #Quiz"
        },
        {
            "pergunta": "Qual sinal costuma iniciar uma fórmula em programas de planilha?",
            "alternativas": [
                "#",
                "=",
                "@"
            ],
            "correta": 1,
            "imagem": "tema15_pergunta02.png",
            "imagem_path": "imagens_perguntas/tema15_pergunta02.png",
            "legenda": "CAPA_SEGUNDOS=2\nTeste sua lógica com planilhas, fórmulas e gráficos!\n#JuhQuiz #Informática #Planilhas #Quiz"
        },
        {
            "pergunta": "Qual recurso transforma dados de uma planilha em uma representação visual?",
            "alternativas": [
                "Pasta",
                "Teclado",
                "Gráfico"
            ],
            "correta": 2,
            "imagem": "tema15_pergunta03.png",
            "imagem_path": "imagens_perguntas/tema15_pergunta03.png",
            "legenda": "CAPA_SEGUNDOS=2\nTeste sua lógica com planilhas, fórmulas e gráficos!\n#JuhQuiz #Informática #Planilhas #Quiz"
        }
    ]
}

LEGENDAS = {
    "Português: ortografia e uso de G, J, S, SS e Ç": "CAPA_SEGUNDOS=2\nTeste sua atenção neste desafio de ortografia!\n#JuhQuiz #Português #Ortografia #Quiz",
    "Matemática: equações do primeiro grau": "CAPA_SEGUNDOS=2\nResolva três equações do primeiro grau no Juh Quiz!\n#JuhQuiz #Matemática #Equações #Quiz",
    "Biologia: microrganismos e suas funções": "CAPA_SEGUNDOS=2\nDescubra o que você sabe sobre microrganismos!\n#JuhQuiz #Biologia #Microrganismos #Quiz",
    "Química: ácidos, bases e escala de pH": "CAPA_SEGUNDOS=2\nDesafio rápido de química: ácidos, bases e pH.\n#JuhQuiz #Química #pH #Quiz",
    "Física: força e leis de Newton": "CAPA_SEGUNDOS=2\nMostre seus conhecimentos sobre força e as leis de Newton!\n#JuhQuiz #Física #LeisDeNewton #Quiz",
    "História: Independência do Brasil e Período Regencial": "CAPA_SEGUNDOS=2\nRevise a Independência do Brasil e o Período Regencial.\n#JuhQuiz #História #Brasil #Quiz",
    "Geografia: população, migrações e urbanização": "CAPA_SEGUNDOS=2\nTrês perguntas sobre população, migrações e cidades.\n#JuhQuiz #Geografia #População #Quiz",
    "Ciências: efeito estufa e mudanças climáticas": "CAPA_SEGUNDOS=2\nTeste seus conhecimentos sobre efeito estufa e clima.\n#JuhQuiz #Ciências #Clima #Quiz",
    "Literatura: narrador, personagens e enredo": "CAPA_SEGUNDOS=2\nEntre na narrativa: quem conta, quem vive e o que acontece?\n#JuhQuiz #Literatura #Narrativa #Quiz",
    "Inglês: dias da semana, meses e horas": "CAPA_SEGUNDOS=2\nPratique dias, meses e horas em inglês!\n#JuhQuiz #Inglês #Vocabulário #Quiz",
    "Artes: escultura e formas tridimensionais": "CAPA_SEGUNDOS=2\nExplore escultura e formas tridimensionais neste desafio!\n#JuhQuiz #Artes #Escultura #Quiz",
    "Educação Física: danças brasileiras e expressão corporal": "CAPA_SEGUNDOS=2\nConheça ritmos e expressões das danças brasileiras!\n#JuhQuiz #EducaçãoFísica #Dança #Quiz",
    "Filosofia: Sócrates, Platão e Aristóteles": "CAPA_SEGUNDOS=2\nUm desafio sobre Sócrates, Platão e Aristóteles.\n#JuhQuiz #Filosofia #Filósofos #Quiz",
    "Sociologia: socialização e instituições sociais": "CAPA_SEGUNDOS=2\nComo aprendemos a conviver em sociedade? Teste seus conhecimentos!\n#JuhQuiz #Sociologia #Sociedade #Quiz",
    "Informática: planilhas, fórmulas e gráficos": "CAPA_SEGUNDOS=2\nTeste sua lógica com planilhas, fórmulas e gráficos!\n#JuhQuiz #Informática #Planilhas #Quiz"
}
