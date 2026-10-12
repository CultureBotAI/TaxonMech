# YAML Record Review: Chelativorans sp. YIM 93876

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/chelativorans_sp_yim_93876.yaml`
- Started UTC: 2026-10-06T05:03:57Z
- Finished UTC: 2026-10-06T05:08:14Z
- Verdict: pass

## Target

Read all 54 lines of the generated `TaxonRecord` for `NCBITaxon:1034980`, Chelativorans sp. YIM 93876. It asserts species rank, bacterial domain, parent `NCBITaxon:2643807`, ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` status, zero imported strains, one NCBI name attestation and one inline seed event. No definition, synonyms, nomenclature, taxonomy mappings, xrefs, literature evidence, strain/genome links or causal graphs are asserted.

`data/taxa/PATHS.tsv:14265` uniquely pairs identifier and stem. `curation/seed_scope.tsv:322085` contains the NCBI-only attestation rule, added 2026-09-13. This target is Chelativorans, not a Bacillus or Brevibacillus isolate sharing a nearby YIM designation.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/chelativorans_sp_yim_93876.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/chelativorans_sp_yim_93876.yaml --out /private/tmp/cyim93876-validation.tsv`: exit 0, one file, zero ERROR rows. Read the header-only diagnostic TSV.
- Structured comparisons matched complete pinned identity, lineage, genetic code, path/scope references, sole attestation and inline event reason. Seven other inventories have no exact target-ID row; the pinned backbone has no children under this target.
- Exact-ID checks of `data/raw/ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` and `dropped.tsv` returned no target rows.
- The initial ignored-inclusive source search returned three rows. A broader numeric-ID and marker-expanded search returned eleven rows, all fully inspected, with read addresses reconciled. The ignored-inclusive prior-report/history search returned no exact ID, full-label or slug match.
- Pre-report `git diff --exit-code HEAD --` covering data, curation, history, code, configuration and guidance exited 0. Guidance/schema remain unchanged from prior full reads. HEAD remains `b6a6508faca1388b88feb5740b1095e9f64cfdb8`.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just test`, `just validate-all`, provenance/history gates, rendering/site drift, README statistics, publication-size and vendored-file gates. This is not corpus release certification.
- `just validate-products` is not applicable without curator-added causal-graph nodes. No undocumented focused term/reference/history validator was invented.

## Identity and Grounding

Complete live [NCBI taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034980&retmode=xml) confirms ID, label, species rank, bacterial division, parent 2643807 and genetic code 11. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034980) agrees and supplies all ten ancestor IDs including root.

The carried chain is root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Alphaproteobacteria, Hyphomicrobiales, Phyllobacteriaceae, Chelativorans and unclassified Chelativorans. Every pinned ancestor ID, label and rank matches the YAML; live NCBI confirms the non-root chain. The family is `NCBITaxon:69277`, genus `NCBITaxon:449972` and unclassified parent `NCBITaxon:2643807`. The inspected [parent taxonomy page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=2643807&lvl=&mode=tree) also lists this exact isolate under unclassified Chelativorans.

The parent has `NO_RANK`, while the target has explicit NCBI `SPECIES` rank. This isolate-bearing placeholder satisfies species-level eligibility without establishing a formally named species or requiring a change to `STRAIN`. `EXACT` means an exact NCBI concept match, not nomenclatural validation or curator sign-off.

## Evidence

1. **Pinned identity and provenance.** Complete `data/raw/ncbitaxon_taxa.tsv:221792` supplies matching label, rank, parent, code and the 2026-09-13 snapshot, with empty synonym and retirement-target fields. Complete `data/catalog/ncbi_names-0005.jsonl.gz:31215` supplies the same scientific name/ID and an empty unique name. The complete scope row agrees with the seed reason. The sole `NCBITAXON` attestation has count 1 and unit `NAME`, not a genome or trait count. The inline `SEEDED_FROM_SOURCES` event at `2026-09-13T17:54:04Z` names `seed_from_sources` and reproduces the scope reason. `SEEDED` does not assert human review.

