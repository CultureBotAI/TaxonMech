# YAML Record Review: Aminobacter anthyllidis

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/aminobacter_anthyllidis.yaml`
- Started UTC: 2026-10-06T10:24:31Z
- Finished UTC: 2026-10-06T10:30:11Z
- Verdict: pass with minor issues

## Target

Read the complete 724-line generated `TaxonRecord` for `NCBITaxon:1035067`, Aminobacter anthyllidis. It carries species rank, bacterial domain, parent Aminobacter (`NCBITaxon:31988`), nine ancestors, genetic code 11, `EXACT` grounding, `SEEDED` status, one LPSN nomenclature entry, one GTDB mapping, ten related synonyms, two xrefs and one BacDive type-strain entry. That strain carries ten assembly assertions, eight genome-record assertions and 26 related-record assertions. Five source attestations and one inline seed event supply provenance. Optional definition, causal graph, record-level evidence and discussion are unasserted. No generated record, source input or history is changed by this review.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/aminobacter_anthyllidis.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/aminobacter_anthyllidis.yaml --out /private/tmp/aanth-validation.tsv`: exit 0, one file scanned, zero errors. Read the header-only diagnostic TSV.
- Structured source comparisons verified identity, every lineage entry, genetic code, the unique index/scope entries, attestations and inline event. Nine type-material rows and eight merged-ID rows were inspected; the dropped-record scan found no target entry.
- A separate structured diagnostic compared every strain assembly, non-ATB genome and related-record assertion with its complete raw/StrainInfo inventory row, including parsed nested evidence. All matched. The ATB assertion matches the overlap metadata and all seven prior BIOSAMPLE assertions exactly. This is a bounded diagnostic, not a substitute for corpus reproduction.
- The repository's CAFI matcher accepts `LMG 26462` and `CFBP 7437`, yielding their existing deposit keys. It rejects bare aliases `STM 4645` and `D-10A` as genome-join keys. The percent-encoded STM alias is retained as source metadata, not promoted to a registered collection deposit.
- Ignored-inclusive searches of reports and `history/` found mentions in two preceding Mesorhizobium reviews but no target review or separate target history artifact. An ignored-inclusive filename search independently found no prior report/history filename for this stem. The inline seed event remains unchanged.
- Not checked: full-corpus `just qc`, `just verify-corpus`, `just validate-all`, `just test`, `just validate-history`, site drift and publication gates. No focused term/reference/history validator was invented. `just validate-products` is inapplicable without curator-added graph nodes. Focused checks do not certify whole-corpus or release readiness.

## Identity and Grounding

The backbone is `data/raw/ncbitaxon_taxa.tsv:221871`; native name rows are `data/catalog/ncbi_names-0005.jsonl.gz:31297` through `31307`. The index is `data/taxa/PATHS.tsv:14353`, and maintained scope is `curation/seed_scope.tsv:14832`. The scope date is 12 September 2026; the later seed event correctly uses the extraction timestamp. No classified children or retirement destination are present in the pinned backbone.

Complete [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035067&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035067) confirm the current identity, rank, parent and genetic code. The chain is root (`1`), cellular organisms (`131567`), Bacteria (`2`), Pseudomonadati (`3379134`), Pseudomonadota (`1224`), Alphaproteobacteria (`28211`), Hyphomicrobiales (`356`), Phyllobacteriaceae (`69277`) and Aminobacter (`31988`). Datasets includes root; EFetch verifies the remaining labels and ranks.

The ten related synonyms correspond to one NCBI authority name and nine `includes` names: Aminobacter sp. STM 4640, 4641, 4643, 4644, 4645, 4646, 4653, 6498 and 6499. They are correctly not exact synonym assertions equating all isolates. Type-material strings are retained separately in `data/raw/ncbi_type_material.tsv:1801` through `1809`. The merged table at lines 1040-1047 maps historical IDs `1035058`, `1035061`-`1035066` and `1035068` to this taxon; no claim is made that these historical IDs are additional currently reviewed records.

