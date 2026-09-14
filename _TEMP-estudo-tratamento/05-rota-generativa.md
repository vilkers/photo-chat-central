# Rota generativa — estudos com modelos, não upscale

Decisão do usuário: o estudo é **gerado** pelos modelos de imagem com as referências,
não construído por upscale/skin enhancer/relight. O pipeline do arquivo `02` fica
arquivado como rota alternativa.

## Nomenclatura (corrigida)

| Pedido | Nome real no Magnific | Slug |
|---|---|---|
| "nano banana" | Google Nano Banana Pro | `imagen-nano-banana-2` |
| "seedance" | Seedream 5 Pro (Seedance é o modelo de **vídeo**) | `seedream-5-pro` |
| "gpt image" | GPT 2 | `gpt-2` |

## Referências — as do usuário mandam

O usuário subiu 7 referências próprias e indicou quais são, por eliminação numa
captura da grade de Uploads: tudo menos a foto-base dele e uma imagem roxa antiga.
A grade do app lista do mais recente para o mais antigo, linha a linha, e a imagem
roxa ser um upload de 3/9 (e não do lote das 02:55) confirmou o alinhamento.

**Foto-base:** o tile central da grade (upload de 02:55:48).

As 7 refs do usuário são retrato de campanha em luz dura — cor saturada mas
controlada, sombra densa com cor dentro, pele real com brilho, fundo presente e
subordinado. É uma direção diferente da que eu tinha puxado do Savee (âmbar-oliva
dessaturado) e mais próxima da foto original. **A direção do usuário prevalece.**

As 9 referências que eu havia importado da CDN do Savee continuam na biblioteca e
não foram usadas em nenhuma geração. São descartáveis.

## Custos simulados (exatos, por imagem, 3:4, com referência)

| Modelo | Config | Créditos |
|---|---|---|
| Nano Banana Pro | 2k | **75** |
| Seedream 5 Pro | 2k | **100** |
| GPT 2 | 1k / medium | **100** |
| GPT 2 | 2k / high | **650** ← fora de cogitação |

GPT 2 entra só em 1k/medium, e como controle. O próprio catálogo o recomenda para
texto, infográfico e layout — explicitamente **não** para fotografia fotorrealista.
A 650 créditos a imagem, seria 30% da carteira para o modelo menos indicado à tarefa.

## O que rodou (2026-09-14)

Prompt mínimo, deliberado: trava identidade, expressão, roupa, pose, enquadramento e
cena, e entrega **todo** o tratamento para a referência de estilo. "Siga as refs" —
o texto não disputa com a imagem.

```
Keep the man in the first image exactly as he is: same face, same facial features,
same beard, same expression, same eye direction, same cap, same t-shirt, same pose,
same framing, same background scene. Change nothing about who he is or what is in
the frame. Apply the photographic treatment of the style reference: its colour
grade, contrast, light quality, skin rendering, grain and overall finish.
No altered facial features, no beauty retouch, no smoothing, no illustration, no CGI.
```

Todas 2k, 3:4, 1 imagem, foto-base como referência de imagem + 1 ref como estilo.

| # | Referência de estilo | Modelo | Prompt | Créditos | Creation |
|---|---|---|---|---|---|
| A1 | garoto camisa azul / céu | Nano Banana Pro | com direção escrita | 75 | `nVIzlIzYQD` |
| A2 | garoto camisa azul / céu | Seedream 5 Pro | com direção escrita | 100 | `EblCWSMuuO` |
| B1 | capuz laranja / noturno | Nano Banana Pro | mínimo | 75 | `XmHdN6gBfo` |
| B2 | veludo azul / caminhão | Nano Banana Pro | mínimo | 75 | `1l4kX8lr4r` |
| B3 | FILA verde / interior | Nano Banana Pro | mínimo | 75 | `KLy5eomkqp` |
| B4 | perfil dourado / blur | Nano Banana Pro | mínimo | 75 | `N2V9bxc6D9` |
| B5 | Paris / vitrine | Nano Banana Pro | mínimo | 75 | `LwijICBswO` |
| B6 | viaduto noturno | Nano Banana Pro | mínimo | 75 | `rg91Bfjxtc` |

