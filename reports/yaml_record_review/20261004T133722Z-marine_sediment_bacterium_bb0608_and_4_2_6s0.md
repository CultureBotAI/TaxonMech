# YAML Record Review: marine sediment bacterium BB0608_AND_4.2_6S0

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_4_2_6s0.yaml`
- Started UTC: 2026-10-04T13:36:29Z
- Finished UTC: 2026-10-04T13:37:22Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: `NCBITaxon:1033551`, species, Bacteria,
`EXACT`, `SEEDED`, genetic code 11, four ancestors, zero inventoried strains,
one NCBITAXON NAME attestation and one seed event. BB0608_AND_4.2_6S0
distinguishes this record from neighboring AND_4.2 isolates.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_4_2_6s0.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_4_2_6s0.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Full backbone, lineage, synonyms, attestation, scope and seed-text comparisons passed. Exact type-material, merged-ID and dropped scans found no target rows; direct children: zero.
- Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global term/reference checks, provenance/history/product gates and rendering. Bounded comparisons do not replace those gates.

## Identity and Grounding

Backbone row 221185 and scientific-name row 30493 in
`data/catalog/ncbi_names-0005.jsonl.gz` agree with the YAML. Live NCBI
[EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033551&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033551)
confirm identity and species rank; EFetch confirms parent 49928 and code 11.
Root-first lineage matches root (1), cellular organisms (131567), Bacteria
(2) and unclassified Bacteria (49928). Species rank does not establish valid
nomenclatural publication or finer taxonomic placement.

## Evidence

Exact Nuccore search returned one sequence, [JF750096.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750096.1),
UID 333384443, a 445-base partial 16S rRNA gene. Source qualifiers name
strain BB0608_AND_4.2_6S0, taxon 1033551, coastal marine sediment,
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
name, three unrelated ATB rows and one unrelated GenBank row.
Recursive structured SOURCE.json scans found no matches. These checks
do not establish universal absence.

- ATB row 64907 in `data/catalog/allthebacteria.tsv.xz`: SAMEA1033551, run ERR068168, analysis ERZ3068942; scientific name and both Sylph fields Streptococcus pneumoniae. FASTA available, assembly/Sylph/HQ filters PASS, prior-HQ T. Only the BioSample suffix matches.
- ATB row 346558: SAMEA115796729, run ERR13374670, analysis ERZ26372841; scientific and earlier Sylph names Streptococcus pneumoniae, current Sylph name unknown. FASTA available, assembly filter PASS, prior-HQ T, current Sylph/HQ filters SYLPH_RESULTS_FAIL. Only SeqKit signature `seqkit.v0.1_DLS_k0_1033551ad4439197da7785520b16455c` matches; this signature is not MD5.
- ATB row 1013310: SAMN01907457, run SRR1033551, analysis ERZ3639984; scientific name Salmonella enterica subsp. enterica serovar Newport, both Sylph names Salmonella enterica. FASTA available, assembly/Sylph/HQ filters PASS, prior-HQ T. Only the run suffix matches.
- Full native GenBank `data/catalog/ncbi_genbank-0062.jsonl.gz:46128`: GCA_963992005.1, uncultured Puniceicoccaceae bacterium, taxon/species 1101446, isolate SRR5787989_concoct_12, SAMEA115401660, PRJEB45427 and CAXDSJ000000000.1. This contig assembly has 407 contigs and no RefSeq pair; source exclusion reasons include contamination, metagenome derivation, fragmentation and undefined genus. Only total/ungapped length 1033551 matches.

Exclusions are identity-based. Non-HQ or failed Sylph classification alone
does not make an available FASTA ineligible. None supports a target
strain/deposit/genome chain; the unrelated assembly's quality flags do
not change the target record's verdict.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the record and stated checks.

## Recommended Edits

None. Future corrections belong in maintained source inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope ownership is
`curation/seed_scope.tsv:321537`. Do not hand-edit generated YAML.

## Follow-up Checks

After an authorized correction, verify exact strain/deposit evidence,
inspect inventory deltas, run `just seed-canary NCBITaxon:1033551 --force`,
both focused validators, `just verify-corpus` and remaining QC gates.
No canary or regeneration was run.

## Additional Notes

Unique path: `data/taxa/PATHS.tsv:13634`. Seed event remains
2026-09-13T17:54:04Z. NCBI's browser page was inaccessible; EFetch and
Datasets succeeded. iModulonDB was not applicable to this taxonomy-only
record. Only this report and the documented validation TSV were written;
YAML, maintained inputs, scope, history, status and GitHub were unchanged.

