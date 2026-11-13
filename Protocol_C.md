# Protocol_C: formal proof relative to published theorems

Framework edition 2 | November 13, 2026

This edition fixes the review standard only. How a project implements and enforces it is not yet specified.

## Completion standard

Meet Protocol_B, and in addition supply a machine-checked formal proof of every project argument that supports the announced results. The formal proof may assume published theorems, and nothing else beyond the declared foundations of the proof system.

The standard is met when all of the following hold:

1. **Formal targets.** Each announced result has a formal statement, and that statement has been compared with the intended mathematics: quantifiers, domains, hidden parameters, degenerate cases and non-vacuity.
2. **Listed assumptions only.** The dependency closure of each formal target contains only the declared foundations and an explicit, published list of published-theorem assumptions. It contains no project-specific axiom, placeholder or unfinished proof.
3. **Faithful assumptions.** Each assumption states its published source faithfully: the final published version, its hypotheses, conventions and corrections. Any specialization or translation that needs new mathematics is itself formally proved from the assumption.
4. **Computation discharged.** Every essential computational fact enters the proof through a formally verified check. A computation that is only attested externally is an additional assumption and must be listed as one.
5. **Same results.** The manuscript states the same results and limitations as the formal targets.

Unpublished, disputed or unknown results cannot be listed as published-theorem assumptions. Prove them in the project, or state a conditional target with the premise exposed.

## Trust boundary

What remains trusted: the listed published theorems and their translation into formal statements, the fidelity of the formal targets to the intended claims, and the proof system's foundations and implementation. A successful build does not show that a statement means what was intended.

## Reporting

Report completion as **Protocol_C formal verification relative to the listed published-theorem assumptions**, and publish the list prominently. Do not describe the result as fully formalized.
