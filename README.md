# Mathematical research protocols

Edition 2 | November 13, 2026

These four frameworks specify the evidence a mathematical research repository should contain before it reports an AI-generated result as verified. They are designed to run without a human in the loop. They are not a replacement for peer review by experts; they are evidence for a result's correctness before experts are brought in.

Each protocol extends the one before it, and each step adds a different kind of evidence.

| Framework | Review standard | Evidence it adds | What remains trusted |
| --- | --- | --- | --- |
| [Protocol_A](Protocol_A.md) | Tracked author verification | Source and application inventory, findings ledger, explicit and reproducible computations | The author's own reasoning and inventory |
| [Protocol_B](Protocol_B.md) | A plus automated cross-family audit | Review of load-bearing steps by a model family other than the author's, run as a required check | Informal reasoning; published theorems; reviewers that can share mistakes |
| [Protocol_C](Protocol_C.md) | B plus formal proof relative to published theorems | Machine-checked proof of the project's own arguments | The listed published theorems and their translation; the formal statements; the proof system |
| [Protocol_D](Protocol_D.md) | Full formalization | Machine-checked proof of the cited theorems as well | The formal statements; the proof system and its foundations |

Protocols A and B are complete. Protocols C and D currently fix the review standard only; their implementation is not yet specified.

None of these guarantees that a claim is correct because its requirements are complete.

## Roles

An **author** is whoever produced the argument, construction or code under review: a person, an AI agent, or both. A **reviewer** examines it. A reviewer is **outside** when it is a model from a different family than the author, or a human expert. Agreement between two model families is stronger evidence than agreement within one, and weaker than review by an expert.

A **repository collaborator** is called on at one point only: when a reviewer and an author's rebuttal remain in disagreement under Protocol_B.

## Labor

No labor estimates are given. Each time a protocol is run on a project, record the labor it took (agent-hours, tokens and elapsed time, split into mathematics, review and release work) and publish the measurement here. Estimates will be made from those measurements.

## Edition 1

Edition 1 had six frameworks. Its names do not carry over. Its complete text, starter kits and packaging checks are preserved unchanged in [edition1/](edition1/README.md).

| Edition 1 | Edition 2 |
| --- | --- |
| Protocol_A, tracked verification | Protocol_A, with lighter release requirements |
| Protocol_B, targeted independent review | Retired |
| Protocol_C, complete independent review | Retired |
| Protocol_D, review protocol version 1.4 | Retired |
| Protocol_E, formal proof relative to published theorems | Protocol_C, as an extension of the new B |
| Protocol_F, full formal dependency closure | Protocol_D |

The new Protocol_B has no edition 1 counterpart.

Work reviewed under edition 1 keeps the review it actually received. A result reviewed under edition 1 Protocol_D does not thereby meet edition 2 Protocol_B, C or D. Describe it under edition 2 by the standard it meets.
