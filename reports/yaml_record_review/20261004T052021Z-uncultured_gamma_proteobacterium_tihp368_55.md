# YAML Record Review: uncultured gamma proteobacterium TIHP368-55

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_55.yaml`
- Started UTC: 2026-10-04T05:19:35Z
- Finished UTC: 2026-10-04T05:20:21Z
- Verdict: pass

## Target

The full generated `TaxonRecord` identifies `NCBITaxon:103311`, uncultured gamma proteobacterium TIHP368-55. It carries species rank, BACTERIA domain, parent 50423, seven root-first ancestors, code 11, EXACT grounding, SEEDED status and zero BacDive strains. NCBITAXON is the sole attestation, 1 NAME, snapshot 2026-09-13; the seed event is dated 2026-09-13T17:54:04Z.

Future corrections belong to maintained source inputs, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` and, for inclusion changes, `curation/seed_scope.tsv`. Generated YAML is read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_55.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_55.yaml`: passed, one file, zero errors; refreshed the standard strict-validation TSV.
- Structured checks matched complete backbone identity, lineage, code, attestation, scope/PATHS registration and seed text. These checks do not replace corpus reproduction.
- Not checked: full-corpus `verify-corpus`, QC/tests, global term/reference/history/provenance/product gates or rendering. No canary, regeneration or history/status mutation ran.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:18420`, name-catalog shard 0000 row 38438, PATHS row 13359 and scope row 144080 agree. Live NCBI EFetch and Datasets confirm the exact label, species rank, parent 50423, code 11 and lineage IDs 1, 131567, 2, 3379134, 1224, 1236, 50423. The parent is the environmental-samples grouping beneath Gammaproteobacteria. [NCBI taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103311&retmode=xml)

The complete clone designation is retained without extra synonyms, a formal binomial, cultivation or type-material claims. Source species rank supports inclusion without implying nomenclatural publication.

## Evidence

Pinned and live taxonomy support the NCBITAXON NAME attestation. Exact-taxid Nuccore ESearch returned one entry, UID 5869747. Its inspected qualifiers identify AB031653.1, a 572 bp partial 16S rRNA sequence, with taxon:103311, clone TIHP368-55, environmental_sample and coastal marine sediment. This directly resolved marker is not an assembly or culture deposit. [NCBI nucleotide](https://www.ncbi.nlm.nih.gov/nuccore/AB031653.1)

Reference metadata describes an unpublished coastal-community 16S/quinone study by Urakawa, Yoshida, Nishimura and Ohwada, plus direct submission on 1999-08-25. Neither those entries nor the YAML supply a DOI/PMID. Study context does not establish clone-specific phenotype claims.

Exact-taxid Assembly ESearch returned zero results with a phrase-not-found/no-items warning. This bounded query result is not universal proof of genome absence.

## Completeness

Complete exact-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row, direct backbone child, or own-ID type-material, merged-ID or dropped-ID row. Optional strains, nomenclature, mappings and functional fields are appropriately empty. Zero strain_count follows the BacDive-subtree definition.

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` covered bounded 103311, TIHP368-55/underscore spelling and the full stem across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 38 matched lines and structured contexts were inspected. SOURCE.json files were separately scanned, yielding two BacDive request matches in its own namespace. No target-specific deposit, assembly, non-NCBI attestation or separate history reference was found within these bounds.

CIP 103311 concerns KBC 1/KBC1, BacDive 13995, strain taxid 1121034/species 34011 and SI-ID 1059's own deposit 4282. BacDive, StrainInfo and LPSN 11111 use Niveispirillum irakense; the NCBI type-material rows, GOLD Go0624819 and LPSN synonym 773594 use Azospirillum irakense. These source names were preserved. Their type material, publications and Z29583 marker do not concern this clone.

Other excluded matches include BacDive 103311, Agromyces sp. ST027958/51513; SI-DP 103311, Bacillus subtilis ATCC 23858 in SI-ID 38269; KY103311 in Brettanomyces bruxellensis SI-ID 177734; and CP103311 in RL-GZ01/taxid 103816, GCA_024760325.1. Genome collisions include Lactiplantibacillus plantarum SRCM103311/GCA/GCF_004101325.1, uncultured Prevotella sp. MGBC103311/GCA_948626385.1 with historical RefSeq GCF_948626385.1, Pseudomonas aeruginosa PSA-BAB-IMI-103311/GCA_033091635.1, Salmonella enterica PNUSAS103311/GCA_008789605.1 and Saccharimonadales bacterium (SeqCode) PELAGICS-MAG-m2-bin103311-CADAX-SM-03sep20/GCA_964905565.1. The latter source's isolate field includes a trailing period, unlike its assembly name; neither is a target identity match. ATB DRR103311 belongs to E. coli sample SAMD00077719. An unrelated assembly statistic does not establish identity. Source-specific names and accession versions were preserved.

No gene, resistance, pathway, expression-module or causal assertion is present. iModulonDB is not applicable, not negative evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed record and source scope.

## Recommended Edits

None required. Future enrichment should preserve exact environmental-clone identity and represent AB031653.1 only as directly sourced marker evidence. Do not infer neighboring accessions or transfer culture, genome, nomenclature or phenotype claims through numeric collisions.

## Follow-up Checks

After an authorized maintained-input change, run `just seed-canary NCBITaxon:103311 --force`, inspect the output and repeat both focused validators. No canary ran here. Reconfirm sequence source qualifiers before enrichment; run corpus-wide gates before broader release.

## Additional Notes

The web tool could not retrieve the taxonomy browser page; direct public NCBI EFetch, Datasets, ESearch and nucleotide EFetch succeeded. Reference metadata was inspected without claiming access to unpublished results. Source-name differences for the unrelated CIP culture are excluded context, not findings against this clone.

No YAML, source input, curation event, mapping status, separate history, generated page or GitHub item changed. Only this new report was manually written; earlier reports were preserved.
