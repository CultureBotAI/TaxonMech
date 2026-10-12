# YAML Record Review: Wolbachia endosymbiont of Urbanus albimargo

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_urbanus_albimargo.yaml`
- Started UTC: 2026-10-07T16:02:40Z
- Finished UTC: 2026-10-07T16:04:52Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1035984`,
Wolbachia endosymbiont of Urbanus albimargo. It asserts species rank,
bacterial domain, parent 2640676, code 11, 11 root-first ancestors,
`EXACT` grounding, `SEEDED` lifecycle, zero inventoried BacDive strains,
one NCBITAXON name attestation, and one inline seed event.
No synonyms, nomenclature, mappings, strain/genome objects, citations,
phenotypes, supergroup, or causal graph are asserted. Seeded fields are read-only.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/wolbachia_endosymbiont_of_urbanus_albimargo.yaml`: passed, no issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/wolbachia_endosymbiont_of_urbanus_albimargo.yaml --out /private/tmp/wol-urbanus-strict.tsv`: passed, one file and zero errors; complete header-only diagnostics read.
- Parsed comparisons passed for the complete backbone row, every ancestor label/rank/parent link, empty synonym columns, unique scope/path rows, attestation, and seed wording. These bounded checks do not reproduce the corpus.
- Live NCBI EFetch XML and Datasets JSON, exact Assembly/Nuccore queries, and the sole nucleotide object's complete metadata/features/references were inspected. Sequence/translation payloads were excluded.
- `just validate-products`: not applicable; no curator-added graph grounding/label pairs. Taxonomy IDs and labels were checked at NCBI.
- Standalone `just validate-history`: not applicable after ignored-independent content and filename searches found no target artifact. Inline history passed schema, strict, and source checks.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just validate-all`, `just provenance-check`, `just render-check`, `just docs-check`, `just vendored-check`, and the test suite.
- The NCBI taxonomy browser was unavailable through the web tool; authoritative EFetch and Datasets responses were available.
- Not checked: independent BOLD/protein objects, sequence alignment, or the related primary paper's Table S2. The paper/GenBank marker-context discrepancy described below remains unresolved; no such claim is present in the YAML.

## Identity and Grounding

[NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035984&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035984)
confirm the active exact taxid, label, species rank, bacterial lineage,
and parent `NCBITaxon:2640676`, unclassified Wolbachia. EFetch confirms
code 11. This denotes the bacterium, not the Urbanus host; NCBI species
rank does not establish formal nomenclatural status for the name.

Full pinned rows agree at `data/raw/ncbitaxon_taxa.tsv:222243`,
`data/catalog/ncbi_names-0005.jsonl.gz:31756`,
`data/taxa/PATHS.tsv:14741`, and `curation/seed_scope.tsv:322500`.
The native row is a scientific name with empty unique name. Backbone
synonym columns and live alternate-name fields are empty, consistent
with YAML omission. Snapshot date is 2026-09-13; `retired_into` is empty.

Every ancestor ID, label, rank, and parent link agrees with the pinned
root-first chain. Datasets includes root; EFetch supplies the remaining
labeled chain through Pseudomonadati, Pseudomonadota, Alphaproteobacteria,
Rickettsiales, Anaplasmataceae, Wolbachieae, Wolbachia, and unclassified
Wolbachia. Parsed inventories contain no target child, type-material,
merged-ID, or dropped row. `EXACT` grounding does not promote `SEEDED` lifecycle.

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

Exact Nuccore query `txid1035984[Organism:noexp]` returned
[JF902251.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902251.1), a 657-nt
partial COI object explicitly identifying the target organism and
`taxon:1035984`, with host Urbanus albimargo. Its specimen voucher is
`BIOUG<CAN>:MHAHG182-06.w`, with GenBank-reported BOLD cross-reference
`ASLEP050-10.COI-5P`. It reports collection on 18 February 2006 by
Jose Cortez at Vado Andira, Sector Mundo Nuevo, Area de Conservacion
Guanacaste, Guanacaste, Costa Rica, coordinates 10.728 N, 85.412 W.
The CDS uses codon start 1 and translation table 11, with protein
cross-reference `AEG78072.1`. Identification and primer qualifiers
were read. Independent BOLD/protein objects were not retrieved.

GenBank retains a Smith unpublished manuscript reference and a direct
submission dated 1 May 2011 at the University of Guelph. The related
[Smith et al. primary PLOS ONE paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0036514),
DOI `10.1371/journal.pone.0036514`, provides barcoding methods and
accession details in Table S2. Its main text does not match albimargo.
It discusses wsp fragments in Urbanus belliDHJ01 and belliDHJ03 as
consistent with Supergroup B, not an albimargo COI assignment. In its
Urbanus discussion it also states that bacterial COI was not
inadvertently amplified from that genus. This is an unresolved
marker-context tension with JF902251.1, not permission to silently
prefer either source or transfer the belli-host result to albimargo.
Table S2 and accession-specific primary context were not inspected
to resolve it. No supergroup, allele, prevalence, amplification-method,
or reproductive-phenotype claim is inferred for this record.

The discrepancy is retained for future enrichment, not classified as a
YAML defect: the YAML asserts NCBI identity and source provenance,
not the paper's experimental interpretation or a COI annotation.
GenBank's unpublished reference label does not establish that no
related publication exists.

Exact Assembly query `txid1035984[Organism:noexp]` returned zero with
phrase-not-found/no-items diagnostics. This bounded index result does
not prove global or historical genome absence. A marker is not an
assembly or cultured strain; its voucher is not a culture deposit.
The inspected object establishes neither a missing strain-genome link
nor a contradictory inventoried BacDive count.

## Completeness

Complete enough for its generated NCBI-only identity purpose.
Optional nomenclature, mappings, strain/genome objects, and causal
claims are appropriately unasserted. The unresolved external marker
context should remain unresolved until accession-level evidence is inspected.

Ignored-independent search used `rg --no-ignore --hidden -n -z -i`
across `data/raw/`, `data/catalog/`, `data/bacdive/`, `data/bvbrc/`,
`data/gold/`, `data/seqcode/`, `data/straininfo/`, `data/atb/`,
`curation/`, and `history/`, including ignored, hidden, and compressed
content. Patterns covered taxid, label, slug, JF902251, MHAHG182-06,
and ASLEP050-10.

All 31 candidate rows were fully read:

- Three describe the target backbone, scope, and native scientific name.
- One GenBank row at `data/catalog/ncbi_genbank-0009.jsonl.gz:6818` describes Campylobacter jejuni PNUSAC014838, taxid 197, GCA_010359845.1, and BioSample SAMN13750326. The accession digits cause the match.
- Ten ATB rows at lines 143659-143668 describe Escherichia coli samples SAMEA110359840 through SAMEA110359849. Sample digits cause the matches.
- Six ATB rows at lines 401107-401112 describe Enterococcus cecorum samples SAMEA12751086 through SAMEA12751091. Runs ERR10359842, ERR10359843, ERR10359845, ERR10359846, ERR10359847, and ERR10359848 cause the matches. Sylph's Enterococcus_E cecorum names were preserved as source classifications.
- One ATB row at line 549325 describes Klebsiella variicola sample SAMEA3357204, assembly ERZ3256726, and run ERR1035984. The run ID is a numeric collision.
- Ten ATB rows at lines 1716057-1716058, 1716062, 1716065-1716069, 1716073, and 1716082 have Salmonella enterica scientific names and runs SRR10359840 through SRR10359849. Samples are SAMN13152873, SAMN13152874, SAMN13152878, SAMN13152881 through SAMN13152885, SAMN13152889, and SAMN13152899. SAMN13152878 has SYLPH_RESULTS_FAIL, current Sylph species unknown, and earlier Salmonella houtenae. This foreign-source uncertainty is retained, not a target conflict; run digits cause these matches.

Expanded marker/voucher/BOLD search added no rows. Five native
`SOURCE.json` files were parsed completely and history filenames
searched independently. No additional applicable local assertion,
culture deposit, strain-genome link, or standalone target history
artifact was found within these bounded roots. No global absence is claimed.

iModulonDB is not applicable: no regulator, expression module, or
transcriptomic dataset is asserted. COI/wsp context does not establish
an expression-module claim or matching expression dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the generated identity record. Identity, lineage, empty
synonym fields, one-name attestation, inventoried strain count, and seed
provenance are supported. The external paper/marker discrepancy remains
an explicitly bounded enrichment uncertainty, not an asserted YAML claim.

## Recommended Edits

None required. Preserve generated YAML and `mapping_status: SEEDED`.
Do not add supergroup or experimental marker claims while the source
discrepancy remains unresolved. No status promotion or curation-history
event is authorized by this review.
Future source corrections belong to maintained upstream inputs and
`src/taxonmech/extract.py`/`src/taxonmech/seed.py`; scope changes belong
to `curation/seed_scope.tsv`. Do not patch generated YAML/pages.

## Follow-up Checks

No corrective YAML follow-up is required. Before optional marker
enrichment, inspect Table S2 for JF902251/ASLEP050-10/MHAHG182-06 and
the accession-specific BOLD/GenBank evidence; reconcile experimental
scope with the paper's Urbanus statements before assigning a supergroup
or method. Sequence analysis would require the actual sequence and
appropriate reference evidence, not only a database feature label.
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
