# YAML Record Review: Wolbachia endosymbiont of Talides sinois

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_talides_sinois.yaml`
- Started UTC: 2026-10-07T15:55:16Z
- Finished UTC: 2026-10-07T15:56:59Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1035982`,
Wolbachia endosymbiont of Talides sinois. It asserts species rank,
bacterial domain, parent 2640676, code 11, 11 root-first ancestors,
`EXACT` grounding, `SEEDED` lifecycle, zero inventoried BacDive strains,
one NCBITAXON name attestation, and one inline seed event.
No synonyms, nomenclature, mappings, strain/genome objects, citations,
phenotypes, or causal graph are asserted. Seeded fields are read-only.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/wolbachia_endosymbiont_of_talides_sinois.yaml`: passed, no issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/wolbachia_endosymbiont_of_talides_sinois.yaml --out /private/tmp/wol-sinois-strict.tsv`: passed, one file and zero errors; complete header-only diagnostics read.
- Parsed comparisons passed for the full backbone row, every ancestor label/rank/parent link, empty synonym columns, unique scope/path rows, attestation, and seed wording. These bounded checks do not reproduce the corpus.
- Live NCBI EFetch XML and Datasets JSON and full GenBank metadata/features/references were retrieved and inspected earlier in this same turn during Talides disambiguation, then reread for this target. A fresh exact Assembly/Nuccore search confirms the sole matching nucleotide UID. Sequence/translation payloads were excluded from metadata reads.
- `just validate-products`: not applicable; no curator-added graph grounding/label pairs. Taxonomy IDs and labels were checked at NCBI.
- Standalone `just validate-history`: not applicable after ignored-independent content and filename searches found no target artifact. Inline history passed schema, strict, and source checks.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just validate-all`, `just provenance-check`, `just render-check`, `just docs-check`, `just vendored-check`, and the test suite.
- The NCBI taxonomy browser was unavailable through the web tool; authoritative EFetch and Datasets responses were available.
- Not checked: independent BOLD/protein objects, sequence alignment, or the related primary paper's Table S2.

## Identity and Grounding

[NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035982&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035982)
confirm the active exact taxid, label, species rank, bacterial lineage,
and parent `NCBITaxon:2640676`, unclassified Wolbachia. EFetch confirms
code 11. This denotes the bacterium, not the Talides sinois host;
NCBI species rank does not establish formal nomenclatural status.

Full pinned rows agree at `data/raw/ncbitaxon_taxa.tsv:222241`,
`data/catalog/ncbi_names-0005.jsonl.gz:31754`,
`data/taxa/PATHS.tsv:14739`, and `curation/seed_scope.tsv:322498`.
The native row is a scientific name with empty unique name. Backbone
synonym columns and live alternate-name fields are empty, consistent
with YAML omission. Snapshot date is 2026-09-13; `retired_into` is empty.

Every ancestor ID, label, rank, and parent link agrees with the pinned
root-first chain. Datasets includes root; EFetch supplies the remaining
labeled chain through Pseudomonadati, Pseudomonadota, Alphaproteobacteria,
Rickettsiales, Anaplasmataceae, Wolbachieae, Wolbachia, and unclassified
Wolbachia. Parsed inventories contain no target child, type-material,
merged-ID, or dropped row. `EXACT` grounding does not promote `SEEDED` lifecycle.

The separate bacterial taxids
[1035981, Talides sp.](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035981),
and [1094265, Talides Burns01](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1094265),
were also confirmed active at NCBI this turn. Their source rows and
shared parent do not establish synonyms or equivalence with this taxon.

## Evidence

The sole NCBITAXON attestation counts one `NAME`, not specimens,
infections, cultures, sequences, or genomes. Exact-target scans of
raw BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, and BactoTraits
inventories found no applicable rows. With no backbone descendants,
zero inventoried BacDive strains agrees with the inputs without
implying biological absence of strains or infections.

Inline seed wording matches the scope row and attestation.
The `2026-09-13T17:54:04Z` timestamp equals the latest inspected raw,
ATB, and StrainInfo extraction timestamp, following
`src/taxonmech/seed.py::_seed_timestamp`.

Exact Nuccore query `txid1035982[Organism:noexp]` returned UID 334360855,
[JF902249.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902249.1).
This 646-nt partial COI object explicitly identifies the target
bacterial organism and `taxon:1035982`, with host Talides sinois.
It supplies specimen voucher `BIOUG<CAN>:MHAHL310-07.w`, GenBank-reported
BOLD cross-reference `ASLEP064-10.COI-5P`, codon start 1, translation
table 11, and protein cross-reference `AEG78070.1`. Its locality is
only Costa Rica; no collection date, collector, coordinates, or finer
locality are supplied. Identification and primer qualifiers were read.
Independent BOLD/protein objects were not retrieved.

The broader Wolbachia/Talides query inspected earlier this turn returned
this object and
[JF902248.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902248.1),
which explicitly identifies taxid 1094265, Talides Burns01, despite a
Talides sp. host qualifier. That neighbor's voucher, 2002 collection
date, and finer Costa Rican locality are not imported into JF902249.1
or this record. Neither marker is a genome assembly; specimen vouchers
are not culture deposits or evidence of equivalent strains.

JF902249.1 retains a Smith unpublished manuscript reference and a
direct submission dated 1 May 2011 at the University of Guelph.
The related
[Smith et al. primary PLOS ONE paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0036514),
DOI `10.1371/journal.pone.0036514`, describes bacterial COI recovered
during insect barcoding, `.w` sample IDs, and accession details in
Table S2. Main-text search did not match Talides; Table S2 was not
inspected. This supplies methodological context, not an inspected
exact-target allele, prevalence, or reproductive-phenotype assignment.
GenBank's unpublished label is not evidence that no related publication exists.

Exact Assembly query `txid1035982[Organism:noexp]` returned zero with
phrase-not-found/no-items diagnostics. This bounded index result does
not prove global or historical genome absence. The marker establishes
neither a missing strain-genome link nor a contradictory BacDive count.

## Completeness

Complete enough for its generated NCBI-only identity purpose.
Optional nomenclature, mappings, strain/genome objects, and causal
claims are appropriately unasserted on the inspected evidence.

Ignored-independent search used `rg --no-ignore --hidden -n -z -i`
across `data/raw/`, `data/catalog/`, `data/bacdive/`, `data/bvbrc/`,
`data/gold/`, `data/seqcode/`, `data/straininfo/`, `data/atb/`,
`curation/`, and `history/`, including ignored, hidden, and compressed
content. Patterns covered taxid, label, slug, JF902249, MHAHL310-07,
and ASLEP064-10.

All 22 target-search candidate rows were fully read:

- Three describe the target backbone, scope, and native scientific name.
- One GTDB row at `data/catalog/gtdb_genomes-0016.jsonl.gz:386` describes Clostridioides difficile 17cd, taxid 1496, RS_GCF_041537845.1, BioSample SAMN43297758. Its contig N50 value 1035982 is a numeric collision.
- One GenBank row at `data/catalog/ncbi_genbank-0009.jsonl.gz:6817` describes Campylobacter jejuni PNUSAC014937, taxid 197, GCA_010359825.1, BioSample SAMN13825583. Its accession digits cause the match.
- Ten ATB rows at lines 143639-143648 describe Escherichia coli samples SAMEA110359820 through SAMEA110359829. Sample digits cause the matches.
- One ATB row at line 549321 describes sample SAMEA3357200, ERZ3256714, and run ERR1035982. The scientific name is mixed culture bacterium while Sylph assigns Klebsiella pneumoniae; both source classifications were retained as inspected, not reconciled. The run ID causes the match, not target identity.
- Six ATB rows at lines 1716050, 1716051, and 1716053-1716056 have Salmonella enterica scientific names and samples SAMN13152866, SAMN13152867, and SAMN13152869 through SAMN13152872. Run accessions SRR10359824 through SRR10359829 cause the matches. Sylph labels samples SAMN13152870 and SAMN13152872 Salmonella houtenae; these foreign-source differences are not target conflicts.

Expanded marker/voucher/BOLD search added no rows. Five native
`SOURCE.json` files were parsed completely and history filenames
searched independently. The additional six raw backbone/scope/native-name
rows for Talides sp. and Talides Burns01 had also been fully read during
the immediately preceding disambiguation; neither is a target synonym.
No additional applicable local assertion, culture deposit, strain-genome
link, or standalone target history artifact was found within these
bounded roots. No global absence is claimed.

iModulonDB is not applicable: no regulator, expression module, or
transcriptomic dataset is asserted. Optional COI barcoding evidence
does not establish an expression-module claim.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, empty synonym fields, one-name attestation,
inventoried strain count, optional omissions, and seed provenance are
supported. Exact-taxid marker evidence does not establish a missing
genome link or justify importing neighboring specimen metadata.

## Recommended Edits

None required. Preserve generated YAML and `mapping_status: SEEDED`.
No status promotion or curation-history event is authorized by this review.
Future source corrections belong to maintained upstream inputs and
`src/taxonmech/extract.py`/`src/taxonmech/seed.py`; scope changes belong
to `curation/seed_scope.tsv`. Do not patch generated YAML/pages.

## Follow-up Checks

No corrective follow-up is required. Before optional marker enrichment,
inspect Table S2 and accession-specific primary evidence without filling
missing collection fields from neighboring specimens or taxa.
After separately authorized maintained-input changes, rerun the owning
generator, per-file schema/strict validation, and applicable full-corpus
acceptance gates. New curated history requires `just validate-history`;
new graph terms/evidence require `just validate-products`.

## Additional Notes

The entire YAML was reread and remained byte-identical before report
creation. All bounded local reads and public retrievals reached terminal
results. No YAML, source inventory, lifecycle, standalone history,
generated page, GitHub state, branch, or worktree was changed.
Eukaryota records were not re-reviewed. Only this new timestamped
report was written for this target.
