# Protocol_A: tracked verification

Framework edition 2 | November 13, 2026

## Completion standard

Produce an explicit mathematical argument whose external inputs are identified published theorems, with checked applications and reproducible computational evidence. Maintain enough versioned evidence for another researcher to inspect the work. The author performs the required mathematical checks. Independent review is welcome but is not a condition of Protocol_A completion.

A completion claim means the following requirements have been met. It does not mean independent review, formal verification, or freedom from error. An unresolved mathematical premise must appear in the stated conditional result. It cannot be omitted to declare the unconditional target complete.

## Fix the target and trust boundary

Record the target statements, ambient objects, quantifiers, parameter ranges, intended bounds and representations in `PROJECT.md`. List any deliberately conditional assumptions. Name the manuscript, computational artifacts, release destinations and restrictions. Treat the project brief as a scope agreement, not a proof.

Use published external theorems after checking their actual statements. Record the work, publication, exact edition or revision, theorem location, definitions needed for the application, and the version actually read. Compare the final published statement and applicable corrections. An inaccessible final text remains an open source check. A preprint, software output or assertion by another agent is not a published theorem. Prove any needed unpublished input in a linked project argument or label the result conditional on it.

Published proofs need not be reconstructed in full without a concrete concern. Inspect proof passages when a statement or convention is ambiguous. If an objection affects a required published result, record and resolve its impact rather than treating publication as an answer.

## Keep one inspectable inventory

Use a single ledger or a small set of linked tables for claims, source applications, computations, findings and releases. Give entries stable identifiers. Record all substantive internal dependencies and external inputs, including uncited standard facts. Group repeated applications only when the same justification covers them, and list their consuming locations.

For each substantive application, state what is available, what is needed, and why they match. Identify the objects and maps actually used. Check hypotheses, domains, quantifiers, local conditions, exceptional cases, normalization, signs, coefficient rings, uniformity, parameter choices and limit order where applicable. An elementary identification may be proved directly in the manuscript. Do not create a separate record for every algebraic operation.

Make connecting arguments explicit. An exact sequence is not automatically an isomorphism. A rational identity need not hold integrally. Independently available witnesses need not exist simultaneously. A bound for each fixed parameter need not be uniform. A theorem's name or a matching conclusion does not settle these questions.

The author checks that the title, abstract, main results and corollaries are supported by the complete argument. Record the proof locations and the conclusions they support. No separate independent reconstruction or passage-by-passage coverage index is required in this framework.

## Make constructions and computations explicit

Specify every constructed object's domain, constants, parameters, algorithms and output representation. Prove required existence and termination. A finite unambiguous generator may describe an impractically large object, but distinguish a generator from a full expansion.

For each essential computation, preserve the specification, input files, program or certificate, relevant tool versions, invocation, output and file hashes. Explain why the check establishes the mathematical assertion consumed by the proof. Reproduce the essential check from the release inputs. Examples or sampled tests do not establish a universal claim.

Separate search from verification where feasible. Test an essential checker on deliberately invalid data when an appropriate negative test exists. Describe any unchecked software or numerical assumptions. External checking recorded as an axiom is an additional formal assumption, even if the computation is convincing informally.

## Track findings and changes

Register every received substantive objection, including unfavorable human and model reviews. Record the exact claim questioned, the affected version, the evidence considered, the resolution and any remaining work. Resolve by a demonstrated repair, a reasoned rebuttal, or an explicit change to the claimed scope. Duplicates may point to the same resolution. Lack of a reply is not resolution.

Separate an actual gap from a review not yet performed and from a source-access problem. Search prior evidence before claiming that a justification never existed. Record separately whether a valid earlier argument has been incorporated into the current manuscript. Protocol_A allows author resolution, and the record must say when that is the only review performed.

Bind evidence to file hashes or immutable revisions. After changes, recheck the affected applications and consumers, even when a consumer's wording did not change. Preserve unaffected evidence. Keep earlier verdicts and append corrections; do not replace their hashes to suggest they reviewed a later argument.

## Close a research release

The author checks the assembled proof after the last substantive repair. Confirm that every announced claim has a supporting argument, every necessary external input is qualified, essential computations pass, and no known required mathematical or source check remains open. Correct every current occurrence of a rejected assertion within the affected scope.

A release is a tagged commit containing the manuscript in TeX and PDF, the inventory, the findings ledger, and commands that reproduce the computations. Record the version, date, review scope and remaining limitations. Each release that changes the main result increments the version number and includes a complete manuscript, not a note against an earlier one.

A cumulative research handoff is optional and belongs at milestones, not at every release. Exclude conversations, credentials and unrelated private material, and do not redistribute source material without authority.

Report completion as **Protocol_A tracked author verification**. Identify any additional review separately and at its actual scope. No schema check, successful build or favorable agent response proves mathematical correctness.
