# YAML Record Review: Rickettsiella ixodidis

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/rickettsiella_ixodidis.yaml`
- Started UTC: 2026-10-05T09:05:45Z
- Finished UTC: 2026-10-05T09:10:07Z
- Verdict: pass with minor issues

## Target

The complete 64-line `TaxonRecord` was read before judgment. It denotes `NCBITaxon:1034400`, Rickettsiella ixodidis, rank `SPECIES`, domain `BACTERIA`, with `grounding_status: EXACT` and `mapping_status: SEEDED`. This generated record represents an NCBI concept, not an independently adjudicated species boundary or genome assembly. Future seeded-field corrections belong to maintained source capture/transform inputs, `src/taxonmech/extract.py`, `src/taxonmech/seed.py`, or `curation/seed_scope.tsv`, not direct YAML edits.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/rickettsiella_ixodidis.yaml`: exit 0, no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/rickettsiella_ixodidis.yaml --out /private/tmp/ixodidis-strict-20261005.tsv`: exit 0; one file scanned, zero error rows.
- Read-only full-table comparisons checked identity, every ancestor, synonym content/scope, direct inventory rows, attestation, PATHS/scope uniqueness, and the inline seed event. Full backbone/status scans found no children, target type-material row, merged-ID row involving the target, or dropped row.
- `just verify-corpus`: not run because it is a full-corpus reproduction gate, not a focused record validator. Its `--max-diffs` option limits diagnostics, not scope. The bounded comparisons above do not replace full reproduction.
- `validate-products`: not applicable because no curator-added causal graph is present. `validate-history`: not run; ignored-inclusive filename and content searches found no target history artifact. The inline event was checked separately. No undocumented focused term/reference validator was invented.

## Identity and Grounding

The pinned backbone at `data/raw/ncbitaxon_taxa.tsv:221585`, live [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034400&retmode=xml), and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034400) agree on the ID, label, species rank, and bacterial placement. EFetch confirms parent Rickettsiella (`NCBITaxon:59195`) and genetic code 11. Exact grounding to this source concept does not assert valid publication or resolve alternative species assignments in the literature.

All nine root-first ancestors agree with the pinned backbone: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Legionellales, Coxiellaceae, and Rickettsiella. Datasets confirms their IDs; EFetch confirms the eight non-root labels and ranks.

The five complete native name objects at `data/catalog/ncbi_names-0005.jsonl.gz:30965` through line 30969 distinguish one scientific name, one authority, and three synonyms. The authority is correctly `RELATED_SYNONYM`; the pathotype and two Ixodes woodi names are correctly `EXACT_SYNONYM`. Live EFetch confirms those classes. The authority's author spelling is source-derived but bibliographically wrong, as detailed in the minor finding.

## Evidence

- The sole `NCBITAXON` attestation matches the source row in ID, label, one `NAME`, and 2026-09-13 snapshot. It counts a source concept, not separate name strings, cultures, experiments, or genomes.
- Complete direct scans found no target row in BacDive, LPSN, GTDB mappings, GOLD organisms, MediaDive, Madin, or BactoTraits. No mapped nomenclature or type-strain inventory assertion was omitted by the seeder.
- The [2012 primary paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0038062), its open-access XML body, and [PMID 22675436](https://pubmed.ncbi.nlm.nih.gov/22675436/) verify Leclerque and Kleespies, PLoS ONE 7(5):e38062, published 2012-05-31, DOI `10.1371/journal.pone.0038062`. It uses ixodidis as a pathotype designation, assigns the studied tick bacterium to R. grylli, and distinguishes the cricket-associated comparator from the differently placed genome-project strain. This historical species interpretation differs from NCBI's separate ixodidis concept; neither is silently substituted for the other.
- Table 1 of that paper explicitly links five marker accessions to the studied bacterium. Direct accession retrieval succeeded even though exact Assembly and Nuccore queries `txid1034400[Organism:noexp]` both returned zero items with phrases-not-found warnings. Those query results therefore do not establish absence of relevant sequence evidence.
- [AF383621.1](https://www.ncbi.nlm.nih.gov/nuccore/AF383621.1) is a 1,538 bp partial 16S sequence with source Rickettsiella sp. GSU, strain GSU, host Ixodes woodi, and `taxon:162467`, not 1034400. Its cited [PMID 12061452](https://pubmed.ncbi.nlm.nih.gov/12061452/) verifies Kurtti, Palmer, and Oliver, Journal of Medical Entomology 39(3):534-540 (2002), DOI `10.1603/0022-2585-39.3.534`. The PubMed accession list explicitly names AF383621. Its abstract supports a Rickettsiella-related endosymbiont from the examined I. woodi population; it does not establish a genome or universal host phenotype. The 2002 study was reviewed at abstract/bibliographic level.
- Four accession records identify Rickettsiella grylli, strain GSU-Iw1, host Ixodes woodi, and `taxon:59196`: [JQ740154.1](https://www.ncbi.nlm.nih.gov/nuccore/JQ740154.1), 996 bp complete ftsY CDS; [JQ070345.1](https://www.ncbi.nlm.nih.gov/nuccore/JQ070345.1), 786 bp partial gidA; [JQ070346.1](https://www.ncbi.nlm.nih.gov/nuccore/JQ070346.1), 894 bp partial rpsA; and [JQ070347.1](https://www.ncbi.nlm.nih.gov/nuccore/JQ070347.1), 924 bp partial sucB. All cite PMID 22675436 and its DOI, and use translation table 11. Complete metadata, source qualifiers, references, and features were inspected with bases/translations omitted.
- Table 1 lists an amplified rpsA length of 879 bp, whereas JQ070346.1 is 894 bp. Both source values are preserved here; no trimming history or correction is inferred. The discrepancy is external evidence context, not an error in a YAML field that contains neither accession nor length.
- Live taxonomy independently resolves [162467 as Rickettsiella sp. GSU](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/162467) and [59196 as Rickettsiella grylli](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/59196). Neither lookup redirects to 1034400. A paper-level relationship does not authorize merging their source concepts, importing all R. grylli assemblies, or representing the five markers as whole genomes.
- The complete SeqCode object at `data/seqcode/names.jsonl.gz:34917` provides name ID 36804, matching name, and resource/API URLs only. It is a name-catalog lead, not an explicit NCBI equivalence, formal nomenclature status, or type-genome link. The attempted LPSN name URL returned HTTP 404; no external valid-publication conclusion is based on that failure.

## Completeness

The zero BacDive strain count agrees with the direct inventory, and the complete backbone has no target descendants from which further strains could be gathered. Literature strain designations and differently classified marker sequences do not supply a missing BacDive deposit or a supported target genome link.

Gitignore-independent, compressed-aware searches used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. The primary search covered ID, label, historical Ixodes woodi names, and stem, returning eight contexts in scope/backbone/NCBI names/SeqCode. The secondary search covered the bounded numeric ID, Rickettsiella sp. GSU, GSU-Iw1, and all five bounded marker accessions, returning 12 contexts. No accession or GSU-Iw1 hit occurred in those roots.

The secondary results include the separate GSU concept in scope, backbone, and native names, but no target-specific BacDive strain, LPSN mapping, GTDB genome/mapping, GOLD/BV-BRC genome chain, StrainInfo deposit, ATB sample chain, or history artifact. Two numeric-ID hits are BioSample SAMEA1034400 for Streptococcus equi subsp. zooepidemicus, not this taxon. Shared digits are not identity evidence.

Optional definitions, phenotypes, evidence, nomenclature, and causal graphs need not be invented. The cross-source classification remains a documented reconciliation question rather than a demonstrated omitted required field. External discovery was bounded, not exhaustive.

## Findings

Counts: 0 blocker, 0 major, 1 minor.

1. **Minor: inherited authority-name typo.** `data/taxa/bacteria/rickettsiella_ixodidis.yaml:37` spells the author Kleepsies. The publication's author list and PubMed identify Regina G. Kleespies. The wrong spelling is present in the pinned native authority, derived backbone, and live NCBI EFetch, so this is upstream source metadata, not a seeder transcription or synonym-scope bug. The biological identity is unaffected. The maintained local source pin is `conf/ncbi_taxdump.yaml`; `src/taxonmech/ncbi_taxdump.py:81` preserves names and classifies authority as related, `src/taxonmech/extract.py:641` consumes the pin, and `src/taxonmech/seed.py:381` emits the source spelling.

No blocker or major finding was established. The paper's taxonomic interpretation and sequence-source IDs are explicitly retained as conflicts requiring source-aware reconciliation, not grounds for a hand-edited merge. This review does not promote the lifecycle status or imply human sign-off.

## Recommended Edits

Resolve the spelling at the NCBI-owned authority assertion, then capture a corrected snapshot through `conf/ncbi_taxdump.yaml` and the maintained extraction/seeding pipeline in a separately authorized change. The intended corrected author token is Kleespies. Preserve the original source assertion until the correction has explicit provenance; do not patch generated YAML, cached name objects, or `data/raw/ncbitaxon_taxa.tsv` in isolation, and do not add a one-off spelling rewrite to the seeder.

Any future taxonomic reconciliation must distinguish the literature's isolate/pathotype relationship from equivalence of whole NCBI concepts. Do not merge 1034400, 162467, and 59196, import the latter's assemblies, or normalize conflicting marker lengths on this review's authority alone. No source contact or correction request was sent.

## Follow-up Checks

For the minor correction, inspect the corrected native authority and provenance, refresh the pinned source only after separate authorization, and verify the generated synonym retains `RELATED_SYNONYM` with the corrected author spelling. Rerun both focused validators and `just verify-corpus` after authorized regeneration. Confirm the ID, rank, lineage, three exact synonyms, counts, and lifecycle state are unchanged.

Before future sequence or genome enrichment, recheck each accession's source taxon/strain and establish an explicit supported relationship to the reviewed concept. The current markers are not assemblies, and no inferred transfer of genomes across R. grylli should occur. The authority spelling and cross-source classification remain unresolved externally; neither prevented this bounded review.

## Additional Notes

- `data/taxa/PATHS.tsv:14050` uniquely maps the target to its stem. `curation/seed_scope.tsv:321897` supplies the 2026-09-13 one-source inclusion reason. The inline 2026-09-13T17:54:04Z seed event correctly names NCBITAXON and that reason.
- Ignored-inclusive filename searches found no earlier target report or history path, and history content was searched. Prior Rickettsiella reviews did not substitute for this target's evidence.
- The previously read review skill, CLAUDE guidance, curation skill/checklist, justfile, curation/harmonization/schema/history documentation, and schema had no current tracked changes. The NCBI parser, extraction input, seeder synonym block, and source configuration were inspected for finding ownership.
- NCBI browser and initial LPSN web requests failed; EFetch/Datasets, PubMed XML, PLOS article text, and Europe PMC full-text XML resolved. The standard-library LPSN retry returned 404. An earlier optional HTML parsing attempt lacked BeautifulSoup; no dependency was installed. The 2012 article body/tables were read, but the 2002 full text was not obtained.
- iModulonDB is not applicable because the YAML makes no gene, regulator, pathway, stress-response, or transcriptomic assertion. Marker features were inspected only for identity and source scope.
- Tracked/staged diffs were empty before report creation. Only this new report was written; no taxon YAML, source data, code, page, lifecycle status, curation event, prior report, or history entry was edited. No paid research, external contact, or GitHub mutation was performed.
