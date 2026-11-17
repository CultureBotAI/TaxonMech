# YAML Record Review: uncultured gamma proteobacterium TIHP368-31

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_31.yaml`
- Started UTC: 2026-10-04T05:11:01Z
- Finished UTC: 2026-10-04T05:11:45Z
- Verdict: pass

## Target

The full generated `TaxonRecord` identifies `NCBITaxon:103306`, uncultured gamma proteobacterium TIHP368-31. It has species rank, BACTERIA domain, parent 50423, seven root-first ancestors, code 11, EXACT grounding, SEEDED status and zero BacDive strains. Its sole attestation is NCBITAXON, 1 NAME, snapshot 2026-09-13; its seed event is dated 2026-09-13T17:54:04Z.

Future corrections belong to maintained source inputs, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` and, for inclusion changes, `curation/seed_scope.tsv`. Generated YAML is read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_31.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_31.yaml`: passed, one file, zero errors; refreshed the standard strict-validation TSV.
- Structured checks matched complete backbone identity, lineage, code, attestation, scope/PATHS registration and seed text. These checks do not replace corpus reproduction.
- Not checked: full-corpus `verify-corpus`, QC/tests, global term/reference/history/provenance/product gates or rendering. No canary, regeneration or history/status mutation ran.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:18415`, name-catalog shard 0000 row 38433, PATHS row 13354 and scope row 144075 agree. Live NCBI EFetch and Datasets confirm the exact label, species rank, parent 50423, code 11 and lineage IDs 1, 131567, 2, 3379134, 1224, 1236, 50423. The parent is the environmental-samples grouping beneath Gammaproteobacteria. [NCBI taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103306&retmode=xml)

The full clone designation is retained without extra synonyms, a formal binomial, cultivation or type-material claims. Source species rank supports inclusion without implying nomenclatural publication.

## Evidence

Pinned and live taxonomy support the NCBITAXON NAME attestation. Exact-taxid Nuccore ESearch returned one entry, UID 5869741. Its inspected qualifiers identify AB031647.1, a 722 bp partial 16S rRNA sequence, with taxon:103306, clone TIHP368-31, environmental_sample and coastal marine sediment. This directly resolved marker is not an assembly or culture deposit. [NCBI nucleotide](https://www.ncbi.nlm.nih.gov/nuccore/AB031647.1)

Reference metadata describes an unpublished coastal-community 16S/quinone study by Urakawa, Yoshida, Nishimura and Ohwada, plus direct submission on 1999-08-25. No DOI/PMID is supplied by those entries or the YAML. Study context is not clone-specific phenotype evidence.

Exact-taxid Assembly ESearch returned zero results with a phrase-not-found/no-items warning. This bounded result is not universal proof of genome absence.

## Completeness

Complete exact-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row, direct backbone child, or own-ID type-material, merged-ID or dropped-ID row. Optional strains, nomenclature, mappings and functional fields are appropriately empty. Zero strain_count follows the BacDive-subtree definition.

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` covered bounded 103306, TIHP368-31/underscore spelling and the full stem across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 37 matched lines and structured contexts were inspected. SOURCE.json files were separately scanned, yielding two BacDive request matches in its own namespace. No target-specific deposit, assembly, non-NCBI attestation or separate history reference was found within these bounds.

CIP 103306 belongs to Vogesella indigofera/45465, BacDive 10507, designations Ml/M1, LPSN 783059 and SI-ID 4115's own deposit 156208. LPSN synonym Pseudomonas indigofera/780040 shares that culture context. Their type material, nomenclature, publications and AB021385 marker do not support this clone.

Other excluded matches include BacDive 103306, Agromyces sp. ST027925/51513, and CP103306 in PLL12/taxid 2971128. Five BV-BRC records, 2971128.3 through 2971128.7, carry the latter accession; only the inspected 2971128.4 row supplied GCA_024760305.1. That co-occurrence was not used to assert genome equivalence or transfer an assembly to this taxon.

Genome collisions include Levilactobacillus brevis SRCM 103306/GCA/GCF_004055405.1, uncultured Muribaculaceae bacterium MGBC103306/GCA_910577355.1, Shigella flexneri PNUSAE103306/GCA_023670545.1, Salmonella enterica PNUSAS103306/GCA_008789425.1, Listeria monocytogenes FLAG-103306/GCA_050885025.1, Pseudomonas aeruginosa PSA-BAB-IMI-103306/GCA_023905375.1 and uncultured bacterium MarMAG_103306/GCA_977611405.1. ATB DRR103306 belongs to E. coli sample SAMD00077714. Assembly-statistic matches are unrelated. Source-specific names, spacing and accession versions were preserved.

No gene, resistance, pathway, expression-module or causal assertion is present. iModulonDB is not applicable, not negative evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed record and source scope.

## Recommended Edits

None required. Future enrichment should preserve exact environmental-clone identity and represent AB031647.1 only as directly sourced marker evidence. Do not infer neighboring accessions, genome equivalence from co-occurrence, or culture/phenotype claims from numeric collisions.

## Follow-up Checks

After an authorized maintained-input change, run `just seed-canary NCBITaxon:103306 --force`, inspect the output and repeat both focused validators. No canary ran here. Reconfirm exact sequence source qualifiers before enrichment; run corpus-wide gates before broader release.

## Additional Notes

The web tool could not retrieve the taxonomy browser page; direct public NCBI EFetch, Datasets, ESearch and nucleotide EFetch succeeded. Reference metadata was inspected without claiming access to unpublished results.

No YAML, source input, curation event, mapping status, separate history, generated page or GitHub item changed. Only this new report was manually written; earlier reports were preserved.
