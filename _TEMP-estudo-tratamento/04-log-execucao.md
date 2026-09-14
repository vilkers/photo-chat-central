# Log de execução

## Sessão 2026-09-14

**Feito**
- Pesquisa e inspeção visual de 16 referências no Savee; 9 selecionadas.
- Board privada criada: `Tratamento Cinema - estudo TEMP` (9 itens).
- Diagnóstico da foto original (ver `00`), incluindo o achado do espelhamento.
- Matriz de testes Magnific com custos simulados reais (ver `02`).
- Prompts prontos (ver `03`).

**Rota alterada pelo usuário:** os estudos são gerados pelos modelos de imagem com
as referências dele, não construídos por upscale. Ver `05-rota-generativa.md`.

**Bloqueado**
- A foto não pôde ser enviada ao Magnific a partir desta sessão: a política de egress
  do ambiente remoto nega conexão a `ak-data.magnific.com` (host de upload) e a
  `pikaso.cdnpk.net` (CDN de leitura). Sem upload, nenhuma geração foi disparada —
  **zero crédito consumido até aqui.**
- Pela mesma razão, resultados do Magnific não podem ser inspecionados visualmente
  nesta sessão. Nada foi avaliado sem ser visto.

**Atualização — 8 uploads recebidos**
O usuário subiu 7 referências + a foto pelo app (biblioteca saltou de 736 para 744
itens, todos às 02:55). Todos entraram como "Unnamed Creation" e o CDN continua
bloqueado nesta sessão, então não há como identificar visualmente qual creation é a
foto-base. Falta o identificador da foto para disparar o pipeline.

**Destravamento**
Subir a foto na biblioteca do Magnific pelo app e informar o nome/link da creation.
Com o identificador em mãos, a rodada 1→5 do pipeline pode ser disparada por MCP.
O julgamento visual dos resultados acontece no app (ou numa sessão com acesso ao CDN).

**Rodadas executadas**

| # | Data | Ferramenta | Parâmetros | Créditos | Veredito |
|---|---|---|---|---|---|
| 1 | 14/09 | images_generate | 8 estudos, ver `05-rota-generativa.md` | 625 | pendente de inspeção do usuário |

| 2 | 14/09 | images_generate | 5 versões analógicas + refação da V3, ver `05` | 450 | pendente de inspeção do usuário |

| 3 | 14/09 | images_generate | 6 testes de acting e figurino, 2 por ref, ver `05` | 450 | pendente de inspeção do usuário |

Saldo após a rodada 3: ~627 créditos.
