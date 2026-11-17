# YAML Record Review: Fusobacterium sp. OBRC1

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/fusobacterium_sp_obrc1.yaml`
- Started UTC: 2026-10-04T00:53:37Z
- Finished UTC: 2026-10-04T00:55:43Z
- Verdict: pass

## Target

Read all 78 lines of generated `TaxonRecord` NCBITaxon:1032505,
Fusobacterium sp. OBRC1. It carries `SPECIES`, `BACTERIA`, `EXACT`,
`SEEDED`, parent NCBITaxon:2648384, code11, ten ancestors, one GTDB
mapping/synonym/xref, three attestations and `strain_count: 0`.
No listed strains, genomes, nomenclature, general evidence or causal
graph are carried. No YAML, source, history or status was edited.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/fusobacterium_sp_obrc1.yaml` | Passed; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/fusobacterium_sp_obrc1.yaml` | Passed; one file, zero ERROR rows; diagnostic `reports/instance_validation_failures.tsv`. |
| Source comparison | Identity, parent, code, full lineage, names, mapping, path, scope, attestations and seed event agree. |
| History/reference checks | Embedded event checked; ignored-inclusive searches found no target standalone history entry. No curator-added graph/product grounding requires validation. |
| Source census checks | All 901,341 native GTDB rows scanned for the exact species cluster; all 3,227,665 ATB rows scanned for both relevant whole BioSample accessions. |

Not checked: full-corpus `just verify-corpus`, `just qc`, global provenance,
full tests, rendering, exports, sequence alignment, FASTA download or
complete review of the other GTDB members. Focused comparisons do not
prove corpus reproduction. No generator ran.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220864`, the
[NCBI browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1032505),
live [EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032505&retmode=xml)
and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032505)
agree on exact identity, species rank, parent2648384 and code11. The full
root-first lineage agrees through Fusobacteriati, Fusobacteriota,
Fusobacteriia, Fusobacteriales, Fusobacteriaceae, Fusobacterium and
unclassified Fusobacterium. Complete backbone scanning found no children.

The NCBI concept is a species-level placeholder, not a `STRAIN` child of
F. polymorphum. GTDB assigns its genome to the F. polymorphum species
cluster. The retained source-specific species name is supported as a
GTDB classification; it must not be read as NCBI synonym approval or as
equivalence between OBRC1 and the type strain. No lineage reconciliation
or change of NCBI identifier is warranted.

Native names0005:30153 supports the scientific name; no NCBI synonym is
carried. `data/taxa/PATHS.tsv:13237`, scope row36142 and legacy row775
agree. The September13 seed event reproduces the September12 scope reason.

## Evidence

- Raw GTDB mapping1348 supplies `GTDB:s__Fusobacterium_polymorphum`,
  `skos:closeMatch` and count162; species row65325 confirms the count.
  All 162 native entries have distinct genome accessions. Their NCBI
  taxon counts are 76857:108, 851:45, 393480:3 and one each for1032505,
  936563, 68766, 1316587, 1357398 and1739543. This is the source
  species-cluster size, exactly the schema's `genome_count` meaning,
  not 162 OBRC1 assemblies. Multiple source mappings are retained;
  they are not proof that all mapped NCBI concepts are interchangeable.
- Native GTDB0000:34486 explicitly places RS_GCF_000524235.1, strain
  OBRC1, taxon/species1032505 and sample SAMN02641567 in that cluster.
  It is nonrepresentative. The representative at GTDB0008:43572 is
  RS_GCF_001457555.1, NCTC10562, taxon76857, sample SAMEA2479572,
  explicitly from type material. The representative's strain, sample
  and isolation metadata were not transferred to OBRC1.
- Live [assembly metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCF_000524235.1/dataset_report)
  confirms current GCF_000524235.1, paired GCA_000524235.1, OBRC1,
  sample SAMN02641567, project PRJNA165911 and the 87-contig,
  2,497,272bp assembly. Its ANI context reports a 97.2% best match to
  type assembly GCA_000153625.1, F. polymorphum, with 80.23% assembly
  coverage and 82.11% type-assembly coverage. This supports the GTDB
  species placement while NCBI still retains its placeholder identity;
  it does not claim identical genomes or a deposited type strain.
