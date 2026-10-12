# YAML Record Review: uncultured marine bacterium D015

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_marine_bacterium_d015.yaml`
- Started UTC: 2026-10-09T10:21:24Z
- Finished UTC: 2026-10-09T10:27:25Z
- Verdict: pass

## Target

The complete 39-line generated `TaxonRecord` was read independently. Its identifier is `NCBITaxon:103668`, label is `uncultured marine bacterium D015`, rank is `SPECIES`, domain is `BACTERIA`, and direct parent is `NCBITaxon:150608` (marine bacteria D ensemble). The record carries five root-first ancestors, genetic code 11, `grounding_status: EXACT`, `mapping_status: SEEDED`, zero classified BacDive strains, one NCBITAXON name attestation, and one embedded seed event. No synonyms, nomenclature, cross-taxonomy mappings, equivalent xrefs, strain entries, literature evidence, causal graphs, or discussions are asserted.

This is an environmental-clone-associated NCBI taxon concept. A species rank in NCBI does not make its placeholder label a formally established species name or its clone designation a culture-collection accession. Only this record receives a verdict.

## Validation

Both focused validators passed using the existing offline environment:

```bash
UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/uncultured_marine_bacterium_d015.yaml
UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline python scripts/validate_strict.py data/taxa/bacteria/uncultured_marine_bacterium_d015.yaml --out /private/tmp/taxonmech-d015-review-strict.tsv
```

- LinkML: exit 0, `No issues found`.
- Closed-schema strict validation: exit 0, one file scanned, zero error files and zero error rows. The temporary TSV contains its header only.
- Read-only structured comparisons verified the complete own backbone row, all five ancestor rows, source attestations, scope admission, and embedded seed-event wording. Exact-field scans checked children, type material, retired identifiers, and dropped rows.
- Live NCBI Taxonomy EFetch and Datasets responses independently confirmed the identifier and lineage. These are authority checks, not a claim that a full ontology gate ran.
- `just validate-products` was not run: this target has no curator-added graph nodes or edges requiring its ID-label checks. No paper citation or graph reference is asserted in the YAML; the newly discovered sequence citation was checked separately below.
- `just validate-history` was not run: ignored-independent filename and content searches found no target-specific external history record in `history/`; no history record was created. The embedded event was inspected and validated with the YAML.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, provenance gates, tests, generated-site drift, and corpus-wide history/product gates. This one-record review did not regenerate any artifact or substitute a custom reproduction check for those gates.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18533` exactly supports the identifier, label, species rank, parent, genetic code, empty synonym fields, and 2026-09-13 snapshot annotation. Its `retired_into` field is empty. `data/catalog/ncbi_names-0000.jsonl.gz:38549` independently retains the exact scientific name under the same taxon ID.

The live [NCBI Taxonomy record](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=103668), inspected through [taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103668&retmode=xml), identifies D015 as taxon 103668, parent 150608, species rank, and genetic code 11. The [Datasets taxonomy response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103668) supplies the root-inclusive ancestor IDs `1, 131567, 2, 48479, 150608`. The YAML and pinned backbone agree on their labels and ranks: root, cellular organisms, Bacteria, environmental samples, marine bacteria D ensemble.

`EXACT` is supported as a link to this NCBI concept, not as a claim of resolved phylogeny, species circumscription, or experimental characterization. The carried environmental lineage is consistent with repository policy. Nothing inspected supports replacing it with a phylogenetic inference from the paper's broader results.

There are no direct children in the pinned backbone, so the zero own BacDive rows also resolve the descendant-inclusive strain count for this record. Exact target-ID scans of `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv`, and `data/raw/dropped.tsv` found no rows. These are bounded snapshot checks, not universal absence claims.

## Evidence

The own source inventory and scope establish the seeded assertions:

- `data/raw/ncbitaxon_taxa.tsv:18533`: one NCBI name, exact target identity, code and snapshot; no synonym or retirement value.
- `data/taxa/PATHS.tsv:15099`: identifier-to-slug association.
- `curation/seed_scope.tsv:144177`: admission on 2026-09-13, with the exact NCBI-only attestation reason reproduced in the embedded event.
- Exact taxon-field scans found no own rows in `data/raw/bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv`, or `bactotraits_taxa.tsv`.

