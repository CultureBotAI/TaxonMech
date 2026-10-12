# YAML Record Review: uncultured Treponema clone RsDiSp8

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_treponema_clone_rsdisp8.yaml`
- Started UTC: 2026-10-07T20:40:19Z
- Finished UTC: 2026-10-07T20:46:45Z
- Verdict: pass

## Target

Generated `TaxonRecord` for `NCBITaxon:103614`, uncultured Treponema clone RsDiSp8, rank `SPECIES`, domain `BACTERIA`. The entire YAML was read independently. It contains ten ancestors, code 11, exact grounding, seeded mapping status, one NCBI name attestation and `strain_count: 0`. No synonyms, nomenclature, mappings, strains, evidence objects, graph, discussion or dataset are asserted.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/uncultured_treponema_clone_rsdisp8.yaml`: exit 0, no issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/uncultured_treponema_clone_rsdisp8.yaml --out /private/tmp/rs8-strict.tsv`: exit 0, one file, zero errors. The diagnostic TSV contains only its header.
- Structured comparisons checked every backbone field, ten ancestors, attestation, path and scope reason. No pinned descendants or exact type-material, merged-ID or dropped-ID rows were found.
- Not checked: full-corpus `verify-corpus`, `provenance-check`, `qc`, `validate-all`, tests, render/docs and vendored gates. Bounded comparisons do not reproduce the corpus. There is no target graph; the stated search found no standalone history record, so specialized graph/history checks had no target.

## Identity and Grounding

Live Taxonomy EFetch confirms identifier, exact label, species rank, code 11 and parent `NCBITaxon:77353`, environmental samples. Its administrative division is Environmental samples; its lineage places it in Bacteria. Datasets confirms all ten ancestor IDs including root. The pinned labels and ranks agree: root, cellular organisms, Bacteria, Pseudomonadati, Spirochaetota, Spirochaetia, Treponematales, Treponemataceae, Treponema and environmental samples. [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=103614), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103614).

This is a sequence-linked environmental clone, not a culture-collection deposit. Exact grounding concerns the NCBI node; NCBI species rank does not establish formal nomenclatural standing. RsDiSp8 is distinct from similarly named termite clones and from unrelated identifiers containing 103614.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:18516` matches every backbone field, empty synonym fields, sole NCBI source and the 2026-09-13 snapshot. The complete native name object is `data/catalog/ncbi_names-0000.jsonl.gz:38524`.
- `data/taxa/PATHS.tsv:14771` uniquely links the identifier and slug. `curation/seed_scope.tsv:144162` supplies the one-source inclusion reason and 2026-09-13 date.
- Exact-taxonomy Nucleotide search returned one record, [AB032006.1](https://www.ncbi.nlm.nih.gov/nuccore/AB032006.1), a 1,458-base partial 16S rRNA sequence. Complete non-sequence metadata explicitly link clone RsDiSp8, taxon 103614 and host Reticulitermes speratus, and mark an environmental sample. The source note repeats the clone name. Direct submission was 29 August 1999 by Iida, Ohkuma and Kudo at RIKEN. The inspected metadata contain no culture deposit, BioSample, BioProject, protein or assembly accession. This marker is not a genome.
- The marker cites Iida and colleagues, FEMS Microbiology Ecology 34(1):17-26 (2000). Fresh PubMed metadata verify PMID 11053732 and DOI 10.1111/j.1574-6941.2000.tb00750.x. [PubMed record](https://pubmed.ncbi.nlm.nih.gov/11053732/).
- The inspected original article places RsDiSp8 among cluster-I sequences amplified from micromanipulated Dinenympha porteri fractions from R. speratus. Its comparison with Rs21 reports 96% similarity, not clone equivalence. Its cluster-II hybridization results and metabolic hypotheses do not establish RsDiSp8-specific localization or function. [Author-uploaded primary article](https://www.researchgate.net/publication/12272419_Symbiotic_spirochetes_in_the_termite_hindgut_phylogenetic_identification_of_ectosymbiotic_spirochetes_of_oxymonad_protists).
- A later study explicitly discusses RsDiSp8 as the cluster-I phylotype from D. porteri associated with restricted surface localization. Its relevant experiment uses the cluster-I consensus probe TTI-732; the phylotype-specific probes concern NkS-Dev1, NkS-Dev14, NkS-Oxy8 and NkS-Oxy26, not RsDiSp8. Thus the authors' interpretation is relevant context, but is not an RsDiSp8-specific probe result. Methods, results, discussion and figure captions were inspected; fresh PubMed metadata confirm PMID 12514050 and DOI 10.1128/AEM.69.1.625-633.2003. [Noda and colleagues, 2003](https://journals.asm.org/doi/10.1128/aem.69.1.625-633.2003), [PubMed record](https://pubmed.ncbi.nlm.nih.gov/12514050/).
- Exact-taxonomy Assembly search returned zero with phrase-not-found/no-items warnings. This bounded query does not establish genome absence under all identifiers.
- The seed event and sole `NAME` attestation agree with the inventory and scope row. Its `2026-09-13T17:54:04Z` timestamp is the latest extraction time among raw, ATB and StrainInfo manifests, as used by `src/taxonmech/seed.py:139`. It records seeding, not human review.

## Completeness

Exact BacDive comparison found no target row; the pinned backbone has no descendants. These support the source-specific zero strain count, not a general cultivation assessment. Exact LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventory comparisons also returned no target rows. Empty optional slots are appropriate for this seeded record.

The gitignore-independent search used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. It covered digit-bounded 103614, RsDiSp8 label/slug variants, AB032006, PMID 11053732 and its DOI. All 34 candidate rows were inspected completely: 16 catalog/BV-BRC objects, five BacDive/GOLD/StrainInfo objects and 13 TSV rows. Five SOURCE.json files were parsed separately and history filenames checked independently.

Three candidates describe this target: backbone, native name and scope. The other 31 are unrelated identifier, designation or numeric collisions. No supported target culture/genome link, curation overlay or standalone history record was found within those bounded roots. The later paper was inspected independently; its citation identifiers were not included in this local candidate count.

The sequence and two inspected publications offer optional context, not a missing required field. There is no gene-function, regulator, transcriptomic or dataset claim in this YAML; iModulonDB is not applicable. No required representation was demonstrated missing.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, attestation, inventory-specific strain count and seeded provenance are supported. The record does not overstate the ecological or functional evidence discussed in the literature.

## Recommended Edits

None required. Preserve the generated YAML and seed event. Any optional enrichment belongs in maintained source/extractor inputs or an appropriate durable curator representation, not a hand-edited generated artifact. Preserve exact accession-to-taxon identity and distinguish the later authors' RsDiSp8 interpretation from direct clone-specific hybridization. No culture or genome should be attached through bare numeric matching.

## Follow-up Checks

Before adding a clone-specific localization or function claim, require evidence at that scope and retain the experimental probe specificity. Before adding a genome or deposit, require an explicit source link to taxon 103614 or AB032006.1. After any future maintained-input change, regenerate through the documented pipeline and run focused schema/strict checks plus corpus/provenance gates.

## Additional Notes

- HEAD was `b6a6508faca1388b88feb5740b1095e9f64cfdb8`; the YAML was byte-identical before report creation. Existing branches and worktrees were preserved.
- BacDive ID 103614 denotes Rhodococcus sp. ST031461, taxon 194249. The matching SOURCE.json request is in the BacDive-ID namespace, not NCBI Taxonomy.
- CIP 103614/VPI 6325/7G5 belongs to BacDive 135303, StrainInfo 69022 with deposit 152085, and GOLD Go0238864, all in Lactobacillus gasseri context. Complete native and related objects were inspected; this deposit is not RsDiSp8.
- CP103614 belongs to Klebsiella pneumoniae 3571, GCA_024917495.1, GOLD Ga0608790 and BV-BRC 573.50466/573.50838. MGBC103614 is Parabacteroides distasonis in GCA_948851355.1 and BV-BRC 823.4804. Neither provides a target link.
- Other collisions include Salmonella strains OSF103614 and PNUSAS103614, Crocinitomicaceae PELAGICS-MAG-m2-bin103614-CEPXH-LM-31jul20, MarMAG_103614, Pseudomonas aeruginosa assembly name ASM103614v1, GTDB scaffold statistics, E. coli run DRR103614 and a Pseudomonas assembly checksum. Mycobacterium tuberculosis BioSample SAMN11053732 repeats the original PMID's digits but is not a publication link.
- The original article was inspected through the author's public full text; publisher access and its figure image were unavailable in the preceding source inspection. Its textual RsDiSp8 placement is explicit. The later paper's PMC page presented a browser challenge; the public ASM publisher text was accessible. No challenge or access restriction was bypassed, and no visual measurement was inferred from captions.
- No sequence alignment, exhaustive literature review, current deposit-availability assessment or taxonomic reassignment was performed. Search leads about similar clones were not promoted to identity assertions.
- Only this new report was written for this target. No YAML, source inventory, history/lifecycle or GitHub state changed.
