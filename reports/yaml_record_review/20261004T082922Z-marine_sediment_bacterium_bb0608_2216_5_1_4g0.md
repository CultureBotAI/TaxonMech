# YAML Record Review: marine sediment bacterium BB0608_2216_5.1_4G0

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_2216_5_1_4g0.yaml`
- Started UTC: 2026-10-04T08:28:29Z
- Finished UTC: 2026-10-04T08:29:22Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: `NCBITaxon:1033397`, species, Bacteria,
`EXACT`, `SEEDED`, code 11, four ancestors, zero inventoried strains, one
NCBITAXON NAME attestation and one seed event. The complete designation
BB0608_2216_5.1_4G0 distinguishes this record from neighboring isolates.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_2216_5_1_4g0.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_2216_5_1_4g0.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Complete backbone, lineage, synonym, attestation, scope and seed-event comparisons passed. Exact type-material, merged-ID and dropped scans returned no target rows; direct children: zero.
- Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global term/reference checks, provenance/history/product gates and rendering. Focused comparisons are not substitutes for those gates.

## Identity and Grounding

Backbone row 221031 and scientific-name row 30339 in
`data/catalog/ncbi_names-0005.jsonl.gz` match the YAML. Live NCBI
[EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033397&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033397)
confirm identity, species rank and parent 49928; EFetch confirms code 11.
The root-first chain matches root (1), cellular organisms (131567), Bacteria
(2) and unclassified Bacteria (49928). Species rank does not imply valid
nomenclatural publication or a finer taxonomic placement.

## Evidence

Exact Nuccore search returned one entry, [JF750260.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750260.1),
UID 333384607, a 533-base partial 16S rRNA gene. Its source explicitly names
strain BB0608_2216_5.1_4G0 and taxon 1033397, coastal marine sediment,
Australia: Gulf of Carpentaria, and June 2008 collection. It supplies a
strain qualifier, not a clone or environmental-sample qualifier. This locus
is not a genome, collection deposit or independent taxonomic classification.

Both references were inspected: Cornall, Beyer, Streten-Joyce, McGuinness,
Parry and Gibb's marine-sediment cryopreservation study marked unpublished,
and Cornall's direct submission dated 2011-04-01. Neither includes a DOI or
PMID. Full manuscript text was not obtained; no phenotype was inferred from
the title. Exact Assembly search returned zero with a phrase-not-found and
no-items warning. The single NAME attestation and 2026-09-13 snapshot agree
with the pinned inventory; counts do not denote independent studies.

## Completeness

Complete exact-ID scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and
BactoTraits inventories returned no rows. Empty optional slots reflect
checked source coverage; zero inventoried strains does not mean never cultured.

Ignored-inclusive `rg --no-ignore --hidden -n -z` searched the digit-bounded
numeric ID and complete label/stem designation, allowing dots/underscores,
across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`.
All seven matches were inspected: target backbone, scope and scientific name,
two unrelated genome-statistics matches and two unrelated ATB samples.
Recursive structured SOURCE.json searches found no matches. These are
bounded local searches, not universal absence claims.

Full native objects at `data/catalog/ncbi_genbank-0020.jsonl.gz:2805` and
`data/catalog/gtdb_genomes-0012.jsonl.gz:40184` describe GCA_021730225.1,
Candidatus Vesicomyidisocius sp. Agig_15_S12, taxon 2763509, isolate
Agig_15_S12, BioSample SAMN15822718 and BioProject PRJNA641445. Their
1,033,397-base total/ungapped length, also present in scaffold statistics,
caused the numeric match. GTDB GB_GCA_021730225.1 classifies that isolate as
Ruthia sp021730225. Neither that classification nor the unrelated source's
literature was used as target evidence.

ATB sample SAMEA1033397, run ERR084534 and ENA analysis ERZ3068736 is
Staphylococcus aureus. The other ATB match is Streptococcus pneumoniae sample
SAMEA114341799, run ERR12314322, analysis ERZ26374339, whose SeqKit sum
`seqkit.v0.1_DLS_k0_05d5df97475fe4b92267b1033397a843` contains the numeric ID.
SeqKit sum is not a taxonomic identifier or MD5. Both rows have available
FASTAs and passing source filters, but those statuses do not establish
target identity. No target strain/deposit/genome chain was found in these
unrelated hits.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the record and stated checks.

## Recommended Edits

None. Future source-backed corrections belong in maintained inventory inputs
and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope is maintained
at `curation/seed_scope.tsv:321383`. Do not hand-edit generated YAML.

## Follow-up Checks

After an authorized source correction, verify exact strain/deposit identity,
inspect inventory deltas, run `just seed-canary NCBITaxon:1033397 --force`,
both focused validators, `just verify-corpus` and remaining QC gates.
No canary or regeneration was run for this review.

## Additional Notes

Unique path: `data/taxa/PATHS.tsv:13480`. Seed event remains
2026-09-13T17:54:04Z. NCBI's browser page was inaccessible; EFetch and
Datasets succeeded. iModulonDB was not applicable to this taxonomy-only
record. Only this report and the documented validation TSV were written;
YAML, maintained inputs, scope, history, status and GitHub were not changed.