[LPSN record 790620](https://lpsn.dsmz.de/species/aminobacter-anthyllidis) verifies the species name, Maynaud et al. 2013 authority, valid publication under the ICNP, correct-name status, type designations and linked 16S accession. The distinction between effective publication in 2012 and validation in 2013 is sound. The imported `legitimate=True` value matches the maintained LPSN status row; the public page does not separately expose that API boolean. LPSN and the [SeqCode entry](https://registry.seqco.de/names/2469) support the name identity; the latter is an ICNP-valid-name registry entry, not a claim of a separate SeqCode type genome.

The GTDB `closeMatch` and xref agree with `data/raw/gtdb_mappings.tsv:1410`, `gtdb_species.tsv:8975` and the LPSN mapping. Both complete native GTDB genome rows classify LMG 26462 and D-10A in this species, supporting the imported count of two. This does not imply two BacDive strains or equivalence of those isolates.

## Evidence

The imported nomenclature row is `data/raw/lpsn_names.tsv:27560`. Its authority, statuses, URL, citations, accession and single type-designation entry are emitted faithfully. The source-level completeness difference in that designation list is the minor finding below.

The inspected [Maynaud et al. PubMed record](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=22221859&retmode=xml) verifies PMID `22221859`, DOI `10.1016/j.syapm.2011.11.002`, the 2012 species study and STM4645/LMG26462/CFBP7437 type-strain equivalences. The [validation-list publisher page](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.052571-0) verifies DOI `10.1099/ijs.0.052571-0`, publication on 1 May 2013 and the naming procedure; its dynamically loaded species table was not available. LPSN explicitly identifies validation list 151 and notes the corrected spacing of the collection designations. The 2012 full experimental text was not inspected in this review; the primary abstract suffices for the identity claims used here, not a comprehensive phenotype audit.

[FR869633](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=FR869633&rettype=gb&retmode=xml) resolves to version `.2`, a 1,455-bp partial 16S sequence explicitly naming STM 4645 and type material of this taxon. Its reference matches the species paper. The YAML preserves LPSN's unversioned accession rather than inventing a version. A marker sequence is not counted as a genome.

The complete native [BacDive 168687](https://bacdive.dsmz.de/strain/168687) projection at `data/bacdive/records.jsonl.gz:90919`, the public page and `data/raw/bacdive_strains.tsv:90920` agree on CFBP 7437, LMG 26462 and STM 4645. The existing LMG type designation justifies `is_type_strain: true`. Native BacDive reference `66792` supplies unversioned `GCA_018555685`, BV-BRC `1035067.4` and IMG `8002285264`; its annotation is explicitly automated source evidence, not proof that all database identifiers are interchangeable.

| Source | Inspected strain-to-genome support |
| --- | --- |
| NCBI Assembly | Native GenBank `0016:49826` and RefSeq `0003:30716` explicitly name LMG 26462, the GCA/GCF `018555685.1` pair, sample `SAMN18148366`, contig-level assembly `ASM1855568v1` and type-material status. Both live assembly reports agree. |
| BV-BRC | Native `0000:3300` gives `1035067.4`, LMG 26462 in both culture-collection and strain fields, `GCA_018555685.1`, `SAMN18148366` and `PRJNA706925`. Both retained match paths are supported. |
| GTDB | Native `0002:49536` gives representative `RS_GCF_018555685.1`, paired GenBank accession, whole deposit `LMG 26462`, sample and RefSeq project context. The namespace, version and source fields are retained. |
| GOLD | Organism `Go0657084` at `organisms.jsonl.gz:483605` names LMG 26462; project `Gp0701350` at `projects.jsonl.gz:526921` explicitly links that organism and sample; analysis `Ga0594671` at `analyses.jsonl.gz:389943` explicitly links that project and supplies the GCA accession and IMG ID. Its organism field is empty, but the inspected project supplies an unambiguous known-organism chain. |
| StrainInfo | Native `records.jsonl.gz:289789` and the complete live API record verify strain `377733`, DOI `10.60712/SI-ID377733.3`, LMG deposit `866368` and CFBP deposit `886751`, both available and non-deprecated. The genome assertion explicitly names only LMG deposit `866368`; it is not transferred to CFBP by shared SI-ID membership. |
| AllTheBacteria | Native catalog row `2012469`, overlap `assemblies.tsv:8176` and `strain_links.tsv:2773` agree on the exact sample, run `SRR13863412`, analysis `ERZ25889052`, dataset `r0.2`, available FASTA and passing pipeline/Sylph/HQ filters. All seven prior source sample links are preserved. |

The complete [NCBI assembly response](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035067/dataset_report?page_size=100) contains four accession reports, representing two GenBank/RefSeq pairs, not four distinct isolates. The LMG pair has 6,717,907 bp in 30 contigs. The [BioSample XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=biosample&id=SAMN18148366&retmode=xml) confirms its strain, taxon, type-material assertion and `PRJNA706925` connection. Native RefSeq and GTDB rows additionally retain [PRJNA224116](https://www.ncbi.nlm.nih.gov/bioproject/PRJNA224116), the general RefSeq annotation project; it is not a second isolate-specific sequencing experiment.

The [Artuso et al. primary genome paper](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8235418/fullTextXML), DOI `10.3390/microorganisms9061332`, PMID `34205374`, corroborates the culture source and sequencing. Read its bibliographic record/abstract, sequencing methods, genome-size result and data-availability statement. The latter explicitly links LMG 26462 to WGS `JAFLWW000000000` (described version `JAFLWW010000000`), `SRR13863412`, `PRJNA706925` and `SAMN18148366`. No inferred metabolic or nodulation claim from that paper is added to this taxonomic record.

ATB retains SeqKit sum `seqkit.v0.1_DLS_k0_8f81f8180b09386873645e79c4f8e090`, the native AWS URL and OSF batch-95 archive metadata. These were inspected, not downloaded or recomputed; SeqKit sum is not MD5. Five derived crosslinks at `data/atb/genome_links.tsv:11704` through `11708` retain matching genome/sample provenance and use `shares_biosample`, never genome identity. Projects, samples, GOLD entities, SI-ID/SI-DP and the versioned StrainInfo DOI remain separate entity types.

Attestations match their maintained rows: one NCBI name, one LPSN name, two GTDB genomes, one BacDive strain and two GOLD organism records. The two GOLD organisms, `Go0044089` (CFBP) and `Go0657084` (LMG), are source records for deposits of the retained strain, not two biological strains. No cross-source sum is justified. The inline seed event at `2026-09-13T17:54:04Z` correctly lists the five sources.

iModulonDB is inapplicable: the YAML contains no gene-function, regulator, pathway, stress or transcriptomics assertion. A taxonomic 16S accession and genome links do not require an expression-module interpretation.

## Completeness

Candidate discovery used `rg --no-ignore --hidden -n -z -i` across `data/raw/`, `data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`, `data/seqcode/`, `data/straininfo/`, `data/atb/`, `curation/` and `history/`. It included ignored/compressed files, target ID/name/slug, both collection designations, STM aliases, the marker/genome/sample/run/analysis identifiers, GOLD chain identifiers and StrainInfo's additional lab aliases. Only `SOURCE.json` provenance sidecars were excluded. This is bounded local evidence discovery, not a claim to search every external collection.

Initial and genome-identifier-expanded searches returned 131 rows; expansion to the remaining STM aliases produced 140. All 140 complete rows were read, using lossless common-field factoring for repetitive source rows. Address reconciliation found no unread or extra candidates. No target rows appeared in the imported MediaDive, Madin or BactoTraits tables; the BacDive medium count is zero. Optional phenotype/medium/graph enrichment is neither required nor inferred.

D-10A has its own native BV-BRC, GenBank, RefSeq and GTDB rows: `1035067.5`, `GCA_029872135.1`/`GCF_029872135.1`, `SAMN34244583`, `PRJNA957092`. Live metadata retain the same strain and classification. Its bare name is not an eligible collection accession, and no inspected deposit path connects it to BacDive 168687. Keeping its genome out of the LMG strain entry is correct; the species-level GTDB count still includes it.

Four similarly numbered Mesorhizobium taxa require caution: STM 4644 (`1665048`), STM 4645 (`1665049`), STM 4653 (`1665050`) and STM 6499 (`1665054`). Twelve inspected backbone/name/scope rows retain them separately. Live taxonomy independently confirms that `1665049` currently remains Mesorhizobium sp. STM 4645, not a redirect to this record. Shared bare STM designations do not authorize a merge or transfer of genomes. This is unresolved cross-source identity context for later strain-specific investigation, not evidence that the well-supported Aminobacter type identity is wrong. These comparator records were not fully reviewed or counted as covered here.

## Findings

Counts: 0 blocker, 0 major, 1 minor.

1. Minor: incomplete imported LPSN type-designation list. The YAML and `data/raw/lpsn_names.tsv:27560` retain only `kgmicrobe.strain:LMG-26462`, whereas the inspected LPSN page also identifies CFBP 7437 and the lab designation STM 4645. CFBP is independently supported by the primary species abstract, BacDive, NCBI type-material inventory and StrainInfo, and the local CAFI matcher recognizes it. This is non-blocking because the strain entry already retains CFBP/STM and is correctly flagged as the type strain through LMG. The maintained owner is the kg-microbe LPSN transform supplying `data/transformed/lpsn/edges.tsv`, with the import boundary in `src/taxonmech/extract.py`; `src/taxonmech/seed.py` faithfully copies the incomplete inventory. The configured original KGX paths could not be opened locally, so the precise upstream omission mechanism was not proved.

No unsupported strain-genome assertion, wrong identifier or invalid YAML was found. Taxonomy disagreements described below remain explicitly bounded to their sources.

## Recommended Edits

In a separately authorized curation change, inspect/refresh the pinned kg-microbe LPSN source and restore the supported CFBP 7437 type-designation assertion through the maintained transform. Preserve STM 4645 as a source lab designation under existing conventions; do not make it a CAFI-authorized genome-join key. If the missing edge is already present in the original transform, fix the demonstrated extraction defect instead. Regenerate the maintained inventory and seed through the documented workflow; never hand-edit this YAML or derived TSV to conceal the source gap.

Retain accession versions as supplied, including the unversioned BacDive/StrainInfo assertions. Keep D-10A separate from LMG 26462 and do not merge the Mesorhizobium comparators solely by designation. Leave `SEEDED` status and both history surfaces unchanged. No code, source or record correction was performed in this review.

## Follow-up Checks

Obtain the exact source transform used by `data/raw/MANIFEST.yaml`; confirm all type-designation edges for `lpsn:790620` before choosing a transform versus extractor fix. Add a targeted regression test proving the additional CFBP designation survives extraction/seeding without altering the existing type flag or transferring sequences between deposits. After actual curation, rerun both focused validators, inspect a canary for `NCBITaxon:1035067`, and run documented corpus reproduction, tests, history and publication gates.

Any proposed reconciliation of the similarly numbered Mesorhizobium taxa needs explicit primary isolate/sequence evidence and an authoritative taxonomy decision. No contact, paid research or upstream mutation is authorized by this report. No blocking follow-up is required for the existing Aminobacter identity or strain-genome links.

## Additional Notes

Preserved classification conflict: NCBI and the native BacDive top-level taxonomy use Phyllobacteriaceae; BacDive's nested LPSN taxonomy and public page use Bartonellaceae; the two GTDB rows use Rhizobiales/Rhizobiaceae. These are different source classifications, not permission to replace the carried NCBI lineage. The species-level GTDB match does not assert agreement of all higher ranks.

The 21 unrelated numeric-substring candidates were fully inspected: five Staphylococcus haemolyticus 51-18 rows (BV-BRC `1283.100`, `GCA_001227245.1`, `SAMEA1035067`, GOLD `Gp0140446`/`Go0134563`, ATB `ERR085186`/`ERZ3070513`); two Mycobacterium tuberculosis rows (`1773.20508`, `ERR1035067`, `SAMEA3558600`, `ERZ3501831`); four Phocaeicola vulgatus rows (`821.6666`, `GCA_040928505.1`/`GCF_040928505.1`, `SAMN41035067`); and ten community-level GOLD projects. The latter are seven Pinus/Suillus metatranscriptomes (`Gp0331467`, `Gp0331475`, `Gp0331540`, `Gp0331549`, `Gp0331558`, `Gp0331561`, `Gp0331564`), two Rhodopseudomonas/Escherichia cocultures (`Gp0344952`, `Gp0344953`) and one coral-community metatranscriptome (`Gp0344957`), all with empty GOLD organism fields. None supplies target strain evidence. The unrelated Staphylococcus ATB row has available FASTA/pipeline PASS but failing Sylph/HQ filters; it was not described as fully passing.

The original configured kg-microbe LPSN and LPSN-API files returned file-not-found errors; no claim is made that copies do not exist elsewhere. The live GTDB, GOLD, IMG and ENA detail pages were unavailable through the web tool; their identifiers were checked against complete source-native snapshots and independent linked primary evidence where available, not certified as live resolvable URLs. Collection pages also failed to render. StrainInfo's browser page was an application shell, but its public API succeeded. PMC's web page showed a browser challenge and MDPI returned 429; Europe PMC supplied the primary XML used above. The validation list's full species table was not inspected. These limitations do not erase the inspected source support and are not presented as successful live checks.

The source comparison diagnostics did not rewrite files. Reports remain separate from curation history and do not constitute a human `REVIEWED` promotion. Existing reports and the completed Eukaryota corpus were left untouched.
