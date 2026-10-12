# YAML Record Review: Wolbachia endosymbiont of Polyctor polyctor

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_polyctor_polyctor.yaml`
- Started UTC: 2026-10-07T15:32:26Z
- Finished UTC: 2026-10-07T15:34:47Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1035977`,
Wolbachia endosymbiont of Polyctor polyctor. It asserts species rank,
bacterial domain, code 11, 11 root-first ancestors, `EXACT` grounding,
`SEEDED` lifecycle, one NCBI exact synonym, zero inventoried BacDive
strains, one NCBITAXON name attestation, and one inline seed event.
No nomenclature, mappings, strain/genome objects, citations, phenotypes,
or causal graph are asserted. Seeded fields are generated and read-only.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/wolbachia_endosymbiont_of_polyctor_polyctor.yaml`: passed, no issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/wolbachia_endosymbiont_of_polyctor_polyctor.yaml --out /private/tmp/wol-ppolyctor-strict.tsv`: passed, one file and zero errors; complete header-only diagnostics read.
- Parsed source checks passed for the complete backbone row, every ancestor label/rank/parent link, synonym, unique scope/path rows, attestation, and seed wording. These bounded checks are not corpus reproduction.
- Live NCBI EFetch XML and Datasets JSON and exact Assembly/Nuccore queries were inspected. All seven nucleotide objects' metadata/features/references were read completely, excluding sequence/translation payloads.
- `just validate-products`: not applicable; no curator-added graph grounding/label pairs. Taxonomy identifiers and labels were checked at NCBI.
- Standalone `just validate-history`: not applicable after ignored-independent content and filename searches found no target artifact. Inline history passed schema, strict, and source checks.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just validate-all`, `just provenance-check`, `just render-check`, `just docs-check`, `just vendored-check`, and the test suite.
- The NCBI taxonomy browser was unavailable through the web tool; authoritative EFetch and Datasets responses were available.
- Not checked: independent BOLD/protein objects, sequence alignment, or the related primary paper's Table S2.

## Identity and Grounding

[NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035977&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035977)
confirm the active exact taxid, label, species rank, bacterial lineage,
and parent `NCBITaxon:2640676` (unclassified Wolbachia).
EFetch confirms code 11 and synonym Wolbachia sp. Polyctor polyctor.
This is the bacterial node, not its host or a similarly named
Polyctor-associated bacterium. Species rank does not establish formal
nomenclatural status for the host-qualified bacterial name.

Complete pinned rows agree at `data/raw/ncbitaxon_taxa.tsv:222236`,
`data/catalog/ncbi_names-0005.jsonl.gz:31748` and line 31749,
`data/taxa/PATHS.tsv:14734`, and `curation/seed_scope.tsv:322493`.
The two native rows classify the current name as scientific name and
Wolbachia sp. Polyctor polyctor as synonym. The latter maps to
`EXACT_SYNONYM` under `src/taxonmech/ncbi_taxdump.py`'s name-class rule;
the raw exact-synonym column and YAML agree. Related/broad synonym
columns are empty. Snapshot date is 2026-09-13 and `retired_into` is empty.

Every ancestor ID, label, rank, and parent link agrees with the pinned
root-first chain. Datasets includes root; EFetch supplies the remaining
labeled chain through Pseudomonadati, Pseudomonadota, Alphaproteobacteria,
Rickettsiales, Anaplasmataceae, Wolbachieae, and Wolbachia.
Parsed inventories contain no target child, type-material, merged-ID,
or dropped row. `EXACT` grounding and `SEEDED` lifecycle remain distinct.

## Evidence

The attestation counts one NCBITAXON `NAME` concept, not the number of
alternate strings, specimens, sequences, cultures, or genomes.
Exact-target scans of raw BacDive, LPSN, GTDB, GOLD, MediaDive, Madin,
and BactoTraits inventories found no applicable rows. With no backbone
descendants, zero inventoried BacDive strains agrees with the source
inputs without implying absence of biological strains or infections.

Inline seed wording matches the scope row and attestation.
The `2026-09-13T17:54:04Z` timestamp equals the latest inspected raw,
ATB, and StrainInfo extraction timestamp, following
`src/taxonmech/seed.py::_seed_timestamp`.

Exact Nuccore query `txid1035977[Organism:noexp]` returned seven
partial COI records. Each explicitly identifies `taxon:1035977`
and the target bacterial organism. Host qualifiers say Polyctor
polyctor, with specimen codes appended in the four JN records.
All use translation table 11 and report Costa Rican specimens:

| Accession | Length (nt) | Codon start | Specimen voucher | GenBank-reported BOLD cross-reference |
| --- | --- | --- | --- | --- |
| [JF902225.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902225.1) | 610 | 1 | `BIOUG<CAN>:MHAHE055-05.w` | `ASLEP033-10.COI-5P` |
| [JF902226.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902226.1) | 614 | 1 | `BIOUG<CAN>:MHMYB144-09.w` | `ASLEP087-10.COI-5P` |
| [JF902227.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902227.1) | 597 | 1 | `BIOUG<CAN>:MHMYB145-09.w` | `ASLEP088-10.COI-5P` |
| [JN674129.1](https://www.ncbi.nlm.nih.gov/nuccore/JN674129.1) | 658 | 2 | `MHMYB140-09.w` | `ASWLP027-11.COI-5P` |
| [JN674130.1](https://www.ncbi.nlm.nih.gov/nuccore/JN674130.1) | 423 | 2 | `MHAHF703-06.w` | `ASWLP015-11.COI-5P` |
| [JN674131.1](https://www.ncbi.nlm.nih.gov/nuccore/JN674131.1) | 424 | 2 | `MHAHF702-06.w` | `ASWLP014-11.COI-5P` |
| [JN674132.1](https://www.ncbi.nlm.nih.gov/nuccore/JN674132.1) | 445 | 2 | `MHAHF700-06.w` | `ASWLP013-11.COI-5P` |

JF902225.1 reports Pasmompa, Sector Pitilla, Guanacaste, collected
7 December 2004. JF902226.1 and JF902227.1 provide only Costa Rica
and no collection-date qualifier; dates and precise sites are not
inferred from their voucher codes or neighboring specimens.
JN674129.1 reports Meteorologico, Sector Del Oro, Guanacaste,
14 February 2009. JN674130.1 and JN674131.1 report Puente Palma,
Sector San Cristobal, Alajuela, on 13 and 7 November 2005 respectively.
JN674132.1 reports Pasmompa on 10 September 2005.

Primer, collector, identifier, coordinate, and protein qualifiers
were inspected where supplied. The three JF protein cross-references
are `AEG78046.1` through `AEG78048.1`; the four JN cross-references
are `AEQ36793.1` through `AEQ36796.1`, in accession order.
Independent BOLD/protein objects were not retrieved. Shared host or
taxid does not prove sequence, strain, or genome equivalence.

The JF records retain direct submissions dated 1 May 2011 and the
JN records 13 September 2011 at the University of Guelph, alongside
unpublished Smith manuscript references. The related
[Smith et al. primary PLOS ONE paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0036514),
DOI `10.1371/journal.pone.0036514`, supplies insect-barcoding methods,
including bacterial `.w` sample IDs and accession details in Table S2.
Main-text search did not match Polyctor; the supplement was not
inspected. No exact-target allele, prevalence, or reproductive
phenotype is inferred from the cohort-level paper. GenBank's
unpublished labels are retained as stored, not interpreted as
absence of a relevant publication.

Exact Assembly query `txid1035977[Organism:noexp]` returned zero
with phrase-not-found/no-items diagnostics. This bounded index result
does not prove global or historical genome absence.
The seven COI markers are not seven cultured strains or assemblies;
specimen vouchers are not culture deposits. They establish neither
a missing strain-genome link nor a contradictory inventoried strain count.

## Completeness

Complete enough for its generated NCBI-only identity purpose.
Optional nomenclature, mappings, strain/genome objects, and causal
claims are appropriately unasserted on the inspected evidence.

Ignored-independent search used `rg --no-ignore --hidden -n -z -i`
across `data/raw/`, `data/catalog/`, `data/bacdive/`, `data/bvbrc/`,
`data/gold/`, `data/seqcode/`, `data/straininfo/`, `data/atb/`,
`curation/`, and `history/`, including ignored, hidden, and compressed
content. Patterns covered taxid, label, synonym's host-qualified text,
slug, and all seven marker, specimen-voucher, and BOLD stems above.

All 17 candidate rows were fully read:

- Four describe the target backbone, scope, native scientific name, and native synonym.
- Ten ATB rows at lines 143589-143598 describe Escherichia coli samples SAMEA110359770 through SAMEA110359779. Their sample digits cause false matches.
- Two ATB rows at lines 401102-401103 describe Enterococcus cecorum samples SAMEA12751081 and SAMEA12751082, assemblies ERZ25181910 and ERZ25181922. Their runs ERR10359773 and ERR10359774 contain the matching digits.
- One ATB row at line 3073981 describes Salmonella enterica subsp. enterica serovar Typhi sample SAMN43931658, assembly ERZ27097411; its SeqKit sum contains the digits. None of these foreign objects supplies target taxonomic or strain-link evidence.

Expanded marker/voucher/BOLD search added no rows. Five native
`SOURCE.json` files were parsed completely and history filenames
searched independently. No additional applicable local assertion,
culture deposit, strain-genome link, or standalone history artifact
was found within these bounded roots. No global absence is claimed.

iModulonDB is not applicable: no regulator, expression module, or
transcriptomic dataset is asserted. Optional COI barcoding evidence
does not establish an expression-module claim.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, exact synonym, one-name attestation,
inventoried strain count, optional omissions, and seed provenance
are supported. The additional markers are compatible with the
generated record without establishing missing genome links.

## Recommended Edits

None required. Preserve generated YAML and `mapping_status: SEEDED`.
No status promotion or curation-history event is authorized by this review.
Future source corrections belong to maintained upstream inputs and
`src/taxonmech/extract.py`/`src/taxonmech/seed.py`; scope changes belong
to `curation/seed_scope.tsv`. Do not patch generated YAML/pages.

## Follow-up Checks

No corrective follow-up is required. Before optional marker enrichment,
inspect Table S2 and exact accession-level primary evidence, keeping
specimen, marker, strain, and assembly identities separate and retaining
missing collection qualifiers rather than filling them by inference.
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
