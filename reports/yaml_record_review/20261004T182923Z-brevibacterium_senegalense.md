# YAML Record Review: Brevibacterium senegalense

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/brevibacterium_senegalense.yaml`
- Started UTC: 2026-10-04T18:25:58Z
- Finished UTC: 2026-10-04T18:29:23Z
- Verdict: pass with minor issues

## Target

The entire 334-line generated TaxonRecord was read: `NCBITaxon:1033736`, Brevibacterium senegalense, rank SPECIES, domain BACTERIA, EXACT grounding, SEEDED lifecycle status. An ignored-inclusive identifier search resolved only this YAML. The record carries one nomenclatural name, two GTDB mappings, one listed BacDive strain, eight source attestations, and one seed event.

This review does not edit the record, source inventories, prior reports, lifecycle status, or curation history. The only new review artifact is this report. Generated-field fixes belong to maintained source transforms or the seed generator.

## Validation

The documented single-record commands passed:

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/brevibacterium_senegalense.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/brevibacterium_senegalense.yaml`: exit 0, one file, zero errors; standard diagnostic output at `reports/instance_validation_failures.tsv`.

Manual structured comparisons checked the backbone, full lineage, synonyms, nomenclature, counts, scope, and the displayed strain assertions against their inventories and native source objects. These checks are not a replacement for corpus reproduction.

Skipped: full-corpus `just verify-corpus`, `just qc`, `just provenance-check`, tests, rendering, and all-reference/history gates. There is no documented record-only corpus-reproduction substitute. The record contains no causal graph applicable to `validate-products`; NCBI identity was verified at its source. No target-specific standalone history entry was found in the ignored-inclusive history search. The embedded seed event was covered by schema validation and compared with the scope row and source timestamps.

## Identity and Grounding

The pinned `data/raw/ncbitaxon_taxa.tsv:221301` row and live [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033736&retmode=xml) agree on species identity, parent Brevibacterium `NCBITaxon:1696`, and genetic code 11. All nine root-first ancestor identifiers, names, and ranks match the backbone. The [NCBI Datasets taxonomy response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033736) also confirms the complete lineage identifiers. The taxonomy browser failed through the web tool; the API responses supplied the live verification.

Both NCBI names are appropriately RELATED_SYNONYM values. The backbone has no children for this taxon. Exact structured searches of merged and dropped tables found no relevant rows.

