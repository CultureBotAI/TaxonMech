# YAML Record Review: marine sediment bacterium BB0608_AND_6.1_1S0

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_6_1_1s0.yaml`
- Started UTC: 2026-10-04T14:14:47Z
- Finished UTC: 2026-10-04T14:15:50Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: `NCBITaxon:1033570`, species, Bacteria,
`EXACT`, `SEEDED`, genetic code 11, four ancestors, zero inventoried strains,
one NCBITAXON NAME attestation and one seed event. Exact designation
BB0608_AND_6.1_1S0 distinguishes neighboring records.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_6_1_1s0.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_6_1_1s0.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Complete backbone/ancestor, synonym, attestation, scope and seed-text comparisons passed. Exact type-material, merged-ID and dropped scans found no target rows; direct children: zero.
- Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global term/reference checks, provenance/history/product gates and rendering. Bounded comparisons do not replace these gates.

## Identity and Grounding

Backbone row 221204 and scientific-name row 30512 in
`data/catalog/ncbi_names-0005.jsonl.gz` match. Live
[EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033570&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033570)
confirm the exact name and species rank; EFetch confirms parent 49928 and
code 11. Root-first lineage is root (1), cellular organisms (131567),
Bacteria (2), unclassified Bacteria (49928), with matching ranks.
Species rank does not prove valid publication or finer placement.

## Evidence

Exact Nuccore search returned [JF750116.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750116.1),
UID 333384463, one 565-base partial 16S rRNA sequence. Source qualifiers
explicitly identify strain BB0608_AND_6.1_1S0, taxon 1033570, genomic DNA,
coastal marine sediment, Australia: Gulf of Carpentaria and June 2008.
The qualifier is strain, not clone or environmental sample. This locus is
not a genome, deposit or independent classification.

Both sequence references were inspected: the unpublished Cornall, Beyer,
Streten-Joyce, McGuinness, Parry and Gibb cryopreservation study and
Cornall's direct submission dated 2011-04-01. Neither supplies a DOI/PMID;
full manuscript text was not obtained and no phenotype was inferred from
the title. Exact Assembly search returned zero with phrase-not-found and
no-items warnings. The NCBITAXON NAME count and 2026-09-13 snapshot match
the inventory; one name is not one experiment.

## Completeness

Full exact-ID scans found no target entries in BacDive, LPSN, GTDB, GOLD,
MediaDive, Madin or BactoTraits inventories. Optional fields may remain
empty; zero inventoried strains does not establish absence of cultivation.

Ignored-inclusive `rg --no-ignore --hidden -n -z` searched the digit-bounded
ID and full label/stem designation with dot/underscore alternatives across
`data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`.
All eleven matches were inspected: target scope/backbone/scientific name,
two ATB rows and six native objects, each read in full. Recursive structured
SOURCE.json scans found zero matches. These searches do not establish
universal absence.

- `data/catalog/allthebacteria.tsv.xz:64926`: SAMEA1033570, runs ERR068260 and ERR085969, ERZ3068963; scientific name and both Sylph fields Streptococcus pneumoniae. Only the BioSample suffix and its AWS URL match.
- ATB row 1021131: SAMN02345331, SRR1033570, ERZ4070096; scientific name Salmonella enterica subsp. enterica serovar Javiana, both Sylph fields Salmonella enterica. Only the run suffix matches.
- `data/bvbrc/bvbrc-0002.jsonl.gz:15007`: genome 1313.8833, Streptococcus pneumoniae B18107, taxon 1313, explicit GCF_900053645.1, SAMEA1033570, PRJEB2656 and unversioned FIVY00000000.
- GenBank `data/catalog/ncbi_genbank-0056.jsonl.gz:35276` and RefSeq `data/catalog/ncbi_refseq-0009.jsonl.gz:23351`: GCA_900053645.1 and GCF_900053645.1, explicitly reciprocal identical pairs, same B18107 strain, taxon/species 1313, BioSample SAMEA1033570 and versioned WGS FIVY00000000.1. GenBank project PRJEB2656 and RefSeq project PRJNA224116 remain distinct. Both are Contig assemblies with 51 contigs and total/ungapped length 2124610.
- `data/catalog/gtdb_genomes-0007.jsonl.gz:26771`: RS_GCF_900053645.1 explicitly links GCA_900053645.1, with the same strain, taxon, sample, versioned WGS and PRJNA224116. GTDB and carried NCBI classification both name Streptococcus pneumoniae.
- GenBank `data/catalog/ncbi_genbank-0017.jsonl.gz:41173` and GTDB `data/catalog/gtdb_genomes-0007.jsonl.gz:36543`: GCA_019416985.1 and GB_GCA_019416985.1 with an explicit GenBank link; bacterium, taxon/species 1869227, isolate HRGM_Genome_3508, SAMN19225205, PRJNA730993 and DXWF00000000.1. This metagenome-derived Scaffold assembly has 247 contigs, 206 scaffolds and no RefSeq pair. Only ungapped length 1033570 matches; total length is 1034064 and GTDB gap length is 494. GTDB places it in Onthocola_B sp944331865 whereas carried NCBI taxonomy is unclassified bacterium. PMID 34446072 on this unrelated assembly was not retrieved or used as target evidence.

Both ATB rows have available FASTAs, assembly/Sylph/HQ filters PASS and
prior-HQ T. Exclusions are identity-based, not quality-based. Shared
BioSample alone does not establish ATB/NCBI assembly equivalence. Explicit
crosslinks and source accession versions are preserved, but none supplies
a target strain/deposit/genome chain.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the record and stated checks.

## Recommended Edits

None. Future corrections belong in maintained source inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope ownership is
`curation/seed_scope.tsv:321556`. Do not hand-edit generated YAML.

## Follow-up Checks

After an authorized correction, verify exact strain/deposit evidence and
inventory deltas, run `just seed-canary NCBITaxon:1033570 --force`, both
focused validators, `just verify-corpus` and remaining QC gates.
No canary or regeneration was run.

## Additional Notes

Unique path: `data/taxa/PATHS.tsv:13653`. Seed event remains
2026-09-13T17:54:04Z. NCBI's browser page was inaccessible; EFetch and
Datasets succeeded. iModulonDB was not applicable to this taxonomy-only
record. Only this report and the documented validation TSV were written;
YAML, maintained inputs, scope, history, status and GitHub were unchanged.
