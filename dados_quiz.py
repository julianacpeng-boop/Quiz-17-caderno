# -*- coding: utf-8 -*-
# Juh Quiz 17 — 15 temas novos, 3 perguntas por tema.
# O gerador acrescenta CAPA_SEGUNDOS=2 ao início de cada arquivo TXT.

QUIZZES = {
    "Português: pontuação e efeitos de sentido": [
        {
            "pergunta": "Em qual frase os dois-pontos introduzem corretamente uma lista?",
            "alternativas": [
                "Trouxe três materiais: lápis, régua e caderno.",
                "Trouxe: três materiais lápis, régua e caderno.",
                "Trouxe três: materiais lápis, régua e caderno."
            ],
            "correta": 0,
            "imagem": "tema01_pergunta01.png"
        },
        {
            "pergunta": "Qual sinal costuma indicar a fala de uma personagem em um diálogo?",
            "alternativas": [
                "Parênteses",
                "Travessão",
                "Ponto e vírgula"
            ],
            "correta": 1,
            "imagem": "tema01_pergunta02.png"
        },
        {
            "pergunta": "Na frase “Que surpresa maravilhosa!”, o ponto de exclamação expressa principalmente:",
            "alternativas": [
                "Uma pergunta direta",
                "Uma pausa entre itens",
                "Uma emoção ou ênfase"
            ],
            "correta": 2,
            "imagem": "tema01_pergunta03.png"
        }
    ],
    "Matemática: geometria plana e sólidos geométricos": [
        {
            "pergunta": "Quantos lados tem um hexágono?",
            "alternativas": [
                "Seis",
                "Cinco",
                "Oito"
            ],
            "correta": 0,
            "imagem": "tema02_pergunta01.png"
        },
        {
            "pergunta": "Qual sólido geométrico tem duas bases circulares e uma superfície lateral curva?",
            "alternativas": [
                "Cone",
                "Cilindro",
                "Pirâmide"
            ],
            "correta": 1,
            "imagem": "tema02_pergunta02.png"
        },
        {
            "pergunta": "Um retângulo mede 8 cm por 3 cm. Qual é sua área?",
            "alternativas": [
                "11 cm²",
                "22 cm²",
                "24 cm²"
            ],
            "correta": 2,
            "imagem": "tema02_pergunta03.png"
        }
    ],
    "Biologia: ecossistemas e cadeias alimentares": [
        {
            "pergunta": "Em uma cadeia alimentar, qual ser vivo geralmente produz seu próprio alimento usando luz?",
            "alternativas": [
                "Planta",
                "Fungo",
                "Onça"
            ],
            "correta": 0,
            "imagem": "tema03_pergunta01.png"
        },
        {
            "pergunta": "Qual é o papel comum de fungos e muitas bactérias nos ecossistemas?",
            "alternativas": [
                "Produzir luz solar",
                "Decompor matéria orgânica",
                "Caçar grandes animais"
            ],
            "correta": 1,
            "imagem": "tema03_pergunta02.png"
        },
        {
            "pergunta": "Em uma cadeia alimentar, a energia passa entre os seres vivos principalmente por meio:",
            "alternativas": [
                "Do som",
                "Da água da chuva",
                "Da alimentação"
            ],
            "correta": 2,
            "imagem": "tema03_pergunta03.png"
        }
    ],
    "Química: misturas e métodos de separação": [
        {
            "pergunta": "Qual método pode separar areia da água usando um material poroso?",
            "alternativas": [
                "Filtração",
                "Imantação",
                "Destilação fracionada"
            ],
            "correta": 0,
            "imagem": "tema04_pergunta01.png"
        },
        {
            "pergunta": "Para separar limalha de ferro de areia, qual recurso é mais adequado?",
            "alternativas": [
                "Peneira fina",
                "Ímã",
                "Funil de decantação"
            ],
            "correta": 1,
            "imagem": "tema04_pergunta02.png"
        },
        {
            "pergunta": "A destilação simples pode separar um líquido de um sólido dissolvido aproveitando diferenças de:",
            "alternativas": [
                "Cor",
                "Tamanho dos grãos",
                "Ponto de ebulição"
            ],
            "correta": 2,
            "imagem": "tema04_pergunta03.png"
        }
    ],
    "Física: calor, temperatura e mudanças de estado": [
        {
            "pergunta": "Como se chama a transferência de calor por contato direto entre partículas?",
            "alternativas": [
                "Condução",
                "Reflexão",
                "Eletrização"
            ],
            "correta": 0,
            "imagem": "tema05_pergunta01.png"
        },
        {
            "pergunta": "Qual instrumento é usado para medir a temperatura?",
            "alternativas": [
                "Barômetro",
                "Termômetro",
                "Bússola"
            ],
            "correta": 1,
            "imagem": "tema05_pergunta02.png"
        },
        {
            "pergunta": "Quando a água líquida passa lentamente para vapor pela superfície, ocorre:",
            "alternativas": [
                "Solidificação",
                "Condensação",
                "Evaporação"
            ],
            "correta": 2,
            "imagem": "tema05_pergunta03.png"
        }
    ],
    "História: Idade Média, feudos e vida cotidiana": [
        {
            "pergunta": "Como era chamado o território rural que organizava grande parte da sociedade feudal?",
            "alternativas": [
                "Feudo",
                "Município industrial",
                "Colônia espacial"
            ],
            "correta": 0,
            "imagem": "tema06_pergunta01.png"
        },
        {
            "pergunta": "Na sociedade feudal, quem trabalhava principalmente nas terras e prestava obrigações ao senhor?",
            "alternativas": [
                "Mercadores marítimos",
                "Servos",
                "Senadores romanos"
            ],
            "correta": 1,
            "imagem": "tema06_pergunta02.png"
        },
        {
            "pergunta": "Qual construção era comum como centro de proteção e moradia de muitos senhores feudais?",
            "alternativas": [
                "Farol moderno",
                "Fábrica a vapor",
                "Castelo"
            ],
            "correta": 2,
            "imagem": "tema06_pergunta03.png"
        }
    ],
    "Geografia: clima e biomas brasileiros": [
        {
            "pergunta": "Qual bioma brasileiro é conhecido por longos períodos de seca e vegetação adaptada à falta de água?",
            "alternativas": [
                "Caatinga",
                "Pampa",
                "Pantanal"
            ],
            "correta": 0,
            "imagem": "tema07_pergunta01.png"
        },
        {
            "pergunta": "Qual bioma ocupa grande parte do Brasil central e apresenta árvores retorcidas e estação seca marcada?",
            "alternativas": [
                "Mata Atlântica",
                "Cerrado",
                "Amazônia"
            ],
            "correta": 1,
            "imagem": "tema07_pergunta02.png"
        },
        {
            "pergunta": "O clima equatorial costuma apresentar temperaturas elevadas e:",
            "alternativas": [
                "Invernos longos com neve",
                "Chuvas raras o ano inteiro",
                "Umidade e chuvas abundantes"
            ],
            "correta": 2,
            "imagem": "tema07_pergunta03.png"
        }
    ],
    "Ciências: ciclo da água e tratamento": [
        {
            "pergunta": "Como se chama a passagem da água líquida para vapor causada pelo calor?",
            "alternativas": [
                "Evaporação",
                "Precipitação",
                "Infiltração"
            ],
            "correta": 0,
            "imagem": "tema08_pergunta01.png"
        },
        {
            "pergunta": "No ciclo da água, a formação de gotículas nas nuvens é chamada de:",
            "alternativas": [
                "Fusão",
                "Condensação",
                "Combustão"
            ],
            "correta": 1,
            "imagem": "tema08_pergunta02.png"
        },
        {
            "pergunta": "Em uma estação de tratamento, qual etapa ajuda a remover partículas sólidas em suspensão?",
            "alternativas": [
                "Cloração final",
                "Aeração da água",
                "Filtração"
            ],
            "correta": 2,
            "imagem": "tema08_pergunta03.png"
        }
    ],
    "Literatura: escolas literárias brasileiras": [
        {
            "pergunta": "Qual movimento literário brasileiro valorizou a identidade nacional e a natureza no século XIX?",
            "alternativas": [
                "Romantismo",
                "Realismo",
                "Naturalismo"
            ],
            "correta": 0,
            "imagem": "tema09_pergunta01.png"
        },
        {
            "pergunta": "Qual movimento cultural de 1922 propôs renovar a arte e a literatura no Brasil?",
            "alternativas": [
                "Arcadismo",
                "Modernismo",
                "Trovadorismo"
            ],
            "correta": 1,
            "imagem": "tema09_pergunta02.png"
        },
        {
            "pergunta": "Qual estilo literário é conhecido por contrastes, linguagem elaborada e conflitos entre fé e razão?",
            "alternativas": [
                "Parnasianismo",
                "Simbolismo",
                "Barroco"
            ],
            "correta": 2,
            "imagem": "tema09_pergunta03.png"
        }
    ],
    "Inglês: pronomes pessoais e possessivos": [
        {
            "pergunta": "Qual pronome pessoal em inglês significa “eles” ou “elas”?",
            "alternativas": [
                "They",
                "We",
                "She"
            ],
            "correta": 0,
            "imagem": "tema10_pergunta01.png"
        },
        {
            "pergunta": "Complete: “This is Ana. ___ is my friend.”",
            "alternativas": [
                "He",
                "She",
                "It"
            ],
            "correta": 1,
            "imagem": "tema10_pergunta02.png"
        },
        {
            "pergunta": "Qual palavra completa corretamente: “That book is ___.” (o livro é meu)",
            "alternativas": [
                "your",
                "their",
                "mine"
            ],
            "correta": 2,
            "imagem": "tema10_pergunta03.png"
        }
    ],
    "Artes: movimentos artísticos do século XX": [
        {
            "pergunta": "Qual movimento artístico ficou conhecido por representar objetos usando formas geométricas e vários pontos de vista?",
            "alternativas": [
                "Cubismo",
                "Impressionismo",
                "Romantismo"
            ],
            "correta": 0,
            "imagem": "tema11_pergunta01.png"
        },
        {
            "pergunta": "Qual movimento buscava registrar efeitos de luz e cor em cenas do cotidiano?",
            "alternativas": [
                "Barroco",
                "Impressionismo",
                "Expressionismo abstrato"
            ],
            "correta": 1,
            "imagem": "tema11_pergunta02.png"
        },
        {
            "pergunta": "Qual movimento explorou imagens de sonhos e do inconsciente?",
            "alternativas": [
                "Realismo",
                "Futurismo",
                "Surrealismo"
            ],
            "correta": 2,
            "imagem": "tema11_pergunta03.png"
        }
    ],
    "Educação Física: capacidades físicas, como força e resistência": [
        {
            "pergunta": "Qual capacidade física ajuda a manter um esforço por mais tempo?",
            "alternativas": [
                "Resistência",
                "Equilíbrio",
                "Agilidade"
            ],
            "correta": 0,
            "imagem": "tema12_pergunta01.png"
        },
        {
            "pergunta": "Qual capacidade está relacionada à amplitude dos movimentos das articulações?",
            "alternativas": [
                "Velocidade",
                "Flexibilidade",
                "Potência"
            ],
            "correta": 1,
            "imagem": "tema12_pergunta02.png"
        },
        {
            "pergunta": "Qual capacidade física permite vencer ou sustentar uma resistência muscular?",
            "alternativas": [
                "Coordenação",
                "Ritmo",
                "Força"
            ],
            "correta": 2,
            "imagem": "tema12_pergunta03.png"
        }
    ],
    "Filosofia: lógica e construção de argumentos": [
        {
            "pergunta": "Em um argumento, como se chamam as afirmações usadas para apoiar uma ideia final?",
            "alternativas": [
                "Premissas",
                "Exemplos visuais",
                "Interjeições"
            ],
            "correta": 0,
            "imagem": "tema13_pergunta01.png"
        },
        {
            "pergunta": "A afirmação que o argumento procura justificar é chamada de:",
            "alternativas": [
                "Pergunta retórica",
                "Conclusão",
                "Hipótese experimental"
            ],
            "correta": 1,
            "imagem": "tema13_pergunta02.png"
        },
        {
            "pergunta": "Um raciocínio que parece convincente, mas contém um erro, pode ser chamado de:",
            "alternativas": [
                "Definição",
                "Observação",
                "Falácia"
            ],
            "correta": 2,
            "imagem": "tema13_pergunta03.png"
        }
    ],
    "Sociologia: cidadania, direitos e participação social": [
        {
            "pergunta": "Qual atitude é um exemplo de participação cidadã na comunidade?",
            "alternativas": [
                "Participar de uma reunião comunitária",
                "Ignorar decisões coletivas",
                "Impedir outras pessoas de falar"
            ],
            "correta": 0,
            "imagem": "tema14_pergunta01.png"
        },
        {
            "pergunta": "Qual documento reúne direitos e deveres fundamentais no Brasil?",
            "alternativas": [
                "Manual de instruções",
                "Constituição Federal",
                "Mapa rodoviário"
            ],
            "correta": 1,
            "imagem": "tema14_pergunta02.png"
        },
        {
            "pergunta": "A participação social pode ajudar uma comunidade a:",
            "alternativas": [
                "Eliminar todas as diferenças individuais",
                "Evitar qualquer diálogo",
                "Debater necessidades e propor melhorias"
            ],
            "correta": 2,
            "imagem": "tema14_pergunta03.png"
        }
    ],
    "Informática: hardware, software e sistemas operacionais": [
        {
            "pergunta": "Qual item é um componente físico de um computador?",
            "alternativas": [
                "Teclado",
                "Editor de texto",
                "Navegador de internet"
            ],
            "correta": 0,
            "imagem": "tema15_pergunta01.png"
        },
        {
            "pergunta": "Qual é uma função principal do sistema operacional?",
            "alternativas": [
                "Imprimir sem equipamento",
                "Gerenciar recursos e permitir a execução de programas",
                "Criar energia elétrica"
            ],
            "correta": 1,
            "imagem": "tema15_pergunta02.png"
        },
        {
            "pergunta": "Qual componente armazena temporariamente dados enquanto programas estão em uso?",
            "alternativas": [
                "Monitor",
                "Impressora",
                "Memória RAM"
            ],
            "correta": 2,
            "imagem": "tema15_pergunta03.png"
        }
    ]
}

