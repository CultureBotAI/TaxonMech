# YAML Record Review: Pseudoduganella lurida

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudoduganella_lurida.yaml`
- Started UTC: 2026-10-08T02:34:52Z
- Finished UTC: 2026-10-08T02:48:30Z
- Verdict: pass with minor issues

## Target

One generated `TaxonRecord`, `NCBITaxon:1036180`, Pseudoduganella lurida, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:1522432` (Pseudoduganella). Grounding is `EXACT`; mapping status remains `SEEDED`. All 556 YAML lines were read before the verdict. This review is not a curation action or human approval.

The record is generated from the pinned inventories and maintained seed scope, not an independently maintained YAML document. `data/taxa/PATHS.tsv:14812`, `curation/seed_scope.tsv:10804`, and `curation/legacy_page_paths.tsv:888` resolve this target consistently. The scope row names six sources. The embedded seed event is dated `2026-09-13T17:54:04Z`.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1` for the existing local environment.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/pseudoduganella_lurida.yaml` | Pass; no issues found. |
| `just validate-strict data/taxa/bacteria/pseudoduganella_lurida.yaml --out /private/tmp/plurida-strict.tsv` | Pass; one file, zero errors; diagnostic TSV contains only its header. |
| Structured comparison against the backbone, lineage, source inventories, scope, and path index | All represented identities, ranks, lineage entries, counts, and source fields agree with the pinned rows. |
| Complete-field comparison of strain links against raw, StrainInfo, and ATB inputs | Exact agreement: eight assembly assertions, seven genome-record assertions, and 18 related-record assertions. Raw inputs contribute 8/6/18; ATB contributes one genome record; no eligible StrainInfo links were found in these inputs. |
| Primary-source identity and accession checks | NCBI taxonomy, LPSN, BacDive, NCBI assembly/BioSample/BioProject, marker metadata, publication metadata, and ENA run/analysis evidence inspected as detailed below. |

Not run: full-corpus `just verify-corpus`, `just provenance-check`, `just render-check`, `just docs-check`, `just qc`, the complete test suite, or whole-corpus history validation. The bounded comparisons above are diagnostics, not substitutes for those gates. No focused reference validator is documented for this record. `just validate-products` covers ontology-grounded causal nodes, not these taxonomic identifiers; this record has no causal graph. No target-specific append-only history file was found in the ignored-inclusive bounded searches, so no such file was available for `just validate-history`.

## Identity and Grounding

The pinned backbone at `data/raw/ncbitaxon_taxa.tsv:222306` and both live NCBI taxonomy interfaces agree on the identifier, scientific name, species rank, parent, genetic code 11, and lineage. All ten root-first ancestors have the expected labels and ranks. NCBI's XML omits the root node from `LineageEx`, while its Datasets lineage includes taxon 1. No child taxon was found in the complete pinned backbone comparison. Exact-ID reads found six type-material rows at `data/raw/ncbi_type_material.tsv:1873` through 1878, and no entry in the complete merged-ID or dropped inventories. [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1036180), [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036180).

The naming disagreement is real and preserved: NCBI uses Pseudoduganella lurida; LPSN identifies `lpsn:30126` as a validly published homotypic synonym and prefers Massilia lurida, `lpsn:790876`. LPSN also explains that the Pseudoduganella combination is correct when that separate genus is accepted. The record's `is_correct_name: false`, authority, and separately sourced Massilia synonym retain this distinction. It should not be silently renamed to follow LPSN. The misleading chronological wording is a minor finding below. [LPSN Pseudoduganella lurida](https://lpsn.dsmz.de/species/pseudoduganella-lurida), [LPSN Massilia lurida](https://lpsn.dsmz.de/species/massilia-lurida).

The pinned GTDB species is `GTDB:s__Rugamonas_lurida`, with one representative genome and a species-to-species `skos:closeMatch`. `data/raw/gtdb_mappings.tsv:1454`, `data/raw/gtdb_species.tsv:156847`, and the complete native representative record `data/catalog/gtdb_genomes-0011.jsonl.gz:38300` support this mapping through the same type-strain genome. The source-attributed GTDB synonym and xref do not replace the NCBI lineage. GTDB's higher classification differs, including class Gammaproteobacteria and family Burkholderiaceae_D; that source conflict must remain separate from NCBI's classification. Live GTDB retrieval was unavailable, so this assessment is pinned-snapshot support, not a current GTDB recertification.

