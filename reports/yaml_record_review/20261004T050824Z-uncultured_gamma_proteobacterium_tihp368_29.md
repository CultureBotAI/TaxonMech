# YAML Record Review: uncultured gamma proteobacterium TIHP368-29

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_29.yaml`
- Started UTC: 2026-10-04T05:07:24Z
- Finished UTC: 2026-10-04T05:08:24Z
- Verdict: pass

## Target

The full generated `TaxonRecord` denotes `NCBITaxon:103304`, uncultured gamma proteobacterium TIHP368-29. It carries species rank, BACTERIA domain, parent 50423, seven root-first ancestors, code 11, EXACT grounding, SEEDED status and zero BacDive strains. NCBITAXON is its sole attestation, 1 NAME, snapshot 2026-09-13; its seed event is dated 2026-09-13T17:54:04Z.

Future corrections belong to maintained source inputs, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` and, for inclusion changes, `curation/seed_scope.tsv`. Generated YAML is read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_29.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_29.yaml`: passed, one file, zero errors; refreshed the standard strict-validation TSV.
- Structured checks matched complete backbone identity, lineage, code, attestation, scope/PATHS registration and seed text. They do not replace corpus reproduction.
- Not checked: full-corpus `verify-corpus`, QC/tests, global term/reference/history/provenance/product gates or rendering. No canary, regeneration or history/status mutation ran.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:18413`, name-catalog shard 0000 row 38431, PATHS row 13352 and scope row 144073 agree. Live NCBI EFetch and Datasets confirm the exact label, species rank, parent 50423, code 11 and lineage IDs 1, 131567, 2, 3379134, 1224, 1236, 50423. The parent is the environmental-samples grouping beneath Gammaproteobacteria. [NCBI taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103304&retmode=xml)

No extra synonym, formal binomial, cultivation or type-material claim is asserted. The full clone suffix is preserved. Source species rank supports inclusion without implying nomenclatural publication.

## Evidence

Pinned and live taxonomy support the NCBITAXON NAME attestation. Exact-taxid Nuccore ESearch returned one entry, UID 5869739. Its inspected qualifiers identify AB031645.1, a 743 bp partial 16S rRNA sequence, with taxon:103304, clone TIHP368-29, environmental_sample and coastal marine sediment. This directly resolved marker is not an assembly or culture deposit. [NCBI nucleotide](https://www.ncbi.nlm.nih.gov/nuccore/AB031645.1)

Reference metadata describes an unpublished coastal-community 16S/quinone study by Urakawa, Yoshida, Nishimura and Ohwada, plus direct submission on 1999-08-25. Neither these entries nor the YAML supply a DOI/PMID. Study context does not prove clone-specific functional traits.

Exact-taxid Assembly ESearch returned zero results with a phrase-not-found/no-items warning. This bounded query result is not universal proof of genome absence.

## Completeness

Complete exact-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row, direct backbone child, or own-ID type-material, merged-ID or dropped-ID row. Optional strains, nomenclature, mappings and functional fields are appropriately empty. Zero strain_count follows the BacDive-subtree definition.

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` covered bounded 103304, TIHP368-29/underscore spelling and the complete stem across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 42 matched lines and structured contexts were inspected. Separately scanned SOURCE.json files yielded two BacDive request matches in its own namespace. No target-specific deposit, assembly, non-NCBI attestation or separate history reference was found within these bounds.

CIP 103304 concerns Hydrogenophaga palleronii strain 362, BacDive 2965, strain taxid 1349791/species 65655 and SI-ID 92268's own deposit 151676. LPSN 776947 and the Pseudomonas palleronii synonym 780088 carry that designation and AF078769 marker. These type-material, nomenclature and publication assertions do not concern TIHP368-29.

DSM 103304 concerns taxid 1852379, BacDive 160767, also Marseille-P2911, and SI-ID 403653's own deposit 910739. BacDive and StrainInfo label it Colibacter massiliensis, while the NCBI type-material row and LPSN 68478 use Megasphaera coli. BacDive marks it non-type, whereas the NCBI type-material and LPSN rows identify DSM 103304 as type material. These source differences were preserved rather than reconciled. They and marker LT576403 remain unrelated to this clone.

Other excluded matches include BacDive 103304, Agromyces sp. ST027919/51513; KY103304 in Brettanomyces anomalus SI-ID 178054; and CP103304 in Klebsiella pneumoniae Kpn1695/573, GCA_025723265.1. Genome collisions include uncultured Eubacteriales bacterium MGBC103304/GCA_948665745.1, Shigella flexneri PNUSAE103304/GCA_023670465.1, Listeria monocytogenes FLAG-103304/GCA_050885045.1, Salmonella enterica PNUSAS103304/GCA_008791605.1 and uncultured bacterium MarMAG_103304/GCA_977587775.1. ATB DRR103304 belongs to E. coli sample SAMD00077712. Assembly statistics and Streptococcus/Campylobacter SeqKit-checksum substrings are not identity evidence. Source-specific names and accession versions were preserved.

No gene, resistance, pathway, expression-module or causal assertion is present. iModulonDB is not applicable, not negative evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed record and source scope.

## Recommended Edits

None required. Future enrichment should preserve exact environmental-clone identity and represent AB031645.1 only as directly sourced marker evidence. Do not infer adjacent accessions or transfer culture, genome, nomenclature or phenotype evidence through numeric collisions.

## Follow-up Checks

After an authorized maintained-input change, run `just seed-canary NCBITaxon:103304 --force`, inspect the output and repeat both focused validators. No canary ran here. Reconfirm sequence qualifiers before enrichment; run corpus-wide gates before broader release.

## Additional Notes

The web tool could not retrieve the taxonomy browser page; direct public NCBI EFetch, Datasets, ESearch and nucleotide EFetch succeeded. Reference metadata was inspected without claiming access to unpublished results. The DSM culture's source-name and type-status differences are excluded context, not findings against this clone.

No YAML, source input, curation event, mapping status, separate history, generated page or GitHub item changed. Only this new report was manually written; earlier reports were preserved.
