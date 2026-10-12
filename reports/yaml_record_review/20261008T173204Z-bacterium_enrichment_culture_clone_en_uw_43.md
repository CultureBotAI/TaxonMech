# YAML Record Review: bacterium enrichment culture clone En_UW_43

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_43.yaml`
- Started UTC: 2026-10-08T17:27:23Z
- Finished UTC: 2026-10-08T17:32:04Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` for `NCBITaxon:1036429`, bacterium enrichment culture clone En_UW_43, was read before judgment. It carries rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:48479`, genetic code 11, `EXACT` grounding, `SEEDED` mapping status and zero associated strain records. This is an NCBI environmental-clone taxon; species rank does not establish a formally named species or a pure culture.

An ignored-inclusive filename search of `data/taxa/`, `reports/yaml_record_review/` and `history/` resolved exactly one YAML for the identifier, slug and clone-label pattern and found no previous report for the stem. No other record was judged as part of this review. Generated YAML, maintained inputs, history and status remain unchanged.

## Validation

The following focused commands completed with the existing environment, `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `just validate data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_43.yaml`: pass, no issues found.
- `just validate-strict data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_43.yaml --out /private/tmp/uw43-strict.tsv`: pass, one file scanned, zero files with errors and zero error rows. The complete TSV contains only its header.
- Structured comparison of all populated record fields with the applicable pinned backbone, lineage, source attestation, scope, path-index and seed-event evidence: pass.
- Current primary taxonomy and linked nucleotide/protein inspection: completed, with limitations recorded below.

Not checked: full-corpus `just verify-corpus`, `just provenance-check`, `just validate-history`, `just qc`, `just test`, vendored synchronization, global statistics and generated-site drift. Focused source comparison is not proof of corpus reproduction. No unsupported per-record reproduction/history command was invented. The embedded seed event was manually checked against its source and scope rows; the bounded history search found no matching standalone artifact.

Graph grounding validation is not applicable because the YAML contains no curator-added graph. iModulonDB was not run: there is no stored gene, regulator, pathway or expression-module claim, and this environmental clone was not resolved to a covered strain/dataset. This is not negative evidence about the contents of iModulonDB.

## Identity and Grounding

The complete relevant rows were inspected at `data/raw/ncbitaxon_taxa.tsv:222431`, `data/catalog/ncbi_names-0005.jsonl.gz:31975`, `data/taxa/PATHS.tsv:14938` and `curation/seed_scope.tsv:322678`. Identifier, scientific label, rank, parent, genetic code and snapshot date agree. Source synonym fields and the YAML synonym set are empty. The root-first four-ancestor lineage, including labels and ranks, matches the pinned backbone. A complete backbone comparison found no direct children for this identifier.

Live [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036429&retmode=xml) confirms the scientific name, species rank, parent 48479 and genetic code 11. [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036429) supplies the same four ancestor IDs: 1, 131567, 2 and 48479. EFetch's omission of root from `LineageEx` is a representation difference, not disagreement with the YAML. Its environmental-samples division is compatible with bacterial domain placement. No additional names were supplied in the inspected response.

Exact scans of the pinned type-material, merged-ID and dropped-record inventories found no target rows. `EXACT` is supported for the NCBI identity; it is not a claim of cultured-species resolution. No broader taxon, neighboring clone, reference sequence or deposit is substituted for this target.

## Evidence

The single `NCBITAXON` attestation agrees with the scientific-name and backbone rows: one assertion with unit `NAME`, not a strain/genome count. Its 2026-09-13 snapshot note is consistent. The embedded 2026-09-13 seed event and scope reason agree, with no unsupported review promotion. This read-only report does not change `SEEDED` to `REVIEWED`.

An exact, non-expanded Nuccore search for `txid1036429[Organism:noexp]` returned one UID, 336092272. The complete [HQ630102.1 GenBank XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=336092272&rettype=gb&retmode=xml) was read, including every feature and the sequence. It explicitly identifies En_UW_43 and taxon 1036429, with 341 bases of partial `nosZ`. Both CDS ends are partial; codon start is 3 and translation table 11. The source is an environmental sample from an anode biofilm, with a Na2S2O3-supplemented mineral-medium note. There are no strain, culture-deposit or geographic source qualifiers. The study reference is unpublished and the direct submission is dated 17 November 2010. These annotations support a submitted fragment, not a pure isolate, measured enzyme activity or a whole-genome phenotype.

