# YAML Record Review: uncultured gamma proteobacterium TIHP368-08

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_08.yaml`
- Started UTC: 2026-10-04T04:48:55Z
- Finished UTC: 2026-10-04T04:49:38Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` identifies `NCBITaxon:103296`, uncultured gamma proteobacterium TIHP368-08. It has rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:50423`, seven root-first ancestors, code 11, `EXACT` grounding, `SEEDED` status and zero BacDive strains. Its sole attestation is NCBITAXON, 1 NAME, snapshot 2026-09-13; its seed event is dated 2026-09-13T17:54:04Z.

Future corrections belong to maintained upstream transforms, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` and, if inclusion changes, `curation/seed_scope.tsv`. Generated YAML is read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_08.yaml`: passed, no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/uncultured_gamma_proteobacterium_tihp368_08.yaml`: passed, one file and zero errors; refreshed the standard strict-validation TSV.
- Structured comparisons matched complete backbone identity/lineage/code, source attestation, scope/PATHS registration and seed text. Evidence audits do not replace corpus reproduction.
- Not checked: full-corpus `verify-corpus`, QC/tests, global term/reference/history/provenance/product gates or rendering. No canary, regeneration or history/status mutation ran.

## Identity and Grounding

Backbone row `data/raw/ncbitaxon_taxa.tsv:18405`, name-catalog shard 0000 row 38423, PATHS row 13342 and scope row 144065 agree on this exact target. Live NCBI EFetch and Datasets confirm the preferred label, species rank, parent 50423, code 11 and lineage IDs 1, 131567, 2, 3379134, 1224, 1236, 50423. The final ancestor is the environmental-samples grouping beneath Gammaproteobacteria, not a named genus. [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103296&retmode=xml)

The source species rank supports inclusion without claiming valid nomenclatural publication, cultivation or type-strain status. The complete clone designation is preserved; it is not interchangeable with another TIHP368 suffix. No extra synonym or formal binomial is asserted.

## Evidence

The pinned backbone/name row and live taxonomy support the NCBITAXON NAME attestation. Exact-taxid Nuccore ESearch returned one entry, UID 5869724; its source qualifiers and reference metadata were inspected. AB031630.1 is a 760 bp partial 16S rRNA sequence with explicit taxon:103296, clone TIHP368-08, environmental_sample and coastal-marine-sediment qualifiers. It is a marker, not an assembly or deposit. Its accession was resolved directly, not inferred from adjacent records. [NCBI nucleotide](https://www.ncbi.nlm.nih.gov/nuccore/AB031630.1)

Reference metadata names Urakawa, Yoshida, Nishimura and Ohwada for an unpublished coastal-community study using 16S and quinone profiling, plus a separate direct submission dated 1999-08-25. These entries supply no DOI/PMID, and the YAML cites no publication. The study context does not prove clone-specific phenotype assertions.

Exact-taxid Assembly ESearch returned zero results with a phrase-not-found/no-items warning. This bounded result agrees with the inspected marker-only context, not a universal genome-absence claim.

## Completeness

Complete exact-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row, no direct backbone child, and no own-ID type-material, merged-ID or dropped-ID row. Empty optional strains, nomenclature, mappings and functional fields are appropriate. Zero strain_count follows the BacDive-subtree definition.

The ignored-inclusive search used `rg --no-ignore --hidden -n -z -i` for bounded 103296, TIHP368-08/underscore spelling and the complete stem across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 40 matched lines and structured contexts were inspected. SOURCE.json files were separately scanned; two BacDive request matches concern that resource's own identifier namespace. No target-specific deposit, assembly, non-NCBI attestation or separate history reference was found within these bounds.

CIP 103296 is an excluded culture collision: BacDive 11358, strain 266, also ATCC 14670/DSM 10281, with source taxids 86172 and 863372. BacDive labels it Herbaspirillum huttiense subsp. putei, while the inspected LPSN designation sets include Herbaspirillum huttiense, historical Pseudomonas huttiensis and subsp. huttiense. GOLD Go0253018 uses Herbaspirillum huttiense/863372. StrainInfo SI-ID 4110 has that species context and owns CIP deposit 154272, whose deposit taxon field is absent. These differing source classifications were preserved, not reconciled or transferred to TIHP368-08. EU024131 16S, EU024189 gyrB and EU024255 rpoB references concern that culture, not this environmental clone.

Other excluded matches include BacDive 103296, Agromyces sp. STI07704/51513; KY103296 in Debaryomyces udenii SI-ID 65170; and CP103296 in Escherichia coli 2e/GCA_024760205.1. Genome collisions include Thomasclavelia cocleata MGBC103296/GCA_948651055.1, Vibrio brasiliensis MarMAG_103296/GCA/GCF_977601525.1 and Escherichia coli PNUSAE103296/GCA_023758645.1. ATB DRR103296 belongs to Escherichia coli sample SAMD00077704; unrelated assembly-statistic and SeqKit checksum substrings do not assert this taxon identity.

No gene, resistance, pathway, expression-module or causal-graph assertion is present. iModulonDB is not applicable, not negative evidence; marker context does not require functional enrichment.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed record and source scope.

## Recommended Edits

None required. Future enrichment should preserve the exact environmental-clone identity and represent AB031630.1 only as directly sourced marker evidence. Do not infer accessions from numbering, transfer unrelated culture/genome evidence by numeric substring or infer phenotype from the study title.

## Follow-up Checks

After an authorized maintained-input change, run `just seed-canary NCBITaxon:103296 --force`, inspect the result and repeat both focused validators. No canary ran here. Reconfirm exact marker/taxon/source qualifiers before adding sequence evidence, and run corpus-wide gates before broader release.

## Additional Notes

The web tool could not retrieve the browser page; direct public NCBI EFetch, Datasets, ESearch and nucleotide EFetch succeeded. Reference metadata was inspected without claiming access to unpublished study results. Contextual discrepancies among unrelated Herbaspirillum records are not findings against this target.

No YAML, source input, curation event, mapping status, separate history, generated page or GitHub item changed. Only this new report was manually written, preserving earlier reports.
