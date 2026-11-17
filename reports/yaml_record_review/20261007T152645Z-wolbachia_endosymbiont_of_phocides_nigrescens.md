# YAML Record Review: Wolbachia endosymbiont of Phocides nigrescens

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_phocides_nigrescens.yaml`
- Started UTC: 2026-10-07T15:24:36Z
- Finished UTC: 2026-10-07T15:26:45Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1035975`,
Wolbachia endosymbiont of Phocides nigrescens. It asserts species rank,
bacterial domain, code 11, 11 root-first ancestors, `EXACT` grounding,
`SEEDED` lifecycle, zero inventoried BacDive strains, one NCBITAXON
name attestation, and one inline seed event. No synonyms, nomenclature,
mappings, strain/genome objects, citations, phenotypes, or causal
graph are asserted. Seeded fields are generated and read-only.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/wolbachia_endosymbiont_of_phocides_nigrescens.yaml`: passed, no issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/wolbachia_endosymbiont_of_phocides_nigrescens.yaml --out /private/tmp/wol-phocides-strict.tsv`: passed, one file and zero errors; complete header-only diagnostics read.
- Parsed source checks passed for the complete backbone row, every ancestor label/rank/parent link, empty synonym columns, unique scope/path rows, attestation, and seed wording. These bounded checks are not corpus reproduction.
- Live NCBI EFetch XML and Datasets JSON, exact Assembly/Nuccore queries, and complete candidate nucleotide metadata/features/references were read. Sequence and translation payloads were excluded from metadata inspection.
- `just validate-products`: not applicable; no curator-added graph grounding/label pairs. Taxonomy identifiers and labels were checked at NCBI.
- Standalone `just validate-history`: not applicable after ignored-independent content and filename searches found no target artifact. Inline history passed schema, strict, and source checks.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just validate-all`, `just provenance-check`, `just render-check`, `just docs-check`, `just vendored-check`, and the test suite.
- The NCBI taxonomy browser was unavailable through the web tool; authoritative EFetch and Datasets responses were available.
- Not checked: independent BOLD/protein objects, sequence alignment, or the related primary paper's Table S2.

## Identity and Grounding

[NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035975&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035975)
confirm the active exact taxid, label, species rank, bacterial lineage,
and parent `NCBITaxon:2640676` (unclassified Wolbachia).
EFetch confirms code 11. The record denotes the bacterium, not
its Phocides host. NCBI species rank does not establish formal
nomenclatural status for this host-qualified bacterial name.

Complete pinned rows agree at `data/raw/ncbitaxon_taxa.tsv:222234`,
`data/catalog/ncbi_names-0005.jsonl.gz:31746`,
`data/taxa/PATHS.tsv:14732`, and `curation/seed_scope.tsv:322491`.
The native row is a scientific name. All pinned synonym columns
are empty, consistent with live alternate-name fields and YAML omission.
Snapshot date is 2026-09-13 and `retired_into` is empty.

Every ancestor ID, label, rank, and parent link agrees with the pinned
root-first chain. Datasets includes root; EFetch supplies the remaining
labeled chain through Pseudomonadati, Pseudomonadota, Alphaproteobacteria,
Rickettsiales, Anaplasmataceae, Wolbachieae, and Wolbachia.
Parsed inventories contain no target child, type-material, merged-ID,
or dropped row. `EXACT` grounding does not promote `SEEDED` lifecycle.

## Evidence

The NCBITAXON attestation counts one `NAME`, not a specimen, sequence,
infection, culture, or genome. Exact-target scans of raw BacDive,
LPSN, GTDB, GOLD, MediaDive, Madin, and BactoTraits inventories found
no applicable rows. With no backbone descendants, zero inventoried
BacDive strains agrees with the source inputs, without implying
absence of biological strains or infections.

Inline seed wording matches the scope row and attestation.
Its `2026-09-13T17:54:04Z` timestamp equals the latest inspected
raw, ATB, and StrainInfo extraction timestamp, as specified by
`src/taxonmech/seed.py::_seed_timestamp`.

Exact Nuccore query `txid1035975[Organism:noexp]` returned one record:
[JF902217.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902217.1), a 657-nt
partial COI sequence explicitly assigned to `taxon:1035975`.
Its source organism agrees with the target and its host qualifier
is Phocides nigrescens. The specimen voucher is
`BIOUG<CAN>:MHAHG336-06.w`; the GenBank-reported BOLD cross-reference
is `ASLEP059-10.COI-5P`. Collection was 15 March 2006 at Quebrada
Trigal, Sector Del Oro, Guanacaste, Costa Rica.
The CDS uses codon start 1 and translation table 11, with protein
cross-reference `AEG78038.1`. Primer and other source qualifiers
were inspected; BOLD/protein objects were not independently fetched.

GenBank retains an unpublished Smith manuscript reference and a
direct submission dated 1 May 2011 at the University of Guelph.
The related
[Smith et al. primary PLOS ONE paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0036514),
DOI `10.1371/journal.pone.0036514`, supplies insect-barcoding
methodological context, including bacterial `.w` sample IDs and
accession details in Table S2. Main-text search did not match
Phocides, and the supplement was not inspected. No exact-target
allele, prevalence, or reproductive phenotype is inferred from
the cohort-level paper. GenBank's unpublished label is retained
as stored, not interpreted as absence of a relevant publication.

Exact Assembly query `txid1035975[Organism:noexp]` returned zero
with phrase-not-found/no-items diagnostics. This bounded index
result does not prove global or historical genome absence.
The partial COI marker is not an assembly and its specimen voucher
is not a culture deposit; neither establishes a missing strain-genome
link or contradicts the inventoried strain count.

## Completeness

Complete enough for its generated NCBI-only identity purpose.
Optional nomenclature, mappings, strain/genome objects, citations,
and causal assertions are appropriately unpopulated on this evidence.

Ignored-independent search used `rg --no-ignore --hidden -n -z -i`
across `data/raw/`, `data/catalog/`, `data/bacdive/`, `data/bvbrc/`,
`data/gold/`, `data/seqcode/`, `data/straininfo/`, `data/atb/`,
`curation/`, and `history/`, including ignored, hidden, and compressed
content. Patterns covered taxid, label, slug, and marker/voucher/BOLD
stems `JF902217`, `MHAHG336-06`, and `ASLEP059-10`.

All 23 candidate rows were fully read:

- Three describe the target backbone, scope, and native scientific name.
- Five describe Pseudomonas aeruginosa Pae_CF67.10p, taxid 287: GenBank GCA_001035975.1, RefSeq GCF_001035975.1, GTDB RS_GCF_001035975.1, BV-BRC 287.1650, and GOLD analysis Ga0158579 linked to Gp0189810. GOLD's analysis has no organism ID and is not itself a genome identifier; none of these foreign rows supports a target strain link.
- Three describe Klebsiella aerogenes isolate 1900124, taxid 548, current GCA_031035975.3 and replaced versions .1/.2.
- One describes Enterocloster sp. isolate 1937_1937B_C_4, taxid 2719315, GCA_061035975.1.
- One GTDB row describes Sphingobacterium anhuiense NPDC090200, taxid 493780, RS_GCF_049546425.1; its scaffold N50 is 1035975, a numeric collision.
- Ten ATB rows at lines 143569-143578 describe Escherichia coli samples SAMEA110359750 through SAMEA110359759.

The non-target genome accessions, N50, and sample digits explain the
false matches. Expanded marker/voucher/BOLD search added no rows.
Five native `SOURCE.json` files were parsed completely and history
filenames searched independently. No additional applicable local
assertion, culture deposit, strain-genome link, or standalone history
artifact was found within the bounded roots. No global absence is claimed.

iModulonDB is not applicable: no regulator, expression module, or
transcriptomic dataset is asserted. Optional COI barcoding evidence
does not establish an expression-module claim.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, empty synonym fields, one-name
attestation, inventoried strain count, optional omissions, and seed
provenance are supported. The exact-taxid marker is compatible
with this generated record and does not require a genome link.

## Recommended Edits

None required. Preserve generated YAML and `mapping_status: SEEDED`.
No status promotion or curation-history event is authorized by this review.
Future source corrections belong to maintained upstream inputs and
`src/taxonmech/extract.py`/`src/taxonmech/seed.py`; scope changes belong
to `curation/seed_scope.tsv`. Do not patch generated YAML/pages.

## Follow-up Checks

No corrective follow-up is required. Before optional marker enrichment,
inspect Table S2 and exact accession-level primary evidence, keeping
specimen, marker, strain, and assembly identities separate.
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
