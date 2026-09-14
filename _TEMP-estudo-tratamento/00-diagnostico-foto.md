# Diagnóstico da foto original

Arquivo de origem: selfie, **1932 × 2576 px** (≈ 5 MP), vertical 3:4, JPEG 1,7 MB.

## O que a imagem é, fotograficamente

- **Lente/enquadramento:** selfie de braço, equivalente ~24–26 mm, câmera abaixo da
  linha dos olhos e muito próxima. Consequência: nariz e testa ampliados, orelha
  comprimida, linha do ombro em fuga. É perspectiva de celular, não de retrato.
- **Luz:** sol alto, ligeiramente frontal-esquerda, céu limpo como fill gigante.
  A aba do boné corta a testa e joga sombra na parte alta do rosto; o resto da face
  fica em luz aberta, com specular na ponta do nariz e na maçã direita. Não há
  modelagem — é luz chapada de meio-dia.
- **Fundo:** rua. Prédios amarelo-creme e turquesa à esquerda, árvore e muro de pedra
  à direita, fiação elétrica cortando o céu, três figuras humanas e uma moto.
  Concorre com o rosto em cor e em detalhe.
- **Processamento nativo:** HDR de smartphone. Sombras levantadas, highlight
  comprimido, microcontraste local exagerado (halo em volta da barba e das
  sobrancelhas), sharpening digital visível nos fios, céu em ciano saturado.

## Achado que muda a peça

**A imagem está espelhada.** O bordado do boné lê "MES / ITA" invertido — o original é
`ITA / MES` (ou similar) lido ao contrário. Toda selfie frontal sai espelhada.

Se isso virar peça, o logo do boné aparece invertido e qualquer diretor de arte
percebe em dois segundos. **Primeiro passo do pipeline: flip horizontal.** Depois do
flip, a repartição do cabelo, o piercing no nariz e o brinco trocam de lado — é o lado
correto, o que as pessoas veem ao vivo.

## O que trava o look de cinema (em ordem de impacto)

1. **Curva de HDR de celular.** Sombra sem densidade e highlight sem roll-off. Cinema
   tem preto que fecha e highlight que morre devagar. É o item nº 1 — sem resolver
   isso, nenhum grão ou LUT salva.
2. **Espelhamento.** Craft básico.
3. **Céu ciano.** O azul de celular puxa para ciano elétrico. Cinema quer azul mais
   denso, menos saturado, levemente puxado para o cinza-cobalto.
4. **Fundo poluído.** Fiação, pessoas, dois prédios coloridos. Falta separação de
   planos: a foto não tem compressão de teleobjetiva nem profundidade de campo.
5. **Textura de pele artificial.** O sharpening do celular criou uma pele "de plástico
   com poro desenhado". Precisa voltar a ter microtextura real e grão.
6. **Camiseta branca sem informação.** Ocupa o terço inferior e está perto do clipping.
   Um upscale de precisão devolve trama do algodão — isso sozinho já dá sensação de
   fotografia real.
7. **Distorção de selfie.** Só corrigível mexendo na geometria do rosto. Fica fora do
   escopo "sem me modificar" — anotado como opção consciente, não como default.

## Direção de tratamento proposta

Um **daylight cinema quente e denso**, não um teal & orange genérico:

- Blacks fechando em ~8–12 IRE com leve verde-oliva (ver ref. Ines Manai).
- Pele preservada em tom quente real, sem empurrar para laranja.
- Céu dessaturado uns 20–25% e puxado de ciano para azul-cobalto.
- Highlight com roll-off longo; camiseta entregando trama em vez de branco chapado.
- Grão fino e uniforme, presente também no céu (grão só na pele denuncia filtro).
- Halation mínima ou zero: é luz de dia, não neon noturno. Halation aqui vira efeito.
