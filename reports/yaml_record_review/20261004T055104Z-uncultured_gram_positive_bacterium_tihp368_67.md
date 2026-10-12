# YAML Record Review: uncultured Gram-positive bacterium TIHP368-67

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_gram_positive_bacterium_tihp368_67.yaml`
- Started UTC: 2026-10-04T05:50:16Z
- Finished UTC: 2026-10-04T05:51:04Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` identifies `NCBITaxon:103324`, uncultured Gram-positive bacterium TIHP368-67: species rank, BACTERIA, parent 51666, six root-first ancestors, code 11, EXACT grounding, SEEDED status and zero BacDive strains. Its sole attestation is NCBITAXON, 1 NAME, snapshot 2026-09-13; its seed event is dated 2026-09-13T17:54:04Z.

Future corrections belong to maintained source inputs, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` and, for inclusion changes, `curation/seed_scope.tsv`. Generated YAML is read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_gram_positive_bacterium_tihp368_67.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/uncultured_gram_positive_bacterium_tihp368_67.yaml`: passed, one file, zero errors; refreshed the standard strict-validation TSV.
- Structured checks matched complete backbone identity, lineage, code, attestation, PATHS/scope registration and seed text. These checks do not replace corpus reproduction.
- Not checked: full-corpus `verify-corpus`, QC/tests, global term/reference/history/provenance/product gates or rendering. No canary, regeneration or history/status promotion ran.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:18433`, name-catalog shard 0000 row 38451, PATHS row 13375 and scope row 144093 agree. Live NCBI EFetch and Datasets confirm exact label, species rank, parent 51666, code 11 and the complete lineage: 1/root, 131567/cellular organisms, 2/Bacteria, 2323/Bacteria incertae sedis, 31986/Gram-positive bacteria incertae sedis and 51666/environmental samples. Both incertae sedis entries are unranked. [NCBI taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103324&retmode=xml)

The unresolved source placement is preserved without inferring a kingdom or phylum. Gram-positive is part of the source name and grouping, not an independently inspected staining assay. No formal binomial, synonyms, cultivation or type-material status is invented. NCBI species rank does not imply nomenclatural publication.

## Evidence

Pinned and live taxonomy support the sole NCBITAXON NAME attestation. Exact-taxid Nuccore ESearch returned one record, UID 5869751. Directly resolved AB031657.1 is a 727 bp partial 16S rRNA sequence whose source qualifiers identify taxon:103324, clone TIHP368-67, environmental_sample and coastal marine sediment. It is a marker, not an assembly or culture deposit. [NCBI nucleotide](https://www.ncbi.nlm.nih.gov/nuccore/AB031657.1)

Reference metadata describes an unpublished coastal-community 16S/quinone study by Urakawa, Yoshida, Nishimura and Ohwada, plus direct submission on 1999-08-25. Neither these entries nor the YAML supply a DOI/PMID. Study context does not establish clone-specific phenotype claims or resolve its lineage further.

Exact-taxid Assembly ESearch returned zero results with a phrase-not-found/no-items warning. This bounded result is not universal proof of genome absence.

## Completeness

Complete exact-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row, direct backbone child, or own-ID type-material, merged-ID or dropped-ID row. Optional strains, nomenclature, mappings and functional fields are appropriately empty. Zero strain_count follows the BacDive-subtree definition.

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searched bounded 103324, TIHP368-67/underscore spelling and the full stem across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 38 matched lines and their structured contexts were inspected. Separate SOURCE.json scans yielded two BacDive request matches in its own namespace. No target-specific deposit, assembly, non-NCBI attestation or separate history reference was found within these bounds.

CIP 103324 denotes Yersinia mollaretii, BacDive 5225, species taxid 33060 and strain taxid 349967, with LPSN 785225 and GOLD Go0630215. NCBI type-material and native BacDive support that culture's type status, while the extracted BacDive inventory has flag 0. SI-ID 42157 owns SI-DP 147821, with species taxid 33060 on strain and own deposit. This unrelated discrepancy and the species/strain scopes were preserved, not resolved or transferred to the target. LPSN KJ606911 and publication metadata are excluded culture evidence.

SI-DP 103324 instead denotes Planomonospora parontospora subsp. antibiotica ATCC 23864, SI-ID 38273/BacDive 16578, taxid 97193 on strain and own deposit. BacDive 103324 itself is Agromyces sp. ST018441/51513. KY103324 occurs in Derxomyces anomalus SI-ID 180677. The full native BV-BRC row 1590.4194 identifies CP103324 as part of Lactiplantibacillus plantarum Ep-M17/GCA_032818175.1, not this clone.

Other excluded genome collisions include uncultured Muribaculaceae bacterium MGBC103324/GCA_948646335.1, uncultured bacterium MarMAG_103324/GCA_977587595.1, Pseudomonas aeruginosa PSA-BAB-IMI-103324/GCA_033091095.1, Shigella sonnei PNUSAE103324/GCA_023696705.1, Salmonella enterica PNUSAS103324/GCA_008815715.1 and E. coli strain 103324/GCA_049979445.1. Saccharimonadales bacterium (SeqCode) GCA_964965255.1 has assembly name PELAGICS-MAG-m2-bin103324-CADAX-SM-03sep20 and an isolate string with an additional trailing period. Unrelated assembly statistics and an ATB Staphylococcus saprophyticus checksum substring in sample SAMN32942784 do not establish identity. GOLD object identifiers were not counted as assemblies.

No gene, resistance, pathway, expression-module or causal assertion is present in the target. iModulonDB is not applicable, not negative evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed record and source scope.

## Recommended Edits

None required for this target. Preserve its exact clone identity and unresolved NCBI lineage. Future enrichment should represent AB031657.1 only as directly sourced marker evidence, without converting the name into a measured staining phenotype or transferring culture, genome or type-material claims through numeric collisions.

## Follow-up Checks

After an authorized maintained-input change, run `just seed-canary NCBITaxon:103324 --force`, inspect the output and repeat both focused validators. No canary ran here. Reconfirm exact sequence qualifiers before enrichment and run corpus-wide gates before broader release.

## Additional Notes

The web tool could not retrieve the taxonomy browser page; direct public NCBI EFetch, Datasets, ESearch and nucleotide EFetch succeeded. Reference metadata was inspected without claiming access to unpublished results. The unrelated Yersinia culture's flag discrepancy is outside this record's scope; any correction belongs to its maintained source/extraction inputs, not this YAML.

No YAML, source input, curation event, mapping status, separate history, generated page or GitHub item changed. Only this new report was manually written; prior reports were preserved.
