# YAML Record Review: Ligilactobacillus salivarius CELA2

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/ligilactobacillus_salivarius_cela2.yaml`
- Started UTC: 2026-10-09T13:51:21Z
- Finished UTC: 2026-10-09T13:53:59Z
- Verdict: pass

## Target

One generated `TaxonRecord` was reviewed in full: all 74 lines of `NCBITaxon:1036738`, Ligilactobacillus salivarius CELA2. It is a `STRAIN` in `BACTERIA`, below species `NCBITaxon:1624`, not the entire species or a different salivarius isolate. The record carries ten root-first ancestors, three NCBI exact synonyms, genetic code 11, zero emitted BacDive strains, three source attestations, `EXACT` grounding, `SEEDED` mapping status and one seed event.

The file SHA-256 was unchanged across the review: `21bce4d1abc0e6364f340c4349b29ead94ebab22baf49985f1e112a940f754e8`. Generated records are read-only; this report is the only new repository artifact for this review.

## Validation

Both commands exited zero with `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

```bash
just validate data/taxa/bacteria/ligilactobacillus_salivarius_cela2.yaml
just validate-strict data/taxa/bacteria/ligilactobacillus_salivarius_cela2.yaml --out /private/tmp/taxonmech-lsalCela2-review-strict.tsv
```

LinkML found no issues. Strict validation scanned one file, reported zero error rows, and produced a header-only TSV that was read in full. The backbone, every ancestor, exact source-count rows, PATHS/scope identity and seed-event reason were independently compared. Those bounded checks do not substitute for corpus reproduction.

