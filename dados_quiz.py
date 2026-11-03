# -*- coding: utf-8 -*-
"""Quiz 17 – Caderno: 15 disciplinas, 45 questões e imagens com fundo.

Substitua o conteúdo do arquivo dados_quiz.py do repositório por este arquivo.
As 45 imagens devem ficar em imagens_perguntas/ com os nomes aqui indicados.
O gerador atual acrescenta CAPA_SEGUNDOS=2 ao TXT final.
"""

QUIZZES = {'Português — Figuras de linguagem': [{'pergunta': "Na frase 'Seu sorriso é um sol', qual figura de "
                                                   'linguagem aparece?',
                                       'alternativas': ['Ironia', 'Metáfora', 'Hipérbole'],
                                       'correta': 1,
                                       'imagem': 'tema01_pergunta01.jpg',
                                       'imagem_path': 'imagens_perguntas/tema01_pergunta01.jpg',
                                       'legenda': '📚 Português: Figuras de linguagem. Você acerta as '
                                                  'três?\n'
                                                  '#JuhQuiz #Quiz17 #QuizEscolar #Desafio'},
                                      {'pergunta': "Alguém diz 'Que dia maravilhoso!' em meio a um "
                                                   'temporal. Qual figura pode estar presente?',
                                       'alternativas': ['Ironia', 'Comparação', 'Personificação'],
                                       'correta': 0,
                                       'imagem': 'tema01_pergunta02.jpg',
                                       'imagem_path': 'imagens_perguntas/tema01_pergunta02.jpg',
                                       'legenda': '📚 Português: Figuras de linguagem. Você acerta as '
                                                  'três?\n'
                                                  '#JuhQuiz #Quiz17 #QuizEscolar #Desafio'},
                                      {'pergunta': "Em 'Tenho uma montanha de tarefas', o exagero é "
                                                   'chamado de quê?',
                                       'alternativas': ['Metonímia', 'Antítese', 'Hipérbole'],
                                       'correta': 2,
                                       'imagem': 'tema01_pergunta03.jpg',
                                       'imagem_path': 'imagens_perguntas/tema01_pergunta03.jpg',
                                       'legenda': '📚 Português: Figuras de linguagem. Você acerta as '
                                                  'três?\n'
                                                  '#JuhQuiz #Quiz17 #QuizEscolar #Desafio'}],
 'Matemática — Porcentagem': [{'pergunta': 'Um produto de R$ 200 recebe 25% de desconto. Qual é o preço '
                                           'final?',
                               'alternativas': ['R$ 150', 'R$ 175', 'R$ 125'],
                               'correta': 0,
                               'imagem': 'tema02_pergunta01.jpg',
                               'imagem_path': 'imagens_perguntas/tema02_pergunta01.jpg',
                               'legenda': '📚 Matemática: Porcentagem. Você acerta as três?\n'
                                          '#JuhQuiz #Quiz17 #QuizEscolar #Desafio'},
                              {'pergunta': 'Um valor de 80 aumenta 20%. Quanto passa a valer?',
                               'alternativas': ['88', '96', '100'],
                               'correta': 1,
                               'imagem': 'tema02_pergunta02.jpg',
                               'imagem_path': 'imagens_perguntas/tema02_pergunta02.jpg',
                               'legenda': '📚 Matemática: Porcentagem. Você acerta as três?\n'
                                          '#JuhQuiz #Quiz17 #QuizEscolar #Desafio'},
                              {'pergunta': 'Descontos sucessivos de 20% e 10% equivalem a qual desconto '
                                           'total?',
                               'alternativas': ['30%', '32%', '28%'],
                               'correta': 2,
                               'imagem': 'tema02_pergunta03.jpg',
                               'imagem_path': 'imagens_perguntas/tema02_pergunta03.jpg',
                               'legenda': '📚 Matemática: Porcentagem. Você acerta as três?\n'
                                          '#JuhQuiz #Quiz17 #QuizEscolar #Desafio'}],
 'Biologia — Genética': [{'pergunta': 'Por que irmãos podem ter características genéticas diferentes?',
                          'alternativas': ['Porque recebem combinações diferentes de genes',
                                           'Porque irmãos sempre têm DNA idêntico',
                                           'Porque só herdam genes da mãe'],
                          'correta': 0,
                          'imagem': 'tema03_pergunta01.jpg',
                          'imagem_path': 'imagens_perguntas/tema03_pergunta01.jpg',
                          'legenda': '📚 Biologia: Genética. Você acerta as três?\n'
                                     '#JuhQuiz #Quiz17 #QuizEscolar #Desafio'},
                         {'pergunta': 'Em uma célula humana somática típica, quantos cromossomos '
                                      'existem?',
                          'alternativas': ['23', '46', '44'],
                          'correta': 1,
                          'imagem': 'tema03_pergunta02.jpg',
                          'imagem_path': 'imagens_perguntas/tema03_pergunta02.jpg',
                          'legenda': '📚 Biologia: Genética. Você acerta as três?\n'
                                     '#JuhQuiz #Quiz17 #QuizEscolar #Desafio'},
                         {'pergunta': 'Qual destes exemplos representa uma característica com '
                                      'influência genética?',
                          'alternativas': ['Idioma que a pessoa fala',
                                           'Esporte que prefere',
                                           'Cor natural dos olhos'],
                          'correta': 2,
                          'imagem': 'tema03_pergunta03.jpg',
                          'imagem_path': 'imagens_perguntas/tema03_pergunta03.jpg',
                          'legenda': '📚 Biologia: Genética. Você acerta as três?\n'
                                     '#JuhQuiz #Quiz17 #QuizEscolar #Desafio'}],
 'Química — Tabela periódica': [{'pergunta': 'Na tabela periódica moderna, os elementos são ordenados '
                                             'pelo quê?',
                                 'alternativas': ['Número de massa', 'Número atômico', 'Estado físico'],
                                 'correta': 1,
                                 'imagem': 'tema04_pergunta01.jpg',
                                 'imagem_path': 'imagens_perguntas/tema04_pergunta01.jpg',
                                 'legenda': '📚 Química: Tabela periódica. Você acerta as três?\n'
                                            '#JuhQuiz #Quiz17 #QuizEscolar #Desafio'},
                                {'pergunta': 'Qual elemento químico é representado pelo símbolo Au?',
                                 'alternativas': ['Alumínio', 'Argônio', 'Ouro'],
                                 'correta': 2,
                                 'imagem': 'tema04_pergunta02.jpg',
                                 'imagem_path': 'imagens_perguntas/tema04_pergunta02.jpg',
                                 'legenda': '📚 Química: Tabela periódica. Você acerta as três?\n'
                                            '#JuhQuiz #Quiz17 #QuizEscolar #Desafio'},
                                {'pergunta': 'Quando substâncias se transformam em outras, ocorre '
                                             'uma...',
                                 'alternativas': ['Reação química',
                                                  'Mudança de volume apenas',
                                                  'Mudança de estado apenas'],
                                 'correta': 0,
                                 'imagem': 'tema04_pergunta03.jpg',
                                 'imagem_path': 'imagens_perguntas/tema04_pergunta03.jpg',
                                 'legenda': '📚 Química: Tabela periódica. Você acerta as três?\n'
                                            '#JuhQuiz #Quiz17 #QuizEscolar #Desafio'}],
 'Física — Eletricidade': [{'pergunta': 'Em um circuito simples, o que acontece se o interruptor for '
                                        'aberto?',
                            'alternativas': ['A tensão da bateria dobra',
                                             'A corrente é interrompida',
                                             'A resistência desaparece'],
                            'correta': 1,
                            'imagem': 'tema05_pergunta01.jpg',
                            'imagem_path': 'imagens_perguntas/tema05_pergunta01.jpg',
                            'legenda': '📚 Física: Eletricidade. Você acerta as três?\n'
                                       '#JuhQuiz #Quiz17 #QuizEscolar #Desafio'},
                           {'pergunta': 'Qual grandeza elétrica é medida em volts (V)?',
                            'alternativas': ['Resistência elétrica',
                                             'Corrente elétrica',
                                             'Tensão elétrica'],
                            'correta': 2,
                            'imagem': 'tema05_pergunta02.jpg',
                            'imagem_path': 'imagens_perguntas/tema05_pergunta02.jpg',
                            'legenda': '📚 Física: Eletricidade. Você acerta as três?\n'
                                       '#JuhQuiz #Quiz17 #QuizEscolar #Desafio'},
                           {'pergunta': 'Dois aparelhos têm a mesma potência. Qual tende a gastar mais '
                                        'energia?',
                            'alternativas': ['O usado por mais tempo',
                                             'O de cor mais escura',
                                             'O de cabo mais comprido'],
                            'correta': 0,
                            'imagem': 'tema05_pergunta03.jpg',
                            'imagem_path': 'imagens_perguntas/tema05_pergunta03.jpg',
                            'legenda': '📚 Física: Eletricidade. Você acerta as três?\n'
                                       '#JuhQuiz #Quiz17 #QuizEscolar #Desafio'}],
 'História — Ditadura Militar no Brasil': [{'pergunta': 'Em que ano começou a ditadura militar no '
                                                        'Brasil?',
                                            'alternativas': ['1964', '1979', '1988'],
                                            'correta': 0,
                                            'imagem': 'tema06_pergunta01.jpg',
                                            'imagem_path': 'imagens_perguntas/tema06_pergunta01.jpg',
                                            'legenda': '📚 História: Ditadura Militar no Brasil. Você '
                                                       'acerta as três?\n'
                                                       '#JuhQuiz #Quiz17 #QuizEscolar #Desafio'},
                                           {'pergunta': 'Qual ato institucional de 1968 ampliou a '
                                                        'repressão política?',
                                            'alternativas': ['AI-2', 'AI-5', 'AI-1'],
                                            'correta': 1,
                                            'imagem': 'tema06_pergunta02.jpg',
                                            'imagem_path': 'imagens_perguntas/tema06_pergunta02.jpg',
                                            'legenda': '📚 História: Ditadura Militar no Brasil. Você '
                                                       'acerta as três?\n'
                                                       '#JuhQuiz #Quiz17 #QuizEscolar #Desafio'},
                                           {'pergunta': 'Em qual década ganhou força o movimento '
                                                        'Diretas Já?',
                                            'alternativas': ['Década de 1960',
                                                             'Década de 1990',
                                                             'Década de 1980'],
                                            'correta': 2,
                                            'imagem': 'tema06_pergunta03.jpg',
                                            'imagem_path': 'imagens_perguntas/tema06_pergunta03.jpg',
                                            'legenda': '📚 História: Ditadura Militar no Brasil. Você '
                                                       'acerta as três?\n'
                                                       '#JuhQuiz #Quiz17 #QuizEscolar #Desafio'}],
 'Geografia — Países e capitais': [{'pergunta': 'Qual é a capital do Canadá?',
                                    'alternativas': ['Toronto', 'Ottawa', 'Vancouver'],
                                    'correta': 1,
                                    'imagem': 'tema07_pergunta01.jpg',
                                    'imagem_path': 'imagens_perguntas/tema07_pergunta01.jpg',
                                    'legenda': '📚 Geografia: Países e capitais. Você acerta as três?\n'
                                               '#JuhQuiz #Quiz17 #QuizEscolar #Desafio'},
                                   {'pergunta': 'Em que país fica a cidade de Roma?',
                                    'alternativas': ['Grécia', 'Espanha', 'Itália'],
                                    'correta': 2,
                                    'imagem': 'tema07_pergunta02.jpg',
                                    'imagem_path': 'imagens_perguntas/tema07_pergunta02.jpg',
                                    'legenda': '📚 Geografia: Países e capitais. Você acerta as três?\n'
                                               '#JuhQuiz #Quiz17 #QuizEscolar #Desafio'},
                                   {'pergunta': 'Qual capital brasileira foi inaugurada em 1960?',
                                    'alternativas': ['Brasília', 'Salvador', 'Belo Horizonte'],
                                    'correta': 0,
                                    'imagem': 'tema07_pergunta03.jpg',
                                    'imagem_path': 'imagens_perguntas/tema07_pergunta03.jpg',
                                    'legenda': '📚 Geografia: Países e capitais. Você acerta as três?\n'
                                               '#JuhQuiz #Quiz17 #QuizEscolar #Desafio'}],
 'Ciências — Sistema Solar': [{'pergunta': 'Como se chama o movimento da Terra ao redor do Sol?',
                               'alternativas': ['Rotação', 'Translação', 'Precessão'],
                               'correta': 1,
                               'imagem': 'tema08_pergunta01.jpg',
                               'imagem_path': 'imagens_perguntas/tema08_pergunta01.jpg',
                               'legenda': '📚 Ciências: Sistema Solar. Você acerta as três?\n'
                                          '#JuhQuiz #Quiz17 #QuizEscolar #Desafio'},
                              {'pergunta': 'Um eclipse solar total pode ser visto de toda a Terra ao '
                                           'mesmo tempo?',
                               'alternativas': ['Sim, de todos os continentes',
                                                'Somente do lado noturno',
                                                'Não, apenas de uma faixa limitada'],
                               'correta': 2,
                               'imagem': 'tema08_pergunta02.jpg',
                               'imagem_path': 'imagens_perguntas/tema08_pergunta02.jpg',
                               'legenda': '📚 Ciências: Sistema Solar. Você acerta as três?\n'
                                          '#JuhQuiz #Quiz17 #QuizEscolar #Desafio'},
                              {'pergunta': 'A Lua produz sua própria luz visível?',
                               'alternativas': ['Não, ela reflete luz solar',
                                                'Sim, por combustão interna',
                                                'Apenas quando está cheia'],
                               'correta': 0,
                               'imagem': 'tema08_pergunta03.jpg',
                               'imagem_path': 'imagens_perguntas/tema08_pergunta03.jpg',
                               'legenda': '📚 Ciências: Sistema Solar. Você acerta as três?\n'
                                          '#JuhQuiz #Quiz17 #QuizEscolar #Desafio'}],
 'Literatura — Escritores brasileiros': [{'pergunta': 'Quem escreveu o romance Dom Casmurro?',
                                          'alternativas': ['Jorge Amado',
                                                           'Machado de Assis',
                                                           'José de Alencar'],
                                          'correta': 1,
                                          'imagem': 'tema09_pergunta01.jpg',
                                          'imagem_path': 'imagens_perguntas/tema09_pergunta01.jpg',
                                          'legenda': '📚 Literatura: Escritores brasileiros. Você acerta '
                                                     'as três?\n'
                                                     '#JuhQuiz #Quiz17 #QuizEscolar #Desafio'},
                                         {'pergunta': 'Quem é o narrador de Memórias Póstumas de Brás '
                                                      'Cubas?',
                                          'alternativas': ['Bentinho', 'Quincas Borba', 'Brás Cubas'],
                                          'correta': 2,
                                          'imagem': 'tema09_pergunta02.jpg',
                                          'imagem_path': 'imagens_perguntas/tema09_pergunta02.jpg',
                                          'legenda': '📚 Literatura: Escritores brasileiros. Você acerta '
                                                     'as três?\n'
                                                     '#JuhQuiz #Quiz17 #QuizEscolar #Desafio'},
                                         {'pergunta': 'Qual escritora brasileira escreveu A Hora da '
                                                      'Estrela?',
                                          'alternativas': ['Clarice Lispector',
                                                           'Cecília Meireles',
                                                           'Rachel de Queiroz'],
                                          'correta': 0,
                                          'imagem': 'tema09_pergunta03.jpg',
                                          'imagem_path': 'imagens_perguntas/tema09_pergunta03.jpg',
                                          'legenda': '📚 Literatura: Escritores brasileiros. Você acerta '
                                                     'as três?\n'
                                                     '#JuhQuiz #Quiz17 #QuizEscolar #Desafio'}],
 'Inglês — Falsos cognatos': [{'pergunta': "Na frase 'They pretend to sleep', o verbo pretend "
                                           'significa...',
                               'alternativas': ['Pretender', 'Fingir', 'Prevenir'],
                               'correta': 1,
                               'imagem': 'tema10_pergunta01.jpg',
                               'imagem_path': 'imagens_perguntas/tema10_pergunta01.jpg',
                               'legenda': '📚 Inglês: Falsos cognatos. Você acerta as três?\n'
                                          '#JuhQuiz #Quiz17 #QuizEscolar #Desafio'},
                              {'pergunta': 'Em inglês, a palavra fabric significa...',
                               'alternativas': ['Fábrica', 'Fabricação', 'Tecido'],
                               'correta': 2,
                               'imagem': 'tema10_pergunta02.jpg',
                               'imagem_path': 'imagens_perguntas/tema10_pergunta02.jpg',
                               'legenda': '📚 Inglês: Falsos cognatos. Você acerta as três?\n'
                                          '#JuhQuiz #Quiz17 #QuizEscolar #Desafio'},
                              {'pergunta': "Na frase 'I actually live here', actually significa...",
                               'alternativas': ['Na verdade', 'Atualmente', 'Eventualmente'],
                               'correta': 0,
                               'imagem': 'tema10_pergunta03.jpg',
                               'imagem_path': 'imagens_perguntas/tema10_pergunta03.jpg',
                               'legenda': '📚 Inglês: Falsos cognatos. Você acerta as três?\n'
                                          '#JuhQuiz #Quiz17 #QuizEscolar #Desafio'}],
 'Artes — Obras e expressões artísticas': [{'pergunta': 'Quem pintou o famoso retrato Mona Lisa?',
                                            'alternativas': ['Vincent van Gogh',
                                                             'Leonardo da Vinci',
                                                             'Michelangelo'],
                                            'correta': 1,
                                            'imagem': 'tema11_pergunta01.jpg',
                                            'imagem_path': 'imagens_perguntas/tema11_pergunta01.jpg',
                                            'legenda': '📚 Artes: Obras e expressões artísticas. Você '
                                                       'acerta as três?\n'
                                                       '#JuhQuiz #Quiz17 #QuizEscolar #Desafio'},
                                           {'pergunta': 'Uma escultura é uma obra que ocupa, em geral, '
                                                        'quantas dimensões?',
                                            'alternativas': ['Duas', 'Uma', 'Três'],
                                            'correta': 2,
                                            'imagem': 'tema11_pergunta02.jpg',
                                            'imagem_path': 'imagens_perguntas/tema11_pergunta02.jpg',
                                            'legenda': '📚 Artes: Obras e expressões artísticas. Você '
                                                       'acerta as três?\n'
                                                       '#JuhQuiz #Quiz17 #QuizEscolar #Desafio'},
                                           {'pergunta': 'Na música, ritmo está relacionado '
                                                        'principalmente a quê?',
                                            'alternativas': ['Organização de sons e pausas no tempo',
                                                             'Altura de uma única nota',
                                                             'Tamanho do instrumento'],
                                            'correta': 0,
                                            'imagem': 'tema11_pergunta03.jpg',
                                            'imagem_path': 'imagens_perguntas/tema11_pergunta03.jpg',
                                            'legenda': '📚 Artes: Obras e expressões artísticas. Você '
                                                       'acerta as três?\n'
                                                       '#JuhQuiz #Quiz17 #QuizEscolar #Desafio'}],
 'Educação Física — Corpo humano em movimento': [{'pergunta': 'Qual sistema transporta oxigênio pelo '
                                                              'corpo durante uma corrida?',
                                                  'alternativas': ['Sistema digestório',
                                                                   'Sistema circulatório',
                                                                   'Sistema urinário'],
                                                  'correta': 1,
                                                  'imagem': 'tema12_pergunta01.jpg',
                                                  'imagem_path': 'imagens_perguntas/tema12_pergunta01.jpg',
                                                  'legenda': '📚 Educação Física: Corpo humano em '
                                                             'movimento. Você acerta as três?\n'
                                                             '#JuhQuiz #Quiz17 #QuizEscolar #Desafio'},
                                                 {'pergunta': 'Que tipo de tecido permite a contração '
                                                              'dos músculos do corpo?',
                                                  'alternativas': ['Tecido nervoso',
                                                                   'Tecido epitelial',
                                                                   'Tecido muscular'],
                                                  'correta': 2,
                                                  'imagem': 'tema12_pergunta02.jpg',
                                                  'imagem_path': 'imagens_perguntas/tema12_pergunta02.jpg',
                                                  'legenda': '📚 Educação Física: Corpo humano em '
                                                             'movimento. Você acerta as três?\n'
                                                             '#JuhQuiz #Quiz17 #QuizEscolar #Desafio'},
                                                 {'pergunta': 'Para repor líquidos após exercícios '
                                                              'habituais, qual bebida é mais indicada?',
                                                  'alternativas': ['Água',
                                                                   'Refrigerante',
                                                                   'Bebida alcoólica'],
                                                  'correta': 0,
                                                  'imagem': 'tema12_pergunta03.jpg',
                                                  'imagem_path': 'imagens_perguntas/tema12_pergunta03.jpg',
                                                  'legenda': '📚 Educação Física: Corpo humano em '
                                                             'movimento. Você acerta as três?\n'
                                                             '#JuhQuiz #Quiz17 #QuizEscolar #Desafio'}],
 'Filosofia — Grandes filósofos e ideias': [{'pergunta': 'Qual filósofo grego tornou-se conhecido pelo '
                                                         'método de perguntas e diálogo?',
                                             'alternativas': ['Aristóteles', 'Sócrates', 'Epicuro'],
                                             'correta': 1,
                                             'imagem': 'tema13_pergunta01.jpg',
                                             'imagem_path': 'imagens_perguntas/tema13_pergunta01.jpg',
                                             'legenda': '📚 Filosofia: Grandes filósofos e ideias. Você '
                                                        'acerta as três?\n'
                                                        '#JuhQuiz #Quiz17 #QuizEscolar #Desafio'},
                                            {'pergunta': 'Qual área da filosofia investiga como '
                                                         'conhecemos e justificamos o saber?',
                                             'alternativas': ['Ética', 'Estética', 'Epistemologia'],
                                             'correta': 2,
                                             'imagem': 'tema13_pergunta02.jpg',
                                             'imagem_path': 'imagens_perguntas/tema13_pergunta02.jpg',
                                             'legenda': '📚 Filosofia: Grandes filósofos e ideias. Você '
                                                        'acerta as três?\n'
                                                        '#JuhQuiz #Quiz17 #QuizEscolar #Desafio'},
                                            {'pergunta': 'Que tema é estudado pela ética na filosofia?',
                                             'alternativas': ['O que torna nossas ações certas ou '
                                                              'erradas',
                                                              'A composição química dos metais',
                                                              'A posição dos planetas'],
                                             'correta': 0,
                                             'imagem': 'tema13_pergunta03.jpg',
                                             'imagem_path': 'imagens_perguntas/tema13_pergunta03.jpg',
                                             'legenda': '📚 Filosofia: Grandes filósofos e ideias. Você '
                                                        'acerta as três?\n'
                                                        '#JuhQuiz #Quiz17 #QuizEscolar #Desafio'}],
 'Sociologia — Desigualdade social': [{'pergunta': 'Qual expressão descreve diferenças sistemáticas de '
                                                   'renda e oportunidades?',
                                       'alternativas': ['Igualdade de renda',
                                                        'Desigualdade social',
                                                        'Equilíbrio ambiental'],
                                       'correta': 1,
                                       'imagem': 'tema14_pergunta01.jpg',
                                       'imagem_path': 'imagens_perguntas/tema14_pergunta01.jpg',
                                       'legenda': '📚 Sociologia: Desigualdade social. Você acerta as '
                                                  'três?\n'
                                                  '#JuhQuiz #Quiz17 #QuizEscolar #Desafio'},
                                      {'pergunta': 'O que significa mobilidade social?',
                                       'alternativas': ['Mudar de cidade',
                                                        'Trocar de profissão uma vez',
                                                        'Mudar de posição socioeconômica'],
                                       'correta': 2,
                                       'imagem': 'tema14_pergunta02.jpg',
                                       'imagem_path': 'imagens_perguntas/tema14_pergunta02.jpg',
                                       'legenda': '📚 Sociologia: Desigualdade social. Você acerta as '
                                                  'três?\n'
                                                  '#JuhQuiz #Quiz17 #QuizEscolar #Desafio'},
                                      {'pergunta': 'Por que a origem social pode influenciar as '
                                                   'oportunidades de alguém?',
                                       'alternativas': ['Pelo acesso desigual a recursos e educação',
                                                        'Porque todas as famílias têm a mesma renda',
                                                        'Porque a cultura determina todo o futuro'],
                                       'correta': 0,
                                       'imagem': 'tema14_pergunta03.jpg',
                                       'imagem_path': 'imagens_perguntas/tema14_pergunta03.jpg',
                                       'legenda': '📚 Sociologia: Desigualdade social. Você acerta as '
                                                  'três?\n'
                                                  '#JuhQuiz #Quiz17 #QuizEscolar #Desafio'}],
 'Informática — Segurança na internet': [{'pergunta': 'Você recebe um link estranho numa rede social. '
                                                      'Qual é a atitude mais segura?',
                                          'alternativas': ['Abrir para descobrir o conteúdo',
                                                           'Verificar a origem antes de clicar',
                                                           'Compartilhar com outros contatos'],
                                          'correta': 1,
                                          'imagem': 'tema15_pergunta01.jpg',
                                          'imagem_path': 'imagens_perguntas/tema15_pergunta01.jpg',
                                          'legenda': '📚 Informática: Segurança na internet. Você acerta '
                                                     'as três?\n'
                                                     '#JuhQuiz #Quiz17 #QuizEscolar #Desafio'},
                                         {'pergunta': 'O que é um vírus de computador?',
                                          'alternativas': ['Um componente físico da memória',
                                                           'Um defeito do monitor',
                                                           'Um programa malicioso que pode infectar '
                                                           'sistemas'],
                                          'correta': 2,
                                          'imagem': 'tema15_pergunta02.jpg',
                                          'imagem_path': 'imagens_perguntas/tema15_pergunta02.jpg',
                                          'legenda': '📚 Informática: Segurança na internet. Você acerta '
                                                     'as três?\n'
                                                     '#JuhQuiz #Quiz17 #QuizEscolar #Desafio'},
                                         {'pergunta': 'Qual prática ajuda a proteger uma conta contra '
                                                      'invasões?',
                                          'alternativas': ['Ativar autenticação em dois fatores',
                                                           'Repetir a senha em todos os sites',
                                                           'Enviar o código de acesso a amigos'],
                                          'correta': 0,
                                          'imagem': 'tema15_pergunta03.jpg',
                                          'imagem_path': 'imagens_perguntas/tema15_pergunta03.jpg',
                                          'legenda': '📚 Informática: Segurança na internet. Você acerta '
                                                     'as três?\n'
                                                     '#JuhQuiz #Quiz17 #QuizEscolar #Desafio'}]}