**Total: 625 créditos.** Saldo após: ~1.527.

### Ressalvas registradas

- **A rodada A não é A/B limpo de prompt.** A1 e A2 usaram prompt com direção escrita;
  B1–B6 usaram prompt mínimo. Comparar entre os grupos mistura modelo e prompt.
  Falta rodar a ref do céu azul com prompt mínimo (75 cr) para fechar o A/B.
- **As duas refs noturnas** (B1, B6) obrigam o modelo a reacender uma foto de meio-dia.
  Relight generativo redesenha sombra por cima de feição, então o drift de identidade
  nesses dois tende a ser maior por construção, não por falha do modelo.
- **Nenhum resultado foi avaliado por mim.** O CDN de leitura está bloqueado nesta
  sessão; a inspeção visual é do usuário. Nada foi julgado sem ser visto.

### Critério de aprovação

Reprova, por melhor que esteja: sobrancelha, lábio, orelha, piercing ou pupila
alterados; pele mais lisa que a referência; grão só na pele; céu de volta ao ciano.

## Risco assumido

Reconstrução generativa sobre rosto real tem drift de identidade por natureza — o
modelo reconstrói a partir do entendimento dele de rosto, e a semelhança escorre
primeiro em orelha, dente e desenho do olho. O critério acima existe para medir isso.
Decisão do usuário, com o risco declarado.

---

# Rodada 2 — manipulação liberada, 5 versões analógicas

Escopo ampliado pelo usuário: pode redesenhar luz, cor e textura, ajustar o acting e
limpar o fundo. A identidade continua travada (rosto, barba, piercing, brinco, boné,
camiseta); o que ficou livre foi a direção da cena.

Todas Nano Banana Pro, 2k, 3:4, 1 imagem, foto-base como referência de imagem + 1 ref
do usuário como estilo. Todas com a mesma limpeza de fundo: **sem outras pessoas,
sem fiação aérea**, rua simplificada e subordinada ao sujeito.

| V | Direção | Acting | Luz | Filme | Ref de estilo | Creation |
|---|---|---|---|---|---|---|
| V1 | sol duro frontal | queixo baixo, olhar firme na lente | sol de meio-dia frente-esquerda, céu como fill | Portra 400 | camisa azul / céu | `DoEM4sapcl` |
| V2 | contraluz de fim de tarde | 3/4, olhar fora de quadro, queixo alto | rim quente por trás do ombro direito, fill frio do céu | Ektachrome | perfil dourado | `JNn7QmhOq4` |
| V3 | sombra aberta, casting frame | frontal, sério, cabeça nivelada, imóvel | open shade suave pela esquerda, sem sol direto | Pro 400H | veludo azul | `4R0P5AX9Aa` |
| V4 | flash direto de dia | pego no meio do gesto, lábios entreabertos | flash on-camera, sombra recortada atrás | Gold 200 puxado | FILA verde | `Sy2gfv2Ub8` |
| V5 | luz rasante lateral | cabeça à esquerda, olhar voltando de lado | raking light baixo, metade do rosto em sombra densa | Portra 800 puxado | capuz laranja | `3zpirrNREY` |

**Variável deliberada:** V2 e V3 pedem render "como se fosse 85mm". É a tentativa de
corrigir a distorção de selfie — o maior afastamento entre a foto original e as refs,
que são todas de lente longa. V1, V4 e V5 ficaram na geometria original, então o par
V1 × V3 mostra o efeito isolado da lente.

**Erro e correção:** a primeira V3 (`hurmzR1vqL`) foi disparada sem a foto-base — a
referência entrou como imagem principal, então o resultado não é o sujeito. 75
créditos perdidos. Refeita corretamente em `4R0P5AX9Aa`; descartar a primeira.

**Custo da rodada 2: 450 créditos** (375 + 75 da refação). Saldo após: ~1.077.

**Nenhuma versão foi avaliada por mim** — CDN bloqueado nesta sessão.
