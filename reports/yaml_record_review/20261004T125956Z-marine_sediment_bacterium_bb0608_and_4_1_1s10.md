# YAML Record Review: marine sediment bacterium BB0608_AND_4.1_1S10

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_4_1_1s10.yaml`
- Started UTC: 2026-10-04T12:58:25Z
- Finished UTC: 2026-10-04T12:59:56Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: `NCBITaxon:1033532`, species, Bacteria,
`EXACT`, `SEEDED`, genetic code 11, four ancestors, zero inventoried strains,
one NCBITAXON NAME attestation and one seed event. The full designation
BB0608_AND_4.1_1S10 distinguishes AND_4.1_1S0 and 1G10. NCBITaxon:1033532
is not the identically numbered BioProject PRJNA1033532.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_4_1_1s10.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_4_1_1s10.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Full backbone, lineage, synonyms, attestation, scope and seed-text comparisons passed. Exact type-material, merged-ID and dropped scans found no target rows; direct children: zero.
- Structured exclusion checks read all 755 full native objects matching PRJNA1033532, confirmed their project fields, different taxon identities and lack of any BB0608 designation. Six complete examples were also inspected directly.
- Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global term/reference checks, provenance/history/product gates and rendering. Bounded comparisons do not replace those gates.

## Identity and Grounding

Backbone row 221166 and scientific-name row 30474 in
`data/catalog/ncbi_names-0005.jsonl.gz` agree with the YAML. Live NCBI
[EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033532&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033532)
confirm identity and species rank; EFetch confirms parent 49928 and code 11.
Root-first lineage matches root (1), cellular organisms (131567), Bacteria
(2) and unclassified Bacteria (49928). Species rank does not establish valid
nomenclatural publication or finer taxonomic placement.

## Evidence

Exact Nuccore search returned one sequence, [JF750089.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750089.1),
UID 333384436, a 518-base partial 16S rRNA gene. Source qualifiers explicitly
name strain BB0608_AND_4.1_1S10, taxon 1033532, coastal marine sediment,
Australia: Gulf of Carpentaria and June 2008 collection. The qualifier is
strain, not clone or environmental sample. This locus is not a genome,
culture deposit or independent taxonomic classification.

Both references were inspected: Cornall, Beyer, Streten-Joyce, McGuinness,
Parry and Gibb's marine-sediment cryopreservation study marked unpublished,
and Cornall's direct submission dated 2011-04-01. Neither supplies a DOI
or PMID. Full manuscript text was not obtained; no phenotype was inferred
from the title. Exact Assembly search returned zero with phrase-not-found
and no-items warnings. The NAME attestation and 2026-09-13 snapshot match
the inventory; the count is not independent experiments.

## Completeness

Complete exact-ID scans found no target rows in BacDive, LPSN, GTDB, GOLD,
MediaDive, Madin or BactoTraits inventories. Empty optional slots reflect
bounded coverage; zero inventoried strains does not mean never cultured.

Ignored-inclusive `rg --no-ignore --hidden -n -z` searched the digit-bounded
numeric ID and complete label/stem designation, allowing dots/underscores,
across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`.
All 760 matches were classified: three target scope/backbone/name rows,
two unrelated ATB rows and 755 project-accession collisions. Recursive
structured SOURCE.json scans found no matches. These checks do not establish
universal absence.

- ATB row 64888 in `data/catalog/allthebacteria.tsv.xz`: SAMEA1033532, run ERR068057, analysis ERZ3068925; scientific name and both Sylph fields are Streptococcus pneumoniae. Only the BioSample suffix matches.
- ATB row 1013299: SAMN01907446, run SRR1033532, analysis ERZ3639976; scientific name is Salmonella enterica subsp. enterica serovar Montevideo and both Sylph fields are Salmonella enterica. Only the run suffix matches.

Both ATB FASTAs are available, assembly/Sylph/HQ filters PASS, prior-HQ T.
Exclusions are identity-based, not quality-based.

The 755 project collisions were exhaustively parsed and checked, not counted
as evidence for this taxon:

| Native source | Rows | Sole matching field | Identity check |
| --- | ---: | --- | --- |
| BV-BRC | 280 | bioproject_accession | 145 other taxon IDs; 280 assembly IDs |
| GTDB | 195 | ncbi_bioproject | 105 other NCBI taxon IDs; all metagenome-derived |
| GenBank | 280 | bioproject | 145 other taxon IDs; all metagenome-derived, Contig level |

All matching field values are PRJNA1033532. Full-object checks found no
BB0608 designation and no target taxon identity. These are source-row
counts, not independent genome counts or a target-strain crosswalk.

Directly inspected examples further establish the exclusion:

- `data/bvbrc/bvbrc-0000.jsonl.gz:10314` and `:18409`: 1099853.208 / GCA_037069145.1 / SAMN38172329, Coprobacter fastidiosus bin.434, and 1150298.2744 / GCA_037067945.1 / SAMN38172380, Fusicatenibacter saccharivorans bin.320. Their source WGS identifiers are unversioned JBAMRD000000000 and JBAMTC000000000; no version was invented.
- `data/catalog/gtdb_genomes-0000.jsonl.gz:8` and `:3951`: GB_GCA_037069995.1, Bacteroides uniformis bin.257, taxon 820, SAMN38172284, JBAMPK000000000.1; and GB_GCA_037071625.1, Alistipes finegoldii bin.598, taxon 214856, SAMN38172243, JBAMNV000000000.1. Their explicit NCBI assembly accessions are GCA_037069995.1 and GCA_037071625.1.
- `data/catalog/ncbi_genbank-0034.jsonl.gz:33743` and `:33744`: GCA_037064665.1, Victivallales bacterium contig_4242.circular, taxon 2212475, SAMN38172502, JBAMXU000000000.1; and GCA_037064675.1, Victivallis sp. bin.327, taxon 2049020, SAMN38172504, JBAMXW000000000.1. These two rows have no RefSeq pair. Their PMID 38014294 was not retrieved or used as target evidence.

Neither shared project membership nor a shared numeric suffix establishes
strain identity, deposit identity or genome equivalence. No target
strain/deposit/genome chain is supported by these unrelated rows.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the record and stated checks.

## Recommended Edits

None. Future corrections belong in maintained source inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope ownership is
`curation/seed_scope.tsv:321518`. Do not hand-edit generated YAML.

## Follow-up Checks

After an authorized correction, verify exact strain/deposit evidence,
inspect inventory deltas, run `just seed-canary NCBITaxon:1033532 --force`,
both focused validators, `just verify-corpus` and remaining QC gates.
No canary or regeneration was run.

## Additional Notes

Unique path: `data/taxa/PATHS.tsv:13615`. Seed event remains
2026-09-13T17:54:04Z. NCBI's browser page was inaccessible; EFetch and
Datasets succeeded. iModulonDB was not applicable to this taxonomy-only
record. Only this report and the documented validation TSV were written;
YAML, maintained inputs, scope, history, status and GitHub were unchanged.