LEGENDAS = {'Português — Figuras de linguagem': '📚 Português: Figuras de linguagem. Você acerta as três?\n'
                                     '#JuhQuiz #Quiz17 #QuizEscolar #Desafio',
 'Matemática — Porcentagem': '📚 Matemática: Porcentagem. Você acerta as três?\n'
                             '#JuhQuiz #Quiz17 #QuizEscolar #Desafio',
 'Biologia — Genética': '📚 Biologia: Genética. Você acerta as três?\n'
                        '#JuhQuiz #Quiz17 #QuizEscolar #Desafio',
 'Química — Tabela periódica': '📚 Química: Tabela periódica. Você acerta as três?\n'
                               '#JuhQuiz #Quiz17 #QuizEscolar #Desafio',
 'Física — Eletricidade': '📚 Física: Eletricidade. Você acerta as três?\n'
                          '#JuhQuiz #Quiz17 #QuizEscolar #Desafio',
 'História — Ditadura Militar no Brasil': '📚 História: Ditadura Militar no Brasil. Você acerta as '
                                          'três?\n'
                                          '#JuhQuiz #Quiz17 #QuizEscolar #Desafio',
 'Geografia — Países e capitais': '📚 Geografia: Países e capitais. Você acerta as três?\n'
                                  '#JuhQuiz #Quiz17 #QuizEscolar #Desafio',
 'Ciências — Sistema Solar': '📚 Ciências: Sistema Solar. Você acerta as três?\n'
                             '#JuhQuiz #Quiz17 #QuizEscolar #Desafio',
 'Literatura — Escritores brasileiros': '📚 Literatura: Escritores brasileiros. Você acerta as três?\n'
                                        '#JuhQuiz #Quiz17 #QuizEscolar #Desafio',
 'Inglês — Falsos cognatos': '📚 Inglês: Falsos cognatos. Você acerta as três?\n'
                             '#JuhQuiz #Quiz17 #QuizEscolar #Desafio',
 'Artes — Obras e expressões artísticas': '📚 Artes: Obras e expressões artísticas. Você acerta as '
                                          'três?\n'
                                          '#JuhQuiz #Quiz17 #QuizEscolar #Desafio',
 'Educação Física — Corpo humano em movimento': '📚 Educação Física: Corpo humano em movimento. Você '
                                                'acerta as três?\n'
                                                '#JuhQuiz #Quiz17 #QuizEscolar #Desafio',
 'Filosofia — Grandes filósofos e ideias': '📚 Filosofia: Grandes filósofos e ideias. Você acerta as '
                                           'três?\n'
                                           '#JuhQuiz #Quiz17 #QuizEscolar #Desafio',
 'Sociologia — Desigualdade social': '📚 Sociologia: Desigualdade social. Você acerta as três?\n'
                                     '#JuhQuiz #Quiz17 #QuizEscolar #Desafio',
 'Informática — Segurança na internet': '📚 Informática: Segurança na internet. Você acerta as três?\n'
                                        '#JuhQuiz #Quiz17 #QuizEscolar #Desafio'}
