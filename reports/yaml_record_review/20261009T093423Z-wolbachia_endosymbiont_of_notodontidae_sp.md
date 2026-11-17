# YAML Record Review: Wolbachia endosymbiont of Notodontidae sp.

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_notodontidae_sp.yaml`
- Started UTC: 2026-10-09T09:29:57Z
- Finished UTC: 2026-10-09T09:34:23Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` denotes `NCBITaxon:1036670`, Wolbachia endosymbiont of Notodontidae sp. It carries rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2640676`, genetic code 11, eleven root-first ancestors, `EXACT` grounding, `SEEDED` mapping status and zero linked strains. Its one NCBITAXON attestation counts one NAME from the 2026-09-13 snapshot. The sole embedded history event records seeding on 2026-09-13T17:54:04Z.

The target was uniquely resolved by an ignored-independent filename inventory and read in full. This is an individual judgement of this file, not an inherited verdict from adjacent Wolbachia records. The bacterial taxon is not the Notodontidae host family record.

## Validation

Both documented focused validation implementations completed with exit 0:

```bash
UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/wolbachia_endosymbiont_of_notodontidae_sp.yaml
UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline python scripts/validate_strict.py data/taxa/bacteria/wolbachia_endosymbiont_of_notodontidae_sp.yaml --out /private/tmp/taxonmech-wolbachia-noto-review-strict.tsv
```

- Schema result: `No issues found`.
- Strict result: one file scanned, zero files with ERROR, zero ERROR rows. The complete temporary TSV was header-only.
- Structured comparison of the complete YAML against the pinned backbone, all eleven ancestors, supplied synonym fields, all attestations, path index and scope/history text passed. These checks are not a replacement for corpus reproduction.
- Exact-field scans found no target rows in `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv` or `data/raw/dropped.tsv`. The backbone had no children of the target. These are results for the inspected snapshots, not universal absence claims.
- The related marker JF902215.1 declares and contains 628 bases with no non-ACGT characters. Its full source, gene and CDS features were read. This length/alphabet check was not an independent translation, alignment, strain typing or identity-equivalence test.
- Not checked: full-corpus `just verify-corpus`, `just qc`, all-record strict validation, complete test suite, provenance gates, generated-page drift, or full history validation. The record has no curator-added graph grounding requiring the OAK product-label gate. No separate history entry was created or validated because review does not authorize curation-history mutation.

The target SHA-256 before and after evidence gathering was `bfa6da27747ad39b39b36f591d53d16c67d2afa43f70bc2630fd8a751069da90`.

## Identity and Grounding

The complete [NCBI Taxonomy EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036670&retmode=xml) and [Datasets taxonomy response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036670) confirm the target's exact identifier, label and species rank. EFetch confirms its parent and code; the two responses agree with the carried chain through Bacteria, Pseudomonadati, Pseudomonadota, Alphaproteobacteria, Rickettsiales, Anaplasmataceae, Wolbachieae, Wolbachia and unclassified Wolbachia, with root and cellular organisms included in the YAML. No name replacement or alternative name was supplied.

`EXACT` describes grounding to that authority identity. It is not evidence that every Wolbachia sampled from a notodontid host is the same organism, or that this host-associated label is a formally described species. The record correctly preserves `SEEDED`, without implying human review.

The host-family sequence query returned a different taxon: [NCBITaxon:1094269](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1094269&retmode=xml), Wolbachia endosymbiont of notobiolep01 biolep01. Its complete EFetch and Datasets responses also resolve as a species under unclassified Wolbachia. The inspected authorities do not supply a merge or equivalence with 1036670. Similar host context is not sufficient to collapse these identifiers.

## Evidence

The seeded assertions agree with these complete local source rows:

| Source address | Evidence checked |
| --- | --- |
| `data/raw/ncbitaxon_taxa.tsv:222573` | Exact identity, rank, parent, code, snapshot, NCBI attestation and empty supplied synonym fields |
| `data/catalog/ncbi_names-0005.jsonl.gz:32117` | Scientific name and target taxon identifier |
| `curation/seed_scope.tsv:322820` | Admission date and one-source NCBI reason reflected in seed history |
| `data/taxa/PATHS.tsv:15091` | Exact identifier-to-slug mapping |

The complete GenBank XML for [JF902215.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902215.1), UID 334360787, identifies taxon 1094269, host Notodontidae sp., voucher `BIOUG<CAN>:BLPCI211-08.w` and BOLD `ASLEP001-10.COI-5P`. Its source records a 7 December 2007 Costa Rican collection in Guanacaste, Sector Santa Rosa, Sendero los Patos. The sequence is a partial COI CDS, with translation table 11, codon start 2 and protein AEG78036.1. It is not a genome assembly or culture deposit. No assertion in the target YAML cites this accession.

The marker's bibliographic text names Smith's barcoding study as unpublished and records a 1 May 2011 direct submission. The published [Smith et al. paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0036514), PMID 22567162, DOI 10.1371/journal.pone.0036514, was verified through its complete PubMed abstract, selected publisher methods/discussion and supplementary Table S2. The methods distinguish bacterial COI from insect barcodes and explain the specimen-associated identifiers; they do not establish species equivalence from a shared host family.

Table S2's `Wolbachia CO1` sheet, physical row 162, explicitly joins JF902215, ASLEP001-10, BLPCI211-08.w, 628 bases, the notobiolep01 biolep01 label and Notodontidae context. Rows 43 and 115 instead concern Microcharops and Mesochorus-associated sequences, with Notodontidae in their ecological notes. Those are not this specimen. All four sheets were searched across all cell values for the host family and exact marker/specimen terms, and every matching row was read in full. No explicit target-ID equivalence was established.

The additional PubMed hit [Avtzis et al. 2019](https://pubmed.ncbi.nlm.nih.gov/31550003/), DOI 10.1093/jee/toz216, concerns screened Thaumetopoea pityocampa populations in Greece. Its complete abstract reports no detections among its 28 sampled individuals. That bounded negative survey does not refute this bacterial taxon or establish absence across Notodontidae. Its full text was not reviewed, and no reproductive or infection-status claim was transferred to the YAML.

The expanded local search also returned the sibling's backbone row `data/raw/ncbitaxon_taxa.tsv:235315`, admission row `curation/seed_scope.tsv:333628` and name row `data/catalog/ncbi_names-0005.jsonl.gz:47544`. They consistently identify 1094269, not the target. A fourth additional hit, `data/catalog/ncbi_genbank-0062.jsonl.gz:16840`, is assembly GCA_963634035.1 under taxon 1869227: 1094269 occurs as its ungapped genome size. The complete row was read and excluded as a numeric collision, not treated as a Wolbachia genome.

No unsupported evidence, mismatched citation or over-scoped claim was found in the target. iModulonDB was not applicable because the record asserts no gene, regulatory module, expression dataset or phenotype.

## Completeness

The record is complete enough for its generated NCBI-attested scope. Optional synonym, nomenclature, strain/deposit, genome, taxonomy-mapping and causal-graph entries are correctly unasserted. The inventory count of zero strains is not a statement that no biological strain or sequence exists. A related specimen voucher and a partial CDS do not establish a missing culture-deposit or genome link.

Ignored files and compressed inventories were included through `rg --no-ignore --hidden -n -z -i` over `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. The initial pattern matched the target numeric identifier and space/underscore forms of its label/slug. The expanded pattern was:

