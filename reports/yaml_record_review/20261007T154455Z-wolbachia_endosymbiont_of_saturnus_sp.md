# YAML Record Review: Wolbachia endosymbiont of Saturnus sp.

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_saturnus_sp.yaml`
- Started UTC: 2026-10-07T15:39:17Z
- Finished UTC: 2026-10-07T15:44:55Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1035979`,
Wolbachia endosymbiont of Saturnus sp. It asserts species rank,
bacterial domain, parent 2640676, code 11, 11 root-first ancestors,
`EXACT` grounding, `SEEDED` lifecycle, zero inventoried BacDive
strains, one NCBITAXON name attestation, and one inline seed event.
No synonyms, nomenclature, mappings, strain/genome objects, citations,
phenotypes, or causal graph are asserted. Seeded fields are read-only.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/wolbachia_endosymbiont_of_saturnus_sp.yaml`: passed, no issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/wolbachia_endosymbiont_of_saturnus_sp.yaml --out /private/tmp/wol-saturnus-strict.tsv`: passed, one file and zero errors; complete header-only diagnostics read.
- Parsed checks passed for the full backbone row, every ancestor label/rank/parent link, empty synonym columns, unique scope/path rows, attestation, and seed wording. These bounded checks do not reproduce the corpus.
- Live NCBI EFetch XML and Datasets JSON were inspected for the target and the separate Saturnus Janzen01 taxon. Exact Assembly/Nuccore and broader Saturnus Nuccore searches were inspected. Complete metadata, features, and references for all ten broader-search nucleotide objects were read, excluding sequence/translation payloads.
- `just validate-products`: not applicable; no curator-added graph grounding/label pairs. Taxonomy IDs and labels were checked at NCBI.
- Standalone `just validate-history`: not applicable after ignored-independent content and filename searches found no target artifact. Inline history passed schema, strict, and source checks.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just validate-all`, `just provenance-check`, `just render-check`, `just docs-check`, `just vendored-check`, and the test suite.
- The NCBI taxonomy browser was unavailable through the web tool; authoritative EFetch and Datasets responses were available.
- Not checked: independent BOLD/protein objects, sequence alignment, historical accession reassignment, or the related primary paper's Table S2.

## Identity and Grounding

[NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035979&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035979)
confirm the active exact taxid, label, species rank, bacterial lineage,
and parent `NCBITaxon:2640676`, unclassified Wolbachia.
EFetch confirms code 11. This is the bacterial taxon, not its host.
NCBI species rank does not establish formal nomenclatural status
for the host-qualified name.

Full pinned rows agree at `data/raw/ncbitaxon_taxa.tsv:222238`,
`data/catalog/ncbi_names-0005.jsonl.gz:31751`,
`data/taxa/PATHS.tsv:14736`, and `curation/seed_scope.tsv:322495`.
The native row is a scientific name; its unique-name field is empty.
All backbone synonym columns are empty, consistent with live alternate
name fields and YAML omission. Snapshot date is 2026-09-13;
`retired_into` is empty.

Every ancestor ID, label, rank, and parent link agrees with the pinned
root-first chain. Datasets includes root; EFetch supplies the remaining
labeled lineage through Pseudomonadati, Pseudomonadota,
Alphaproteobacteria, Rickettsiales, Anaplasmataceae, Wolbachieae,
Wolbachia, and unclassified Wolbachia. Parsed inventories contain
no target child, type-material, merged-ID, or dropped row.
`EXACT` grounding does not promote the `SEEDED` lifecycle.

The similarly named
[NCBITaxon:1094263](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1094263&retmode=xml),
Wolbachia endosymbiont of Saturnus Janzen01, independently resolves
as an active species under the same parent in EFetch and
[Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1094263).
Shared lineage and a Saturnus sp. host label do not make these two
taxids equivalent. This review does not merge their evidence.

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

Exact Assembly and Nuccore queries `txid1035979[Organism:noexp]`
each returned zero with phrase-not-found/no-items diagnostics.
These bounded index results do not prove global or historical
absence of sequences or assemblies.

The broader Nuccore query `Wolbachia[Organism] AND Saturnus[All Fields]`
returned ten partial COI records. Every organism qualifier and
taxonomy cross-reference identifies **1094263, Saturnus Janzen01**,
not the reviewed taxid 1035979. Every host qualifier says Saturnus sp.;
that is a host assertion, not a replacement for the bacterial taxid.
The following are disambiguated neighboring-taxon candidates only:

| Accession | Length (nt) | Specimen voucher | GenBank-reported BOLD cross-reference |
| --- | --- | --- | --- |
| [JF902237.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902237.1) | 657 | `BIOUG<CAN>:MHAHG098-06.w` | `ASLEP044-10.COI-5P` |
| [JF902238.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902238.1) | 657 | `BIOUG<CAN>:MHAHG099-06.w` | `ASLEP045-10.COI-5P` |
| [JF902239.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902239.1) | 657 | `BIOUG<CAN>:MHAHG100-06.w` | `ASLEP046-10.COI-5P` |
| [JF902240.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902240.1) | 657 | `BIOUG<CAN>:MHAHG101-06.w` | `ASLEP047-10.COI-5P` |
| [JF902241.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902241.1) | 657 | `BIOUG<CAN>:MHAHG203-06.w` | `ASLEP051-10.COI-5P` |
| [JF902242.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902242.1) | 657 | `BIOUG<CAN>:MHAHG373-06.w` | `ASLEP060-10.COI-5P` |
| [JF902243.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902243.1) | 657 | `BIOUG<CAN>:MHAHG374-06.w` | `ASLEP061-10.COI-5P` |
| [JF902244.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902244.1) | 657 | `BIOUG<CAN>:MHAHG375-06.w` | `ASLEP062-10.COI-5P` |
| [JF902245.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902245.1) | 611 | `BIOUG<CAN>:MHAHJ409-07.w` | `ASLEP063-10.COI-5P` |
| [JF902246.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902246.1) | 609 | `BIOUG<CAN>:MHMXY1035-09.w` | `ASLEP071-10.COI-5P` |

All ten report translation table 11. Codon start is 1 except
JF902246.1, which uses 3. Protein cross-references AEG78058.1 through
AEG78067.1, primer qualifiers (including repeated qualifiers),
collectors, identifiers, coordinates, and dates were also inspected
as GenBank data; independent protein/BOLD objects were not retrieved.
All ten report Alajuela, Area de Conservacion Guanacaste, Costa Rica.
Nine report Camino Brasilia, Sector San Cristobal; JF902245.1 instead
reports Camino Porvenir, Rincon Rainforest. These are not target
habitat assertions, cultured strains, or genome assemblies.

All ten retain an unpublished Smith manuscript reference and a
direct submission dated 1 May 2011 at the University of Guelph.
The related
[Smith et al. primary PLOS ONE paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0036514),
DOI `10.1371/journal.pone.0036514`, describes bacterial COI recovered
during insect barcoding, `.w` specimen IDs, and accession details in
Table S2. Main-text search did not match Saturnus; Table S2 was not
inspected. The paper provides methodological context, not an inspected
exact-target allele, prevalence, or reproductive-phenotype assignment.
GenBank's unpublished reference labels are not evidence that no
related publication exists.

No sequence, voucher, locality, allele, phenotype, or infection count
from taxid 1094263 is transferred to taxid 1035979. Current NCBI
date fields alone do not establish historical reassignment or synonymy.

## Completeness

Complete enough for its generated NCBI-only identity purpose.
Optional nomenclature, mappings, strain/genome objects, and causal
claims are appropriately unasserted on the inspected evidence.

Ignored-independent search used `rg --no-ignore --hidden -n -z -i`
across `data/raw/`, `data/catalog/`, `data/bacdive/`, `data/bvbrc/`,
`data/gold/`, `data/seqcode/`, `data/straininfo/`, `data/atb/`,
`curation/`, and `history/`, including ignored, hidden, and compressed
content. Patterns covered taxid, label, slug, broader Wolbachia/Saturnus
combinations, and all ten marker, voucher, and BOLD stems above.

All 22 candidate rows were fully read:

- Three are the target backbone, scope, and native scientific-name rows.
- Three concern the separate taxid 1094263: backbone line 235309, scope line 333622, and native name line 47538 in `ncbi_names-0005.jsonl.gz`. Their complete rows support the neighboring identity, not a target alias.
- Two concern Actinomycetota bacterium WBB_12_002, taxid 2900548, GCA_010030895.1, at `data/catalog/gtdb_genomes-0017.jsonl.gz:16295` and `data/catalog/ncbi_genbank-0008.jsonl.gz:40774`. The genome-size value 1035979 causes the match. SAMN10223862, PRJNA495371, and the Chattahoochee River metagenome context are unrelated to the target.
- Three concern Bradyrhizobium japonicum USDA 160, taxid 375, GCA/GCF_040549585.1 and SAMN41513998, at `data/catalog/ncbi_genbank-0037.jsonl.gz:3543`, `data/catalog/ncbi_refseq-0006.jsonl.gz:14461`, and `data/catalog/gtdb_genomes-0003.jsonl.gz:24425`. The genome-size value 10359791 causes a substring match. Their source-classification differences do not concern this target.
- Ten ATB rows at lines 143609-143618 concern Escherichia coli samples SAMEA110359790 through SAMEA110359799. Sample digits cause the matches.
- One ATB row at line 549209 concerns Klebsiella pneumoniae sample SAMEA3357088, assembly ERZ3256563, and run ERR1035979. The run ID is a numeric collision, not taxonomy evidence.

The expanded marker/voucher/BOLD search added no rows. Five native
`SOURCE.json` files were parsed completely and history filenames
searched independently. No additional applicable local assertion,
culture deposit, strain-genome link, or standalone target history
artifact was found within these bounded roots. No global absence
is claimed.

iModulonDB is not applicable: no regulator, expression module, or
transcriptomic dataset is asserted. Neighboring COI barcoding data
does not establish an expression-module claim.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, empty synonym fields, one-name
attestation, inventoried strain count, optional omissions, and seed
provenance are supported. The broader sequence hits resolve to a
separate taxid and do not establish missing target genome links.

## Recommended Edits

None required. Preserve generated YAML and `mapping_status: SEEDED`.
No status promotion or history event is authorized by this review.
Future source corrections belong to maintained upstream inputs and
`src/taxonmech/extract.py`/`src/taxonmech/seed.py`; scope changes belong
to `curation/seed_scope.tsv`. Do not patch generated YAML/pages.

## Follow-up Checks

No corrective follow-up is required. Any proposed linkage to Saturnus
Janzen01 requires explicit authoritative taxonomic or accession-level
evidence; the host string alone is insufficient. Optional enrichment
should inspect Table S2 and exact accession-level primary evidence
without importing neighboring-taxon claims.
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
