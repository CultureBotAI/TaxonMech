# YAML Record Review: marine sediment bacterium BB0608_AND_4.2_3G0

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_4_2_3g0.yaml`
- Started UTC: 2026-10-04T13:31:45Z
- Finished UTC: 2026-10-04T13:32:34Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: `NCBITaxon:1033548`, species, Bacteria,
`EXACT`, `SEEDED`, genetic code 11, four ancestors, zero inventoried strains,
one NCBITAXON NAME attestation and one seed event. BB0608_AND_4.2_3G0
distinguishes this record from neighboring AND_4.2 isolates.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_4_2_3g0.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_4_2_3g0.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Full backbone, lineage, synonyms, attestation, scope and seed-text comparisons passed. Exact type-material, merged-ID and dropped scans found no target rows; direct children: zero.
- Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global term/reference checks, provenance/history/product gates and rendering. Bounded comparisons do not replace those gates.

## Identity and Grounding

Backbone row 221182 and scientific-name row 30490 in
`data/catalog/ncbi_names-0005.jsonl.gz` agree with the YAML. Live NCBI
[EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033548&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033548)
confirm identity and species rank; EFetch confirms parent 49928 and code 11.
Root-first lineage matches root (1), cellular organisms (131567), Bacteria
(2) and unclassified Bacteria (49928). Species rank does not establish valid
nomenclatural publication or finer taxonomic placement.

## Evidence

Exact Nuccore search returned one sequence, [JF750093.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750093.1),
UID 333384440, a 286-base partial 16S rRNA gene. Source qualifiers name
strain BB0608_AND_4.2_3G0, taxon 1033548, coastal marine sediment,
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
All nine matches were inspected: target scope, backbone and scientific
name, plus six unrelated catalog rows. The four matching native JSON
objects were read in full. Recursive structured SOURCE.json scans found
no matches. These checks do not establish universal absence.

- ATB row 64904 in `data/catalog/allthebacteria.tsv.xz`: SAMEA1033548, run ERR068177, analysis ERZ3068947; scientific name and both Sylph fields Streptococcus pneumoniae. FASTA available, assembly/Sylph/HQ filters PASS, prior-HQ T. Only the BioSample suffix matches.
- ATB row 1020839: SAMN02345035, run SRR1033548, analysis ERZ4069621; scientific name Salmonella enterica subsp. enterica serovar Newport, both Sylph names Salmonella enterica. FASTA available, assembly/HQ filters META_FAIL, Sylph filter PASS, prior-HQ T. Source comments distinguish passing earlier 661k metadata checks from failing ATB checks. Only the run suffix matches; META_FAIL additionally excludes this row from eligible strain/genome links.
- BV-BRC `data/bvbrc/bvbrc-0002.jsonl.gz:15021`: genome 1313.8847, Streptococcus pneumoniae A31122, taxon 1313, explicit assembly GCF_900053895.1, SAMEA1033548, PRJEB2656 and unversioned WGS FIYR00000000.
- GenBank `data/catalog/ncbi_genbank-0056.jsonl.gz:35301` and RefSeq `data/catalog/ncbi_refseq-0009.jsonl.gz:23376`: GCA_900053895.1 and GCF_900053895.1, respectively, both Streptococcus pneumoniae A31122, taxon/species 1313, SAMEA1033548 and FIYR00000000.1. They explicitly reciprocally pair as identical. GenBank project is PRJEB2656; RefSeq project is PRJNA224116. Both are scaffold assemblies with 65 contigs, 63 scaffolds, total length 2171358 and ungapped length 2171320.
- GTDB `data/catalog/gtdb_genomes-0011.jsonl.gz:48847`: RS_GCF_900053895.1, explicit GenBank link GCA_900053895.1, Streptococcus pneumoniae A31122, taxon/species 1313, SAMEA1033548, PRJNA224116 and FIYR00000000.1. The BioSample suffix, not the target taxon, matches in these four BV-BRC/NCBI/GTDB rows.

None supports a target strain/deposit/genome chain. Shared BioSample alone
does not establish equivalence between the explicit NCBI assembly pair
and ATB's assembly. Versions, the unversioned BV-BRC WGS accession and
distinct project fields are preserved.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the record and stated checks.

## Recommended Edits

None. Future corrections belong in maintained source inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope ownership is
`curation/seed_scope.tsv:321534`. Do not hand-edit generated YAML.

## Follow-up Checks

After an authorized correction, verify exact strain/deposit evidence,
inspect inventory deltas, run `just seed-canary NCBITaxon:1033548 --force`,
both focused validators, `just verify-corpus` and remaining QC gates.
No canary or regeneration was run.

## Additional Notes

Unique path: `data/taxa/PATHS.tsv:13631`. Seed event remains
2026-09-13T17:54:04Z. NCBI's browser page was inaccessible; EFetch and
Datasets succeeded. iModulonDB was not applicable to this taxonomy-only
record. Only this report and the documented validation TSV were written;
YAML, maintained inputs, scope, history, status and GitHub were unchanged.

