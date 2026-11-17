# YAML Record Review: Bradyrhizobium sp. TARC 64

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bradyrhizobium_sp_tarc_64.yaml`
- Started UTC: 2026-10-10T02:13:23Z
- Finished UTC: 2026-10-10T02:17:42Z
- Verdict: pass

## Target

The entire 54-line generated `TaxonRecord` was read. `NCBITaxon:103739` denotes Bradyrhizobium sp. TARC 64, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2631580`, genetic code 11, grounding `EXACT` and status `SEEDED`.

The record contains ten ancestors, zero inventoried strains, one NCBITAXON name attestation and one seed event. It makes no nomenclatural, genome, mechanistic or causal-graph assertion.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/bradyrhizobium_sp_tarc_64.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/bradyrhizobium_sp_tarc_64.yaml --out /private/tmp/taxonmech-bradyrhizobium-tarc64-20261010-validation.tsv --workers 1`: one file, zero errors; output reread, header only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured source comparisons verified identity, the complete lineage, genetic code, empty synonym fields, attestation, unique index/scope resolution and exact seed reason. Complete backbone scanning found no immediate child. Own type-material, merged-ID and dropped-record inventories had no matching row.
- Native source candidates, complete relevant TSV rows and three live nucleotide records were inspected. Both linked PubMed abstracts and bibliographic identifiers were read; the articles' full texts were not available through the attempted DOI page reads.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, original-source replay, rendering and publication gates. No graph is present, so the graph ID/label gate `just validate-products` is inapplicable. Focused checks do not establish full-corpus reproduction.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18565`, live [NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103739&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103739) agree on the exact name, rank, parent and genetic code.

Every stored ancestor ID, label and rank agrees with the backbone: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Alphaproteobacteria, Hyphomicrobiales, Nitrobacteraceae, Bradyrhizobium and unclassified Bradyrhizobium. Live taxonomy confirms this chain; EFetch omits root from its lineage structure and Datasets includes root 1. Retain the unclassified `NO_RANK` parent rather than replacing it with the genus.

The complete native name row `data/catalog/ncbi_names-0000.jsonl.gz:38624` identifies the scientific name and has no unique-name qualifier. Live EFetch supplies no alternate names. The strain-labelled name has NCBI species rank, but that is not evidence of a validly published ICNP species name, a type strain, or synonymy with Bradyrhizobium japonicum.

`EXACT` describes grounding to this NCBI identifier. The attestation correctly records one NAME from the 2026-09-13 snapshot; it does not count experimental observations or independent cultured strains.

## Evidence

The live query `txid103739[Organism:exp]` returned three nucleotide records. All three were read with complete annotation metadata and checked for declared/actual length agreement and A/C/G/T sequence alphabets:

