# YAML Record Review: marine sediment bacterium BB0608_AND_9.2_4S0

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_9_2_4s0.yaml`
- Started UTC: 2026-10-04T16:45:29Z
- Finished UTC: 2026-10-04T16:46:37Z
- Verdict: pass

## Target

Read the entire generated TaxonRecord for NCBITaxon:1033637: marine sediment bacterium BB0608_AND_9.2_4S0, rank SPECIES, domain BACTERIA, parent NCBITaxon:49928, genetic code 11. It retains EXACT grounding, SEEDED status, zero inventoried strains, one NCBITAXON NAME attestation and the 2026-09-13T17:54:04Z seed event. This is a report-only review.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_9_2_4s0.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_9_2_4s0.yaml`: one file, zero ERROR rows.
- Ignored-inclusive exact identifier search across `data/taxa` found only this YAML; ignored-inclusive review filename search found no prior report for this stem.
- Complete structured comparisons passed for the backbone ancestry, seven source inventories, PATHS, scope reason, NCBI attestation and seed text. Type-material, merged-ID and dropped inventories were scanned for the exact identifier.
- Not checked: full-corpus `just qc`, `just verify-corpus`, tests, provenance, global term/reference and history/product gates, or rendering. Bounded source checks are not a substitute for corpus reproduction. No curator-added graph nodes or external evidence references occur in this record.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221271` agrees on identity, rank, parent, code and the 2026-09-13 snapshot; synonyms and retirement are empty. All four root-first ancestors agree: root 1 (NO_RANK), cellular organisms 131567 (CELLULAR_ROOT), Bacteria 2 (DOMAIN), unclassified Bacteria 49928 (NO_RANK). The scientific-name object is `data/catalog/ncbi_names-0005.jsonl.gz:30579`. PATHS row 13724 and `curation/seed_scope.tsv:321623` confirm the slug and scope reason.

Live [NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033637&retmode=xml) and [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033637) were read and agree on identity, rank and ancestry. EFetch confirms parent and code; Datasets includes the root omitted from EFetch's displayed lineage. The Taxonomy Browser was inaccessible through the web tool, and structured authority responses supplied the check. Species rank is an NCBI classification, not proof of valid nomenclatural publication or independent sequence-based placement.

## Evidence

The NCBI attestation correctly counts one NAME. Complete source scans found no direct children or exact matches in BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventories, nor in type-material, merged-ID or dropped rows.

Live exact-organism Assembly search returned zero results, including phrase-not-found/no-items warnings. Nuccore returned one result, UID 333384529: [JF750182.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750182.1), a 368 bp partial 16S rRNA sequence. Inspected source qualifiers explicitly name strain BB0608_AND_9.2_4S0, taxon:1033637 and genomic DNA, with coastal marine sediment, Australia: Gulf of Carpentaria and Jun-2008 collection context. The short marker is not an assembly, culture deposit or independent resolution of the organism's finer taxonomy.

Both reference entries were inspected. Cornall, Beyer, Streten-Joyce, McGuinness, Parry and Gibb's bulk-sediment cryopreservation study is marked Unpublished; Cornall's direct submission is dated 2011-04-01. Neither supplies a DOI or PMID. The full study was not obtained, and no phenotype, viability or treatment-response claim is inferred from its title.

## Completeness

Ignored-inclusive compressed-file search covered taxon-number boundaries, label/designation variants and filename slug in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Eight rows matched: three target rows and five unrelated BioSample matches. Recursive structured SOURCE.json search returned no additional match. All four unrelated native JSON objects were read in full:

- `data/bvbrc/bvbrc-0002.jsonl.gz:15052`: genome 1313.8878 explicitly names GCF_900054375.1, Streptococcus pneumoniae A32497 (taxon 1313), SAMEA1033637, PRJEB2656 and unversioned FIXD00000000, with WGS status.
- `data/catalog/ncbi_genbank-0056.jsonl.gz:35349` and `data/catalog/ncbi_refseq-0009.jsonl.gz:23424`: GCA_900054375.1 and GCF_900054375.1 reciprocally report identical partners for A32497. Both are latest Contig assemblies, 31 contigs / 31 scaffolds, total and ungapped length 2018520, SAMEA1033637 and FIXD00000000.1. GenBank's project is PRJEB2656; RefSeq's is PRJNA224116. Neither has a PMID.
- `data/catalog/gtdb_genomes-0004.jsonl.gz:43427`: RS_GCF_900054375.1 explicitly supplies GCA_900054375.1, A32497, SAMEA1033637, PRJNA224116 and FIXD00000000.1. Both classifications are Streptococcus pneumoniae; Malawi/Blood context belongs to that genome. This GTDB object retains 31 contigs but its scaffold count is `none`, unlike the NCBI catalog objects; source metadata are not silently harmonized.
- `data/catalog/allthebacteria.tsv.xz:64993`: SAMEA1033637, ERR068186 and ERZ3069058; scientific name and both Sylph fields are Streptococcus pneumoniae, available FASTA, assembly/Sylph/HQ PASS, prior-HQ T. The native header was checked in this review session. The numeric BioSample suffix is not the taxon ID. A shared sample with the preceding genomes does not establish assembly equivalence, and no target-linked strain/deposit/sample chain is present. SeqKit is not MD5 and the AWS URL is mutable.

No supported omitted target strain, deposit or genome association was found in these bounded sources; worldwide absence is not claimed. Empty optional synonyms, nomenclature, mappings, genomes, literature evidence and mechanisms are appropriate. Zero BacDive strains is an inventory count, not a claim of never having been cultivated. iModulonDB is not applicable to this record without a gene, regulator, expression dataset or mechanism assertion.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The unavailable manuscript and bounded genome query limit interpretation but do not contradict the actual seeded assertions.

## Recommended Edits

None. Do not edit the generated YAML or transfer unrelated BioSample/genome context. Any future evidence-backed correction belongs in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope changes belong in `curation/seed_scope.tsv:321623`.

## Follow-up Checks

For an authorized future correction, establish explicit strain/deposit/sample identity, refresh the owning inventory, run the seed dry-run and `just seed-canary NCBITaxon:1033637 --force`, inspect the output, rerun both focused validators and then `just verify-corpus` / `just qc`. No canary or regeneration was performed here.

## Additional Notes

Review followed the local single-record skill and checklist. No curation/history event, human-reviewed promotion, generated-page change or GitHub mutation was made. Eukaryota coverage was not reopened.
