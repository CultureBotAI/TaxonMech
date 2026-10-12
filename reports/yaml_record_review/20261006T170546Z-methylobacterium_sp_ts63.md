# YAML Record Review: Methylobacterium sp. TS63

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/methylobacterium_sp_ts63.yaml`
- Started UTC: 2026-10-06T17:02:31Z
- Finished UTC: 2026-10-06T17:05:46Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` was read. It denotes `NCBITaxon:1035231`, Methylobacterium sp. TS63, rank SPECIES, domain BACTERIA, parent `NCBITaxon:2615210`, genetic code 11, grounding EXACT, mapping status SEEDED. It carries ten ancestors, zero inventoried BacDive strains, one NCBITAXON NAME attestation and one seed event. No synonyms, xrefs, nomenclature, taxonomy mappings, strain entries, genome links, definition, record-level evidence, host/phenotype claim, discussions or causal graphs occur.

Identity resolves uniquely through `data/taxa/PATHS.tsv:14443`; scope is `curation/seed_scope.tsv:322227`. These assertions are generated from maintained source inputs and seeding logic. HEAD was rechecked as `b6a6508faca1388b88feb5740b1095e9f64cfdb8`.

## Validation

Local guidance, review checklist, schema and authoritative recipes were inspected at the unchanged revision. Project commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/methylobacterium_sp_ts63.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/methylobacterium_sp_ts63.yaml --out /private/tmp/mts63-strict.tsv`: exit 0, one file scanned, zero errors. The actual TSV was read and contains only its header.
- Bounded structured source comparisons passed for identity, full lineage, path/scope, attestation and event text. These manual checks do not replace corpus reproduction.
- Not run: `just verify-corpus`, full-corpus strict validation, `just qc`, tests, provenance/site gates and global `just validate-history`. Corpus-wide reproducibility and reference integrity remain unproven here. The inspected reproduction script has no target selector; `--max-diffs` only limits displayed diffs.
- `just validate-products` was not run: its configured OAK target is curator-added graph grounding, absent here, and `conf/id_label_targets.yaml` skips NCBITaxon. Taxonomic identifiers were checked against pinned and live NCBI.
- Ignored-inclusive content and filename searches found no target external history artifact to validate. No history entry or mapping-status promotion was made.
- Before web follow-up, `uv run --offline --no-sync --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw kg-microbe-sources imodulondb datasets` succeeded. All 28 rows were inspected; no Methylobacterium/Methylorubrum dataset applies. This is not negative phenotype evidence.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221952` supports the exact identifier, label, species rank, parent, code 11, empty synonym fields and snapshot 2026-09-13. The full scientific-name row is `data/catalog/ncbi_names-0005.jsonl.gz:31420`. Exact type-material, merged-ID and dropped-record scans returned no target rows.

The complete current [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035231&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035231) agree with the record. Its root-first chain is root (1), cellular organisms (131567), Bacteria (2), Pseudomonadati (3379134), Pseudomonadota (1224), Alphaproteobacteria (28211), Hyphomicrobiales (356), Methylobacteriaceae (119045), Methylobacterium (407), unclassified Methylobacterium (2615210). Every label and rank matches the pinned chain. XML LineageEx omits root; Datasets includes it.