## Evidence

| Claim or link | Inspected support and scope |
| --- | --- |
| NCBI names and synonym scopes | Complete native name objects in `data/catalog/ncbi_names-0005.jsonl.gz:31835` through 31839 agree with the current taxonomy response: Massilia lurida is an exact synonym; the two authorities and Massilia sp. D5 retain related scope. |
| LPSN status, identifiers, publications, and marker | Both complete inventory rows, `data/raw/lpsn_names.tsv:5621` and 27787, agree with the represented status and synonym relationship. Current LPSN pages resolve both name IDs, their authorities, the shared type, and HQ839786. Both inventory rows carry only KCTC in their type-deposit list, the upstream completeness issue described below. |
| Type strain and culture collections | `data/raw/bacdive_strains.tsv:56237`, the complete native object `data/bacdive/records.jsonl.gz:56236`, and the live BacDive entry agree on BacDive 133930, designation D5, CGMCC 1.10822, KCTC 23880, and taxon 1036180. NCBI culture-collection rows 38796 and 117630 independently retain both deposits. The original species paper explicitly identifies D5 as their shared type strain. [BacDive](https://bacdive.dsmz.de/strain/133930), [original paper, PMID 23087170](https://pubmed.ncbi.nlm.nih.gov/23087170/). |
| Nomenclatural literature | PMID 36063369 resolves to DOI `10.1099/ijsem.0.005407`, Lu and colleagues' 2022 phylogenomic paper. The publisher abstract explicitly supports transferring M. lurida into Pseudoduganella. PubMed returned bibliographic metadata without an abstract; the publisher supplied the abstract. DOI `10.1099/ijsem.0.005681` resolves to the notification for volume 72, part 9 and is linked by LPSN. Its full notification table was not independently retrieved. [2022 paper](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijsem.0.005407), [notification](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijsem.0.005681). |
| INSDC HQ839786 | Current identity/source/reference metadata resolves to HQ839786.2, 1,486 bp, partial 16S rRNA, strain D5, taxon 1036180, type material of Massilia lurida. Its citation is PMID 23087170 / DOI `10.1099/ijs.0.047068-0`. The record's unversioned accession remains valid; sequence bases and non-source features were not reanalyzed. [NCBI marker record](https://www.ncbi.nlm.nih.gov/nuccore/HQ839786.2). |
| Genome assemblies | All eight complete raw assertions at `data/raw/strain_assemblies.tsv:33174` through 33181 match the YAML. The unversioned BacDive accession, versioned GenBank accession GCA_007830455.1, and paired RefSeq GCF_007830455.1 represent source-specific links, not eight independent genomes. Live NCBI reports a current type-material assembly for CGMCC 1.10822, 27 contigs, 6,000,972 bases, BioSample SAMN02927932, and BioProject PRJNA255574. Complete native GenBank and RefSeq rows agree. [NCBI assembly report](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_007830455.1/dataset_report). |
| BV-BRC, GOLD, GTDB, and IMG links | Complete native BV-BRC `data/bvbrc/bvbrc-0000.jsonl.gz:3358` supports `patric:1036180.3`, the named strain, assembly, sample, and project. Complete GOLD organism 55012, project 55494, and analysis 26047 support `Go0093921`, `Gp0093921`, `Ga0040943`, and `img.taxon:2596583599`. The analysis has a blank direct organism field, but its single project resolves unambiguously to that organism. Explicit culture-collection and strain fields are retained as separate evidence assertions. GTDB's representative agrees on the same deposit and assembly pair. The six raw genome assertions at `data/raw/strain_genome_records.tsv:26059` through 26064 and all 18 raw related assertions at `data/raw/strain_related_records.tsv:89146` through 89163 were read completely. BacDive reference 66792 identifies automated DiASPora crosslinks, not independent experimental evidence. |
| BioSample and project scope | The complete live BioSample record identifies SAMN02927932 as CGMCC 1.10822, type material, taxon 1036180, with secondary SRA sample SRS1667079. Bounded primary BioProject fields confirm PRJNA255574 is this isolate's sequencing project. PRJNA224116 is the multispecies RefSeq annotation umbrella, correctly retained only as a related project, not isolate-identity evidence. [BioSample](https://www.ncbi.nlm.nih.gov/biosample/SAMN02927932), [isolate project](https://www.ncbi.nlm.nih.gov/bioproject/PRJNA255574), [annotation project](https://www.ncbi.nlm.nih.gov/bioproject/PRJNA224116). |
| ATB assembly and provenance | Complete `data/atb/assemblies.tsv:3606`, `data/atb/strain_links.tsv:1094`, all five genome-link rows 4844 through 4848, and the full catalog row `data/catalog/allthebacteria.tsv.xz:1058603` agree on `atb.assembly:202505.SAMN02927932`, dataset 661k, run SRR4128952, analysis ERZ3988557, PASS filters, SeqKit identifier, and the release-specific URLs. All six embedded same-sample evidence assertions match the YAML. Live ENA confirms SRR4128952 and ERZ3988557 refer to SAMN02927932 / SRS1667079; the analysis is a Shovill third-party assembly, not the JGI AllPaths assembly. The crosswalk correctly says `shares_biosample`, not sequence equivalence. [ENA run](https://www.ebi.ac.uk/ena/browser/view/SRR4128952), [ENA analysis](https://www.ebi.ac.uk/ena/browser/view/ERZ3988557). |
| Source attestations | Direct inventory rows support NCBI 1 NAME, LPSN 1 NAME, GTDB 1 GENOME, BacDive 1 STRAIN, GOLD 1 ORGANISM, and Madin 18 TRAIT_ASSERTION. The counts are not summed into a biological claim. GOLD row 495 and Madin row 686 agree with the YAML; the BacDive list contains its one advertised strain, with no hidden cap. |

SeqCode native name objects at `data/seqcode/names.jsonl.gz:11620` and 28704 were also read as corroborating nomenclatural context; they are not invented YAML attestations. No phenotype, habitat, resistance mechanism, pathway, or causal edge is asserted here. Literature about the other organisms in the 2022 paper is not evidence about this strain. iModulonDB is not applicable to these identity and provenance claims.

## Completeness

The two minor issues below concern nomenclatural wording and an incomplete LPSN-specific deposit list. The sole strain entry itself retains both deposits and has the correct type flag, so the missing LPSN designation does not break the genome joins or change identity.

Ignored-inclusive target resolution searched `data/taxa`, `reports/yaml_record_review`, `history`, and `curation` by identifier, name, and slug. It resolved one target, the path/scope/legacy rows, and no pre-existing target report or separate target history. An ignored-inclusive compressed-source search covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`, using the taxon ID, all three genus/species forms, both deposits, and the represented assembly/sample/project/run/analysis/marker identifiers. It returned 73 addresses. Relevant native JSON objects and complete TSV rows, including the ATB catalog row, were inspected; this is not a claim to have read every object in those source corpora. The five `SOURCE.json` files were separately parsed, and history filenames were independently checked.

No direct MediaDive or BactoTraits inventory row and no eligible StrainInfo link emerged from those bounded checks. BacDive carries a legacy StrainInfo cross-reference 28119; an additional complete structured scan of all 314,470 objects in `data/straininfo/records.jsonl.gz` found no matching `strain.siID`. That does not prove that the historical link never existed or identify its current replacement. No link was inferred from this unresolved external cross-reference. Absence statements here include ignored files within the stated roots and are not claims about all online databases or uninspected accessions. The generic designation D5 was not used as a global identity join.

Optional discussion, separate experimental evidence, causal graph, and curated-history slots are appropriately unfilled for this seeded identity record. Source presence counts do not require importing the underlying phenotypes. Eukaryota was excluded from review and left unchanged as instructed.

## Findings

Counts: 0 blocker, 0 major, 2 minor.

1. **Minor: the deprecated-name note implies the wrong publication chronology.** YAML line 59 describes a synonym of a later correct name. LPSN's preferred Massilia lurida dates to 2013; the represented Pseudoduganella combination dates to 2022. The status flags and linked synonym are otherwise correct. A neutral statement that LPSN treats this name as a synonym, optionally naming its preferred taxon, would avoid conflating preference with publication date. Maintained owner: `src/taxonmech/seed.py:418`, which emits this generic wording. This is a documentation defect, not evidence that the taxon should be renamed.

2. **Minor: the LPSN type-strain list omits CGMCC 1.10822.** YAML lines 51-52 contain only KCTC 23880, while both live LPSN name pages and the original species description support D5 = CGMCC 1.10822 = KCTC 23880. The strain block already contains both normalized culture-collection identifiers. The omission is present in `data/raw/lpsn_names.tsv:5621` and 27787, so hand-editing this generated YAML would not repair it. Maintained ownership begins in the KG-Microbe LPSN transform feeding `data/transformed/lpsn/edges.tsv`; the local consumer is `src/taxonmech/extract.py:424`, particularly the type-deposit edge handling at line 461, followed by `src/taxonmech/seed.py:405`. The configured upstream edge files were unavailable at the explicit paths checked, so the precise upstream parser cause remains unconfirmed. This is a nonblocking inventory-completeness gap, not an unsupported existing deposit or a lost strain link.

## Recommended Edits

1. In a separate authorized curation/code change, revise the generic deprecated-name text in `src/taxonmech/seed.py` to avoid chronological assumptions. Resolve and name the preferred LPSN synonym where supported by the inventory, while preserving the NCBI label, LPSN status flags, and source-attributed GTDB classification. Add a focused regression case for a newer combination whose preferred name is older.
2. Inspect the maintained KG-Microbe LPSN type-strain extraction and normalization for `lpsn:30126` and `lpsn:790876`, then refresh the relevant transform and TaxonMech inventory through the documented extraction workflow. Retain CGMCC 1.10822 and KCTC 23880 as collection identifiers; do not invent a culture-collection identifier for bare D5. Correct `src/taxonmech/extract.py` only if inspection shows that it drops a valid upstream edge. Regenerate this record from corrected maintained inputs; do not patch the inventory, YAML, or pages merely to make the review pass.

No edits were made by this review, except this new report. The active generated record remains `SEEDED`, with no appended history event.

## Follow-up Checks

- Verify the corrected note against the two LPSN pages and authorities, and test its generation for reversed publication chronology.
- Inspect both maintained LPSN name records and their normalized type-deposit edges; confirm the refreshed inventory includes CGMCC 1.10822 without losing KCTC 23880 or synonym direction.
- After authorized generation, rerun the documented one-record schema and strict commands above; confirm both deposits, the type flag, and all strain links remain supported. The documented `just seed-canary NCBITaxon:1036180` is a write operation and was not run during this review.
- Run `just verify-corpus` and the repository's provenance, rendering, documentation, and QC gates before publishing a maintained-input change. Validate a new append-only history event only if a later curation change actually creates one.
- Optionally resolve BacDive's legacy StrainInfo reference and retry the live GTDB/GOLD pages and publisher full text. None is an identity blocker under the inspected pinned evidence.

## Additional Notes

Review HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The target's SHA-256 before review and immediately before reporting was `3d42283b6fe58afbd51bbfb0cd7aea1bd1381d60721326049431c1df03a84986`. Tracked diffs were empty; pre-existing untracked reports and all seven registered worktrees were preserved. No source refresh, archive download, paid research, outreach, GitHub mutation, or lifecycle promotion occurred.

Access limits: live GTDB and GOLD pages were unavailable; IMG and BV-BRC services were not independently queried beyond their inspected native exports and BacDive crosslinks. The 2022 paper's species-specific full text and the notification table could not be obtained through the attempted publisher endpoints, although the former's abstract, citation identity, LPSN association, and notification title were verified. Initial ENA XML access with a JSON Accept header returned 406; retrying with an XML Accept header succeeded. ATB archive and FASTA bytes were not downloaded or rehashed; the release metadata and same-sample provenance, not sequence identity, were reviewed. Full BioProject secondary-identifier and locus lists were not printed or analyzed; only primary identity, description, and project-type fields were used.

The two explicit configured KG-Microbe LPSN edge paths returned file-not-found diagnostics; no claim is made that copies do not exist elsewhere. The named code consumers and committed inventory establish where to start the later repair, not which uninspected upstream version caused the omission.
