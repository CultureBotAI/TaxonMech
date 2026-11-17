# YAML Record Review: NC10 bacterium enrichment culture clone SFBR 2

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/nc10_bacterium_enrichment_culture_clone_sfbr_2.yaml`
- Started UTC: 2026-10-06T19:53:44Z
- Finished UTC: 2026-10-06T19:56:49Z
- Verdict: pass with minor issues

## Target

The complete generated `TaxonRecord` was read: `NCBITaxon:1035284`, NC10 bacterium enrichment culture clone SFBR 2. It has species rank, BACTERIA domain, parent environmental samples (`NCBITaxon:671142`), seven root-first ancestors, genetic code 11, EXACT grounding, SEEDED lifecycle, zero BacDive strains, one NCBITAXON name attestation and one seed event. There are no synonym, nomenclature, mapping, genome, phenotype or causal-graph claims.

The target is not the distinct inoc SFBR 2 taxon, 1035285. Generated YAML is read-only; any future correction belongs to maintained source inputs, extraction, scope or seeding. No neighboring record receives a verdict from this review.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/nc10_bacterium_enrichment_culture_clone_sfbr_2.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/nc10_bacterium_enrichment_culture_clone_sfbr_2.yaml --out /private/tmp/n2-strict.tsv`: exit 0, one record, zero errors. The actual TSV was read and contains only the header.
- Bounded manual comparisons verified all lineage fields, inventories, path lock, scope, attestation and seed event. These are not a target-level reproduction gate.
- `shasum -a 256 data/raw/ncbitaxon_taxa.tsv data/catalog/ncbi_names-0005.jsonl.gz` confirmed hashes 97ff340e1eebf62ea541a299e5c798cdcc24ef935c636fb059df48ab45d6f2f6 and 31c672adade0c3485ee5d6817567f7972b06ce3b6853cf191159b76cad3b023c, matching the previously inspected manifest entries. This is a bounded file-consistency check, not full provenance validation.
- The configured original taxdump archive is unavailable locally, so no original names.dmp or archive-hash verification was possible.
- Not run: full `just verify-corpus`, `just qc`, tests, rendering, full provenance and history gates. Corpus reproduction has no target selector; `--max-diffs` limits diagnostics only. `just validate-products` is not applicable because there are no curator-added graph nodes.
- The local iModulonDB dataset adapter initially failed DNS resolution in the sandbox; an authorized public-network retry exited 0 before external follow-up. All 28 rows were read, with no NC10/Methylomirabilota coverage. No component query applies, and lack of coverage is not biological evidence.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:221985`, path lock `data/taxa/PATHS.tsv:14476`, scope `curation/seed_scope.tsv:322259` and native scientific-name row `data/catalog/ncbi_names-0005.jsonl.gz:31461` agree on this target. Exact type-material, merged-ID and dropped-record scans found no target entry. The pinned backbone has no descendants.

Live [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035284&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035284) confirm the active taxon, canonical label, species rank, parent and genetic code. The entire stored lineage agrees: root, cellular organisms, Bacteria, Bacteria incertae sedis, Bacteria candidate phyla, Methylomirabilota (SeqCode) and environmental samples. Datasets confirms the root ID absent from the XML lineage display.

NCBI's Environmental samples division is compatible with the ancestry-derived BACTERIA domain. Species rank does not establish a described species, pure isolate, culture deposit or type strain. The phylum's SeqCode label is carried taxonomy, not a nomenclature assertion for this clone.

The XML includes NC10 bacterium enrichment culture clone SFBR- 2 as name class misspelling. The minus sign is source-supported; it must not be replaced with the plus sign carried by other SFBR clones. The canonical SFBR 2 label is correct.

## Evidence

The single NCBITAXON attestation correctly counts one pinned name and names the 2026-09-13 snapshot. Exact inventory comparisons found no target BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row. Zero BacDive strains is consistent with the inventories; it does not deny the existence of an enrichment culture.

An exact nonexpanded nucleotide search returned one sequence, [JF803482.1](https://www.ncbi.nlm.nih.gov/nuccore/JF803482.1), UID 337730222. All GenBank metadata were inspected, excluding bases. It is a 417-base partial 16S rRNA marker with ENV division/keyword and an environmental_sample qualifier. Its organism and taxon xref identify 1035284; its definition and clone qualifier retain SFBR- 2. It records Ooijpolder, Netherlands, collection date 29-Oct-2009 and direct submission on 13-Apr-2011. The collection date differs from other SFBR clone markers and is not copied from them. This is not an assembly, registered deposit or pure-isolate proof.

The accession explicitly cites [PMID:22657102](https://pubmed.ncbi.nlm.nih.gov/22657102/) and DOI `10.1016/j.jhazmat.2012.05.032`. Public PubMed EFetch verified their correspondence, bibliography and full abstract. The paper concerns enrichment of denitrifying methanotrophs resembling Candidatus Methylomirabilis oxyfera and reactor-level behavior. It provides study context, not clone-specific rates or identity with that named species. Full text was not inspected, and no reactor phenotype is attributed to this clone.

An exact nonexpanded Assembly ESearch returned zero hits with a phrases-not-found warning. An independent [NCBI Datasets genome query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035284/dataset_report) succeeded and returned an empty object. This bounds the queries, not genome availability everywhere.

The seed-event scope reason agrees with the maintained scope row. Its timestamp 2026-09-13T17:54:04Z is the newest of the raw, ATB and StrainInfo manifest extraction times, consistent with `_seed_timestamp` in `src/taxonmech/seed.py:139`. Lifecycle remains SEEDED.

## Completeness

Ignored-inclusive, compressed-content searches used `rg --no-ignore --hidden -n -z -i` for identifier, label/clone designation and slug across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 12 candidates were read in full native JSON or TSV form, including nested content.

Three rows are the target's backbone, scientific name and scope. Three are the corresponding rows for the distinct inoc SFBR 2 taxon, 1035285. Four contain unrelated Streptococcus anginosus BioSample SAMN41035284, including its GenBank/RefSeq assembly pair, BV-BRC record and GTDB assignment to Streptococcus vaginalis. Two concern Mycobacterium tuberculosis run ERR1035284, one BV-BRC and one ATB. These sample/run substrings, source classifications and genome relationships are not evidence for SFBR 2.

A second ignored-inclusive search for JF803482 or SFBR- 2 found no rows in those same ten roots. All five SOURCE.json files and history filenames were inspected separately for both queries, with no additional target evidence or external history. Ignored-inclusive report-filename discovery found no prior review for this stem.

The configured archive was absent at `data/source_snapshots/ncbi-new-taxdump-2026-09-13.tar.gz`; an ignored-independent filename search under `data` and `/private/tmp` also found no taxdump artifact. This does not establish absence elsewhere on the machine.

No supported missing strain-genome join, nomenclature entry or additional attestation was found within these bounds. Marker/literature enrichment and causal graphs are optional for a seeded NCBI-only record. The alternate spelling is the narrow traceability gap.

## Findings

Counts: 0 blocker, 0 major, 1 minor.

**Minor: the current NCBI misspelling alias is missing from the pinned name representation.** Taxonomy explicitly associates SFBR- 2 with 1035284, and JF803482.1 independently preserves it. The native catalog, raw synonym fields and YAML contain only the canonical form. A source-backed related synonym would improve traceability without changing canonical identity.

Both relevant committed projection hashes agree with the manifest entries. Without the original pinned archive, it remains unresolved whether this is a snapshot/API discrepancy or acquisition/projection loss. `src/taxonmech/ncbi_taxdump.py:81` maps misspelling-class names to RELATED_SYNONYM, not EXACT_SYNONYM, and `scripts/build_source_catalog.py:92` preserves all prokaryotic name classes. An extractor defect is not established.

Maintained owners are `conf/ncbi_taxdump.yaml`, the pinned capture, `src/taxonmech/ncbi_taxdump.py` and `scripts/build_source_catalog.py`, followed by generation through `src/taxonmech/seed.py`. The finding is non-blocking provenance/name coverage, not wrong identity.

## Recommended Edits

During an authorized source refresh, reconcile SFBR- 2 with a verified primary names.dmp snapshot or an explicitly modeled API overlay. If that maintained input supplies the name, preserve its misspelling class in the catalog and related-synonym scope downstream. Do not rename the canonical taxon, make the alias exact, replace minus with plus, merge inoc SFBR 2 or patch generated YAML.

No other change is required by the inspected evidence. Optional literature enrichment needs a maintained overlay and claim-specific support, with clone, enrichment, marker, deposit, sample and genome identity kept distinct.

## Follow-up Checks

Recover the original archive with SHA-256 `8b32317216712ecf04f4c9b65e7ab82dacbd0a0e5512dd7aa904e24cc6bc0955` and inspect all names.dmp rows for 1035284. If the alias is absent, document the snapshot/API difference; if present, trace its extraction and catalog projection. Test minus-sign preservation and related scope without merging neighboring clones.

After authorized changes, regenerate through the validated writer, rerun the two target validators, then full `just verify-corpus` and `just qc`. Any physiological addition also requires inspected primary methods/results at the appropriate scope. No refresh, history append or lifecycle promotion occurred here.

## Additional Notes

HEAD was `b6a6508faca1388b88feb5740b1095e9f64cfdb8` on `codex/record-review-extensimonas-20261003`. The target was reread byte-for-byte unchanged. Only this new report was written for this target; no record, generated site or Git/GitHub state was changed. Eukaryota remained untouched.