| Accession | Length | Supported annotation context |
| --- | --- | --- |
| [AB073141.1](https://www.ncbi.nlm.nih.gov/nuccore/AB073141.1) | 421 bases | TARC 64, Thailand, Glycine max host; nodbox/nodY region with a nodY pseudogene annotation and promoter |
| [AB073135.1](https://www.ncbi.nlm.nih.gov/nuccore/AB073135.1) | 867 bases | TARC 64, Thailand, Glycine max host; partial nodD coding sequence, protein BAB70603.1, translation table 11 |
| [D85404.1](https://www.ncbi.nlm.nih.gov/nuccore/D85404.1) | 264 bases | TARC 64, partial 16S ribosomal RNA; this source block does not specify host or location |

These are partial sequence records, not genomes. In particular, the nodY pseudogene must not be converted into an asserted functional native protein. No assembly-count field was returned in the inspected Datasets taxonomy response; omission is not an explicit zero-assembly result.

The two AB accessions cite [PMID:18449225](https://pubmed.ncbi.nlm.nih.gov/18449225/), DOI `10.1139/w08-021`. Its abstract describes flavonoid-responsive reporter assays across six representatives of three groups, using a plasmid carrying the USDA 110 nodbox/nodY-lacZ construct. The abstract does not name TARC 64. It does not establish a particular TARC 64 response or demonstrate functional endogenous nodY in this strain.

D85404.1 cites [PMID:10528395](https://pubmed.ncbi.nlm.nih.gov/10528395/), DOI `10.1139/w99-061`. The abstract describes Thai soybean-nodulating Bradyrhizobium isolates compared with USDA strains using nifDK RFLP and partial 16S sequences. It does not name TARC 64. Similarity in a partial marker or a study-level group assignment does not justify renaming this taxon or merging it with a named species.

The sequence references and abstracts are bounded review context, not existing YAML citations. No unsupported mechanistic claim is present in the YAML. Optional future enrichment would require strain-specific evidence and preservation of assay and accession scope.

## Completeness

Gitignore-independent, compressed-content-inclusive searches using `rg --no-ignore --hidden -n -z -i` covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, using the bounded taxon ID, label, slug and TARC 64 spelling variants.

The initial search returned 43 lines. Native candidate identity and matching fields and complete relevant TSV rows distinguished the target's backbone, scope and name row from numerical collisions. BacDive 103739 is a Rhodococcus record; CIP 103739 belongs to Bartonella quintana; MGBC103739, CP103739, ASM103739v1 and unrelated deposit/accession numbers are not links to this taxon. No Eukaryota YAML was opened while resolving unrelated source-table hits.

A follow-up accession search returned four ATB checksum matches, not accession links. All seven ATB candidate rows from the two searches were read in full. Their samples/assemblies denote Escherichia coli, Salmonella, Mycobacterium tuberculosis, Neisseria gonorrhoeae or Shigella sonnei-related source classifications, not TARC 64. Numeric or checksum substrings cannot support an organism match.

Complete structured scans found no own-taxonomy BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row. The bounded source search yielded no eligible own culture-deposit or genome join. Five SOURCE.json files were parsed; the metadata hit for BacDive 103739 concerns the unrelated Rhodococcus record. No target-specific history filename was found.

Ignored-independent filename enumeration found exactly one target YAML and no prior target report. Four report names initially matched the numeric ID only because their timestamps contained 103739; an exact-stem search excluded those collisions without opening the unrelated reports.

`strain_count: 0` describes source inventory coverage, not biological absence of a strain or sequence evidence. Optional nomenclature, mappings, deposits, definitions and graphs are appropriately empty. iModulonDB is not applicable to the record's taxonomy/name assertions; the contextual sequence annotations do not create an asserted transcriptomic or regulator claim.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected assertion scope. The record faithfully represents its NCBI source and does not overstate partial sequence evidence, culture identity, formal nomenclature or function.

## Recommended Edits

None required. Leave the generated YAML, seed status and curation history unchanged.

Any future enrichment belongs in maintained source inventories or extraction/harmonization inputs before regeneration, with an authorized schema or seeder change if necessary. Do not hand-edit this generated record, add partial markers as genomes, infer a cultured deposit from an unrelated number, or rename the taxon using a partial-marker similarity.

## Follow-up Checks

For proposed biological enrichment, obtain primary strain-specific evidence and distinguish the heterologous reporter construct from native nodY. Preserve actual accession versions and distinguish an annotation from demonstrated activity.

If maintained inputs change, rerun the documented canary, schema/strict/history checks and full-corpus reproduction/QC gates. No curator change is required merely to retain this supported NCBI-only record.

## Additional Notes

- YAML SHA-256: `bc8f3c254453dc4bf1144c26d117567c44bfd07cc844bbb4c85ada144e5203fe`.
- `data/taxa/PATHS.tsv:15290` and `curation/seed_scope.tsv:144199` uniquely resolve this target. The seed event retains 2026-09-13T17:54:04Z and the exact single-source scope reason.
- Read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Only this new report was added for this target. No record, maintained input, schema, history, page, branch, worktree or GitHub state was changed. No review status was promoted.
