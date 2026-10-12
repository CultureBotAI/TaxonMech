# YAML Record Review: Bacillus timonensis

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacillus_timonensis.yaml`
- Started UTC: 2026-10-04T18:16:44Z
- Finished UTC: 2026-10-04T18:24:04Z
- Verdict: needs curation

## Target

The complete 209-line generated TaxonRecord for `NCBITaxon:1033734` was read. It denotes the bacterial species Bacillus timonensis, not an individual deposit or a GTDB cluster. The record has EXACT NCBI grounding, SEEDED lifecycle status, one listed BacDive strain, three GTDB broad mappings, seven source attestations, and one embedded seed event. Identifier search across the complete record tree, including ignored files, resolved only this target.

This is a read-only review. Future changes belong to maintained source transforms and the seed generator, not the generated YAML. No record, source inventory, lifecycle status, or curation-history entry was changed.

## Validation

Both documented record validators passed, including a final rerun:

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/bacillus_timonensis.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/bacillus_timonensis.yaml`: exit 0, one file, zero errors; standard diagnostic output at `reports/instance_validation_failures.tsv`.

Manual structured comparisons checked the backbone, entire lineage, synonyms, scope row, source counts, all listed strain links, and applicable native source objects. These are evidence checks, not a replacement for corpus reproduction.

Not run: full-corpus `just verify-corpus`, `just qc`, `just provenance-check`, rendering, all-reference/history gates, and the test suite. The repository exposes no documented single-record corpus-reproduction substitute. `validate-products` has no applicable causal-graph grounding in this record; NCBI identity was checked directly. No standalone target history entry was found in the bounded ignored-inclusive history search, so no such entry was submitted to the history validator. Schema validation covered the embedded seed event.

## Identity and Grounding

The pinned backbone row and live [NCBI Taxonomy record](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1033734) agree on identifier, species rank, Bacillus parent `NCBITaxon:1386`, and genetic code 11. Taxonomy EFetch and Datasets responses corroborated the lineage. All nine root-first ancestor identifiers, labels, and ranks match the pinned backbone. No child taxon, retirement target, or merge affecting this record was found in the inspected structured tables.

Both synonyms remain source-attributed RELATED_SYNONYM values. Neither the authority string nor the older Bacillus sp. 10403023 name is incorrectly promoted to an exact synonym.

