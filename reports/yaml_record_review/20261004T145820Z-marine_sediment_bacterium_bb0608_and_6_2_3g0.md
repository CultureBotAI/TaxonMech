# YAML Record Review: marine sediment bacterium BB0608_AND_6.2_3G0

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_6_2_3g0.yaml`
- Started UTC: 2026-10-04T14:57:18Z
- Finished UTC: 2026-10-04T14:58:20Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: NCBITaxon:1033591, species, Bacteria,
EXACT/SEEDED, code 11, four ancestors, zero inventoried strains, one
NCBITAXON NAME attestation and one seed event. The full designation
BB0608_AND_6.2_3G0 distinguishes this target from neighboring records.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_6_2_3g0.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_6_2_3g0.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Complete backbone/ancestor, synonyms, attestation, scope and seed-text comparisons passed. Exact type-material, merged-ID and dropped scans found no target rows; no direct children.
- Not checked: full-corpus `just verify-corpus`, QC, tests, global term/reference checks, provenance/history/product gates and rendering. Bounded comparisons are not substitutes.

## Identity and Grounding

Backbone row 221225 and native scientific-name row 30533 in
`data/catalog/ncbi_names-0005.jsonl.gz` agree with the YAML. Live
[EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033591&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033591)
confirm the exact name and rank; EFetch also confirms parent 49928 and code
11. Root-first lineage is root (1), cellular organisms (131567), Bacteria
(2), unclassified Bacteria (49928), with matching ranks. Species rank is
not proof of valid publication or finer taxonomic placement.

## Evidence

Exact Nuccore search returned one sequence, [JF750136.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750136.1),
UID 333384483, 327 bases of partial 16S rRNA. Inspected source qualifiers
identify strain BB0608_AND_6.2_3G0, taxon 1033591, genomic DNA, coastal
marine sediment, Australia: Gulf of Carpentaria and June 2008. This is an
explicit strain qualifier, not clone or environmental sample. The locus
does not supply a genome, culture deposit or independent classification.

Both references were inspected: Cornall, Beyer, Streten-Joyce, McGuinness,
Parry and Gibb's cryopreservation study is marked unpublished; Cornall's
direct submission is dated 2011-04-01. Neither supplies a DOI/PMID. Full
manuscript text was not obtained; no phenotype was inferred from its title.
Exact Assembly search returned zero, with phrase-not-found/no-items warnings.
The NAME count of one and snapshot 2026-09-13 match the NCBI inventory;
the count represents a name, not an experiment.

## Completeness

Complete exact-ID scans found no target rows in BacDive, LPSN, GTDB, GOLD,
MediaDive, Madin or BactoTraits inventories. Optional fields can remain
empty; zero inventoried strains does not establish absence of cultivation.

Ignored-inclusive `rg --no-ignore --hidden -n -z` searched the digit-bounded
ID, full label/slug and bare strain designation with dot/underscore variants
across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`.
The initial four matches were target scope/backbone/scientific name and
one ATB row. A supplementary bare-designation search found only the same
three target rows. Structured recursive SOURCE.json scans found no matches.
These searches establish bounded local absence, not universal absence.

ATB row `data/catalog/allthebacteria.tsv.xz:64947` has SAMEA1033591,
ERR064772 and ERZ3068997. Scientific name and both Sylph fields identify
Streptococcus pneumoniae; FASTA is available, assembly/Sylph/HQ filters
PASS and prior-HQ T. Only the sample suffix and AWS URL match the taxon
number. There is no target strain/deposit/genome chain. Exclusion is based
on identity, not quality; sample identity is distinct from assembly identity.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the record and stated checks.

## Recommended Edits

None. Future corrections belong in maintained source inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope is owned by
`curation/seed_scope.tsv:321577`. Do not hand-edit generated YAML.

## Follow-up Checks

After an authorized correction, verify exact source identity and inventory
deltas, run `just seed-canary NCBITaxon:1033591 --force`, both focused
validators, `just verify-corpus` and remaining QC gates. No canary or
regeneration was run for this review.

## Additional Notes

Unique PATHS entry: `data/taxa/PATHS.tsv:13674`. Seed event remains
2026-09-13T17:54:04Z. NCBI browser access failed; EFetch and Datasets
succeeded. iModulonDB is not applicable to this taxonomy-only record.
Only this report and the validation TSV were written; record, inputs,
scope, status, history and GitHub were not changed.
