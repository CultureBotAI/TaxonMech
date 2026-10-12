# YAML Record Review: uncultured Gram-positive bacterium TIHP368-02

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_gram_positive_bacterium_tihp368_02.yaml`
- Started UTC: 2026-10-04T05:51:57Z
- Finished UTC: 2026-10-04T05:52:38Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` identifies `NCBITaxon:103325`, uncultured Gram-positive bacterium TIHP368-02: species rank, BACTERIA, parent 51666, six root-first ancestors, code 11, EXACT grounding, SEEDED status and zero BacDive strains. Its sole attestation is NCBITAXON, 1 NAME, snapshot 2026-09-13; the seed event is dated 2026-09-13T17:54:04Z.

Future corrections belong to maintained source inputs, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` and, for inclusion changes, `curation/seed_scope.tsv`. Generated YAML is read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_gram_positive_bacterium_tihp368_02.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/uncultured_gram_positive_bacterium_tihp368_02.yaml`: passed, one file, zero errors; refreshed the standard strict-validation TSV.
- Structured checks matched full backbone identity, lineage, code, attestation, PATHS/scope registration and seed text. These checks do not replace corpus reproduction.
- Not checked: full-corpus `verify-corpus`, QC/tests, global term/reference/history/provenance/product gates or rendering. No canary, regeneration or history/status promotion ran.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:18434`, name-catalog shard 0000 row 38452, PATHS row 13378 and scope row 144094 agree. Live NCBI EFetch and Datasets confirm exact label, species rank, parent 51666, code 11 and the complete lineage: 1/root, 131567/cellular organisms, 2/Bacteria, 2323/Bacteria incertae sedis, 31986/Gram-positive bacteria incertae sedis and 51666/environmental samples. The incertae sedis entries are unranked. [NCBI taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103325&retmode=xml)

The leading zero in clone designation 02 is retained. Unresolved source placement is preserved without inferred kingdom or phylum. Gram-positive is source naming/grouping, not an independently inspected staining assay. No formal binomial, synonyms, cultivation or type-material status is invented; source species rank does not imply nomenclatural publication.

## Evidence

Pinned and live taxonomy support the NCBITAXON NAME attestation. Exact-taxid Nuccore ESearch returned one record, UID 5869722. Directly resolved AB031628.1 is a 736 bp partial 16S rRNA sequence whose qualifiers identify taxon:103325, clone TIHP368-02, environmental_sample and coastal marine sediment. It is a marker, not an assembly or culture deposit. [NCBI nucleotide](https://www.ncbi.nlm.nih.gov/nuccore/AB031628.1)

Reference metadata describes an unpublished coastal-community 16S/quinone study by Urakawa, Yoshida, Nishimura and Ohwada, plus direct submission on 1999-08-25. Neither these entries nor the YAML provide a DOI/PMID. Study context does not establish clone-specific phenotype claims or resolve its lineage further.

Exact-taxid Assembly ESearch returned zero results with a phrase-not-found/no-items warning. This bounded result is not universal proof of genome absence.

## Completeness

Complete exact-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row, direct backbone child, or own-ID type-material, merged-ID or dropped-ID row. Optional strains, nomenclature, mappings and functional fields are appropriately empty. Zero strain_count follows the BacDive-subtree definition.

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searched bounded 103325, TIHP368-02/underscore spelling and the full stem across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 26 matching lines and their structured contexts were inspected. Separate SOURCE.json scans yielded two BacDive request matches in its own namespace. No target-specific deposit, assembly, non-NCBI attestation or separate history reference was found within these bounds.

CIP 103325 concerns culture 798, BacDive 6831, explicitly non-type. BacDive, GOLD Go0271946 and the SI-ID 47959 strain record use Leuconostoc pseudomesenteroides/taxid 33968; the strain record also carries LPSN 777558. Its own SI-DP 152446 instead supplies Leuconostoc mesenteroides mesenteroides/taxid 33967. This source classification conflict is retained at its strain/deposit scopes, not resolved or transferred to TIHP368-02.

BacDive 103325 itself denotes Agromyces sp. ST018443/51513. CP103325 belongs to Lactiplantibacillus plantarum Ep-M17/GCA_032818175.1, BV-BRC 1590.4194. Other excluded genome collisions include uncultured Alphaproteobacteria bacterium MGBC103325/GCA_910576955.1, Pseudomonas aeruginosa PSA-BAB-IMI-103325/GCA_033091055.1, Shigella sonnei PNUSAE103325/GCA_023697305.1, Salmonella enterica PNUSAS103325/GCA_016239935.1 and Listeria monocytogenes FLAG-103325/GCA_050885205.1. Unrelated assembly statistics and an ATB Campylobacter-labelled SeqKit-checksum substring in sample SAMN11975793 do not establish identity. GOLD object identifiers were not counted as assemblies.

No gene, resistance, pathway, expression-module or causal assertion is present in the target. iModulonDB is not applicable, not negative evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed record and source scope.

## Recommended Edits

None required for this target. Preserve its exact clone identity and unresolved NCBI lineage. Future enrichment should represent AB031628.1 only as directly sourced marker evidence, without converting source naming into a measured staining phenotype or transferring culture, genome or type-material claims through numeric collisions.

## Follow-up Checks

After an authorized maintained-input change, run `just seed-canary NCBITaxon:103325 --force`, inspect the output and repeat both focused validators. No canary ran here. Reconfirm exact sequence qualifiers before enrichment and run corpus-wide gates before broader release.

## Additional Notes

The web tool could not retrieve the taxonomy browser page; direct public NCBI EFetch, Datasets, ESearch and nucleotide EFetch succeeded. Reference metadata was inspected without claiming access to unpublished results. The unrelated Leuconostoc classification conflict is outside this record's scope; any later resolution belongs to its maintained source/extraction inputs, not this YAML.

No YAML, source input, curation event, mapping status, separate history, generated page or GitHub item changed. Only this new report was manually written; prior reports were preserved.
