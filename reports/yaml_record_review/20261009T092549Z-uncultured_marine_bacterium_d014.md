# YAML Record Review: uncultured marine bacterium D014

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_marine_bacterium_d014.yaml`
- Started UTC: 2026-10-09T09:16:30Z
- Finished UTC: 2026-10-09T09:25:49Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` identifies `NCBITaxon:103667`, uncultured marine bacterium D014. It carries rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:150608`, genetic code 11, `EXACT` grounding, `SEEDED` mapping status and `strain_count: 0`. Its five root-first ancestors terminate at marine bacteria D ensemble. One NCBITAXON attestation represents one NAME in the 2026-09-13 snapshot. The sole embedded curation event records seeding, not a completed scientific review.

This is an independent review of this file. The filename search uniquely resolved the target; neighboring clone reports did not determine its verdict. Generated records are not maintained correction surfaces.

## Validation

The following focused commands completed successfully, including a final repeat before reporting:

```bash
UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/uncultured_marine_bacterium_d014.yaml
UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline python scripts/validate_strict.py data/taxa/bacteria/uncultured_marine_bacterium_d014.yaml --out /private/tmp/taxonmech-marine-d014-review-strict.tsv
```

- LinkML validation: `No issues found`, exit 0.
- Closed-schema validation: one file scanned, zero files with ERROR, zero ERROR rows, exit 0. The complete temporary TSV contained only its header.
- Read-only structured source comparison checked identifier, label, rank, parent, genetic code, every lineage entry, synonyms, all attestations, scope admission and embedded seed history. All compared values agreed. This check is not a replacement for corpus reproduction.
- Exact-field scans of `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv` and `data/raw/dropped.tsv` returned no rows for this taxon. The complete backbone scan returned no children of this taxon. These are bounded snapshot results, not claims about all external databases.
- Marker annotation consistency: AF177554.1 declares 559 bases and contains 559; its submitted rRNA transcription matches the DNA after case normalization, with no non-ACGT characters. Only source and rRNA features are present. No independent alignment, assembly validation or phylogenetic reconstruction was performed.
- Not checked: full-corpus `just verify-corpus`, `just qc`, all-record strict validation, full history validation, provenance gates, generated-site drift and the complete test suite. No graph-node additions require the OAK product-label gate here; it was not run. No new history record was created or separately validated, because this read-only review does not authorize curation history mutation.

The target SHA-256 before research and before report creation was `06b7dbddd0803be8b65016987728d25da5a4ba472d7cf3ff5c9b1cbe4c592c27`.

## Identity and Grounding

The complete [NCBI Taxonomy EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103667&retmode=xml) and [NCBI Datasets taxonomy response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103667) identify this exact label and species rank. EFetch confirms parent 150608 and genetic code 11; Datasets supplies the complete ancestor identifiers including root. Together they agree with all five YAML ancestors: root, cellular organisms, Bacteria, environmental samples and marine bacteria D ensemble. EFetch's division `Environmental samples` does not conflict with the bacterial domain.

`SPECIES` is the authority's rank for this environmental clone taxon, not evidence of a validly published binomial or independently delineated biological species. `EXACT` accurately describes the identifier grounding; it does not imply a curated genome or a pure culture. The source attestation and seed history retain the same taxon identity.

The specific direct sequence is [AF177554.1](https://www.ncbi.nlm.nih.gov/nuccore/AF177554.1), UID 5882269. Its complete GenBank XML explicitly links `taxon:103667`, organism uncultured marine bacterium D014 and clone D014. It is a partial 16S rRNA sequence, not a genome assembly, culture deposit or evidence that a strain listing should be populated.

## Evidence

Local source provenance was inspected at these physical addresses:

| Source | Address | Supported assertion |
| --- | --- | --- |
| Pinned taxonomy backbone | `data/raw/ncbitaxon_taxa.tsv:18532` | Exact taxon identity, rank, parent, code, snapshot and NCBI attestation; no supplied synonyms |
| Native NCBI names catalog | `data/catalog/ncbi_names-0000.jsonl.gz:38548` | The target's source-native name record |
| Corpus path index | `data/taxa/PATHS.tsv:15090` | Identifier-to-slug correspondence |
| Maintained admission scope | `curation/seed_scope.tsv:144176` | 2026-09-13 admission and one-source NCBI reason reproduced by the seed event |

The GenBank source feature marks an environmental sample and describes surface-associated marine material. Its 16S feature is partial at both ends. The record was created in September 1999 and updated in May 2004, and cites Dang and Lovell's 2000 paper, PMID 10653705, plus their 13 August 1999 direct submission. The accession does not supply a culture collection deposit, host, or collection-date/location qualifier; those fields are not inferred from its submission address.

The [primary paper](https://journals.asm.org/doi/10.1128/aem.66.2.467-475.2000), DOI 10.1128/AEM.66.2.467-475.2000, was checked through its PubMed abstract, publisher methods, Table 1, accession statement and selected results/discussion. Surfaces were deployed at Clam Bank Creek near Georgetown, South Carolina, on 23 June 1998 and sampled after 24 or 72 hours. Table 1 explicitly includes D014, and the deposited accession interval includes AF177554. The frequencies concern clone libraries, not isolated strains or direct cell abundance. Figure 2 was not visually inspected, so no D014-specific phylogenetic placement is inferred here. These observations do not replace NCBI's carried lineage.

All 20 complete Nuccore summaries returned by the same-code query were read. Complete GenBank XML was additionally inspected for the target and four close textual candidates:

| Accession | Inspected source identity | Relationship to this record |
| --- | --- | --- |
| AF177554.1 | 559-base marine D014 clone, taxon 103667 | Direct target evidence |
| FJ825191.1 | 641-base D014 clone, taxon 77133, acid mine drainage context, 2009 submission | Different environmental provenance; no supplied target link |
| AY985771.1 | 1,357-base D014 clone, taxon 77133, human stool, 2005 submission | Different environmental provenance; no supplied target link |
| PQ041478.1 | 1,248-base Niallia circulans strain D014, taxon 1397, Turkey, 2024 submission | Different organism and source history |
| FJ950663.1 | 1,514-base Pseudomonas grimontii strain d014, taxon 129847, wastewater-affected river in China, 2009 submission | Different organism and source history |

The other summaries include E. coli WGS projects DADGYU000000000.1 and DAFABE000000000.1, Dyella and Lysinibacillus markers, environmental dioxygenase markers, contig identifiers and plasmids. Their inspected metadata do not establish this taxon as their source. Those 15 records were checked at complete-summary level, not by reading every underlying sequence or cited paper. Shared short clone/strain strings are not sufficient to transfer identity or phenotype evidence.

The 17 non-target local candidate rows likewise resolve to namespace or text collisions, not missing target attestations:

- BacDive 103667 is Rhodococcus sp. ST030149, taxon 194249: `data/raw/bacdive_strains.tsv:27790` and `data/bacdive/records.jsonl.gz:27789`.
- CIP 103667 belongs to Neisseria meningitidis, taxon 487, associated with BacDive 134615, SI-ID 69497, SI-DP 153281 and GOLD Go0280339. Its ten matching rows span strain links, related records, BacDive, GOLD and culture-collection data. These are not alternative identifiers of NCBITaxon:103667.
- SI-DP 103667 is an ATCC 25121 deposit on SI-ID 38365, Mycobacterium intracellulare, taxon 1767: `data/straininfo/records.jsonl.gz:26761`.
- GCA_016999235.1 and GCA_020269625.1 concern E. coli D014-11 and d014-24.5, respectively: `data/catalog/ncbi_genbank-0015.jsonl.gz:24918` and `data/catalog/ncbi_genbank-0018.jsonl.gz:32535`.
- The number 103667 is a contiguity statistic, not this taxon identifier, in `data/catalog/gtdb_genomes-0006.jsonl.gz:6785` and `data/catalog/gtdb_genomes-0008.jsonl.gz:36423`. Differences between authorities on those unrelated genomes were not adjudicated as target findings.

No unsupported assertion, citation mismatch or over-scoped biological claim was found in the YAML. iModulonDB was not applicable: this record asserts no gene, regulator, expression module or transcriptomic phenotype.

## Completeness

The record is complete enough for its generated, NCBI-attested scope. Optional synonyms, nomenclature, taxonomy mappings, strains, deposits, genome links and causal graphs are correctly unasserted. `strain_count: 0` describes the available linked inventory, not an experimental claim that no culture could exist. Discovery of a partial rRNA accession does not by itself require a genome link or a fabricated strain/deposit record.

Both initial and accession-expanded searches included ignored files using `rg --no-ignore --hidden -n -z -i`, covering `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. The expanded expression was:

