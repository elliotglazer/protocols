# Mathematical research protocols

Six review frameworks for mathematical research repositories, with different labor and assurance requirements. Choose one at the start of a project and state it in the project brief. A higher letter requires stronger evidence, but does not give a numerical guarantee that the mathematics is correct.

**Protocol_D is the original Mathematical Research Review Protocol version 1.4, preserved byte for byte.** Protocols A, B and C provide lighter review processes. Protocols E and F use formal proof for progressively more of the dependency chain.

## Comparison

The baseline, Protocol 0, is the original plan: use published external theorems, check their hypotheses and conventions, give explicit constructions and computations, and check the argument as its author. It is a comparison baseline, not a seventh kit.

| Framework | Required evidence | Estimated labor relative to Protocol 0 | Principal residual risk |
| --- | --- | --- | --- |
| Protocol 0 | Published theorem inputs, application and convention checks, explicit constructions and computations, author review | 1× | Author blind spots, omitted dependencies, unnoticed errors in applications or calculations |
| [Protocol_A](Protocol_A.md) | Tracked verification: source and application inventory, findings ledger, reproducible computation checks, versioned evidence | 1.2–1.7× | An author's inventory or reasoning may be incomplete; independent mathematical review is not required |
| [Protocol_B](Protocol_B.md) | A's evidence plus independent targeted review of novel or fragile arguments, exceptional cases, and essential checkers | 1.5–2.5× | Unselected arguments and interfaces may contain errors; the review plan may miss a fragile step |
| [Protocol_C](Protocol_C.md) | Complete independent mathematical review, including substantive theorem applications, connecting arguments, computations, and final assembly | 2–4× | Reviewers can share misconceptions or miss an implicit dependency; no separate source-first inventory reconstruction is required |
| [Protocol_D](Protocol_D.md) | Exact Protocol 1.4: complete review, independent source-first reconstruction and reconciliation, explicit coverage decisions, related-use checks, and synchronized releases | 3–6× | Informal reasoning can still fail; a carefully inventoried application can still be wrong; published inputs remain trusted |
| [Protocol_E](Protocol_E.md) | Formal proof of all project arguments relative to an explicit, audited list of published-theorem assumptions; independently checked statement fidelity and formal dependency closure | 8–30× | Imported theorem assumptions, their translation, target specification, and the declared formal verification system |
| [Protocol_F](Protocol_F.md) | Full formal dependency closure to declared foundational axioms, including verified computational certificates, with independent specification review | 20–100× or more | Specification errors and defects in the declared kernel, foundational assumptions, or build and checking environment |

These are speculative planning ranges for future projects of comparable depth and complexity. They are not measurements of this project's history or reliable forecasts for every subject. They estimate total labor from a serious candidate argument through proof completion, verification and a reproducible release, assuming an efficient implementation. Initial discovery, unexpected new mathematics, inaccessible sources, and missing formal libraries can dominate the cost. The ranges overlap deliberately. Parallel workers may reduce elapsed time without reducing total labor.

No calibrated percentages for the risk of an incorrect result are available. The table describes which failure modes each process attempts to detect and which it still tolerates. Every framework requires a valid argument for its stated claim and the resolution of known substantive gaps before declaring completion. A lighter framework accepts less evidence against **undetected** errors, not permission to ignore a known defect.

The former selective-formalization tier E has been removed. The former F and G tiers are now E and F. Protocol_D retains the version number 1.4 inside its original text; the letters select frameworks, not successive revisions of that text. E and F replace duplicated manual internal-dependency bookkeeping with inspected formal dependency evidence. They do not claim that a compiler run satisfies all of D's separate documentary requirements.

## Download a starter kit

Each ZIP contains `PROTOCOL.md`, `AGENTS.md`, `PROJECT.md`, `REVIEW_LEDGER.md`, `KIT.md`, and a file manifest. It is self-contained. Download one kit, extract it into a new research repository, and fill in `PROJECT.md`.

