# YAML Record Review: uncultured marine bacterium D021

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_marine_bacterium_d021.yaml`
- Started UTC: 2026-10-09T13:17:31Z
- Finished UTC: 2026-10-09T13:23:43Z
- Verdict: pass

## Target

All 39 lines of the generated `TaxonRecord` for `NCBITaxon:103672` were independently reviewed. The record denotes uncultured marine bacterium D021, an NCBI species-rank environmental taxon in `BACTERIA`, with parent `NCBITaxon:150608`, code 11, `EXACT` grounding, `SEEDED` status, zero inventoried strains, one NCBI name attestation and one embedded seed event. It does not denote a cultured isolate, assembly or collection deposit. No neighboring record supplied this verdict.

Committed source inventories, `curation/seed_scope.tsv` and `scripts/seed_from_sources.py` own the generated representation. This read-only review must not hand-edit the YAML or promote its status.

## Validation

Both documented focused validators passed, exit zero:

```bash
UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/uncultured_marine_bacterium_d021.yaml
UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline python scripts/validate_strict.py data/taxa/bacteria/uncultured_marine_bacterium_d021.yaml --out /private/tmp/taxonmech-d021-review-strict.tsv
```

Schema validation reported no issues. Strict validation scanned one file with zero errors; the complete TSV contained only its header. Read-only comparisons checked the own backbone, all five ancestors, synonyms, attestation, index/scope and embedded event. Exact taxon-field scans found no own type-material, merged-ID or dropped-ID row and no immediate child in the pinned backbone.

Not checked: full-corpus `just verify-corpus`, `just qc`, `just test`, `just validate-history`, provenance, documentation and rendered-site drift gates. Bounded source checks do not reproduce the corpus. The OAK `validate-products` gate was not run because the YAML has no curator-added graph nodes. No literature identifier is asserted in the YAML and no separate history file matched the bounded searches below. No focused substitute for a corpus-only gate was invented.

## Identity and Grounding

The complete backbone at `data/raw/ncbitaxon_taxa.tsv:18537`, native scientific name at `data/catalog/ncbi_names-0000.jsonl.gz:38553`, scope at `curation/seed_scope.tsv:144181` and index at `data/taxa/PATHS.tsv:15134` agree on the exact identifier, name and slug.

The complete [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103672&retmode=xml) confirms identity, species rank, parent and code 11. The full [Datasets response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103672) confirms root-inclusive ancestry. Together with the pinned ancestor rows, these support:

`1 root (NO_RANK) -> 131567 cellular organisms (CELLULAR_ROOT) -> 2 Bacteria (DOMAIN) -> 48479 environmental samples (NO_RANK) -> 150608 marine bacteria D ensemble (NO_RANK)`.

NCBI's Environmental samples division is not the biological domain; the bacterial ancestor supports `BACTERIA`. `EXACT` applies to the NCBI identity grounding, not equivalence to another database's reused number. Species rank here does not establish a validly published species name or a demonstrated biological species boundary.

## Evidence

The sole attestation records one `NCBITAXON` `NAME` for this target at the 2026-09-13 snapshot. It is not an abundance, strain or genome count. The 2026-09-13T17:54:04Z embedded seed event agrees with the own scope reason and source; it does not assert a completed human review.

The exact, non-expanded nuccore query returned UID `5882274`. The complete [GenBank XML for AF177559.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=5882274&rettype=gb&retmode=xml) records a 559-base partial 16S rRNA marker, source taxon `103672`, clone `D021`, an environmental-sample flag and a surface-associated marine source note. Both rRNA endpoints are partial. It cites Dang and Lovell's 2000 paper, PMID `10653705`, and their 13 August 1999 direct submission. This is marker evidence, not a genome or culture accession.

A read-only XML check found 559 declared and actual bases, only A/C/G/T characters, and exact case-normalized agreement between the full transcription qualifier and DNA sequence. This checks internal annotation consistency, not an independent alignment, phylogenetic placement or species assignment.

The full PubMed bibliographic/abstract response verifies PMID `10653705` and DOI `10.1128/AEM.66.2.467-475.2000`. Publisher methods, Table 1 with headers and footnote, results and relevant discussion were inspected. D021 occurs at 2.4% in PEG-S at 72 h, 1.9% in PEG-M at 24 h and 1.9% in PU at 72 h. These are clone-library frequencies, not organism abundance estimates. The experiment sampled submerged surfaces in Clam Bank Creek, North Inlet, South Carolina. The authors caution about rRNA copy-number differences and amplification bias. E. coli JM109 was a cloning host, not evidence that D021 was cultured. These observations do not establish D021-specific metabolism, pathogenicity or polymer degradation. Figure 2 was not independently inspected for its D021 tip; no finer taxonomic reassignment is asserted. [Dang and Lovell, 2000](https://journals.asm.org/doi/10.1128/AEM.66.2.467-475.2000).

## Completeness

The own backbone and native name support the empty synonym representation. Exact taxon-field scans found no own rows in `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`. Optional nomenclature, mappings, strain listings, cross-references, literature and graph fields are defensibly unpopulated in this seeded identity record; optional enrichment is not itself a defect.

The [exact assembly query](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=assembly&term=txid103672%5BOrganism%3Anoexp%5D&retmode=json&retmax=100) returned zero items with phrase-not-found/no-items warnings. This supplies no assembly association for this query, not proof of global genome absence under other identifiers. The clone designation does not establish a collection-backed strain or contradict an inventory-derived zero strain count.

Qualified-name web search produced conference-related leads that were not adopted as evidence; exact `AF177559` search returned no results. Neither is a comprehensive literature census. The directly linked primary paper was inspected independently as described above. iModulonDB was not applicable: the YAML asserts no gene, regulator, pathway, module or transcriptomic claim.

## Findings

None found.

Counts: 0 blocker, 0 major, 0 minor.

## Recommended Edits

None required. Preserve the exact environmental-clone identity and `SEEDED` status. Any later marker or literature enrichment must distinguish clone observations from cultured-organism traits and must not import the unrelated numeric matches below.

Future evidence changes belong in maintained inventories or supported overlays; harmonization belongs in `scripts/seed_from_sources.py` with tests. Scope belongs in `curation/seed_scope.tsv`, and identifier-to-slug assignment belongs in `data/taxa/PATHS.tsv`. Use supported regeneration rather than manual YAML edits.

## Follow-up Checks

No unresolved blocker. Before enrichment, re-resolve exact identifiers and accession versions and inspect any proposed finer phylogenetic placement independently. After regeneration run the focused validators and the documented corpus reproduction/QC gates before publication. This review does not certify those broader checks.

## Additional Notes

Ignored-inclusive filename enumeration under `data/taxa`, `reports/yaml_record_review` and `history`, using `103672|uncultured_marine_bacterium_d021`, found only this target YAML. Content searches used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, including supported compressed catalogs.

The final accession-expanded pattern was:

```text
\b103672\b|\buncultured[ _-]+marine[ _-]+bacterium[ _-]+D021\b|uncultured_marine_bacterium_d021\b|\bAF177559(?:\.1)?\b
```

Initial and expanded searches returned the same 29 candidate rows. All complete rows, including nested native data, were read. Three are this target's backbone, native name and scope rows above; the remaining 26 are numeric collisions, not D021 evidence:

- BacDive `103672` is Rhodococcus sp. ST000796, NCBI `194249`: `data/bacdive/records.jsonl.gz:27793` and `data/raw/bacdive_strains.tsv:27794`.
- DSM `103672` belongs to Undibacterium squillarum CMJ-15, NCBI `1131567`, BacDive `132183`, StrainInfo `379389`, GOLD `Go0620699`: `data/bacdive/records.jsonl.gz:54493`, `data/raw/bacdive_strains.tsv:54494`, `data/straininfo/records.jsonl.gz:290154`, `data/straininfo/strain_links.tsv:12946`, `data/straininfo/related_records.tsv.gz:32739` and `:32741`, `data/raw/strain_related_records.tsv:64881` and `:64882`, `data/raw/culture_collection_strains.tsv:59720`, and `data/gold/organisms.jsonl.gz:451331`. The nested LPSN name and associated culture/genome records concern this other taxon. StrainInfo's GCA_014652435 association specifically names its KCTC 23917 deposit; it supplies no D021 association.
- CIP `103672` belongs to Pseudoalteromonas atlantica 511-T, NCBI `288`, BacDive `135334`, StrainInfo `65564`, GOLD `Go0266906`: `data/bacdive/records.jsonl.gz:57639`, `data/raw/bacdive_strains.tsv:57640`, `data/straininfo/records.jsonl.gz:52890`, `data/straininfo/strain_links.tsv:18226`, `data/straininfo/related_records.tsv.gz:44765` and `:44768`, `data/raw/strain_related_records.tsv:101119` and `:101120`, `data/raw/culture_collection_strains.tsv:43995`, and `data/gold/organisms.jsonl.gz:204954`.
- StrainInfo deposit `103672` is ATCC 25130, Mycobacterium intracellulare, NCBI `1767`, StrainInfo strain `38369`, at `data/straininfo/records.jsonl.gz:26765`.
- Three GTDB-native matches are `ncbi_contig_n50=103672`, not taxon IDs: GB_GCA_948948655.1, uncultured Duncaniella sp., NCBI `2768039`, at `data/catalog/gtdb_genomes-0005.jsonl.gz:362`; RS_GCF_032029195.1, E. coli OC22, NCBI `562`, at `data/catalog/gtdb_genomes-0005.jsonl.gz:14431`; and RS_GCF_000485715.1, E. coli 907779, NCBI `1268988`, at `data/catalog/gtdb_genomes-0008.jsonl.gz:28500`.

Ignored-inclusive discovery under `data`, `curation` and `history` found five source-metadata files, all fully parsed for both patterns: `data/bvbrc/SOURCE.json`, `data/straininfo/SOURCE.json`, `data/bacdive/SOURCE.json`, `data/seqcode/SOURCE.json` and `data/gold/SOURCE.json`. Only BacDive metadata matched: its requested ID and fetch URL use the BacDive namespace described above, not `NCBITaxon:103672`. An ignored-independent recursive history filename scan found no match; history contents were searched above. No extra accession-linked local candidate was found within these roots and terms; this is not an exhaustive census of every spelling or remote database.

The target SHA-256 remained `299f5a571f3352385ec09b52510c1a0a20d79b9774abd900c7e381215582644b` before and after inspection. This review wrote only this new repository report and did not change records, inventories, scope, history, generated pages, branches, worktrees or GitHub state. Eukaryota and unrelated work were preserved.
