# YAML Record Review: uncultured gamma proteobacterium TIHP368-58

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_58.yaml`
- Started UTC: 2026-10-04T05:21:10Z
- Finished UTC: 2026-10-04T05:21:53Z
- Verdict: pass

## Target

The full generated `TaxonRecord` identifies `NCBITaxon:103312`, uncultured gamma proteobacterium TIHP368-58. It carries species rank, BACTERIA domain, parent 50423, seven root-first ancestors, code 11, EXACT grounding, SEEDED status and zero BacDive strains. Its sole attestation is NCBITAXON, 1 NAME, snapshot 2026-09-13; its seed event is dated 2026-09-13T17:54:04Z.

Future corrections belong to maintained source inputs, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` and, for inclusion changes, `curation/seed_scope.tsv`. Generated YAML is read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_58.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_58.yaml`: passed, one file, zero errors; refreshed the standard strict-validation TSV.
- Structured checks matched complete backbone identity, lineage, code, attestation, scope/PATHS registration and seed text. These checks do not replace corpus reproduction.
- Not checked: full-corpus `verify-corpus`, QC/tests, global term/reference/history/provenance/product gates or rendering. No canary, regeneration or history/status mutation ran.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:18421`, name-catalog shard 0000 row 38439, PATHS row 13360 and scope row 144081 agree. Live NCBI EFetch and Datasets confirm the exact label, species rank, parent 50423, code 11 and lineage IDs 1, 131567, 2, 3379134, 1224, 1236, 50423. The parent is the environmental-samples grouping beneath Gammaproteobacteria. [NCBI taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103312&retmode=xml)

The full clone designation is retained without extra synonyms, a formal binomial, cultivation or type-material claims. Source species rank supports inclusion without implying nomenclatural publication.

## Evidence

Pinned and live taxonomy support the NCBITAXON NAME attestation. Exact-taxid Nuccore ESearch returned one entry, UID 5869748. Its inspected qualifiers identify AB031654.1, a 716 bp partial 16S rRNA sequence, with taxon:103312, clone TIHP368-58, environmental_sample and coastal marine sediment. This directly resolved marker is not an assembly or culture deposit. [NCBI nucleotide](https://www.ncbi.nlm.nih.gov/nuccore/AB031654.1)

Reference metadata describes an unpublished coastal-community 16S/quinone study by Urakawa, Yoshida, Nishimura and Ohwada, plus direct submission on 1999-08-25. Neither these entries nor the YAML supply a DOI/PMID. Study context does not establish clone-specific phenotype claims.

Exact-taxid Assembly ESearch returned zero results with a phrase-not-found/no-items warning. This bounded query result is not universal proof of genome absence.

## Completeness

Complete exact-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row, direct backbone child, or own-ID type-material, merged-ID or dropped-ID row. Optional strains, nomenclature, mappings and functional fields are appropriately empty. Zero strain_count follows the BacDive-subtree definition.

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` covered bounded 103312, TIHP368-58/underscore spelling and the full stem across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 31 matching lines and structured contexts were inspected. SOURCE.json files were separately scanned, yielding two BacDive request matches in its own namespace. No target-specific deposit, assembly, non-NCBI attestation or separate history reference was found within these bounds.

CIP 103312 concerns KA3, BacDive 135243/taxid 34011, explicitly non-type in BacDive. SI-ID 1060 owns deposit 4285. The source strain record uses Niveispirillum irakense/LPSN 11111, while the own deposit and BacDive use Azospirillum irakense, with LPSN 773594 on the deposit. These names were preserved at their respective source scopes. This culture is not TIHP368-58, and the type-strain evidence associated with neighboring CIP 103311 was not transferred to it or to the target.

Other excluded matches include BacDive 103312, Agromyces sp. ST027971/51513; KY103312 in Brettanomyces bruxellensis SI-ID 178017; and CP103312 in a GOLD analysis named Mycobacterium ulcerans ATCC 19423. Genome collisions include uncultured Atopobiaceae bacterium MGBC103312/GCA_948653235.1, Pseudomonas aeruginosa PSA-BAB-IMI-103312/GCA_033091715.1, Shigella sonnei PNUSAE103312/GCA_023698005.1, Salmonella enterica PNUSAS103312/GCA_008795135.1, Listeria monocytogenes FLAG-103312/GCA_050885085.1 and uncultured bacterium MarMAG_103312/GCA_977612275.1. ATB DRR103312 belongs to E. coli sample SAMD00077720. Unrelated assembly statistics and Staphylococcus/Salmonella SeqKit-checksum substrings do not establish identity. Source-specific labels and accession versions were preserved.

No gene, resistance, pathway, expression-module or causal assertion is present. iModulonDB is not applicable, not negative evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed record and source scope.

## Recommended Edits

None required. Future enrichment should preserve exact environmental-clone identity and represent AB031654.1 only as directly sourced marker evidence. Do not infer neighboring accessions or transfer culture, genome, type-material or phenotype claims through numeric collisions.

## Follow-up Checks

After an authorized maintained-input change, run `just seed-canary NCBITaxon:103312 --force`, inspect the output and repeat both focused validators. No canary ran here. Reconfirm exact sequence qualifiers before enrichment; run corpus-wide gates before broader release.

## Additional Notes

The web tool could not retrieve the taxonomy browser page; direct public NCBI EFetch, Datasets, ESearch and nucleotide EFetch succeeded. Reference metadata was inspected without claiming access to unpublished results. The unrelated culture's source names are excluded context, not findings against this clone.

No YAML, source input, curation event, mapping status, separate history, generated page or GitHub item changed. Only this new report was manually written; earlier reports were preserved.
