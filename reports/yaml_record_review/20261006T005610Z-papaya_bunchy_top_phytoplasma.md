# YAML Record Review: Papaya bunchy top phytoplasma

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/papaya_bunchy_top_phytoplasma.yaml`
- Started UTC: 2026-10-06T00:49:44Z
- Finished UTC: 2026-10-06T00:56:10Z
- Verdict: needs curation

## Target

Reviewed the complete 54-line generated `TaxonRecord` for `NCBITaxon:1034893`, label `Papaya bunchy top phytoplasma`, rank `SPECIES`, domain `BACTERIA`. The record has parent `NCBITaxon:3042590`, ten root-first ancestors, genetic code 11, `grounding_status: EXACT`, `mapping_status: SEEDED`, and `strain_count: 0`. It contains one NCBITAXON NAME attestation and one seed event, without synonyms, nomenclature, taxonomy mappings, strain listings, literature evidence, discussions, or causal graphs.

This verdict concerns an unresolved upstream biological-classification conflict, not a transcription error in the generated YAML. The record accurately carries the pinned and live NCBI taxonomy. It must not be locally reparented or treated as an authoritative equivalence between all phytoplasmas associated with a similarly named papaya disease.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/papaya_bunchy_top_phytoplasma.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/papaya_bunchy_top_phytoplasma.yaml --out /private/tmp/papaya-bt-validation.tsv`: exit 0; one file, zero errors. The complete result TSV contains only its header.
- Structured reads reconciled the full backbone row, every lineage entry, seven source inventories, the unique PATHS entry, scope row, source attestation, and embedded seed event. This is a bounded source comparison, not the corpus reproduction gate.
- Complete native JSON and TSV candidate rows were read and reconciled against the ignored-inclusive search addresses; no candidate address was left unread. Live NCBI Taxonomy EFetch and Datasets responses and metadata for all 20 exact-taxon Nuccore hits were inspected. A truncated five-record XML read was replaced by a complete compact structured read before judging it.
- Not checked: `just verify-corpus`, `just qc`, full tests, full-corpus strict validation, full history validation, provenance hashes, rendered-product drift, README statistics, publication budget, and vendored sync. These wider gates were not run for this report-only review. No replacement focused gate is claimed.
- No causal-edge evidence, LPSN identifier, GTDB mapping, or iModulonDB claim is present; those claim-specific checks are not applicable.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221736` and live [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1034893) agree on the identifier, exact label, species rank, parent, bacterial domain, and genetic code. [Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034893&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034893) confirm the lineage. Its IDs are 1, 131567, 2, 1783272, 544448, 31969, 186329, 2146, 33926, and 3042590, ending at `16SrI (Aster yellows group)`. The pinned inventory supplies the root entry, also included in Datasets.

The native scientific-name row is `data/catalog/ncbi_names-0005.jsonl.gz:31139`. Neither the pinned row nor the live response supplies an alternative name for this target. Exact-ID checks in the local type-material, merged-ID, and dropped-ID inventories found no target row. The backbone has no children of this taxon. These are bounded source checks, not claims that no alternative classification exists in the literature.

The disease wording is not a unique biological identifier. Complete local rows distinguish `NCBITaxon:65596` (papaya bunchy top disease rickettsia), `NCBITaxon:400090` (Papaya bunchy top-like phytoplasma), and the higher grouping `NCBITaxon:590433` (16SrXVII, Papaya bunchy top group). They are not synonyms of this record. The NCBI species node resolves unambiguously, but its associated sequence set is not biologically homogeneous on the inspected classification evidence; see M1.

## Evidence

The NCBITAXON attestation's count of one NAME traces to the 2026-09-13 snapshot. `curation/seed_scope.tsv:322038` gives the matching one-source attested rule; `data/taxa/PATHS.tsv:14206` uniquely maps the ID to this stem. The embedded event at `2026-09-13T17:54:04Z` matches that provenance. There is no claim that the count denotes strains, isolates, sequences, or disease observations.

The exact query `txid1034893[Organism:noexp]` returned 20 Nuccore IDs. Complete metadata, references, source qualifiers, and feature annotations were read, excluding nucleotide bases and translated sequences. All 20 carry `taxon:1034893` and the current 16SrI lineage. They divide into the following accession-specific evidence sets:

| Accessions | Native biological context | Interpretation |
|---|---|---|
| JF781307.1, JF781308.1, JF781311.1 | Cuban papaya isolates BTSpHav35-IB, BTSpLT138-IX, BTSpLT114-IZ; each 1,246 bp partial 16S rRNA; collected in 2009 | The directly inspected 2011 primary report specifically identifies JF781308 and JF781311 as group 16SrI sequences. |
| JF781309.1, JF781310.1 | Cuban papaya isolates BTSpLT01-IIN and BTSpHav02-IIA; 1,247 and 1,248 bp partial 16S rRNA | Isolate suffixes and literature-search leads suggest a further group-II assignment issue, but suffixes alone are not a classification result. The relevant 2013 article was inaccessible, so this is a follow-up lead, not the basis of M1. |
| KP722520.1, KP722521.1, KP722522.1 | Clones BTSp 45-IB, BTSp Emp 46-IB, BTSp Trial 47-IB; each 1,246 bp partial 16S rRNA; Cuba, 20-Feb-2011 | Source notes explicitly state subgroup 16SrI-B. Hosts are papaya, Empoasca papayae, and postinoculated papaya seedlings respectively. Unpublished reference titles do not independently prove a transmission mechanism. |
| OP123558.1, OP123559.1 | Nigerian NGPBT-15 from tomato and NGPBT-19 from jute mallow; 1,530 bp 16S rRNA/intergenic-spacer fragments | These records cite the Inaba study whose author-hosted technical abstract classifies NGPBT as 16SrXII-O, conflicting with their current NCBI taxon lineage. |
| OP123560.1 through OP123564.1 | NGPBT-12, -13, -15, -19, -20 respectively; 1,238 bp rplV/rpsC fragments | Source hosts are papaya, papaya, tomato, jute mallow, papaya. Separate markers are not separate culture deposits or complete genomes. |
| OP123565.1 through OP123569.1 | The same five NGPBT designations and host order; 2,064 bp rpl15/secY/adk fragments | Same study reference and classification concern; source comments identify Sanger sequencing, not genome assemblies. |

The complete text of [Acosta et al. 2011, New Disease Reports 24:29](https://www.ndrs.org.uk/article.php?id=024029), DOI `10.5197/j.2044-0588.2011.024.029`, was inspected. It directly supports a Cuban group-16SrI phytoplasma occurrence and the JF781308/JF781311 accession link, while distinguishing earlier group-16SrII disease reports. Its observations must not be generalized to every organism called papaya bunchy top phytoplasma. Figures were not independently inspected.

The complete author-hosted [USDA ARS publication record and technical abstract for Inaba et al. 2023](https://www.ars.usda.gov/research/publications/publication/?seqNo115=397640), DOI `10.1094/PDIS-09-22-2192-PDN`, were inspected. The authors classify Nigerian NGPBT as a Candidatus Phytoplasma convolvuli-related 16SrXII-O lineage and report matching marker sequences across papaya, tomato, and jute mallow. This is an explicit classification conflict with the NCBI lineage attached to the OP accessions. The connection is supported by their source designations, hosts, and cited study, not merely the shared disease name. It does not show that the Cuban sequences should be moved with the Nigerian ones.

Publisher requests for the 2013 Crop Protection paper, DOI `10.1016/j.cropro.2012.11.016`, returned HTTP 403; its full text and accession-specific assignments were not inspected. The 2023 Plant Disease publisher URLs also returned HTTP 403; the author-hosted technical abstract supplied the inspected evidence above. An exact DOI PubMed ESearch returned zero hits and a phrase-not-found warning; its attempted follow-on fetch stopped without an article. No PMID was invented. The 2011 Wiley URL was unavailable, but the primary NDRS article was accessible. Search snippets were treated only as leads.

## Completeness

`strain_count: 0` is consistent with the BacDive inventory and absence of descendant taxa. It is not a statement that no field isolates, molecular clones, or nucleotide records exist. None of the 20 inspected sequence metadata records provides a culture-collection deposit. The record therefore does not need invented strain rows or genome links to represent these markers.

Seven exact-taxon inventory reads found no BacDive, LPSN, GTDB, GOLD KGX, MediaDive, Madin, or BactoTraits assertion. An exact-taxon Assembly search returned zero with a phrase-not-found warning; this is not an exhaustive claim that no genome exists under any reclassified name. Optional literature evidence and causal graphs are not mandatory for a seeded record, and the available host observations do not license a whole-taxon disease or vector mechanism.

Ignored-inclusive, hidden-inclusive, compressed-content searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`, excluding `SOURCE.json` provenance descriptors. The ID/name/slug screen produced 26 matching rows; the disease-name screen produced 11. Every candidate native row was read. A further screen for JF781307-JF781311, KP722520-KP722522, OP123558-OP123569, the BTSp designations, and NGPBT-12/-13/-15/-19/-20 found zero matching lines in those same roots. These bounded absences include ignored files and do not cover unscreened external repositories.

