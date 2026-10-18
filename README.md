# Juh Quiz — Caderno

Gerador de vídeos verticais de quiz com visual de folha branca e cinco cores.

## Gerar no GitHub

1. Abra **Actions** neste repositório.
2. Selecione **Gerar Juh Quiz - Caderno**.
3. Clique em **Run workflow** e escolha a cor: verde, azul, coral, violeta ou amarelo.
4. Ao terminar, abra a execução e baixe o artefato JUH-QUIZ-CADERNO.

Cada tema em dados_quiz.py gera um vídeo com até cinco perguntas. Depois da resposta, a folha sobe e a pergunta seguinte entra. A imagem opcional aparece ao lado da pergunta: adicione-a à pasta imagens_perguntas/ e informe "imagem": "nome-do-arquivo.png".

O vídeo usa a voz pt-BR-AntonioNeural em +10%, toca bipes na contagem 3, 2, 1 e lê/destaca a alternativa correta.

## Perguntas em lote

Em dados_quiz.py, cada pergunta usa três alternativas e o índice da resposta correta começa em zero:

```python
QUIZZES = {
    "Cultura geral": [
        {
            "pergunta": "Qual alimento causa sono?",
            "alternativas": ["Chocolate", "Café", "Maracujá"],
            "correta": 2
        }
    ]
}
```

correta: 0 marca a primeira alternativa; 1, a segunda; 2, a terceira. Cada lote de perguntas deve estar salvo em dados_quiz.py antes de iniciar a Action.

## Cópia opcional no Google Drive

O workflow guarda os vídeos como artefato do GitHub. Para ativar a cópia no Drive depois, cadastre:

- Secret GOOGLE_DRIVE_SERVICE_ACCOUNT_JSON: JSON da conta de serviço autorizada a gravar na pasta do Drive.
- Variable GOOGLE_DRIVE_FOLDER_ID: ID da pasta de destino.

Sem esses valores, a etapa do Drive é ignorada e o quiz continua sendo gerado normalmente. Não é preciso cadastrar nenhuma chave agora.
