# YAML Record Review: Rickettsiella sp. 'Phyllophaga sp.'

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/rickettsiella_sp_phyllophaga_sp.yaml`
- Started UTC: 2026-10-05T08:54:16Z
- Finished UTC: 2026-10-05T08:58:40Z
- Verdict: pass

## Target

The complete 61-line `TaxonRecord` was read before judgment. It denotes `NCBITaxon:1034386`, Rickettsiella sp. 'Phyllophaga sp.', rank `SPECIES`, domain `BACTERIA`, with `grounding_status: EXACT` and `mapping_status: SEEDED`. It is a generated NCBI-backed host-associated taxon record, not a formal species description or a genome record. Future seeded-field corrections belong to the responsible source capture/transform, `src/taxonmech/extract.py`, `src/taxonmech/seed.py`, or `curation/seed_scope.tsv`, not manual YAML edits.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/rickettsiella_sp_phyllophaga_sp.yaml`: exit 0, no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/rickettsiella_sp_phyllophaga_sp.yaml --out /private/tmp/phyllophaga-strict-20261005.tsv`: exit 0; one file scanned, zero error rows.
- Read-only full-table comparisons checked the identity, every ancestor, synonyms, direct source inventory rows, attestation, PATHS/scope uniqueness, and inline seed event. Full backbone/status scans found no children, target type-material row, merged-ID row involving the target, or dropped row.
- `just verify-corpus`: not run because it is a full-corpus reproduction gate, not a focused record validator. Its `--max-diffs` option caps diagnostics, not scope. The bounded comparisons above do not replace full reproduction.
- `validate-products`: not applicable because no curator-added causal graph is present. `validate-history`: not run; ignored-inclusive filename and content searches found no target history artifact. The inline event was checked separately. No undocumented focused term/reference validator was invented.

## Identity and Grounding

The pinned backbone at `data/raw/ncbitaxon_taxa.tsv:221584`, live [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034386&retmode=xml), and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034386) agree on the taxon ID, label, species rank, and bacterial placement. EFetch confirms parent `NCBITaxon:2637345`, unclassified Rickettsiella, and genetic code 11. The unclassified parent must not be replaced by the genus merely to resemble nearby named-species records.

Every root-first ancestor agrees with the pinned backbone: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Legionellales, Coxiellaceae, Rickettsiella, and unclassified Rickettsiella. Datasets supplies all ten corresponding IDs; EFetch supplies the nine non-root ancestor labels and ranks. Exact grounding is to this NCBI concept, not a claim of valid nomenclatural publication or identity with a named sibling species.

Complete native objects at `data/catalog/ncbi_names-0005.jsonl.gz:30962` through line 30964 classify the current label as `scientific name` and both historical names as `synonym`: Rickettsiella pathotype Rickettsiella phyllophagae and Rickettsiella symbiont of Phyllophaga sp. Live EFetch confirms both synonym classes. Their `EXACT_SYNONYM` treatment is source-supported; neither is an `includes` or authority entry mispromoted to exactness.

## Evidence

- The sole `NCBITAXON` attestation matches the backbone in ID, label, one `NAME`, and the 2026-09-13 snapshot. It counts a source concept, not strains, genomes, experiments, or the three native name strings separately.
- Complete direct inventory scans found no target row in BacDive, LPSN, GTDB mappings, GOLD organisms, MediaDive, Madin, or BactoTraits. The record does not invent nomenclature, type-strain, mapping, genome, or phenotype assertions from adjacent Rickettsiella records.
- The exact NCBI Assembly query `txid1034386[Organism:noexp]` returned zero items and a phrases-not-found warning. This is a bounded query result, not proof that no genome exists. The corresponding Nuccore query returned seven IDs; all seven records' metadata, source qualifiers, references, and feature annotations were inspected, omitting sequence bases and translations.
- Four markers identify strain JKI AMX2008-1, taxon 1034386, and host Phyllophaga sp.: [JF505109.1](https://www.ncbi.nlm.nih.gov/nuccore/JF505109.1), 1,357 bp partial 16S; [JF505110.1](https://www.ncbi.nlm.nih.gov/nuccore/JF505110.1), 932 bp partial 23S; [JF505111.1](https://www.ncbi.nlm.nih.gov/nuccore/JF505111.1), 996 bp complete ftsY CDS; and [JF708249.1](https://www.ncbi.nlm.nih.gov/nuccore/JF708249.1), 291 bp partial 23S with an intervening sequence annotated at positions 79-205. Their isolation source is an infected grub.
- Three additional markers retain the same strain and taxon ID, but explicitly name host Phyllophaga vetula: [JQ086565.1](https://www.ncbi.nlm.nih.gov/nuccore/JQ086565.1), 786 bp partial gidA; [JQ086566.1](https://www.ncbi.nlm.nih.gov/nuccore/JQ086566.1), 894 bp partial rpsA; and [JQ086567.1](https://www.ncbi.nlm.nih.gov/nuccore/JQ086567.1), 891 bp partial sucB. Their narrower host metadata does not rename the NCBI concept or establish a species-wide host range.
- All seven sequence records retain an unpublished reference about a Rickettsiella-like bacterium from Mexican May beetles and direct-submission metadata. No DOI or PMID is supplied by those references. Searches for the title and complete strain designation did not establish a target-specific published primary paper in this bounded review; this is not a claim that none exists. No publication conclusions from other Rickettsiella pathotypes were transferred to this target.
- These are gene records, not assemblies. A complete ftsY CDS is not a complete genome. Neither the source phrase genomic DNA nor Datasets' dsDNA taxonomy metadata establishes an assembly or a culture-deposit association.

## Completeness

The zero BacDive strain count matches the complete direct inventory, and the target has no descendant taxa from which additional inventory strains could be gathered. A strain designation on marker sequences does not supply a missing BacDive record or authorize a deposit-to-genome join. No supported missing strain-genome association was identified.

Gitignore-independent, compressed-aware searches used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. The primary search covered the CURIE, numeric taxonomy-ID fields, scientific/historical host-associated names, and stem; it returned five contexts, all in the scope, backbone, or native NCBI names. The secondary search covered the bounded numeric ID, complete JKI AMX2008-1 designation, and all seven marker accessions; it returned seven contexts, none matching the strain designation or markers.

The two additional numeric-ID hits concern BioSample SAMEA1034386 in a GenBank assembly object and the ATB inventory. Their organism is Streptococcus equi subsp. zooepidemicus, with GenBank taxid 40041 and species taxid 1336, not this target. Shared digits do not establish taxon identity. Neither search supplied a target-specific LPSN inventory row, GTDB mapping, BacDive entry, GOLD/BV-BRC genome chain, StrainInfo deposit, SeqCode object, ATB sample chain, or history artifact within the searched roots.

Optional definitions, nomenclature, evidence, phenotype, and causal-graph slots need not be populated merely to make this generated record longer. This review does not claim exhaustive external literature, nomenclature, or genome discovery.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed record. Identity, synonym scope, full lineage, counts, attestation, and seed history are supported. The informal taxon label and differing marker-host specificity are preserved without inventing formal nomenclature, sibling-species equivalence, or a genome link. A pass verdict is not human sign-off or promotion to `REVIEWED`.

## Recommended Edits

None required for the current generated record. Any separately authorized source enrichment should establish an explicit authority mapping and preserve strain-level provenance before changing the source inventories through their maintained capture/transform. Do not hand-edit this YAML, collapse its unclassified parent, promote phyllophagae to a formally established species name, or treat marker records as genome assemblies.

## Follow-up Checks

No additional action is required to accept this bounded review. After any separately authorized source refresh, compare the resulting target row and rerun both focused validators. Use `just verify-corpus` after authorized regeneration to prove full reproduction. A proposed nomenclature or genome enrichment needs target-specific primary-source support and explicit taxon/strain/sample scope, not inference from related pathotypes or shared identifier digits.

## Additional Notes

- `data/taxa/PATHS.tsv:14048` uniquely maps this ID to its stem. `curation/seed_scope.tsv:321896` provides the 2026-09-13 one-source inclusion reason. The inline 2026-09-13T17:54:04Z event correctly records `seed_from_sources`, `SEEDED_FROM_SOURCES`, NCBITAXON, and that reason; YAML escaping preserves the nested apostrophes.
- Ignored-inclusive filename searches found no previous target report or history path; history contents were also searched. The previous named Rickettsiella reviews did not substitute for this record's checks.
- The previously read review/curation guidance, checklist, justfile, curation/harmonization/schema/history documentation, and schema had no tracked changes. The checklist and curation skill were reread before final judgment.
- The NCBI Taxonomy browser request failed, but complete EFetch and Datasets responses resolved and were inspected. Sequence metadata also resolved. Search snippets and unrelated literature were not used as evidence for the verdict.
- iModulonDB is not applicable: the YAML makes no gene, regulator, pathway, stress-response, or transcriptomic assertion. Marker features were inspected only for identity and the gene/genome distinction.
- The other Codex session was reported closed. One worktree was present on `codex/record-review-extensimonas-20261003`, and tracked/staged diffs were empty before report creation. No new worktree was necessary for this read-only review.
- No taxon YAML, source data, code, page, lifecycle status, curation event, previous report, or history entry was edited. No paid research, external contact, or GitHub mutation was performed.
