# YAML Record Review: Wolbachia endosymbiont of Lepidoptera sp.

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_lepidoptera_sp.yaml`
- Started UTC: 2026-10-09T09:08:37Z
- Finished UTC: 2026-10-09T09:12:46Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1036669`, Wolbachia endosymbiont of Lepidoptera sp. It asserts species rank, Bacteria, parent 2640676, eleven root-first ancestors, code 11, `EXACT` grounding, `SEEDED` mapping status, zero represented BacDive strains and one NCBITAXON name attestation. The seed event is dated 2026-09-13T17:54:04Z.

Ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` uniquely resolved this YAML and found no prior target report. Synonyms, nomenclature, mappings, deposits, genomes, phenotypes, discussion and graphs are unasserted. Generated YAML is not a maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/wolbachia_endosymbiont_of_lepidoptera_sp.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/wolbachia_endosymbiont_of_lepidoptera_sp.yaml --out /private/tmp/taxonmech-wolbachia-lep-review-strict.tsv`: passed, one file and zero errors; complete TSV was header-only.
- Structured comparisons matched own identity, every ancestor, PATHS, scope reason, attestation and seed wording. Exact scans covered seven supplemental raw inventories, type material, merged IDs and dropped taxa.
- Marker consistency checks found declared and actual lengths of 938 for MG384538.1 and 639 for JF902213.1. The former has only ACGT; the latter has W at position 59. This is a length/alphabet check, not independent alignment, CDS translation verification or strain identification.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Focused comparisons do not prove corpus reproduction. Embedded history was read; ignored-inclusive content and filename searches found no separate target history artifact within the stated roots. Graph-product validation is inapplicable without nodes.

## Identity and Grounding

Complete [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036669&retmode=xml) and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036669) responses agree with label, species rank and lineage. EFetch confirms parent 2640676 and code 11; Datasets includes root. Ancestors are root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Alphaproteobacteria, Rickettsiales, Anaplasmataceae, Wolbachieae, Wolbachia and unclassified Wolbachia.

Live taxonomy has no other names, pinned synonym fields are empty, and no own type-material, merged-ID or dropped-taxon row, or backbone child, was found. Species rank is an NCBI classification, not evidence of formal nomenclatural standing or one biologically homogeneous strain. The host-order wording is not a claim that all Wolbachia associated with Lepidoptera belong to this node.

Complete live EFetch and Datasets responses for 1084559 identify a separate species node, Wolbachia sp. MHMYB170-09, also parented by 2640676, with no other names. Its specimen-like name overlaps the Costa Rican marker below, but the current authority does not present it as a synonym or merge of 1036669. Preserve that unresolved provenance relationship rather than collapsing the nodes.

## Evidence

Complete own rows inspected: `data/raw/ncbitaxon_taxa.tsv:222572`, `data/catalog/ncbi_names-0005.jsonl.gz:32116`, `data/taxa/PATHS.tsv:15089` and `curation/seed_scope.tsv:322819`. Snapshot 2026-09-13, one-name unit and admission reason support the attestation and seed event. Exact target scans found no row in the BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits raw inventories. A name count is not a genome or experiment count.

Exact Nuccore taxon-ID and organism-name queries both returned the same two records. Complete GenBank XML, references, features, translations and nucleotide sequences were inspected for both.

[JF902213.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902213.1), UID 334360783, is a 639-base partial COI gene marker, code 11 and codon start 1, with both CDS ends partial. It identifies taxon 1036669, host Lepidoptera sp., Costa Rica, specimen voucher `BIOUG<CAN>:MHMYB170-09.w`, BOLD ASLEP089-10.COI-5P and identifier Alex Smith. The source supplies PCR primers but no cultured-deposit, genome, collection-date or finer locality annotation. Creation/update date is 30-APR-2012; references comprise an unpublished Smith barcoding title and direct submission dated 01-MAY-2011 from the University of Guelph. Its protein accession is AEG78034.1. The ambiguous base and translated X remain source-reported uncertainty, not a YAML defect.