| Kit | Agent instructions | Project brief | Review ledger |
| --- | --- | --- | --- |
| [Protocol_A.zip](kits/Protocol_A.zip) | [A instructions](companions/Protocol_A/AGENTS.md) | [A brief](companions/Protocol_A/PROJECT.md) | [A ledger](companions/Protocol_A/REVIEW_LEDGER.md) |
| [Protocol_B.zip](kits/Protocol_B.zip) | [B instructions](companions/Protocol_B/AGENTS.md) | [B brief](companions/Protocol_B/PROJECT.md) | [B ledger](companions/Protocol_B/REVIEW_LEDGER.md) |
| [Protocol_C.zip](kits/Protocol_C.zip) | [C instructions](companions/Protocol_C/AGENTS.md) | [C brief](companions/Protocol_C/PROJECT.md) | [C ledger](companions/Protocol_C/REVIEW_LEDGER.md) |
| [Protocol_D.zip](kits/Protocol_D.zip) | [D instructions](companions/Protocol_D/AGENTS.md) | [D brief](companions/Protocol_D/PROJECT.md) | [D ledger](companions/Protocol_D/REVIEW_LEDGER.md) |
| [Protocol_E.zip](kits/Protocol_E.zip) | [E instructions](companions/Protocol_E/AGENTS.md) | [E brief](companions/Protocol_E/PROJECT.md) | [E ledger](companions/Protocol_E/REVIEW_LEDGER.md) |
| [Protocol_F.zip](kits/Protocol_F.zip) | [F instructions](companions/Protocol_F/AGENTS.md) | [F brief](companions/Protocol_F/PROJECT.md) | [F ledger](companions/Protocol_F/REVIEW_LEDGER.md) |

For an existing repository, merge the instructions and brief deliberately. Preserve existing work, evidence and authorizations. Installing a lighter kit does not erase unresolved findings or retroactively change a prior review claim. A change of framework needs the project owner's explicit choice and an explanation of the changed completion standard.

Suggested starting instruction:

> Read PROTOCOL.md, AGENTS.md and PROJECT.md. Work toward the stated mathematical objective and satisfy the selected framework's requirements. Use one canonical review ledger, reuse evidence at its exact accepted scope, and review only affected work after changes. Report unresolved mathematics, reviewed work awaiting incorporation, and remaining release work separately. Do not claim a stronger review or formalization status than the evidence supports.

## Common operating principles

- Start research and recordkeeping together. A custom review service or GitHub App is not a prerequisite.
- Record coherent mathematical units. An application, lemma or connecting argument is usually a better unit than a sentence or a checklist cell.
- Store each current assertion once where possible. Link repeated uses to it and keep their actual contexts visible.
- Preserve accepted work when its proof, definitions, assumptions and consumers remain unchanged. Reopen affected work after a real change or concrete objection.
- Keep source qualification, mathematical correctness, review coverage, incorporation and release status distinct.
- Update the cumulative research handoff, inventory, findings, manuscript and artifact index together for a research release. Do not rebuild the release archive after every internal edit.
- Stop when the selected completion criteria pass. Additional rounds need an identified question, changed input or coverage defect.

Every companion is specific to its framework. For example, A does not require a non-author coverage review, and B does not silently require a full D audit. All six preserve explicit computations, findings, provenance and cumulative handoffs.

## Maintenance and provenance

[PROVENANCE.md](PROVENANCE.md) identifies the unchanged version 1.4 source and the origins of the variants. The companion files are templates, not completed audit evidence. The repository's checks validate packaging, file identity and local links; they do not review a mathematical proof.

With Python 3.10 or later, no third-party packages are needed:

```sh
python scripts/build_kits.py
python scripts/check_protocols.py
```

The first command deterministically regenerates the kits. The second checks the six kits against the source files, their manifests, the version 1.4 digest, and local Markdown links.
