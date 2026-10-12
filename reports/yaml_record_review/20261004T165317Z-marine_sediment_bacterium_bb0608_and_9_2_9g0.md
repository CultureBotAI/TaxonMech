# YAML Record Review: marine sediment bacterium BB0608_AND_9.2_9G0

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_9_2_9g0.yaml`
- Started UTC: 2026-10-04T16:52:05Z
- Finished UTC: 2026-10-04T16:53:17Z
- Verdict: pass

## Target

The complete generated TaxonRecord for NCBITaxon:1033640 was read: marine sediment bacterium BB0608_AND_9.2_9G0, SPECIES / BACTERIA, parent NCBITaxon:49928, genetic code 11. EXACT grounding, SEEDED status, zero inventoried strains, one NCBITAXON NAME attestation and the 2026-09-13T17:54:04Z seed event remain unchanged.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_9_2_9g0.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_9_2_9g0.yaml`: one file, zero ERROR rows.
- Ignored-inclusive exact identifier search across `data/taxa` resolved one file; ignored-inclusive report filename search found no previous report for this stem.
- Structured comparisons passed for the full backbone lineage, seven source inventories, PATHS, scope, NCBI attestation and seed text. Exact type-material, merged-ID and dropped scans were completed.
- Not checked: full-corpus `just qc`, `just verify-corpus`, tests, provenance, global term/reference and history/product gates, or rendering. Bounded checks are not corpus reproduction. There are no curator-added graph nodes or external record-level evidence references requiring an additional product check.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221274` matches the identity, rank, parent, code and snapshot 2026-09-13; synonym and retirement fields are empty. All four ancestors agree: root 1 (NO_RANK), cellular organisms 131567 (CELLULAR_ROOT), Bacteria 2 (DOMAIN), unclassified Bacteria 49928 (NO_RANK). The native scientific-name object is `data/catalog/ncbi_names-0005.jsonl.gz:30582`. PATHS row 13727 and `curation/seed_scope.tsv:321626` match the slug and scope reason.

Live [NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033640&retmode=xml) and [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033640) were inspected and confirm identity, rank and ancestry. EFetch confirms parent and genetic code; Datasets includes root, which EFetch omits from its displayed lineage. The Taxonomy Browser was inaccessible through the web tool; successful structured authority responses supplied the check. Species rank is NCBI's classification, not evidence of valid publication or an independently resolved finer placement.

## Evidence

The sole NCBI attestation correctly counts one NAME, not a genome. Complete scans found no direct children or exact target matches in BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventories. Type-material, merged-ID and dropped inventories also had no exact target entry.

Live exact-organism Assembly query returned zero results, with phrase-not-found/no-items warnings. Nuccore returned one result, UID 333384532: [JF750185.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750185.1), a 357 bp partial 16S rRNA sequence. Inspected qualifiers explicitly identify strain BB0608_AND_9.2_9G0, taxon:1033640 and genomic DNA, with coastal marine sediment, Australia: Gulf of Carpentaria and Jun-2008 collection context. This short marker is not an assembly or culture-collection accession, nor independent evidence for a finer taxonomic assignment.

Both reference entries were read. Cornall, Beyer, Streten-Joyce, McGuinness, Parry and Gibb's bulk-sediment cryopreservation study is marked Unpublished; Cornall's direct submission is dated 2011-04-01. Neither carries a DOI or PMID. The full manuscript was not obtained; phenotype, viability and treatment-response claims cannot be inferred from its title.

## Completeness

Ignored-inclusive compressed-file search covered taxon-number boundaries, label/designation variants and filename slug across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Six rows matched: three target rows and three unrelated rows below. Recursive structured SOURCE.json inspection found no further match. Both unrelated native genome objects were read in full:

- `data/catalog/ncbi_genbank-0063.jsonl.gz:30030`: GCA_964555185.1 is uncultured Candidatus Saccharibacteria bacterium, taxon/species 179883, isolate SRP179991_co3_31, SAMEA117290169, PRJEB82487, CAZKRD000000000.1. It is latest Scaffold, 11 contigs / 7 scaffolds, total length 1033640 and ungapped length 1033330, with no RefSeq partner or PMID. Only its genome-size value matches the target number.
- `data/catalog/gtdb_genomes-0006.jsonl.gz:36780`: GB_GCA_964555185.1 explicitly retains that GenBank assembly, isolate, sample, project and WGS accession. Its total length is the numeric match. GTDB classifies it as CAZKRD01 sp964555185 within Patescibacteriota; the NCBI classification retains Candidatus Saccharimonadota and the uncultured Saccharibacteria name. Those source classifications are preserved, not reconciled with this target. Its unrelated identity, not metagenomic origin or RefSeq exclusion, is decisive.
- `data/catalog/allthebacteria.tsv.xz:64996`: SAMEA1033640, ERR068212 and ERZ3069062. Using the previously inspected header, scientific name and both Sylph fields are Streptococcus pneumoniae, FASTA is available, assembly/Sylph/HQ filters are PASS and prior-HQ is T. Only a BioSample suffix and its download URL match. No target-linked strain/deposit/sample chain exists in the inspected evidence. Shared sample alone would not prove assembly equivalence; SeqKit is not MD5 and AWS URLs are mutable.

No supported omitted target strain/deposit/genome link was found in these bounded sources; worldwide biological absence is not claimed. Empty optional synonyms, nomenclature, mappings, genomes, literature evidence and mechanisms are appropriate. Zero inventoried BacDive strains does not mean never cultivated. iModulonDB is not applicable because there is no gene, regulator, expression dataset or mechanism claim.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The unavailable manuscript and bounded genome search remain interpretation limits rather than defects in the actual assertions.

## Recommended Edits

None. Do not edit generated YAML or join on genome-size values or BioSample suffixes. Future evidence-backed corrections belong in maintained source inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope ownership is `curation/seed_scope.tsv:321626`.

## Follow-up Checks

For an authorized future correction, verify explicit identity and strain/deposit/sample chains, refresh the owning inventory, run the seed dry-run and `just seed-canary NCBITaxon:1033640 --force`, inspect the resulting YAML, rerun both focused validators and then `just verify-corpus` / `just qc`. No canary or regeneration was performed here.

## Additional Notes

The local review skill and checklist governed this read-only review. No curation/history event, human-reviewed promotion, generated-page change or GitHub mutation was made. Eukaryota coverage was not reopened.
