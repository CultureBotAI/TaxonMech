# YAML Record Review: Lactobacillales bacterium BCOT-1

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/lactobacillales_bacterium_bcot_1.yaml`
- Started UTC: 2026-10-04T17:28:32Z
- Finished UTC: 2026-10-04T17:29:43Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for NCBITaxon:1033678, Lactobacillales bacterium BCOT-1. It is a species-ranked placeholder in BACTERIA, with `EXACT` grounding, `SEEDED` status, genetic code 11, zero inventoried BacDive strains, one NCBITAXON NAME attestation and a deterministic seed event at 2026-09-13T17:54:04Z. A species-ranked placeholder is not necessarily a formally published species. No generated field was edited.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/lactobacillales_bacterium_bcot_1.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/lactobacillales_bacterium_bcot_1.yaml`: passed, one file and zero errors.
- Ignored-inclusive exact-identifier search across `data/taxa` returned only this YAML; ignored-inclusive report-filename search found no prior report for this stem.
- Structured comparisons matched backbone, full lineage, child scan, seven source inventories, PATHS, scope, source attestation and embedded seed text. Separate type-material, merged-ID and dropped-row checks completed.
- Not run: corpus-wide `just qc`, `just verify-corpus`, tests, provenance, render and documentation gates. Global term/reference and history validation were skipped; this target has no curator-added graph term, literature citation or separate history artifact. Strict validation covered embedded history shape. Focused source comparisons are not a corpus reproduction check.

## Identity and Grounding

The target backbone row is `data/raw/ncbitaxon_taxa.tsv:221288`; the full native name object is `data/catalog/ncbi_names-0005.jsonl.gz:30596`. `data/taxa/PATHS.tsv:13741` pins the identifier/slug and `curation/seed_scope.tsv:321640` records the 2026-09-13 attested-rule inclusion. All agree with the record.

Live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033678&retmode=xml) and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033678) confirm the canonical name, species rank, parent 263855 and code 11. The browser was unavailable, so structured authority responses were inspected. No alternate name was returned. The root-first chain matches: root 1 (NO_RANK), cellular organisms 131567 (CELLULAR_ROOT), Bacteria 2 (DOMAIN), Bacillati 1783272 (KINGDOM), Bacillota 1239 (PHYLUM), Bacilli 91061 (CLASS), Lactobacillales 186826 (ORDER), unclassified Lactobacillales 263855 (NO_RANK). Datasets explicitly includes root 1.

The record denotes BCOT-1, not BCOT-10, BCOT-11 or another similarly prefixed isolate. Its classification remains unresolved below the order in NCBI; a shared study or order does not identify a genus or species.

## Evidence

The NCBITAXON attestation correctly counts one NAME from snapshot 2026-09-13. There are no direct BacDive, LPSN, GTDB mapping, GOLD, MediaDive, Madin or BactoTraits rows and no child taxa in the inspected inventories. Exact type-material, merged-ID and dropped-row scans were empty. Zero strains is therefore the supported BacDive inventory count, not evidence against cultivation.

The exact-taxid Assembly query returned zero hits with no-items/phrase warnings; Nuccore returned one. [HQ616499.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ616499.1), UID 333408579, is a 748-base partial 16S sequence. Inspected source qualifiers identify genomic DNA, BCOT-1, taxon 1033678, Mexico, collection on 2010-02-01 by R. Flores-Magallon and PCR primers. They do not supply an isolation-source qualifier or a culture-collection deposit. Marker identity is not a genome association.

Both sequence references were inspected: an unpublished Cotija-cheese study and a direct submission on 2010-11-10 by Flores-Magallon, Oliva-Hernandez and Narvaez-Zapata from Instituto Politecnico Nacional, Reynosa. The publisher metadata and abstract of [DOI 10.1007/s10068-011-0137-z](https://link.springer.com/article/10.1007/s10068-011-0137-z), inspected earlier in this session, confirm a related 2011 study but do not name BCOT-1 or HQ616499. The full article and institutional thesis were not accessible in those checks. No isolate-level phenotype or finer classification is inferred from that literature lead.

The complete local objects at `data/bvbrc/bvbrc-0002.jsonl.gz:14995`, `data/catalog/ncbi_genbank-0056.jsonl.gz:35243`, `data/catalog/ncbi_refseq-0009.jsonl.gz:23318` and `data/catalog/gtdb_genomes-0014.jsonl.gz:27499` describe Streptococcus pneumoniae A32849, taxon 1313, BioSample SAMEA1033678. They retain BV-BRC 1313.8821, paired GCA_900053315.1/GCF_900053315.1, and GTDB RS_GCF_900053315.1. The GenBank/RefSeq pair is source-declared identical, 2,007,501 bases, 39 contigs/scaffolds; GTDB's missing scaffold count is not converted into zero. Project differences PRJEB2656 versus PRJNA224116 and WGS FIYQ00000000.1 remain source-specific. These objects matched a BioSample suffix, not BCOT-1 identity.

The corresponding ATB row, `data/catalog/allthebacteria.tsv.xz:65039`, supplies SAMEA1033678, ERR068188 and ERZ3069120. Scientific and both Sylph names are Streptococcus pneumoniae; available FASTA and assembly/Sylph/HQ PASS statuses, with prior HQ T, do not supply a BCOT-1 link. The batch-600 archive, SeqKit sum and mutable AWS URL stay with that source sample. A shared BioSample can establish an association among source assertions, not universal assembly equivalence and not equivalence to this target taxon.

A separate complete GenBank object at `data/catalog/ncbi_genbank-0064.jsonl.gz:35813` is GCA_977110225.1, uncultured Clostridia bacterium taxon 244328, isolate ERR2194095_concoct_40, SAMEA120639360, PRJEB82499 and WGS CDSAZL000000000.1. Its 374-contig/scaffold metagenomic assembly matches only through total/ungapped length 1,033,678. It supplies no BCOT-1 relationship.

## Completeness

Ignored-inclusive compressed searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. The bounded taxid and BCOT-1 label/slug/separator patterns returned nine lines: three target rows and six unrelated source objects discussed above. Structured SOURCE.json searches found no matching manifest evidence in those source roots.

No required representation is missing from the checked inventories. Optional nomenclature, mappings, strains, literature evidence, discussions, datasets and causal graphs may remain absent. No supported genome relationship was found in this bounded review; zero exact-taxid Assembly hits do not establish global absence under other identifiers. Similar study labels and matching numerical suffixes cannot transfer strain evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the currently asserted fields. Unavailable full literature limits optional enrichment, not the verified source identity.

## Recommended Edits

None required. Future enrichment must be maintained in the configured upstream source, `scripts/extract_source_inventory.py`, or a tested `src/taxonmech/seed.py` change. Do not patch generated YAML, invent a BacDive identity, add either unrelated assembly, or refine the lineage by inference. Classification changes belong upstream at NCBI.

## Follow-up Checks

Require inspected primary text explicitly connecting BCOT-1 or HQ616499 to any proposed literature assertion. For later maintained-source changes, run the seed dry-run and single-record canary, inspect emitted YAML, then repeat open/strict validation and full reproduction/QC. No seed mutation was performed during this review.

## Additional Notes

iModulonDB was not applicable: no gene, locus, regulator, pathway or expression-module claim is asserted. No paid research, outbound contact, GitHub operation, status promotion or history write occurred. Tracked status was clean at the start; only reports were untracked. Eukaryota was not revisited.