[MG384538.1](https://www.ncbi.nlm.nih.gov/nuccore/MG384538.1), UID 1486392388, is a 938-base partial ftsZ coding sequence, code 11 and codon start 2, with both CDS ends partial. Its six source qualifiers identify the same taxon, genomic DNA, host Lepidoptera sp., India and collector Pradeeksha Shetty. No specimen voucher, collection date, culture deposit, BioSample or assembly accession is supplied. The Sanger sequencing comment uses an Assembly-Data block, but this does not turn the single-gene record into a genome assembly. Protein accession AYF52849.1 is likewise not a genome identifier.

MG384538.1 was created/updated 09-OCT-2018. Pradeeksha, Puttaraju, Jalali and Kandan are listed on an unpublished diversity-study reference and a direct submission dated 01-NOV-2017 from Bangalore University. No DOI or PMID is supplied in the marker. This submission supports source-reported provenance, not demonstrated reproductive effects, host specificity or experimental characterization of the annotated protein.

The different locations, loci and submission histories do not establish that the two markers represent one strain or specimen. Their shared taxon ID is classification evidence only.

The primary [Smith et al. 2012 barcoding paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0036514), DOI 10.1371/journal.pone.0036514, PMID 22567162 and PMCID PMC3342236, was read during this turn through its complete PubMed abstract, bibliographic identifiers and selected primary HTML Discussion, Methods and supporting-information text. Methods explain the .w host-extract identifier convention. Its [Table S2](https://journals.plos.org/plosone/article/file?id=10.1371%2Fjournal.pone.0036514.s003&type=supplementary) was searched anew for this target and its markers across all cells of all four sheets. Headers and the sole matching row, Wolbachia CO1 row 248, were read in full. The exact accession, BOLD process and voucher link JF902213 to that specimen.

Row 248 supplies field/catalog number 08-SRNP-42270, collection 08-Jan-2009 by Anabelle Cordoba at Sendero Rincon, Costa Rica, and Hesperiidae in Extra Info. This is narrower host context than the GenBank order-level label, not evidence that the Indian sample has the same host family. The row's Wolbachia sp. MHMYB170-09 name overlaps the separate taxonomy node above, while current GenBank assigns the accession to 1036669. The workbook length field says 639[1n], whereas current sequence uses W, not a literal N; the raw ambiguous call should not be normalized away. Historical bacterial Family Rickettsiaceae differs from current Anaplasmataceae. The workbook internally says Table S1 although its publisher calls it Table S2. These contextual differences do not contradict the YAML's current NCBI-grounded claims.

## Completeness

Complete enough for supported taxonomy-seed claims. The two gene markers are useful bounded enrichment leads, not missing genome links. Zero represented BacDive strains does not deny the sampled endosymbionts' existence. No inspected source establishes a cultured-deposit-to-genome relationship for this target.

Gitignore-independent `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Initial terms were word-bounded 1036669, exact slug and literal full name. Expansions added MG384538 and JF902213 with optional .1, UIDs 1486392388/334360783, MHMYB170-09, ASLEP089-10, 1084559 and 08-SRNP-42270. The broad host-order name alone was not treated as an exact-taxon key.

Eight final rows were fully read in native form: four TSV and four JSON rows. Besides the three own rows, `data/raw/ncbitaxon_taxa.tsv:233026`, `curation/seed_scope.tsv:331573` and `data/catalog/ncbi_names-0005.jsonl.gz:44826` represent 1084559. Two other rows are numerical collisions, not Wolbachia links: `data/catalog/gtdb_genomes-0000.jsonl.gz:26868` is RS_GCF_001846505.1, Mycobacterium tuberculosis, taxon 1773, matching N50 values 1036669; `data/catalog/ncbi_genbank-0062.jsonl.gz:9126` is GCA_963549975.1, uncultured Kingella sp., taxon 159270, matching genome lengths 1084559. Their native rows suffice to reject these matches; their remote records were not independently revalidated.

Five SOURCE.json files were separately parsed in full for the expanded terms, with no matching keys or values; history filenames were independently inventoried. Search completeness is limited to those roots and terms. The supplement search found no additional matches in its other three sheets; nonmatching study rows were not individually adjudicated.

Exact Assembly taxon query and Nuccore query for the near-name taxon 1084559 returned zero with missing-phrase/no-items diagnostics, not proof of global absence. PubMed rejected the quoted target name and expanded it to Wolbachia AND endosymbiont AND Lepidoptera, returning 67 IDs. Those abstracts were not individually adjudicated and do not form an exact-taxon literature census. The two-accession PubMed query returned zero with both accessions unrecognized; Pradeeksha[Author] AND Wolbachia returned zero with an author-term-not-found diagnostic. Neither establishes absent literature.

Web queries used both accessions, the diversity-study title and submission authors. A HAYATI bibliographic lead led to a [2025 publisher page](https://journal.ipb.ac.id/hayati/article/view/51095) whose complete abstract concerns Hypothenemus hampei mitochondrial COI population genetics. Its PDF timed out; search excerpts and the landing page do not establish an MG384538-specific publication link. No result was promoted to evidence for the target's phenotype. Whole-paper, figure and exhaustive literature review are not claimed.

iModulonDB was not run: the YAML asserts no gene, regulator or expression claim and no applicable target strain/dataset was established. Empty optional fields are not automatic defects.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in stored claims. Identity, lineage, source attestation and admission agree with pinned and live authorities. The specimen-code overlap with 1084559 is an unresolved upstream enrichment question, not demonstrated wrong grounding in the current taxonomy seed.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Future taxonomy corrections belong first at NCBI, then pinned inputs governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection fixes belong in `src/taxonmech/seed.py` with tests; admission changes belong in `curation/seed_scope.tsv`. Do not merge nodes on specimen-code similarity or infer common strain identity from shared taxonomy.

## Follow-up Checks

Optional enrichment should inspect accession/taxonomy history for the MHMYB170-09 overlap and retain the supplement's provenance separately from current GenBank annotation. The Indian marker requires its own specimen and host-identification chain. Any future gene evidence must remain typed as a related sequence rather than a genome; cultured-deposit and assembly joins need explicit independent support. No alignment, independent translation verification, genome comparison or experimental reanalysis was performed.

After an authorized maintained-input change, run focused tests, `just seed-canary NCBITaxon:1036669`, inspect output, rerun both individual validators and `just verify-corpus`, then full publication QC. No regeneration ran.

## Additional Notes

Independent review followed the local skill/checklist; no neighboring verdict was inherited. Entire YAML, eight local candidate rows, own and near-name live taxonomy, two full marker XML records and the target-specific supplement row were inspected. The public XLS was reused from the current review session and read with temporary xlrd without workbook or dependency changes; its verified SHA-256 is `8df12e221a835a4504e4ce0a30e5aed17a4e906c9bc2e1bffcd4113adf0f0a1e`.

Before/after YAML SHA-256: `d06ad5b500c5d42a4d148cc470df09fa352d2fb3fa9846cee2733d25c77d9a1b`. Only this new report was written in the repository for the target. This review did not change YAML, sources, status, history, pages, Eukaryota, GitHub objects or worktrees.
