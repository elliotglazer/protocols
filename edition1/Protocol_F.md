# Protocol_F: full formal dependency closure

Framework edition 1 | November 9, 2026

## Completion standard and trust boundary

Formalize every announced result and all mathematical dependencies down to an explicit foundational basis. Every essential computation must be justified through the declared verified checking path. No project-specific axiom, imported published-theorem axiom, externally attested computation, or unfinished proof may remain in the dependency closure of a completed target.

Foundational assumptions and the proof system's trusted implementation remain. State them precisely. Full formalization does not by itself prove that the chosen formal statement describes the intended mathematical claim or that every implementation component is flawless.

Formal dependency closure replaces a duplicate manual record for every internal inference. Independent statement, definition, computational-meaning and release audits remain required. This is a complete alternative framework, not a demand to maintain both a full formal dependency graph and every Protocol_D internal application record by hand.

## Agree on the targets and foundations

Record the exact intended mathematical claims, objects, quantifiers, uniformity, bounds, representations and deliverables in `PROJECT.md`. Identify all target declarations. Declare the foundational axioms, permitted classical principles, prover and kernel versions, libraries and checking path.

Independent reviewers compare the complete elaborated target types and all meaning-bearing definitions against the intended results. Check hidden arguments, coercions, instances, quantifier order, domains, nonvacuity, conventions and the interpretation of finite encodings. Proofs of weakened statements, alternate definitions or conclusions already assumed in the hypotheses do not satisfy the target.

Assess implications of the foundations for the advertised result. For example, a classical existence proof is not automatically an executable algorithm or an effective quantitative bound. Formalize the stronger conclusion when it is claimed.

## Close mathematical dependencies

Use existing formal library theorems where they prove the needed assertions. Pin their versions, inspect their complete types and relevant definitions, and check their actual transitive assumptions. A reputable library name or successful import is not a substitute for this check.

Any needed mathematical result unavailable in the selected libraries must be formally proved, replaced by a proved route, or left as explicitly incomplete work. Do not introduce it as an axiom because it is published, standard, expensive or difficult to formalize.

Maintain source attribution and an inventory of mathematical results used to develop or explain the formal proof. For each external theorem whose published identity is claimed, check the cited version, statement, definitions and relevant corrections. If a formal proof establishes a different variant, describe and prove that variant accurately rather than misattributing it. An inaccessible source or disputed citation cannot be used to justify a missing formal step.

All connecting arguments, changes of object, normalizations, limiting operations, specializations, existence and termination assertions must be proved within the formal dependency chain. Local proofs must use the same definitions and parameters that the final root consumes.

Audit root assumptions mechanically and independently. In Lean, `#print axioms` or equivalent inspection must show only the declared foundational assumptions. Check for `sorryAx`, unapproved axioms, hidden assumption parameters and unexpected trust introduced by tactics or evaluation backends. A source grep alone is insufficient. Check proof terms through the declared trusted path.

Clearly isolate incomplete experiments from accepted modules. Do not count them as completed theorems, and do not import them into the completed roots. Preserve them in the research history when useful.

## Verify computation end to end

External search programs may discover certificates, witnesses, decompositions or proof strategies. Their correctness need not be trusted when the output is independently verified by the formal proof.

Provide an exact specification of the certificate representation and a proved checker-soundness theorem. Prove that the actual certificate is accepted using the declared verification path. External assertions of successful execution, hash matches or exhaustive search are not mathematical axioms permitted by this framework.

If the claimed result concerns a released artifact, establish the link between its encoding and the formal mathematical object. Check the parser, numeral semantics, indexes, arithmetic and serialization assumptions relevant to that link. For a huge object supplied by a generator, formalize the generator's mathematical specification and any required termination and correctness properties. Do not call a symbolic or generated representation a complete expanded table.

Choose proof-producing or verified evaluation appropriate to the size of the computation. An unverified native evaluator may be used during exploration, but not as an undeclared substitute for final checking. Document the remaining software trust, including any compiler or runtime that the chosen checking mode truly relies on. Negative tests help detect engineering mistakes but do not replace the formal soundness and acceptance arguments.

## Review meaning, findings and changes

An author may prove a statement, but must not supply its sole independent semantic acceptance. Record non-author reviewers, model or human identity, reviewed files, prior exposure, scope and decisions. Multiple agent identities do not eliminate correlated errors.

Review important module interfaces, the source-to-formal translations and final target meanings. Verify that actual dependency extraction reaches the intended roots and approved definitions. A correct theorem about the wrong object is a specification failure.

Register every substantive objection, including objections to definitions, assumptions, encodings and source attribution. Resolve with a checked repair and corresponding semantic review, or a supported independent rebuttal. Formal build success does not dismiss a finding outside the scope of the formal statement. Preserve the original objection and earlier decisions.

Use one ledger linking targets, formal modules, source citations, statement reviews, computations, findings and releases. Reuse proofs and reviews at unchanged interfaces. Recheck affected consumers after changes to definitions, axioms, libraries, compiler or checking mode. Do not repeat reviews of unaffected proofs solely because line numbers moved.

## Final audit and release

A non-author reviewer must verify that the final formal roots express every announced claim and that their dependency closure contains only the approved foundations. Rebuild and check from a clean checkout with pinned dependencies. Record complete commands, target names, axiom reports, certificate identities and the verification environment. Inspect the exact released sources and outputs.

Make the trust statement specific. Identify the logical foundations, kernel and any remaining trusted implementation components, and distinguish their correctness from the mathematical result checked within that system. Independent implementation or a second prover may add assurance, but is not an automatic extra requirement of Protocol_F.

Synchronize the formal files, manuscript and PDF if supplied, README, source inventory, axiom report, findings, artifact catalog and cumulative research handoff. Include relevant derivations, failed approaches, repairs, source and computational provenance, and reviews. Exclude conversations, credentials and unrelated private material. Record restricted or missing historical evidence without treating it as a substitute for a formal proof.

Bind version, date, source revision, dependency pins, foundational declaration, build and verification commands, formal roots, artifacts and hashes in the release record. Preserve old releases, check links and read back authorized destinations. Do not publish a result as complete while a required semantic audit, dependency check or artifact verification remains open.

Report completion as **Protocol_F full formal verification relative to the declared foundations and checking system**. Explain what mathematical statements were checked and what remains trusted. Completion is not a guarantee against an incorrect specification or a defect in that trust base.
