# Juh Quiz — Caderno

Gerador de vídeos verticais de quiz com visual de folha branca, marca Juh Quiz e cinco cores que se alternam automaticamente.

## Gerar no GitHub

1. Abra **Actions** neste repositório.
2. Selecione **Gerar Juh Quiz - Caderno** e clique em **Run workflow**.
3. O GitHub gera os vídeos e as legendas; não é preciso escolher a cor.
4. Ao terminar, abra a execução e baixe o artefato **JUH-QUIZ-CADERNO**.

A cada três vídeos a folha muda de cor, seguindo a sequência verde, azul, coral, violeta e amarelo. Depois do quinto grupo, o ciclo recomeça. Cada tema em `dados_quiz.py` gera um vídeo com até cinco perguntas. Depois de cada resposta, a folha sobe e a pergunta seguinte entra. A imagem opcional aparece ao lado da pergunta: adicione-a à pasta `imagens_perguntas/` e informe `"imagem": "nome-do-arquivo.png"`.

O vídeo usa a voz `pt-BR-AntonioNeural` em +10%, toca bipes na contagem 3, 2, 1 e lê/destaca a alternativa correta.

## Perguntas em lote

Em `dados_quiz.py`, cada pergunta usa três alternativas e o índice da resposta correta começa em zero:

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

`correta: 0` marca a primeira alternativa; `1`, a segunda; `2`, a terceira. Cada lote de perguntas deve estar salvo em `dados_quiz.py` antes de iniciar a Action.

## Google Drive

O envio de MP4 e TXT usa o mesmo secret do Quiz-13: `RCLONE_DRIVE_TOKEN`. Cadastre no Quiz-17 o JSON completo do token rclone do Drive. Não precisa criar variável de pasta nem configurar outra chave.

Enquanto a chave não estiver cadastrada, a cópia no Drive é pulada e os vídeos continuam disponíveis como artefato do GitHub. Depois de configurar `RCLONE_DRIVE_TOKEN`, cada execução salva os arquivos em `saida/Juh-Quiz-17/caderno/execucao-ID/`, na pasta-base do Drive já usada pelo Quiz-13.
