# Protocol_D: full formalization

Framework edition 2 | November 13, 2026

This edition fixes the review standard only. How a project implements and enforces it is not yet specified.

## Completion standard

Meet Protocol_C with an empty list of published-theorem assumptions. Every announced result and every mathematical dependency is formally proved down to an explicit foundational basis.

The standard is met when all of the following hold:

1. **Formal targets.** Each announced result has a formal statement that has been compared with the intended mathematics, as in Protocol_C.
2. **Foundations only.** The dependency closure of each formal target contains only the declared foundational axioms. It contains no project-specific axiom, no imported published-theorem axiom, no externally attested computation and no unfinished proof.
3. **Library results checked.** Results taken from existing formal libraries are pinned by version, and their statements and transitive assumptions have been inspected.
4. **Computation verified end to end.** Every essential computation is justified through the declared verified checking path, including the link between any released artifact and the formal object it represents.
5. **Same results.** The manuscript states the same results and limitations as the formal targets.

A needed result that is unavailable in the chosen libraries must be formally proved, replaced by a proved route, or left as explicitly incomplete work. It may not be assumed because it is published, standard or expensive to formalize.

## Trust boundary

What remains trusted: the declared foundations, the proof system's kernel and checking environment, and the fidelity of the formal targets to the intended claims. Full formalization does not show that the chosen formal statement describes the intended mathematics.

## Reporting

Report completion as **Protocol_D full formal verification relative to the declared foundations and checking system**. State which mathematical statements were checked and what remains trusted.
