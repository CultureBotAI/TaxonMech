# YAML Record Review: Gracilibacillus sp. YIM 94049

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/gracilibacillus_sp_yim_94049.yaml`
- Started UTC: 2026-10-06T05:25:28Z
- Finished UTC: 2026-10-06T05:26:57Z
- Verdict: pass

## Target

Read all 54 lines of the generated `TaxonRecord` for `NCBITaxon:1034986`, Gracilibacillus sp. YIM 94049. It asserts species rank, bacterial domain, parent `NCBITaxon:2625209`, ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` status, zero imported strains, one NCBI name attestation and one inline seed event. No definition, synonyms, nomenclature, mappings, xrefs, literature evidence, strain/genome links or causal graphs are asserted.

`data/taxa/PATHS.tsv:14271` uniquely pairs ID and stem. `curation/seed_scope.tsv:322091` records the NCBI-only attestation rule, added 2026-09-13. The target is the exact YIM 94049 concept, not the genus or another YIM isolate.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/gracilibacillus_sp_yim_94049.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/gracilibacillus_sp_yim_94049.yaml --out /private/tmp/gyim94049-validation.tsv`: exit 0, one file, zero ERROR rows. Read the header-only diagnostic TSV.
- Structured comparisons matched complete pinned identity, all lineage entries, code, unique path/scope references, sole attestation and inline event reason. The backbone has no classified children under this target.
- Exact-ID checks of `data/raw/ncbi_type_material.tsv`, `ncbi_merged_ids.tsv` and `dropped.tsv` returned no target row. Seven other inventories have no exact target-ID row.
- Initial and marker-expanded ignored-inclusive compressed-source searches each returned four rows, all fully inspected and reconciled by address. Three were target identity/scope rows; one was an unrelated contig-N50 match. The ignored-inclusive exact ID/full-label/slug search of prior reports and `history` returned no target match.
- Pre-report tracked-file diff against HEAD exited 0 across data, curation, history, code, configuration and guidance. Guidance/schema remain unchanged from prior full reads; the review skill and checklist were reread this turn. HEAD is `b6a6508faca1388b88feb5740b1095e9f64cfdb8`.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just test`, `just validate-all`, provenance/history gates, rendering/site drift, README statistics, publication-size and vendored-file checks. No separate target history artifact was found to validate; the inline event was checked with the YAML and source comparison.
- `just validate-products` is not applicable without curator-added causal-graph nodes. No undocumented focused term/reference/history validator was invented. This is not corpus release certification.

## Identity and Grounding

Complete live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034986&retmode=xml) confirms ID, label, species rank, bacterial division, parent 2625209 and genetic code 11. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034986) agrees and supplies all ten ancestor IDs including root.

The chain is root, cellular organisms, Bacteria, Bacillati, Bacillota, Bacilli, Caryophanales, Bacillaceae, Gracilibacillus and unclassified Gracilibacillus. Every pinned ancestor ID, label and rank matches the YAML; live taxonomy confirms the non-root entries. Family `NCBITaxon:186817`, genus `NCBITaxon:74385` and parent `NCBITaxon:2625209` are supported for this exact target independently of nearby YIM records.

The parent has `NO_RANK`; NCBI explicitly ranks the target as `SPECIES`. The isolate designation does not require changing that rank to `STRAIN`. `EXACT` means an exact NCBI concept match, not formal nomenclatural validation or curator sign-off.

## Evidence

1. **Pinned source and audit trail.** Complete `data/raw/ncbitaxon_taxa.tsv:221798` supplies matching identity, parent, code and the 2026-09-13 snapshot, with empty synonym and retirement-target fields. Complete `data/catalog/ncbi_names-0005.jsonl.gz:31221` supplies the same ID/scientific name and empty unique name. The full scope row agrees with the seed reason. The sole `NCBITAXON` attestation has count 1 and unit `NAME`, not a strain, genome or phenotype count. The inline event at `2026-09-13T17:54:04Z` names `seed_from_sources`, action `SEEDED_FROM_SOURCES`, and the same scope reason. `SEEDED` does not assert human review.

