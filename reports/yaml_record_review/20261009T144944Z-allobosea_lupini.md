# YAML Record Review: Allobosea lupini

- Repository: TaxonMech
- Record: `data/taxa/bacteria/allobosea_lupini.yaml`
- Started UTC: 2026-10-09T14:39:05Z
- Finished UTC: 2026-10-09T14:49:44Z
- Verdict: needs curation

## Target

Reviewed the complete 1,056-line generated `TaxonRecord`, `NCBITaxon:1036779`, a bacterial species with `grounding_status: EXACT` and `mapping_status: SEEDED`. Its parent is `NCBITaxon:85413`, Allobosea. The record lists one BacDive type strain, R-45681, with three culture deposits; 13 assembly assertions, 11 genome-record assertions, and 40 related-record assertions. These are source assertions, not counts of distinct biological genomes.

Baseline HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Target SHA-256 before and after inspection: `d928a3ec36817b9615dfbb99765d00e80ecd39b721880dba3b7d70b0fca3125f`.

The species identity is supported. One strain-to-sequence association is not: `KF730777` is attributed to LMG 26383 in the generated record, although its primary nucleotide record identifies isolate JG24. This review does not edit the YAML, inventories, source snapshots, history, pages, or status.

## Validation

Commands used the writable temporary uv cache and offline dependencies:

```bash
UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/allobosea_lupini.yaml
UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline python scripts/validate_strict.py data/taxa/bacteria/allobosea_lupini.yaml --workers 1 --out /private/tmp/taxonmech-alupini-20261009-validation.tsv
```

- Open-mode schema validation: exit 0, no issues.
- Strict validation: exit 0; one file scanned, zero error rows; output TSV contains only its header.
- Read-only full-object comparisons against the target's own raw rows, StrainInfo `_link` output, and ATB sample evidence: all 13 assembly, 11 genome-record, and 40 related-record assertions match, including nested evidence. All eight ATB sample assertions also occur among the related records. This verifies faithful generation, not biological correctness of the source.
- Identity, lineage, nomenclature, accessions, and source references were inspected against the authority records and native rows described below.
- `validate-products`: not applicable to this target; it has no causal graph or ontology-grounded nodes. `conf/id_label_targets.yaml` excludes ordinary record identity and strain surfaces from this OAK gate.
- History: inline seed event inspected. No target-specific external history filename or matching history content was found in ignored-inclusive searches. No review event was created, as required by the read-only review skill.
- Not run: full-corpus `verify-corpus`, `provenance-check`, render/docs checks, full test suite, and `qc`. There is no claim that the focused comparisons replace those repository-wide gates.
- One coverage-command attempt using uv's default cache failed on a sandboxed cache path; rerunning with the temporary cache succeeded. This was not a record-validation failure.

## Identity and Grounding

The pinned backbone row `data/raw/ncbitaxon_taxa.tsv:222619`, fresh NCBI Taxonomy XML, and NCBI Datasets agree on species ID 1036779, current label Allobosea lupini, parent 85413, bacterial domain, and genetic code 11. The nine root-first ancestors match: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Alphaproteobacteria, Hyphomicrobiales, Alloboseaceae, and Allobosea. Source: [NCBI taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1036779).

Five own NCBI names at `data/catalog/ncbi_names-0005.jsonl.gz:32188` onward support the scientific name, two authorities, Bosea lupini synonym, and included Bosea sp. LMG 26383 name. Authority and includes names remain related synonyms, not exact identities. The separate LPSN synonym is retained with its own provenance.

