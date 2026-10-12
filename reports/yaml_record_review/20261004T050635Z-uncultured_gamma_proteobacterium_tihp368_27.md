# YAML Record Review: uncultured gamma proteobacterium TIHP368-27

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_27.yaml`
- Started UTC: 2026-10-04T05:05:33Z
- Finished UTC: 2026-10-04T05:06:35Z
- Verdict: pass

## Target

The full generated `TaxonRecord` identifies `NCBITaxon:103303`, uncultured gamma proteobacterium TIHP368-27. It has species rank, BACTERIA domain, parent 50423, seven root-first ancestors, code 11, EXACT grounding, SEEDED status and zero BacDive strains. NCBITAXON is its sole attestation, 1 NAME, snapshot 2026-09-13; its seed event is dated 2026-09-13T17:54:04Z.

Future corrections belong to maintained source inputs, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` and, for inclusion changes, `curation/seed_scope.tsv`. Generated YAML is read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_27.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_27.yaml`: passed, one file, zero errors; refreshed the standard strict-validation TSV.
- Structured checks matched complete backbone identity, lineage, code, attestation, scope/PATHS registration and seed text. These checks do not replace corpus reproduction.
- Not checked: full-corpus `verify-corpus`, QC/tests, global term/reference/history/provenance/product gates or rendering. No canary, regeneration or history/status mutation ran.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:18412`, name-catalog shard 0000 row 38430, PATHS row 13351 and scope row 144072 agree. Live NCBI EFetch and Datasets confirm the exact label, species rank, parent 50423, code 11 and lineage IDs 1, 131567, 2, 3379134, 1224, 1236, 50423. The parent is the environmental-samples grouping beneath Gammaproteobacteria. [NCBI taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103303&retmode=xml)

The complete clone designation is retained without extra synonyms, a formal binomial, cultivation or type-material claims. Source species rank supports inclusion without implying nomenclatural publication.

## Evidence

Pinned and live taxonomy support the NCBITAXON NAME attestation. Exact-taxid Nuccore ESearch returned one entry, UID 5869738. Its inspected qualifiers identify AB031644.1, an 806 bp partial 16S rRNA sequence, with taxon:103303, clone TIHP368-27, environmental_sample and coastal marine sediment. This directly resolved marker is not an assembly or culture deposit. [NCBI nucleotide](https://www.ncbi.nlm.nih.gov/nuccore/AB031644.1)

Reference metadata describes an unpublished coastal-community 16S/quinone study by Urakawa, Yoshida, Nishimura and Ohwada, plus direct submission on 1999-08-25. Neither these entries nor the YAML supply a DOI/PMID. Study context is not clone-specific phenotype evidence.

Exact-taxid Assembly ESearch returned zero results with a phrase-not-found/no-items warning. This bounded query result is not universal proof of genome absence.

## Completeness

Complete exact-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row, direct backbone child, or own-ID type-material, merged-ID or dropped-ID row. Optional strains, nomenclature, mappings and functional fields are appropriately empty. Zero strain_count follows the BacDive-subtree definition.

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` covered bounded 103303, TIHP368-27/underscore spelling and the complete stem in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 49 matched lines and structured contexts were inspected. SOURCE.json files were separately scanned, yielding two BacDive request matches in its own namespace. No target-specific deposit, assembly, non-NCBI attestation or separate history reference was found within these bounds.

CIP 103303 concerns BacDive 2885, designation 133/FD-6, taxid 47920, and SI-ID 92080's own deposit 148000. BacDive, StrainInfo and LPSN 772600 call it Acidovorax delafieldii; the NCBI type-material row and LPSN synonym 780003 use Pseudomonas delafieldii. GOLD Go0207021 instead labels CIP 103303 Pseudomonas putida/303. These source classifications were preserved, not reconciled or transferred to TIHP368-27. Their type material, nomenclature, publications and AF078764 marker do not support this clone. DSM 103303 is Shigella dysenteriae RKI00-04776/622, BacDive 131935, SI-ID 399936's own deposit 906765, distinct from both CIP 103303 and this taxon.

Other excluded matches include BacDive 103303, Agromyces sp. ST027895/51513; SI-DP 103303, Salmonella enterica subsp. enterica ATCC 23855 in SI-ID 38267; KY103303 in Brettanomyces anomalus SI-ID 180275; and CP103303 in Klebsiella pneumoniae Kpn1695/573, GCA_025723265.1. Genome collisions include Lactiplantibacillus plantarum SRCM103303/GCA/GCF_004141895.1, uncultured Duncaniella sp. MGBC103303/GCA_948651185.1, Shigella flexneri PNUSAE103303/GCA_023670475.1 and isolate 103303/GCA_026021775.1, Salmonella enterica PNUSAS103303/GCA_008791585.1, and Acidaminobacteraceae bacterium MarMAG_103303/GCA_977601505.1. ATB DRR103303 belongs to E. coli sample SAMD00077711. Assembly-statistic matches are unrelated. Source-specific names and accession versions were preserved.

No gene, resistance, pathway, expression-module or causal claim occurs. iModulonDB is not applicable, not negative evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed record and source scope.

## Recommended Edits

None required. Future enrichment should preserve exact environmental-clone identity and represent AB031644.1 only as directly sourced marker evidence. Do not infer neighboring accessions or transfer culture, genome, nomenclature or phenotype claims through numeric coincidences.

## Follow-up Checks

After an authorized maintained-input change, run `just seed-canary NCBITaxon:103303 --force`, inspect the output and repeat both focused validators. No canary ran here. Reconfirm sequence source qualifiers before enrichment; run corpus-wide gates before broader release.

## Additional Notes

The web tool could not retrieve the taxonomy browser page; direct public NCBI EFetch, Datasets, ESearch and nucleotide EFetch succeeded. Reference metadata was inspected without claiming access to unpublished results. The conflicting CIP culture classifications are excluded context, not findings against this clone.

No YAML, source input, curation event, mapping status, separate history, generated page or GitHub item changed. Only this new report was manually written; earlier reports were preserved.
