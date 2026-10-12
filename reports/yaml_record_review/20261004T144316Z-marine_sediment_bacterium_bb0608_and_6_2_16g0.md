# YAML Record Review: marine sediment bacterium BB0608_AND_6.2_16G0

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_6_2_16g0.yaml`
- Started UTC: 2026-10-04T14:42:19Z
- Finished UTC: 2026-10-04T14:43:16Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: `NCBITaxon:1033585`, species, Bacteria,
`EXACT`, `SEEDED`, genetic code 11, four ancestors, zero inventoried strains,
one NCBITAXON NAME attestation and one seed event. Exact designation
BB0608_AND_6.2_16G0 distinguishes neighboring records.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_6_2_16g0.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_6_2_16g0.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Complete backbone/ancestor, synonym, attestation, scope and seed-text comparisons passed. Exact type-material, merged-ID and dropped scans found no target rows; direct children: zero.
- Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global term/reference checks, provenance/history/product gates and rendering. Bounded comparisons do not replace these gates.

## Identity and Grounding

Backbone row 221219 and scientific-name row 30527 in
`data/catalog/ncbi_names-0005.jsonl.gz` match. Live
[EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033585&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033585)
confirm the exact name and species rank; EFetch confirms parent 49928 and
code 11. Root-first lineage is root (1), cellular organisms (131567),
Bacteria (2), unclassified Bacteria (49928), with matching ranks.
Species rank does not prove valid publication or finer placement.

## Evidence

Exact Nuccore search returned [JF750131.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750131.1),
UID 333384478, one 289-base partial 16S rRNA sequence. Source qualifiers
explicitly identify strain BB0608_AND_6.2_16G0, taxon 1033585, genomic DNA,
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
All six matches were inspected: target scope/backbone/scientific name,
one ATB row and two native JSON objects, each read in full. Recursive
structured SOURCE.json scans found zero matches. These bounded searches
do not establish universal absence.

- `data/catalog/allthebacteria.tsv.xz:64941`: SAMEA1033585, ERR068238, ERZ3068986; scientific name Streptococcus pneumoniae, both Sylph fields unknown. FASTA available, assembly filter PASS, prior-HQ F, Sylph/HQ filters SYLPH_RESULTS_FAIL. Only the BioSample suffix and its AWS URL match.
- GenBank `data/catalog/ncbi_genbank-0035.jsonl.gz:49139` and GTDB `data/catalog/gtdb_genomes-0017.jsonl.gz:47664`: GCA_038891995.1 and GB_GCA_038891995.1 with an explicit GenBank link; Acidilobaceae archaeon, taxon/species 2933264, isolate ZMQR_201808_bins_1, SAMN36038390, PRJNA544494 and JAWAUG000000000.1. This metagenome-derived Scaffold assembly has 143 contigs, 129 scaffolds and no RefSeq pair. Only ungapped length 1033585 matches; total length is 1033725, a 140-base difference also carried as GTDB gap length. Both identify Archaea, not the target's Bacteria domain. GTDB places it in Thermoprotei_A/Sulfolobales, species JAWAWX01 sp038824665, while carried NCBI classification uses Thermoprotei/Acidilobales and unclassified Acidilobaceae. PMID 38744885 on the unrelated GenBank record was not retrieved or used as target evidence.

Exclusions are identity-based, not based on non-HQ status or failed Sylph
alone. Neither supplies a target strain/deposit/genome chain. Explicit
assembly crosslinks, accession versions and source classifications are
preserved without transferring evidence to the target.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the record and stated checks.

## Recommended Edits

None. Future corrections belong in maintained source inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope ownership is
`curation/seed_scope.tsv:321571`. Do not hand-edit generated YAML.

## Follow-up Checks

After an authorized correction, verify exact strain/deposit evidence and
inventory deltas, run `just seed-canary NCBITaxon:1033585 --force`, both
focused validators, `just verify-corpus` and remaining QC gates.
No canary or regeneration was run.

## Additional Notes

Unique path: `data/taxa/PATHS.tsv:13668`. Seed event remains
2026-09-13T17:54:04Z. NCBI's browser page was inaccessible; EFetch and
Datasets succeeded. iModulonDB was not applicable to this taxonomy-only
record. Only this report and the documented validation TSV were written;
YAML, maintained inputs, scope, history, status and GitHub were unchanged.