`lpsn:70770` denotes the current legitimate, validly published correct name; `lpsn:790218` is the former Bosea lupini combination, validly published but illegitimate and no longer the correct name. Both share the type material. The current authority, three deposit identifiers, FR774992, DOI 10.1099/ijsem.0.007072, DOI 10.1099/ijsem.0.007121, and PMID 41649870 agree with inspected LPSN and bibliographic authority records. Sources: [current LPSN name](https://lpsn.dsmz.de/species/allobosea-lupini), [former LPSN name](https://lpsn.dsmz.de/species/bosea-lupini), [replacement-name paper](https://pubmed.ncbi.nlm.nih.gov/41649870/), [notification DOI metadata](https://api.crossref.org/works/10.1099/ijsem.0.007121).

The `skos:closeMatch` to `GTDB:s__Allobosea_lupini` is supported by the pinned mapping and six complete native GTDB rows. The count is the GTDB cluster size, not six assemblies from R-45681. Its members are GCF_900109525.1, GCF_002831785.1, GCF_037120455.1, GCF_037402175.1, GCF_037483275.1, and GCA_051861005.1. Four other NCBI mapping rows share this cluster; exact equivalence to one NCBI species is not asserted. Only the representative GCF_900109525.1 carries this record's eligible culture identifiers. The native GTDB higher classification differs from NCBI's, and the native type-material designation is `na`; neither is silently overwritten. The live GTDB page was inaccessible, so this check rests on the inspected pinned native catalog, not a claimed live census.

## Evidence

**Type strain and deposits.** BacDive 1792 identifies R-45681 as the type strain and supplies CCUG 61248, DSM 26673, and LMG 26383. All nine own NCBI type-material rows were inspected. The original description equates LMG 26383, CCUG 61248, and R-45681; current LPSN and BacDive additionally support DSM 26673. CAFI normalization accepts all three complete deposit identifiers but not the bare research designation. Sources: [BacDive 1792](https://bacdive.dsmz.de/strain/1792), [original description](https://pubmed.ncbi.nlm.nih.gov/22155761/).

**Assemblies and genome records.** The own BacDive, BV-BRC, GOLD, GTDB, NCBI assembly-summary, and StrainInfo rows were read in full. GCA_900109525.1 and GCF_900109525.1 are the paired assemblies for the compound strain designation containing LMG 26383 and CCUG 61248. Fresh NCBI Datasets confirms taxon 1036779, SAMN04515666, a 24-contig assembly of 6,128,076 bases, and the IMG-derived assembly name. The unversioned GCA accession from BacDive and StrainInfo is preserved as supplied, not silently rewritten. Source: [NCBI assembly report](https://api.ncbi.nlm.nih.gov/datasets/v2alpha/genome/accession/GCF_900109525.1/dataset_report).

BV-BRC `patric:1036779.5` has the matching compound strain field and DSM 26673 culture field. GOLD analysis Ga0074804 connects through project Gp0116466 to organism Go0044040, carrying IMG 2634166302, GCA_900109525.1, SAMN04515666, and PRJNA311480. The analysis has no direct organism field; the project-to-organism relationship was checked rather than invented. Go0615890 independently supplies the LMG 26383 organism references. Go0615889 has only R-45681 and no eligible culture identifier, so its species-level organism count does not authorize a new strain link.

The related projects retain their actual source contexts: PRJEB16864 from BV-BRC/GenBank, PRJNA224116 from the pinned RefSeq/GTDB metadata, and PRJNA311480 from GOLD/BioSample. A current Datasets response displays PRJEB16864 for the paired assembly; it does not invalidate the separately sourced project assertions.

**ATB.** `atb.assembly:202505.SAMN04515666` retains dataset 661k, run SRR4181646, analysis ERZ26861674, both PASS filters, its SeqKit identifier, and the exact download/archive fields in the native metadata. Eight source-specific sample assertions provide the strain connection. Fresh ENA XML links the same analysis to SAMN04515666 and SRR4181646; the run title identifies DSM 26673. This is an independently assembled ATB genome record, not proof of sequence identity with the NCBI assembly. FASTA/archive payloads and their checksums were not independently downloaded or recomputed. Sources: [ENA analysis](https://www.ebi.ac.uk/ena/browser/api/xml/ERZ26861674), [ENA run](https://www.ebi.ac.uk/ena/browser/api/xml/SRR4181646).

**StrainInfo.** Native `data/straininfo/records.jsonl.gz:286716` and a fresh [StrainInfo API response](https://api.straininfo.dsmz.de/v2/data/strain/max/371081) agree on strain 371081, DOI version 3, BacDive 1792, and three available, non-erroneous deposits: 865460/LMG 26383, 873365/CCUG 61248, and 905443/DSM 26673. The genome sequence explicitly names LMG and CCUG deposits only. Its two assembly assertions and all deposit/strain references preserve that scope. DataCite confirms the DOI and dataset version. Source: [StrainInfo DOI](https://doi.org/10.60712/SI-ID371081.3).

All eight nucleotide authority records were read, including source qualifiers, references, features, version, actual length, alphabet, and sequence digest:

| Accession/version | Length | Primary-record identity and interpretation |
| --- | ---: | --- |
| FR774992.1 | 1444 | Original 16S sequence, R-45681 = 1121, Lupinus polyphyllus root nodules, NCBI 946785. LPSN explicitly uses it for the named species. |
| FR871207.1 | 505 | atpD, type strain LMG 26383, taxon 1036779. |
| FR871219.1 | 461 | recA, type strain LMG 26383, taxon 1036779. |
| FR871227.1 | 673 | gyrB, type strain LMG 26383, taxon 1036779. |
| FR871235.3 | 371 | rpoB, type strain LMG 26383, taxon 1036779; the unversioned YAML accession resolves to version 3. |
| FR871243.1 | 285 | dnaK, type strain LMG 26383, taxon 1036779. |
| FR872720.1 | 317 | Deposited as nifH for LMG 26383; functional interpretation is disputed by the original paper's nonspecific-PCR result. |
| KF730777.1 | 1425 | 16S sequence from isolate JG24, soil; primary record does not identify R-45681 or any of its deposits. See M1. |

The record preserves FR872720's source description as a related-sequence name. It does not assert nitrogen fixation, a causal mechanism, or a confirmed functional nifH locus. The original paper reports nonspecific nifH PCR products; therefore the sequence annotation cannot be promoted to such a claim. Sources: [FR872720](https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=FR872720&db=nuccore&report=genbank&retmode=text), [original paper abstract](https://pubmed.ncbi.nlm.nih.gov/22155761/).

**Attestations.** Every count/unit matches the own inventory rows: NCBI 1 NAME, LPSN 1 NAME, GTDB 6 GENOME, BacDive 1 STRAIN, MediaDive 1 MEDIUM, GOLD 3 ORGANISM, Madin 5 TRAIT_ASSERTION, and BactoTraits 6 TRAIT_ASSERTION. The MediaDive inventory names medium 1; BacDive's page corroborates nutrient agar. Counts are not summed into organism-wide phenotypes. The underlying Madin/BactoTraits KGX edges were not independently replayed: an ignored-independent `find` found no edge files in the configured kg-microbe `data/` root. This limitation does not mean those sources lack evidence globally.

## Completeness

The complete own inventory and source search used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`, covering ignored and compressed files. Initial searches used taxon ID, both species names, R-45681, and all three deposits; all 131 candidate rows were inspected in full. Expanded searches covered the eight nucleotide accessions, assembly, IMG/GOLD identifiers, sample, run, analysis, and JG24. Three new JG24 substring hits identify Micrococcus sp. NBRAJG24, not evidence equating this isolate to R-45681. Complete SOURCE metadata and target history filenames were also examined.

No target-specific decision resolving KF730777's isolate conflict was found in ignored-inclusive searches of `conf`, `curation`, `src`, `tests`, and `history`. This is a bounded repository finding, not a statement that no external synonym could exist.

Other catalog genomes are correctly not attached merely because they share a species label: BV-BRC FBZP-16, the CCNWLW174/CCNWLY174/CCNWYY174 GTDB members, and the CCAP1427_2_bin-010 metagenome-derived assembly lack this strain's eligible deposit match. The two other ATB species candidates, SAMEA5613776 and SAMN44683077, lack the inspected own-strain sample chain. Their presence does not change the BacDive strain count.

The absent direct NCBI_ASSEMBLY assertions have a reproducible parser explanation: `strain_tokens` retains the compound value `LMG 26383,CCUG 61248,R- 45681` as one token, which whole-identifier normalization rejects. Both assembly accessions are already represented through other matching sources. A future parser improvement belongs in `src/taxonmech/ncbi_assemblies.py` with tests, not a fabricated direct NCBI assertion in this YAML.

The record has no phenotype claims, causal graph, expression dataset, or experimental mechanism requiring invented content. The structured `kg-microbe-sources imodulondb datasets` command returned 28 datasets, none for Allobosea/Bosea. iModulonDB is not applicable to this target; lack of coverage is not negative functional evidence.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

**M1 - Major: unsupported attribution of KF730777 to type strain LMG 26383.** At YAML line 871, the related sequence is nested under BacDive 1792 and explicitly matched to `kgmicrobe.strain:LMG-26383`, with `sequence_deposit_id: straininfo.deposit:865460`. The primary [KF730777.1 record](https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=KF730777&db=nuccore&report=genbank&retmode=text) instead specifies isolate JG24 and soil, with a 2013 submission associated with a pepper root-zone study. It has the same species taxonomy ID but supplies no type-strain or culture-collection equivalence. Species identity alone cannot establish deposit identity.

The local generator faithfully reproduces the error-bearing source assertion: the pinned StrainInfo row and fresh API both attach KF730777 to deposit 865460. BacDive also lists it through automatically matched sequence data, reference 124043; that secondary repetition is not independent proof of the missing equivalence. The finding is an unsupported strain-level assignment, not a broken accession, wrong species ID, or claim that the entire record denotes the wrong species. A curator must quarantine/remove this deposit-specific link unless primary evidence establishes JG24 = LMG 26383.

Maintained owner: StrainInfo's upstream sequence/deposit association and TaxonMech's acceptance logic in `src/taxonmech/straininfo_links.py:219`, with regression coverage in `tests/test_straininfo_links.py`. If an upstream correction is not available, introduce a reviewed, evidence-backed exclusion input under `curation/` and consume it through this importer. Do not edit the immutable snapshot, generated `data/straininfo/related_records.tsv.gz`, or generated taxon YAML to conceal the discrepancy. This review does not claim an existing record-specific exclusion mechanism.

## Recommended Edits

1. Resolve M1 in the maintained source/import path. Preserve the original StrainInfo assertion and primary NCBI evidence in provenance while preventing an unqualified LMG 26383 sequence link. Do not reassign JG24 to a new curated strain without additional evidence.
2. Add a focused regression in `tests/test_straininfo_links.py` that rejects/quarantines the conflicting accession/deposit pair while retaining the supported six other marker links, two assembly assertions, and three deposit associations. Any exclusion should be tuple-scoped and evidence-backed, not a species-wide ban on KF730777.
3. After an authorized source refresh or importer correction, rebuild the StrainInfo overlay using `scripts/straininfo.py`, then regenerate this target with `scripts/seed_from_sources.py --apply --only NCBITaxon:1036779`. Broader source changes require the full governed regeneration/validation workflow before publication. None of these write commands was run during this review.

## Follow-up Checks

- Reinspect the complete primary KF730777 feature table and any proposed JG24/type-strain equivalence. A shared taxonomy ID or sequence similarity alone is not sufficient.
- Run the targeted StrainInfo regression tests, including `tests/test_straininfo_links.py` and relevant seed/schema tests, after implementing the maintained correction.
- Rebuild the overlay through its documented dry-run and apply workflow; inspect the exclusion provenance and resulting target before promotion.
- Rerun the exact focused schema/strict commands above. Then run `just verify-corpus`, `just provenance-check`, and the applicable full quality gates after authorized regeneration. A schema pass alone does not close M1.
- Retain FR872720 as source-labeled sequence context only unless primary functional evidence resolves the nonspecific-PCR issue.

## Additional Notes

- FR774992 remains under current NCBI 946785, Allobosea sp. R-45681, beneath unclassified Allobosea, whereas the named species is 1036779. Fresh taxonomy and the original sequence preserve this distinction. LPSN and the original type designations support the sequence's nomenclatural use, but do not authorize silently merging the two NCBI IDs.
- BacDive's host evidence conflicts internally: literature/CCUG rows identify Lupinus polyphyllus, while its DSMZ-derived row says Robinia pseudoacacia. The YAML asserts neither host; this source disagreement must remain visible in any later phenotype/habitat curation.
- BV-BRC's FBZP-16 taxon assignment differs from the pinned GTDB member's NCBI identifier. Neither row was used to attach that genome to the type strain.
- The inline seed event at 2026-09-13T17:54:04Z matches the eight-source scope reason and retains SEEDED status. No human review or biological validation is inferred from generation.
- Live GTDB inspection and independent payload checksums remain unverified. Native catalog evidence, DOI registration, ENA metadata, and validators are not substitutes for those checks.
- Eukaryota was not reviewed again. The closed parallel session required no coordination action; all existing branches/worktrees were preserved.
