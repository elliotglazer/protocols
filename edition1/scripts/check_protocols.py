"""Validate source identity, links and starter-kit packaging, not mathematics."""
from __future__ import annotations

import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
import zipfile

from build_kits import ROOT, LETTERS, D_SHA256, digest, index_bytes, kit_bytes, kit_files


def main() -> int:
    errors: list[str] = []
    expected_names = {f'Protocol_{letter}.md' for letter in LETTERS}
    actual_names = {p.name for p in ROOT.glob('Protocol_*.md')}
    if actual_names != expected_names:
        errors.append('The repository must contain exactly Protocol_A.md through Protocol_F.md')

    actual_kits = {p.name for p in (ROOT / 'kits').glob('Protocol_*.zip')}
    if actual_kits != {f'Protocol_{letter}.zip' for letter in LETTERS}:
        errors.append('The repository must contain exactly six named starter ZIPs')

    for letter in LETTERS:
        protocol = ROOT / f'Protocol_{letter}.md'
        if not protocol.is_file():
            continue
        text = protocol.read_text(encoding='utf-8')
        if letter == 'D':
            if digest(protocol.read_bytes()) != D_SHA256:
                errors.append('Protocol_D is not the exact preserved version 1.4')
        elif not text.startswith(f'# Protocol_{letter}:'):
            errors.append(f'Protocol_{letter} has an incorrect heading')
        for required in ('AGENTS.md', 'PROJECT.md', 'REVIEW_LEDGER.md', 'KIT.md'):
            if not (ROOT / 'companions' / f'Protocol_{letter}' / required).is_file():
                errors.append(f'Missing Protocol_{letter} companion {required}')

    # Check file targets of actual Markdown links; external URLs are outside this check.
    for source in ROOT.rglob('*.md'):
        if '.git' in source.parts:
            continue
        content = source.read_text(encoding='utf-8')
        for target in re.findall(r'\[[^\]\n]*\]\(([^)\n]+)\)', content):
            target = target.strip().strip('<>')
            parts = urlsplit(target)
            if parts.scheme or parts.netloc or not parts.path:
                continue
            resolved = (source.parent / unquote(parts.path)).resolve()
            if not resolved.is_relative_to(ROOT.resolve()) or not resolved.exists():
                errors.append(f'Broken or escaping link in {source.relative_to(ROOT)}: {target}')

    built: dict[str, bytes] = {}
    for letter in LETTERS:
        archive_path = ROOT / 'kits' / f'Protocol_{letter}.zip'
        try:
            expected = kit_files(letter)
            rebuilt = kit_bytes(letter)
            actual = archive_path.read_bytes()
            built[letter] = actual
            if actual != rebuilt:
                errors.append(f'Protocol_{letter} kit is stale or nondeterministic')
            with zipfile.ZipFile(archive_path) as archive:
                names = archive.namelist()
                if len(names) != len(set(names)) or set(names) != set(expected):
                    errors.append(f'Protocol_{letter} ZIP has unexpected or duplicate members')
                if archive.testzip() is not None:
                    errors.append(f'Protocol_{letter} ZIP has an invalid CRC')
                for name, data in expected.items():
                    if archive.read(name) != data:
                        errors.append(f'Protocol_{letter} ZIP differs at {name}')
                manifest = json.loads(archive.read('MANIFEST.json'))
                for name, metadata in manifest['files'].items():
                    data = archive.read(name)
                    if digest(data) != metadata['sha256'] or len(data) != metadata['bytes']:
                        errors.append(f'Protocol_{letter} manifest mismatch at {name}')
        except (OSError, ValueError, KeyError, zipfile.BadZipFile) as exc:
            errors.append(f'Protocol_{letter}: {exc}')

    try:
        if len(built) == 6 and (ROOT / 'kits/MANIFEST.json').read_bytes() != index_bytes(built):
            errors.append('Kit index does not match distributed files')
    except OSError as exc:
        errors.append(str(exc))

    if errors:
        print('\n'.join('FAIL: ' + error for error in errors), file=sys.stderr)
        return 1
    print('PASS: six protocols, companion sets, local links, kit contents/manifests, deterministic builds, and exact Protocol_D identity.')
    print('Scope: file and packaging integrity only; no mathematical review or reliability claim.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
