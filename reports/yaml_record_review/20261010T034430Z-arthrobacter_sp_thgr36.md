# YAML Record Review: Arthrobacter sp. THGR36

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/arthrobacter_sp_thgr36.yaml`
- Started UTC: 2026-10-10T03:42:38Z
- Finished UTC: 2026-10-10T03:44:30Z
- Verdict: pass

## Target

The complete 54-line generated `TaxonRecord` was read. `NCBITaxon:1037487` denotes Arthrobacter sp. THGR36, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:235627`, genetic code 11, grounding `EXACT`, mapping status `SEEDED`.

Its ten ancestors, zero inventoried strains, one NCBITAXON name attestation and one seed event are the assertion scope. No synonym, formal nomenclature, GTDB mapping, culture deposit, genome, phenotype or causal graph is asserted. THGR36 is distinct from THGR17 and other similarly named isolates.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/arthrobacter_sp_thgr36.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/arthrobacter_sp_thgr36.yaml --out /private/tmp/taxonmech-thgr36-20261010-validation.tsv --workers 1`: one file, zero errors; TSV reread, header only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons verified identity, genetic code, every ancestor, empty source synonyms, seven source inventories, unique index/scope resolution and the exact seed reason. No immediate child or own type-material, merged-ID or dropped-record row was found.
- Complete native name and four assembly-catalog hits were read. Live NCBI EFetch/Datasets taxonomy, nucleotide search and complete marker annotations were inspected; marker length and sequence hash were checked.
- Not available: short and full-node NCBI taxonomy browser URLs both failed through the web reader. Both structured taxonomy endpoints succeeded. No DOI or PMID is cited by this record or its sequence submission.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, original source replay, rendering and publication gates. No graph is present for `just validate-products`.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222759` agrees with [NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037487&retmode=xml) on name, species rank, parent 235627 and genetic code 11. [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037487) confirms the lineage including root 1.

The root-first chain is root, cellular organisms, Bacteria, Bacillati, Actinomycetota, Actinomycetes, Micrococcales, Micrococcaceae, Arthrobacter and unclassified Arthrobacter. Every identifier, label and rank matches the pinned backbone, including the final `NO_RANK` grouping. No named-species assignment is inferred.

`data/catalog/ncbi_names-0005.jsonl.gz:32397` is the exact scientific name with an empty unique-name qualifier. Neither backbone nor EFetch supplies alternate names. The species-ranked placeholder and sequence strain qualifier describe different layers, not inconsistent ranks. Exact grounding does not establish formal nomenclature, type status or measured phenotype; the broad BLAST category is not a strain-specific Gram-stain or genomic-GC assay.

## Evidence

The one-NAME NCBITAXON attestation and 2026-09-13 snapshot note match the pinned source. No additional own source-count inventory row was found.

The nucleotide query returns one entry, UID 334361433, [JF799801.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799801.1). It is a 772-base partial 16S rRNA sequence with both ends marked partial. Source qualifiers explicitly link Arthrobacter sp. THGR36, strain THGR36, `taxon:1037487` and wetland soil. Declared and observed lengths agree, with alphabet `acgt`. This supports a sequence-to-taxon link, not a genome assembly or culture deposit.

The sole reference is a direct submission dated 10-Apr-2011 by Liu, Shao, Li and Sun at Hebei University. No DOI, PMID, collection country, coordinates or collection date is supplied. Institutional address and submission date are not sampling metadata. Bounded exact-name and accession web searches returned no results, which does not establish publication absence.

Four assembly-catalog hits are off-target:

- `data/catalog/gtdb_genomes-0009.jsonl.gz:10695`, `data/catalog/ncbi_genbank-0009.jsonl.gz:7554` and `data/catalog/ncbi_refseq-0002.jsonl.gz:41291` describe Klebsiella pneumoniae ATCC 4353, taxon 573, paired `GCA_010374875.1`/`GCF_010374875.1` and GTDB `RS_GCF_010374875.1`, classified as `s__Klebsiella pneumoniae`. The matching text is assembly name `ASM1037487v1`.
- `data/catalog/ncbi_genbank-0053.jsonl.gz:19764` describes `GCA_057742735.1`, Candidatus Planktophila sp., taxon 2175601, isolate `ME2009-05-12D11_3300042287_group3_bin67`. Its matching fields are genome size and ungapped genome size, both 1037487, not taxon identity. This is explicitly a metagenome-derived assembly.

None supports a THGR36 genome, GTDB mapping, ATCC deposit or metagenomic origin. The Klebsiella rows' PMID 32021174 was not treated as a target citation and was not resolved for this review. Datasets omits an assembly-count field rather than explicitly returning zero; no target assembly was established from the inspected evidence. Similarity of genus, submission authors or isolation-source wording is not proof that THGR36 and THGR17 are the same isolate.

## Completeness

Ignored-inclusive, compressed-content-inclusive `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, using bounded taxon ID, slug and designation. A second search added JF799801. Both found exactly seven lines: own backbone/name/scope and four unrelated assembly rows.

Full source-inventory scans found no own BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row. Five independently enumerated SOURCE.json files were parsed without a target match. Ignored-independent filename scans found exactly this YAML, no prior target report and no target-specific history filename. Absence claims are bounded to these inspected repository surfaces.

Zero strain count means zero represented culture inventory, not absence of the isolate or proof of unculturability. Empty optional slots are appropriate without exact source joins. The partial marker is optional taxon-level context, not a missing required genome. iModulonDB is not applicable to this taxonomy/name-only assertion.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the checked assertion scope. Identity, lineage, source count and seed audit are supported; every apparent assembly match is a non-target numeric coincidence.

## Recommended Edits

No generated-record correction is justified. Preserve the exact designation, species rank, NCBI chain, `SEEDED` status and history. Do not import off-target culture/assembly associations or repurpose the partial marker as a genome.

Any separately authorized correction belongs in maintained upstream evidence and extraction/seeding inputs consumed by `src/taxonmech/extract.py` and `src/taxonmech/seed.py`, not a direct generated-YAML edit. Optional marker enrichment requires a supported taxon-level representation, not an invented strain container.

## Follow-up Checks

For authorized enrichment, confirm THGR36 linkage and preserve JF799801.1's version. Inspect typed taxon fields, not assembly names or numeric size fields. A genuine genome association requires both an assembly accession and explicit organism/strain evidence.

After authorized source changes, run the documented seed canary, schema/strict/history checks, corpus reproduction and QC. Any future primary paper needs an independent claim-level review. Browser access may be retried; structured authority checks succeeded here.

## Additional Notes

- YAML SHA-256: `65d698a53f49c0327639d01fadffeb5229f77f495ceeb5598f01e43c6bbde783`.
- JF799801.1 lowercase sequence SHA-256: `2cc412f51fe0438a48f75e9751507b909e75319fab98d72dae1c270fe91c2875`.
- `data/taxa/PATHS.tsv:15312` and `curation/seed_scope.tsv:322976` uniquely resolve the target. Scope addition is 2026-09-13; the seed event retains 2026-09-13T17:54:04Z and the exact one-source NCBITAXON reason.
- Read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Only this new report was written for the target. No tracked record, input, schema, history, page, branch, worktree or GitHub state changed. No Eukaryota YAML was opened or review status promoted.
