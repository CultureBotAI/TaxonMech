# YAML Record Review: Tenuibacillus halotolerans

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/tenuibacillus_halotolerans.yaml`
- Started UTC: 2026-10-06T08:59:24Z
- Finished UTC: 2026-10-06T09:07:39Z
- Verdict: pass

## Target

Read the complete 287-line generated `TaxonRecord` for `NCBITaxon:1035043`, Tenuibacillus halotolerans. It carries species rank, bacterial domain, parent `NCBITaxon:286800`, nine root-first ancestors, genetic code 11, `EXACT` grounding and `SEEDED` status. Its enrichment consists of one LPSN name, three related synonyms, one LPSN xref, one BacDive strain with four culture identifiers, two NCBI assembly records, twelve typed related records, six source attestations and one inline seed event.

`data/taxa/PATHS.tsv:14334` uniquely resolves the ID/stem. `curation/seed_scope.tsv:10797` records inclusion on 2026-09-12 under the six-source attestation rule. Strain, deposit, organism-reference and assembly counts represent different entities.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/tenuibacillus_halotolerans.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/tenuibacillus_halotolerans.yaml --out /private/tmp/thalo-validation.tsv`: exit 0; one file, zero ERROR rows. Read the header-only diagnostic TSV.
- Read-only structured comparisons verified the complete pinned identity, lineage, parent, code, synonyms, unique path/scope, attestations and inline seed reason. No classified child was found in the backbone.
- Exact source comparisons verified the full LPSN object, BacDive strain/culture list, type-designation intersection and all source/count/unit triples. Whole-object multiset comparison reproduced both assemblies, zero genome records and all twelve related records, including nested StrainInfo evidence. Culture normalization validated complete CCTCC, DSM, KCTC and YIM identifiers through the repository's CAFI-aware helpers.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just straininfo-query --bacdive 22932 --evidence`: exit 0; one deposit match, two StrainInfo references, no StrainInfo assemblies, and two separately labeled existing TaxonMech assembly associations.
- Initial and expanded ignored-inclusive compressed-source searches returned the same 73 row addresses. Complete TSV/native rows were read for every address; reconciliation found no unread or extra row. Ignored-inclusive ID/name/slug searches found no prior target report or separate target history artifact.
- The review skill, curation boundaries, checklist and documented validator recipes were inspected. The pre-report tracked-file diff against HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8` exited 0.
- Not run: full-corpus `just verify-corpus`, `just qc`, tests, all-record strict validation, full provenance/history gates, site/render drift, README statistics, publication-size and vendored-file checks. No undocumented focused term/reference/history validator was invented. Inline history was checked; no separate target history artifact was available to validate.
- `just validate-products` is not applicable without curator-added causal-graph nodes. This report does not certify corpus reproducibility or release readiness.

## Identity and Grounding

Complete live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035043&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035043) agree on the identifier, name, species rank, bacterial placement, parent and code. The root-first chain is root, cellular organisms, Bacteria, Bacillati, Bacillota, Bacilli, Caryophanales, Bacillaceae and Tenuibacillus. Every pinned ancestor ID, label and rank agrees with the YAML; live taxonomy confirms the non-root chain and Datasets includes root.

The three NCBI names remain related synonyms: the quoted 2013 authority form, the 2021 authority form and Tenuibacillus sp. YIM 94025. They are not evidence for three species. Exact grounding denotes the NCBI concept, not human review. The record remains `SEEDED`.

The [LPSN authority page](https://lpsn.dsmz.de/species/tenuibacillus-halotolerans) resolves record 18916 and supports the 2021 authority, valid ICNP publication and correct-name status. Its type designations are CCTCC AB 2012860, KCTC 33046 and YIM 94025. The YAML's LPSN type list contains the inventory-supported KCTC designation only; all three occur in the BacDive culture list, along with DSM 25925. This is a nonexhaustive LPSN designation projection, not a wrong type-strain match.

## Evidence

1. **Pinned taxonomy and status.** `data/raw/ncbitaxon_taxa.tsv:221854` supports the complete identity and 2026-09-13 snapshot; native name rows `data/catalog/ncbi_names-0005.jsonl.gz:31277-31280` preserve the scientific name and three synonyms. Seven type-material rows at `data/raw/ncbi_type_material.tsv:1794-1800` supply spelling variants for CCTCC AB 2012860, KCTC 33046 and YIM 94025. Exact-ID scans found no merged-ID or dropped entry. The inline event at 2026-09-13T17:54:04Z, curator `seed_from_sources`, action `SEEDED_FROM_SOURCES`, agrees with the six-source scope reason.

2. **Nomenclature and publications.** `data/raw/lpsn_names.tsv:3525` reproduces the full nomenclature object, xref and LPSN close-match attestation. The complete [PubMed 22941247](https://pubmed.ncbi.nlm.nih.gov/22941247/) bibliography and abstract verify DOI 10.1007/s10482-012-9802-3, Gao and colleagues' 2013 species description, and the YIM/CCTCC/KCTC type-strain equivalence. DOI [10.1099/ijsem.0.004688](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijsem.0.004688) resolves to Oren and Garrity's Validation List 198, published in 2021; publisher metadata and LPSN's explicit citation were inspected. The 2013 effective description and 2021 nomenclatural validation are distinct events, not an authority-year inconsistency. The complete effective-paper text and validation-list table were not retrieved; no uninspected experimental result is asserted here.

3. **BacDive identity.** `data/raw/bacdive_strains.tsv:22738`, complete native `data/bacdive/records.jsonl.gz:22737` and the [BacDive 22932 page](https://bacdive.dsmz.de/strain/22932) support the taxon association, four deposit identifiers and type strain. Four culture inventory rows at 14626, 74133, 118386 and 154853 were read. The type flag follows the exact KCTC intersection with LPSN, not name similarity. The native BacDive general taxonomy retains older 2013/Firmicutes/Bacillales wording while its LPSN block supplies the newer name; the YAML's independently sourced NCBI lineage is not overwritten. The inspected web page's cited version and pinned native version differ, so they were not treated as the same snapshot.

4. **NCBI assemblies and related resources.** Complete inventory rows `data/raw/strain_assemblies.tsv:107591-107592` and native GenBank/RefSeq rows `data/catalog/ncbi_genbank-0055.jsonl.gz:34117` and `data/catalog/ncbi_refseq-0009.jsonl.gz:12377` support GCA_060125485.1 and GCF_060125485.1. The whole source value `strain=KCTC 33046` in `infraspecific_name` matches the registered deposit. Live [NCBI assembly summary 35115651](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=assembly&id=35115651&retmode=json) explicitly pairs the two accessions as identical and confirms taxon 1035043, ASM6012548v1, Contig level, eleven contigs, type material and sample SAMN51215260. GenBank project PRJNA1321507 and RefSeq project PRJNA224116 remain separately attributed. The four associated project/sample rows preserve those source paths. The live reference-genome category differs from the older snapshot value, but that category is not asserted in the YAML. No assembly equivalence was inferred by changing an accession prefix or sharing a sample.

5. **GOLD source paths and count boundary.** Complete native organism rows `data/gold/organisms.jsonl.gz:445802-445804` support Go0615088/YIM 94025, Go0615089/KCTC 33046 and Go0615091/CCTCC AB 2012860. Both the culture-collection and strain fields independently carry the matching complete identifier, producing six provenance-distinct related-record entries. They are GOLD organism references, not six genomes. The GOLD attestation of four organisms exactly reproduces `data/raw/gold_organisms.tsv:474`; it is not a recount of these three native workbook rows. Inspection of `src/taxonmech/extract.py` confirms that this count comes from the older transformed GOLD subclass inventory. The configured upstream transformed inputs are unavailable, so the four source organism IDs could not be independently reconstructed. This is a verification limit, not evidence to replace four with three.

6. **StrainInfo deposit evidence.** Complete native row `data/straininfo/records.jsonl.gz:303871`, link row 80126, related rows 192584-192585 and the live [StrainInfo API record](https://api.straininfo.dsmz.de/v2/data/strain/max/405982) support SI-ID 405982, its own SI-DP 913248, DSM 25925, BacDive 22932, published-online strain status and available deposit status. [DataCite's DOI record](https://api.datacite.org/dois/10.60712/SI-ID405982.3) verifies version 3 of this dataset. No sequence list is supplied for the own deposit. The API's aggregate `strain.typeStrain: false` conflicts with its own deposit's `typeStrain: true`; both scopes are preserved here. The YAML does not assert the aggregate StrainInfo flag, and LPSN/BacDive independently support its type flag. Existing NCBI associations must not be recast as StrainInfo-provided assemblies.

7. **Markers stay outside genome counts.** LPSN cites unversioned JF792128, which is correctly preserved. Complete sequence metadata/features/references identify [JF792128.1](https://www.ncbi.nlm.nih.gov/nuccore/JF792128.1) as a 630-base partial 16S record for type strain YIM 94025 and this taxon. Other inspected rRNA records are JQ995150.1, 1,539 bases for YIM 94025; NR_132611.1, 1,539 bases explicitly derived identically from JQ995150; KY457283.1, 541 bases for different strain YIM 98197; and PQ326972.1, 1,476 bases for different strain B4. The latter two do not become links for BacDive 22932. Exact Nuccore search found eighteen records; the five rRNA records were fully inspected as metadata, not all eighteen records or sequence bases. The two longer type-strain markers cite PMID 22941247. No marker was counted as a whole genome or assigned to the DSM deposit through a StrainInfo grouping.

8. **Other attestations.** NCBI and LPSN each count one name, BacDive one strain, MediaDive one medium, GOLD four transformed organism records and BactoTraits one inventory assertion. `data/raw/mediadive_taxa.tsv:117` names medium 1467; the live [T5 medium strain table](https://mediadive.dsmz.de/strains/medium/1467) explicitly lists Tenuibacillus halotolerans DSM 25925. The page's long autocomplete list was not mistaken for associated strains. `data/raw/bactotraits_taxa.tsv:88` supports the assertion count, not a specific phenotype. Native SeqCode name 21154 and its [API record](https://api.seqco.de/v1/names/21154.json) corroborate name/type context without becoming a required attestation or overriding NCBI hierarchy.

## Completeness

No consequential omission was established in the represented seeded claims. There is one imported BacDive strain, not four strains because it has four deposit identifiers. No eligible additional genome record or own-deposit StrainInfo sequence was found within the searched inventories. Exact GTDB and Madin mapping inventories have no target entry; those optional fields appropriately remain absent.

The ignored-inclusive compressed search used `rg --no-ignore --hidden -z` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding manifests named `SOURCE.json`. Queries covered the unbounded taxon number, name, slug and culture variants; expansion included BacDive, assembly, sample, GOLD, StrainInfo and marker identifiers. All 73 candidates were read: 46 target/provenance rows and 27 unrelated matches. Separate snapshot archives and all external resources were not exhaustively searched. No eligible GOLD project/analysis chain for these three organisms emerged from this bounded search.

The missing upstream KGX files were checked at the configured kg-microbe path, with an ignored-inclusive filename search. Notebook merged/pivot TSV archives exist but are not the manifest-pinned source-specific inputs. The attempted source hash/row audit stopped at the missing LPSN nodes file; no upstream hash verification is claimed. Committed inventories remain available and sufficient for the comparisons actually performed.

The single imported LPSN type designation is supported but not a complete transcription of the live authority's three designations. GOLD's old count cannot be certified against unavailable transformed rows. Neither limitation hides an established false identifier or lost strain/genome relationship. No exhaustive literature census, sequence alignment, experimental reanalysis or genome-content comparison was performed. iModulonDB was not applicable to this identity/nomenclature/linkage record; source counts and unrelated transcriptomes do not constitute expression evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Inspected evidence supports the represented identity, lineage, nomenclature, type strain, source-owned links and inventory count semantics. The pass is bounded by the unavailable transformed-input recount, publication full-text limitations and skipped corpus gates described above. It is not a claim that all current source records or type-designation aliases have been imported.

## Recommended Edits

None required for the supported record. Preserve the generated YAML, accession versions, unversioned LPSN marker, distinct source evidence and `SEEDED` status. Do not replace the GOLD inventory count using a different catalog, collapse source-specific project/sample evidence, transfer links from other strains, or treat source references as genomes.

Any future LPSN designation refresh or GOLD count reconciliation belongs in the configured upstream transforms and `src/taxonmech/extract.py` / `scripts/extract_source_inventory.py`, followed by the documented generation path in `src/taxonmech/seed.py` / `scripts/seed_from_sources.py`. Strain-link changes belong in `src/taxonmech/genome_sources.py`; StrainInfo changes require its own pinned deposit/sequence evidence and overlay workflow. Do not patch generated records or old reports to hide a source difference.

## Follow-up Checks

- At an authorized source refresh, obtain the manifest-matching GOLD/LPSN inputs, verify their hashes and reconstruct the old count/type projection before comparing with newer native catalogs.
- Preserve the aggregate/deposit StrainInfo type-flag conflict and require an explicit same-SI-DP sequence link before importing any new StrainInfo sequence.
- Recheck assembly pairing, complete CAFI identifiers, source-owned BioProject/BioSample relationships and current taxonomy. Do not infer cross-database genome equivalence from taxonomy or sample sharing.
- Obtain and inspect publication full text before making new claims beyond the abstract, authority status and bibliographic identity verified here.
- After authorized input/generator changes, use the documented dry run and single-record canary, both focused validators, then full `just verify-corpus` and `just qc` before release.

## Additional Notes

All twenty-seven rejected numeric matches were inspected as complete rows:

- Six Staphylococcus haemolyticus rows concern taxon 1283, strain 131974, sample SAMEA1035043 and the explicit GCA/GCF_001233205.1 pair: BV-BRC row `bvbrc-0001.jsonl.gz:18204` (genome 1283.144), GOLD project row 87419 (Gp0140477, Go0134594), GTDB row `gtdb_genomes-0015.jsonl.gz:10548`, RefSeq row `ncbi_refseq-0000.jsonl.gz:38386`, GenBank row `ncbi_genbank-0000.jsonl.gz:45598` and AllTheBacteria row 66023. GenBank/BV-BRC/GOLD give PRJEB2705; RefSeq/GTDB give PRJNA224116. ATB supplies ERR085278 and ERZ3070473 with passing filters.
- Two Mycobacterium tuberculosis rows concern taxon 1773 and run-designated strain ERR1035043: BV-BRC `bvbrc-0006.jsonl.gz:8496` (genome 1773.20482) and AllTheBacteria row 569513 (SAMEA3558576, ERZ3501731, passing filters).
- Four Escherichia coli rows match BioProject PRJNA1035043, not taxon 1035043. BV-BRC `bvbrc-0022.jsonl.gz:21348-21349` and GenBank `ncbi_genbank-0036.jsonl.gz:46660-46661` identify taxon 562: strain 56, genome 562.157000, GCA_040407945.1, SAMN38080761; and strain 410, genome 562.157001, GCA_040407955.1, SAMN38080766. Explicit paired-accession fields were retained, not inferred. The unrelated citation field was not treated as a target publication.
- Four Bacteroides rows concern taxon 3143218, strain 2201st1_D9_2201SCRN_220225, SAMN41035043 and GCA/GCF_040928965.1: BV-BRC `bvbrc-0019.jsonl.gz:2207` (genome 3143218.3), GenBank `ncbi_genbank-0037.jsonl.gz:21052`, RefSeq `ncbi_refseq-0006.jsonl.gz:20162` and GTDB `gtdb_genomes-0005.jsonl.gz:30971`. GenBank/BV-BRC give PRJNA1093465; RefSeq/GTDB give PRJNA224116. NCBI's unnamed species and GTDB's Bacteroides stercoris classification remain distinct.
- One GTDB row, `gtdb_genomes-0002.jsonl.gz:25523`, matches N50 1035043. It is GB_GCA_963758035.1, MAG MFD00964.bin.1.57, SAMEA114809453 and PRJEB58634. NCBI taxon 3039803 is an uncultured Actinomycetota bacterium; GTDB assigns its own Palsa-465 species classification. A length statistic is not a taxon match.

Ten remaining rows in `data/gold/projects.jsonl.gz` are Pinaceae seedling/Suillus metatranscriptome projects with empty organism GOLD IDs. They match longer BioSample accessions, not this bacterial species. Their separate source relationships are retained below; no Eukaryota record or report was changed.

| Row | GOLD project | BioProject | BioSample | Project suffix | Location in title |
| --- | --- | --- | --- | --- | --- |
| 228299 | Gp0333904 | PRJNA501959 | SAMN10350432 | Sgla/Pstro_rep2 | Minnesota, United States |
| 228303 | Gp0333908 | PRJNA501963 | SAMN10350433 | Sgla/Prad_rep3 | Minnesota, United States |
| 228311 | Gp0333916 | PRJNA501971 | SAMN10350434 | Sgla/Pmari_rep2 | Minnesota, United States |
| 228319 | Gp0333924 | PRJNA501979 | SAMN10350435 | Ssub/Prad_rep1 | New York, United States |
| 228331 | Gp0333936 | PRJNA501992 | SAMN10350436 | Spla/Psyl_rep1 | New York, United States |
| 228368 | Gp0333973 | PRJNA501921 | SAMN10350437 | Spun/Pstro_ES_rep2 | Michigan, United States |
| 228372 | Gp0333977 | PRJNA501925 | SAMN10350430 | Sfus/Pstro_ES_rep3 | California, United States |
| 228374 | Gp0333979 | PRJNA501927 | SAMN10350431 | Sfus/Prad_ES_rep2 | California, United States |
| 228377 | Gp0333982 | PRJNA501930 | SAMN10350438 | Ssub/Psyl_ES_rep2 | New York, United States |
| 228381 | Gp0333986 | PRJNA501914 | SAMN10350439 | Ssub/Pstro_ES_rep3 | New York, United States |

Only this new timestamped report was written for the target. Records, source inventories, scope, history, prior reports, generated products and Eukaryota reviews remain unchanged. External reads were public and unpaid. No commits, GitHub mutations, contacts, provider-credit jobs or lifecycle promotions occurred.
