# Matriz de testes Magnific — qual modelo serve para o quê

Premissa do briefing: **reconstruir a foto sem modificar a pessoa.** Isso elimina de
saída qualquer rota text-to-image sobre o rosto. Tudo abaixo respeita identidade.

## Situação da conta (checada nesta sessão)

- Plano Advanced, **Unlimited não ativo neste contexto** → toda geração queima crédito.
- **2.152 créditos disponíveis.**

## Custos reais (simulados, não estimados de cabeça)

| Ferramenta | Parâmetros simulados | Créditos |
|---|---|---|
| `images_resize` | 1932×2576 → 1449×1932 | **40** (exato) |
| `images_skin_enhancer` | faithful, skinDetail 45, smartGrain 12 | **200** (exato) |
| `images_relight` | 1 luz, 2k, 1 imagem | **75** (exato) |
| `images_change_camera` | padrão | **~50** (base) |
| `images_upscale` | qualquer modo | **variável por tier: S 90 / M 180 / L 270 / XL 1080** |

> ⚠️ O tier do upscale sai do tamanho de saída. A foto tem 5 MP; **2x = 20 MP**, o que
> cai em tier alto (L/XL). Um único upscale 2x no arquivo cheio pode custar até 1.080
> créditos — metade da carteira. Por isso a rodada de estudo roda em cópia reduzida,
> e o arquivo cheio só entra na direção aprovada.

---

## Veredito por modelo

### ✅ `ultra-photo` — Precision (photo) · **a base certa**
Criatividade zero, o mais fiel ao original. É o único upscaler do Magnific que não
inventa nada no rosto — por isso é ele que atende "sem me modificar". Só 2x.

Parâmetros para esta foto (não use o preset `portraits` cru):

```
mode: ultra-photo
scale: 2x
sharpness: 5      ← preset portraits usa 12; aqui só empilharia no sharpening do iPhone
grain: 11         ← faixa 7–12 preserva grão real; 11 já dá corpo analógico
ultraDetail: 6    ← segura o poro sem virar mapa de textura
```

### ✅ `ultra-denoiser` — Precision (photo denoiser) · **se as sombras tiverem ruído**
Mesma família, com denoise. Rodar só se o crop 100% da sombra sob o boné mostrar
ruído de sensor. Senão, é perda de detalhe de graça.

### 🟡 `ultra-sublime` — Precision (sublime) · **para o entregável grande**
O mais versátil, brilha em 4x. É o caminho para o master de KV/OOH **depois** da
direção aprovada, com `precisionPreset: grainyAnalog` (sharpness 5 / grain 12).
4x de 5 MP = 80 MP → tier XL. Não usar em fase de estudo.

### 🟡 `creative` — Magnific Creative · **só como plano B, com coleira curta**
Alucina detalhe. Em rosto real isso vira troca de feição. Se a precision não resolver
a textura, entra assim e não mais que isso:

```
mode: creative
scale: 2x
optimised: FilmAndPhotography
presets: custom
creativity: -6     ← bem abaixo do subtle (-3)
resemblance: 6     ← puxa forte para o original
hdr: -3            ← a foto já vem com HDR demais
fractality: -2     ← menos detalhe por pixel, menos glitch na barba
engine: magnific_sparkle   ← reduz artefato de JPEG; sharpy empilharia halo
```

**Critério de descarte:** se o desenho da sobrancelha, do lábio ou da pupila mudar,
o teste morreu, independente de estar bonito.

### ✅ `images_skin_enhancer` (faithful) · **o que realmente mata o look de celular**
`faithful` preserva identidade por definição. É a ferramenta com maior retorno por
crédito aqui: desfaz a pele plastificada do HDR e devolve microtextura.

```
version: faithful
skinDetail: 45     ← 40–50; acima de 60 vira pele de fotômetro
smartGrain: 12     ← casa com o grain 11 do upscale
sharpen: 0         ← nunca somar sharpen; o arquivo já vem sobre-sharpened
```

### ✅ `images_relight` · **o salto de cinema de verdade**
Relight troca a luz, não a fisionomia — continua sendo você. A luz chapada de meio-dia
é o maior motivo de a foto não parecer cinema. Duas variantes a testar:

```
# V1 — key lateral quente, sol baixo (a mais provável de acertar)
lights:
  - azimuth: -45, elevation: 45, type: gel, color: "#FFD9A8", intensity: 6
  - azimuth: 135, elevation: 0,  type: neutral,               intensity: 2
resolution: 2k

# V2 — contraluz de fim de tarde com fill frio do céu
lights:
  - azimuth: 180, elevation: 45, type: gel, color: "#FFC98A", intensity: 7
  - azimuth: -90, elevation: 0,  type: gel, color: "#9FB8D6", intensity: 3
resolution: 2k
```

### ❌ `images_change_camera` · **fora do escopo**
Resolveria a distorção de selfie simulando lente mais longa — e ao fazer isso muda a
geometria do rosto. Isso é "modificar". Fica registrado como opção consciente, não
como etapa do pipeline.

### ❌ Seedream 5 Pro / Nano Banana Pro / Recraft / GPT-2 sobre o rosto
São text-to-image. Mesmo com referência de `character`, reconstroem o rosto a partir
de um entendimento do rosto — a identidade escorre em pele, dentes, orelha e olhar.
Para "sem me modificar", não entram no rosto.
**Onde eles servem:** reconstruir **só o fundo** (fiação, pessoas, prédios) com máscara,
ou gerar estudo de paleta para apresentação. Nesse caso, Nano Banana Pro em `image_edit`
com máscara, ou `images_retouch` com máscara por região.

---

## Pipeline recomendado (ordem importa)

```
0. Flip horizontal          → fora do Magnific (o bordado do boné está invertido)
1. images_resize p/ ~1450px → cópia de trabalho barata                      40 cr
2. images_skin_enhancer     → faithful, tira o HDR de celular              200 cr
3. images_upscale ultra-photo 2x → devolve trama da camiseta e do boné   90–270 cr
4. images_relight V1 e V2   → duas leituras de luz cinema              75 + 75 cr
5. Grade final              → Photoshop/Lightroom/Resolve com as refs do Savee
```

**Custo da rodada de estudo: ~480–660 créditos.** Cabem ~3 rodadas na carteira atual.

Ordem 2 antes de 3 é deliberada: o skin enhancer trabalha melhor antes de o upscaler
multiplicar a textura. Invertendo, você amplia o artefato e depois pede para limpar.

O grade fica fora do Magnific de propósito. O Magnific é excelente em textura,
resolução e luz; ele não é uma mesa de cor. Curva, matiz do céu e densidade de preto
se resolvem melhor à mão, com as referências do bloco A3/B1 abertas ao lado.
