# YAML Record Review: marine sediment bacterium BB0608_AND_5.2_2S10

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_5_2_2s10.yaml`
- Started UTC: 2026-10-04T14:02:10Z
- Finished UTC: 2026-10-04T14:03:31Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: `NCBITaxon:1033565`, species, Bacteria,
`EXACT`, `SEEDED`, genetic code 11, four ancestors, zero inventoried strains,
one NCBITAXON NAME attestation and one seed event. BB0608_AND_5.2_2S10
distinguishes this record from neighboring AND_5.2 isolates.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_5_2_2s10.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_5_2_2s10.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Full backbone, lineage, synonyms, attestation, scope and seed-text comparisons passed. Exact type-material, merged-ID and dropped scans found no target rows; direct children: zero.
- Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global term/reference checks, provenance/history/product gates and rendering. Bounded comparisons do not replace those gates.

## Identity and Grounding

Backbone row 221199 and scientific-name row 30507 in
`data/catalog/ncbi_names-0005.jsonl.gz` agree with the YAML. Live NCBI
[EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033565&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033565)
confirm identity and species rank; EFetch confirms parent 49928 and code 11.
Root-first lineage matches root (1), cellular organisms (131567), Bacteria
(2) and unclassified Bacteria (49928). Species rank does not establish valid
nomenclatural publication or finer taxonomic placement.

## Evidence

Exact Nuccore search returned one sequence, [JF750114.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750114.1),
UID 333384461, a 350-base partial 16S rRNA gene. Source qualifiers name
strain BB0608_AND_5.2_2S10, taxon 1033565, coastal marine sediment,
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
All twelve matches were inspected: target scope, backbone and scientific
name, two unrelated ATB rows and seven unrelated native assembly rows.
All seven native JSON objects were read in full. Recursive structured
SOURCE.json scans found no matches. These checks do not establish
universal absence.

- ATB row 64921 in `data/catalog/allthebacteria.tsv.xz`: SAMEA1033565, run ERR068179, analysis ERZ3068962; scientific name and both Sylph fields Streptococcus pneumoniae. FASTA available, assembly/Sylph/HQ filters PASS, prior-HQ T. Only the BioSample suffix matches.
- ATB row 1020837: SAMN02345032, run SRR1033565, analysis ERZ25473278; scientific name Salmonella enterica subsp. enterica serovar Meleagridis, earlier Sylph name Salmonella enterica, current Sylph name unknown. FASTA available, assembly filter PASS, prior-HQ T, current Sylph/HQ filters SYLPH_RESULTS_FAIL. Only the run suffix matches.
- BV-BRC `data/bvbrc/bvbrc-0002.jsonl.gz:14917`: genome 1313.8739, Streptococcus pneumoniae A31198a, taxon 1313, explicit assembly GCF_900051615.1, SAMEA1033565, PRJEB2656 and unversioned WGS FIWD00000000.
- GenBank `data/catalog/ncbi_genbank-0056.jsonl.gz:35073` and RefSeq `data/catalog/ncbi_refseq-0009.jsonl.gz:23148`: GCA_900051615.1 and GCF_900051615.1, respectively, both Streptococcus pneumoniae A31198a, taxon/species 1313, SAMEA1033565 and FIWD00000000.1. They explicitly reciprocally pair as identical. GenBank project is PRJEB2656; RefSeq project is PRJNA224116. Both are contig assemblies with 57 contigs and total/ungapped length 2120610.
- GTDB `data/catalog/gtdb_genomes-0016.jsonl.gz:30869`: RS_GCF_900051615.1, explicit GenBank link GCA_900051615.1, Streptococcus pneumoniae A31198a, taxon/species 1313, SAMEA1033565, PRJNA224116 and FIWD00000000.1. The BioSample suffix, not the target taxon, matches in these four BV-BRC/NCBI/GTDB rows. Shared sample alone does not establish equivalence between the NCBI pair and ATB's assembly.
- GenBank `data/catalog/ncbi_genbank-0066.jsonl.gz:37463`: GCA_982812565.1, Candidatus Actinomarinaceae bacterium, taxon/species 2952897, isolate FORT15-1_SAMEA3355530_MAG_00000002, BioSample SAMEA122253682, PRJEB72989 and CEYEUT000000000.1. This metagenome-derived scaffold assembly has 97 contigs, 63 scaffolds and no RefSeq pair. Only total length 1033565 matches; ungapped length is 1030165, a difference of 3400 bases. The sample token embedded in the isolate label is not its BioSample field.
- GenBank `data/catalog/ncbi_genbank-0017.jsonl.gz:6360` and GTDB `data/catalog/gtdb_genomes-0000.jsonl.gz:2252`: GCA_018700535.1 and GB_GCA_018700535.1 with explicit GenBank link, Candidatus Uhrbacteria bacterium, taxon/species 2053634, isolate SI072_bin28, SAMN14915176, PRJNA630981 and JABITQ000000000.1. This metagenome-derived contig assembly has 96 contigs and no RefSeq pair; GTDB classifies it as UM-FILTER-50-9 sp018700535. Only total/ungapped length 1033565 matches. PMID 33504941 on the unrelated GenBank row was not retrieved or used as target evidence.

Exclusions are identity-based. Non-HQ or failed Sylph classification alone
does not make an available FASTA ineligible. None supports a target
strain/deposit/genome chain. Source versions, the unversioned BV-BRC WGS
accession and distinct project fields are preserved.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the record and stated checks.

## Recommended Edits

None. Future corrections belong in maintained source inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope ownership is
`curation/seed_scope.tsv:321551`. Do not hand-edit generated YAML.

## Follow-up Checks

After an authorized correction, verify exact strain/deposit evidence,
inspect inventory deltas, run `just seed-canary NCBITaxon:1033565 --force`,
both focused validators, `just verify-corpus` and remaining QC gates.
No canary or regeneration was run.

## Additional Notes

Unique path: `data/taxa/PATHS.tsv:13648`. Seed event remains
2026-09-13T17:54:04Z. NCBI's browser page was inaccessible; EFetch and
Datasets succeeded. iModulonDB was not applicable to this taxonomy-only
record. Only this report and the documented validation TSV were written;
YAML, maintained inputs, scope, history, status and GitHub were unchanged.

