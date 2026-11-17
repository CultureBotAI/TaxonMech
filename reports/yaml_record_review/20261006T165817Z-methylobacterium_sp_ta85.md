# YAML Record Review: Methylobacterium sp. TA85

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/methylobacterium_sp_ta85.yaml`
- Started UTC: 2026-10-06T16:56:03Z
- Finished UTC: 2026-10-06T16:58:17Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` was inspected. Its identity is `NCBITaxon:1035229`, Methylobacterium sp. TA85, rank SPECIES, domain BACTERIA, parent `NCBITaxon:2615210`, genetic code 11, grounding EXACT, mapping status SEEDED. Its material assertions are ten root-first ancestors, zero inventoried BacDive strains, one NCBITAXON NAME attestation and one seed event. Synonyms, xrefs, nomenclature, taxonomy mappings, strain entries, genome links, definition, record-level evidence, discussion and causal graphs are absent.

The identifier resolves uniquely through `data/taxa/PATHS.tsv:14441`; the scope row is `curation/seed_scope.tsv:322225`. Seeded fields are generated from maintained inventories and seeding logic, not hand-edited YAML. Repository HEAD was `b6a6508faca1388b88feb5740b1095e9f64cfdb8`.

## Validation

Review skill and checklist were re-read; the curation guidance, schema, documentation and authoritative recipes had been inspected at this unchanged revision. Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/methylobacterium_sp_ta85.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/methylobacterium_sp_ta85.yaml --out /private/tmp/mta85-strict.tsv`: exit 0, one file scanned, zero errors. The actual TSV was read and contains only its header.
- Bounded structured comparisons confirmed identity, every ancestor, path/scope rows, attestation and seed-event text. These manual source checks are not a focused replacement for corpus reproduction.
- Not run: `just verify-corpus`, full-corpus strict validation, `just qc`, tests, provenance/site checks, and global `just validate-history`. This report does not certify corpus-wide reproducibility or reference integrity.
- `just validate-products` was not run: the configured OAK surface is curator-added graph grounding, absent here. `conf/id_label_targets.yaml` explicitly skips NCBITaxon; identity was checked against pinned and live NCBI.
- Ignored-inclusive history content and path searches found no target external artifact to validate. No history entry or status promotion was made.
- Before web follow-up, `uv run --offline --no-sync --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw kg-microbe-sources imodulondb datasets` succeeded. All 28 dataset rows were inspected; none covers Methylobacterium or Methylorubrum. Not applicable, not negative phenotype evidence.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221950` supplies the exact taxid, label, species rank, parent, code 11, empty synonym fields and 2026-09-13 snapshot. `data/catalog/ncbi_names-0005.jsonl.gz:31418` retains the scientific-name row. Exact scans of `data/raw/ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` and `dropped.tsv` returned no target rows.

The complete current [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035229&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035229) agree with identity and placement. The stored chain is root (1), cellular organisms (131567), Bacteria (2), Pseudomonadati (3379134), Pseudomonadota (1224), Alphaproteobacteria (28211), Hyphomicrobiales (356), Methylobacteriaceae (119045), Methylobacterium (407), and unclassified Methylobacterium (2615210). All ancestor labels and ranks match the pinned chain; XML LineageEx omits root, while Datasets includes it.

