# YAML Record Review: Tenuibacillus sp. YIM 94174

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/tenuibacillus_sp_yim_94174.yaml`
- Started UTC: 2026-10-06T09:13:46Z
- Finished UTC: 2026-10-06T09:17:44Z
- Verdict: pass with minor issues

## Target

Read the complete 54-line generated `TaxonRecord` for `NCBITaxon:1035045`, Tenuibacillus sp. YIM 94174. It asserts species rank, bacterial domain, parent `NCBITaxon:1508757`, ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` status, zero imported strains, one NCBI name attestation and one inline seed event. It has no synonym, nomenclature, mapping, xref, strain/genome relationship, literature assertion, discussion or causal graph.

`data/taxa/PATHS.tsv:14336` uniquely resolves the ID/stem; `curation/seed_scope.tsv:322148` supplies the NCBI-only inclusion rule dated 2026-09-13. A same-designation deposit under Filobacillus was inspected as comparison evidence, not as a second reviewed target.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/tenuibacillus_sp_yim_94174.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/tenuibacillus_sp_yim_94174.yaml --out /private/tmp/tyim94174-validation.tsv`: exit 0; one file, zero ERROR rows. Read the header-only TSV.
- Structured comparisons verified complete pinned identity, lineage, code, parent, unique scope/path, attestation and inline seed reason. No classified child was found.
- Exact-ID scans found no target row in seven other source inventories or the type-material, merged-ID and dropped tables. This does not erase the same-designation BacDive candidate filed under a different taxon.
- Initial ignored-inclusive searches found 33 rows; marker/deposit-expanded searches found 37. All complete rows were inspected and reconciled by address, with no unread candidate. Ignored-inclusive ID/name/slug searches found no prior target report or separate target history artifact.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just straininfo-query --bacdive 160598 --evidence`: exit 0; one own-deposit match, two typed StrainInfo references, no StrainInfo assemblies and no existing TaxonMech genome associations. This tests the comparison deposit, not a proven link to the target.
- Review guidance/checklist and relevant source-ownership, discussion and strain-generation rules were inspected. The pre-report tracked diff against HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8` exited 0.
- Not run: full-corpus `just verify-corpus`, `just qc`, tests, all-record validation, full provenance/history gates, rendering/site drift, README statistics, publication-size and vendored-file checks. No undocumented focused term/reference/history validator was invented. Inline history was checked; no separate target history artifact was available.
- `just validate-products` is not applicable without curator-added causal-graph nodes. This is not release certification.

## Identity and Grounding

Complete live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035045&retmode=xml) confirms the exact ID/name, species rank, bacterial division, parent 1508757 and code 11. [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035045) agrees and includes all ten ancestor IDs, including root.

The chain is root, cellular organisms, Bacteria, Bacillati, Bacillota, Bacilli, Caryophanales, Bacillaceae, Tenuibacillus and unclassified Tenuibacillus. Every pinned ancestor ID, label and rank matches the YAML; live taxonomy confirms the non-root chain. The inspected [NCBI genus tree](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=286800&lvl=&mode=tree) lists YIM 94174 separately from YIM 94141, YIM 94239 and named species.

NCBI's species rank is retained despite the isolate designation and no-rank parent. `EXACT` means exact NCBI concept grounding, not formal nomenclatural validation, reviewed status or equivalence to every culture using that designation.

There is a real cross-source designation/classification discrepancy: the deposit authorities associate YIM 94174 with DSM 25926 under Filobacillus, whereas NCBI's target and marker remain Tenuibacillus. Evidence currently supports keeping the sources distinct, not declaring either classification biologically correct or merging their taxon concepts.

## Evidence

1. **Pinned identity and audit.** Complete `data/raw/ncbitaxon_taxa.tsv:221856` supports the identity, rank, parent, code and 2026-09-13 snapshot, with empty synonym and retirement-target fields. Complete `data/catalog/ncbi_names-0005.jsonl.gz:31282` supplies the scientific name. The attestation counts one `NAME`. The inline event at 2026-09-13T17:54:04Z, `seed_from_sources` / `SEEDED_FROM_SOURCES`, matches the scope reason.

2. **Target marker.** Exact Nuccore search returned UID 333798079. Complete metadata, features and references for [JF792153.1](https://www.ncbi.nlm.nih.gov/nuccore/JF792153.1), excluding sequence bases, identify a 691-base 16S rRNA gene partial at both ends. Organism, strain YIM 94174 and `taxon:1035045` agree. C. Chen submitted it on 7 April 2011 through the Yunnan Institute of Microbiology / Yunnan University. Creation and update dates are 28 May 2011 and 26 August 2015. No culture-collection, BioSample or assembly accession is supplied in the inspected qualifiers. The associated Qijiaojing Lake bacteria/enzyme study is marked unpublished with no DOI or PMID. Its title is not isolate-specific phenotype evidence.

3. **Deposit authority.** Complete `data/bacdive/records.jsonl.gz:82834` and `data/raw/bacdive_strains.tsv:82835` identify BacDive 160598, cultures DSM 25926 and YIM 94174, and classification `NCBITaxon:2587215`, Filobacillus sp. The live [BacDive page](https://bacdive.dsmz.de/strain/160598) agrees and supplies a deposition history from the Yunnan institute. The live [DSMZ catalog](https://www.dsmz.de/collection/catalogue/details/culture/DSM-25926) independently lists DSM 25926, designation YIM 94174 and Filobacillus sp. Neither inspected source identifies JF792153 or establishes a sequence-backed link to NCBI 1035045. Their common designation makes this a relevant unresolved candidate, not an unrelated numeric false positive.

4. **StrainInfo source scope.** Complete `data/straininfo/records.jsonl.gz:301794` and the live [StrainInfo API](https://api.straininfo.dsmz.de/v2/data/strain/max/403905) support SI-ID 403905, its own SI-DP 911006, DSM 25926, BacDive 160598 and relation designation YIM 94174. The available nondeprecated DSM deposit has a nonerroneous relationship; both strain and deposit use the genus-level Filobacillus taxon 160794. [DataCite metadata](https://api.datacite.org/dois/10.60712/SI-ID403905.2) verifies the version-2 strain-record DOI. There is no sequence list. Link row `data/straininfo/strain_links.tsv:60030` and related-record rows 141072 and 141073 preserve the DSM match and source taxonomy. StrainInfo grouping does not transfer the Tenuibacillus marker to this deposit.

5. **Existing placement explains the count.** Culture inventory rows `data/raw/culture_collection_strains.tsv:74134` and `data/raw/culture_collection_strains.tsv:154854` both file DSM 25926/YIM 94174 under NCBI 2587215. Live [NCBI taxonomy for 2587215](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=2587215&retmode=xml) and Datasets confirm a separate Filobacillus sp. concept under unclassified Filobacillus, not a replacement for 1035045. The complete comparison file `data/taxa/bacteria/filobacillus_sp.yaml` already carries BacDive 160598 and the two StrainInfo references. `src/taxonmech/seed.py:487` gathers BacDive strains by taxon/subtree, so the target's zero strain count is reproducible; the culture is not missing from the repository. No independent verdict is assigned to the comparison record here.

6. **Genome and literature boundaries.** Exact NCBI assembly search `txid1035045[Organism:noexp]` returned zero with no-items/phrase-not-found diagnostics. The deposit query also has no genome association. These results do not prove universal genome absence. Name and marker searches supplied taxonomic/catalog context but no inspected publication establishing a reclassification or sequence-to-deposit equivalence. Search snippets were not used as evidence. No phenotype, medium requirement or habitat was transferred from DSM 25926 to this NCBI concept.

## Completeness

The represented NCBI identity and source count are supported, but the record does not expose the same-designation cross-source discrepancy. That non-blocking provenance gap is the minor finding below. It is not evidence that `strain_count: 0` should simply become one or that the target should be renamed or deprecated.

Ignored-inclusive compressed searches used `rg --no-ignore --hidden -z` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding manifests named `SOURCE.json`. Queries covered the unbounded taxon number, full label, slug and YIM94174 variants; expansion added JF792153, DSM 25926, BacDive 160598 and the StrainInfo IDs. The 37 complete rows comprise three target provenance rows, eight comparison-deposit context rows and twenty-six unrelated numeric matches.

Exact-ID scans covered BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories. No target type-material, merger or dropped entry was found. Prior-report/history searches included ignored files. Separate snapshot archives and all external databases were not exhaustively searched. iModulonDB was not applicable to this identity record. No sequence alignment, experimental reanalysis, genome comparison or exhaustive literature census was performed.

## Findings

Counts: 0 blocker, 0 major, 1 minor.

**Minor: Same-designation deposit/classification discrepancy is not represented as record-level provenance.** The target's NCBI-only record, including `strain_count` at line 40, has no discussion pointing to the DSM 25926/YIM 94174 candidate classified as Filobacillus by BacDive, DSMZ and StrainInfo. The comparison is supported by complete source rows and live deposit authorities, not a substring match. Without this context, a curator may mistake zero imported strains for no available deposit candidate, or join the two taxa solely by designation.

The target still exactly matches current NCBI and its marker. There is no verified erroneous taxon ID, missing eligible genome, or basis to declare NCBI and Filobacillus concepts equivalent, so this is not a blocker or major identity finding. The unresolved question is whether the deposit and submitted marker represent the same biological isolate and, if so, which authority records require correction.

Ownership: source identity/classification reconciliation belongs to the NCBI/DSMZ/BacDive authorities and their imported evidence, not a hand-edited lineage. A durable TaxonMech discussion would require a maintained seeder change and tests in `src/taxonmech/seed.py` and the existing test suite, or a separately approved curator-input design. The current documentation states that curator overlays are not yet implemented; an ignored-inclusive search of code, scripts, tests and curation found discussion schema/rendering support but no existing discussion ingestion path.

## Recommended Edits

1. Preserve this discrepancy as an unresolved, source-attributed curation question. Record both NCBI concepts, the partial marker, BacDive 160598, DSM 25926, YIM 94174 and the own StrainInfo deposit without asserting equivalence. This report is the current read-only audit artifact; do not patch the generated YAML to add a transient note.
2. Before any identity change, obtain explicit deposit/submission evidence connecting or distinguishing JF792153 and DSM 25926. An upstream correction, if warranted, should flow through the relevant pinned sources and `scripts/extract_source_inventory.py`; keep the NCBI lineage unchanged until the authority changes it.
3. If a record-level discussion is later authorized, implement it through a maintained generator/input path with preservation tests, as required by `docs/CURATION.md`. Do not add a one-off name-based strain join, silently copy the Filobacillus strain, alter the zero count, promote status, or invent a replacement relationship.

## Follow-up Checks

- Verify the deposit-to-marker chain and any authoritative reidentification before transferring culture or sequence evidence. Distinguish a source strain alias from taxon-concept equivalence.
- Recheck taxonomy/merged-ID status for both 1035045 and 2587215, and the current DSM/BacDive/StrainInfo deposit records.
- For any discussion implementation, test that both source assignments survive generation without changing lineage, duplicating the BacDive strain or introducing a genome link.
- After authorized maintained-input/generator changes, run the documented dry run and single-record canary, both focused validators, then full `just verify-corpus` and `just qc` before release.

## Additional Notes

The DSMZ page initially failed retrieval but was subsequently read through BacDive's catalog link. Its summary calls the culture a type strain, whereas pinned BacDive and live StrainInfo type flags are false. The DSMZ page also has an outbound-link label mentioning Paracoccus tegillarcae despite its Filobacillus identity fields. These source-internal inconsistencies were not silently used to infer a target type flag, rename the record or establish deposit-to-marker identity. The catalog's direct designation and deposition history, corroborated by BacDive and StrainInfo, support only the bounded candidate relationship described above.

The twenty-six unrelated numeric matches were inspected in full:

- Six Staphylococcus haemolyticus rows match sample SAMEA1035045: BV-BRC `bvbrc-0001.jsonl.gz:18438` (taxon 1283, genome 1283.182, strain 51-15); GOLD project row 87387 (Gp0140445, Go0134562); GTDB `gtdb_genomes-0004.jsonl.gz:18113`; RefSeq `ncbi_refseq-0000.jsonl.gz:38589`; GenBank `ncbi_genbank-0000.jsonl.gz:45807`; and AllTheBacteria row 66025. They preserve the explicit GCA/GCF_001237405.1 pair. GenBank/BV-BRC/GOLD give PRJEB2705; RefSeq/GTDB give PRJNA224116. GTDB retains its own higher classification. ATB supplies ERR085230 and ERZ3070489, species agreement and passing pipeline/HQ/Sylph filters.
- Two Mycobacterium tuberculosis rows concern strain ERR1035045: BV-BRC `bvbrc-0006.jsonl.gz:8501` gives taxon 1773 and genome 1773.20487; AllTheBacteria row 569515 gives SAMEA3558578 and ERZ3501746, with species agreement and passing filters.
- Four Bacteroides thetaiotaomicron rows concern taxon 818, strain 2201st1_E11_2201SCRN_220225, SAMN41035045 and the explicit GCA/GCF_040928925.1 pair: BV-BRC `bvbrc-0027.jsonl.gz:21487` (genome 818.3301), GenBank `ncbi_genbank-0037.jsonl.gz:21050`, RefSeq `ncbi_refseq-0006.jsonl.gz:20160` and GTDB `gtdb_genomes-0009.jsonl.gz:17632`. GenBank/BV-BRC give PRJNA1093465; RefSeq/GTDB give PRJNA224116, with species agreement.
- GOLD analysis `data/gold/analyses.jsonl.gz:437368` matches IMG ID 8103504592. It is Ga0653394, project Gp0811466, Salmonella enterica enterica sv. Onireke 441460, with empty organism GOLD ID and explicit GCA_007152225.1 / AAHDVM000000000 fields. It supplies no target organism/project/analysis chain.
- GenBank `ncbi_genbank-0037.jsonl.gz:25640` matches accession GCA_041035045.1. It identifies Klebsiella pneumoniae, taxon 573, strain zj02058, SAMN37542648 and PRJNA1021041, without a listed RefSeq partner and with a large-multi-isolate-project exclusion.
- Two Vibrio parahaemolyticus rows match the GCA/GCF_051035045.1 accession pair: GenBank `ncbi_genbank-0047.jsonl.gz:6712` and historical RefSeq `ncbi_refseq_historical-0001.jsonl.gz:38982`. They identify taxon 670, strain VP20063 and SAMN46338800. GenBank gives PRJNA1213288 and latest status; RefSeq gives PRJNA224116 and suppressed status, with not-live date 2025-06-27. Both carry the large-multi-isolate-project exclusion. A historical paired accession is not evidence of a current target genome.

Ten GOLD project rows match longer BioSample IDs. Each is a Pinaceae seedling/Suillus metatranscriptome with an empty organism GOLD ID, not a target isolate genome.

| Row in `data/gold/projects.jsonl.gz` | GOLD project | BioProject | BioSample | Project suffix | Location in title |
| --- | --- | --- | --- | --- | --- |
| 228172 | Gp0333777 | PRJNA502018 | SAMN10350450 | Same/Pstro_rep1 | Pennsylvania, United States |
| 228177 | Gp0333782 | PRJNA502023 | SAMN10350451 | Same/Prad_rep3 | Pennsylvania, United States |
| 228182 | Gp0333787 | PRJNA502028 | SAMN10350452 | Same/Pmen_rep2 | Pennsylvania, United States |
| 228189 | Gp0333794 | PRJNA502035 | SAMN10350453 | Scot/Psyl_rep3 | North Carolina, United States |
| 228200 | Gp0333805 | PRJNA502046 | SAMN10350454 | Scot/Pmen_rep2 | North Carolina, United States |
| 228210 | Gp0333815 | PRJNA502056 | SAMN10350455 | Sgre/Pstro_rep3 | Minnesota, United States |
| 228211 | Gp0333816 | PRJNA502057 | SAMN10350456 | Sgre/Prad_rep1 | Minnesota, United States |
| 228226 | Gp0333831 | PRJNA502072 | SAMN10350457 | Slak/Pstro_rep1 | Colorado, United States |
| 228231 | Gp0333836 | PRJNA502198 | SAMN10350458 | Slak/Prad_rep3 | Colorado, United States |
| 228234 | Gp0333839 | PRJNA502201 | SAMN10350459 | Slak/Pmen_rep3 | Colorado, United States |

Only this new timestamped report was written for the target. No record, source inventory, history, prior report, generated product or Eukaryota review was changed. No taxonomic reconciliation was implemented. External reads were public and unpaid; no contacts, commits, GitHub mutations, provider-credit jobs or lifecycle promotions occurred.
