# YAML Record Review: marine sediment bacterium BB0608_AND_4.2_2S0

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_4_2_2s0.yaml`
- Started UTC: 2026-10-04T13:29:01Z
- Finished UTC: 2026-10-04T13:30:08Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: `NCBITaxon:1033547`, species, Bacteria,
`EXACT`, `SEEDED`, genetic code 11, four ancestors, zero inventoried strains,
one NCBITAXON NAME attestation and one seed event. BB0608_AND_4.2_2S0
distinguishes this record from neighboring AND_4.2 isolates.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_4_2_2s0.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_4_2_2s0.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Full backbone, lineage, synonyms, attestation, scope and seed-text comparisons passed. Exact type-material, merged-ID and dropped scans found no target rows; direct children: zero.
- Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global term/reference checks, provenance/history/product gates and rendering. Bounded comparisons do not replace those gates.

## Identity and Grounding

Backbone row 221181 and scientific-name row 30489 in
`data/catalog/ncbi_names-0005.jsonl.gz` agree with the YAML. Live NCBI
[EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033547&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033547)
confirm identity and species rank; EFetch confirms parent 49928 and code 11.
Root-first lineage matches root (1), cellular organisms (131567), Bacteria
(2) and unclassified Bacteria (49928). Species rank does not establish valid
nomenclatural publication or finer taxonomic placement.

## Evidence

Exact Nuccore search returned one sequence, [JF750092.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750092.1),
UID 333384439, a 578-base partial 16S rRNA gene. Source qualifiers name
strain BB0608_AND_4.2_2S0, taxon 1033547, coastal marine sediment,
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
All eleven matches were inspected: target scope, backbone and scientific
name, plus eight unrelated catalog rows. The six matching native JSON
objects were read in full. Recursive structured SOURCE.json scans found
no matches. These checks do not establish universal absence.

- ATB row 64903 in `data/catalog/allthebacteria.tsv.xz`: SAMEA1033547, runs ERR068261 and ERR085970, analysis ERZ3068943; scientific name and both Sylph fields Streptococcus pneumoniae. Only the BioSample suffix matches.
- ATB row 1013301: SAMN01907448, run SRR1033547, analysis ERZ3639971; scientific name Salmonella enterica subsp. enterica serovar Montevideo, both Sylph names Salmonella enterica. Only the run suffix matches. Both ATB rows have available FASTAs, assembly/Sylph/HQ filters PASS and prior-HQ T.
- BV-BRC `data/bvbrc/bvbrc-0002.jsonl.gz:14979`: genome 1313.8805, Streptococcus pneumoniae B18210a, taxon 1313, explicit assembly GCF_900052895.1, SAMEA1033547, PRJEB2656 and unversioned WGS FIXU00000000.
- GenBank `data/catalog/ncbi_genbank-0056.jsonl.gz:35201` and RefSeq `data/catalog/ncbi_refseq-0009.jsonl.gz:23276`: GCA_900052895.1 and GCF_900052895.1, respectively, both Streptococcus pneumoniae B18210a, taxon/species 1313, SAMEA1033547 and FIXU00000000.1. They explicitly reciprocally pair as identical; this is stronger than a shared BioSample. GenBank project is PRJEB2656; RefSeq project is PRJNA224116. Both are scaffold assemblies with 50 contigs, 49 scaffolds, total length 2151828 and ungapped length 2151795.
- GTDB `data/catalog/gtdb_genomes-0012.jsonl.gz:28208`: RS_GCF_900052895.1, explicit GenBank link GCA_900052895.1, Streptococcus pneumoniae B18210a, taxon/species 1313, SAMEA1033547, PRJNA224116 and FIXU00000000.1. The BioSample suffix, not the target taxon, matches in these four BV-BRC/NCBI/GTDB rows. Shared sample alone does not establish equivalence between their assembly pair and ATB's assembly.
- GTDB `data/catalog/gtdb_genomes-0010.jsonl.gz:32998` and GenBank `data/catalog/ncbi_genbank-0063.jsonl.gz:38633`: GB_GCA_964641555.1 explicitly links GCA_964641555.1, uncultured Candidatus Peribacteria bacterium, taxon/species 2501586, isolate binchicken_co105_396, SAMEA117322964, PRJEB82487 and CAZXKA000000000.1. This metagenome-derived contig assembly has 12 contigs and no RefSeq pair. GTDB places it in DALYDP01 sp964641555. Only total/ungapped length 1033547 matches.

All exclusions are identity-based, not quality-based. None supports a
target strain/deposit/genome chain. Source accession versions, the
unversioned BV-BRC WGS accession and distinct project fields are preserved.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the record and stated checks.

## Recommended Edits

None. Future corrections belong in maintained source inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope ownership is
`curation/seed_scope.tsv:321533`. Do not hand-edit generated YAML.

## Follow-up Checks

After an authorized correction, verify exact strain/deposit evidence,
inspect inventory deltas, run `just seed-canary NCBITaxon:1033547 --force`,
both focused validators, `just verify-corpus` and remaining QC gates.
No canary or regeneration was run.

## Additional Notes

Unique path: `data/taxa/PATHS.tsv:13630`. Seed event remains
2026-09-13T17:54:04Z. NCBI's browser page was inaccessible; EFetch and
Datasets succeeded. iModulonDB was not applicable to this taxonomy-only
record. Only this report and the documented validation TSV were written;
YAML, maintained inputs, scope, history, status and GitHub were unchanged.