EXACT denotes this NCBI taxon, not a validly published binomial or strain/deposit equivalence. The [LPSN genus page](https://lpsn.dsmz.de/genus/methylobacterium), previously fully inspected and searched specifically for TS63, supplies no TS63 identity bridge. Genus nomenclature and properties must not be copied. The legacy NCBI browser failed through the web tool; both current NCBI authority APIs succeeded.

## Evidence

The NCBITAXON attestation matches identifier, label, count 1, unit NAME and snapshot note. One source-name assertion is not a genome or biological strain count. The `seed_from_sources` event at 2026-09-13T17:54:04Z, action SEEDED_FROM_SOURCES, exactly matches the one-source scope reason.

Exact scans found no target rows in `data/raw/bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv`, or `bactotraits_taxa.tsv`. The target has no direct backbone children. Zero BacDive strain records agrees with the seeder's own/subtree gathering rule; it does not mean TS63 was never cultured.

The live exact query `txid1035231[Organism:noexp]` returned zero assemblies with phrases-not-found/no-items diagnostics and one nucleotide UID, 347300728. Full [FR869827.1 NCBI metadata](https://www.ncbi.nlm.nih.gov/nuccore/FR869827.1), excluding bases, was read: a 1333-nt partial 16S rRNA gene, strain TS63, explicit `taxon:1035231`, and isolation source host leaf surface. Submission was 18 May 2011, creation 18 September, update 6 December 2011. No culture-collection, BioSample, BioProject or assembly identifier is supplied. Genomic DNA describes the molecule source, not a complete genome.

The source explicitly cites [PMID 22000032](https://pubmed.ncbi.nlm.nih.gov/22000032/) and [DOI 10.1016/j.syapm.2011.08.005](https://doi.org/10.1016/j.syapm.2011.08.005). The current PubMed bibliography and complete abstract fetched earlier this session were re-read for TS63. They describe community comparisons, not named TS63-specific growth, phenotype or collection locality. Full text and supplements were not inspected.

**External host caveat, not a YAML finding:** the NCBI source qualifier says `Trifolium holosteoides`. The cited abstract instead names Trifolium repens and Cerastium holosteoides as the study's hosts. A direct read of the full [ENA FR869827.1 flatfile](https://www.ebi.ac.uk/ena/browser/api/embl/FR869827.1?download=false) confirmed the same `Trifolium holosteoides` qualifier, strain TS63 and taxon 1035231. ENA was unavailable through the web tool but the read-only HTTP request subsequently succeeded. This confirms the deposited wording, not which biological host was intended. Do not silently substitute either study host or a neighboring isolate's host. The YAML asserts no host, so this unresolved external inconsistency does not make its current assertions wrong.

## Completeness

Searches included ignored and compressed files with `rg --no-ignore --hidden -n -z -i` over `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Taxid, bounded exact label and slug yielded 12 rows, all fully inspected: three genuine taxonomy/name/scope rows plus nine unrelated numeric matches below. All five discovered `SOURCE.json` metadata files were separately parsed for target values and yielded no match. Ignored-independent history path enumeration found no target artifact.

The expanded same-root query `(Methylobacterium|Methylorubrum).*\bTS[- _]?63\b|\bTS[- _]?63\b.*(Methylobacterium|Methylorubrum)` returned only those three genuine rows. Variants are search leads, not aliases. An accession search for FR869827 found no rows in the same roots. These are bounded local-catalog and exact live-query results, not universal absence claims.

The current `normalize_culture_identifier` returned empty for TS63, TS-63 and TS 63. No eligible deposit or owning strain bridge was established, and no required missing strain/genome association was demonstrated. The marker may supply optional identity evidence but does not establish an owning BacDive strain or same-deposit StrainInfo assertion. Optional definition, evidence and graphs need not be invented, especially not a resolved host claim from inconsistent external metadata.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the stored assertions. Pass is bounded by the inspected evidence and searches; unrun corpus gates and the unresolved external host wording are explicitly not certified.

## Recommended Edits

None required to the current YAML. Keep the generated record and SEEDED status unchanged.

Do not add or normalize a TS63 host assertion until target-specific primary evidence resolves the deposited wording. Any future host/phenotype representation must respect sibling-repository ownership in `docs/CURATION.md`; this review does not authorize a source correction or outbound contact.

Future supported strain/deposit/genome additions belong in maintained extraction/matching/seeding logic under `src/taxonmech/`, with regression tests and documented regeneration. Scope edits belong in `curation/seed_scope.tsv`; upstream mapping fixes belong in kg-microbe. Never patch generated YAML or pages to insert an inferred link.

## Follow-up Checks

For the external host uncertainty, inspect an isolate-labelled table, supplement or corrected primary submission that explicitly connects TS63 or FR869827 to the host. The community abstract and adjacent isolate designations cannot resolve it. Preserve the original qualifier and source provenance until a supported correction exists.

Before any new genome link, require the target's own eligible culture accession and source chain. StrainInfo sequences must name that same SI-DP; GOLD must resolve the own-organism/project/analysis chain; ATB requires an exact already-supported BioSample and eligible available FASTA. Keep taxon, strain, deposit, sample, project, marker and assembly identities separate.

After any authorized maintained-input change, run target schema/strict validation and relevant regression tests, then `just verify-corpus` and `just qc`.

## Additional Notes

- Four excluded rows are Lactobacillus gasseri taxid 1596, strain 1001285st1_G3_RTP21277_210401, GCA/GCF_040925185.1, BV-BRC 1596.1053, sample SAMN41035231: `data/bvbrc/bvbrc-0004.jsonl.gz:16797`, `data/catalog/ncbi_genbank-0037.jsonl.gz:20864`, `data/catalog/ncbi_refseq-0006.jsonl.gz:20010`, `data/catalog/gtdb_genomes-0012.jsonl.gz:37649`.
- Two rows are Alphaproteobacteria bacterium taxid 1913988, isolate RGIG8297, GCA_017614525.1, sample SAMN16348799: `data/catalog/gtdb_genomes-0017.jsonl.gz:22061` and `data/catalog/ncbi_genbank-0016.jsonl.gz:5229`. Total/ungapped length 1035231 triggered the search, not their taxid. Their metagenomic gastrointestinal provenance and GTDB UBA3830 classification do not identify TS63.
- `data/bvbrc/bvbrc-0006.jsonl.gz:6253` is Mycobacterium tuberculosis taxid 1773, genome 1773.18447, strain/run ERR1035231.
- `data/catalog/ncbi_genbank-0053.jsonl.gz:47921` is Vibrio parahaemolyticus taxid 670, strain PNUSAV007787, GCA_058323135.1, sample SAMN61035231.
- `data/catalog/allthebacteria.tsv.xz:569701` is Mycobacterium tuberculosis, run ERR1035231, sample SAMEA3558764, analysis ERZ3502572. Its available FASTA and PASS filters do not supply TS63 identity.
- All native candidate fields were losslessly inspected. No unrelated genome or sample was transferred. ENA retains historical classification strings Proteobacteria/Rhizobiales; the current NCBI backbone governs the YAML lineage. ENA's additional sequence-database crossreferences were not used to infer taxon identity, host or genome equivalence.
- The target was re-read and byte-identical before reporting. Only this new report was written; no YAML, history, mapping status, generated product, Git or GitHub mutation was performed.