LEGENDAS = {
    "Português: pontuação e efeitos de sentido": "Pontuação muda o ritmo e o sentido das frases. Acerte esse desafio! ✍️\n#JuhQuiz #Português #Pontuação",
    "Matemática: geometria plana e sólidos geométricos": "Figuras planas e sólidos: teste seu olhar para a geometria! 📐\n#JuhQuiz #Matemática #Geometria",
    "Biologia: ecossistemas e cadeias alimentares": "Vamos explorar as relações entre os seres vivos nos ecossistemas? 🌿\n#JuhQuiz #Biologia #Ecossistemas",
    "Química: misturas e métodos de separação": "Filtração, ímã ou destilação? Descubra quanto você sabe de misturas! ⚗️\n#JuhQuiz #Química #Misturas",
    "Física: calor, temperatura e mudanças de estado": "Calor e mudanças de estado: encare este quiz de Física! 🌡️\n#JuhQuiz #Física #Ciências",
    "História: Idade Média, feudos e vida cotidiana": "Como era a vida nos feudos medievais? Teste seus conhecimentos! 🏰\n#JuhQuiz #História #IdadeMédia",
    "Geografia: clima e biomas brasileiros": "Climas e biomas do Brasil: quantas você consegue acertar? 🌳\n#JuhQuiz #Geografia #Brasil",
    "Ciências: ciclo da água e tratamento": "Do ciclo da água ao tratamento: responda ao desafio! 💧\n#JuhQuiz #Ciências #Água",
    "Literatura: escolas literárias brasileiras": "Romantismo, Modernismo e outros movimentos: teste sua memória literária! 📚\n#JuhQuiz #Literatura #EscolasLiterárias",
    "Inglês: pronomes pessoais e possessivos": "Hora de praticar pronomes pessoais e possessivos em inglês! 🇬🇧\n#JuhQuiz #Inglês #Pronomes",
    "Artes: movimentos artísticos do século XX": "Cubismo, Impressionismo e Surrealismo: reconhece esses movimentos? 🎨\n#JuhQuiz #Artes #HistóriaDaArte",
    "Educação Física: capacidades físicas, como força e resistência": "Força, resistência e flexibilidade: teste seus conhecimentos! 🏃\n#JuhQuiz #EducaçãoFísica #Movimento",
    "Filosofia: lógica e construção de argumentos": "Premissas, conclusões e falácias: bora pensar com lógica? 💭\n#JuhQuiz #Filosofia #Lógica",
    "Sociologia: cidadania, direitos e participação social": "Cidadania também é participação. Veja quantas você acerta! 🤝\n#JuhQuiz #Sociologia #Cidadania",
    "Informática: hardware, software e sistemas operacionais": "Hardware, software e sistema operacional: encare o quiz! 💻\n#JuhQuiz #Informática #Tecnologia"
}

