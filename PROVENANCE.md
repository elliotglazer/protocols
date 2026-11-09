# Provenance and versioning

## Protocol_D

Protocol_D is the original **Mathematical research review protocol, version 1.4, November 7, 2026**, supplied for this project as `mathematical-research-review-protocol-v1.4.md` and already used in the mathematical research repository.

The authoritative source file and [Protocol_D.md](Protocol_D.md) have the same SHA-256:

```text
3d16c4d58d030ff745460386b081eb21c8c0d3f375cbfb06c4f9777c235a12f9
```

The original title, version line, contents and line endings are preserved. The name Protocol_D selects that text without rewriting it. Its [agent companion](companions/Protocol_D/AGENTS.md) is also copied unchanged from the existing version 1.4 starter kit. The other companion templates are adapted for this collection.

## Variants and companions

Protocols A, B, C, E and F and their companion templates were prepared using OpenAI Codex at Elliot Glazer's request on November 9, 2026. They implement the requested framework comparison. They are proposed operating standards, not evidence that any mathematical result has passed those standards.

The former selective-formalization tier E is omitted. The former F and G are relabeled E and F. No selective-formalization seventh kit is included.

The labor ranges in the README are judgmental planning estimates for comparable projects, not empirical benchmarks. They should not be read as measured error rates, guarantees, or retrospective accounting of a particular research effort.

## Maintaining the collection

The letter identifies the selected assurance framework. The framework edition identifies a revision of that variant. Protocol_D continues to identify the unchanged original version 1.4; do not edit its text while retaining that identity. A future revised standard must be named and versioned explicitly.

When changing any variant, update its matching companions and explain the changed requirements. Regenerate the kits and their manifest with `scripts/build_kits.py`, then run `scripts/check_protocols.py`. The kit manifest binds the distributed templates; a research project needs its own manifest for its actual evidence and releases.

Git history preserves revisions of this collection. The kit build uses a fixed timestamp so identical input files produce identical ZIP bytes. That timestamp is a packaging convention, not evidence of when a mathematical review occurred.
