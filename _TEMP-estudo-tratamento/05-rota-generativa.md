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

## Referências importadas por mim (identidade conhecida)

Importadas direto da CDN do Savee trocando `.avif` por `.jpg` — o Magnific busca pelo
servidor dele, então o bloqueio de rede desta sessão não atrapalha. São duplicatas das
que o usuário subiu; as dele podem ser apagadas depois, ou as minhas.

| Ref | Papel | Creation |
|---|---|---|
| A1 | pele em sol duro (olho/sardas) — ref-mestre de textura | `WDmYlZucXe` |
| A2 | specular de pele controlado (pescoço/ombro) | `s73LIOAl8e` |
| A3 | curva de contraste, preto quente (Santoni) | `XmHd9aeBfo` |
| A4 | temperatura quente + grão (Nora Hollstein) | `Lwij8P3swO` |
| B1 | paleta âmbar-oliva de campanha (Wales Bonner) | `3zpi5JTREY` |
| B2 | céu azul cobalto denso | `jU6xBqlLD0` |
| C1 | rua urbana em grade cinema (Paris) | `lJRstNrgv9` |
| C2 | separação figura/fundo (TJ Park) | `cphWStR0eP` |
| C3 | grão grosso e preto com cor (Jack Davison) | `8a5oi5lIrU` |

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

## Rodada 1 — comparativo de modelos

Mesmo prompt, mesmas referências, uma imagem por modelo. 3:4 (o original é 1932×2576).

- Referência de **imagem**: a foto-base (âncora de identidade e enquadramento)
- Referência de **estilo**: A1 (pele em sol duro)

**Custo: 275 créditos.**

### Prompt único (idêntico nos três)

```
Rework this photograph of the man in the reference image. Keep his face, beard,
cap, t-shirt, pose and framing exactly as they are: same person, same facial
features, same expression, same crop, same eye direction. Change only the
photographic treatment. Replace the smartphone HDR look with a cinematic daylight
grade: dense blacks with a slight olive cast, long highlight roll-off, warm real
skin with visible pores and fine hair, deep cobalt sky with lower saturation,
background street muted and darker than the subject, white cotton t-shirt showing
woven fabric texture instead of clipped white. Fine even film grain across the
entire frame, including the sky. Shot on 35mm film, campaign photography finish.
No smoothing, no plastic skin, no altered facial features, no beauty retouch,
no teal and orange LUT, no illustration, no CGI look.
```

### Critério de aprovação

Reprova, por melhor que esteja: sobrancelha, lábio, orelha, piercing ou pupila
alterados; pele mais lisa que a A1; grão só na pele; céu de volta ao ciano.

## Rodada 2 — só no modelo vencedor

Três direções de tratamento, uma referência de estilo cada (nunca empilhar):
**A1** textura de pele · **B1** paleta de campanha · **C2** separação de planos.
~225–300 créditos.

## Risco assumido

Reconstrução generativa sobre rosto real tem drift de identidade por natureza — o
modelo reconstrói a partir do entendimento dele de rosto, e a semelhança escorre
primeiro em orelha, dente e desenho do olho. O critério de aprovação acima existe
justamente para medir isso. Decisão tomada pelo usuário, com o risco declarado.
