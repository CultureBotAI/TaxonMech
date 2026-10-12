# YAML Record Review: uncultured gamma proteobacterium TIHP368-54

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_54.yaml`
- Started UTC: 2026-10-04T05:18:02Z
- Finished UTC: 2026-10-04T05:18:47Z
- Verdict: pass

## Target

The full generated `TaxonRecord` identifies `NCBITaxon:103310`, uncultured gamma proteobacterium TIHP368-54. It has species rank, BACTERIA domain, parent 50423, seven root-first ancestors, code 11, EXACT grounding, SEEDED status and zero BacDive strains. The sole attestation is NCBITAXON, 1 NAME, snapshot 2026-09-13; the seed event is dated 2026-09-13T17:54:04Z.

Future corrections belong to maintained source inputs, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` and, for inclusion changes, `curation/seed_scope.tsv`. Generated YAML is read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_54.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_54.yaml`: passed, one file, zero errors; refreshed the standard strict-validation TSV.
- Structured checks matched complete backbone identity, lineage, code, attestation, scope/PATHS registration and seed text. These checks do not replace corpus reproduction.
- Not checked: full-corpus `verify-corpus`, QC/tests, global term/reference/history/provenance/product gates or rendering. No canary, regeneration or history/status mutation ran.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:18419`, name-catalog shard 0000 row 38437, PATHS row 13358 and scope row 144079 agree. Live NCBI EFetch and Datasets confirm the exact label, species rank, parent 50423, code 11 and lineage IDs 1, 131567, 2, 3379134, 1224, 1236, 50423. The parent is the environmental-samples grouping beneath Gammaproteobacteria, not the Halieaceae environmental grouping carried by TIHP368-52. [NCBI taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103310&retmode=xml)

The full clone designation is retained without extra synonyms, a formal binomial, cultivation or type-material claims. Source species rank supports inclusion without implying nomenclatural publication; the lineage is independently verified, not copied from neighboring records.

## Evidence

Pinned and live taxonomy support the NCBITAXON NAME attestation. Exact-taxid Nuccore ESearch returned one entry, UID 5869746. Its inspected qualifiers identify AB031652.1, a 755 bp partial 16S rRNA sequence, with taxon:103310, clone TIHP368-54, environmental_sample and coastal marine sediment. This directly resolved marker is not an assembly or deposit. [NCBI nucleotide](https://www.ncbi.nlm.nih.gov/nuccore/AB031652.1)

Reference metadata describes an unpublished coastal-community 16S/quinone study by Urakawa, Yoshida, Nishimura and Ohwada, plus direct submission on 1999-08-25. No DOI/PMID is supplied by these entries or the YAML. Study context is not clone-specific phenotype evidence.

Exact-taxid Assembly ESearch returned zero results with a phrase-not-found/no-items warning. This bounded query result is not universal proof of genome absence.

## Completeness

Complete exact-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row, direct backbone child, or own-ID type-material, merged-ID or dropped-ID row. Optional strains, nomenclature, mappings and functional fields are appropriately empty. Zero strain_count follows the BacDive-subtree definition.

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` covered bounded 103310, TIHP368-54/underscore spelling and the full stem across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 38 matched lines and structured contexts were inspected. SOURCE.json files were separately scanned, yielding two BacDive request matches in its own namespace. No target-specific deposit, assembly, non-NCBI attestation or separate history reference was found within these bounds.

CIP 103310 concerns Salinivibrio costicola, BacDive 17241, species taxid 51367/subspecies 149710, LPSN 780733/780735 and GOLD organism Go0298940. SI-ID 5062 has subspecies context and owns CIP deposit 22362; the inspected own-deposit taxon field is absent. NCBI type-material rows use Vibrio costicola; LPSN 782997 represents that synonym and 12856 the misspelling Vibrio costicolus. These source names and taxonomic scopes were preserved, not transferred to the clone or used to fill the missing deposit field. Their type material, references and X95527 marker do not support TIHP368-54.

Other excluded matches include BacDive 103310, Agromyces sp. ST027954/51513; CP103310 in RL-GZ01/taxid 103816, GCA_024760325.1; Pseudomonas aeruginosa PSA-BAB-IMI-103310/GCA_033091595.1; Paramuribaculum intestinale MGBC103310/GCA_948713115.1 with historical RefSeq GCF_948713115.1 also represented in the GTDB snapshot; Shigella flexneri PNUSAE103310/GCA_023674365.1; and Salmonella enterica PNUSAS103310/GCA_008791645.1. ATB DRR103310 belongs to E. coli sample SAMD00077718. Assembly-statistic matches are unrelated. Source-specific names, status and accession versions were preserved.

No gene, resistance, pathway, expression-module or causal assertion occurs. iModulonDB is not applicable, not negative evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed record and source scope.

## Recommended Edits

None required. Future enrichment should preserve exact environmental-clone identity and independently sourced lineage, and represent AB031652.1 only as marker evidence. Do not infer neighboring accessions or transfer culture, genome, nomenclature or phenotype claims through numeric collisions.

## Follow-up Checks

After an authorized maintained-input change, run `just seed-canary NCBITaxon:103310 --force`, inspect the output and repeat both focused validators. No canary ran here. Reconfirm exact source lineage and sequence qualifiers before enrichment; run corpus-wide gates before broader release.

## Additional Notes

The web tool could not retrieve the taxonomy browser page; direct public NCBI EFetch, Datasets, ESearch and nucleotide EFetch succeeded. Reference metadata was inspected without claiming access to unpublished results.

No YAML, source input, curation event, mapping status, separate history, generated page or GitHub item changed. Only this new report was manually written; earlier reports were preserved.
