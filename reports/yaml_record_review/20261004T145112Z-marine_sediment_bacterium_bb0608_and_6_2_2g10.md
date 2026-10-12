# YAML Record Review: marine sediment bacterium BB0608_AND_6.2_2G10

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_6_2_2g10.yaml`
- Started UTC: 2026-10-04T14:50:11Z
- Finished UTC: 2026-10-04T14:51:12Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: `NCBITaxon:1033589`, species, Bacteria,
`EXACT`, `SEEDED`, genetic code 11, four ancestors, zero inventoried strains,
one NCBITAXON NAME attestation and one seed event. Exact designation
BB0608_AND_6.2_2G10 distinguishes neighboring records, including 2G0.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_6_2_2g10.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_6_2_2g10.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Complete backbone/ancestor, synonym, attestation, scope and seed-text comparisons passed. Exact type-material, merged-ID and dropped scans found no target rows; direct children: zero.
- Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global term/reference checks, provenance/history/product gates and rendering. Bounded comparisons do not replace these gates.

## Identity and Grounding

Backbone row 221223 and scientific-name row 30531 in
`data/catalog/ncbi_names-0005.jsonl.gz` match. Live
[EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033589&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033589)
confirm the exact name and species rank; EFetch confirms parent 49928 and
code 11. Root-first lineage is root (1), cellular organisms (131567),
Bacteria (2), unclassified Bacteria (49928), with matching ranks.
Species rank does not prove valid publication or finer placement.

## Evidence

Exact Nuccore search returned [JF750140.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750140.1),
UID 333384487, one 380-base partial 16S rRNA sequence. Source qualifiers
explicitly identify strain BB0608_AND_6.2_2G10, taxon 1033589, genomic DNA,
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

- `data/catalog/allthebacteria.tsv.xz:64945`: SAMEA1033589, ERR068301 and ERR086010, ERZ3068989; scientific name and both Sylph fields Streptococcus pneumoniae. FASTA available, assembly/Sylph/HQ filters PASS, prior-HQ T. Only the BioSample suffix and its AWS URL match.
- GenBank `data/catalog/ncbi_genbank-0024.jsonl.gz:2504` and GTDB `data/catalog/gtdb_genomes-0017.jsonl.gz:33593`: GCA_025937375.1 and GB_GCA_025937375.1 with an explicit GenBank link; Nitrososphaera sp., taxon/species 1971748, isolate TY_ISSM_2_bin.16, SAMN20133325, PRJNA744024 and JAICRK000000000.1. This metagenome-derived Contig assembly has 220 contigs and no RefSeq pair. Only total and ungapped length 1033589 match. Both identify Archaea, not this target's Bacteria domain. GTDB places it in Thermoproteota, species Nitrososphaera sp025929855; carried NCBI classification uses Nitrososphaerota and unclassified Nitrososphaera. These source classifications concern the unrelated assembly and are not reconciled here.

Exclusions are identity-based, not quality-based. Neither supplies a target
strain/deposit/genome chain. Explicit assembly links, accession versions
and source classifications are preserved without transferring evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the record and stated checks.

## Recommended Edits

None. Future corrections belong in maintained source inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope ownership is
`curation/seed_scope.tsv:321575`. Do not hand-edit generated YAML.

## Follow-up Checks

After an authorized correction, verify exact strain/deposit evidence and
inventory deltas, run `just seed-canary NCBITaxon:1033589 --force`, both
focused validators, `just verify-corpus` and remaining QC gates.
No canary or regeneration was run.

## Additional Notes

Unique path: `data/taxa/PATHS.tsv:13672`. Seed event remains
2026-09-13T17:54:04Z. NCBI's browser page was inaccessible; EFetch and
Datasets succeeded. iModulonDB was not applicable to this taxonomy-only
record. Only this report and the documented validation TSV were written;
YAML, maintained inputs, scope, history, status and GitHub were unchanged.
