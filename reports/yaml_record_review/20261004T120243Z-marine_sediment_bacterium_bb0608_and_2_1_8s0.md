# YAML Record Review: marine sediment bacterium BB0608_AND_2.1_8S0

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_2_1_8s0.yaml`
- Started UTC: 2026-10-04T12:01:43Z
- Finished UTC: 2026-10-04T12:02:43Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: `NCBITaxon:1033504`, species, Bacteria,
`EXACT`, `SEEDED`, genetic code 11, four ancestors, zero inventoried strains,
one NCBITAXON NAME attestation and one seed event. The full designation
BB0608_AND_2.1_8S0 distinguishes neighboring AND_2.1 isolates.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_2_1_8s0.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_2_1_8s0.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Complete backbone, lineage, synonym, attestation, scope and seed-event comparisons passed. Exact type-material, merged-ID and dropped scans found no target rows; direct children: zero.
- Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global term/reference checks, provenance/history/product gates and rendering. Bounded comparisons do not replace those gates.

## Identity and Grounding

Backbone row 221138 and scientific-name row 30446 in
`data/catalog/ncbi_names-0005.jsonl.gz` agree with the YAML. Live NCBI
[EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033504&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033504)
confirm identity and species rank; EFetch confirms parent 49928 and code 11.
The root-first lineage matches root (1), cellular organisms (131567),
Bacteria (2) and unclassified Bacteria (49928). Species rank does not prove
valid nomenclatural publication or a finer taxonomic placement.

## Evidence

Exact Nuccore search returned one entry, [JF750047.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750047.1),
UID 333384394, a 547-base partial 16S rRNA gene. Its source names strain
BB0608_AND_2.1_8S0, taxon 1033504, coastal marine sediment, Australia:
Gulf of Carpentaria, and June 2008 collection. The qualifier is strain,
not clone or environmental sample. This locus is not a genome, culture
deposit or independent taxonomic classification.

Both references were inspected: Cornall, Beyer, Streten-Joyce, McGuinness,
Parry and Gibb's marine-sediment cryopreservation study marked unpublished,
and Cornall's direct submission dated 2011-04-01. Neither supplies a DOI
or PMID. Full manuscript text was not obtained; no phenotype was inferred
from the title. Exact Assembly search returned zero with phrase-not-found
and no-items warnings. The NAME attestation and 2026-09-13 snapshot agree
with the inventory; the count is not a number of independent experiments.

## Completeness

Complete exact-ID scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and
BactoTraits inventories found no rows. Empty optional slots reflect bounded
source coverage; zero inventoried strains does not mean never cultured.

Ignored-inclusive `rg --no-ignore --hidden -n -z` searched the digit-bounded
numeric ID and complete label/stem designation, allowing dots/underscores,
across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`.
All seven matches were inspected: target backbone, scope and scientific
name, two unrelated ATB rows and two genome-length collisions. Recursive
structured SOURCE.json searches found no matches. These checks do not
establish universal absence.

- ATB row 64860 in `data/catalog/allthebacteria.tsv.xz` identifies SAMEA1033504, run ERR068144 and ENA analysis ERZ3068885 as Streptococcus pneumoniae in the scientific-name and both Sylph fields. FASTA is available, assembly/Sylph filters pass, prior-HQ status is F, and the HQ filter is CHECKM2_MAX_CONTAM. Its BioSample suffix is not this taxon ID. Non-HQ status alone does not disqualify an available FASTA; exclusion is identity, not quality.
- ATB row 1021128 identifies SAMN02345328, run SRR1033504 and ENA analysis ERZ4070100. Its scientific name is Salmonella enterica subsp. enterica serovar Hvittingfoss; both Sylph species fields are Salmonella enterica. FASTA is available; assembly/Sylph/HQ filters pass, with prior-HQ status T. Only the run suffix matches the numeric search.
- The full native row `data/catalog/ncbi_genbank-0026.jsonl.gz:13808` identifies GCA_028255425.1, Akkermansiaceae bacterium, taxon and species taxon 2562705, isolate AH-654-A06, BioSample SAMN29372420, project PRJNA846736 and WGS JAOKQH000000000.1. It is single-cell-derived, has 88 contigs and no paired RefSeq assembly. Its PMID 36477536 was not retrieved or used as target evidence; the native identity fields already exclude it.
- The full native row `data/catalog/ncbi_genbank-0065.jsonl.gz:21093` identifies GCA_977869525.1, Christensenellales bacterium, taxon and species taxon 3083246, isolate shnw1_bin_226, BioSample SAMEA118406158, project PRJEB89408 and WGS CDWIWV000000000.1. It is metagenome-derived, has 29 contigs and no paired RefSeq assembly. Both unrelated genomes match only through total/ungapped length 1033504, not taxon identity.

No target strain/deposit/genome chain is supported by these unrelated rows.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the record and stated checks.

## Recommended Edits

None. Future corrections belong in maintained source inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope ownership is
`curation/seed_scope.tsv:321490`. Do not hand-edit generated YAML.

## Follow-up Checks

After an authorized correction, verify exact strain/deposit evidence,
inspect inventory deltas, run `just seed-canary NCBITaxon:1033504 --force`,
both focused validators, `just verify-corpus` and remaining QC gates.
No canary or regeneration was run.

## Additional Notes

Unique path: `data/taxa/PATHS.tsv:13587`. Seed event remains
2026-09-13T17:54:04Z. NCBI's browser page was inaccessible; EFetch and
Datasets succeeded. iModulonDB was not applicable to this taxonomy-only
record. Only this report and the documented validation TSV were written;
YAML, maintained inputs, scope, history, status and GitHub were not changed.