Separate ignored-inclusive report/history searching and an exact-stem filesystem search found no earlier report for this target before this report was created. There is no local biological-classification resolution in the inspected target-related evidence. The consequential gap is the unresolved source identity/classification conflict, not absence of optional descriptive fields by itself.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

- **M1, major: the upstream taxon-associated sequence set spans conflicting phytoplasma classifications.** The generated parent and terminal lineage are 16SrI, faithfully matching NCBI. However, OP123558.1/OP123559.1 and the associated OP123560.1-OP123569.1 markers carry this same NCBI ID while their cited study's inspected author-hosted technical abstract identifies the Nigerian NGPBT lineage as 16SrXII-O. This is a material biological-scope conflict, not support for merging those lineages. The source-grounded ID/label match remains valid; the review cannot certify that every sequence under it denotes one coherent 16SrI taxon. The primary correction owner is NCBI Taxonomy/GenBank for the sequence assignments and taxon concept. Local refresh ownership is `conf/ncbi_taxdump.yaml` and the extraction workflow behind `scripts/extract_source_inventory.py`; `data/raw/ncbitaxon_taxa.tsv` and the taxon YAML are generated products. Any future curator-facing conflict annotation needs a maintained, tested input path consumed by `src/taxonmech/seed.py`, not a hand edit. No local lineage override, taxon split, scope removal, or replacement identifier is justified by this review alone.

