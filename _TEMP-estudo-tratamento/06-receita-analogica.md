# Receita analógica — aplicar à mão sobre a versão aprovada

Zero crédito. Camera Raw, Lightroom ou Capture One. Os valores são ponto de partida
calibrados para **esta** imagem (sombra aberta, fundo de rua cinza-azulado,
camiseta branca, pele com leve tendência magenta).

## Diagnóstico da imagem aprovada

Boa base: geometria de 85mm, fundo limpo e separado por profundidade de campo,
camiseta ainda com detalhe, veludo cotelê do boné legível. O que falta:

- Pretos não fecham — o fundo fica em cinza médio e a imagem lê digital
- Meios-tons altos demais, achatando o volume do rosto
- Magenta nas maçãs do rosto, típico de render neutro
- Specular do nariz perto do estouro
- Grão praticamente ausente

## Ordem de aplicação

**1 · Flip horizontal.** Antes de tudo. O bordado do boné continua espelhado.

**2 · Balanço de branco**
- Temperatura +3
- Matiz −4 (tira o magenta das maçãs)

**3 · Curva de tom**
- Pretos fechando em ~10 IRE
- Toe de filme: levantar os 2–3 pontos mais baixos da curva, preto fosco em vez de preto absoluto
- S suave nos meios, sem tocar nos highlights
- Highlights −12, para o brilho do nariz voltar ao roll-off

**4 · HSL**
| Faixa | Sat | Lum |
|---|---|---|
| Vermelho (maçãs) | −8 | 0 |
| Laranja (pele) | −4 | +4 |
| Azul (fundo/rua) | −12 | −8 |

**5 · Presença**
- Textura +6
- Nitidez/Clarity **−10** (desfaz o microcontraste sintético)
- Dehaze −3

**6 · Split tone**
- Sombras: matiz 170, saturação 6 (verde-ciano — é o que dá cara de negativo)
- Altas: matiz 40, saturação 4

**7 · Grão**
- Quantidade 22 · Tamanho 28 · Rugosidade 55
- No frame inteiro. Grão só na pele denuncia filtro.

**8 · Halation** (Photoshop, opcional mas é o que fecha)
- Duplicar a camada, extrair as altas (Blend If ou canal de luminância)
- Desfoque gaussiano 8 px
- Empurrar para laranja-avermelhado
- Modo Tela, opacidade 12–18%
- Só nas bordas de alto contraste: aba do boné contra o fundo, ombro da camiseta

**9 · Vinheta** −6 no máximo. Acima disso vira efeito.

## Ordem importa

Curva → HSL → textura → grão → halation. Grão sempre depois do tratamento de cor e
sempre por último antes da halation. Invertendo, o grão entra na conta da curva e
vira ruído colorido.

## Se recarregar créditos

Prioridade, nesta ordem:
1. `images_relight` (75 cr) em mais dois desenhos de luz — é a única coisa aqui que
   redesenha luz sem reconstruir o rosto.
2. `images_skin_enhancer` faithful (200 cr) — devolve microtextura real de pele.
3. `images_upscale` modo `ultra-photo` 2x (90–270 cr) — só no final, na versão
   fechada, para o master de apresentação.

Gerar de novo por text-to-image não entra nessa lista: é o que mexe na fisionomia.
