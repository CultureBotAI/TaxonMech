# YAML Record Review: Actinomycetales sp. THGR11

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/actinomycetales_sp_thgr11.yaml`
- Started UTC: 2026-10-10T03:24:17Z
- Finished UTC: 2026-10-10T03:26:17Z
- Verdict: pass

## Target

The entire 48-line generated `TaxonRecord` was read. `NCBITaxon:1037482` denotes Actinomycetales sp. THGR11, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:105426`, genetic code 11, grounding `EXACT` and mapping status `SEEDED`.

It carries eight ancestors, zero inventoried strains, one NCBITAXON name attestation and one seed event. No synonym, formal nomenclature, GTDB mapping, culture deposit, genome, phenotype or causal graph is asserted. Although its label begins with an order name, the target is NCBI's species-level placeholder, not the order itself.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/actinomycetales_sp_thgr11.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/actinomycetales_sp_thgr11.yaml --out /private/tmp/taxonmech-thgr11-20261010-validation.tsv --workers 1`: one file, zero errors. The output was reread and is header-only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Complete structured comparisons verified identity, genetic code, every ancestor, empty source synonyms, seven source inventories, unique index/scope resolution and exact seed reason. Full backbone scanning found no immediate child. Own type-material, merged-ID and dropped-record inventories had no rows.
- The full native scientific-name row, direct NCBI EFetch/Datasets taxonomy, nucleotide search and complete marker annotations were inspected. The marker's declared/observed length and sequence hash were checked.
- Both short and full node URLs for the NCBI browser were unavailable through the web reader. Structured taxonomy APIs succeeded. No DOI or PMID is cited by the YAML or the sequence submission.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, original source replay, rendering and publication gates. No graph is present for `just validate-products`.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222754`, [NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037482&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037482) agree on Actinomycetales sp. THGR11, species rank and bacterial placement. EFetch confirms parent 105426 and code 11; Datasets includes root 1.

The complete root-first chain matches the pinned backbone: root, cellular organisms, Bacteria, Bacillati, Actinomycetota, Actinomycetes, Actinomycetales and unclassified Actinomycetales. The phylum, class and order are distinct entries; the final grouping node correctly retains `NO_RANK`. NCBI supplies no intervening family or genus. Their omission is faithful to the authority and must not be repaired by inference.

The target taxon 1037482 is distinct from order taxon 2037 and grouping taxon 105426. Its species rank meets the repository's scope rule; an order-derived label does not make it a prohibited higher-rank record. The full native name row `data/catalog/ncbi_names-0005.jsonl.gz:32392` is the scientific name with an empty unique-name qualifier. No alternate name is provided by the backbone or EFetch.

Exact grounding establishes the NCBI placeholder identity, not a formal binomial, type strain, family assignment or isolate phenotype. Datasets' broad BLAST category is not a strain-specific Gram-stain or genomic-GC measurement.

## Evidence

The NCBITAXON one-NAME assertion, source label and 2026-09-13 snapshot note agree with the pinned backbone. No additional own source-count inventory row was found.

The live nucleotide query returns one record, UID 334361432, [JF799800.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799800.1), a 780-base partial 16S rRNA gene. Its source explicitly names Actinomycetales sp. THGR11, strain THGR11, `taxon:1037482` and wetland soil. Both rRNA ends are marked partial. Declared and observed lengths agree with alphabet `acgt`. This supports marker-to-taxon identity, not a whole genome, culture-collection deposit or experimentally measured biological trait.

The sequence has one direct-submission reference dated 10-Apr-2011, attributed to Liu, Shao, Li and Sun at Hebei University. It provides no PMID or DOI, collection country, coordinates or collection date. The institutional address and submission date must not be substituted for sample collection metadata.

Exact designation and accession web searches did not establish a THGR11-specific primary paper. The NCBI order-tree search lead contains the target but is not an experimental publication. Absence from these bounded search results is not proof that no publication exists.

Datasets omits an assembly-count field rather than explicitly returning zero. No target assembly was established by the inspected sources. The similar THGR13 designation belongs to a different NCBI taxon and sequence; shared submitters and wetland-source wording do not establish equivalence, a common deposit or transferable traits.

## Completeness

Ignored-inclusive, compressed-content-inclusive `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. The initial pattern included bounded taxon ID, slug and designation; an expanded search added JF799800. Both returned exactly three source lines: own backbone, native name and scope.

Complete source-inventory scans found no own BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row. Five independently enumerated SOURCE.json files were parsed without a target match. Ignored-independent filename scans found exactly this YAML, no prior target report and no target-specific history filename. These findings describe the inspected repository surfaces, not global biological absence.

The zero strain count is an inventory count, not a claim that no isolate existed or could be cultured. Empty nomenclature, synonyms, mappings, deposits, genomes and graph slots are appropriate without exact joins. The 16S accession is useful optional taxon-level context, not a missing required genome field. No family/genus fill-in or causal graph is required. iModulonDB is not applicable to this taxonomy/name-only assertion.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the checked scope. NCBI identity, the deliberately sparse lineage, source count and seed audit are supported. The higher-rank-looking name does not imply an identity or scope-rule error.

## Recommended Edits

No generated-record correction is justified. Preserve THGR11, species rank, the authority's lineage, `SEEDED` status and history. Do not convert the record into the Actinomycetales order, assign an unsupported family/genus, add a marker as a genome or borrow evidence from another THGR isolate.

Any future taxonomic correction belongs at NCBI and in the maintained backbone extraction/seeding path. Optional marker, collection or bibliographic enrichment requires supported maintained inputs and a suitable schema representation, not a direct YAML edit or an invented strain entry.

## Follow-up Checks

For separately authorized enrichment, resolve exact THGR11 evidence and retain the JF799800.1 version. A genome claim requires a genuine assembly identifier and explicit organism/strain linkage; a related marker or shared submitting group is insufficient. A primary paper would require its own scope-sensitive review.

For authorized source changes, run the documented seed canary, schema/strict/history checks, full corpus reproduction and QC. Do not infer collection metadata, Gram response or GC content from administrative or broad taxonomic labels.

## Additional Notes

- YAML SHA-256: `acb87fec8cba17731914056e47454dd53ffb062a18ad0f6f83950767ff24323c`.
- JF799800.1 lowercase nucleotide-sequence SHA-256: `35de06efa9aa8ae4d75f6772d38ef7986038b00582c987b561ab05105d3563ed`.
- `data/taxa/PATHS.tsv:15307` and `curation/seed_scope.tsv:322971` uniquely resolve the record. Scope addition is 2026-09-13; the seed event retains 2026-09-13T17:54:04Z and the exact one-source NCBITAXON reason.
- Read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Only this new report was written for this target. No tracked record, input, schema, history, page, branch, worktree or GitHub state changed. No Eukaryota YAML was opened or review status promoted.
