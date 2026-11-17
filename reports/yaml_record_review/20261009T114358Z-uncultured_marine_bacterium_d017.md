# YAML Record Review: uncultured marine bacterium D017

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_marine_bacterium_d017.yaml`
- Started UTC: 2026-10-09T11:40:03Z
- Finished UTC: 2026-10-09T11:43:58Z
- Verdict: pass

## Target

The complete 39-line generated `TaxonRecord` was read twice, including numbered lines. It denotes `NCBITaxon:103670`, uncultured marine bacterium D017, at `SPECIES` rank in `BACTERIA`, under `NCBITaxon:150608`, marine bacteria D ensemble. It carries five ancestors, `EXACT` grounding, `SEEDED` status, code 11, zero classified BacDive strains, one NCBITAXON name attestation, and one embedded seed event.

No synonyms, nomenclature, mappings, xrefs, strain entries, literature citations, graphs, or discussions are asserted. This is an environmental clone-associated taxon, not a cultured strain. Its identity and evidence were checked independently of nearby D-series records.

## Validation

Both focused validators passed:

```bash
UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/uncultured_marine_bacterium_d017.yaml
UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline python scripts/validate_strict.py data/taxa/bacteria/uncultured_marine_bacterium_d017.yaml --out /private/tmp/taxonmech-d017-review-strict.tsv
```

- LinkML: exit 0, `No issues found`.
- Strict validation: exit 0, one file scanned, zero error files and rows. The read temporary TSV is header-only.
- Read-only structured comparisons verified the own backbone, complete lineage, PATHS, scope, attestation, and embedded event. Exact-ID scans covered children, seven other raw source tables, type material, merged IDs, and dropped rows.
- All 28 local content-search candidates were read completely. Live Taxonomy, Datasets, GenBank, PubMed bibliographic data and abstract, and relevant publisher full-text methods/results/discussion were inspected.
- `just validate-products` was not run because this record has no curator-added graph grounding. No YAML citation needs a reference check; the newly discovered accession and publication were checked separately.
- `just validate-history` was not run: ignored-independent searches found no target-specific external history filename or content in the searched tree. The embedded event was inspected and validated with the YAML.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, provenance checks, site drift, and corpus-wide history/product gates. No generator ran. These focused results do not establish full-corpus reproduction.

## Identity and Grounding

The fully read backbone row at `data/raw/ncbitaxon_taxa.tsv:18535` matches the ID, label, rank, parent, code, and 2026-09-13 snapshot. Its synonym and retirement fields are empty. The complete native scientific-name row at `data/catalog/ncbi_names-0000.jsonl.gz:38551` agrees.

Live [NCBI Taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103670&retmode=xml) confirms the label, species rank, parent 150608, and code 11. [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103670) confirms root-inclusive ancestry `1, 131567, 2, 48479, 150608`. The entire pinned lineage matches the YAML: root, cellular organisms, Bacteria, environmental samples, and marine bacteria D ensemble, with every rank and label agreeing.

The authority's species rank does not assert a validly named cultured species. `EXACT` describes the source-concept match, not phenotype certainty. NCBI's environmental placement must remain carried rather than being replaced by a literature-derived phylogeny. No direct child occurs in the backbone. Exact own-ID scans found no type-material, merged-ID, or dropped row in their respective `data/raw/` tables; these results are snapshot-scoped.

## Evidence

`data/taxa/PATHS.tsv:15113` maps the target ID to its slug. `curation/seed_scope.tsv:144179` gives its NCBI-only admission reason and 2026-09-13 date. The embedded 2026-09-13T17:54:04Z event reproduces that reason. The attestation counts one `NAME`, not an isolate or genome.

The own-ID scans found no target rows in `data/raw/bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv`, or `bactotraits_taxa.tsv`. With no backbone children, zero classified BacDive strains is supported. The inspected generation owners in `src/taxonmech/seed.py` are line 341 for identity/lineage/status, 479 for code, 543 for classified-strain count, 549 for NCBI attestation, and 630 for seed history.

The exact nuccore query `txid103670[Organism:noexp]` returned UID 5882272. Its complete [GenBank XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=5882272&rettype=gb&retmode=xml) identifies [AF177557.1](https://www.ncbi.nlm.nih.gov/nuccore/AF177557.1), a 559-base partial 16S sequence. Its source explicitly names clone D017 and `taxon:103670`, marks an environmental sample, and describes an uncultured surface-associated marine bacterium. Both rRNA boundaries are partial. All bases are A/C/G/T, and the submitted transcription and declared length match the sequence. No independent alignment was performed.

GenBank cites a 13-Aug-1999 direct submission by H. Dang and C. R. Lovell and their 2000 paper. [PubMed EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=10653705&retmode=xml) verifies PMID 10653705, authors, journal, February 2000 date, and DOI `10.1128/AEM.66.2.467-475.2000`.

The [publisher article](https://journals.asm.org/doi/10.1128/AEM.66.2.467-475.2000) describes culture-independent analysis of submerged surfaces in a South Carolina salt-marsh creek. Its accession range includes AF177557. Table 1 explicitly records D017 at 1.8% in PVA-72, 1.7% in PEG-L-24, 1.5% in PEG-L-72, and 3.9% in PEG-M-24. The table footnote defines these as clone-library frequencies. The discussion warns that PCR bias and rRNA copy variation prevent equating these values with organism abundance. This supports bounded recovery context, not an isolate growth assay, metabolic mechanism, or proof of culture availability. No figure-specific placement or modern taxonomic reassignment was inferred.

The exact assembly query returned zero entries with `phrasesnotfound` and `No items found` diagnostics. It supplied no target assembly association; this is not universal genome absence.

The 25 additional local candidate rows are excluded on their native fields:

- BacDive 103670 denotes Rhodococcus sp. ST018641(HKI), BI 08483, taxon 194249. It is a database-record-number collision, not NCBI taxon 103670.
- CIP 103670 belongs to Pseudoalteromonas atlantica, taxon 288, BacDive 135332, StrainInfo 65562/deposit 154027, and GOLD Go0266900. Its separate 16S reference LC379072 is not D017's accession.
- DSM 103670 belongs to Sulfobacillus thermosulfidooxidans, taxon 28034, BacDive 139830, StrainInfo 401503/deposit 908446. Its sequence metadata do not link D017.
- StrainInfo deposit 103670 denotes ATCC 25125, Mycobacterium taxon 1763, within strain 38368. Again, the integer belongs to a different identifier namespace.
- GCA_014081525.1 and GCA_014081645.1 denote E. coli taxon 562 strains d017-46.1a and d017-46.1b, respectively. These are short-label near matches, not the marine clone.
- GTDB RS_GCF_009800325.1, E. coli taxon 562, contains 103670 as total gap length. RS_GCF_002463565.1, E. coli taxon 562, and RS_GCF_902499445.1, Klebsiella pneumoniae taxon 573, contain it as contig N50. None has the target taxon ID.

No neighboring YAML was reviewed or modified, and none of these excluded records supplies a target strain/genome link.

## Completeness

Complete enough for this NCBI-only seed. Empty optional nomenclature, mappings, strains, citations, definitions, and graphs are not defects. The exact marker and study are useful optional provenance enrichment, not required evidence of a culture or genome.

The initial case-insensitive content pattern was `\b103670\b|\bD017\b|uncultured_marine_bacterium_d017`; the second appended `|\bAF177557(?:\.1)?\b`. Both used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` over `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Each found the same 28 rows, all fully read. The accession added no match. Ignored and compressed files were included.

All five `SOURCE.json` files discovered with ignored-inclusive searches under `data`, `curation`, and `history` were separately parsed fully for both patterns. Only BacDive metadata matched: response 278's requested ID and fetch URL contain BacDive 103670, whose native record has the different taxon described above. This is not a target NCBI attestation. No target-specific history filename appeared. An ignored-independent filename search across `data/taxa`, `reports/yaml_record_review`, and `history`, using `103670|uncultured_marine_bacterium_d017`, returned only the target YAML before this report.

Exact name/accession web queries produced broad conference-program leads, not evidence adopted for this taxon. Primary evidence was obtained from the accession's explicit citation and publisher. PubMed's browser view returned only footer material, so its complete EFetch abstract and bibliography were used instead. The publisher methods, Table 1 headers/row/footnote, sequence-results text, and discussion were inspected; no figure was used to assert placement. iModulonDB was not applicable to this record's claim set.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the asserted scope. Identity, lineage, code, source counts, admission, and history are supported. Excluded numeric and short-label matches are not missing target associations.

## Recommended Edits

None required. Preserve the generated YAML and `mapping_status: SEEDED`; an agent report is not human sign-off. Any future literature/marker enrichment belongs in maintained inventory/source-transform inputs and the seeder. Keep AF177557.1 tied explicitly to NCBITaxon:103670, outside genome counts, and preserve study-specific scope. No scope or lineage change is supported.

## Follow-up Checks

- Require an explicit clone-to-sample, deposit, or assembly relationship before adding a culture/genome link.
- Preserve namespace prefixes and native field meanings; never join on the bare integer 103670 or a D017 substring.
- After later authorized maintained-input curation, rerun focused validators, inspect the regenerated canary, and run full `just verify-corpus` and `just qc` gates. Append history only within that later curation workflow.

## Additional Notes

For reproducibility, the fully read non-own candidate addresses were `data/straininfo/strain_links.tsv:18220` and `:26617`; `data/raw/strain_related_records.tsv:101107` and `:101108`; `data/raw/bacdive_strains.tsv:27792`, `:57638`, and `:62125`; `data/raw/culture_collection_strains.tsv:43993` and `:59718`; `data/straininfo/related_records.tsv.gz:44753`, `:44756`, `:64348`, and `:64349`; `data/gold/organisms.jsonl.gz:204948`; `data/bacdive/records.jsonl.gz:27791`, `:57637`, and `:62124`; `data/straininfo/records.jsonl.gz:26764`, `:52888`, and `:299392`; `data/catalog/ncbi_genbank-0012.jsonl.gz:35960` and `:35966`; and `data/catalog/gtdb_genomes-0015.jsonl.gz:11580`, `gtdb_genomes-0010.jsonl.gz:13392`, and `gtdb_genomes-0006.jsonl.gz:38130`.

The one-record skill and local checklist were applied independently at unchanged HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Target SHA-256 remained `06f16c36bc6ee3fbf72866e65fbf19a4302a14267d33525741abafa480a2124c`. This review wrote only this new repository report and changed no YAML, inventories, scope, pages, history, review status, GitHub, branches, or worktrees. Eukaryota remained untouched.