The one NCBITAXON `NAME` assertion is a source-record count, not a genome, culture, phenotype, or publication count. `src/taxonmech/seed.py:341`, `src/taxonmech/seed.py:479`, `src/taxonmech/seed.py:543`, `src/taxonmech/seed.py:549`, and `src/taxonmech/seed.py:630` show the maintained generation paths for identity/lineage, genetic code, classified strains, attestation, and seed history. These paths agree with the inspected source rows.

The exact, non-expanded NCBI nuccore query `txid103668[Organism:noexp]` returned one record, UID 5882270. Its complete [GenBank XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=5882270&rettype=gb&retmode=xml) was read: [AF177555.1](https://www.ncbi.nlm.nih.gov/nuccore/AF177555.1) is a 559-base partial 16S rRNA sequence whose source feature explicitly names clone D015 and `taxon:103668`, flags an environmental sample, and describes a surface-associated marine source. Both terminal rRNA boundaries are partial. The source record cites Dang and Lovell, PMID 10653705, and their 13-Aug-1999 submission. Its entire DNA sequence is 559 A/C/G/T bases and matches the supplied rRNA transcription case-insensitively. This checks annotation consistency only; no independent alignment or species inference was performed.

The exact assembly query returned zero entries with NCBI's `phrasesnotfound`/`No items found` diagnostics. It did not positively identify a genome and is not proof that a related organism has never been sequenced. AF177555.1 itself is a marker, not a genome or culture deposit.

[Dang and Lovell (2000), PMID 10653705](https://pubmed.ncbi.nlm.nih.gov/10653705/), resolves to DOI `10.1128/AEM.66.2.467-475.2000`, Applied and Environmental Microbiology 66:467-475. Its complete PubMed abstract and identifiers were inspected. The study used cultivation-independent ribosomal-marker analysis of colonization on test surfaces in a salt-marsh estuary. Those experiment-wide results are not D015-specific evidence for a mechanism, phenotype, substrate preference, named-species equivalence, or culture. The clone-to-citation link comes from D015's own GenBank record. The [PMC article](https://pmc.ncbi.nlm.nih.gov/articles/PMC91850/) returned a browser-verification page, so its full text, tables, and figures were not inspected and the access challenge was not bypassed.

All 33 candidate content rows from the initial ignored-inclusive search were read completely, including compressed native records. The following native distinctions exclude false joins:

- `data/bacdive/records.jsonl.gz:27790` has BacDive ID 103668, but its NCBI field is 194249, Rhodococcus sp., designation ST030157. Its corresponding raw row is `data/raw/bacdive_strains.tsv:27791`. The 103668 request in `data/bacdive/SOURCE.json` belongs to this BacDive identifier namespace; its complete enclosing response metadata was inspected.
- BacDive 137252 and StrainInfo SI-ID 69499 describe Neisseria meningitidis, NCBI 487, deposit CIP 103668. Their complete native rows are `data/bacdive/records.jsonl.gz:59554` and `data/straininfo/records.jsonl.gz:56677`. GOLD `Go0280340` likewise names this deposit and taxon at `data/gold/organisms.jsonl.gz:218367`.
- BacDive 140269 and StrainInfo SI-ID 406729 describe Ileibacterium valens, NCBI 1862668, with DSM 103668. See `data/bacdive/records.jsonl.gz:62553`, `data/straininfo/records.jsonl.gz:304618`, and GOLD `Go0620694` at `data/gold/organisms.jsonl.gz:451326`. `data/raw/lpsn_names.tsv:31707` and type-material rows 65690-65691 explicitly concern this other taxon.
- `data/straininfo/records.jsonl.gz:26762` uses 103668 as SI-DP for ATCC 25122 within SI-ID 38366, Mycobacterium intracellulare, NCBI 1767. It does not identify D015.
- `data/catalog/ncbi_genbank-0012.jsonl.gz:35963` and `data/catalog/ncbi_genbank-0015.jsonl.gz:24919` describe Escherichia coli, taxon 562, with strain d015-06.3 and isolate D015-18 respectively. Their assemblies GCA_014081585.1 and GCA_016999255.1 are not assigned to this record.
- `data/catalog/gtdb_genomes-0006.jsonl.gz:15878` uses 103668 as a contig N50 for Lactiplantibacillus plantarum CECT 8962; `data/catalog/gtdb_genomes-0003.jsonl.gz:1959` uses it as scaffold N50 for a Rhizobiaceae bacterium assembly. Their native taxonomy fields identify other taxa.

The corresponding complete raw culture-collection and related-record rows, StrainInfo links, and compressed StrainInfo related-record rows were also inspected. They retain the above other-taxon classifications; repeated numeric strings do not provide target evidence. No verdict is assigned to those other TaxonMech records.

## Completeness

The record is complete enough for its supported seeded scope. A clone name does not require a BacDive strain entry, and optional nomenclature, mapping, xref, definition, literature, and causal-graph slots need not be populated. The discovered marker and paper offer possible future provenance enrichment, not an unmet required field. No own culture/genome linkage was established.

The initial case-insensitive search used `\b103668\b|\bD[ _-]?015\b|uncultured_marine_bacterium_d015\b`. It was repeated with `|\bAF177555(?:\.1)?\b` after inspecting the sequence. Both used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` over `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Ignored and compressed files were included. Each search returned the same 33 content rows, with no new accession match in those roots. All matched TSV and JSONL rows were parsed and read in full, not judged from search excerpts.

Separately, all five discovered `SOURCE.json` documents under `data`, `curation`, and `history` were parsed completely with ignored-inclusive discovery. The only matching metadata values were the BacDive batch request discussed above. An ignored-independent filename search under `data/taxa`, `reports/yaml_record_review`, and `history` resolved only the target YAML before this report was written; no earlier target report or target-specific history filename was found. These scoped searches do not claim that every file elsewhere in the repository or every external resource was searched.

iModulonDB was not applicable: this record names no strain-specific expression dataset, gene, regulator, module, or transcriptomic claim. No paid research or ungrounded phenotype expansion was attempted.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the record's asserted scope. Identity, lineage, code, strain count, source attestation, scope admission, and seeded status agree with the inspected evidence. The publication full-text access limitation is an evidence boundary, not a defect in this NCBI-only record.

## Recommended Edits

None required. Leave generated YAML unchanged and retain `mapping_status: SEEDED`; a read-only agent report is not human sign-off.

Any later literature enrichment must use a maintained, validated source/curation path, preserve the specific AF177555.1-to-D015 link, and keep this partial rRNA marker separate from genome and culture identifiers. Identity or lineage corrections belong in the maintained NCBI inventory/source transform and `src/taxonmech/seed.py`, not in a hand-edited record or rendered page. No change to `curation/seed_scope.tsv` is supported by this review.

## Follow-up Checks

- Revisit the paper's complete text through an authorized accessible source before adding D015-specific experimental claims. Its abstract alone cannot supply clone-level table values or phylogenetic assignments.
- Before any future culture or genome association, require an explicit taxon/sample/deposit/accession relationship, not D015 substring similarity, a numeric namespace collision, or a nearest sequence match.
- After any authorized maintained-input change, rerun both focused validators, inspect the generated canary, and use the documented full `just verify-corpus` and `just qc` gates before publication. Add a history record only as part of that later authorized curation workflow.

## Additional Notes

This review followed `.claude/skills/review-yaml-record/SKILL.md` and the local field checklist. The source comparison, validation, authority requests, and sequence/citation inspection were performed for D015 itself; no adjacent record's verdict was inherited.

Target SHA-256 was unchanged before and after inspection: `1be31f2ccf0a47e7724a821befaad757f70b8a5606ceda6c18ee0b0126422a9b`.

This review wrote only this new report in the repository. It did not alter the taxon YAML, source inventories, generated pages, scope, history, review status, GitHub state, or existing worktrees. Eukaryota remained untouched. The user reported that the parallel session had closed; existing worktrees were retained without cleanup or branch switching.
