# YAML Record Review: Enterobacter sp. CCF01Et-UAEM

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/enterobacter_sp_ccf01et_uaem.yaml`
- Started UTC: 2026-10-06T19:36:44Z
- Finished UTC: 2026-10-06T19:39:23Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` was read: `NCBITaxon:1035281`, Enterobacter sp. CCF01Et-UAEM, species-rank Bacteria under unclassified Enterobacter (`NCBITaxon:2608935`). It stores ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` lifecycle, zero BacDive strains, one NCBITAXON name attestation and one seed event. Synonyms, nomenclature, mappings, genomes, phenotypes and causal graphs are not asserted.

Generated YAML is read-only. Future fixes belong to maintained acquisition/extraction, `src/taxonmech/seed.py` or `curation/seed_scope.tsv`, not the generated file.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/enterobacter_sp_ccf01et_uaem.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/enterobacter_sp_ccf01et_uaem.yaml --out /private/tmp/ec-strict.tsv`: exit 0, one file, zero errors. The actual output TSV was read; only its header is present.
- Manual bounded comparisons checked the full backbone lineage, source rows, scope, path lock, attestation, names and lifecycle. These are not a target-level corpus-reproduction validator.
- Not run: full `just verify-corpus`, `just qc`, tests, rendering, full provenance and history gates. `scripts/verify_corpus.py` has no target selector; `--max-diffs` only limits diagnostics.
- `just validate-products` is not applicable because no curator-added graph nodes exist. Authority and literature references were checked using the primary services below. No target-specific external history entry was found in the ignored-inclusive bounded search.
- The local `culturebotai-claw` iModulonDB dataset adapter ran before web follow-up. Its complete 28-row output contains no Enterobacter dataset. No component query was applicable; Escherichia coli datasets cannot substitute for this strain, and absence from iModulonDB is not negative biological evidence.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:221982`, path lock `data/taxa/PATHS.tsv:14473` and scope `curation/seed_scope.tsv:322256` identify exactly this target. The native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31458` preserves the label and capitalization. The backbone has no descendants; exact type-material, merged-ID and dropped-record scans found no target entry.

Live [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035281&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035281) confirm the active identity, species rank, parent, Bacteria placement and genetic code. All stored ancestors agree: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Enterobacterales, Enterobacteriaceae, Enterobacter and unclassified Enterobacter. Datasets confirms the root ID omitted from the XML lineage display.

The placeholder is eligible because NCBI assigns species rank. Its strain designation does not prove a registered culture deposit, formal species description, type-strain status or equivalence to another Enterobacter taxon. No such claims are stored.

## Evidence

The NCBITAXON attestation correctly states one name and the 2026-09-13 taxonomy snapshot. Full exact-row comparisons found no target BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits assertion. With no descendants, the BacDive subtree is also empty. `strain_count: 0` counts BacDive records, not whether the source organism has a strain designation or has been isolated.