```text
\b103667\b|uncultured_marine_bacterium_d014\b|\bD[ _-]?014\b|\bAF177554(?:\.1)?\b|\b5882269\b
```

It includes the target label's distinctive clone token, identifier, slug, accession and sequence UID. Both passes returned the same 20 candidate rows: three target rows and 17 non-target rows. Every complete matching TSV or JSON row was read, using parsed common-plus-difference displays where appropriate with lossless reconstruction checks. No additional target association was established within these searched inventories. This is not an exhaustive census of the internet or every possible spelling.

Five discovered `SOURCE.json` files were separately parsed in full. BacDive metadata matched `responses/278/requested_ids/88` and its fetch URL because of BacDive identifier 103667, the Rhodococcus namespace collision above. The other four metadata files supplied no matches. Thus metadata matches were not incorrectly counted as an NCBI taxon attestation. Ignored-independent filename inventories covered `data/taxa`, `reports/yaml_record_review` and `history`; they found this target YAML but no pre-existing target report or target-named separate history file.

Exact taxon scans of the seven raw supplementary inventories for BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits found no rows for NCBITaxon:103667. No omission was inferred from unmatched neighboring strain names.

Public-search limits were retained:

- Nuccore `txid103667[Organism:exp]` returned one sequence, the direct marker above.
- Assembly returned zero and a phrase-not-found warning for that taxon query. This only describes the current index response, not a universal absence of genomes.
- Nuccore `"D014"[All Fields] AND Bacteria[Organism]` returned 20 summaries. Its translation expanded Bacteria to both the bacterial domain and the zoological genus with the same name; the returned summaries were inspected individually rather than trusting that filter as a precise identity test.
- PubMed `"D014" AND marine` returned zero, with an inappropriate expansion of marine toward military personnel. The known paper was instead resolved through the direct GenBank PMID. That zero result is not evidence of no literature.

