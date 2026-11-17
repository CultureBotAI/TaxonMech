# YAML Record Review: marine sediment bacterium BB0608_2216_8.1_3G0

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_2216_8_1_3g0.yaml`
- Started UTC: 2026-10-04T10:13:47Z
- Finished UTC: 2026-10-04T10:16:57Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: `NCBITaxon:1033450`, species, Bacteria,
`EXACT`, `SEEDED`, genetic code 11, four ancestors, zero inventoried strains,
one NCBITAXON NAME attestation and one seed event. The complete designation
BB0608_2216_8.1_3G0 distinguishes this record from neighboring isolates.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_2216_8_1_3g0.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_2216_8_1_3g0.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Complete backbone, lineage, synonym, attestation, scope and seed-event comparisons passed. Exact type-material, merged-ID and dropped scans found no target rows; direct children: zero.
- Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global term/reference checks, provenance/history/product gates and rendering. Bounded comparisons do not replace those gates.

## Identity and Grounding

Backbone row 221084 and scientific-name row 30392 in
`data/catalog/ncbi_names-0005.jsonl.gz` agree with the YAML. Live NCBI
[EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033450&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033450)
confirm identity, species rank and parent 49928; EFetch confirms code 11.
The root-first lineage matches root (1), cellular organisms (131567),
Bacteria (2) and unclassified Bacteria (49928). Species rank does not prove
valid nomenclatural publication or a finer taxonomic placement.

## Evidence

Exact Nuccore search returned one entry, [JF750313.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750313.1),
UID 333384660, a 373-base partial 16S rRNA gene. Its source names strain
BB0608_2216_8.1_3G0, taxon 1033450, coastal marine sediment, Australia:
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
two unrelated ATB rows and one contig-N50 collision. Recursive structured
SOURCE.json searches found no matches. These checks do not establish
universal absence.

- ATB SAMEA1033450, run ERR084613 and ENA analysis ERZ3068805 is Staphylococcus aureus. Its BioSample suffix is not this taxon ID.
- ATB SAMN12429441, run SRR9887396 and ENA analysis ERZ25608342 is Escherichia coli. Only its SeqKit signature, `seqkit.v0.1_DLS_k0_4c0d1033450fac95b85c8bc78e138afb`, matches the numeric search. This is a SeqKit signature, not an asserted MD5 identity bridge. Both ATB rows have available FASTA and passing filters, but fail target identity.
- Full native row `data/catalog/gtdb_genomes-0000.jsonl.gz:27640` identifies RS_GCF_030362835.1, explicit GenBank accession GCA_030362835.1, Cellulomonas alba, taxon 3053467, raw strain MW4, BioSample SAMN35727582, project PRJNA224116 and WGS JAUCGQ000000000.1. Only contig N50, 1033450, matches; total length is 3795804 and ungapped length 3795794. Source context is soil in South Korea: Ilsan. Its type-material flag belongs to Cellulomonas, not the target. Native GTDB and NCBI order placements differ; neither is transferred to this record.

No target strain/deposit/genome chain is supported by these unrelated rows.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the record and stated checks.

## Recommended Edits

None. Future corrections belong in maintained source inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope ownership is
`curation/seed_scope.tsv:321436`. Do not hand-edit generated YAML.

## Follow-up Checks

After an authorized correction, verify exact strain/deposit evidence,
inspect inventory deltas, run `just seed-canary NCBITaxon:1033450 --force`,
both focused validators, `just verify-corpus` and remaining QC gates.
No canary or regeneration was run.

## Additional Notes

Unique path: `data/taxa/PATHS.tsv:13533`. Seed event remains
2026-09-13T17:54:04Z. NCBI's browser page was inaccessible; EFetch and
Datasets succeeded. iModulonDB was not applicable to this taxonomy-only
record. Only this report and the documented validation TSV were written;
YAML, maintained inputs, scope, history, status and GitHub were not changed.