An exact nonexpanded nucleotide search returned one record, [JF837335.1](https://www.ncbi.nlm.nih.gov/nuccore/JF837335.1). Its full metadata, excluding bases and translation strings, identify 1,106 bases of genomic DNA from strain CCF01Et-UAEM and taxon 1035281. Source qualifiers specify agricultural soil in Morelos, Mexico. The opdE CDS occupies positions 133 through 894, uses translation table 11 and names protein AEH22107.1. This is a gene fragment with complete CDS, not a genome assembly, 16S marker or culture deposit.

The sequence explicitly cites [PMID:22065283](https://pubmed.ncbi.nlm.nih.gov/22065283/) and DOI `10.1007/s10532-011-9517-6`. PubMed EFetch verified their correspondence and supplied the full abstract. The [publisher abstract and bibliographic page](https://link.springer.com/article/10.1007/s10532-011-9517-6) agree on the article and describe an opdE study using Enterobacter strain Cons002. Publication was online in November 2011 and in the June 2012 issue of Biodegradation, pages 387-397.

There are two unresolved external-source distinctions: the paper abstract calls the strain Cons002, whereas the accession says CCF01Et-UAEM, and the abstract describes a 753-base gene whereas current accession coordinates span 762 bases. The explicit accession-to-paper reference supports a bibliographic association, not a verified culture identity or resolution of the length difference. Full text and underlying sequence revisions were not inspected. No Cons002 synonym, gene-length statement or pesticide-degradation phenotype is stored in this YAML, so these are follow-up boundaries for possible enrichment, not current record defects.

The exact nonexpanded NCBI Assembly search returned zero hits with a phrases-not-found warning. An independent [NCBI Datasets genome request](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035281/dataset_report) returned HTTP 200 and an empty object. Neither result makes a universal claim that no genome exists elsewhere. The paper's chromosome characterization is not an assembly accession and cannot supply a genome link.

The scope reason and single-source seed-event text agree. Its 2026-09-13T17:54:04Z timestamp is the newest of the raw, ATB and StrainInfo manifests, matching `src/taxonmech/seed.py:139`. Lifecycle remains SEEDED; this read-only review is not human approval.

## Completeness

Ignored-inclusive compressed-content searches used `rg --no-ignore --hidden -n -z -i` for the taxid, designation, label and slug across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All 13 candidate rows were read fully as native JSON or TSV, including nested values.

Three rows concern this target: backbone, scientific name and scope. The other ten are numeric collisions: four Schaalia turicensis rows contain BioSample SAMN41035281; three Halalkalibacter rows contain BioProject PRJNA1035281; two Mycobacterium tuberculosis rows contain run ERR1035281; one Thermoproteota archaeon row has genome size 1035281. Their classifications, genomes, sample/project IDs and source counts must not be transferred here.

A follow-up search for JF837335, AEH22107 and the shorter designation CCF01Et returned only the same three target rows, with no local gene accession. A separate search for Cons002 and separator variants returned no rows within the same roots. All five SOURCE.json files and history filenames were inspected separately for each search; no additional target metadata or history entry appeared. Report-filename discovery included ignored files and found no earlier report for this stem.

No supported deposit, strain-genome join, taxonomy mapping, nomenclature entry or missing attestation was found within these bounds. Empty optional slots are appropriate. Literature citations and a general taxon-to-gene catalog are not required for an NCBI-only seeded record, and gene evidence cannot create a BacDive strain. The biological designation and study-linked gene remain useful external context without inventing identity equivalences.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the reviewed YAML. Stored identity, lineage, source semantics, provenance and lifecycle agree with inspected evidence. The external strain-label and gene-length discrepancies do not affect a claim currently asserted by the record.

## Recommended Edits

None required. Do not hand-edit generated YAML, promote JF837335.1 to a genome identifier or infer Cons002 as an exact synonym from the citation alone.

Optional future literature enrichment requires an explicitly maintained overlay and generator support. Before it asserts strain equivalence, resolve CCF01Et-UAEM versus Cons002 through inspected primary methods or deposit records and resolve the accession/paper length difference. Any new strain-genome association must enter maintained acquisition/extraction with explicit deposit and source-chain evidence.

## Follow-up Checks

For authorized enrichment, inspect the full original article and relevant accession history, verify the precise strain identity, and keep gene sequence, chromosome characterization, culture deposit and genome assembly separate. Do not transfer a consortium-wide or related-strain phenotype. After authorized input changes and validated regeneration, rerun the target schema and strict validators, full `just verify-corpus` and `just qc`.

## Additional Notes

The Taxonomy browser page failed through the web tool. Public NCBI XML and Datasets APIs supplied the inspected identity evidence. The PubMed browser response contained only boilerplate; the independent EFetch response supplied the actual bibliographic record and abstract. The publisher page exposed abstract/metadata, not the full article. Search snippets and secondary aggregators were not treated as evidence.

HEAD was `b6a6508faca1388b88feb5740b1095e9f64cfdb8` on `codex/record-review-extensimonas-20261003`. The complete record was reread byte-unchanged. Only this new report was written for this target. No history entry, lifecycle promotion, source refresh, regeneration, Git/GitHub mutation or Eukaryota review occurred.