[LPSN name 790160](https://lpsn.dsmz.de/species/bacillus-timonensis) identifies the same proposed species and deposit set, but distinguishes effective usage from valid publication: the name is not validly published, and its taxonomic status is preferred rather than correct. That distinction is missing from the generated record. The NCBI label itself does not require renaming.

GTDB uses different genus/species concepts here. None of the three broad mappings is emitted as an exact synonym or xref, which is appropriate. The live [SeqCode API entry for Ferdinandcohnia timonensis](https://api.seqco.de/v1/names/42620.json) has automated-discovery status and incomplete nomenclatural information; it does not establish a validly published recombination or justify replacing the NCBI label.

## Evidence

### Backbone and Source Counts

`data/raw/ncbitaxon_taxa.tsv` was checked through the structured source comparison. Other inspected rows include:

| Source inventory | Location | Supported assertion |
| --- | --- | --- |
| `data/raw/gtdb_mappings.tsv` | lines 1359-1361 | Three broad mappings, counts 2, 1, 1 |
| `data/raw/bacdive_strains.tsv` | line 1316 | One strain, BacDive 1320, two deposits |
| `data/raw/mediadive_taxa.tsv` | line 103 | One medium, ID 220 |
| `data/raw/gold_organisms.tsv` | line 446 | Five organism records |
| `data/raw/madin_taxa.tsv` | line 624 | Six trait assertions |
| `data/raw/bactotraits_taxa.tsv` | line 77 | One trait assertion |
| `curation/seed_scope.tsv` | line 10795 | Original scope reason and date |

These units are not interchangeable. The primary GTDB attestation counts two genomes for its named cluster and explicitly mentions two further mapped species; it need not be replaced with four.

The full 901,341-record GTDB native catalog scan found four relevant genomes:

| GTDB species | Assembly in pinned catalog | NCBI taxon |
| --- | --- | --- |
| Ferdinandcohnia timonensis | GCF_000285535.1 | 1033734 |
| Ferdinandcohnia timonensis | GCF_902374785.1 | 1033734 |
| Ferdinandcohnia timonensis_A | GCF_004799755.1 | 1033734 |
| JAIVAN01 sp020171895 | GCA_020171895.1 | 1033734 |

The complete mapping-table cross-check likewise found only this NCBI target for these three clusters. Pooling is supported; the generated claim that each cluster also maps to other NCBI taxa is not. Live GTDB pages were unavailable or returned a JavaScript loading shell, so cluster membership verification rests on the inspected pinned catalog, not an asserted live release check.

### Strain and Genome Links

[BacDive 1320](https://bacdive.dsmz.de/strain/1320), its full native capture, and the [DSMZ DSM 25372 catalogue](https://www.dsmz.de/collection/catalogue/details/culture/DSM-25372) support the recorded strain designations and deposits. BacDive reference 66792 supplies the unversioned GCA_000285535 assertion, IMG 2547132138, and BV-BRC/PATRIC 1033734.3. These are source assertions about the one strain, not three independent cultured strains.

The live [NCBI assembly report](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000285535.1/dataset_report) resolves the accession to the current type-derived GCA/GCF_000285535.1 assembly, BioSample SAMEA2272358, and project PRJEA70827. Pinned GenBank, RefSeq, BV-BRC, GTDB, and GOLD metadata corroborate the accession family and organism context. A source-preserved unversioned accession is not, by itself, a broken link.

The other three exact-taxon assembly families represent AF060A6, AcN35-3, and MGYG-HGUT-01405. Their BioSamples are respectively SAMN11029899, SAMN21542845, and SAMEA5850908. Shared species classification does not attach these isolates to DSM 25372. The current MGYG assembly is version .2, whereas GTDB retains historical .1; the AcN35-3 RefSeq assembly is suppressed and the GenBank record carries an organism-verification exclusion. These differences were preserved rather than merged away.

Two GOLD links to Go0614539 are intentional: one matches the culture-collection field and the other the strain field. The full native object has DSM 25372 in both fields. The other four GOLD organisms explain the count of five, not five eligible DSM-deposit genome links. In particular, Go0017284 links the type assembly through CSUR P162, which the pinned CAFI-based matcher does not accept as a validated culture key. Bare laboratory identifiers are also ineligible; no join was inferred from their resemblance.

The complete StrainInfo native object supports SI-ID397955, SI-DP904628, versioned DOI `10.60712/SI-ID397955.3`, the deposit status, BacDive cross-reference, and published-online status. It has no sequence array. Its strain/deposit related-record pair is justified, not duplicate genome evidence. The live StrainInfo webpage was unavailable, so this verification is explicitly against the pinned capture.

Ignored-inclusive searches of the full compressed AllTheBacteria catalog and local ATB crosswalk found SAMN11029899, with assembly run ERZ25546346 and dataset r0.2. That sample belongs to AF060A6, not this BacDive deposit. No ATB strain link should be manufactured from the species label.

### Publication and Correction

The inspected [species description](https://link.springer.com/article/10.4056/sigs.2776064), also identified as PMID 23408487 in the sequence record, links the proposed species to its culture deposits and CAET genome project. Its historical assembly figures differ from current NCBI assembly statistics; the YAML does not reproduce those figures.

The [2023 correction](https://link.springer.com/article/10.1186/s40793-022-00448-8) explicitly adds 10403188 as the intended type-strain designation in place of the originally written MM10403188, and corrects DSM 253720 to DSM 25372. The current LPSN display still includes the longer DSM number. This is a documented source conflict, not support for adding another deposit.

[JF824810.1](https://www.ncbi.nlm.nih.gov/nuccore/JF824810.1) is a 1,472-base partial 16S sequence attributed to strain 10403023 and this taxon. The record's source-preserved BacDive designation should not be silently rewritten from the corrected paper. Any future alias reconciliation needs explicit provenance.

## Completeness

The material gap is the missing name-level nomenclature and resulting absent type-strain flag. It is not a demand to fill every optional slot. LPSN identity, nomenclatural status, and proposed type information can qualify the NCBI name without conflating taxonomic databases.

No row for the target name or LPSN identifier was found in `data/raw/lpsn_names.tsv`, including an ignored-independent exact identifier/name search. The BacDive inventory also has no LPSN identifier. Consequently, the generator cannot populate this information from its present inputs.

Broader searches used `rg --no-ignore --hidden -z` across raw inventories, native catalogs, BacDive, BV-BRC, GOLD, SeqCode, StrainInfo, ATB, curation, and history. SOURCE.json files excluded from the initial content scan were checked separately through a recursive structured search. No target-specific manifest value was found in the searched raw/catalog/BacDive/BV-BRC/GOLD/SeqCode/StrainInfo manifests. These are bounded local absence findings, not claims that an external authority lacks evidence.

The configured kg-microbe LPSN and LPSN-API node/edge files were unavailable at their configured paths. Thus the precise loss point, upstream extraction versus local ingestion, remains unresolved. The absence is already visible in the maintained pipeline's generated inventory, not merely in the final YAML.

There is no missing mandatory causal graph, phenotype narrative, or arbitrary gene/regulator evidence. iModulonDB is not applicable to the claims in this record. An uncapped listing of one strain agrees with the inventory. MediaDive 220 is supported by the species inventory and [medium page](https://mediadive.dsmz.de/medium/220); the separate strain-level medium count of zero in the raw projection does not invalidate the species attestation.

## Findings

Counts: 0 blocker, 1 major, 1 minor.

1. **Major: missing nomenclatural qualification and source-backed type designation.** The record omits the LPSN name object and `strains[0].is_type_strain`, despite the convergent authority/deposit evidence described above. This hides a consequential distinction about publication status and the strain's role. The field-by-field rubric calls for those distinctions when known. This is not an identity failure or a schema error. Owner: the configured kg-microbe LPSN/LPSN-API transforms and `src/taxonmech/extract.py:420`, followed by `src/taxonmech/seed.py:514`. The local type flag deliberately depends on a mapped LPSN deposit; do not bypass that contract with a guessed flag.

2. **Minor: three GTDB notes assert unsupported reverse mapping multiplicity.** Target lines 42, 49, and 56 all state that the respective GTDB species also maps to other NCBI taxa. The complete catalog and mapping inspection supports three clusters pooling onto this one taxon, not that assertion. Owner: the broadMatch note template in `src/taxonmech/seed.py:463`. Counts, predicates, and the absence of identity xrefs are otherwise appropriate.

## Recommended Edits

1. Restore a provenance-backed LPSN 790160 mapping through the maintained upstream transform and local inventory extractor. Preserve the negative publication/correct-name statuses and qualify the proposed type accordingly. Reconcile the documented correction without promoting DSM 253720 into a supported culture deposit. Keep the original BacDive designation as source evidence.
2. Before ingesting that status, fix or verify the status parser in `src/taxonmech/extract.py:479` and `:481`: substring checks would mistake negative phrases containing "validly published" or "correct name" for positive statuses. Add explicit negative-status regression cases. This is a prospective import hazard, not a false boolean currently present in this YAML.
3. Replace the broadMatch note template with wording supported by the mapping direction, or compute reverse multiplicity before mentioning other NCBI taxa. Do not upgrade these mappings to equivalence.
4. After approved curation and source refresh, regenerate inventories and corpus with the documented extraction/seed workflow. Do not hand-edit generated YAML or historical seed text.

## Follow-up Checks

- Confirm the refreshed name row's identifier, taxon mapping, false publication/correct-name booleans, qualified type designations, and correction provenance against the authorities.
- Confirm the DSM 25372 intersection produces the schema-defined type flag without changing the underlying BacDive assertion or importing unrelated genomes.
- Test negative status strings, API-only/base-node coverage, and broadMatch explanatory text in the maintained extractor/generator tests.
- Rerun the two record validators, then the full corpus reproduction, provenance, test/QC, and rendering checks for any actual generator or input change.
- Recheck the four GTDB genomes and all three predicates after refresh. Keep historical accession versions and suppressed RefSeq status explicit.
- Resolve live GTDB/StrainInfo availability and the unavailable configured kg-microbe files before claiming a fresh end-to-end source reproduction.

## Additional Notes

The seed event's six-source scope wording exactly preserves the historical scope reason; the current seven attestations are not evidence that the history should be rewritten. No human-reviewed status was implied or assigned.

The DSMZ page's related-link label names Cytobacillus kochii despite the Bacillus timonensis catalogue body and BacDive target. That isolated link label was not used as a taxonomic reidentification. Likewise, the sequence submission chronology and historical paper assembly figures were not generalized into unsupported record changes.

The complete corpus filesystem coverage check included ignored files: 625,960 YAML records, 22,250 matching per-record reports before this report, no duplicate report stems or unmatched report stems, and all 6,243 eukaryota records covered. Coverage is report existence, not a claim that every record passes review. This report adds one completed individual review.