2. **Sequence identity.** Exact Nuccore search returned [JF792130.1](https://www.ncbi.nlm.nih.gov/nuccore/JF792130.1), UID 333798056, as its sole result. Full metadata, references and feature qualifiers were read, excluding sequence bases. It is a 671-base partial 16S rRNA gene, partial at both ends, with organism Gracilibacillus sp. YIM 94049, strain YIM 94049 and explicit `taxon:1034986`. Its sequence taxonomy agrees with Bacillaceae and Gracilibacillus. C. Chen submitted it on 7 April 2011 through the Yunnan Institute of Microbiology / Yunnan University; it was created 28 May 2011 and updated 26 August 2015. The inspected metadata supplies no culture-collection, BioSample or assembly identifier. This marker is not a genome or deposit accession.

3. **Publication boundary.** GenBank lists C. Chen's study of culturable bacteria from Qijiaojing Lake and enzyme production as unpublished, with no DOI or PMID. Exact full-name and marker-accession web searches returned no results. These bounded queries do not prove publication absence. The study title does not establish isolate-specific enzyme activity, habitat or culture requirements, and none was inferred.

4. **Coverage counts.** No exact BacDive target row or classified descendant was found, so `strain_count: 0` agrees with imported coverage, not absence of the isolate. Assembly search for `txid1034986[Organism:noexp]` returned zero with no-items/phrase-not-found diagnostics. This exact-query result does not exclude assemblies under other classifications or in other databases.

5. **Rejected contig-statistic collision.** Fully read `data/catalog/gtdb_genomes-0008.jsonl.gz:32538`. It concerns `GB_GCA_963849055.1`, assembly `GCA_963849055.1`, BioSample SAMEA114828434, isolate MFD09212.bin.2.54, classified by NCBI as uncultured Actinomycetota bacterium, taxon 3039803, and by GTDB as Mycobacterium sp963849055. It is a metagenome-derived assembly with total length 5805097; its `ncbi_contig_n50` value of 1034986 caused the match. Neither its taxon, organism nor isolate matches YIM 94049. The numeric coincidence establishes no strain/genome relationship.

## Completeness

No consequential omission was established under the seeded-record model. Empty optional fields are appropriate where no supported claim is carried. The marker corroborates identity but does not establish an eligible deposit/genome relationship; a laboratory designation alone is not a registered culture-collection accession.

Both source searches used `rg --no-ignore --hidden -z` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding manifests named `SOURCE.json`. Queries covered the word-bounded ID, full label, slug and YIM94049 separator variants; the second added JF792130 and its versioned spelling. Both returned the same four fully inspected rows described above. No additional eligible strain/genome or marker crosslink was found in those roots. Ignored files and compressed rows were included, not every external database or separate snapshot archive.

Exact-ID comparisons of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories returned no target row. The prior-report/history search also included ignored files; the inline seed event remains present.

iModulonDB was not applicable to identity-only assertions. No marker alignment, genome comparison, experimental reanalysis or exhaustive literature census was performed. Search snippets were not accepted as evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, grounding, provenance and imported coverage agree with inspected sources. This pass does not certify formal nomenclature, biological traits, worldwide assembly absence or full-corpus reproducibility.

## Recommended Edits

None required on the inspected evidence. Keep the generated YAML, NCBI species rank, unclassified parent, zero imported strain count and `SEEDED` status unchanged. Do not infer enzyme activity from an unpublished title, count a partial 16S marker as a genome, or import the unrelated metagenome assembly.

Future authority corrections belong to `conf/ncbi_taxdump.yaml`, `src/taxonmech/ncbi_taxdump.py` and `scripts/extract_source_inventory.py`. Generation belongs to `src/taxonmech/seed.py` and `scripts/seed_from_sources.py`; actual scope changes belong to `curation/seed_scope.tsv`. Enrichment requires explicit source-owned strain/deposit/genome evidence.

## Follow-up Checks

- At source refresh, repeat exact taxonomy, replacement/retirement and JF792130 authority reads.
- Require whole culture identifiers and explicit sequence/genome relationships before enrichment. Keep partial markers outside genome counts and distinguish taxon IDs from assembly statistics.
- Inspect a primary publication with isolate-specific results before phenotype or habitat curation in the appropriate sibling repository.
- After an authorized source or generation change, use the documented dry run and single-record canary, repeat both focused validators, then full `just verify-corpus` and `just qc` before release.

## Additional Notes

Only this new timestamped report was written for this target. Records, inventories, scope, history, prior reports, generated products and Eukaryota reviews remain unchanged. External reads were public and unpaid; no commits, GitHub mutations, contacts, provider-credit jobs or lifecycle promotions occurred.

The existing single worktree was retained because the other Codex session is closed. The full corpus-review goal remains incomplete.
