# YAML Record Review: marine sediment bacterium BB0608_AND_9.2_3S0

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_9_2_3s0.yaml`
- Started UTC: 2026-10-04T16:41:47Z
- Finished UTC: 2026-10-04T16:43:07Z
- Verdict: pass

## Target

The entire generated TaxonRecord for NCBITaxon:1033635 was read. It denotes marine sediment bacterium BB0608_AND_9.2_3S0, SPECIES / BACTERIA, parent NCBITaxon:49928, genetic code 11. EXACT grounding, SEEDED status, zero inventoried strains, one NCBITAXON NAME attestation and the 2026-09-13T17:54:04Z seed event are retained unchanged.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_9_2_3s0.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_9_2_3s0.yaml`: one file, zero ERROR rows.
- Ignored-inclusive exact identifier search in `data/taxa` resolved only this file; ignored-inclusive review filename search found no prior report for its stem.
- Complete structured source comparisons passed for backbone ancestry, seven attestation inventories, PATHS, scope, seed text and the NCBI attestation. Type-material, merged-ID and dropped inventories were also scanned for the exact identifier.
- Not checked: full-corpus `just qc`, `just verify-corpus`, tests, provenance, global term/reference and history/product gates, or rendering. Bounded source checks do not establish corpus reproduction. There are no curator-added graph nodes or external evidence references in this record.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221269` agrees on label, rank, parent, code and snapshot 2026-09-13; synonym and retirement fields are empty. All four ancestors agree with the generated lineage: root 1 (NO_RANK), cellular organisms 131567 (CELLULAR_ROOT), Bacteria 2 (DOMAIN), and unclassified Bacteria 49928 (NO_RANK). The native scientific-name object is `data/catalog/ncbi_names-0005.jsonl.gz:30577`. PATHS row 13722 and `curation/seed_scope.tsv:321621` agree on slug and scope reason.

Live [NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033635&retmode=xml) and [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033635) were inspected and confirm the identity, rank and ancestry. EFetch confirms parent 49928 and code 11; Datasets includes root, omitted from EFetch's displayed lineage. The Taxonomy Browser was inaccessible through the web tool, so successful structured authority responses supplied verification. NCBI species rank is not evidence of valid nomenclatural publication or a finer taxonomic assignment.

## Evidence

The sole source attestation correctly reports one NAME, not one genome. No child taxa or exact matching BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory rows were found. Exact type-material, merged and dropped scans returned no target rows.

The live exact-organism Assembly search returned zero results, including phrase-not-found/no-items warnings. Nuccore returned one result, UID 333384527: [JF750180.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750180.1), a 483 bp partial 16S rRNA sequence. Its inspected source qualifiers explicitly name strain BB0608_AND_9.2_3S0, taxon:1033635 and genomic DNA, with coastal marine sediment, Australia: Gulf of Carpentaria and Jun-2008 context. A marker sequence is neither an assembly nor a culture-collection deposit; its submitted identity does not independently resolve the unclassified placement.

Both reference entries were read. Cornall, Beyer, Streten-Joyce, McGuinness, Parry and Gibb's bulk-sediment cryopreservation study is marked Unpublished; Cornall's direct submission is dated 2011-04-01. Neither entry carries a DOI or PMID. The full manuscript was not obtained, and its title is not used to infer phenotype, viability or treatment-response claims.

## Completeness

Ignored-inclusive compressed-file search covered taxon-number boundaries, designation/label variants and slug in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Eight rows matched: three target rows and five unrelated BioSample matches. Recursive structured SOURCE.json search found no additional match. All four unrelated native JSON objects were read in full:

- `data/bvbrc/bvbrc-0002.jsonl.gz:14821`: genome 1313.8643 explicitly names GCF_900049745.1, Streptococcus pneumoniae A32279 (taxon 1313), SAMEA1033635, PRJEB2656 and unversioned FIXS00000000, with WGS status.
- `data/catalog/ncbi_genbank-0056.jsonl.gz:34887` and `data/catalog/ncbi_refseq-0009.jsonl.gz:22965`: GCA_900049745.1 and GCF_900049745.1 are reciprocally identified as identical assembly partners for A32279, both latest Scaffold, 50 contigs / 49 scaffolds, total length 2099610 and ungapped length 2099536. Both retain SAMEA1033635 and FIXS00000000.1; GenBank's project is PRJEB2656 and RefSeq's is PRJNA224116. Neither supplies a PMID.
- `data/catalog/gtdb_genomes-0007.jsonl.gz:725`: RS_GCF_900049745.1 explicitly retains GCA_900049745.1, A32279, SAMEA1033635, PRJNA224116, FIXS00000000.1 and both source classifications as Streptococcus pneumoniae. Malawi/Blood metadata belong to that genome, not this target.
- `data/catalog/allthebacteria.tsv.xz:64991`: SAMEA1033635, ERR068185 and ERZ3069051; scientific name and both Sylph fields are Streptococcus pneumoniae, FASTA is available, assembly/Sylph/HQ filters are PASS and prior-HQ is T. The header was checked in this review session. Only the numeric BioSample suffix matches the target ID. Sharing a sample with the preceding assemblies does not establish sequence/assembly equivalence, and none provides a target-linked culture/sample chain. SeqKit is not MD5; the AWS URL is mutable.

Thus the inspected sources supply no omitted target strain/deposit/genome association. This is bounded local-source and live-query coverage, not a claim of global biological absence. Empty optional synonyms, nomenclature, mappings, literature evidence and mechanisms are appropriate. Zero BacDive strains does not mean never cultivated. iModulonDB is not applicable: this record asserts no gene, regulator, expression dataset or mechanism.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Partial-marker evidence and the unavailable manuscript limit interpretation but do not contradict the narrow seeded assertions.

## Recommended Edits

None. Preserve the generated YAML. Any future source-backed correction belongs in maintained source inputs, `src/taxonmech/extract.py` or `src/taxonmech/seed.py`; scope ownership is `curation/seed_scope.tsv:321621`. Never join by numeric suffix or transfer habitat metadata from the unrelated A32279 genome.

## Follow-up Checks

For an authorized future correction, verify explicit strain/deposit/sample evidence, refresh the owning inventory, run the seed dry-run and `just seed-canary NCBITaxon:1033635 --force`, inspect the output and rerun both focused validators, `just verify-corpus` and `just qc`. No canary, regeneration or corpus-wide check was run here.

## Additional Notes

The local review skill's read-only boundary takes precedence over curation scaffolding: no curation/history event, status promotion, generated-page change or GitHub mutation was made. Eukaryota was not reopened.
