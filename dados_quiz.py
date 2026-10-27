# -*- coding: utf-8 -*-
# 15 temas, 45 perguntas e 4 hashtags por legenda.
QUIZZES = {'Português: pontuação': [{'pergunta': 'Qual sinal encerra uma pergunta?',
                           'alternativas': ['Ponto final', 'Ponto de interrogação', 'Vírgula'],
                           'correta': 1,
                           'imagem': 'tema01_pergunta01.png',
                           'imagem_path': 'imagens_perguntas/tema01_pergunta01.png',
                           'legenda': 'Teste seus conhecimentos sobre pontuação! Quantas você consegue '
                                      'acertar?\n'
                                      '#JuhQuiz #Quiz #Aprendizado #Desafio'},
                          {'pergunta': 'Qual sinal pode indicar uma pausa breve?',
                           'alternativas': ['Vírgula', 'Interrogação', 'Travessão'],
                           'correta': 0,
                           'imagem': 'tema01_pergunta02.png',
                           'imagem_path': 'imagens_perguntas/tema01_pergunta02.png',
                           'legenda': 'Teste seus conhecimentos sobre pontuação! Quantas você consegue '
                                      'acertar?\n'
                                      '#JuhQuiz #Quiz #Aprendizado #Desafio'},
                          {'pergunta': 'Qual sinal encerra uma frase exclamativa?',
                           'alternativas': ['Dois-pontos', 'Ponto final', 'Ponto de exclamação'],
                           'correta': 2,
                           'imagem': 'tema01_pergunta03.png',
                           'imagem_path': 'imagens_perguntas/tema01_pergunta03.png',
                           'legenda': 'Teste seus conhecimentos sobre pontuação! Quantas você consegue '
                                      'acertar?\n'
                                      '#JuhQuiz #Quiz #Aprendizado #Desafio'}],
 'Matemática: operações': [{'pergunta': 'Quanto é 7 vezes 8?',
                            'alternativas': ['54', '56', '64'],
                            'correta': 1,
                            'imagem': 'tema02_pergunta01.png',
                            'imagem_path': 'imagens_perguntas/tema02_pergunta01.png',
                            'legenda': 'Teste seus conhecimentos sobre operações! Quantas você consegue '
                                       'acertar?\n'
                                       '#JuhQuiz #Quiz #Aprendizado #Desafio'},
                           {'pergunta': 'Quanto é 96 dividido por 3?',
                            'alternativas': ['32', '30', '33'],
                            'correta': 0,
                            'imagem': 'tema02_pergunta02.png',
                            'imagem_path': 'imagens_perguntas/tema02_pergunta02.png',
                            'legenda': 'Teste seus conhecimentos sobre operações! Quantas você consegue '
                                       'acertar?\n'
                                       '#JuhQuiz #Quiz #Aprendizado #Desafio'},
                           {'pergunta': 'Quanto é 125 mais 75?',
                            'alternativas': ['190', '210', '200'],
                            'correta': 2,
                            'imagem': 'tema02_pergunta03.png',
                            'imagem_path': 'imagens_perguntas/tema02_pergunta03.png',
                            'legenda': 'Teste seus conhecimentos sobre operações! Quantas você consegue '
                                       'acertar?\n'
                                       '#JuhQuiz #Quiz #Aprendizado #Desafio'}],
 'Biologia: plantas': [{'pergunta': 'Qual parte da planta absorve água do solo?',
                        'alternativas': ['Raiz', 'Flor', 'Fruto'],
                        'correta': 0,
                        'imagem': 'tema03_pergunta01.png',
                        'imagem_path': 'imagens_perguntas/tema03_pergunta01.png',
                        'legenda': 'Teste seus conhecimentos sobre plantas! Quantas você consegue acertar?\n'
                                   '#JuhQuiz #Quiz #Aprendizado #Desafio'},
                       {'pergunta': 'Qual processo permite que a planta produza alimento usando luz?',
                        'alternativas': ['Digestão', 'Fotossíntese', 'Respiração pulmonar'],
                        'correta': 1,
                        'imagem': 'tema03_pergunta02.png',
                        'imagem_path': 'imagens_perguntas/tema03_pergunta02.png',
                        'legenda': 'Teste seus conhecimentos sobre plantas! Quantas você consegue acertar?\n'
                                   '#JuhQuiz #Quiz #Aprendizado #Desafio'},
                       {'pergunta': 'Qual estrutura pode proteger as sementes?',
                        'alternativas': ['Raiz', 'Caule', 'Fruto'],
                        'correta': 2,
                        'imagem': 'tema03_pergunta03.png',
                        'imagem_path': 'imagens_perguntas/tema03_pergunta03.png',
                        'legenda': 'Teste seus conhecimentos sobre plantas! Quantas você consegue acertar?\n'
                                   '#JuhQuiz #Quiz #Aprendizado #Desafio'}],
 'Química: estados físicos': [{'pergunta': 'Em qual estado a água tem forma própria?',
                               'alternativas': ['Líquido', 'Sólido', 'Gasoso'],
                               'correta': 1,
                               'imagem': 'tema04_pergunta01.png',
                               'imagem_path': 'imagens_perguntas/tema04_pergunta01.png',
                               'legenda': 'Teste seus conhecimentos sobre estados físicos! Quantas você '
                                          'consegue acertar?\n'
                                          '#JuhQuiz #Quiz #Aprendizado #Desafio'},
                              {'pergunta': 'Como se chama a passagem do líquido para o gasoso?',
                               'alternativas': ['Evaporação', 'Solidificação', 'Fusão'],
                               'correta': 0,
                               'imagem': 'tema04_pergunta02.png',
                               'imagem_path': 'imagens_perguntas/tema04_pergunta02.png',
                               'legenda': 'Teste seus conhecimentos sobre estados físicos! Quantas você '
                                          'consegue acertar?\n'
                                          '#JuhQuiz #Quiz #Aprendizado #Desafio'},
                              {'pergunta': 'Como se chama a passagem do sólido para o líquido?',
                               'alternativas': ['Condensação', 'Evaporação', 'Fusão'],
                               'correta': 2,
                               'imagem': 'tema04_pergunta03.png',
                               'imagem_path': 'imagens_perguntas/tema04_pergunta03.png',
                               'legenda': 'Teste seus conhecimentos sobre estados físicos! Quantas você '
                                          'consegue acertar?\n'
                                          '#JuhQuiz #Quiz #Aprendizado #Desafio'}],
 'Física: luz e som': [{'pergunta': 'Qual sentido usamos para perceber sons?',
                        'alternativas': ['Visão', 'Audição', 'Paladar'],
                        'correta': 1,
                        'imagem': 'tema05_pergunta01.png',
                        'imagem_path': 'imagens_perguntas/tema05_pergunta01.png',
                        'legenda': 'Teste seus conhecimentos sobre luz e som! Quantas você consegue '
                                   'acertar?\n'
                                   '#JuhQuiz #Quiz #Aprendizado #Desafio'},
                       {'pergunta': 'Qual objeto produz luz própria?',
                        'alternativas': ['Lua', 'Espelho', 'Sol'],
                        'correta': 2,
                        'imagem': 'tema05_pergunta02.png',
                        'imagem_path': 'imagens_perguntas/tema05_pergunta02.png',
                        'legenda': 'Teste seus conhecimentos sobre luz e som! Quantas você consegue '
                                   'acertar?\n'
                                   '#JuhQuiz #Quiz #Aprendizado #Desafio'},
                       {'pergunta': 'O som consegue se propagar no vácuo?',
                        'alternativas': ['Não', 'Sim, sempre', 'Somente à noite'],
                        'correta': 0,
                        'imagem': 'tema05_pergunta03.png',
                        'imagem_path': 'imagens_perguntas/tema05_pergunta03.png',
                        'legenda': 'Teste seus conhecimentos sobre luz e som! Quantas você consegue '
                                   'acertar?\n'
                                   '#JuhQuiz #Quiz #Aprendizado #Desafio'}],
 'História: Brasil colonial': [{'pergunta': 'Qual foi a primeira capital do Brasil?',
                                'alternativas': ['Rio de Janeiro', 'Salvador', 'Brasília'],
                                'correta': 1,
                                'imagem': 'tema06_pergunta01.png',
                                'imagem_path': 'imagens_perguntas/tema06_pergunta01.png',
                                'legenda': 'Teste seus conhecimentos sobre Brasil colonial! Quantas você '
                                           'consegue acertar?\n'
                                           '#JuhQuiz #Quiz #Aprendizado #Desafio'},
                               {'pergunta': 'Qual produto foi muito cultivado nos engenhos coloniais?',
                                'alternativas': ['Cana-de-açúcar', 'Trigo', 'Café'],
                                'correta': 0,
                                'imagem': 'tema06_pergunta02.png',
                                'imagem_path': 'imagens_perguntas/tema06_pergunta02.png',
                                'legenda': 'Teste seus conhecimentos sobre Brasil colonial! Quantas você '
                                           'consegue acertar?\n'
                                           '#JuhQuiz #Quiz #Aprendizado #Desafio'},
                               {'pergunta': 'Quem vivia no território brasileiro antes da colonização '
                                            'portuguesa?',
                                'alternativas': ['Somente europeus',
                                                 'Somente africanos',
                                                 'Diversos povos indígenas'],
                                'correta': 2,
                                'imagem': 'tema06_pergunta03.png',
                                'imagem_path': 'imagens_perguntas/tema06_pergunta03.png',
                                'legenda': 'Teste seus conhecimentos sobre Brasil colonial! Quantas você '
                                           'consegue acertar?\n'
                                           '#JuhQuiz #Quiz #Aprendizado #Desafio'}],
 'Geografia: clima e tempo': [{'pergunta': 'O que descreve as condições atmosféricas de um momento?',
                               'alternativas': ['Clima', 'Tempo', 'Relevo'],
                               'correta': 1,
                               'imagem': 'tema07_pergunta01.png',
                               'imagem_path': 'imagens_perguntas/tema07_pergunta01.png',
                               'legenda': 'Teste seus conhecimentos sobre clima e tempo! Quantas você '
                                          'consegue acertar?\n'
                                          '#JuhQuiz #Quiz #Aprendizado #Desafio'},
                              {'pergunta': 'Qual instrumento mede a temperatura do ar?',
                               'alternativas': ['Termômetro', 'Bússola', 'Régua'],
                               'correta': 0,
                               'imagem': 'tema07_pergunta02.png',
                               'imagem_path': 'imagens_perguntas/tema07_pergunta02.png',
                               'legenda': 'Teste seus conhecimentos sobre clima e tempo! Quantas você '
                                          'consegue acertar?\n'
                                          '#JuhQuiz #Quiz #Aprendizado #Desafio'},
                              {'pergunta': 'O que é uma previsão do tempo?',
                               'alternativas': ['Um mapa de estradas',
                                                'Uma lista de cidades',
                                                'Uma estimativa das condições atmosféricas'],
                               'correta': 2,
                               'imagem': 'tema07_pergunta03.png',
                               'imagem_path': 'imagens_perguntas/tema07_pergunta03.png',
                               'legenda': 'Teste seus conhecimentos sobre clima e tempo! Quantas você '
                                          'consegue acertar?\n'
                                          '#JuhQuiz #Quiz #Aprendizado #Desafio'}],
 'Ciências: alimentação': [{'pergunta': 'Qual nutriente é uma fonte importante de energia?',
                            'alternativas': ['Carboidrato', 'Água', 'Mineral'],
                            'correta': 0,
                            'imagem': 'tema08_pergunta01.png',
                            'imagem_path': 'imagens_perguntas/tema08_pergunta01.png',
                            'legenda': 'Teste seus conhecimentos sobre alimentação! Quantas você consegue '
                                       'acertar?\n'
                                       '#JuhQuiz #Quiz #Aprendizado #Desafio'},
                           {'pergunta': 'Qual hábito ajuda na hidratação?',
                            'alternativas': ['Evitar líquidos',
                                             'Beber água regularmente',
                                             'Comer apenas doces'],
                            'correta': 1,
                            'imagem': 'tema08_pergunta02.png',
                            'imagem_path': 'imagens_perguntas/tema08_pergunta02.png',
                            'legenda': 'Teste seus conhecimentos sobre alimentação! Quantas você consegue '
                                       'acertar?\n'
                                       '#JuhQuiz #Quiz #Aprendizado #Desafio'},
                           {'pergunta': 'Qual prática ajuda na higiene dos alimentos?',
                            'alternativas': ['Deixar expostos',
                                             'Usar utensílios sujos',
                                             'Lavar frutas e verduras'],
                            'correta': 2,
                            'imagem': 'tema08_pergunta03.png',
                            'imagem_path': 'imagens_perguntas/tema08_pergunta03.png',
                            'legenda': 'Teste seus conhecimentos sobre alimentação! Quantas você consegue '
                                       'acertar?\n'
                                       '#JuhQuiz #Quiz #Aprendizado #Desafio'}],
 'Literatura: narrativas': [{'pergunta': 'Quem conta a história em um texto narrativo?',
                             'alternativas': ['Narrador', 'Leitor', 'Ilustrador'],
                             'correta': 0,
                             'imagem': 'tema09_pergunta01.png',
                             'imagem_path': 'imagens_perguntas/tema09_pergunta01.png',
                             'legenda': 'Teste seus conhecimentos sobre narrativas! Quantas você consegue '
                                        'acertar?\n'
                                        '#JuhQuiz #Quiz #Aprendizado #Desafio'},
                            {'pergunta': 'Como se chama o lugar onde a história acontece?',
                             'alternativas': ['Título', 'Espaço', 'Rima'],
                             'correta': 1,
                             'imagem': 'tema09_pergunta02.png',
                             'imagem_path': 'imagens_perguntas/tema09_pergunta02.png',
                             'legenda': 'Teste seus conhecimentos sobre narrativas! Quantas você consegue '
                                        'acertar?\n'
                                        '#JuhQuiz #Quiz #Aprendizado #Desafio'},
                            {'pergunta': 'Como se chama o conjunto de acontecimentos de uma história?',
                             'alternativas': ['Capa', 'Autor', 'Enredo'],
                             'correta': 2,
                             'imagem': 'tema09_pergunta03.png',
                             'imagem_path': 'imagens_perguntas/tema09_pergunta03.png',
                             'legenda': 'Teste seus conhecimentos sobre narrativas! Quantas você consegue '
                                        'acertar?\n'
                                        '#JuhQuiz #Quiz #Aprendizado #Desafio'}],
 'Inglês: cotidiano': [{'pergunta': 'Como se diz gato em inglês?',
                        'alternativas': ['Dog', 'Cat', 'Bird'],
                        'correta': 1,
                        'imagem': 'tema10_pergunta01.png',
                        'imagem_path': 'imagens_perguntas/tema10_pergunta01.png',
                        'legenda': 'Teste seus conhecimentos sobre cotidiano! Quantas você consegue '
                                   'acertar?\n'
                                   '#JuhQuiz #Quiz #Aprendizado #Desafio'},
                       {'pergunta': 'O que significa book em português?',
                        'alternativas': ['Livro', 'Mesa', 'Escola'],
                        'correta': 0,
                        'imagem': 'tema10_pergunta02.png',
                        'imagem_path': 'imagens_perguntas/tema10_pergunta02.png',
                        'legenda': 'Teste seus conhecimentos sobre cotidiano! Quantas você consegue '
                                   'acertar?\n'
                                   '#JuhQuiz #Quiz #Aprendizado #Desafio'},
                       {'pergunta': 'Como se diz água em inglês?',
                        'alternativas': ['Milk', 'Bread', 'Water'],
                        'correta': 2,
                        'imagem': 'tema10_pergunta03.png',
                        'imagem_path': 'imagens_perguntas/tema10_pergunta03.png',
                        'legenda': 'Teste seus conhecimentos sobre cotidiano! Quantas você consegue '
                                   'acertar?\n'
                                   '#JuhQuiz #Quiz #Aprendizado #Desafio'}],
 'Artes: música': [{'pergunta': 'Qual elemento da música está relacionado à duração dos sons?',
                    'alternativas': ['Cor', 'Ritmo', 'Textura'],
                    'correta': 1,
                    'imagem': 'tema11_pergunta01.png',
                    'imagem_path': 'imagens_perguntas/tema11_pergunta01.png',
                    'legenda': 'Teste seus conhecimentos sobre música! Quantas você consegue acertar?\n'
                               '#JuhQuiz #Quiz #Aprendizado #Desafio'},
                   {'pergunta': 'Qual instrumento possui teclas?',
                    'alternativas': ['Piano', 'Tambor', 'Violão'],
                    'correta': 0,
                    'imagem': 'tema11_pergunta02.png',
                    'imagem_path': 'imagens_perguntas/tema11_pergunta02.png',
                    'legenda': 'Teste seus conhecimentos sobre música! Quantas você consegue acertar?\n'
                               '#JuhQuiz #Quiz #Aprendizado #Desafio'},
                   {'pergunta': 'Como se chama a pessoa que compõe uma música?',
                    'alternativas': ['Pintor', 'Atleta', 'Compositor'],
                    'correta': 2,
                    'imagem': 'tema11_pergunta03.png',
                    'imagem_path': 'imagens_perguntas/tema11_pergunta03.png',
                    'legenda': 'Teste seus conhecimentos sobre música! Quantas você consegue acertar?\n'
                               '#JuhQuiz #Quiz #Aprendizado #Desafio'}],
 'Educação física: esportes': [{'pergunta': 'Em qual esporte se usa uma cesta?',
                                'alternativas': ['Futebol', 'Basquete', 'Natação'],
                                'correta': 1,
                                'imagem': 'tema12_pergunta01.png',
                                'imagem_path': 'imagens_perguntas/tema12_pergunta01.png',
                                'legenda': 'Teste seus conhecimentos sobre esportes! Quantas você consegue '
                                           'acertar?\n'
                                           '#JuhQuiz #Quiz #Aprendizado #Desafio'},
                               {'pergunta': 'Qual atividade acontece na água?',
                                'alternativas': ['Natação', 'Corrida', 'Ciclismo'],
                                'correta': 0,
                                'imagem': 'tema12_pergunta02.png',
                                'imagem_path': 'imagens_perguntas/tema12_pergunta02.png',
                                'legenda': 'Teste seus conhecimentos sobre esportes! Quantas você consegue '
                                           'acertar?\n'
                                           '#JuhQuiz #Quiz #Aprendizado #Desafio'},
                               {'pergunta': 'Qual hábito é importante antes de exercícios?',
                                'alternativas': ['Ignorar o corpo',
                                                 'Ficar sem água',
                                                 'Preparar o corpo com aquecimento'],
                                'correta': 2,
                                'imagem': 'tema12_pergunta03.png',
                                'imagem_path': 'imagens_perguntas/tema12_pergunta03.png',
                                'legenda': 'Teste seus conhecimentos sobre esportes! Quantas você consegue '
                                           'acertar?\n'
                                           '#JuhQuiz #Quiz #Aprendizado #Desafio'}],
 'Filosofia: convivência': [{'pergunta': 'O que significa empatia?',
                             'alternativas': ['Ignorar os outros',
                                              'Buscar compreender o outro',
                                              'Impor uma opinião'],
                             'correta': 1,
                             'imagem': 'tema13_pergunta01.png',
                             'imagem_path': 'imagens_perguntas/tema13_pergunta01.png',
                             'legenda': 'Teste seus conhecimentos sobre convivência! Quantas você consegue '
                                        'acertar?\n'
                                        '#JuhQuiz #Quiz #Aprendizado #Desafio'},
                            {'pergunta': 'Qual atitude favorece o diálogo?',
                             'alternativas': ['Ouvir com respeito', 'Interromper sempre', 'Ofender'],
                             'correta': 0,
                             'imagem': 'tema13_pergunta02.png',
                             'imagem_path': 'imagens_perguntas/tema13_pergunta02.png',
                             'legenda': 'Teste seus conhecimentos sobre convivência! Quantas você consegue '
                                        'acertar?\n'
                                        '#JuhQuiz #Quiz #Aprendizado #Desafio'},
                            {'pergunta': 'O que é uma escolha ética?',
                             'alternativas': ['Escolha feita sem pensar',
                                              'Escolha sempre mais rápida',
                                              'Escolha que considera consequências e respeito'],
                             'correta': 2,
                             'imagem': 'tema13_pergunta03.png',
                             'imagem_path': 'imagens_perguntas/tema13_pergunta03.png',
                             'legenda': 'Teste seus conhecimentos sobre convivência! Quantas você consegue '
                                        'acertar?\n'
                                        '#JuhQuiz #Quiz #Aprendizado #Desafio'}],
 'Sociologia: sociedade': [{'pergunta': 'O que é cultura?',
                            'alternativas': ['Somente comidas',
                                             'Hábitos e conhecimentos compartilhados',
                                             'Apenas roupas'],
                            'correta': 1,
                            'imagem': 'tema14_pergunta01.png',
                            'imagem_path': 'imagens_perguntas/tema14_pergunta01.png',
                            'legenda': 'Teste seus conhecimentos sobre sociedade! Quantas você consegue '
                                       'acertar?\n'
                                       '#JuhQuiz #Quiz #Aprendizado #Desafio'},
                           {'pergunta': 'Qual atitude respeita a diversidade?',
                            'alternativas': ['Valorizar diferenças', 'Zombar de costumes', 'Excluir pessoas'],
                            'correta': 0,
                            'imagem': 'tema14_pergunta02.png',
                            'imagem_path': 'imagens_perguntas/tema14_pergunta02.png',
                            'legenda': 'Teste seus conhecimentos sobre sociedade! Quantas você consegue '
                                       'acertar?\n'
                                       '#JuhQuiz #Quiz #Aprendizado #Desafio'},
                           {'pergunta': 'O que é convivência social?',
                            'alternativas': ['Viver sem contato',
                                             'Evitar todas as regras',
                                             'Relacionar-se com outras pessoas'],
                            'correta': 2,
                            'imagem': 'tema14_pergunta03.png',
                            'imagem_path': 'imagens_perguntas/tema14_pergunta03.png',
                            'legenda': 'Teste seus conhecimentos sobre sociedade! Quantas você consegue '
                                       'acertar?\n'
                                       '#JuhQuiz #Quiz #Aprendizado #Desafio'}],
 'Informática: segurança digital': [{'pergunta': 'Uma senha forte deve ter:',
                                     'alternativas': ['Só o nome',
                                                      'Combinação variada de caracteres',
                                                      'A data de nascimento'],
                                     'correta': 1,
                                     'imagem': 'tema15_pergunta01.png',
                                     'imagem_path': 'imagens_perguntas/tema15_pergunta01.png',
                                     'legenda': 'Teste seus conhecimentos sobre segurança digital! Quantas '
                                                'você consegue acertar?\n'
                                                '#JuhQuiz #Quiz #Aprendizado #Desafio'},
                                    {'pergunta': 'O que fazer diante de um link suspeito?',
                                     'alternativas': ['Verificar antes de clicar',
                                                      'Compartilhar imediatamente',
                                                      'Informar a senha'],
                                     'correta': 0,
                                     'imagem': 'tema15_pergunta02.png',
                                     'imagem_path': 'imagens_perguntas/tema15_pergunta02.png',
                                     'legenda': 'Teste seus conhecimentos sobre segurança digital! Quantas '
                                                'você consegue acertar?\n'
                                                '#JuhQuiz #Quiz #Aprendizado #Desafio'},
                                    {'pergunta': 'Para que serve a autenticação em duas etapas?',
                                     'alternativas': ['Apagar arquivos',
                                                      'Aumentar o volume',
                                                      'Adicionar uma camada de segurança'],
                                     'correta': 2,
                                     'imagem': 'tema15_pergunta03.png',
                                     'imagem_path': 'imagens_perguntas/tema15_pergunta03.png',
                                     'legenda': 'Teste seus conhecimentos sobre segurança digital! Quantas '
                                                'você consegue acertar?\n'
                                                '#JuhQuiz #Quiz #Aprendizado #Desafio'}]}

