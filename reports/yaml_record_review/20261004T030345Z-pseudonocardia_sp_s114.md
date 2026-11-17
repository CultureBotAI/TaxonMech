# YAML Record Review: Pseudonocardia sp. S114

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudonocardia_sp_s114.yaml`
- Started UTC: 2026-10-04T03:02:45Z
- Finished UTC: 2026-10-04T03:03:45Z
- Verdict: pass

## Target

Read the whole generated TaxonRecord for `NCBITaxon:1032724`, Pseudonocardia sp. S114. It has SPECIES rank, BACTERIA domain, parent unclassified Pseudonocardia (2619320), ten lineage entries, EXACT grounding, SEEDED status, genetic code 11, zero BacDive strains, one NCBITAXON NAME assertion and one seed event. No phenotype, gene-function, host-interaction, causal-graph or genome-equivalence assertion is present.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pseudonocardia_sp_s114.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/pseudonocardia_sp_s114.yaml` passed for one file with zero errors and refreshed the diagnostic TSV.

Read-only structured comparisons checked all lineage entries, source inventories, attestation, path, scope and seed text. Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused substitute was used. No curator-added graph terms or separate history references require a target-specific gate.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220908` and `data/catalog/ncbi_names-0005.jsonl.gz:30214` agree with the YAML. Live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032724&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032724) confirm exact label, species rank, parent, code 11, bacterial domain and all ten root-first lineage IDs. Labels and ranks through Bacillati, Actinomycetota, Actinomycetes, Pseudonocardiales and Pseudonocardiaceae agree with the carried hierarchy.

Complete structured scans found no backbone synonyms or direct children and no own-ID type-material, merged-ID or dropped entry. EXACT identifies this NCBI placeholder, not a formally named species or every strain and sample labeled S114.

## Evidence

The NAME assertion and 2026-09-13 snapshot note match the inventory. `data/taxa/PATHS.tsv:13295` and `curation/seed_scope.tsv:321279` confirm identifier, slug and NCBI-only scope reason. The 2026-09-13T17:54:04Z seed event preserves that reason without claiming human review.

Exact-taxon Nuccore search returned one entry, inspected as GenBank XML. [JF793507.1](https://www.ncbi.nlm.nih.gov/nuccore/JF793507.1) is a 1,387-base partial 16S rRNA gene sequence with genomic DNA molecule type, strain S114 and explicit taxon 1032724. Source qualifiers identify rhizosphere, host wild rice and China: Dongxiang, Jiangxi.

The references comprise an unpublished actinomycete study by Fei and a direct submission on 2011-04-05. No PMID or DOI is supplied. This supports the source identity and bounded collection context, not a scientific host-species grounding, internal plant colonization, antimicrobial production or plant-growth promotion. No such stronger claim appears in the YAML.

Exact Assembly search returned zero with a phrase-not-found warning, a bounded result rather than proof of universal genome absence. The marker is not an assembly. Both structured taxonomy requests and GenBank XML retrieval succeeded.

## Completeness

Complete scans of BacDive, LPSN, GTDB mapping, GOLD aggregate, MediaDive, Madin and BactoTraits inventories found no exact target row. No descendant taxon or target-classified BacDive strain occurs in the checked backbone/inventory, supporting `strain_count: 0` as an upstream source count.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered the numeric identifier with digit boundaries, full label, slug and bounded S114 separator variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. There were 162 matching lines. An initially truncated GOLD-project portion was recovered through a complete structured scan of all 38 matching project rows; all matched contexts were then inspected. Recursive SOURCE.json traversal included ignored files and found no matching metadata entry.

Within those bounded surfaces, no independently supported target culture deposit, genome association, extra source mapping or separate history record was found. S114 alone is not a collection accession. Optional nomenclature, strains, phenotype and graph slots may remain empty. iModulonDB is not applicable to the taxonomy-only YAML. Unrelated community metatranscriptomes labeled S114 are not expression evidence for this strain.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found.

## Recommended Edits

None required. Preserve generated ownership, source-carried taxonomy and SEEDED status. Future authority corrections belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope belongs to `curation/seed_scope.tsv`. Require direct strain-specific functional evidence and explicit identity crosswalks before attaching culture or genome identifiers.

## Follow-up Checks

For an authorized source refresh, inspect changed evidence, regenerate one canary with `just seed-canary NCBITaxon:1032724 --force`, inspect its YAML and rerun both focused validators. Run documented corpus reproduction, provenance, history and QC gates before publishing corpus changes. No unresolved record-level blocker was found.

## Additional Notes

Clostridium butyricum S114 (1492) is BacDive 169215 and StrainInfo strain 403157, with DSM 107392 and other designations. Unrelated StrainInfo names include Vibrio alginolyticus S114-12, Corynebacterium capitovis S114/98/4 and Phytophthora cinnamomi S114. These are source strain designations, not eligible crosswalks to the target.

Vibrio parahaemolyticus S114 is taxon 1394649 with GCA_000490155.1 / GCF_000490155.1. Salmonella sp. S114-49411 is taxon 2665604 with GCA_014491565.1 / GCF_014491565.1. Other excluded taxon labels include uncultivated soil bacterium clone S114 (64345), Myxococcus sp. S114 (1227562), Flavobacterium sp. S114.08.P.BNT.WR.H.Fin.D (1278666) and Salmonella sp. Plate1-B3_S114 (3098385); the latter appears in ATB with SAMN38415563 and run SRR26954177. None establishes target identity.

Other genome matches classify S114 or S114-prefixed samples as Escherichia, Salmonella, Staphylococcus, Neisseria, Pseudomonas, Bacteroides, Erwinia, Listeria, Klebsiella, Acinetobacter, Stenotrophomonas or Shigella. Corynebacterium diphtheriae bv. gravis strain 4004 has assembly name S114, illustrating that assembly names are not strain identifiers. GTDB coordinate strings containing south latitude followed by longitude 114 are also search collisions, not aliases.

SAMEA1032724 belongs to Streptococcus pneumoniae 146066 (1313), with GCA_001117165.1/.2, GCF_001117165.1, BV-BRC 1313.5795 and ATB run ERR069774. PRJNA1032724 instead belongs to Streptomyces roseofulvus A1 (33902), GCA_036624895.1. Numeric overlap does not supply target evidence.

GOLD S114 projects include Pinus/Suillus root metatranscriptomes, human and other host-associated communities, soils, seawater and blood-plasma viral communities. Their explicitly different subjects, sample IDs and project IDs were retained. No primary source chain connects those communities to this wild-rice-associated Pseudonocardia isolate.

Only this new report was manually written for the target. No YAML, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