2. **Direct marker linkage.** Exact-taxonomy Nuccore search returned one result, [JF792107.1](https://www.ncbi.nlm.nih.gov/nuccore/JF792107.1), UID 333798033. Complete metadata, references and feature qualifiers were inspected, excluding sequence bases. It is a 631-base partial 16S rRNA gene, partial at both ends, with organism Chelativorans sp. YIM 93876, strain YIM 93876 and explicit `taxon:1034980`. Its sequence taxonomy independently names Phyllobacteriaceae and Chelativorans. C. Chen submitted it on 7 April 2011 through the Yunnan Institute of Microbiology / Yunnan University; creation was 28 May 2011 and update 26 August 2015. The inspected metadata supplies no culture-collection, BioSample or assembly identifier. This marker is not a genome or deposit accession.

3. **Publication boundary.** GenBank lists C. Chen's study of culturable bacteria from Qijiaojing Lake and enzyme production as unpublished, without DOI or PMID. Its title does not prove isolate-specific enzyme activity. The initial exact full-name web query returned no results. Subsequent quoted marker and organism/designation queries surfaced the inspected parent taxonomy page, not a matching primary publication. These bounded searches do not prove publication absence. No phenotype, habitat or culture recipe was inferred.

4. **Coverage counts.** No exact target-ID BacDive inventory row or classified descendant was found. Thus `strain_count: 0` agrees with imported coverage, not absence of the isolate or its marker. Live Assembly ESearch for `txid1034980[Organism:noexp]` returned zero results with no-items/phrase-not-found diagnostics. This bounded result does not exclude assemblies under other classifications or in other databases.

5. **Rejected numeric collisions.** The eight additional source rows in the broader search concern unrelated organisms. BV-BRC `1773.20417` is Mycobacterium tuberculosis ERR1034980, taxon 1773. GenBank `GCA_010349805.1` is Campylobacter jejuni PNUSAC013784, taxon 197; `GCA_020045645.1` is Salmonella enterica strain 1034980001, taxon 28901; `GCA_027161725.1` is Staphylococcus aureus 8-353-171, taxon 1280, BioSample SAMEA1034980. Four AllTheBacteria rows concern Staphylococcus aureus SAMEA1034980/ERR086112/ERZ3070417, Mycobacterium tuberculosis SAMEA3558513/ERR1034980/ERZ3501484, Salmonella enterica serovar Kentucky SAMN14051069/SRR11034980/ERZ25717511, and rejected Escherichia coli sample SAMN31034980/SRR21722754. None is evidence for this Chelativorans record.

## Completeness

No consequential omission was established under the seeded-record model. Optional definition, literature evidence, synonyms, nomenclature, mappings, xrefs, strain/genome links and causal graphs may remain empty. The matching marker corroborates identity but does not establish an eligible deposit/genome relationship; a laboratory designation alone is not a registered culture-collection accession.

Both source searches used `rg --no-ignore --hidden -z` through a row-address reader across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding manifests named `SOURCE.json`. The initial query covered exact identity, full label and slug. The second included unbounded digits 1034980, YIM93876 separator variants and JF792107 with its versioned spelling. It returned three target rows and eight rejected numeric collisions, not an eligible marker crosslink or strain/genome candidate. Ignored files and compressed rows were included, not every separate snapshot archive or live database.

The complete expanded candidate rows were `curation/seed_scope.tsv:322085`, `data/raw/ncbitaxon_taxa.tsv:221792`, `data/catalog/ncbi_names-0005.jsonl.gz:31215`, `data/bvbrc/bvbrc-0006.jsonl.gz:8424`, `data/catalog/ncbi_genbank-0009.jsonl.gz:6328`, `data/catalog/ncbi_genbank-0018.jsonl.gz:21553`, `data/catalog/ncbi_genbank-0025.jsonl.gz:11966`, and `data/catalog/allthebacteria.tsv.xz` rows 65987, 569450, 1776327 and 2431881. All eleven were fully read, rather than judged from search snippets.

Exact-ID comparisons of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories returned no target rows. The prior-report/history search also included ignored files; the inline seed event remains present.

iModulonDB was not applicable to identity-only assertions. No marker alignment, genome comparison, experimental reanalysis or exhaustive literature census was performed. Search snippets were not accepted as evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the current YAML. Identity, grounding, lineage, provenance and imported coverage agree with the inspected pinned and live sources. This pass does not certify a formal species name, biological traits, worldwide assembly absence or full-corpus reproducibility.

## Recommended Edits

None required on the inspected evidence. Keep the generated YAML unchanged, including its Chelativorans label and lineage, NCBI species rank, unclassified parent, zero imported strain count and `SEEDED` status. Do not infer enzyme activity from an unpublished study title or import unrelated relationships based on shared numeric substrings.

Future authority corrections belong to `conf/ncbi_taxdump.yaml`, `src/taxonmech/ncbi_taxdump.py` and `scripts/extract_source_inventory.py`. Generation is owned by `src/taxonmech/seed.py` and `scripts/seed_from_sources.py`; genuine scope changes belong in `curation/seed_scope.tsv`. Future enrichment requires explicit source-owned strain/deposit/genome provenance.

## Follow-up Checks

- At source refresh, repeat exact taxonomy, retirement/replacement and JF792107 authority reads.
- Require whole culture identifiers and explicit sequence/genome relationships before enrichment; partial markers remain outside genome counts.
- Inspect an actual primary publication with isolate-specific results before phenotype or habitat curation in the appropriate sibling repository.
- After an authorized source/extraction/seeding change, use the documented dry run and single-record canary, rerun `just validate` and `just validate-strict`, then full `just verify-corpus` and `just qc` before release.

## Additional Notes

Only this new timestamped report was written for this target. Generated records, inventories, scope, history, prior reports, rendered products and Eukaryota reviews remain unchanged. All external reads were public and unpaid; no commits, GitHub mutations, external contacts, provider-credit jobs or lifecycle promotions occurred.

The existing single worktree was retained. The other Codex session is closed, and the full corpus-review goal remains incomplete.
