# Maintaining this protocols repository

This repository contains reusable research protocols and templates. It is not itself a proof project running every protocol at once. Instructions under `companions/` are documents to distribute, not commands to launch their research workflows here.

Preserve Protocol_D.md byte for byte as version 1.4. Its authoritative SHA-256 appears in PROVENANCE.md and is checked by the packaging validator. Do not normalize its line endings.

Keep six variants, A through F. A is tracked author verification; B is targeted independent review; C is complete independent informal review; D is exact 1.4; E is formal proof relative to audited published-theorem assumptions; F is full formal dependency closure to declared foundations. Do not silently add D's obligations to lighter companions or allow E's source assumptions in F.

Keep the comparison table, variant text and companion instructions consistent. Label labor ranges as estimates and never invent reliability percentages. Preserve the difference between an undetected error and a known unresolved gap.

After edits, run `python scripts/build_kits.py` and `python scripts/check_protocols.py`. Inspect affected prose for substantive contradictions as well. These checks validate packaging and references, not the quality of a future mathematical review. Do not add a custom approval service or impose a second human review requirement without the owner's request.
