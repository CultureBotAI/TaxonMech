# YAML Record Review: marine sediment bacterium BB0608_2216_7.2_7G0

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_2216_7_2_7g0.yaml`
- Started UTC: 2026-10-04T10:05:27Z
- Finished UTC: 2026-10-04T10:06:26Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: `NCBITaxon:1033446`, species, Bacteria,
`EXACT`, `SEEDED`, genetic code 11, four ancestors, zero inventoried strains,
one NCBITAXON NAME attestation and one seed event. The full designation
BB0608_2216_7.2_7G0 distinguishes neighboring isolates.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_2216_7_2_7g0.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_2216_7_2_7g0.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Complete backbone, lineage, synonym, attestation, scope and seed-event comparisons passed. Exact type-material, merged-ID and dropped scans found no target rows; direct children: zero.
- Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global term/reference checks, provenance/history/product gates and rendering. Bounded comparisons do not replace those gates.

## Identity and Grounding

Backbone row 221080 and scientific-name row 30388 in
`data/catalog/ncbi_names-0005.jsonl.gz` agree with the YAML. Live NCBI
[EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033446&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033446)
confirm identity, species rank and parent 49928; EFetch confirms code 11.
The root-first lineage matches root (1), cellular organisms (131567),
Bacteria (2) and unclassified Bacteria (49928). Species rank does not prove
valid nomenclatural publication or a finer taxonomic placement.

## Evidence

Exact Nuccore search returned one entry, [JF750309.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750309.1),
UID 333384656, a 547-base partial 16S rRNA gene. Its source names strain
BB0608_2216_7.2_7G0, taxon 1033446, coastal marine sediment, Australia:
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
All six matches were inspected: target backbone, scope and scientific name,
two unrelated ATB rows and one genome-length collision. Recursive structured
SOURCE.json searches found no matches. These checks do not establish
universal absence.

- ATB SAMEA1033446, run ERR223114 and ENA analysis ERZ3068800 is Staphylococcus aureus. Its BioSample suffix is not this taxon ID.
- ATB SAMN12747978, run SRR10119456 and ENA analysis ERZ25648922 matches only the substring in `seqkit.v0.1_DLS_k0_0b27ca09a2e7a1033446b19fc39e415e`. The TSV header was inspected: scientific_name is Shigella sonnei, while both supplied Sylph species fields say Escherichia coli. These fields are not interchangeable. A SeqKit sum is not MD5 or an identity key for the target.
- Full native row `data/catalog/ncbi_genbank-0066.jsonl.gz:40506` identifies GCA_982880845.1 as Synechococcus sp., taxon 1131, isolate GIFF20-1_SAMN15311067_MAG_00000014, BioSample SAMEA122259955, project PRJEB72997 and WGS CEYOXO000000000.1. Only ungapped length 1033446 matches; total length is 1036546. It is metagenome-derived with no supplied RefSeq pair.

Both ATB rows have available FASTAs and passing filters, but those statuses
do not establish target identity. No target strain/deposit/genome chain is
supported by these unrelated entries.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the record and stated checks.

## Recommended Edits

None. Future corrections belong in maintained source inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope ownership is
`curation/seed_scope.tsv:321432`. Do not hand-edit generated YAML.

## Follow-up Checks

After an authorized correction, verify exact strain/deposit evidence,
inspect inventory deltas, run `just seed-canary NCBITaxon:1033446 --force`,
both focused validators, `just verify-corpus` and remaining QC gates.
No canary or regeneration was run.

## Additional Notes

Unique path: `data/taxa/PATHS.tsv:13529`. Seed event remains
2026-09-13T17:54:04Z. NCBI's browser page was inaccessible; EFetch and
Datasets succeeded. iModulonDB was not applicable to this taxonomy-only
record. Only this report and the documented validation TSV were written;
YAML, maintained inputs, scope, history, status and GitHub were not changed.
