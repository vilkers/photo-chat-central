"""Prepare auditable Magnific requests; never submits paid generations."""
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PHOTO_FIELDS = ('composition', 'camera', 'environment', 'exposure', 'light', 'contrast', 'color', 'focus', 'texture')


def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def require(condition, message):
    if not condition:
        raise ValueError(message)


def compile_request(brief, shot):
    require(shot.get('direction_status') == 'ready', 'Complete a direção da rodada antes de compilar.')
    require(not shot.get('unresolved_conflicts'), 'Resolva os conflitos de direção registrados.')
    for field in ('id', 'series_id', 'person_direction'):
        require(isinstance(shot.get(field), str) and shot[field].strip(), f'Campo obrigatório: {field}')
    cast = next((p for p in brief['casting'] if p['id'] == shot.get('casting_id')), None)
    require(cast is not None, 'Selecione uma referência de casting existente.')
    photo = shot.get('photography', {})
    for field in PHOTO_FIELDS:
        require(isinstance(photo.get(field), str) and photo[field].strip(), f'Analise a fotografia: {field}')
    require(photo.get('reference_identifier'), 'Falta o ID real da referência fotográfica no Magnific.')
    require(shot.get('casting_identifier'), 'Falta o ID real do casting no Magnific.')
    product = brief['product']
    require(product.get('creation_identifier'), 'Falta referência do cartão.')
    require(type(shot.get('count')) is int and 1 <= shot['count'] <= 8, 'Defina count entre 1 e 8 conforme o pedido da rodada.')
    refs = [
        {'type': 'image', 'identifier': photo['reference_identifier']},
        {'type': 'image', 'identifier': shot['casting_identifier']},
        {'type': 'image', 'identifier': product['creation_identifier']},
    ]
    require(all(isinstance(r['identifier'], str) and r['identifier'].strip() for r in refs), 'IDs devem ser strings não vazias.')
    require(len({r['identifier'] for r in refs}) == 3, 'Referências de fotografia, casting e cartão devem ter papéis distintos.')
    prompt = '\n\n'.join([
        'Reconstrua uma fotografia para o KV de iFood Benefícios. As referências têm funções distintas: imagem 1 define fotografia; imagem 2 informa casting e acting; imagem 3 define exclusivamente o produto.',
        'DIREÇÃO DA PESSOA E ACTING\n' + shot['person_direction'],
        'REPERTÓRIO DE CASTING\n' + cast['description'] + '\n' + cast['acting'],
        'FOTOGRAFIA — reproduzir a intenção da imagem 1\n' + '\n'.join(f'{k}: {photo[k]}' for k in PHOTO_FIELDS),
        'MARCA\nMarsala, acqua e off-white, com tons terrosos no figurino quando cabíveis. Distribua a paleta em materiais e superfícies sem filtro global. Preserve a exposição, contraste e caráter claro ou escuro da referência. Pele com cor natural. Não copiar automaticamente a luz do casting.',
        'PRODUTO\nUse o layout completo da imagem 3: proporção, vermelho, smile, chip, contactless, iFood Benefícios e elo. Sem espelhar ou redesenhar. Perspectiva, luz e reflexos devem corresponder à cena. Contato plausível com os dedos, sem anatomia extra ou cartão flutuante.',
        'CRAFT\nPessoa, roupa e cartão pertencem à mesma luz e perspectiva. Preserve textura natural e detalhes observados; não adicionar HDR, suavização plástica, flare ou grão não solicitado. Respeite a fotografia analisada em vez de aplicar um preset genérico.',
        'AJUSTES DESTA RODADA\n' + (shot.get('local_adjustments') or 'Nenhum ajuste adicional.'),
    ])
    return {**brief['generation'], 'count': shot['count'], 'prompt': prompt, 'references': refs}


def append_feedback(path, scope, target, text, status):
    require(scope in ('image', 'series', 'campaign', 'general'), 'Escopo inválido.')
    require(status in ('approved', 'rejected', 'hypothesis', 'unreviewed'), 'Status inválido.')
    require(bool(target.strip()) and bool(text.strip()), 'Alvo e feedback são obrigatórios.')
    event = {'timestamp': datetime.now(timezone.utc).isoformat(), 'scope': scope,
             'target': target, 'text': text, 'status': status,
             'source': 'user' if status in ('approved', 'rejected') else 'unconfirmed'}
    with Path(path).open('a', encoding='utf-8') as f:
        f.write(json.dumps(event, ensure_ascii=False) + '\n')
    return event


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    inspect = sub.add_parser('inspect')
    inspect.add_argument('brief')
    compile_cmd = sub.add_parser('compile')
    compile_cmd.add_argument('brief')
    compile_cmd.add_argument('shot')
    feedback = sub.add_parser('feedback')
    feedback.add_argument('--scope', required=True, choices=['image', 'series', 'campaign', 'general'])
    feedback.add_argument('--target', required=True)
    feedback.add_argument('--text', required=True)
    feedback.add_argument('--status', required=True, choices=['approved', 'rejected', 'hypothesis', 'unreviewed'])
    feedback.add_argument('--file', default=str(ROOT / 'feedback.jsonl'))
    args = parser.parse_args()
    try:
        if args.command == 'compile':
            result = compile_request(read(args.brief), read(args.shot))
        elif args.command == 'inspect':
            brief = read(args.brief)
            result = {'campaign': brief['name'], 'status': brief['status'],
                      'casting_count': len(brief['casting']), 'generation': brief['generation'],
                      'next': 'Receber referências de fotografia e completar a rodada.'}
        else:
            result = append_feedback(args.file, args.scope, args.target, args.text, args.status)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except (ValueError, KeyError, OSError, TypeError) as error:
        parser.exit(2, f'Não foi possível concluir: {error}\n')


if __name__ == '__main__':
    main()