EXACT means exact grounding to this NCBI concept, not valid nomenclature, a type strain or culture-deposit equivalence. The [LPSN genus page](https://lpsn.dsmz.de/genus/methylobacterium), previously fully inspected and searched specifically for TA85 again, supplies no TA85 identity bridge. Genus nomenclature and properties must not be transferred. The legacy NCBI browser was inaccessible through the web tool; the two current NCBI APIs succeeded.

## Evidence

The sole attestation agrees with NCBITAXON, its source identifier and label, count 1, unit NAME and snapshot note. It counts one source-name assertion, not genomes or biological strains. The `seed_from_sources` event at 2026-09-13T17:54:04Z, action SEEDED_FROM_SOURCES, exactly matches the scope's one-source reason.

Exact scans found no target rows in `data/raw/bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv`, or `bactotraits_taxa.tsv`. No backbone taxon has this target as its parent. Zero BacDive strain records therefore agrees with the own/subtree gathering rule in `src/taxonmech/seed.py`; it does not mean TA85 was never cultured.

The live exact query `txid1035229[Organism:noexp]` returned zero assembly records, with phrases-not-found/no-items diagnostics, and one nucleotide UID, 347300726. Full [FR869825.1 metadata](https://www.ncbi.nlm.nih.gov/nuccore/FR869825.1), excluding bases, was read: a 1333-nt partial 16S rRNA gene, strain TA85, explicit `taxon:1035229`, host Trifolium repens and isolation source host leaf surface. Submission was 18 May 2011, creation 18 September, update 6 December 2011. No culture-collection, BioSample, BioProject or assembly identifier is supplied. Genomic DNA is the source molecule; the partial marker is not a genome assembly.

The marker explicitly cites [PMID 22000032](https://pubmed.ncbi.nlm.nih.gov/22000032/) and [DOI 10.1016/j.syapm.2011.08.005](https://doi.org/10.1016/j.syapm.2011.08.005). The current PubMed bibliography and complete abstract were fetched and inspected. The study compares phyllosphere communities across hosts, locations and land-use conditions. Its abstract does not name TA85 or establish isolate-specific growth, phenotype or collection locality. The host association is supported by TA85's own marker metadata, not inferred from community results or the submission address. Full text and supplements were not inspected.

## Completeness

Ignored and compressed files were included via `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Taxid, bounded exact label and slug produced 11 rows, all fully read: three genuine taxonomy/name/scope rows and eight unrelated numeric matches detailed below. The five discovered `SOURCE.json` metadata files were separately parsed for target values; none matched. Ignored-independent history filename enumeration likewise found no target artifact.

The expanded same-root query `(Methylobacterium|Methylorubrum).*\bTA[- _]?85\b|\bTA[- _]?85\b.*(Methylobacterium|Methylorubrum)` returned only the three genuine rows. Variants are search leads, not established aliases. A follow-up FR869825 search returned no rows in these roots. These are bounded catalog and exact-query results, not claims of universal external absence.

The repository's `normalize_culture_identifier` returned empty for TA85, TA-85 and TA 85. No eligible culture deposit or owning strain identity bridge was established; no required missing strain/genome link was demonstrated. The marker could be useful optional identity evidence but does not warrant creating a BacDive strain, genome record, nomenclature entry or own-deposit StrainInfo association. Optional definitions, record-level evidence and causal graphs need not be invented.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected claims and bounded completeness checks. Pass does not certify unrun corpus gates or uninspected full-text evidence.

## Recommended Edits

None required. Preserve the generated YAML and SEEDED status.

Any future evidence-backed strain/deposit/genome addition belongs in maintained extraction, matching or seeding logic under `src/taxonmech/`, with regression tests and documented regeneration. Scope changes belong in `curation/seed_scope.tsv`; upstream mapping corrections belong in kg-microbe. Do not hand-edit this YAML or its generated page.

## Follow-up Checks

Require the target's own whole eligible culture accession before adding deposit-dependent links. StrainInfo sequences must identify the same matched SI-DP; GOLD needs an unambiguous own-organism/project/analysis chain; ATB needs existing exact BioSample evidence and an eligible available FASTA. A sample, marker, project or deposit is not a genome, and shared sample evidence does not establish assembly equivalence.

After an authorized maintained-input change, run target schema/strict checks and relevant join tests, then `just verify-corpus` and `just qc`. Read full text or supplements before asserting any TA85-specific literature phenotype or locality.

## Additional Notes

- Four excluded rows are Lactobacillus gasseri taxid 1596, strain 1001285st1_A1_RTP21277_210401, GCA/GCF_040925245.1, BV-BRC 1596.1055 and BioSample SAMN41035229: `data/bvbrc/bvbrc-0004.jsonl.gz:16799`, `data/catalog/ncbi_genbank-0037.jsonl.gz:20866`, `data/catalog/ncbi_refseq-0006.jsonl.gz:20012`, `data/catalog/gtdb_genomes-0008.jsonl.gz:34487`.
- `data/catalog/ncbi_genbank-0022.jsonl.gz:48600` is Salmonella enterica subsp. enterica serovar Derby, taxid 28144/species taxid 28901, isolate MS160164, GCA_024802705.1, BioSample SAMEA103522918. Its publication is not target evidence.
- `data/catalog/allthebacteria.tsv.xz:66146` is that Salmonella sample SAMEA103522918, run ERR1865243, analysis ERZ3070653, with an available FASTA; the digit match is not taxon identity.
- `data/catalog/allthebacteria.tsv.xz:569699` is Mycobacterium tuberculosis, run ERR1035229, sample SAMEA3558762, rejected ASM_SHV, no available FASTA or analysis accession. It supplies neither the right identity nor an eligible assembly.
- `data/catalog/allthebacteria.tsv.xz:1599102` is Campylobacter coli, sample SAMN11669435, run SRR9080624, analysis ERZ25566285. Its SeqKit sum contains 1035229; its available FASTA and PASS filters do not identify TA85.
- All native candidate fields were read losslessly. None of these numeric collisions supplies a target strain, deposit, sample or genome link.
- The target was re-read and unchanged before this report. Only this new report was written; no YAML, history, mapping status, generated product, Git or GitHub mutation was performed.

