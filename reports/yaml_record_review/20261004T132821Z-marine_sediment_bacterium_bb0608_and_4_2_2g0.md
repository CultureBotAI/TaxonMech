# YAML Record Review: marine sediment bacterium BB0608_AND_4.2_2G0

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_4_2_2g0.yaml`
- Started UTC: 2026-10-04T13:27:26Z
- Finished UTC: 2026-10-04T13:28:21Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: `NCBITaxon:1033546`, species, Bacteria,
`EXACT`, `SEEDED`, genetic code 11, four ancestors, zero inventoried strains,
one NCBITAXON NAME attestation and one seed event. BB0608_AND_4.2_2G0
distinguishes this record from neighboring AND_4.2 isolates.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_4_2_2g0.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_4_2_2g0.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Full backbone, lineage, synonyms, attestation, scope and seed-text comparisons passed. Exact type-material, merged-ID and dropped scans found no target rows; direct children: zero.
- Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global term/reference checks, provenance/history/product gates and rendering. Bounded comparisons do not replace those gates.

## Identity and Grounding

Backbone row 221180 and scientific-name row 30488 in
`data/catalog/ncbi_names-0005.jsonl.gz` agree with the YAML. Live NCBI
[EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033546&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033546)
confirm identity and species rank; EFetch confirms parent 49928 and code 11.
Root-first lineage matches root (1), cellular organisms (131567), Bacteria
(2) and unclassified Bacteria (49928). Species rank does not establish valid
nomenclatural publication or finer taxonomic placement.

## Evidence

Exact Nuccore search returned one sequence, [JF750091.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750091.1),
UID 333384438, a 434-base partial 16S rRNA gene. Source qualifiers name
strain BB0608_AND_4.2_2G0, taxon 1033546, coastal marine sediment,
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
All seven matches were inspected: target scope, backbone and scientific
name, plus three unrelated ATB rows and one unrelated GenBank row.
Recursive structured SOURCE.json scans found no matches. These checks
do not establish universal absence.

- ATB row 64902 in `data/catalog/allthebacteria.tsv.xz`: SAMEA1033546, run ERR064718, analysis ERZ3068945; scientific name and both Sylph fields Streptococcus pneumoniae. Only the BioSample suffix matches.
- ATB row 1021064: SAMN02345262, run SRR1033546, analysis ERZ4069990; scientific name Salmonella enterica subsp. enterica serovar Rissen, both Sylph names Salmonella enterica. Only the run suffix matches.
- ATB row 2808101: SAMN39485433, run SRR27607450, analysis ERZ26706172; scientific name and both Sylph fields Escherichia coli. Only the SeqKit signature `seqkit.v0.1_DLS_k0_da112b0001330c18f8f1033546ab19ec` matches; this signature is not MD5.
- Full native GenBank row 41268 in `data/catalog/ncbi_genbank-0066.jsonl.gz`: GCA_982931575.1, Methylophilaceae bacterium, taxon/species 2030816, isolate KRUG19-1_SAMN06266123_MAG_00000076, BioSample SAMEA122294760, BioProject PRJEB73043, WGS CEYWKK000000000.1. This metagenome-derived scaffold assembly has 98 contigs, 81 scaffolds and no RefSeq pair. Only ungapped length 1033546 matches the query; total length is 1035246, a difference of 1700 bases. The embedded SAMN token in the isolate label is not its BioSample field.

All three ATB rows have available FASTAs, assembly/Sylph/HQ filters PASS
and prior-HQ T. Exclusions are identity-based, not quality-based. None
supports a target strain/deposit/genome chain.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the record and stated checks.

## Recommended Edits

None. Future corrections belong in maintained source inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope ownership is
`curation/seed_scope.tsv:321532`. Do not hand-edit generated YAML.

## Follow-up Checks

After an authorized correction, verify exact strain/deposit evidence,
inspect inventory deltas, run `just seed-canary NCBITaxon:1033546 --force`,
both focused validators, `just verify-corpus` and remaining QC gates.
No canary or regeneration was run.

## Additional Notes

Unique path: `data/taxa/PATHS.tsv:13629`. Seed event remains
2026-09-13T17:54:04Z. NCBI's browser page was inaccessible; EFetch and
Datasets succeeded. iModulonDB was not applicable to this taxonomy-only
record. Only this report and the documented validation TSV were written;
YAML, maintained inputs, scope, history, status and GitHub were unchanged.