The linked [AEI00760.1 protein XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&id=AEI00760.1&rettype=gb&retmode=xml) was independently opened and read in full. It contains 113 amino acids, identifies the same clone/taxon and points back to the partial HQ630102.1 CDS. Actual lengths match the declared nucleotide and protein lengths, and the submitted translation exactly matches this protein sequence. The focused character check detected no non-ACGT base or X/B/Z/J amino-acid ambiguity. This verifies annotation consistency, not an independent translation, alignment or biochemical assay. Its computational PRK02888/CDD:235082 region spans less-than-1 through residue 113. The region annotation's validation label is not experimental proof of activity for this clone.

The cached 164-page [Vilar Sanz dissertation](https://dugi-doc.udg.edu/bitstream/handle/10256/12459/tavs1de1.pdf?sequence=5), dated 2015, had no extracted-text match for HQ630102 or the clone label. Printed pages 54 and 92 were reread in full. The former gives an enrichment-sequence accession range containing HQ630102; the latter explains why a single DGGE band cannot prove culture purity. This is study context, not a species identification. The search excludes a comprehensive raster-text or supplementary-material audit.

Searches for HQ630102 and En_UW_43 in the main HTML of the related [PLOS ONE article](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0063460) returned no matching text. No supplements were exhaustively audited. Exact web queries for HQ630102 and AEI00760, plus a clone query excluding the already inspected NCBI taxonomy listing, returned no results. These are bounded discovery outcomes, not evidence that no publication exists. Community performance and neighboring-clone archive memberships were not transferred to this record.

## Completeness

The supported taxonomy and provenance fields are complete enough for this seed. Optional synonyms, nomenclature, mappings, strains, deposits, genome links, traits and causal graphs do not need unsupported values. Zero associated strains matches the inventory evidence; it does not imply that the organism cannot be cultured.

All seven applicable raw inventories were scanned for the exact identifier: BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits returned no target rows. The compressed-content search used `rg --no-ignore --hidden -n -z -i` over `data/raw/`, `data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`, `data/seqcode/`, `data/straininfo/`, `data/atb/`, `curation/` and `history/`. The identifier, slug and clone-label pattern returned three rows, all inspected completely: backbone, scientific name and scope.

An expanded search adding HQ630102, AEI00760, the submitted study title and the related PLOS DOI returned the same three rows. All five applicable `SOURCE.json` metadata files, excluded from that content scan, were separately read without finding a target identity match. An ignored-independent history filename search found no matching artifact. These are absence findings for the stated local roots and patterns, not all possible data sources.

The exact Assembly query returned zero items with a phrase-not-found warning. It does not establish universal genome absence. No strain/deposit-to-genome association was established from the inspected evidence. The partial gene was not treated as a genome, nor as grounds to add organism-level traits.

## Findings

None found in the record's supported claims.

Counts: 0 blocker, 0 major, 0 minor.

Unresolved environmental-clone identity and limited partial-sequence evidence constrain future biological enrichment but do not contradict this taxonomy-only YAML. No invalid shape, broken stored reference, source conflict, unsupported phenotype or status inflation was identified.

## Recommended Edits

None required. Preserve the generated record and `SEEDED` status.

Any future authoritative taxonomy correction belongs first at NCBI and then in the pinned ingestion workflow, maintained in `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Seeder defects belong in `src/taxonmech/seed.py` with focused tests; scope decisions belong in `curation/seed_scope.tsv`. These routes are recorded for future curation, not as requested changes. Generated YAML must not be patched directly.

## Follow-up Checks

No blocker remains for this record-level verdict. Future strain or phenotype curation requires an explicit clone-to-organism/deposit connection and claim-specific evidence. Preserve the partial-sequence qualifiers and distinguish computational annotation from measured function. Optional supplementary or broader literature searches are not a prerequisite to accepting the present seed.

After an authorized maintained-input change, use the documented canary workflow, inspect the generated record, rerun the focused schema and strict validators, then run the applicable corpus reproduction, provenance, history and QC gates. No generation was run or global gate claimed as passed by this review.

## Additional Notes

This is one sequential individual review. Eukaryota, all other record YAMLs and existing worktrees were left untouched. No curation-history event, status promotion, source refresh, generated output, paid research, outbound communication or GitHub mutation was performed.

The target's SHA-256 was unchanged before and after review: `c6be5954914dad4e9d961301afdac9df39ddbd81a515c3ff3ec6ee9987c119f0`.

Exactly one new timestamped Markdown report is the repository write for this review. Search outcomes and evidence limits above should not be read as a universal census of knowledge about En_UW_43.
