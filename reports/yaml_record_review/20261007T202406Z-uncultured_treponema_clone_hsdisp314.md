# YAML Record Review: uncultured Treponema clone HsDiSp314

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_treponema_clone_hsdisp314.yaml`
- Started UTC: 2026-10-07T20:12:19Z
- Finished UTC: 2026-10-07T20:24:06Z
- Verdict: pass

## Target

Generated `TaxonRecord` for `NCBITaxon:103613`, uncultured Treponema clone HsDiSp314, rank `SPECIES`, domain `BACTERIA`. The entire YAML was read independently. It has ten ancestors, code 11, exact grounding, seeded mapping status, one NCBI name attestation and `strain_count: 0`. No synonyms, nomenclature, mappings, strains, evidence objects, graph or discussion are asserted.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/uncultured_treponema_clone_hsdisp314.yaml`: exit 0, no issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/uncultured_treponema_clone_hsdisp314.yaml --out /private/tmp/hs314-strict.tsv`: exit 0, one file, zero errors. The diagnostic TSV contains only its header.
- Structured comparisons checked every backbone field, ten ancestors, attestation, unique path and scope reason. No pinned descendants or exact type-material, merged-ID or dropped-ID rows were found.
- Not checked: full-corpus `verify-corpus`, `provenance-check`, `qc`, `validate-all`, tests, render/docs and vendored gates. Bounded comparisons do not reproduce the corpus. There is no target graph; no standalone history record was found in the stated search, so specialized graph/history checks had no target.

## Identity and Grounding

Live Taxonomy EFetch agrees on identifier, label, species rank, code 11 and parent `NCBITaxon:77353`, environmental samples. Its administrative division is Environmental samples, while its lineage places it in Bacteria. Datasets confirms all ten ancestor IDs, including root. Names and ranks match the pinned chain: root, cellular organisms, Bacteria, Pseudomonadati, Spirochaetota, Spirochaetia, Treponematales, Treponemataceae, Treponema and environmental samples. [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=103613), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103613).

The clone designation denotes an environmental sequence-linked taxon, not a culture-collection deposit. NCBI species rank does not establish a validly published species name. Exact grounding is to the NCBI node, not a claim of formal nomenclatural standing.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:18515` matches all backbone fields, empty synonym fields, sole NCBI source and the 2026-09-13 snapshot. The complete native scientific-name object is `data/catalog/ncbi_names-0000.jsonl.gz:38523`.
- `data/taxa/PATHS.tsv:14769` uniquely maps the ID and slug; `curation/seed_scope.tsv:144161` supplies the one-source inclusion reason and 2026-09-13 date.
- Exact-taxonomy Nucleotide search returned one record, [AB032005.1](https://www.ncbi.nlm.nih.gov/nuccore/AB032005.1), a 1,509-base partial 16S rRNA sequence. Complete non-sequence metadata explicitly link HsDiSp314 and taxon 103613, mark an environmental sample, identify host Hodotermopsis sjoestedti, and describe a PCR clone from an isolated termite protist. Direct submission was 29 August 1999 by Iida, Ohkuma and Kudo at RIKEN. No culture, BioSample, BioProject, protein or assembly accession appears in the inspected metadata. The marker is not a genome.
- The sequence cites Iida and colleagues, FEMS Microbiology Ecology 34(1):17-26 (2000). Fresh PubMed metadata verify PMID 11053732 and DOI 10.1111/j.1574-6941.2000.tb00750.x. [PubMed record](https://pubmed.ncbi.nlm.nih.gov/11053732/).
- The author's public full text describes PCR from micromanipulated, washed protist fractions and accession range AB031997-AB032009. Cluster-II consensus FISH supports group-level localization; clone-specific probes concern RsDiSp1/RsDiSp3, not HsDiSp314. The discussion treats metabolic functions as hypotheses and cites separate cultivated ZAS strains. These results cannot establish HsDiSp314-specific metabolism or cultivation. The YAML makes no such claims. [Author-uploaded primary article](https://www.researchgate.net/publication/12272419_Symbiotic_spirochetes_in_the_termite_hindgut_phylogenetic_identification_of_ectosymbiotic_spirochetes_of_oxymonad_protists).
- Exact-taxonomy Assembly search returned zero with phrase-not-found/no-items warnings; this bounded result does not prove genome absence under every identifier.
- The seed event matches the inventory and scope reason. Its `2026-09-13T17:54:04Z` timestamp is the latest extraction timestamp among raw, ATB and StrainInfo manifests, as used by `src/taxonmech/seed.py:139`. It records seeding, not human review.

## Completeness

Exact BacDive comparison found no target row and the pinned backbone has no descendants, supporting the inventory-specific zero strain count. Exact LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits comparisons likewise returned no target rows. Optional empty slots are appropriate; the strain count itself is not a cultivation assessment.

The gitignore-independent search used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. It covered digit-bounded 103613, HsDiSp314 label/slug variants, AB032005, PMID 11053732, the verified DOI and article PII. All 46 candidate rows were inspected completely: 16 catalog/BV-BRC objects, 13 BacDive/GOLD/StrainInfo objects and 17 TSV rows. Five SOURCE.json files were parsed separately; history filenames were checked independently.

Only three candidate rows describe the target: backbone, native name and scope. The remaining 43 contain unrelated numeric identifiers or designations, detailed below. No supported additional target culture/genome link, curation overlay or standalone history record was found within those roots. No required representation was demonstrated missing.

The defining citation and sequence are verified. The inspected article text supports context, but its figure image could not be retrieved; no exact HsDiSp314 branch/subcluster assignment was inferred from the label alone. No gene-function, regulator, transcriptomic or dataset claim appears in the YAML; iModulonDB is not applicable.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The complete lineage, identity, attestation, source-specific strain count and seeded provenance are supported. Numeric collisions do not establish additional target evidence.

## Recommended Edits

None required. Preserve the generated YAML and seed event. Any optional sequence or ecological-context enrichment belongs in maintained source/extractor inputs or an appropriate durable curator representation, retaining the exact accession-to-taxon link and evidence scope. Do not add a culture deposit from an unrelated numeric match.

## Follow-up Checks

Before adding a clone-specific localization or function claim, inspect the original figure and relevant experimental evidence and distinguish direct clone evidence from group-level hybridization. Before adding a genome or deposit, require an explicit source link to taxon 103613 or AB032005.1. For any future maintained-input change, regenerate through the documented pipeline, then run record schema/strict and corpus/provenance gates.

## Additional Notes

- HEAD was `b6a6508faca1388b88feb5740b1095e9f64cfdb8`; the YAML was byte-identical before report creation. Existing branches and worktrees were preserved.
- BacDive ID 103613 denotes Rhodococcus sp. ST031455 (taxon 194249), not this NCBI taxon. The matching BacDive SOURCE.json request is in the BacDive-ID namespace.
- DSM 103613/Chol1 belongs to BacDive 131912 and StrainInfo 407521 (deposit 914902), with Pseudomonas/Stutzerimonas stutzeri context. CIP 103613/VPI 6099B belongs to BacDive 135312 and StrainInfo 69021 (deposit 152084), with Lactobacillus gasseri context. Full objects, including taxonless linked rows, were inspected; neither deposit denotes HsDiSp314.
- Other collisions include Itersonilia/Udeniomyces pannonica sequence KY103613; Enterobacter cloacae 3143 plasmid CP103613 within GCA_024917615.1; Escherichia coli strain 103613/GCA_003983455.1; Salmonella strain 103613/GCA_003895435.1, PNUSAS103613 and OSF103613; Muribaculaceae MGBC103613/GCA_948883525.1; and MarMAG_103613/GCA_977543695.1.
- Additional matches were a GTDB scaffold statistic, GOLD community sample NPDC103613_431_D03, E. coli run DRR103613, and Mycobacterium tuberculosis BioSample SAMN11053732. The latter repeats PMID digits but is not a publication link.
- OUP and ScienceDirect publisher retrievals failed; the author-uploaded article's methods, results, tables and discussion were inspected as public HTML. Its figure link returned 404 and the corresponding public image request returned 403. No restricted access was bypassed. Figure placement is not a basis of this verdict.
- No sequence alignment, exhaustive literature review, current deposit-availability check or taxonomic reassignment was performed.
- Only this new report was written for the target. No YAML, source inventory, history/lifecycle or GitHub state changed.