- [LPSN28163](https://lpsn.dsmz.de/species/fusobacterium-polymorphum)
  considers F. polymorphum validly published but taxonomically suspended,
  preferring F. nucleatum subsp. polymorphum. The type includes NCTC10562,
  not OBRC1. The local LPSN row5034 maps this name to NCBITaxon:76857,
  not target1032505. That naming disagreement is preserved; it neither
  invalidates GTDB's explicitly sourced name nor authorizes copying
  LPSN nomenclature and type deposits onto this record.
- Native GenBank0000:17250 and RefSeq0000:14336 supply the explicit
  identical GCA/GCF_000524235.1 pair and SAMN02641567. Their projects
  PRJNA165911 and PRJNA224116 respectively remain separate source
  metadata. BV-BRC0000:3169 supplies1032505.3 with the GenBank
  assembly and sample but an empty culture-collection field and bareOBRC1.
- GOLD organism17482 is Go0020562, taxon1032505, strainOBRC1 with
  no culture-collection identifier. Project16899, Gp0020562, explicitly
  connects that organism to PRJNA165911 and SAMN02641567. Analysis14876,
  Ga0023811, names the project, GCA_000524235.1 and IMG2558860927;
  its organism field is empty, so the project supplies the connection.
  These catalog assertions are real, but without an eligible collection
  deposit they do not supply a BacDive strain join. Go/Gp/Ga remain
  related source records, not genome identifiers.
- ATB row1020545 describes SAMN02344608, SRR965188 and ERZ4069186
  with scientific name OBRC1, F. polymorphum classification, available
  FASTA and PASS filters. Its whole sample accession differs from
  SAMN02641567 carried by the assembly/GOLD chain. Complete ATB scanning
  found that row and no SAMN02641567 row. Neither sample was found in
  the searched raw, BacDive or StrainInfo relationship surfaces, and no
  corresponding ATB overlap entry was found. An eligible FASTA alone
  does not establish a strain/sample/genome evidence chain. No shared-name
  join or cross-database sequence identity is inferred.
- NCBI NAME1, GTDB GENOME162 and Madin TRAIT_ASSERTION1 reproduce
  the exact source units; Madin is `data/raw/madin_taxa.tsv:610`.
  These counts are not summed or promoted to phenotype claims. Full
  exact-target raw scans found no BacDive, LPSN, GOLD aggregate,
  MediaDive or BactoTraits row; native GOLD evidence above remains
  present despite the absent aggregate attestation.

## Completeness

Zero listed strains is consistent with the BacDive inventory and lack of
descendants. It is not biological absence of OBRC1 or its sequenced genome.
The maintained source-catalog design deliberately retains native genomes
without fabricating a culture-deposit association. BareOBRC1, taxon1032505,
HMP1501 and the differently accessioned ATB sample do not substitute for
the required full registered collection identifier and source chain.

Ignored-inclusive identifier, label, slug and whole OBRC1 searches covered
raw tables, catalog shards, BacDive, BV-BRC, GOLD, SeqCode, StrainInfo,
ATB inventories, curation and history. SOURCE.json files were separately
JSON-traversed with no target match. Structured scans found no own NCBI
type-material, merged-ID or dropped row. No standalone history entry or
eligible deposit was found on those surfaces. This is not a claim of
global biological absence. Optional definition, nomenclature, general
evidence and graph slots need not be invented. iModulonDB was not
applicable: the record makes no gene, regulator or transcriptomic claim.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the reviewed record. The differing taxonomic classifications,
species-wide count and unjoined genome catalogs are supported source
context rather than evidence for silent harmonization or fabricated links.

## Recommended Edits

None. Preserve generated YAML and `SEEDED`. Any future mapping-semantics
change belongs in the kg-microbe transform and `src/taxonmech/seed.py`,
with provenance and a regression test, not a manual YAML edit. A future
taxon-native genome presentation would require an explicit maintained model
decision, not an invented BacDive strain entry.

## Follow-up Checks

- At an authorized refresh, recheck NCBI1032505, the GTDB cluster and
  LPSN's nomenclatural status separately; do not conflate their authorities.
- If a deposited culture becomes available, verify its full CAFI accession,
  own source evidence and exact BioSample before generating links.
- Recheck the two distinct sample accessions before any ATB enrichment;
  shared label or species assignment does not establish shared BioSample.
- After maintained changes and regeneration, run both focused validators
  and the full documented corpus gates.

## Additional Notes

The GTDB public page did not supply usable text; its complete pinned
structured catalog supplied the species evidence. Live Nuccore search
returned179 records; only the first20 were inspected, including the WGS
master,18 contigs and a patent sequence. That bounded context check is
not a complete sequence audit. The WGS source names OBRC1/HMP1501
and a2014 JCVI direct submission; the patent's plant-treatment title is
not evidence for this organism's phenotype. No missing host metadata
was inferred from the generic BioSample package title. All checks were
read-only except this report and validator diagnostic. Eukaryota reviews
were untouched.
