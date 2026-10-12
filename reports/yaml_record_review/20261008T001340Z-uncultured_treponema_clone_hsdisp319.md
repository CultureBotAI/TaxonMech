# YAML Record Review: uncultured Treponema clone HsDiSp319

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_treponema_clone_hsdisp319.yaml`
- Started UTC: 2026-10-08T00:07:06Z
- Finished UTC: 2026-10-08T00:13:40Z
- Verdict: pass

## Target

Generated `TaxonRecord` for `NCBITaxon:103617`, uncultured Treponema clone HsDiSp319, rank `SPECIES`, domain `BACTERIA`. The entire YAML was read independently. It carries ten ancestors, genetic code 11, exact grounding, seeded status, one NCBI name attestation and `strain_count: 0`. It asserts no synonyms, nomenclature, taxonomy mappings, listed strains, evidence objects, graph, discussion or dataset.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/uncultured_treponema_clone_hsdisp319.yaml`: exit 0, no issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/uncultured_treponema_clone_hsdisp319.yaml --out /private/tmp/ht319-strict.tsv`: exit 0, one file, zero errors. Diagnostic TSV read, header-only.
- Structured comparisons passed for backbone identity, all ten ancestors, attestation, path and seed-scope history. Exact pinned type-material, merged-ID and dropped-ID checks found no target rows. The backbone has no target children.
- Not checked: full-corpus `verify-corpus`, `provenance-check`, `qc`, `validate-all`, tests, render/docs, product and vendored gates. Bounded source checks do not reproduce the corpus. No graph is asserted and the ignored-inclusive bounded search found no standalone target history record, so specialized graph/history validation had no target.

## Identity and Grounding

Live Taxonomy EFetch agrees with the ID, clone name, species rank, genetic code 11 and parent `NCBITaxon:77353`, environmental samples. Datasets agrees with all ten ancestor IDs including root. Labels and ranks agree through cellular organisms, Bacteria, Pseudomonadati, Spirochaetota, Spirochaetia, Treponematales, Treponemataceae, Treponema and the environmental-samples parent. NCBI's environmental-sample division is compatible with the bacterial lineage; it is not a different organismal domain. [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=103617), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103617).

Exact grounding identifies this NCBI node. The species rank does not establish a formally named or cultured species. HsDiSp319 is a molecular clone designation, not a culture-collection deposit. BacDive 103617, CIP 103617 and DSM 103617 belong to different namespaces and organisms; matching their numerical components is not an identity match.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:18519` matches identity, rank, parent, genetic code, empty synonyms, sole source and snapshot date 2026-09-13. The complete scientific-name object at `data/catalog/ncbi_names-0000.jsonl.gz:38527` agrees.
- `data/taxa/PATHS.tsv:14800` uniquely maps the ID and slug. `curation/seed_scope.tsv:144165` agrees with the seed date and one-source inclusion reason.
- Exact-taxonomy Nucleotide search returned [AB032009.1](https://www.ncbi.nlm.nih.gov/nuccore/AB032009.1), a 1,504-base partial 16S rRNA sequence explicitly assigned to taxon 103617 and clone HsDiSp319. Complete non-sequence GenBank metadata were read. The host qualifier names Hodotermopsis sjoestedti, and the note describes amplification from an isolated protist of that termite. Environmental-sample status is explicit. The direct submission is dated 29 August 1999 from RIKEN, Japan; creation is 29 February 2000 and update 16 December 2008. No culture deposit, BioSample, BioProject, assembly or protein accession appears in those metadata. The marker is not a genome.
- GenBank explicitly cites PMID 11053732. Public PubMed EFetch confirmed the citation, full abstract and DOI `10.1111/j.1574-6941.2000.tb00750.x`. The primary paper's author-uploaded text was inspected for methods, accession reporting, the exact clone passage and Discussion. It lists AB031997-AB032009 and places HsDiSp319 in the minor cluster-I group recovered from the Dinenympha sp. fraction, distinct from the HsDiSp320 group. Crucially, its Discussion says cluster-I cells were not identified in situ as attached versus unattached; entanglement among attached cells was not excluded. This supports sequence recovery and phylogenetic context, not a demonstrated clone-specific attachment mechanism. Acetogenesis of other cultured strains and proposed symbiotic functions are not evidence of HsDiSp319 physiology. [PubMed](https://pubmed.ncbi.nlm.nih.gov/11053732/), [Inspected primary author copy](https://www.researchgate.net/publication/12272419_Symbiotic_spirochetes_in_the_termite_hindgut_phylogenetic_identification_of_ectosymbiotic_spirochetes_of_oxymonad_protists).
- Exact-taxonomy Assembly search returned zero with phrase-not-found/no-items warnings. This is a bounded query result, not proof that no genome exists under any other identifier.
- The attestation counts one NCBI `NAME`, not a cultured strain or sequence count. Seed timestamp `2026-09-13T17:54:04Z` agrees with the latest extracted-at value among raw, ATB and StrainInfo manifests, selected by `src/taxonmech/seed.py:139`; those unchanged inputs and implementation were inspected during this review sequence.

## Completeness

Exact BacDive comparison and lack of classified descendants support the inventory-specific zero strain count. It does not establish permanent uncultivability. Exact LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits comparisons found no target rows. Optional slots are appropriately empty for the identity claims made here.

Resolution searched ignored files in `data/taxa`, `reports`, `curation` and `history`. Source discovery used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Terms included digit-bounded 103617, the clone label/slug and AB032009. All 45 candidate addresses were retained; all 25 JSON objects and 20 TSV rows were read completely. Five SOURCE.json files were separately parsed and history filenames independently checked. BacDive metadata hits concern its own request ID 103617, not this NCBI node.

Three candidates support this target's native name, backbone and scope; the other 42 do not establish target identity. No supported additional target culture/genome link, curation overlay or standalone history record was found within these bounded roots, including ignored files. No required representation was demonstrated missing. iModulonDB is not applicable: this YAML has no gene, regulator, functional, transcriptomic or dataset claim.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found against the current YAML. Its identity, lineage, count and seeded provenance are supported. The source paper's limits on physical association and function are preserved; the YAML does not assert a mechanism, phenotype, confirmed ectosymbiotic attachment or a cultured isolate that would exceed those limits.

## Recommended Edits

None required. Preserve the generated YAML and seed event. Source taxonomy corrections belong upstream at NCBI; demonstrated harmonization defects belong in `src/taxonmech/seed.py` with a test. Extraction changes belong in maintained source/extractor inputs, including `scripts/extract_source_inventory.py`; scope corrections belong in `curation/seed_scope.tsv`. None is justified here. Durable curator overlays need the implementation described in `docs/CURATION.md`, not hand edits to generated records. Optional phenotype and host-association enrichment belongs to the relevant sibling repository.

## Follow-up Checks

Before optional biological enrichment, distinguish the clone from HsDiSp320 and retain the separation between fraction-derived sequence evidence and direct cellular localization. Inspect primary localization evidence for any proposed attachment claim; do not transfer phenotypes from related cultures. Every proposed deposit or genome link requires its own explicit source chain. No alignment, reclassification or inference of equivalence was performed. Future maintained-input changes require regeneration and focused schema/strict plus corpus/provenance gates.

## Additional Notes

- HEAD remained `b6a6508faca1388b88feb5740b1095e9f64cfdb8`; the target was byte-identical before report creation. Existing branches and worktrees were preserved.
- BacDive 103617 is Rhodococcus material assigned to taxon 194249. DSM 103617 is Methylophaga muralis BUR1, taxon 291169, BacDive 132896, StrainInfo 401268/deposit 908189, GOLD Go0620681. CIP 103617 is Lactobacillus gasseri, taxon 1596, BacDive 138807, StrainInfo 69025/deposit 152088, GOLD Go0238867. Their source links remain attached to those organisms.
- Further collection/sequence collisions include IMI 103617, Absidia spinosa, and KY103617 associated with the Monosporozyma/Kazachstania aerobia source record. These source objects were read only to exclude incorrect joins; their taxon records were not reviewed or changed.
- Genome-catalog collisions include a Xanthomonas assembly's N50 value; Muribaculum MGBC103617, GCA/GCF_948840205.1; Salmonella OSF103617, strain 103617 and PNUSAS103617; Enterobacter entries; and Klebsiella pneumoniae 3571 with CP103617 in GCA_024917495.1. The GOLD NPDC103617_432_A07 project/analysis has no target organism identity chain. None supplies a Treponema clone link.
- Three ATB rows concern E. coli or Salmonella; matches are DRR103617 or characters within SeqKit sums. They are not NCBI-taxonomy matches. Historical statuses and alternative classifications in collision records were not transferred to the target.
- Publisher HTML access failed with HTTP 403; no restriction was bypassed. PubMed EFetch and the publicly available primary author text supplied the evidence used. Figure images were not inspected, and no finding relies on a visual interpretation of them or on a search snippet. Other search hits remain discovery leads, not demonstrated culture or genome identities.
- No culture-availability assessment, paid research, outreach or GitHub action was performed. Only this new report was written for this review; YAML, inventories and history/lifecycle state were unchanged. Eukaryota remained untouched.
