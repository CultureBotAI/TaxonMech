# YAML Record Review: marine sediment bacterium BB0608_AND_3.2_5G0

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_3_2_5g0.yaml`
- Started UTC: 2026-10-04T12:42:25Z
- Finished UTC: 2026-10-04T12:43:25Z
- Verdict: pass

## Target

Full generated `TaxonRecord` read: `NCBITaxon:1033523`, species, Bacteria,
`EXACT`, `SEEDED`, genetic code 11, four ancestors, zero inventoried strains,
one NCBITAXON NAME attestation and one seed event. The complete designation
BB0608_AND_3.2_5G0 distinguishes adjacent BB0608 isolates.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_3_2_5g0.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_3_2_5g0.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Full backbone, lineage, synonyms, attestation, scope and seed-text comparisons passed. Exact type-material, merged-ID and dropped scans found no target rows; direct children: zero.
- Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global term/reference checks, provenance/history/product gates and rendering. Bounded comparisons do not replace those gates.

## Identity and Grounding

Backbone row 221157 and scientific-name row 30465 in
`data/catalog/ncbi_names-0005.jsonl.gz` agree with the YAML. Live NCBI
[EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033523&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033523)
confirm identity and species rank; EFetch confirms parent 49928 and code 11.
Root-first lineage is root (1), cellular organisms (131567), Bacteria (2)
and unclassified Bacteria (49928), matching the record. Species rank alone
does not establish valid publication or a finer classification.

## Evidence

Exact Nuccore search returned one sequence, [JF750065.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750065.1),
UID 333384412, a 533-base partial 16S rRNA gene. Source qualifiers explicitly
name strain BB0608_AND_3.2_5G0, taxon 1033523, coastal marine sediment,
Australia: Gulf of Carpentaria and June 2008 collection. This is a strain
qualifier, not clone or environmental sample. The locus is not an assembly,
culture deposit or independent classification.

Both references were read: Cornall, Beyer, Streten-Joyce, McGuinness, Parry
and Gibb's marine-sediment cryopreservation study marked unpublished, and
Cornall's direct submission dated 2011-04-01. Neither reference supplies
a DOI or PMID. Full manuscript text was not obtained; no phenotype is
inferred from the title. Exact Assembly search returned zero with
phrase-not-found and no-items warnings. The one NAME assertion and
2026-09-13 snapshot match the inventory, not a count of experiments.

## Completeness

Complete exact-ID scans found no rows in BacDive, LPSN, GTDB, GOLD,
MediaDive, Madin or BactoTraits inventories. Empty optional slots reflect
bounded coverage; zero inventoried strains does not mean never cultured.

Ignored-inclusive `rg --no-ignore --hidden -n -z` searched the digit-bounded
numeric ID and complete label/stem designation, allowing dots/underscores,
across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`.
All five matches were inspected: target scope, backbone and scientific
name, plus two unrelated ATB rows. Recursive structured SOURCE.json scans
found no matches. These bounded searches do not prove universal absence.

- ATB row 64879 in `data/catalog/allthebacteria.tsv.xz`: SAMEA1033523, runs ERR068291 and ERR086000, analysis ERZ3068913; scientific name and both Sylph fields are Streptococcus pneumoniae. FASTA available, assembly/Sylph/HQ filters PASS, prior-HQ T. Only the BioSample suffix matches this taxon's number.
- ATB row 1021352: SAMN02345554, runs SRR1033523 and SRR3191392, analysis ERZ4070476; scientific name and earlier Sylph name are Salmonella enterica, current Sylph name unknown. FASTA available, assembly filter PASS, prior-HQ T, current Sylph and HQ filters SYLPH_RESULTS_FAIL. Only the run suffix matches.

Exclusion is based on identity, not quality: a non-HQ or Sylph-failing
available FASTA is not automatically ineligible. Neither unrelated row
supports a target strain/deposit/genome chain. ATB column meanings were
checked against the actual header.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the record and stated checks.

## Recommended Edits

None. Future corrections belong in maintained source inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope ownership is
`curation/seed_scope.tsv:321509`. Do not hand-edit generated YAML.

## Follow-up Checks

After an authorized correction, verify exact strain/deposit evidence,
inspect inventory deltas, run `just seed-canary NCBITaxon:1033523 --force`,
both focused validators, `just verify-corpus` and remaining QC gates.
No canary or regeneration was run.

## Additional Notes

Unique path: `data/taxa/PATHS.tsv:13606`. Seed event remains
2026-09-13T17:54:04Z. NCBI's browser page was inaccessible; EFetch and
Datasets succeeded. iModulonDB was not applicable to this taxonomy-only
record. Only this report and the documented validation TSV were written;
YAML, maintained inputs, scope, history, status and GitHub were unchanged.