Not checked: full-corpus `just verify-corpus`, `just qc`, `just test`, provenance, history, generated-site and documentation-statistics gates. The corpus verifier has no single-record selector. There are no target graph nodes or separate history records requiring a focused term/history check, and no writer or generator was invoked.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222616` supports identifier, scientific name, rank, parent, code and three exact synonyms. Complete native rows `data/catalog/ncbi_names-0005.jsonl.gz:32174` through line 32177 distinguish the scientific name from the old-genus synonym Lactobacillus salivarius CELA2 and the two equivalent names with `str. CELA2` and `strain CELA2`.

The live [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036738&retmode=xml) confirms those exact source name classes, strain rank, parent 1624 and code 11. The [NCBI Datasets taxonomy response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036738) confirms all ten ancestor IDs including root. The carried lineage is root, cellular organisms, Bacteria, Bacillati, Bacillota, Bacilli, Lactobacillales, Lactobacillaceae, Ligilactobacillus and L. salivarius, with matching labels and ranks in the pinned backbone.

Retaining the old Lactobacillus combination as an exact synonym is supported by NCBI; it does not require changing the current scientific name. No GTDB equivalence, LPSN nomenclatural status or type-strain status is asserted here. Exact-ID scans of complete type-material, merged-ID and dropped inventories found no target rows.

## Evidence

The GOLD attestation is supported by `data/raw/gold_organisms.tsv:505`, which counts one organism, and complete native record `data/gold/organisms.jsonl.gz:10663`: Go0012111, Lactobacillus salivarius CELA2, taxon 1036738, strain CELA2, with an empty culture-collection field. Its old-genus spelling is consistent with the inspected NCBI synonym.

The complete associated project record `data/gold/projects.jsonl.gz:10521`, Gp0012111, explicitly links Go0012111 to PRJNA67405. Its BioSample field is empty. Live [NCBI BioProject PRJNA67405 XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=bioproject&id=67405&retmode=xml) confirms CELA2, taxon 1036738, species 1624, a mono-isolate genome-sequencing objective, and submission by Universidad Complutense de Madrid on 2011-05-26. A project objective is not proof of an available assembled genome, and neither Go0012111 nor Gp0012111 nor PRJNA67405 is a genome accession. The exact-taxon [NCBI Datasets assembly-report query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1036738/dataset_report) returned an empty JSON object, not a released assembly report. This is a bounded query result, not proof that no CELA2 sequence exists anywhere or under another taxon.

`data/raw/madin_taxa.tsv:697` supports one `TRAIT_ASSERTION`. Its underlying individual transformed edge was not inspected: a fresh ignored-independent filesystem search under the configured kg-microbe checkout found no `madin_etal/edges.tsv`. Consequently, this review confirms the committed count but does not infer which phenotype it represents. The NCBI attestation correctly records one `NAME` identity attestation from the 2026-09-13 snapshot; it is not intended to total the scientific name and all synonyms. Counts from the three source units were not summed.

Two primary publications were checked only to the extent needed for strain context and near-match exclusion:

- The publisher's complete abstract for [Martin et al. 2009, DOI 10.1017/S0022029909990124](https://www.cambridge.org/core/journals/journal-of-dairy-research/article/abs/isolation-of-lactobacilli-from-sow-milk-and-evaluation-of-their-probiotic-potential/AECEC98A2230D49D9265065A4FA709F2) explicitly names CELA2 among lactobacilli investigated from sow milk and describes bacteriocin production and in-vitro probiotic-potential testing. The full article was access-restricted and was not claimed as read. No specific mechanism, clinical benefit or new phenotype field was inferred from its abstract.
- For [Martin et al. 2019, DOI 10.3390/nu11040810](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6521265/fullTextXML), article identifiers, the complete abstract, the isolate-to-deposit paragraph and complete Table 3 were inspected in primary article XML. Table 3 separately lists CELA2 with 64.4% survival under the stated simulated gastrointestinal conditions. The intervention strain is CECT 9145, explicitly derived from V4II-90, not CELA2. Its clinical results and deposit identity must not be transferred to this record. The PMC browser route challenged access and the publisher route returned HTTP 429; the public Europe PMC XML succeeded.

Neither paper is cited by the YAML. These bounded checks corroborate a real strain designation and prevent conflation; they do not impose optional phenotype curation on this identity/count record.

## Completeness

Ignored-inclusive searches used `rg --no-ignore --hidden`, with decompression for native catalogs, across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Searches included 1036738, current and old-genus labels, the slug, equivalent-name forms, and CELA2/CELA 2 variants. All 11 matching rows were read in full. Expansion to PRJNA67405, Go0012111 and Gp0012111 returned only the two already inspected GOLD records. The five source metadata JSON files were read structurally; target filename searches also included ignored files under the taxon, report and history roots.

Within those scopes, no source-supported own BacDive strain/deposit, GTDB mapping/genome, LPSN name, BV-BRC genome, GOLD analysis chain, StrainInfo/ATB link, MediaDive/BactoTraits attestation or additional assembly row was found. Complete backbone scanning found no immediate child. The absence statements are local and snapshot-bounded. They do not make global claims about culture collections or sequence availability.

`strain_count: 0` is consistent with the emitted BacDive-entry model, not a denial that CELA2 exists. A sequencing project alone supplies neither a BacDive strain ID nor an eligible collection deposit nor an assembly accession. Omitting optional strain/genome lists, nomenclature, mappings, xrefs, causal edges and phenotype mechanisms is therefore appropriate on the inspected evidence. iModulonDB is not applicable: no gene, regulator, expression module or transcriptomics claim is present.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the reviewed record. NCBI identity and synonyms, full lineage, source counts and units, zero emitted BacDive entries and seeded provenance are consistent with inspected evidence. The inaccessible individual Madin edge and unavailable full 2009 article are explicit verification limits, not contradictory evidence or claimed completed checks.

## Recommended Edits

None required on the evidence inspected. Do not hand-edit the generated YAML, promote its status, fabricate a collection accession, or convert PRJNA67405 into a genome identifier.

Any separately authorized enrichment should first resolve an eligible strain/deposit and an explicit released-sequence chain. Maintained source projection and emission belong in `src/taxonmech/extract.py` and `src/taxonmech/seed.py`, with source evidence and regression tests, rather than changes to the generated record. Preserve the distinction between CELA2 and CECT 9145/V4II-90.

## Follow-up Checks

No corrective validator is pending for a finding. If primary-source refresh or enrichment is later authorized, recheck the project for actual assembly/sample accessions, recover the pinned Madin source edge before adding a phenotype, and validate evidence ownership before any strain-genome join. Re-run the two focused validators, then the repository's reproduction and quality gates for any maintained-input change.

## Additional Notes

`data/taxa/PATHS.tsv:15139` resolves the identifier to this slug. `curation/legacy_page_paths.tsv:900` is a page-path alias, not another biological record. `curation/seed_scope.tsv:36177` records the 2026-09-12 three-source admission reason. The seed event at 2026-09-13T17:54:04Z matches the reason and source names and does not claim a scientific review.

No external history entry was found by ignored-independent content and filename searches. No curation event was appended. Existing reports, Eukaryota, other taxon records, branches and worktrees were unchanged. This independently authored review makes no genome-equivalence or clinical-efficacy claim.
