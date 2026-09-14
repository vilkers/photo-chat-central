# Prompts prontos

Colar como está. Nenhum precisa de interpretação extra.

---

## 1 · Magnific — `images_upscale` modo creative (campo `prompt`)

Só usado se a rota precision não entregar textura. O prompt do creative é coleira,
não criação: ele descreve o que já existe para o modelo não inventar.

```
Photograph of a bearded man in a grey corduroy cap and white cotton t-shirt,
outdoors in direct midday sun, urban street behind him. Natural skin with visible
pores, freckles and fine beard hairs. Soft highlight roll-off on nose and cheek,
dense shadow under the cap brim. Fine even film grain across the whole frame,
including the sky. Cotton t-shirt shows woven fabric texture. No smoothing,
no plastic skin, no added makeup, no altered facial features, no HDR halo,
no digital sharpening halo.
```

---

## 2 · Nano Banana Pro / Seedream 5 Pro — reconstrução **só do fundo**

Usar com máscara cobrindo apenas o fundo (rosto, boné e camiseta protegidos).
Nunca rodar sem máscara.

```
Replace only the background behind the subject: a simplified Brazilian city street
in late afternoon light, shot on a 85mm lens at f/2 so the background is softly
compressed and out of focus. Keep the same direction of light and the same
colour temperature as the foreground. Muted cobalt sky, no cyan. Remove overhead
power lines and background people. Keep building shapes and the tree, desaturated
and darker than the subject. Photographic, grainy, no illustration, no CGI look.
```

---

## 3 · Freepik Spaces — estudo de tratamento

O Spaces não tem peso de referência: toda imagem entra com a mesma força.
Rodar **uma intenção por vez**, nunca os três blocos juntos.

### Rodada A — pele e contraste
Subir: sua foto (referência de imagem) + A1 (`savee.com/i/aXLU9TC`) + A3 (`savee.com/i/WxChRnH`) como estilo.

```
Keep the subject, framing, pose and identity exactly as in the first image.
Apply the skin rendering and contrast curve of the reference images: real skin
texture with pores and fine hair, dense shadows with warm colour, long highlight
roll-off, low saturation outside skin tones. Remove the smartphone HDR look:
no lifted shadows, no local micro-contrast halo, no digital sharpening.
Fine film grain over the entire frame.
```

### Rodada B — paleta
Subir: sua foto + B1 (`savee.com/i/NLn9DEO`) + B2 (`savee.com/i/8fMkurc`) como estilo.

```
Keep the subject, framing and identity exactly as in the first image.
Apply the colour grade of the reference images: amber-olive mid-tones, blacks
closing with a slight green cast, deep cobalt sky with roughly 25 percent less
saturation than the original, warm skin that never turns orange.
Campaign-grade photographic finish. No teal and orange, no cinematic LUT cliché.
```

---

## 4 · Grade manual — receita numérica

Ponto de partida para Camera Raw / Lightroom / Resolve. Ajustar a olho depois.

| Etapa | Valor de partida |
|---|---|
| Blacks | fechar até ~8–12 IRE, com +green sutil na sombra |
| Shadows | −20 a −30 (desfazer o lift do HDR) |
| Highlights | −15, roll-off longo; camiseta sai do clipping |
| Clarity / Texture | Clarity **−15** (desfaz o microcontraste do celular), Texture +8 |
| Céu (HSL azul) | matiz +8 rumo a cobalto, saturação −25, luminância −10 |
| Pele (HSL laranja) | saturação −5, luminância +3 |
| Verde (árvore/camisa ao fundo) | saturação −30, luminância −15 |
| Grão | quantidade 18–22, tamanho 25, rugosidade 50 |
| Vinheta | no máximo −8, ou nenhuma |

Sequência: **flip → curva → HSL → textura/grão**. Grão sempre por último, e sempre
no frame inteiro. Grão só na pele denuncia filtro.

---

## 5 · Checklist de aprovação

Reprova o teste se qualquer um acontecer:

- [ ] Desenho da sobrancelha, lábio, orelha ou pupila mudou
- [ ] Pele mais lisa do que a referência A1
- [ ] Halo claro em volta da barba ou da aba do boné
- [ ] Céu com banding ou com ciano de volta
- [ ] Camiseta branca ainda sem trama
- [ ] Grão presente na pele e ausente no céu
- [ ] Bordado do boné ainda espelhado
