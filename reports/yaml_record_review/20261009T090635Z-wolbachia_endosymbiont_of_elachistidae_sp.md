# YAML Record Review: Wolbachia endosymbiont of Elachistidae sp.

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_elachistidae_sp.yaml`
- Started UTC: 2026-10-09T09:01:18Z
- Finished UTC: 2026-10-09T09:06:35Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1036668`, Wolbachia endosymbiont of Elachistidae sp. It asserts species rank, Bacteria, parent 2640676, eleven root-first ancestors, code 11, `EXACT` grounding, `SEEDED` mapping status, zero represented BacDive strains and one NCBITAXON name attestation. The seed event is dated 2026-09-13T17:54:04Z.

Ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` uniquely resolved this YAML and found no prior target report. Synonyms, nomenclature, mappings, deposits, genomes, phenotypes, discussion and graphs are unasserted. Generated YAML is not a maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/wolbachia_endosymbiont_of_elachistidae_sp.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/wolbachia_endosymbiont_of_elachistidae_sp.yaml --out /private/tmp/taxonmech-wolbachia-elach-review-strict.tsv`: passed, one file and zero errors; complete TSV was header-only.
- Structured comparisons matched own identity, every ancestor, PATHS, scope reason, attestation and seed wording. Exact scans covered seven supplemental raw inventories, type material, merged IDs and dropped taxa.
- Declared and actual lengths agree for all four contextual COI markers below. JF902198.1 has N bases at positions 309, 588 and 590; the other three contain only ACGT. This is not CDS translation verification, alignment or an identity test for the reviewed taxon.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Focused comparisons do not prove corpus reproduction. Embedded history was read; ignored-inclusive content and filename searches found no separate target history artifact within the stated roots. Graph-product validation is inapplicable without nodes.

## Identity and Grounding

Complete [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036668&retmode=xml) and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036668) responses agree with label, species rank and lineage. EFetch confirms parent 2640676 and code 11; Datasets includes root. Ancestors are root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Alphaproteobacteria, Rickettsiales, Anaplasmataceae, Wolbachieae, Wolbachia and unclassified Wolbachia.

Live taxonomy has no other names, pinned synonym fields are empty, and no own type-material, merged-ID or dropped-taxon row, or backbone child, was found. Species rank is an NCBI classification rather than proof of formal nomenclatural standing. The source label does not establish a taxonomic umbrella over all endosymbionts sampled from that host family.

Complete live EFetch and Datasets responses establish three separately classified sibling taxa, all species under 2640676: 1094267, Wolbachia endosymbiont of elachJanzen01 Janzen01; 1094268, Wolbachia endosymbiont of elachbiolep01 biolep588; and 1084948, Wolbachia endosymbiont of elachBioLep01 BioLep373. Only the last supplies a Wolbachia sp. synonym. No inspected authority declares these aliases or descendants of 1036668.

## Evidence

Complete own rows inspected: `data/raw/ncbitaxon_taxa.tsv:222571`, `data/catalog/ncbi_names-0005.jsonl.gz:32115`, `data/taxa/PATHS.tsv:15088` and `curation/seed_scope.tsv:322818`. Snapshot 2026-09-13, one-name unit and admission reason support the attestation and seed event. Exact target scans found no row in the BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits raw inventories. A name count is not a genome or experiment count.

The host-family Nuccore search returned three partial bacterial COI markers. Complete GenBank XML, including references, source qualifiers, gene/CDS features, translations and nucleotide sequences, was read for each:

| Accession | UID | Taxon | Bases | Specimen voucher suffix | BOLD process |
| --- | --- | --- | --- | --- | --- |
| [JF902196.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902196.1) | 334360749 | 1094268 | 657 | MHMYA588-09.w | ASLEP073-10 |
| [JF902197.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902197.1) | 334360751 | 1094268 | 657 | MHMYA594-09.w | ASLEP074-10 |
| [JF902198.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902198.1) | 334360753 | 1094267 | 595 | MHMXR158-08.w | ASLEP019-10 |

All three annotate host Elachistidae sp., Costa Rica, `BIOUG<CAN>` specimen vouchers, COI-5P BOLD identifiers, code 11, codon start 1 and both CDS ends partial. Creation/update dates are 30-APR-2012. They cite an unpublished Smith barcoding reference and direct submission dated 01-MAY-2011 from the University of Guelph. JF902196 gives Sendero Tucan, 12-Jul-2008 and collector Jose Perez; JF902197 gives Cano, 13-May-2008 and Leonel Siezar. JF902198 lacks that finer collection provenance and includes ambiguous sequence positions. These are specimen-associated gene records, not cultured deposits, assemblies or records assigned to the target ID.

The [primary Smith et al. 2012 paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0036514), DOI 10.1371/journal.pone.0036514, PMID 22567162 and PMCID PMC3342236, concerns Wolbachia detection during insect DNA barcoding. The complete PubMed abstract and bibliographic identifiers were read, together with selected primary HTML Discussion, Methods and supporting-information text. Methods explain the host-extract identifier plus .w convention and direct readers to specimen accessions in Table S2. Whole-paper or figure-image review is not claimed. The study does not establish that the present broad label and the sibling IDs denote the same taxon.

