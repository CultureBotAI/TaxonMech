# YAML Record Review: Geobacillus sp. ZH1

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/geobacillus_sp_zh1.yaml`
- Started UTC: 2026-10-06T19:32:52Z
- Finished UTC: 2026-10-06T19:35:40Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` was read: `NCBITaxon:1035280`, Geobacillus sp. ZH1, species-rank Bacteria under unclassified Geobacillus (`NCBITaxon:2642459`). It carries ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` lifecycle, zero BacDive strains, one NCBITAXON name attestation and one seed event. It asserts no nomenclature, synonyms, taxonomy mappings, genome links, phenotype or causal graph.

Generated YAML is read-only. Future changes belong to maintained source acquisition/extraction, `src/taxonmech/seed.py` or `curation/seed_scope.tsv`, not this file.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/geobacillus_sp_zh1.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/geobacillus_sp_zh1.yaml --out /private/tmp/gz-strict.tsv`: exit 0, one record, zero errors. The actual TSV was read and contains only its header.
- Bounded manual comparisons checked the complete lineage, source inventories, names, scope, path lock, attestation and history. These are not a target-level corpus-reproduction validator.
- Not run: full `just verify-corpus`, `just qc`, tests, rendering, full provenance and history gates. The reproduction script has no target selector; `--max-diffs` limits diagnostic output only.
- `just validate-products` is not applicable: no curator-added graph nodes. Authority/reference checks used the inspected NCBI sources below. No target-specific external history entry was found in the ignored-inclusive bounded search.
- The local `culturebotai-claw` iModulonDB datasets adapter ran before web follow-up. All 28 rows were inspected; none covers Geobacillus. No component query was applicable, and this absence is not biological evidence.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221981`, `data/taxa/PATHS.tsv:14472` and `curation/seed_scope.tsv:322255` agree with the record's identity and scope. The full native name at `data/catalog/ncbi_names-0005.jsonl.gz:31457` is the scientific name, not a synonym or culture accession. Exact scans found no target type-material, merged-ID or dropped-record entry, and no descendants in the pinned backbone.

Live [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035280&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035280) confirm the active taxon, label, species rank, Bacteria placement, parent and genetic code. The full lineage agrees: root, cellular organisms, Bacteria, Bacillati, Bacillota, Bacilli, Caryophanales, Anoxybacillaceae, Geobacillus and unclassified Geobacillus. Datasets includes the root ID omitted from Taxonomy XML's displayed lineage.

The placeholder name does not establish a formally described species or a registered culture deposit. NCBI species rank is nevertheless in repository scope. ZH1 is retained as the source designation; no type-strain status or equivalence to another Geobacillus species is inferred.

## Evidence

The sole attestation correctly counts one NCBI name from the 2026-09-13 snapshot. Exact source-row comparisons found no target LPSN, GTDB, BacDive, GOLD, MediaDive, Madin or BactoTraits inventory assertion. Because the target has no descendants, the empty BacDive direct match also establishes the empty subtree match for this snapshot. `strain_count: 0` means no listed BacDive strain, not that the organism lacks a strain designation or has never been cultured.

An exact nonexpanded NCBI nucleotide search returned one record, [JF803806.1](https://www.ncbi.nlm.nih.gov/nuccore/JF803806.1). Its complete GenBank metadata were read, excluding sequence bases and translation strings. It is a 741-base carboxylesterase mRNA with complete CDS, source strain ZH1 and explicit taxon 1035280; its CDS names protein AEI59125.1 and translation table 11. The source submission gives a hot spring in China. It is a gene/transcript accession, not an assembly or a 16S marker. Its bibliographic entry remains marked unpublished; that source status was not rewritten from a similarly titled later paper.

The exact nonexpanded Assembly ESearch returned zero hits with a phrases-not-found warning. An independent [NCBI Datasets genome request](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035280/dataset_report) returned HTTP 200 and an empty JSON object. These bound the current API checks, not a claim that no sequence or genome can exist elsewhere.

The publisher's [2012 paper abstract and metadata](https://link.springer.com/article/10.1007/s13131-012-0258-0), DOI `10.1007/s13131-012-0258-0`, explicitly discuss a ZH1 carboxylesterase gene expressed in Escherichia coli and assays of the recombinant enzyme. The [2015 PubMed abstract](https://pubmed.ncbi.nlm.nih.gov/26665604/), PMID 26665604, concerns error-prone-PCR mutants and improved enzyme thermal stability. Both support strain-specific literature context; neither supplies a BacDive deposit or assembly relationship. Engineered-enzyme results must not become a wild-type organism-wide phenotype. Full articles were not inspected, and the abstracts are not used for additional assay claims.

The seed event matches the scope's dated NCBI-only inclusion reason. Its timestamp, 2026-09-13T17:54:04Z, is the newest of the raw, ATB and StrainInfo manifests, as `src/taxonmech/seed.py:139` requires. Lifecycle remains SEEDED; this review does not constitute human promotion.

## Completeness

Ignored-independent compressed-content searches used `rg --no-ignore --hidden -n -z -i` for the taxid, label and slug across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All nine candidate rows were read fully in native JSON or TSV form. Three concern this target: backbone, scientific name and scope.

The other six are substring collisions: four source rows for Ruminococcus taxon 3143031 contain BioSample SAMN41035280; one Campylobacter jejuni row contains GCA_010352805.1; one Mycobacterium tuberculosis ATB row contains run ERR1035280. None supplies ZH1 evidence. In particular, the Ruminococcus GTDB classification and paired assembly identifiers must not be transferred here.

A second ignored-inclusive search for JF803806, AEI59125 and the literature spelling ZHl returned no rows within the same roots. Five SOURCE.json files and all history filenames were checked separately for both searches. No matching external history, deposit, eligible strain-genome link or local gene accession was found within these stated bounds. Report-filename discovery also included ignored files and found no earlier report for this stem.

Empty optional fields are appropriate. The repository does not require a general taxon-to-gene catalog, nor may a bare strain name create a BacDive identity. The external transcript and papers are potential evidence for an explicitly maintained future overlay, not required missing genome records. No causal graph or record-level citation is compulsory for an NCBI-only seeded record.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Stored identity, lineage, count semantics, provenance and lifecycle agree with the inspected evidence. Optional literature enrichment is not a curation defect in this generated taxonomic record.

## Recommended Edits

None required. Do not hand-edit YAML, infer a culture accession from ZH1, turn JF803806.1 into a genome link or transfer recombinant/mutant enzyme properties to the whole taxon.

If authorized later, literature or gene enrichment needs a maintained overlay and explicit generator support. New deposit/genome evidence must enter through maintained acquisition/extraction and satisfy existing whole-deposit and source-chain rules before regeneration.

## Follow-up Checks

For any future source refresh, compare exact taxon and accession versions, distinguish transcript from assembly identifiers, and require explicit culture identity before attaching genomes. Rerun the target schema and strict checks after authorized regeneration, then full `just verify-corpus` and `just qc`. Preserve the current NCBI lineage and source-specific evidence scope.

## Additional Notes

The NCBI Taxonomy browser page failed through the web tool; public NCBI XML and Datasets APIs supplied the inspected identity evidence. Publisher and PubMed abstract pages were read directly, not inferred from search snippets. The source-metadata comparisons were bounded reviews, not a full manifest-hash audit or proof of corpus reproduction.

HEAD was `b6a6508faca1388b88feb5740b1095e9f64cfdb8` on `codex/record-review-extensimonas-20261003`. The complete target was reread byte-unchanged. Only this new review report was written for this target; no record, history, lifecycle, site, Git or GitHub state was changed. Eukaryota remained untouched.
