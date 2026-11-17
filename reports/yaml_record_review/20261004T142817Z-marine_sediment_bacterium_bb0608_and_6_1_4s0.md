# YAML Record Review: marine sediment bacterium BB0608_AND_6.1_4S0

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_6_1_4s0.yaml`
- Started UTC: 2026-10-04T14:27:17Z
- Finished UTC: 2026-10-04T14:28:17Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: `NCBITaxon:1033577`, species, Bacteria,
`EXACT`, `SEEDED`, genetic code 11, four ancestors, zero inventoried strains,
one NCBITAXON NAME attestation and one seed event. Exact designation
BB0608_AND_6.1_4S0 distinguishes neighboring records.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_6_1_4s0.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_6_1_4s0.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Complete backbone/ancestor, synonym, attestation, scope and seed-text comparisons passed. Exact type-material, merged-ID and dropped scans found no target rows; direct children: zero.
- Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global term/reference checks, provenance/history/product gates and rendering. Bounded comparisons do not replace these gates.

## Identity and Grounding

Backbone row 221211 and scientific-name row 30519 in
`data/catalog/ncbi_names-0005.jsonl.gz` match. Live
[EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033577&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033577)
confirm the exact name and species rank; EFetch confirms parent 49928 and
code 11. Root-first lineage is root (1), cellular organisms (131567),
Bacteria (2), unclassified Bacteria (49928), with matching ranks.
Species rank does not prove valid publication or finer placement.

## Evidence

Exact Nuccore search returned [JF750122.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750122.1),
UID 333384469, one 490-base partial 16S rRNA sequence. Source qualifiers
explicitly identify strain BB0608_AND_6.1_4S0, taxon 1033577, genomic DNA,
coastal marine sediment, Australia: Gulf of Carpentaria and June 2008.
The qualifier is strain, not clone or environmental sample. This locus is
not a genome, deposit or independent classification.

Both sequence references were inspected: the unpublished Cornall, Beyer,
Streten-Joyce, McGuinness, Parry and Gibb cryopreservation study and
Cornall's direct submission dated 2011-04-01. Neither supplies a DOI/PMID;
full manuscript text was not obtained and no phenotype was inferred from
the title. Exact Assembly search returned zero with phrase-not-found and
no-items warnings. The NCBITAXON NAME count and 2026-09-13 snapshot match
the inventory; one name is not one experiment.

## Completeness

Full exact-ID scans found no target entries in BacDive, LPSN, GTDB, GOLD,
MediaDive, Madin or BactoTraits inventories. Optional fields may remain
empty; zero inventoried strains does not establish absence of cultivation.

Ignored-inclusive `rg --no-ignore --hidden -n -z` searched the digit-bounded
ID and full label/stem designation with dot/underscore alternatives across
`data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`.
All eight matches were inspected: target scope/backbone/scientific name,
two ATB rows and three native GOLD objects, each read in full. Recursive
structured SOURCE.json scans found zero matches. These bounded searches
do not establish universal absence.

- `data/catalog/allthebacteria.tsv.xz:64933`: SAMEA1033577, ERR068223, ERZ3068976; scientific name and both Sylph fields Streptococcus pneumoniae. Only the BioSample suffix and its AWS URL match.
- ATB row 1013264: SAMN01907411, SRR1033577, ERZ3639929; scientific name Salmonella enterica subsp. enterica serovar Tennessee, both Sylph fields Salmonella enterica. Only the run suffix matches.
- `data/gold/organisms.jsonl.gz:339799`: Go0490360, Enterococcus faecium ERS1033577, NCBI taxon 1352, strain ERS1033577 and empty culture-collection field.
- `data/gold/projects.jsonl.gz:261816`: Gp0374219, same organism name, explicit Go0490360, PRJEB12401 and SAMEA3726428.
- `data/gold/analyses.jsonl.gz:197697`: Ga0337715, same name, explicit project Gp0374219, blank AP organism GOLD ID, type Genome Analysis (Isolate), IMG taxon 2875025650 and four explicit GenBank entries for GCA_900044005.1: LN999990, LN999987, LN999989 and LN999988. Those sequence accessions are unversioned as supplied; no version is inferred. The external assembly/IMG/sequence records were not fetched or used as target evidence.

The GOLD matches are only name/strain accession-suffix collisions, not
the target taxon. Go, Gp and Ga denote distinct source records, not genomes;
the blank analysis organism field is not silently filled from a name.
No culture-deposit chain supports a target genome link. Both ATB rows have
available FASTAs, assembly/Sylph/HQ filters PASS and prior-HQ T; their
exclusion is identity-based, not quality-based.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the record and stated checks.

## Recommended Edits

None. Future corrections belong in maintained source inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope ownership is
`curation/seed_scope.tsv:321563`. Do not hand-edit generated YAML.

## Follow-up Checks

After an authorized correction, verify exact strain/deposit evidence and
inventory deltas, run `just seed-canary NCBITaxon:1033577 --force`, both
focused validators, `just verify-corpus` and remaining QC gates.
No canary or regeneration was run.

## Additional Notes

Unique path: `data/taxa/PATHS.tsv:13660`. Seed event remains
2026-09-13T17:54:04Z. NCBI's browser page was inaccessible; EFetch and
Datasets succeeded. iModulonDB was not applicable to this taxonomy-only
record. Only this report and the documented validation TSV were written;
YAML, maintained inputs, scope, history, status and GitHub were unchanged.
