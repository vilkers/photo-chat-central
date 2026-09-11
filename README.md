# KV Lab — Photo Chat Central

O trabalho acontece na conversa com o assistente: ele interpreta as referências, coordena agentes quando úteis, constrói os prompts, usa o Magnific conectado e inspeciona os resultados. O repositório é a memória persistente desse processo; não substitui o julgamento visual do assistente.

## Fluxo

1. Receber a direção de casting, acting, expressões, acessórios e marca.
2. Receber e analisar cada referência fotográfica, preservando sua intenção de luz, exposição, textura e composição.
3. Cruzar as duas etapas e executar a geração pelo MCP conectado na conversa.
4. Inspecionar os resultados com os papéis de diretor de arte, fotógrafo e retoucher, quando úteis.
5. Registrar prompt, referências, decisões e feedback por escopo; consultar o histórico relevante na próxima rodada.

O histórico não treina o modelo. Os agentes só têm uma avaliação registrada quando realmente inspecionam as imagens. Aprovação interna não substitui a decisão do usuário.

## Conteúdo publicado

- `AGENTS.md`: instruções de operação na conversa.
- `src/workflow.py`: utilitário opcional de preparação de pedidos e registro de feedback. Não analisa imagens nem faz chamadas pagas.
- `rounds/template.json`: ficha vazia para documentar uma rodada.
- `feedback.jsonl`: histórico inicialmente vazio.

O usuário não precisa executar Python. O assistente pode usar o utilitário durante o trabalho. Python 3.10+, sem dependências externas; ajuda: `python3 src/workflow.py --help`.

## Materiais pendentes

A revisão automática bloqueou a publicação das imagens e de seus metadados neste repositório público. Os materiais específicos da campanha aguardam autorização explícita para divulgação pública ou um destino privado autorizado. O pacote completo permanece com o usuário.

Não é necessário desenvolver uma interface ou um backend autônomo para começar a trabalhar: o ambiente de operação é esta conversa, com as conexões e ferramentas disponíveis em cada sessão.
