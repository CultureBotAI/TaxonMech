# YAML Record Review: Wolbachia endosymbiont of Tersilochus sp.

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_tersilochus_sp.yaml`
- Started UTC: 2026-10-09T15:10:41Z
- Finished UTC: 2026-10-09T15:13:43Z
- Verdict: pass

## Target

One generated `TaxonRecord`, `NCBITaxon:1036781`, was resolved and read in full. It has rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2640676` (unclassified Wolbachia), grounding `EXACT`, status `SEEDED`, genetic code 11, zero inventoried strains and one NCBITAXON name attestation. Its SHA-256 is `7a444e63de70fe653082627ca2f0b82f491c21020b5e95d22fa4f6a24a6e2855`.

The ignored-inclusive target/report filename search resolved only this YAML and no existing own report. The bacterial endosymbiont is the target, not its eukaryotic host; no host record was reviewed or changed.

## Validation

The existing offline environment was used with `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/wolbachia_endosymbiont_of_tersilochus_sp.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/wolbachia_endosymbiont_of_tersilochus_sp.yaml --workers 1 --out /private/tmp/taxonmech-wter-20261009-validation.tsv`: passed, one file and zero errors. The TSV contains only its header.
- `uv run --offline python scripts/validate_history.py history`: passed, 17 valid records and zero invalid history links.
- Read-only structured checks matched the complete ancestor chain, identity fields, attestation, PATHS/scope rows and seeding-event text against the target's own inventory.
- Not checked: full-corpus `just verify-corpus`, full-corpus schema/provenance/QC/tests and rendered-site drift were not rerun. The reproduction gate has no single-record selector; the targeted comparisons do not establish corpus reproduction.
- Not applicable: OAK graph-node label checks, because this record contains no curator-added graph. The configured product gate excludes carried taxonomy fields.
- Not applicable: iModulonDB gene/component checks. The YAML makes no gene, regulator, pathway, trait or transcriptomic claim. The supplementary COI sequence discovery below does not change that scope.
- The web tool could not open the NCBI Taxonomy browser, but direct live NCBI EFetch and Datasets taxonomy responses were both inspected successfully. The PMC article mirror returned a browser challenge; the publisher's article text was accessible instead.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222621` independently supports label, rank, parent, genetic code, snapshot date and sole attesting source. `data/catalog/ncbi_names-0005.jsonl.gz:32199` contains the scientific name and no alternative-name assertion for this taxon.

Live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036781&retmode=xml) confirms ID 1036781, the exact label, species rank, parent 2640676 and genetic code 11. The [Datasets taxonomy response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036781) independently agrees.

All 11 root-first lineage entries match the backbone and live taxonomy: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Alphaproteobacteria 28211; Rickettsiales 766; Anaplasmataceae 942; Wolbachieae 952; Wolbachia 953; unclassified Wolbachia 2640676. The tribe and unranked grouping are retained rather than dropped or replaced by an inferred species identity.

`SPECIES` here is the NCBI node's rank. It does not establish a validly published binomial, a type culture, a Wolbachia supergroup assignment or equivalence to every Wolbachia found in the host genus. The YAML makes none of those stronger claims.

## Evidence

The one source attestation is precisely one NCBI name from the 2026-09-13 snapshot, not one genome or one cultured isolate. Both identity and count/unit trace to the backbone row.

An exact, non-expanded live NCBI nucleotide query for `txid1036781[Organism:noexp]` returned one record, [JF902305.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902305.1). Its complete GenBank metadata and features identify the same bacterial taxon, a 636-base partial COI coding region, voucher `BIOUG<CAN>:DSWAS098-06.w` and BOLD cross-reference `ASEND110-09.COI-5P`. The source records collection on 2006-08-23 at Churchill, Manitoba, Canada. Declared and actual sequence lengths agree; the sequence uses only A/C/G/T and the CDS uses translation table 11.

This is nucleotide/specimen evidence, not an assembly or eligible culture-deposit identifier. It corroborates the source-specific organism label without requiring a synthetic strain entry. The live [NCBI genome report query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1036781/dataset_report) returned an empty object, not a positive genome hit; this is a bounded API observation, not proof that no genome can exist anywhere.

The sequence's first reference is a Smith manuscript marked unpublished. The accessible [2012 primary article on Wolbachia and DNA barcoding](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0036514) describes bacterial COI amplified from insect DNA extracts and explains why bacterial and host sequences must be distinguished. It supplies study context, not independently verified specimen-specific phenotype, infection prevalence or strain identity here. No accession-specific supplementary-table claim was used. GenBank remains the direct authority for the inspected JF902305 association.

The one assembly-search candidate, `data/catalog/ncbi_genbank-0051.jsonl.gz:19538`, was read completely and rejected. It is `GCA_055615575.1`, Streptococcus pneumoniae, taxon/species ID 1313; only its isolate field is the coincident numeric string `1036781`. Joining that assembly to this Wolbachia by substring or bare numeric occurrence would be incorrect. The YAML correctly contains no such link.

## Completeness

Ignored/hidden and compressed-file searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, using the bounded taxon ID, label and Tersilochus name. All four returned rows were read: backbone, scope, native name and the unrelated numeric-isolate assembly. An additional ignored-inclusive content search for JF902305, DSWAS098 and ASEND110 returned no local candidates in those roots. All five source `SOURCE.json` metadata files were parsed; target-specific history filenames and contents were searched independently.

Complete relevant inventory scans found no own BacDive strain, LPSN name, GTDB mapping, GOLD/MediaDive/Madin/BactoTraits attestation, type-material row, merged-ID row, dropped row or child node. These are local snapshot findings, not universal absence claims. They support leaving synonyms, nomenclature, cross-source mappings and strain/genome lists empty. The external marker discovered during review does not demonstrate a missing required culture-to-genome relationship.

`data/taxa/PATHS.tsv:15149` owns the current slug, and `curation/seed_scope.tsv:322854` records the 2026-09-13 one-source inclusion. The sole YAML event, dated 2026-09-13T17:54:04Z, exactly matches the source/scope-generated text. Its generic reference to inventory directories does not assert that each directory supplied this taxon. No target-specific external history entry was found by ignored-inclusive searches; the record has not been promoted to reviewed status.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, source scope and intentionally empty optional slots are supported within the inspected evidence. No finding is inherited from a neighboring record.

## Recommended Edits

None required. Preserve the generated YAML and do not attach the unrelated Streptococcus assembly, turn the specimen voucher into a culture deposit, or generalize broad Wolbachia biology into target-specific phenotype claims.

Any later authorized enrichment should first obtain source-native, target-specific evidence. Taxonomy/inventory changes belong in the maintained source extraction and seeding inputs, not a hand edit to this record.

## Follow-up Checks

No defect-specific repair check is required. Before a future authorized regeneration, run the documented full-corpus reproduction, provenance, schema, test and publication gates. Any future genome association must demonstrate an explicit target strain/deposit or sample evidence chain; marker identity alone is insufficient.

## Additional Notes

Only this new timestamped review report was written for this target. No record, source, scope, history, generated page, branch, worktree or GitHub item was changed. Eukaryota remains outside the active review queue. The report's pass verdict is bounded to this record and the stated checks, not a corpus-wide validation claim.