No required representation was shown to be missing. More detailed ecological or phylogenetic enrichment would need an explicitly maintained, source-backed representation and is not silently inferred into this seeded record.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within this record-level review. Identity, carried lineage, source counts, grounding and seed provenance agree with the inspected inputs and live authority. The pass does not certify all external literature, genome catalogs, corpus reproducibility or uninspected phylogenetic figures.

## Recommended Edits

None required. Preserve the YAML, `SEEDED` status and embedded history.

If a later authority update establishes a correction, maintain the NCBI pin/extraction through `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`; fix a demonstrated projection defect in `src/taxonmech/seed.py` with focused tests. Scope changes belong in `curation/seed_scope.tsv`. Do not hand-edit generated YAML or pages. A shared D014 label or bare numeric identifier must not become a strain, deposit or genome join key.

## Follow-up Checks

No unresolved blocker requires a follow-up. For later authorized curation, verify the exact authority and accession chain, add a focused regression test for any changed projection, run `just seed-canary NCBITaxon:103667`, inspect the emitted YAML, repeat both focused validators and then run `just verify-corpus` and the authoritative `just qc`. These regeneration and full-corpus operations were not performed in this review.

Before adding a D014-specific phylogenetic assertion, inspect the primary figure and its accession mapping directly; do not extrapolate the study's overall clone distribution. Before adding any strain-genome link, require explicit source evidence for the same strain/deposit and genome, not merely a matching clone string.

## Additional Notes

Work was performed on `codex/record-review-extensimonas-20261003` at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The report is the sole new repository artifact from this target review. Temporary validator output is outside the repository. This review did not change source inventories, generated records, pages, curation histories, statuses, GitHub objects or worktrees; it did not contact people or use paid research.

Publisher HTML supplied the inspected primary-paper passages. The PMC page presented an access challenge, and the Europe PMC full-text API returned HTTP 406; those unsuccessful routes were not treated as inspected full text or bypassed. The publisher article was not read in its entirety and its figure images were not inspected. Near-name papers cited in the non-target GenBank records were not independently reviewed.

For reproducibility, the ten CIP 103667 candidate addresses were `data/straininfo/strain_links.tsv:16820`, `data/raw/strain_related_records.tsv:96959`, `data/raw/strain_related_records.tsv:96960`, `data/raw/bacdive_strains.tsv:56921`, `data/gold/organisms.jsonl.gz:218366`, `data/bacdive/records.jsonl.gz:56920`, `data/straininfo/related_records.tsv.gz:41668`, `data/straininfo/related_records.tsv.gz:41669`, `data/raw/culture_collection_strains.tsv:43990` and `data/straininfo/records.jsonl.gz:56675`. These complete source rows were read as disambiguation evidence; their external records were not all remotely revalidated.
