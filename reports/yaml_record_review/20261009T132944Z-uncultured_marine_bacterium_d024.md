# YAML Record Review: uncultured marine bacterium D024

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_marine_bacterium_d024.yaml`
- Started UTC: 2026-10-09T13:26:40Z
- Finished UTC: 2026-10-09T13:29:44Z
- Verdict: pass

## Target

All 39 lines of this generated `TaxonRecord` were read independently. `NCBITaxon:103673` denotes uncultured marine bacterium D024, an environmental species-rank NCBI taxon, not a cultured isolate, collection deposit or genome. It carries `BACTERIA`, parent `NCBITaxon:150608`, code 11, `EXACT` grounding, `SEEDED` status, zero inventoried strains, one NCBI name attestation and an embedded seed event. No adjacent record supplied the verdict.

Maintained inventories, `curation/seed_scope.tsv` and `scripts/seed_from_sources.py` own this generated representation; the YAML remains read-only.

## Validation

Both focused validators passed with exit zero:

```bash
UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/uncultured_marine_bacterium_d024.yaml
UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline python scripts/validate_strict.py data/taxa/bacteria/uncultured_marine_bacterium_d024.yaml --out /private/tmp/taxonmech-d024-review-strict.tsv
```

Schema validation found no issues. Strict validation scanned one file, reported zero errors, and produced a header-only TSV, read in full. Read-only comparisons verified the own backbone, all five ancestors, synonyms, source attestation, scope/index and embedded event. Exact-field scans found no own type-material, merged-ID or dropped-ID row and no immediate child in the pinned backbone.

Not checked: full-corpus `just verify-corpus`, `just qc`, `just test`, `just validate-history`, provenance, documentation and rendered-site drift gates. Bounded checks are not corpus reproduction. OAK `validate-products` was not run because this record has no curator-added graph nodes. The YAML cites no literature identifier; no separate history file matched the searches below. No focused substitute for a corpus-only gate was invented.

## Identity and Grounding

The complete backbone at `data/raw/ncbitaxon_taxa.tsv:18538`, scientific-name row at `data/catalog/ncbi_names-0000.jsonl.gz:38554`, scope at `curation/seed_scope.tsv:144182` and index at `data/taxa/PATHS.tsv:15135` agree on identifier, name and slug.

The full [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103673&retmode=xml) and [Datasets response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103673) confirm identity, rank, parent, bacterial ancestry and code. Pinned source rows and YAML agree on the root-first chain:

`1 root (NO_RANK) -> 131567 cellular organisms (CELLULAR_ROOT) -> 2 Bacteria (DOMAIN) -> 48479 environmental samples (NO_RANK) -> 150608 marine bacteria D ensemble (NO_RANK)`.

The Environmental samples division is not a domain; the Bacteria ancestor supports `BACTERIA`. `EXACT` is defensible for this NCBI grounding, not for another namespace's reused number. NCBI species rank does not establish a validly published species name or a biological species boundary.

## Evidence

The own attestation is one `NCBITAXON` `NAME` at the 2026-09-13 snapshot, not a count of organisms, strains or genomes. The 2026-09-13T17:54:04Z embedded seed event matches the own scope reason and source. Seeding does not imply human review.

Exact non-expanded nuccore lookup returned UID `5882275`. The complete [GenBank XML for AF177560.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=5882275&rettype=gb&retmode=xml) gives a 559-base partial 16S rRNA marker, source taxon `103673`, clone `D024`, an environmental-sample flag and a surface-associated marine source note. Both rRNA endpoints are partial. References comprise Dang and Lovell's 2000 paper, PMID `10653705`, and their 13 August 1999 direct submission. This is not a genome or collection accession.

An XML consistency check confirmed 559 declared and actual bases, all A/C/G/T, and exact case-normalized agreement between the complete transcription qualifier and DNA sequence. No independent alignment or species assignment was performed.

PubMed bibliographic data and the full abstract verify PMID `10653705` and DOI `10.1128/AEM.66.2.467-475.2000`. The publisher's methods, Table 1 headers/footnote and D024 row, and relevant results/discussion were inspected. D024 is reported in PEG-S at 72 h (1.2%), PEG-L at 72 h (1.5%), PU at 24 h (2.0%) and PU at 72 h (1.9%). These are clone-library frequencies from submerged surfaces in Clam Bank Creek, South Carolina, not organism abundance measurements. PCR and rRNA copy-number biases limit interpretation. E. coli JM109 was the cloning host, not a culture of D024. No metabolic or polymer-degradation trait is established. Figure 2's D024 tip was not independently inspected; no finer taxonomic reassignment is claimed. [Dang and Lovell, 2000](https://journals.asm.org/doi/10.1128/AEM.66.2.467-475.2000).

## Completeness

Own backbone/native-name evidence supports the empty synonyms. Exact taxon-field scans found no own rows in `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`. Optional nomenclature, mappings, strain listings, cross-references, literature and graph slots are defensibly empty in this seeded identity record, not automatic defects.

The [exact assembly query](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=assembly&term=txid103673%5BOrganism%3Anoexp%5D&retmode=json&retmax=100) returned zero with phrase-not-found/no-items warnings. This is a bounded query result, not proof of global genome absence. A clone designation does not establish a collection-backed strain or contradict zero inventoried strains.

Qualified-name search produced conference-related leads not adopted as evidence; exact `AF177560` search returned no results. Neither is a comprehensive literature census. The directly linked primary paper was inspected separately. iModulonDB was not applicable because no gene, regulator, pathway, module or transcriptomic claim is asserted.

## Findings

None found.

Counts: 0 blocker, 0 major, 0 minor.

## Recommended Edits

None required. Retain the exact environmental-clone identity, carried lineage and `SEEDED` status. Optional future literature/marker enrichment must preserve the limited observation scope and distinguish the unrelated matches below.

Evidence changes belong in maintained inventories or supported overlays; harmonization belongs in `scripts/seed_from_sources.py` with tests. Scope belongs in `curation/seed_scope.tsv`; slug assignment belongs in `data/taxa/PATHS.tsv`. Regenerate through the supported workflow, not manual YAML edits.

## Follow-up Checks

No unresolved blocker. Re-resolve exact identifiers and accession versions before enrichment, and inspect any proposed phylogenetic claim independently. After regeneration, run focused validation and the documented corpus reproduction/QC gates before publication. Those broader gates are not certified here.

## Additional Notes

Ignored-inclusive filename enumeration in `data/taxa`, `reports/yaml_record_review` and `history`, using `103673|uncultured_marine_bacterium_d024`, found only this target YAML. Content searches used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, including supported compressed catalogs. The final pattern was:

```text
\b103673\b|\buncultured[ _-]+marine[ _-]+bacterium[ _-]+D024\b|uncultured_marine_bacterium_d024\b|\bAF177560(?:\.1)?\b
```

Initial and accession-expanded searches each returned the same 29 rows, all read completely, including nested data. Three are the own backbone/native-name/scope rows above. The other 26 are unrelated:

- BacDive `103673`: Rhodococcus sp. ST002976, NCBI `194249`, at `data/bacdive/records.jsonl.gz:27794` and `data/raw/bacdive_strains.tsv:27795`.
- DSM `103673`: Mangrovibacter yixingensis TULL-A, NCBI `1529639`, BacDive `132226`, StrainInfo `400628`/deposit `907506`, GOLD `Go0620704`. Complete rows: `data/bacdive/records.jsonl.gz:54536`, `data/raw/bacdive_strains.tsv:54537`, `data/straininfo/records.jsonl.gz:298517`, `data/straininfo/strain_links.tsv:13051`, `data/straininfo/related_records.tsv.gz:32972` and `:32973`, `data/raw/strain_related_records.tsv:65806` and `:65807`, `data/raw/culture_collection_strains.tsv:59721`, `data/gold/organisms.jsonl.gz:451336`. Its type-strain and KM089834 marker evidence do not concern D024.
- CIP `103673`: Pseudoalteromonas atlantica T9, NCBI `288`, BacDive `135335`, StrainInfo `65565`/deposit `154033`, GOLD `Go0266909`. Complete rows: `data/bacdive/records.jsonl.gz:57640`, `data/raw/bacdive_strains.tsv:57641`, `data/straininfo/records.jsonl.gz:52891`, `data/straininfo/strain_links.tsv:18229`, `data/straininfo/related_records.tsv.gz:44771` and `:44774`, `data/raw/strain_related_records.tsv:101125` and `:101126`, `data/raw/culture_collection_strains.tsv:43996`, `data/gold/organisms.jsonl.gz:204957`.
- StrainInfo deposit `103673`: ATCC 25131, Mycobacterium intracellulare, NCBI `1767`, SI strain `38370`, at `data/straininfo/records.jsonl.gz:26766`.
- GTDB numeric statistics: GB_GCA_949398095.1, Bacteroidales bacterium M1, NCBI `1807729`, has contig N50 `103673` at `data/catalog/gtdb_genomes-0016.jsonl.gz:1110`; RS_GCF_028399525.1, Bacteroides stercoris, NCBI `46506`, has scaffold N50 `103673` at `data/catalog/gtdb_genomes-0005.jsonl.gz:19276`; RS_GCF_900120975.1, Mycobacterium tuberculosis, NCBI `1773`, has contig N50 `103673` at `data/catalog/gtdb_genomes-0014.jsonl.gz:9014`. None is a D024 identifier match.

Ignored-inclusive metadata discovery under `data`, `curation` and `history` found five `SOURCE.json` files in `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode` and `data/straininfo`. All were fully parsed for initial and expanded patterns. Only BacDive's requested ID/fetch URL matched, in its own namespace described above. Ignored-independent recursive history filename checks found no match; history contents were searched above. No extra accession-linked local candidate was found within these roots/terms, not every possible spelling or remote source.

Target SHA-256 before and after inspection: `e4f1fb9b8f600bd23e9b761f39c7eb7454156ca27de38d17c3b151ce8b41fe51`. This review wrote only this new repository report, leaving records, source inventories, scope, history, generated pages, branches, worktrees and GitHub unchanged. Eukaryota and unrelated work were preserved.