LEGENDAS = {'Português: pontuação': 'Teste seus conhecimentos sobre pontuação! Quantas você consegue acertar?\n'
                         '#JuhQuiz #Quiz #Aprendizado #Desafio',
 'Matemática: operações': 'Teste seus conhecimentos sobre operações! Quantas você consegue acertar?\n'
                          '#JuhQuiz #Quiz #Aprendizado #Desafio',
 'Biologia: plantas': 'Teste seus conhecimentos sobre plantas! Quantas você consegue acertar?\n'
                      '#JuhQuiz #Quiz #Aprendizado #Desafio',
 'Química: estados físicos': 'Teste seus conhecimentos sobre estados físicos! Quantas você consegue '
                             'acertar?\n'
                             '#JuhQuiz #Quiz #Aprendizado #Desafio',
 'Física: luz e som': 'Teste seus conhecimentos sobre luz e som! Quantas você consegue acertar?\n'
                      '#JuhQuiz #Quiz #Aprendizado #Desafio',
 'História: Brasil colonial': 'Teste seus conhecimentos sobre Brasil colonial! Quantas você consegue '
                              'acertar?\n'
                              '#JuhQuiz #Quiz #Aprendizado #Desafio',
 'Geografia: clima e tempo': 'Teste seus conhecimentos sobre clima e tempo! Quantas você consegue acertar?\n'
                             '#JuhQuiz #Quiz #Aprendizado #Desafio',
 'Ciências: alimentação': 'Teste seus conhecimentos sobre alimentação! Quantas você consegue acertar?\n'
                          '#JuhQuiz #Quiz #Aprendizado #Desafio',
 'Literatura: narrativas': 'Teste seus conhecimentos sobre narrativas! Quantas você consegue acertar?\n'
                           '#JuhQuiz #Quiz #Aprendizado #Desafio',
 'Inglês: cotidiano': 'Teste seus conhecimentos sobre cotidiano! Quantas você consegue acertar?\n'
                      '#JuhQuiz #Quiz #Aprendizado #Desafio',
 'Artes: música': 'Teste seus conhecimentos sobre música! Quantas você consegue acertar?\n'
                  '#JuhQuiz #Quiz #Aprendizado #Desafio',
 'Educação física: esportes': 'Teste seus conhecimentos sobre esportes! Quantas você consegue acertar?\n'
                              '#JuhQuiz #Quiz #Aprendizado #Desafio',
 'Filosofia: convivência': 'Teste seus conhecimentos sobre convivência! Quantas você consegue acertar?\n'
                           '#JuhQuiz #Quiz #Aprendizado #Desafio',
 'Sociologia: sociedade': 'Teste seus conhecimentos sobre sociedade! Quantas você consegue acertar?\n'
                          '#JuhQuiz #Quiz #Aprendizado #Desafio',
 'Informática: segurança digital': 'Teste seus conhecimentos sobre segurança digital! Quantas você consegue '
                                   'acertar?\n'
                                   '#JuhQuiz #Quiz #Aprendizado #Desafio'}
