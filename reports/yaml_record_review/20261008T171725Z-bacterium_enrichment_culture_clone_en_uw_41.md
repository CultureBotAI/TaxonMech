# YAML Record Review: bacterium enrichment culture clone En_UW_41

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_41.yaml`
- Started UTC: 2026-10-08T17:09:44Z
- Finished UTC: 2026-10-08T17:17:25Z
- Verdict: pass

## Target

One complete generated `TaxonRecord` was read and reviewed: `NCBITaxon:1036427`, bacterium enrichment culture clone En_UW_41. It carries rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:48479`, grounding `EXACT`, mapping status `SEEDED`, genetic code 11, and zero associated strain records. The species rank is NCBI's rank for this environmental clone, not evidence of a formally named species or pure isolate.

The identifier, label and filename resolved to exactly one target in the ignored-inclusive filename inventory of `data/taxa/`, `reports/yaml_record_review/` and `history/`. No prior report for this stem was found in that inventory. The review does not change generated YAML, scope, source inventories, history, or status.

## Validation

The following focused commands completed successfully, using the existing environment with `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `just validate data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_41.yaml`: pass, no issues found.
- `just validate-strict data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_41.yaml --out /private/tmp/uw41-strict.tsv`: pass, one file scanned, zero files with errors and zero error rows. The complete output TSV contained only its header.
- Read-only structured comparisons of the complete record, backbone row, all four ancestors, source attestations, scope entry, path index, and seed event: pass.
- Direct primary taxonomy and linked sequence reads: completed; details and scope limits are below.

Not checked: full-corpus `just verify-corpus`, `just provenance-check`, `just validate-history`, `just qc`, `just test`, vendored synchronization, generated-site drift, and global statistics gates. This individual review does not claim to establish corpus-wide reproducibility or publication readiness. No narrower reproduction/history gate was invented. The embedded seed event was inspected against the available source and scope rows; no matching standalone history artifact was identified in the bounded search.

`just validate-products` is not applicable: this record contains no curator-added graph. iModulonDB was not run: the YAML asserts no gene, regulator, pathway, or expression module, and this environmental clone was not resolved to a covered strain/dataset. That is not a claim that iModulonDB lacks related data.

## Identity and Grounding

The pinned evidence is `data/raw/ncbitaxon_taxa.tsv:222429`, scientific-name row `data/catalog/ncbi_names-0005.jsonl.gz:31973`, `data/taxa/PATHS.tsv:14936`, and `curation/seed_scope.tsv:322676`. Each complete relevant row was inspected. The backbone and YAML agree on the identifier, scientific label, rank, parent, code, snapshot date, and empty synonym sets. The four root-first ancestors also match: root, cellular organisms, Bacteria, environmental samples. The complete backbone comparison found no direct children for this target.

Live [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036427&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036427) agree with that identity and placement. EFetch supplies species rank, parent 48479 and genetic code 11, with no additional names in this response. Datasets carries all four ancestor IDs, including root. EFetch's root omission from `LineageEx` is a response-format distinction, not lineage drift. Its environmental-samples division does not conflict with the bacterial domain.

Exact scans of the pinned type-material, merged-ID and dropped-record inventories found no target entry. `EXACT` therefore describes the supported NCBI identifier/name grounding, not biological resolution beyond the source's environmental-clone placement. No genus, cultured-species identification, taxonomic merge, or strain equivalence is inferred from neighboring clones.

## Evidence

The sole `NCBITAXON` attestation is supported by the pinned scientific-name row: one `NAME` assertion, not one genome or cultured strain. Its 2026-09-13 snapshot note matches the backbone. The 2026-09-13 seed event and its scope reason agree with the maintained scope row. `SEEDED` remains appropriate; this read-only report does not confer human review status.

An exact non-expanded Nuccore query for `txid1036427[Organism:noexp]` returned one UID, 336092268. Its complete [HQ630100.1 GenBank XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=336092268&rettype=gb&retmode=xml), including features and sequence, identifies this taxon and clone. It contains a 347-base partial `nosZ` sequence from an anode biofilm, with an environmental-sample qualifier and a Na2S2O3-supplemented mineral-medium note. Both CDS ends are partial, codon start is 3 and translation table is 11. No strain, culture-deposit or geographic source qualifier appears. The associated study is marked unpublished; the direct submission is dated 17 November 2010. These are clone-fragment annotations, not proof of a pure culture, measured enzyme activity, whole-genome content or organism-level denitrification.

The complete linked [AEI00758.1 protein XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&id=AEI00758.1&rettype=gb&retmode=xml) was independently opened and read. It contains 115 amino acids and explicitly traces to the target's partial HQ630100.1 CDS. Declared and actual sequence lengths match, and the submitted CDS translation exactly matches this protein sequence. The DNA has an ambiguous W at base 327 and the protein has X at residue 109. This is annotation-consistency checking, not an independent translation, alignment or biochemical assay. The protein's computational PRK02888/CDD:235082 region ends at residue 108; its annotation does not establish experimental validation of this clone. Neither the fragment nor its ambiguity is asserted in the YAML.

The cached 164-page [Vilar Sanz dissertation](https://dugi-doc.udg.edu/bitstream/handle/10256/12459/tavs1de1.pdf?sequence=5), dated 2015, was searched for this clone and accession, with no extracted-text hit. Printed pages 54 and 92 were read in full again. Page 54 places HQ630100 within the stated enrichment-sequence accession range; page 92 warns that a single DGGE band does not establish culture purity. This supports study context only, not a clone-to-species assignment. The bounded search does not cover every rasterized label or supplementary object.

Exact searches for HQ630100 and En_UW_41 in the main HTML of the related [PLOS ONE article](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0063460) returned no matching text. This was not a supplement audit, and community-level results were not transferred to this clone. Exact web queries for the accession and protein, plus a clone query excluding the already inspected NCBI Taxonomy listing, returned no results. Those search outcomes are discovery limits, not proof of literature absence.

## Completeness

The populated taxonomy, provenance and status fields are complete enough for the supported seed scope. Optional synonyms, nomenclature, GTDB mappings, strain/deposit records, genomes, traits and causal graphs are correctly left unfilled where no target-specific support was established.

All seven relevant raw inventories were scanned for the exact taxon identifier: BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits returned no target rows. The zero strain count agrees with the available BacDive evidence; it does not assert that the organism cannot be cultured.

The compressed-content search used `rg --no-ignore --hidden -n -z -i` over `data/raw/`, `data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`, `data/seqcode/`, `data/straininfo/`, `data/atb/`, `curation/` and `history/`. Identifier, slug and clone-label searches, then an expanded search adding HQ630100, AEI00758, the submitted study title and the related PLOS DOI, each returned four rows. All four complete candidate rows were inspected. Source metadata excluded from that content scan were separately read from all five applicable `SOURCE.json` files; no target identity match was found. History filenames were also searched independently of ignore rules.

Three content matches are the backbone, scientific-name and scope evidence above. The fourth, `data/catalog/ncbi_genbank-0060.jsonl.gz:24072`, is not a target genome: GCA_948730605.1 belongs to an uncultured Eubacteriales bacterium, taxon/species taxon 172733, isolate MGBC149337. Its total genome length happens to be 1036427, while its ungapped length is 1035927. That numerical collision cannot supply a strain/genome link for this record.

The exact NCBI Assembly query returned zero items with a phrase-not-found warning. This establishes only the outcome of that particular search; it does not prove universal assembly absence. No whole-genome or deposit association was established from the inspected sources. A neighboring clone's accession, protein or UniProt archive membership was not adopted for this target.

## Findings

None found in the supported YAML assertions.

Counts: 0 blocker, 0 major, 0 minor.

The external sequence ambiguity and unresolved organism-level identity limit possible future enrichment, but do not contradict the current taxonomy-only record. No required field, broken stored reference, unsupported phenotype, misplaced citation or status promotion was identified.

## Recommended Edits

None required. Preserve the generated YAML and `SEEDED` status.

Any future NCBI identity correction belongs first at the authority, then in the pinned ingestion workflow owned by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Seeder behavior belongs in `src/taxonmech/seed.py` with focused tests; scope changes belong in `curation/seed_scope.tsv`. These are ownership routes, not requested changes. Do not hand-edit generated records or add traits from the fragment, medium note, study title, or neighboring clone evidence.

## Follow-up Checks

No blocker remains for this record-level verdict. Before future sequence-based biological curation, resolve the ambiguous base against primary sequence evidence, preserve partial-sequence qualifiers, and establish an explicit organism/deposit link. A computational protein-region label or single DGGE band is insufficient.

After any authorized maintained-input change, use the documented canary workflow, inspect the generated target, rerun its schema and strict validators, and then run the applicable corpus reproduction, provenance, history and QC gates. Broader source and supplementary-material searches remain optional discovery work, not prerequisites for accepting the present taxonomy seed.

## Additional Notes

This is one sequential individual review, not a batch verdict. Eukaryota and all other records were untouched. Existing worktrees and unrelated files were preserved. No curation event, history artifact, generated product, outbound message, paid research request, or GitHub mutation was created.

The target SHA-256 was unchanged before and after review: `dbae7ba89f6028acbbeba5e22ba8cebe16286e7e5c6c09085ff18caeb9af1a66`.

One new timestamped report is the only repository write for this review. Search absence statements above are bounded to the named roots, exact queries and inspected source responses; they are not an exhaustive census of all external knowledge about the clone.