All cell values in the four sheets of [Table S2](https://journals.plos.org/plosone/article/file?id=10.1371%2Fjournal.pone.0036514.s003&type=supplementary) were searched using the target/context terms. Headers and eight matching rows were read completely, retaining duplicate header names. In Wolbachia CO1, rows 180, 232 and 233 map the three JF markers to their vouchers, lengths and Elachistidae host-family context. Row 482 adds BLPDT1066-10.w, BOLD ASWLP008-11, with accession pending at publication. Rows 67 and 143-145 instead name agathJanzen/ichJanzen-associated Wolbachia with Braconidae or Ichneumonidae in Extra Info, and Elachistidae in Notes. They are not evidence for transferring parasitoid-associated bacteria to this taxon. Those four accessions were not separately fetched from GenBank. Other nonmatching rows were not individually adjudicated; no matching rows occurred in the other three sheets.

The pending accession was resolved by voucher search. Complete [JN674118.1](https://www.ncbi.nlm.nih.gov/nuccore/JN674118.1) XML identifies UID 350996225, 658 bases, taxon 1084948, specimen BLPDT1066-10.w, BOLD ASWLP008-11.COI-5P and the named host specimen elachBioLep01 BioLep373 BLPDT1066-10. Collection is 13-May-2010, Derrumbe, Cacao, Costa Rica, by F.Quesada and R.Franco. Matching voucher, process and collection identifiers support the supplement-to-accession link. This code-11, codon-start-2 partial CDS was submitted 13-SEP-2011, created 12-SEP-2012 and updated 25-JUL-2016. It is a fourth contextual gene marker, not a target genome.

The four directly matching supplement specimens use Elachistidae in their host-family context, consistent with the three JF source records; the JN source uses the specimen name. Historical Rickettsiaceae in the workbook's bacterial Family column differs from current Anaplasmataceae, and the workbook's internal Table S1 label differs from the publisher's Table S2 label. Preserve these source-era/label discrepancies without replacing current carried taxonomy. No reproductive manipulation, supergroup, host specificity or other phenotype is inferred for 1036668.

## Completeness

Complete enough for supported taxonomy-seed claims. Zero represented BacDive strains does not assert biological absence. No inspected evidence establishes an explicit link from 1036668 to the four contextual accessions, a cultured deposit or an assembly. Optional slots should not be populated by borrowing sibling evidence.

Gitignore-independent `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Initial terms were word-bounded 1036668, exact slug and Elachistidae. Expansions added the four listed accessions with optional .1, their four UIDs, sibling IDs 1094267/1094268/1084948, elachJanzen01 and elachbiolep01, all four vouchers and BOLD process codes. Fourteen final matching rows were fully read in native form: eight TSV and six JSON rows, comprising three own rows, ten sibling taxonomy/name rows and one numerical collision. The last expansion added no rows.

Sibling addresses: `data/raw/ncbitaxon_taxa.tsv:233137`, `:235313` and `:235314`; `curation/seed_scope.tsv:331683`, `:333626` and `:333627`; and `data/catalog/ncbi_names-0005.jsonl.gz:44951`, `:44952`, `:47542` and `:47543`. The additional `data/catalog/ncbi_genbank-0066.jsonl.gz:41643` row is GCA_982961495.1, a Crocinitomicaceae bacterium assembly, taxon 2026728. It matched genome size 1094268, not a Wolbachia taxon field. Its full native row was read; it is not a target assembly link and was not independently revalidated remotely.

Five SOURCE.json files were separately parsed in full for the expanded terms, with no matching keys or values; history filenames were independently inventoried. These searches cover the stated local roots and terms, not every possible spelling or external database.

Exact Nuccore and Assembly queries `txid1036668[Organism:exp]` returned zero with missing-phrase/no-items diagnostics, not proof of global absence. `Wolbachia[Organism] AND Elachistidae[All Fields]` returned three, expanding the family term to Organism OR All Fields while retaining the Wolbachia intersection. The supplementary two-term query accepted BLPDT1066-10 but rejected ASWLP008-11 as a quoted phrase not found; its single voucher hit was read completely.

PubMed Wolbachia AND Elachistidae returned zero after genus MeSH/all-fields expansion, without rejecting the family term. Web queries for the exact ID/family, JF902198 and the submission title supplied bibliographic leads. Search snippets are not independent evidence, and these results are not an exhaustive literature census.

iModulonDB was not run: no gene, regulator or expression claim is asserted, and no applicable target strain/dataset was established. Empty optional fields are not automatic defects.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in stored claims. Identity, lineage, source attestation and admission agree with pinned and live authorities. Sibling markers, parasitoid-context table rows and an unrelated assembly's numerical collision do not establish required missing claims for this record.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Future taxonomy corrections belong first at NCBI, then pinned inputs governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection fixes belong in `src/taxonmech/seed.py` with tests; admission changes belong in `curation/seed_scope.tsv`. Do not merge the four taxonomic identities based on host-family wording or similar specimen codes.

## Follow-up Checks

Optional enrichment requires an explicit authority-backed link between 1036668 and a specimen/accession; culture and genome relationships need their own source chain. Preserve the distinction between a bacterium's annotated host and an associated parasitoid's host. No independent sequence alignment, CDS translation verification, genome comparison or experimental reanalysis was performed.

After an authorized maintained-input change, run focused tests, `just seed-canary NCBITaxon:1036668`, inspect output, rerun both individual validators and `just verify-corpus`, then full publication QC. No regeneration ran.

## Additional Notes

Independent review followed the local skill/checklist; no neighboring verdict was inherited. Entire YAML, all fourteen local candidate rows, own and three sibling live taxonomy responses, four complete marker XML records, the publication abstract and selected primary HTML were inspected. Supplement analysis reused the previously downloaded public XLS, rechecked its SHA-256 and ran a new target-specific scan using temporary xlrd, without workbook or repository dependency changes.

Workbook SHA-256: `8df12e221a835a4504e4ce0a30e5aed17a4e906c9bc2e1bffcd4113adf0f0a1e`. Before/after YAML SHA-256: `5eb9cdaf57ec680226d55a5f85abcaac7aadd1fdb028bd48a4854cb0384e10dc`. Only this new report was written in the repository for the target. This review did not change YAML, sources, status, history, pages, Eukaryota, GitHub objects or worktrees.
