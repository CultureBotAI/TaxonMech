# YAML Record Review: marine sediment bacterium BB0608_AND_1.1_3S0

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_1_1_3s0.yaml`
- Started UTC: 2026-10-04T10:57:55Z
- Finished UTC: 2026-10-04T10:58:44Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: `NCBITaxon:1033472`, species, Bacteria,
`EXACT`, `SEEDED`, genetic code 11, four ancestors, zero inventoried strains,
one NCBITAXON NAME attestation and one seed event. The full designation
BB0608_AND_1.1_3S0 distinguishes neighboring isolates, including 3G0 and
records with BB0608_2216 designations.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_1_1_3s0.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_1_1_3s0.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Complete backbone, lineage, synonym, attestation, scope and seed-event comparisons passed. Exact type-material, merged-ID and dropped scans found no target rows; direct children: zero.
- Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global term/reference checks, provenance/history/product gates and rendering. Bounded comparisons do not replace those gates.

## Identity and Grounding

Backbone row 221106 and scientific-name row 30414 in
`data/catalog/ncbi_names-0005.jsonl.gz` agree with the YAML. Live NCBI
[EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033472&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033472)
confirm identity, species rank and parent 49928; EFetch confirms code 11.
The root-first lineage matches root (1), cellular organisms (131567),
Bacteria (2) and unclassified Bacteria (49928). Species rank does not prove
valid nomenclatural publication or a finer taxonomic placement.

## Evidence

Exact Nuccore search returned one entry, [JF750018.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750018.1),
UID 333384365, a 501-base partial 16S rRNA gene. Its source names strain
BB0608_AND_1.1_3S0, taxon 1033472, coastal marine sediment, Australia:
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
All seven matches were inspected: target backbone, scope and scientific name,
two unrelated ATB rows and two genome-length collisions. Recursive structured
SOURCE.json searches found no matches. These checks do not establish
universal absence.

- ATB SAMEA1033472, run ERR084666 and ENA analysis ERZ3068839 is Staphylococcus aureus. Its BioSample suffix is not this taxon ID.
- ATB SAMN02335403, run SRR1033472 and ENA analysis ERZ4068968 has scientific name Salmonella enterica subsp. enterica serovar Agona, with Salmonella enterica in both Sylph species fields. Only the run accession suffix matches the numeric search. Both ATB rows have available FASTA and passing filters, but fail target identity.
- Full native rows `data/catalog/ncbi_genbank-0016.jsonl.gz:37846` and `data/catalog/gtdb_genomes-0017.jsonl.gz:39966` identify GCA_018302805.1 / GB_GCA_018302805.1, Candidatus Woesearchaeota archaeon, taxon 2026803, isolate RIFCSPLOWO2_02_FULL_30_14, BioSample SAMN18341350, project PRJNA288027 and WGS JAGVZD000000000.1. Only ungapped length, 1033472, matches; total length is 1033607. This is a metagenome-derived archaeal assembly with no RefSeq paired assembly. GTDB classifies it as JAGVZF01 sp018302805 in Nanobdellota. Its Rifle, Colorado well context, isolate and archaeal taxonomy differ from the target; neither classification is transferred to this bacterial record.

No target strain/deposit/genome chain is supported by these unrelated rows.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the record and stated checks.

## Recommended Edits

None. Future corrections belong in maintained source inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope ownership is
`curation/seed_scope.tsv:321458`. Do not hand-edit generated YAML.

## Follow-up Checks

After an authorized correction, verify exact strain/deposit evidence,
inspect inventory deltas, run `just seed-canary NCBITaxon:1033472 --force`,
both focused validators, `just verify-corpus` and remaining QC gates.
No canary or regeneration was run.

## Additional Notes

Unique path: `data/taxa/PATHS.tsv:13555`. Seed event remains
2026-09-13T17:54:04Z. NCBI's browser page was inaccessible; EFetch and
Datasets succeeded. iModulonDB was not applicable to this taxonomy-only
record. Only this report and the documented validation TSV were written;
YAML, maintained inputs, scope, history, status and GitHub were not changed.
