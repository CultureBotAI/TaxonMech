# YAML Record Review: Citrobacter sp. 36-4CPA

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/citrobacter_sp_36_4cpa.yaml`
- Started UTC: 2026-10-07T17:16:22Z
- Finished UTC: 2026-10-07T17:26:23Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1036018`,
Citrobacter sp. 36-4CPA: species rank, bacterial domain, parent
2644389, ten root-first ancestors, genetic code 11, `EXACT`
grounding, `SEEDED` lifecycle, zero inventoried BacDive strains,
one NCBITAXON attestation and one inline seed event.
No synonyms, nomenclature, mappings, strain/genome objects,
literature evidence, phenotype, gene or causal graph are asserted.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/citrobacter_sp_36_4cpa.yaml`: passed, no issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/citrobacter_sp_36_4cpa.yaml --out /private/tmp/c364-strict.tsv`: passed, one file, zero errors; complete header-only diagnostics read.
- Structured backbone, parent-chain, scope, path, attestation and seed-wording checks passed. These are bounded comparisons, not corpus reproduction.
- Live taxonomy XML, Datasets JSON, exact Assembly/Nuccore searches, complete metadata for all three nucleotide results, PubMed abstract/identifiers and BioSample XML read.
- Primary article sections 2.1-2.4 and 3.1-3.2 inspected in the author's uploaded full text. No finding relies solely on a search snippet.
- `just validate-products`: not applicable, no curator-added graph terms. Taxonomic identifiers were checked against NCBI.
- Standalone `just validate-history`: not applicable after ignored-independent target content/path searches. Inline history passed schema, strict and source checks.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just validate-all`, `just provenance-check`, `just render-check`, `just docs-check`, `just vendored-check`, and the test suite.
- Not checked: independent sequence alignment, authenticated culture equivalence, historical conference PDFs or old pAH36-4CPA/IBRB naming equivalence. Current assembly endpoints did not resolve the accession embedded in the RefSeq annotation name; that limitation is preserved below.

## Identity and Grounding

[NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036018&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036018)
confirm active identity, exact scientific name, species rank and bacterial
domain. EFetch confirms parent `NCBITaxon:2644389`, unclassified
Citrobacter, and genetic code 11. The strain-like species-rank label
does not establish a formally named species or type-strain status.

Pinned rows agree at `data/raw/ncbitaxon_taxa.tsv:222256`,
`data/catalog/ncbi_names-0005.jsonl.gz:31769`,
`data/taxa/PATHS.tsv:14754` and `curation/seed_scope.tsv:322513`.
The native scientific name has an empty unique name. Source synonym
columns, live alternate-name fields and retirement are empty.
The snapshot is 2026-09-13.

All ten ancestors agree in order, labels, ranks and parent links:
root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota,
Gammaproteobacteria, Enterobacterales, Enterobacteriaceae, Citrobacter
and unclassified Citrobacter. Parsed inventories contain no target
children, type-material, merged-ID or dropped rows.
Exact grounding is distinct from lifecycle promotion.

## Evidence

The attestation counts one NCBITAXON `NAME`, not isolates or genomes.
Exact-target BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits
inventories contain no rows. With no descendants,
`strain_count: 0` correctly describes the BacDive inventory;
it does not deny the cultured isolate.

Scope and attestation reproduce the inline seed event wording.
The unchanged `src/taxonmech/seed.py::_seed_timestamp` and previously
inspected raw, ATB and StrainInfo manifest timestamps support
2026-09-13T17:54:04Z as extraction time, not review time.

Exact Nuccore query `txid1036018[Organism:noexp]` returns three UIDs:

- `334361385`, [JF812082.1](https://www.ncbi.nlm.nih.gov/nuccore/JF812082.1): a 1,480-nt partial 16S rRNA sequence, strain 36-4CPA, taxon 1036018, Russia: Ufa industrial zone, collected by T.V. Markusheva. Direct submission was 14 April 2011, creation 6 June 2011 and update 5 September 2019. No culture collection, BioSample or BioProject is supplied in this marker's metadata.
- `822874973`, [KM373703.1](https://www.ncbi.nlm.nih.gov/nuccore/KM373703.1): a circular, complete 5,217-nt plasmid pCS36-4CPA from strain 36-4CPA, taxon 1036018, Russia. Created 26 December 2015 and updated 6 April 2020; references include the 19 August 2014 submission and 14 February 2020 protein update. Its BioSample is SAMN14226495.
- `1850497258`, [NZ_KM373703.1](https://www.ncbi.nlm.nih.gov/nuccore/NZ_KM373703.1): RefSeq representation of that plasmid, explicitly identical to KM373703.1, created 7 June 2020 and updated 24 August 2024. It links the same BioSample and project PRJNA224116. It is not a second independent isolate or a complete cellular genome.

Complete references and feature metadata were read, excluding sequence
and protein-translation payloads. GenBank and RefSeq have different
annotation sets; these were not combined into an experimentally
validated mechanism claim.

[BioSample SAMN14226495](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=biosample&id=SAMN14226495&retmode=xml)
is live and explicitly links KM373703.1 to taxon 1036018, strain
36-4CPA and Russia. It was submitted/published on 27 February 2020.
This supports sample provenance, not a BacDive entry, deposited culture,
whole-genome assembly or formal species assignment.

The accession-linked study,
[PMID 29736141](https://pubmed.ncbi.nlm.nih.gov/29736141/),
DOI 10.1016/j.sjbs.2016.02.014, was verified through complete PubMed
metadata and [inspected author-uploaded primary text](https://www.researchgate.net/publication/294577256_Isolation_and_sequence_analysis_of_pCS36-4CPA_a_small_plasmid_from_Citrobacter_sp_36-4CPA).
Sections 2.2 and 3.1 describe the isolate from hydrocarbon-contaminated
soil in the Ufa industrial area and its JF812082 marker. The reported
98.9% and 98.7% similarities to C. farmeri and C. amalonaticus are
comparisons, not species or strain equivalence; the authors assign
the isolate to Citrobacter. Section 3.2 explicitly links the
5,217-bp plasmid to KM373703. These observations agree with the
narrow identity asserted by the YAML. Plasmid predictions and
introductory claims about other Citrobacter organisms were not
transferred to the target as phenotypes.

The RefSeq comment names PGAP annotation
`GCF_009963925.1-RS_2024_08_24`. This accession was followed rather
than ignored after the exact-taxon Assembly search returned zero.
[The accession-specific Datasets report](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCF_009963925.1/dataset_report)
returned an empty object; Assembly ESearch for GCF_009963925.1 returned
zero with phrase-not-found/no-items warnings, as did the exact-taxon
Assembly query. The assembly web page was unavailable through the
browser tool. These results do not establish deletion or absence of
all assemblies. The embedded annotation reference remains unresolved
and cannot justify a verified whole-genome link.

## Completeness

Complete enough for the generated NCBI-only identity assertions.
The marker, plasmid, BioSample and literature provide optional
enrichment, not a requirement to fabricate genome, culture-collection,
named-species, phenotype or graph objects.

Ignored-independent searches used `rg --no-ignore --hidden -n -z -i`
across `data/raw/`, `data/catalog/`, `data/bacdive/`, `data/bvbrc/`,
`data/gold/`, `data/seqcode/`, `data/straininfo/`, `data/atb/`,
`curation/` and `history/`. Taxid, label/strain separator variants,
slug, JF812082, KM373703, GCF_009963925, SAMN14226495, PMID 29736141,
the DOI, pCS36, pAH36 and IBRB-36 variants were covered.

All 43 candidate rows were fully read, with lossless common-field
and value-column grouping for repeated native objects:

- Three describe the target backbone, scope and scientific name.
- Thirty-three pig-metagenome rows comprise 14 BV-BRC, nine GTDB and ten GenBank records. PRJEB52643 samples SAMEA110360180 through SAMEA110360189 create numeric matches. Their taxa are Bacteroidales, Clostridia, Lachnospiraceae, Parabacteroides or Ruminococcus, not this isolate.
- Two rows describe Lactobacillus acidophilus NSL, taxon 1579, GCA_033598375.1, SAMN38110916 and PRJNA1036018. The BioProject number is not a target taxon link.
- One GenBank row describes Campylobacter jejuni PNUSAC014801, taxon 197, GCA_010360185.1, SAMN13740207 and PRJNA239251. Accession digits cause the match.
- One GenBank row describes Streptococcus pneumoniae, taxon 1313, isolate 1036018, GCA_058711285.1, SAMEA120831653 and PRJNA514245. The isolate string is not this taxon's identifier.
- Three additional rows describe bacterium enrichment culture clone PAH36-P4, taxon 1487639, parent 48479. The pAH36 search fragment matches a different organism name.

Five native `SOURCE.json` objects were fully parsed, and history
filenames were independently searched. No additional applicable
local assertion, deposit, strain-genome link or target standalone
history artifact was found in these bounded roots, including
ignored/hidden/compressed files. No global absence is claimed.

Historical pAH36-4CPA/IBRB-36-4CPA conference and dissertation search
results are unverified leads here, not accepted aliases or evidence
of target catabolism/resistance. Resolving their original naming and
material identity is deferred unless such enrichment is requested.
iModulonDB is not applicable: the YAML asserts no gene, regulator,
expression module or transcriptomic dataset. Optional plasmid
annotations do not establish such a dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the YAML's asserted scope. Identity, lineage, omitted
synonyms, source attestation, inventory count and seed provenance are
supported. The unresolved external annotation accession is a bounded
enrichment limitation, not a broken reference in this record, which
does not assert it.

## Recommended Edits

None required. Preserve generated YAML and `mapping_status: SEEDED`.
Future corrections belong to maintained upstream inputs and
`src/taxonmech/extract.py`/`src/taxonmech/seed.py`; scope changes
belong to `curation/seed_scope.tsv`. Do not patch generated YAML/pages
or create a lifecycle/history change from this read-only review.

## Follow-up Checks

Any optional genome enrichment must resolve the GCF annotation
reference and explicitly distinguish an isolated plasmid from a
cellular genome. Culture or historical-alias enrichment requires an
authenticated identity chain; marker similarity is insufficient.
After authorized maintained-input changes, rerun the owning
generator, per-file schema/strict checks and applicable corpus gates.
New standalone history requires `just validate-history`; new
graph terms/evidence require `just validate-products`.

## Additional Notes

Direct PMC full-text access encountered a browser challenge;
Europe PMC access failed. Neither restriction was bypassed.
The inspected primary text came from the author's ResearchGate upload.
Search-engine freshness labels were not treated as publication dates.

The full YAML was reread and remained byte-identical before report
creation. All target-specific reads and retrievals reached terminal
outcomes. Only this new report is added; no record, source, history,
lifecycle, page, GitHub, branch or worktree was changed.
The other session is closed. Eukaryota was not re-reviewed.
