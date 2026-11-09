"""Build deterministic, self-contained protocol starter kits using the stdlib."""
from __future__ import annotations

import hashlib
import io
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
LETTERS = 'ABCDEF'
COMPANIONS = ('AGENTS.md', 'PROJECT.md', 'REVIEW_LEDGER.md', 'KIT.md')
D_SHA256 = '3d16c4d58d030ff745460386b081eb21c8c0d3f375cbfb06c4f9777c235a12f9'
ZIP_TIME = (2026, 11, 9, 0, 0, 0)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + '\n').encode('utf-8')


def kit_files(letter: str) -> dict[str, bytes]:
    if letter not in LETTERS or len(letter) != 1:
        raise ValueError('Unknown framework')
    protocol = (ROOT / f'Protocol_{letter}.md').read_bytes()
    if letter == 'D' and digest(protocol) != D_SHA256:
        raise ValueError('Protocol_D differs from the preserved version 1.4 source')
    files = {'PROTOCOL.md': protocol}
    folder = ROOT / 'companions' / f'Protocol_{letter}'
    for name in COMPANIONS:
        files[name] = (folder / name).read_bytes()
    manifest = {
        'schema': 1,
        'framework': f'Protocol_{letter}',
        'framework_edition': 1,
        'status': 'Blank starter kit, not completed research evidence',
        'hash_algorithm': 'SHA-256',
        'files': {name: {'sha256': digest(data), 'bytes': len(data)}
                  for name, data in sorted(files.items())},
    }
    if letter == 'D':
        manifest['preserved_protocol_version'] = '1.4'
    files['MANIFEST.json'] = json_bytes(manifest)
    return files


def kit_bytes(letter: str) -> bytes:
    output = io.BytesIO()
    with zipfile.ZipFile(output, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name, data in sorted(kit_files(letter).items()):
            entry = zipfile.ZipInfo(name, date_time=ZIP_TIME)
            entry.create_system = 3
            entry.external_attr = 0o100644 << 16
            entry.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(entry, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    return output.getvalue()


def index_bytes(built: dict[str, bytes]) -> bytes:
    return json_bytes({
        'schema': 1,
        'hash_algorithm': 'SHA-256',
        'kits': {f'Protocol_{letter}': {
            'path': f'kits/Protocol_{letter}.zip',
            'sha256': digest(data),
            'bytes': len(data),
            'protocol_sha256': digest((ROOT / f'Protocol_{letter}.md').read_bytes()),
        } for letter, data in sorted(built.items())},
    })


def main() -> None:
    built = {letter: kit_bytes(letter) for letter in LETTERS}
    target = ROOT / 'kits'
    target.mkdir(exist_ok=True)
    for letter, data in built.items():
        (target / f'Protocol_{letter}.zip').write_bytes(data)
    (target / 'MANIFEST.json').write_bytes(index_bytes(built))
    print('Built six self-contained starter kits; Protocol_D matches version 1.4.')


if __name__ == '__main__':
    main()
