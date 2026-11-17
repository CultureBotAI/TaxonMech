# YAML Record Review: marine sediment bacterium BB0608_AND_6.1_2G0

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_6_1_2g0.yaml`
- Started UTC: 2026-10-04T14:18:05Z
- Finished UTC: 2026-10-04T14:18:59Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: `NCBITaxon:1033572`, species, Bacteria,
`EXACT`, `SEEDED`, genetic code 11, four ancestors, zero inventoried strains,
one NCBITAXON NAME attestation and one seed event. Exact designation
BB0608_AND_6.1_2G0 distinguishes neighboring records.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_6_1_2g0.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_6_1_2g0.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Complete backbone/ancestor, synonym, attestation, scope and seed-text comparisons passed. Exact type-material, merged-ID and dropped scans found no target rows; direct children: zero.
- Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global term/reference checks, provenance/history/product gates and rendering. Bounded comparisons do not replace these gates.

## Identity and Grounding

Backbone row 221206 and scientific-name row 30514 in
`data/catalog/ncbi_names-0005.jsonl.gz` match. Live
[EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033572&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033572)
confirm the exact name and species rank; EFetch confirms parent 49928 and
code 11. Root-first lineage is root (1), cellular organisms (131567),
Bacteria (2), unclassified Bacteria (49928), with matching ranks.
Species rank does not prove valid publication or finer placement.

## Evidence

Exact Nuccore search returned [JF750117.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750117.1),
UID 333384464, one 423-base partial 16S rRNA sequence. Source qualifiers
explicitly identify strain BB0608_AND_6.1_2G0, taxon 1033572, genomic DNA,
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
All seven matches were inspected: the target scope/backbone/scientific
name, three ATB rows and one native GenBank object, read in full.
Recursive structured SOURCE.json scans found zero matches. These bounded
searches do not establish universal absence.

- `data/catalog/allthebacteria.tsv.xz:64928`: SAMEA1033572, ERR068288 and ERR085997, ERZ3068974; scientific name Streptococcus pneumoniae, both Sylph fields unknown. FASTA available, assembly filter PASS, prior-HQ F, Sylph/HQ filters SYLPH_RESULTS_FAIL. Only the BioSample suffix and its AWS URL match.
- ATB row 1020324: SAMN02335410, SRR1033572, ERZ4068983; scientific name Salmonella enterica subsp. enterica, earlier Sylph Salmonella enterica and current Sylph unknown. FASTA available, assembly filter PASS, prior-HQ T, Sylph/HQ filters SYLPH_RESULTS_FAIL. Only the run suffix matches.
- ATB row 2501535: SAMN32388560, SRR22881718, ERZ26241034; scientific name and both Sylph fields Salmonella enterica. FASTA available, assembly/Sylph/HQ filters PASS, prior-HQ T. Only SeqKit signature `seqkit.v0.1_DLS_k0_0bac7c1033572d732115ac6d4d373f98` matches; it is not MD5.
- `data/catalog/ncbi_genbank-0058.jsonl.gz:3419`: GCA_902836655.1, Oscillospiraceae bacterium, taxon/species 2485925, isolate MGYG-HGUT-04846, SAMEA6784239, PRJEB37358 and CADFRR000000000.1. This Contig assembly has 412 contigs, no RefSeq pair, and exclusions for metagenome derivation, fragmentation and undefined genus. Only total and ungapped length 1033572 match.

Exclusions are identity-based, not based on non-HQ status or failed Sylph
alone. None supplies a target strain/deposit/genome chain; unrelated
assembly accession versions and quality fields remain explicit.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the record and stated checks.

## Recommended Edits

None. Future corrections belong in maintained source inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope ownership is
`curation/seed_scope.tsv:321558`. Do not hand-edit generated YAML.

## Follow-up Checks

After an authorized correction, verify exact strain/deposit evidence and
inventory deltas, run `just seed-canary NCBITaxon:1033572 --force`, both
focused validators, `just verify-corpus` and remaining QC gates.
No canary or regeneration was run.

## Additional Notes

Unique path: `data/taxa/PATHS.tsv:13655`. Seed event remains
2026-09-13T17:54:04Z. NCBI's browser page was inaccessible; EFetch and
Datasets succeeded. iModulonDB was not applicable to this taxonomy-only
record. Only this report and the documented validation TSV were written;
YAML, maintained inputs, scope, history, status and GitHub were unchanged.
