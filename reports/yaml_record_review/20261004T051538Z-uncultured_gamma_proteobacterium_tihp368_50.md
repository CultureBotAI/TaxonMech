# YAML Record Review: uncultured gamma proteobacterium TIHP368-50

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_50.yaml`
- Started UTC: 2026-10-04T05:14:46Z
- Finished UTC: 2026-10-04T05:15:38Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` identifies `NCBITaxon:103308`, uncultured gamma proteobacterium TIHP368-50. It carries species rank, BACTERIA domain, parent 50423, seven root-first ancestors, code 11, EXACT grounding, SEEDED status and zero BacDive strains. NCBITAXON is its sole attestation, 1 NAME, snapshot 2026-09-13; its seed event is dated 2026-09-13T17:54:04Z.

Future corrections belong to maintained source inputs, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` and, for inclusion changes, `curation/seed_scope.tsv`. Generated YAML is read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_50.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_50.yaml`: passed, one file, zero errors; refreshed the standard strict-validation TSV.
- Structured checks matched complete backbone identity, lineage, code, attestation, scope/PATHS registration and seed text. These checks do not replace corpus reproduction.
- Not checked: full-corpus `verify-corpus`, QC/tests, global term/reference/history/provenance/product gates or rendering. No canary, regeneration or history/status mutation ran.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:18417`, name-catalog shard 0000 row 38435, PATHS row 13356 and scope row 144077 agree. Live NCBI EFetch and Datasets confirm the exact label, species rank, parent 50423, code 11 and lineage IDs 1, 131567, 2, 3379134, 1224, 1236, 50423. The parent is an environmental-samples grouping beneath Gammaproteobacteria, not a named genus. [NCBI taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103308&retmode=xml)

The full clone designation is retained without extra synonyms, a formal binomial, cultivation or type-material claims. Source species rank supports inclusion without implying nomenclatural publication.

## Evidence

Pinned and live taxonomy support the NCBITAXON NAME attestation. Exact-taxid Nuccore ESearch returned one entry, UID 5869744. Its inspected qualifiers identify AB031650.1, an 810 bp partial 16S rRNA sequence, with taxon:103308, clone TIHP368-50, environmental_sample and coastal marine sediment. This directly resolved marker is not an assembly or culture deposit. [NCBI nucleotide](https://www.ncbi.nlm.nih.gov/nuccore/AB031650.1)

Reference metadata describes an unpublished coastal-community 16S/quinone study by Urakawa, Yoshida, Nishimura and Ohwada, plus direct submission on 1999-08-25. Neither those entries nor the YAML supply a DOI/PMID. Study context is not clone-specific phenotype evidence.

Exact-taxid Assembly ESearch returned zero results with a phrase-not-found/no-items warning. This bounded query result is not universal proof of genome absence.

## Completeness

Complete exact-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row, direct backbone child, or own-ID type-material, merged-ID or dropped-ID row. Optional strains, nomenclature, mappings and functional fields are appropriately empty. Zero strain_count follows the BacDive-subtree definition.

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` covered bounded 103308, TIHP368-50/underscore spelling and the full stem across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 36 matched lines and structured contexts were inspected. SOURCE.json files were separately scanned, yielding two BacDive request matches in its own namespace. No target-specific deposit, assembly, non-NCBI attestation or separate history reference was found within these bounds.

CIP 103308 belongs to taxid 86667, BacDive 1499, strain 581, and SI-ID 1153's own deposit 148850. BacDive, StrainInfo and LPSN 788329 use Jeotgalibacillus marinus; the NCBI type-material row uses Bacillus globisporus subsp. marinus, and GOLD Go0629362 uses Bacillus globisporus. LPSN synonym entries 773719, 773766 and 777677 represent the Bacillus globisporus marinus, Bacillus marinus and Marinibacillus marinus names. These source names, their type material, publication references and AJ237708 marker remain scoped to that culture. BacDive's NRRL B-14558 and LPSN's NRRL B-14321 designations were not silently reconciled or transferred to the target.

Other excluded matches include BacDive 103308, Agromyces sp. ST027929/51513; SI-DP 103308, Bacillus subtilis ATCC 23857 in SI-ID 38268; and CP103308 in RL-GZ01/taxid 103816, GCA_024760325.1. Genome collisions include uncultured Alistipes sp. MGBC103308/GCA_948675665.1, uncultured bacterium MarMAG_103308/GCA_977601425.1, Pseudomonas aeruginosa PSA-BAB-IMI-103308/GCA_023904905.1, Shigella flexneri PNUSAE103308/GCA_024110635.1 and Salmonella enterica PNUSAS103308/GCA_008791625.1. Assembly-statistic matches and a Salmonella ATB SeqKit-checksum substring are unrelated. Source-specific names and accession versions were preserved.

No gene, resistance, pathway, expression-module or causal assertion is present. iModulonDB is not applicable, not negative evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed record and source scope.

## Recommended Edits

None required. Future enrichment should preserve exact environmental-clone identity and represent AB031650.1 only as directly sourced marker evidence. Do not infer neighboring accessions or transfer culture, genome, nomenclature or phenotype claims through numeric coincidences.

## Follow-up Checks

After an authorized maintained-input change, run `just seed-canary NCBITaxon:103308 --force`, inspect the output and repeat both focused validators. No canary ran here. Reconfirm exact sequence source qualifiers before enrichment; run corpus-wide gates before broader release.

## Additional Notes

The web tool could not retrieve the taxonomy browser page; direct public NCBI EFetch, Datasets, ESearch and nucleotide EFetch succeeded. Reference metadata was inspected without claiming access to unpublished results. The unrelated culture's names and designation differences are excluded context, not findings against this clone.

No YAML, source input, curation event, mapping status, separate history, generated page or GitHub item changed. Only this new report was manually written; earlier reports were preserved.