[LPSN 790607](https://lpsn.dsmz.de/species/brevibacterium-senegalense) supports the name, Kokcha et al. 2013 authority, valid publication under the ICNP, current correct-name status, type strain DSM 25783, and marker JF824806. Its recommendation wording is source nomenclatural metadata, not a clinical recommendation from this review. The raw name row at `data/raw/lpsn_names.tsv:27547` explicitly maps this name to the NCBI taxon and the unsuffixed GTDB species.

The type flag traces to the intersection of the LPSN DSM designation and the BacDive deposits. The LPSN type-designation list is not a requirement to repeat every laboratory alias. CSUR P155 and JCM 30545 remain visible in the strain's deposit list.

## Evidence

### Counts and GTDB Mappings

The source inventory rows support all eight attestations:

| Inventory | Row | Count and unit |
| --- | --- | --- |
| `ncbitaxon_taxa.tsv` | 221301 | 1 name |
| `lpsn_names.tsv` | 27547 | 1 name |
| `gtdb_mappings.tsv` | 1362-1363 | 2 and 1 genomes in distinct clusters |
| `bacdive_strains.tsv` | 22745 | 1 strain |
| `mediadive_taxa.tsv` | 104 | 2 media: 92 and J26 |
| `gold_organisms.tsv` | 447 | 4 organism records |
| `madin_taxa.tsv` | 625 | 5 trait assertions |
| `bactotraits_taxa.tsv` | 78 | 1 trait assertion |

Paths in this table are under `data/raw/`. The GTDB source attestation counts its named primary cluster and separately identifies the additional cluster. It is not missing the third catalogued genome. Counts with different units were not summed.

A complete scan of all 901,341 records in `data/catalog/gtdb_genomes-*.jsonl.gz` found:

| Cluster | Members | NCBI taxon values |
| --- | --- | --- |
| `s__Brevibacterium senegalense` | RS_GCF_000285835.1; RS_GCF_902374775.1 | 1033736 only |
| `s__Brevibacterium senegalense_A` | GB_GCA_020743695.1 | 1033736 only |

All three full native objects were inspected. The complete mapping table and species inventory agree with these counts. The broader NCBI species pools two GTDB concepts, so broadMatch is defensible. The unsuffixed mapping has an independent LPSN identity link, explaining its xref and note under the existing seed policy. The suffixed cluster is not an identity xref or synonym.

Both live GTDB taxon pages were inaccessible through the web tool. This is a pinned-catalog audit, not verification of a newer live GTDB release. The one unsupported explanatory sentence is detailed under Findings.

### Type Strain and Sequence

The full native BacDive object at `data/bacdive/records.jsonl.gz:22744` and [BacDive 22939](https://bacdive.dsmz.de/strain/22939) confirm JC43 and its three deposits. Reference 67770 explicitly supplies GCA_000285835, IMG 2547132136, and BV-BRC 1033736.3 with the recorded assembly description and taxon.

[DSMZ DSM 25783](https://www.dsmz.de/collection/catalogue/details/culture/DSM-25783) confirms the type strain, JC43, CSUR P155, JCM 30545, and the marker/genome project. The [JCM 30545 catalogue](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_number?JCM=30545) independently records the transfer from DSM 25783, accession in 2014, BacDive/NCBI identifiers, and GenBank/RefSeq assembly families. These agree on culture identity.

Live [JF824806.1](https://www.ncbi.nlm.nih.gov/nuccore/JF824806.1) is a 1,491-base partial 16S sequence. Its source feature explicitly names JC43, DSM:25783, CSUR:P155, this taxon, and type material. The YAML correctly preserves the supplied unversioned INSDC accession rather than inventing a version.

The full StrainInfo capture at `data/straininfo/records.jsonl.gz:300939` supports SI-ID403050, its version-3 DOI `10.60712/SI-ID403050.3`, and the eligible own deposit SI-DP910096. Its sole sequence explicitly names that same deposit. The nucleotide reference, strain record, and deposit are therefore correctly typed as related records, not genomes. The source's `rrnaop` type is retained as provenance; the linked accession itself is a partial 16S sequence. The live StrainInfo page returned only a JavaScript shell, so this detailed verification rests on the pinned capture.

### Genome Provenance

The two GCA assertions and two IMG assertions preserve distinct BacDive and GOLD sources. They are not evidence for duplicate strains or multiple independently established genome sequences.

The complete GOLD objects support the exact chain:

`DSM 25783 -> Go0017281 -> Gp0017281 -> Ga0019634`

The organism supplies the culture identifier; the sequencing project supplies SAMEA2272372 and PRJEA82613; the analysis refers to that project and supplies the unversioned GCA accession and IMG identifier. Its direct organism field is blank, not conflicting, and the project chain resolves it. All seven GOLD related assertions and both GOLD genome assertions match the raw tables.

Go0614977 has JCM 30545 in two different source fields, explaining the two related-record assertions. Go0614978 supplies CSUR P155, which is outside the pinned CAFI matcher, and Go0636575 denotes MGYG-HGUT-01408 without an eligible deposit. These four native organisms account for the GOLD species count.

Read-only calls to the actual matcher accept DSM 25783 and JCM 30545, but reject CSUR P155, bare JC43, MGYG-HGUT-01408, and ChiGjej5B5-7349. Repeated laboratory names also occur for unrelated taxa in the ignored-inclusive search. Those names cannot replace a deposit match.

The [NCBI assembly report](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000285835.2/dataset_report) confirms that current GenBank GCA_000285835.2 pairs with RefSeq GCF_000285835.1, is from type material, and has SAMEA2272372/PRJEA82613. The version suffixes differ legitimately. Historical GCA_000285835.1 was replaced. The two source assertions in this YAML were supplied without versions; they should not be silently changed to either version.

The complete pinned NCBI objects and live exact-taxon assembly summaries distinguish the other records:

- GCA_020743695.1 is a ChiGjej5B5-7349 metagenome assembly, BioSample SAMN21194334, excluded from RefSeq for MAG completeness and metagenomic origin.
- Historical GCA/GCF_902374775.1 belongs to MGYG-HGUT-01408, BioSample SAMEA5850911, and is suppressed in the pinned NCBI tables. Its continued presence in GTDB is snapshot history, not proof of another DSM 25783 culture.

The full native BV-BRC objects corroborate the JC43 accession and preserve separate MGYG and ChiGjej records, including deprecated duplicates. None supplies an eligible additional deposit join. Shared assembly statistics, species, or bare strain text was not used to transfer genomes.

### Publications and Media

[PMID 23408786](https://pubmed.ncbi.nlm.nih.gov/23408786/) was verified through NCBI EFetch to identify [DOI 10.4056/sigs.3256677](https://link.springer.com/article/10.4056/sigs.3256677). The inspected description establishes JC43's type-strain/deposit identity and reports the historical genome project. Its effective publication in 2012 is compatible with the nomenclatural authority date in 2013.

[DOI 10.1099/ijs.0.056101-0](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.056101-0) resolves to the 2013 validation-list publication and cites the species description. The publisher's full table did not load; LPSN explicitly identifies validation list 153 as the validating publication. The report does not claim an independently inspected table row.

MediaDive [92](https://mediadive.dsmz.de/medium/92) and [J26](https://mediadive.dsmz.de/medium/J26) resolve to the two named recipes. DSMZ and JCM respectively associate them with these deposits. The separate raw BacDive strain projection has medium_count zero, so the YAML omits that optional strain field while retaining the supported species-level count.

## Completeness

No consequential missing representation was established for this record. It contains the full single-strain listing, source-backed nomenclature and type flag, source-preserved genome assertions, and separate sample/project/organism/sequence identifiers.

A successful `rg --no-ignore --hidden -n -z` scan covered raw inventories, native catalogs, BacDive, BV-BRC, GOLD, SeqCode, StrainInfo, ATB, curation, and history. An initial unsupported look-around expression failed and was replaced with a supported boundary expression; no absence conclusion relies on the failed query. A separate recursive structured SOURCE.json search covered the initially excluded manifests and found no target-specific values in those searched manifests.

An exact ignored-inclusive search of `data/atb/` and the full compressed `data/catalog/allthebacteria.tsv.xz` found no row for the local strain ID or any of the three inspected BioSamples. No ATB link is justified from this snapshot. Exact searches across GOLD and the strain-link tables found no additional project/analysis for the JCM/CSUR organism records. These are bounded local findings, not claims about all external data.

The native SeqCode name entry is a catalog pointer, not an additional genome assertion; its live API was unavailable. The JCM page offers an explicit RefSeq family association that could inform a future provenance-preserving source extension, but it does not authorize changing the current imported assertions or relaxing matching rules.

No causal graph, gene mechanism, or transcriptomic claim requires filling. iModulonDB is not applicable. Optional biological traits were not invented from source counts or predictions.

## Findings

Counts: 0 blocker, 0 major, 1 minor.

1. **Minor: unsupported reverse multiplicity in the suffixed GTDB note.** Target lines 68-69 claim that the GTDB species also maps to other NCBI taxa. The complete native cluster scan and mapping table show only `NCBITaxon:1033736` for that cluster. Two GTDB clusters pool onto this NCBI species, which is a different relationship. Counts and predicates are sound. Maintained owner: the broadMatch note template in `src/taxonmech/seed.py:462`, not the generated YAML.

## Recommended Edits

1. Change the broadMatch explanation in `src/taxonmech/seed.py` to describe only the supported pooling relationship, or compute reverse mapping multiplicity before claiming additional NCBI taxa.
2. Add a generator regression case for multiple GTDB clusters mapping to one NCBI species when each cluster has no other NCBI target. Preserve the LPSN-linked primary mapping's note, xref, counts, and predicates.
3. Following approval of a later curation change, use the documented dry-run/canary and generated-corpus workflow. Do not hand-edit this record or rewrite its original seed event.

## Follow-up Checks

- Run the focused generator regression test and both documented single-record validators after any wording change.
- Run the authoritative full-corpus reproduction, provenance, test/QC, and rendering gates for a shared-generator change.
- Recheck that no GTDB suffixed mapping becomes an exact synonym or xref and that source counts remain 2 and 1.
- Preserve both BacDive/GOLD assertions, the complete GOLD chain, and the StrainInfo same-deposit nucleotide placement.
- Revisit the inaccessible live GTDB pages, StrainInfo detailed view, and validation-list table before claiming complete live-source reproduction.

## Additional Notes

The seed history exactly matches `curation/seed_scope.tsv:4042`. Its timestamp is the newest of the raw, ATB, and StrainInfo manifest extraction times, consistent with `_seed_timestamp()`. This review does not promote SEEDED to REVIEWED.

Source-context differences are retained: the paper reports isolation in December 2010, DSMZ lists sampling in 2011, and the current BioSample records France:Marseille whereas collection/literature descriptions give Senegalese origin. Historical paper assembly figures also differ from current NCBI statistics. The YAML makes none of these geography/date/statistics claims, so these are not record defects.

This is one completed individual review, not a bulk verdict. Previously covered eukaryota records were not changed.

