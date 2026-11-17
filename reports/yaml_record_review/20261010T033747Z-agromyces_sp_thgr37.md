# YAML Record Review: Agromyces sp. THGR37

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/agromyces_sp_thgr37.yaml`
- Started UTC: 2026-10-10T03:34:16Z
- Finished UTC: 2026-10-10T03:37:47Z
- Verdict: pass

## Target

The complete 53-line generated `TaxonRecord` was read. `NCBITaxon:1037485` denotes Agromyces sp. THGR37, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2639701`, genetic code 11, grounding `EXACT` and mapping status `SEEDED`.

The record contains ten ancestors, zero inventoried strains, one NCBITAXON name attestation and one seed event. It asserts no synonym, formal nomenclature, GTDB mapping, culture deposit, genome, phenotype or causal graph. Preserve the exact THGR37 designation, distinct from TGR28 and other similarly named isolates.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/agromyces_sp_thgr37.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/agromyces_sp_thgr37.yaml --out /private/tmp/taxonmech-thgr37-20261010-validation.tsv --workers 1`: one file, zero errors; output reread, header only.
- `python scripts/validate_history.py history`: 17 valid history records, zero invalid links.
- Complete structured comparisons verified identity, genetic code, every ancestor, empty source synonyms, seven source inventories, unique index/scope resolution and the exact seed reason. A full backbone scan found no immediate child. Own type-material, merged-ID and dropped-record inventories had no rows.
- The complete native name row and all three assembly-catalog search hits were inspected. Live NCBI browser, EFetch/Datasets taxonomy, nucleotide search and complete marker annotations were read. Declared and observed marker lengths and its hash were checked.
- The short NCBI browser URL failed through the web reader; the full node URL succeeded. No DOI or PMID is cited by this YAML or its marker submission.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, original source replay, rendering and publication gates. No graph is present for `just validate-products`.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222757` and the [NCBI taxonomy browser](https://ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=1037485&lvl=3&mode=node) agree on the exact scientific name, species rank and genetic code 11. [EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037485&retmode=xml) confirms parent 2639701; [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037485) includes root 1.

The complete root-first chain matches the pinned backbone: root, cellular organisms, Bacteria, Bacillati, Actinomycetota, Actinomycetes, Micrococcales, Microbacteriaceae, Agromyces and unclassified Agromyces. The final grouping node correctly retains `NO_RANK`. No assignment to a formally named species is inferred.

The full native row `data/catalog/ncbi_names-0005.jsonl.gz:32395` is the scientific name with an empty unique-name qualifier. Neither the backbone nor EFetch supplies alternate names. A species-ranked NCBI placeholder and the nucleotide strain qualifier describe different metadata layers, not contradictory ranks. Exact grounding establishes this source identity, not formal nomenclature, type status or a strain-specific Gram-stain or genomic-GC measurement.

## Evidence

The one-NAME NCBITAXON assertion, source label and 2026-09-13 snapshot note agree with the pinned backbone. No additional own source-count inventory row was found.

The nucleotide query returns one record, UID 334361431, [JF799799.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799799.1), a 781-base partial 16S rRNA gene. Its source explicitly links Agromyces sp. THGR37, strain THGR37, `taxon:1037485` and wetland soil. Both rRNA ends are marked partial. Declared and observed sequence lengths agree, with alphabet `acgt`. This is marker-to-taxon evidence, not a genome assembly or culture-deposit accession.

The only sequence reference is a direct submission dated 10-Apr-2011 by Liu, Shao, Li and Sun at Hebei University. It supplies no DOI, PMID, collection country, coordinates or collection date. The institution address and submission date are not collection metadata. Bounded name/accession web searches did not establish a THGR37-specific primary paper; the accession query returned no results. This does not establish publication absence.

Three assembly-catalog matches are rejected numeric-name coincidences:

- `data/catalog/gtdb_genomes-0009.jsonl.gz:47807` describes `RS_GCF_010374855.1`, with NCBI organism Escherichia coli ATCC 11231, NCBI taxon 562, and GTDB species classification `s__Enterobacter flexneri_A`.
- `data/catalog/ncbi_genbank-0009.jsonl.gz:7552` and `data/catalog/ncbi_refseq-0002.jsonl.gz:41289` describe paired assemblies `GCA_010374855.1` and `GCF_010374855.1` of that non-target organism.

The matching field is assembly name `ASM1037485v1`, not its taxon identifier. Preserve the differing source classifications of these off-target rows without treating them as a defect in THGR37. None supports an Agromyces genome, GTDB mapping, ATCC deposit or publication association. Their PMID 32021174 was not treated as a target citation and was not resolved as evidence for this review.

Datasets omits an assembly-count field rather than explicitly returning zero. No target assembly was established from the inspected evidence. Shared genus, submitters or wetland-soil source text does not justify transferring evidence between THGR37 and another isolate.

## Completeness

Ignored-inclusive and compressed-content-inclusive `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, using bounded taxon ID, slug and designation. An expanded search added JF799799. Both returned exactly six lines: own backbone/name/scope and the three unrelated assembly-catalog rows.

Complete source-inventory scans found no own BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row. Five independently enumerated SOURCE.json files were parsed without a target match. Ignored-independent filename scans found exactly this YAML, no prior target report and no target-specific history filename. These absence statements are bounded to the inspected repository surfaces.

The zero strain count describes the represented culture inventory, not the existence or culturability of THGR37. Empty optional nomenclature, mappings, deposits, genomes and graph slots are appropriate without exact source joins. The marker is optional taxon-level context, not a missing required genome field. iModulonDB is not applicable to this taxonomy/name-only assertion.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the checked assertion scope. Identity, lineage, source count and seed audit are supported. The apparent genome matches are non-target catalog entries, not missing links in this YAML.

## Recommended Edits

No generated-record correction is justified. Preserve THGR37, species rank, the complete NCBI lineage, `SEEDED` status and history. Do not add the partial 16S marker as a genome, borrow the off-target ATCC designation, or transfer phenotypes from other Agromyces isolates.

Any separately authorized correction belongs in maintained upstream source evidence and the extraction/seeding inputs consumed by `src/taxonmech/extract.py` and `src/taxonmech/seed.py`, not a direct edit of the generated YAML. Optional marker or citation enrichment needs a supported taxon-level representation rather than an invented strain container.

## Follow-up Checks

For separately authorized enrichment, verify exact THGR37 linkage and preserve JF799799.1's version. Inspect typed taxon fields rather than taxon digits embedded in assembly names. A genuine genome link requires an assembly accession and explicit organism/strain evidence.

After authorized source changes, run the documented seed canary, schema/strict/history checks, full corpus reproduction and QC. Any future primary publication needs a separate claim-level assessment; none was established here.

## Additional Notes

- YAML SHA-256: `266965556c6f05dc6587f38875c942b5e90f672a25bdad5ab7803461c6bf76d3`.
- JF799799.1 lowercase nucleotide-sequence SHA-256: `f3bbf46c5643861979138fd97eee39049eb63eb95ba2e5c240444e89de6ffd20`.
- `data/taxa/PATHS.tsv:15310` and `curation/seed_scope.tsv:322974` uniquely resolve the target. Scope addition is 2026-09-13; the seed event preserves 2026-09-13T17:54:04Z and the exact one-source NCBITAXON reason.
- Read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Only this new report was written for this target. No tracked record, input, schema, history, page, branch, worktree or GitHub state changed. No Eukaryota YAML was opened or review status promoted.
