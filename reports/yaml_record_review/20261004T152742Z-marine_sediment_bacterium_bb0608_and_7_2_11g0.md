# YAML Record Review: marine sediment bacterium BB0608_AND_7.2_11G0

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_7_2_11g0.yaml`
- Started UTC: 2026-10-04T15:26:46Z
- Finished UTC: 2026-10-04T15:27:42Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: NCBITaxon:1033605, species, Bacteria,
EXACT/SEEDED, code 11, four ancestors, zero inventoried strains, one
NCBITAXON NAME attestation and one seed event. Exact designation
BB0608_AND_7.2_11G0 distinguishes this record from neighboring strains.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_7_2_11g0.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_7_2_11g0.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Complete backbone/ancestor, synonym, attestation, scope and seed-text comparisons passed. Exact type-material, merged-ID and dropped scans found no target rows; direct children: zero.
- Not checked: full-corpus `just verify-corpus`, QC, tests, global term/reference checks, provenance/history/product gates and rendering. Bounded comparisons do not replace these gates.

## Identity and Grounding

Backbone row 221239 and scientific-name row 30547 in
`data/catalog/ncbi_names-0005.jsonl.gz` agree with the YAML. Live
[EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033605&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033605)
confirm name and rank; EFetch confirms parent 49928 and code 11. Root-first
lineage is root (1), cellular organisms (131567), Bacteria (2), unclassified
Bacteria (49928), with matching ranks. Species rank alone does not establish
valid publication or finer placement.

## Evidence

Exact Nuccore search returned [JF750151.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750151.1),
UID 333384498, one 457-base partial 16S rRNA sequence. Inspected qualifiers
identify strain BB0608_AND_7.2_11G0, taxon 1033605, genomic DNA, coastal
marine sediment, Australia: Gulf of Carpentaria and June 2008. The source
uses strain, not clone or environmental sample. This locus is not a genome,
culture deposit or independent classification.

Both references were inspected: the Cornall, Beyer, Streten-Joyce,
McGuinness, Parry and Gibb cryopreservation study is unpublished; Cornall's
direct submission is dated 2011-04-01. Neither supplies DOI/PMID. Full
manuscript text was not obtained and no phenotype was inferred from its
title. Exact Assembly search returned zero with phrase-not-found/no-items
warnings. The one NAME attestation and snapshot 2026-09-13 agree with the
inventory; one name is not one experiment.

## Completeness

Full exact-ID scans found no target rows in BacDive, LPSN, GTDB, GOLD,
MediaDive, Madin or BactoTraits inventories. Empty optional fields are
appropriate; zero inventoried strains does not mean never cultivated.

Ignored-inclusive `rg --no-ignore --hidden -n -z` searched the digit-bounded
ID and full designation with dot/underscore variants, including label/slug
forms, across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`,
`data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and
`history`. All six matches were inspected: target scope/backbone/name,
one ATB row and two native JSON objects, each read in full. Structured
recursive SOURCE.json scans found zero matches. Absence is bounded to
these local searches and exact public queries.

- `data/catalog/allthebacteria.tsv.xz:64961`: SAMEA1033605, ERR068136, ERZ3069012; scientific name and both Sylph fields Streptococcus pneumoniae. FASTA available, assembly/Sylph/HQ PASS, prior-HQ T. Only the sample suffix and AWS URL match.
- `data/catalog/ncbi_genbank-0063.jsonl.gz:27500` and `data/catalog/gtdb_genomes-0014.jsonl.gz:17355`: GCA_964529875.1 and GB_GCA_964529875.1 with an explicit GenBank link; uncultured Candidatus Planktophila sp., taxon/species 878252, isolate ERP107066_co1_437, SAMEA117385981, PRJEB82487 and CAZGXO000000000.1. This metagenome-derived Scaffold assembly has 125 contigs, 106 scaffolds and no RefSeq pair. Only total length 1033605 matches; ungapped length is 1031795, with the 1810-base difference matching GTDB's gap-length field. GTDB assigns Planktophila sp964529875; carried NCBI classification retains Candidatus Planktophila and environmental-sample placement. These classifications concern an unrelated assembly and are preserved, not reconciled.

Exclusions are identity-based, not quality-based. Neither sample suffix
nor assembly length supplies a target strain/deposit/genome chain.
Explicit assembly links and supplied accession versions are retained
without transferring evidence; sample and assembly identities differ.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the record and stated checks.

## Recommended Edits

None. Future fixes belong in maintained source inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope ownership is
`curation/seed_scope.tsv:321591`. Do not hand-edit generated YAML.

## Follow-up Checks

After an authorized fix, verify exact source identity and inventory deltas,
run `just seed-canary NCBITaxon:1033605 --force`, both focused validators,
`just verify-corpus` and remaining QC gates. No canary or regeneration ran.

## Additional Notes

Unique PATHS entry: `data/taxa/PATHS.tsv:13689`. Seed event remains
2026-09-13T17:54:04Z. NCBI browser access failed; EFetch and Datasets
succeeded. iModulonDB is not applicable to this taxonomy-only record.
Only this report and the validation TSV were written; YAML, maintained
inputs, scope, status, history and GitHub were not changed.