```text
\b1036670\b|wolbachia[ _]endosymbiont[ _]of[ _]notodontidae\b|\b1094269\b|\bnotobiolep01\b|\bJF902215(?:\.1)?\b|\b334360787\b|\bBLPCI211[ _-]08\b|\bASLEP001[ _-]10\b
```

The first pass returned three target source rows. The expanded pass returned seven rows: those three, three sibling rows and the genome-size collision described above. All seven complete TSV/JSON records were read, including every field rather than only their search projections. No additional target association was established in this bounded search. The seven raw supplemental taxon inventories for BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits also yielded no exact target rows.

Five discovered `SOURCE.json` files were parsed in full in both passes, with no matching values or keys. Ignored-independent filename searches covered `data/taxa`, `reports/yaml_record_review` and `history`; they found the target YAML but no earlier target report or target-named separate history file. Absence statements here cover these explicit roots and terms, not every remote database or alternate spelling.

Live Nuccore and Assembly queries for `txid1036670[Organism:exp]` both returned zero with phrase-not-found warnings. Those responses do not establish global absence or invalidate a taxonomy record that resolves directly. The broader Wolbachia-plus-Notodontidae Nuccore query returned the one sibling marker inspected above; its translation included host-family organism/all-fields alternatives. The analogous quoted PubMed query returned only the Greek population study. None of these index responses authorizes silently merging the target or inferring universal host effects.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected record and evidence scope. Identity, lineage, provenance, source count and seed history agree. The precise relationship between the host-family target and the separately registered notobiolep01 taxon remains unestablished; because the YAML asserts no equivalence or sequence link, that uncertainty is not a demonstrated record defect.

## Recommended Edits

None required. Preserve the generated YAML, `SEEDED` status and history. Do not add JF902215.1 or collapse taxon 1094269 into this record based only on its Notodontidae host qualifier.

Any future authoritative taxonomy correction belongs in the pinned NCBI intake through `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`; a demonstrated projection defect belongs in `src/taxonmech/seed.py` with a focused regression test. Admission changes belong in `curation/seed_scope.tsv`. Generated records and pages must not be hand-edited.

## Follow-up Checks

No unresolved blocker requires immediate action. If equivalence is later asserted, require explicit authority or specimen-level evidence and recheck both taxon identities and any merge status before making a join. For an authorized source/projection correction, run the focused regression test, `just seed-canary NCBITaxon:1036670`, inspect the emitted record, repeat both validators, then run `just verify-corpus` and the authoritative `just qc`. No regeneration was performed by this review.

## Additional Notes

The review used branch `codex/record-review-extensimonas-20261003` at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Its sole new repository artifact is this report. This review did not change source inventories, YAML, generated pages, curation history, statuses, GitHub objects or worktrees, and did not contact people or use paid research. Eukaryota records and reports were not changed.

The publisher-linked supplement was downloaded to `/private/tmp/taxonmech-wolbachia-noto-table-s2.xls` and compared byte-for-byte with the cached workbook read for this target. Both have SHA-256 `8df12e221a835a4504e4ce0a30e5aed17a4e906c9bc2e1bffcd4113adf0f0a1e`. Its internal header says Table S1, but the publisher identifies the linked file `pone.0036514.s003.xls` as Table S2; the actual sheet and row addresses above identify the inspected evidence unambiguously. The publisher article was not read in its entirety, BOLD was not independently revalidated, and no sequence phylogeny or universal host prevalence was inferred.