No blocker was found in YAML validity, reference resolution, or fidelity to the identified NCBI source node. The additional possible group-II issue remains unresolved and is not counted as another independently established finding.

## Recommended Edits

1. Route M1 to an authorized upstream taxonomy/sequence-curation workflow, supplying the exact OP accessions, current taxon ID, and the Inaba study. Establish whether the Nigerian sequences require reassignment, whether the taxon concept requires revision, or whether another source correction is appropriate. Do not move the whole record to 16SrXII or infer an NCBI ID from a disease name.
2. Retain the existing NCBI lineage until its authority changes. After an authoritative correction, refresh the pinned NCBI inputs through `conf/ncbi_taxdump.yaml` and `scripts/extract_source_inventory.py`, inspect generated inventory changes, and regenerate through `scripts/seed_from_sources.py` / `src/taxonmech/seed.py`. Change `curation/seed_scope.tsv` only if the authoritative identifier or scope actually changes.
3. Before any biological enrichment, preserve the conflict in a supported curator-owned annotation workflow. If implementing such a workflow, add a maintained input and tests around `src/taxonmech/seed.py`; do not add an unconsumed overlay, change the global EXACT rule based solely on this case, or directly patch `discussions` in generated YAML. Keep lifecycle changes as proposed until human sign-off.

No recommended edit was applied. This review did not contact NCBI, authors, or other maintainers, or create GitHub items.

## Follow-up Checks

Re-fetch Taxonomy EFetch/Datasets and all affected GenBank source qualifiers after any upstream response. Compare accession-level classifications, not just the shared label. Obtain the 2013 primary article to determine the exact assignments of BTSpLT01-IIN and BTSpHav02-IIA; retain uncertainty until its text and accession mapping can be inspected. Independent sequence classification or alignment was not performed here.

For an authorized local refresh, inspect the inventory and scope diff, run the documented seed dry-run and canary workflow, then the same single-record schema and strict validators. Run `just verify-corpus`, `just qc`, history/provenance gates, and relevant extractor/seeder regression tests before accepting regenerated outputs. Those gates establish reproducibility and structure; resolution of M1 additionally requires authoritative biological evidence. This review alone is not grounds to promote the record to REVIEWED.

## Additional Notes

Numeric search collisions were excluded on their full native identities: Mycobacterium tuberculosis ERR1034893 in BV-BRC and ATB; Listeria monocytogenes samples SAMN10348933/SAMN10348938; Ignavibacteriaceae bacterium BACT-3 with SAMN31034893; Streptomyces sp. H39-C1 with assembly size 10348935; Streptococcus dysgalactiae subsp. equisimilis sample SAMEA1034893; Shigella sonnei samples SAMEA110348930-SAMEA110348939; and Campylobacter sp. OH-18-15554-2 sample SAMN10348930. Substring coincidences do not establish taxon, strain, sample, or assembly equivalence. Their quality flags were not transferred to this record.

The other session is closed. Git lists one worktree, the current repository, on `codex/record-review-extensimonas-20261003` at `b6a6508faca1388b88feb5740b1095e9f64cfdb8`; this is not a separate worktree. Tracked and staged diffs were empty before this report. The ignored-independent filesystem/PATHS reconciliation immediately before writing counted 625,960 records and 22,688 matched reports, including all 6,243 Eukaryota records, without duplicate record stems, duplicate report stems, or unmatched reports. This new report is additional coverage, not proof of whole-corpus completion.

Only this new report was written in the repository. Target YAML, source inventories, scope, history, prior reports, and Eukaryota records were left unchanged. No regeneration, lifecycle promotion, commit, or GitHub mutation was performed.
