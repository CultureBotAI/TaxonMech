# YAML Record Review: Ectopseudomonas oleovorans MOIL14HWK12

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/ectopseudomonas_oleovorans_moil14hwk12.yaml`
- Started UTC: 2026-10-04T23:54:13Z
- Finished UTC: 2026-10-04T23:59:38Z
- Verdict: needs curation

## Target

Read the entire generated `TaxonRecord`, `NCBITaxon:1033992`,
Ectopseudomonas oleovorans MOIL14HWK12. It asserts STRAIN rank,
BACTERIA domain, parent 301, ten ancestors, EXACT grounding, SEEDED
status, one GTDB mapping, two exact synonyms, one xref, genetic code
11, zero inventoried strains, four source attestations and one seed event.
This review changes no record, input, code, status or history.

## Validation

- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/ectopseudomonas_oleovorans_moil14hwk12.yaml`; no issues.
- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/ectopseudomonas_oleovorans_moil14hwk12.yaml`; one file, zero errors; emits `reports/instance_validation_failures.tsv`.
- Bounded backbone, complete lineage, seven mapped inventories, child inventory, scope, filename and inline seed-event checks passed. Source counts were checked separately below.
- Not run: full-corpus `just verify-corpus`, QC, tests or rendering. `--max-diffs` limits diagnostics, not targets. Bounded checks do not establish byte reproduction or semantic correctness.
- Not applicable: `just validate-products`; no curator graph nodes. Authority and native-source references were checked directly.
- Not run: `just validate-history`; ignored-inclusive filename and compressed-content searches found no target history artifact. The inline seed event was inspected.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:221414`, full native names at
`data/catalog/ncbi_names-0005.jsonl.gz:30757` and 30758,
[NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033992&retmode=xml)
and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033992)
agree on the identifier, label, STRAIN rank, bacterial domain, parent
301 and code 11. The old Pseudomonas oleovorans MOIL14HWK12 label is
an NCBI equivalent name for this exact taxon and is a supported synonym.
All ten ancestor IDs agree: root, cellular organisms, Bacteria,
Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Pseudomonadales,
Pseudomonadaceae, Ectopseudomonas and Ectopseudomonas oleovorans.
Expanded labels/ranks agree where supplied. Complete exact-ID scans of
type-material, merged-ID and dropped-taxon inventories found no rows.

The GTDB species cluster is a classification target, not another exact
identity for the strain. Neighboring MOIL14HWK12:I1 and :I2 are distinct
NCBI taxa 1033993 and 1033994 with separate assemblies and BioSamples;
their shared name prefix and cluster membership do not merge them.

## Evidence

The NCBITAXON one-NAME attestation and September 13 snapshot agree
with the backbone. `data/raw/gold_taxa.tsv:460` supports one ORGANISM;
`data/raw/madin_taxa.tsv:641` supports three TRAIT_ASSERTION entries.
The latter checks an inventory count, not three experimentally verified
phenotypes. Directly mapped BacDive, LPSN, MediaDive and BactoTraits
inventories were empty. A complete backbone child scan was empty, so
zero descendant-inclusive BacDive strains agrees with these inputs.

`data/raw/gtdb_mappings.tsv:1387` carries the closeMatch and count 61;
`data/raw/gtdb_species.tsv:42707` agrees. A full scan of all 19 native
GTDB shards examined 901341 rows, matching the RS232 manifest, and
counted 61 distinct accessions in the exact Chryseomonas oryzihabitans
cluster. They span 15 NCBI taxon IDs. The representative is
RS_GCF_000730625.1, Pseudomonas oryzihabitans NBRC 102199, not this
target. MOIL14HWK12 is the nonrepresentative RS_GCF_000510765.1;
its full native object at `data/catalog/gtdb_genomes-0008.jsonl.gz:2847`
was inspected. Cluster examples include RIT_BL1, AG1002, L19, GM_Psu_1,
GM_Psu_2, RIT411, uncultured genome bins and both suffixed MOIL isolates.
Sixty-one is supported as a source-cluster assembly count, not 61
MOIL14HWK12 genomes or 61 distinct cultured strains. The live GTDB tree
was inaccessible; this finding uses the pinned native snapshot.

Full native assembly rows at `data/catalog/ncbi_genbank-0000.jsonl.gz:16675`
and `data/catalog/ncbi_refseq-0000.jsonl.gz:13842` agree with
[live assembly metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCF_000510765.1/dataset_report).
Exact-taxonomy Assembly search returned one assembly. GCF_000510765.1
and GCA_000510765.1 are both current and explicitly sequence-identical;
no RefSeq exclusion was reported. The scaffold assembly has 19 contigs,
12 scaffolds, 5005894 total bases and 5003883 ungapped bases. It links
to BioSample SAMN02597181 and sequencing BioProject PRJNA79065;
PRJNA224116 is the RefSeq umbrella, not a second isolate project.

The BioSample names the exact strain and rhizosphere/soil environment,
but location, collection date, reference biomaterial and growth conditions
are missing. Its non-type status and source annotations do not supply a
culture deposit or independently curated organism traits. NCBI's ANI
taxonomy check is Inconclusive with a mismatch: its best match is
P. oryzihabitans, but an explicit warning says ANI is not suitable or
reliable for classification in the relevant genus. Preserve that caveat
and the NCBI-carried lineage instead of silently selecting one taxonomy.

After resolving initial nuccore pagination, all 38 exact-taxonomy
sequence summaries were inspected. They comprise a GenBank WGS master,
19 contigs, five multi-contig scaffold records, and 13 RefSeq records
(one master and 12 scaffolds). These are not 38 independent genomes.
The full metadata, reference, comments and source feature of
[AZOB00000000.1](https://www.ncbi.nlm.nih.gov/nuccore/AZOB00000000.1)
confirm MOIL14HWK12, taxon 1033992, PRJNA79065, SAMN02597181 and
JGI project 404622. Its displayed master length 19 represents the
contig inventory, not a 19-base genome. Raw bases and every contig's
gene features were not inspected.

The full BV-BRC object at `data/bvbrc/bvbrc-0000.jsonl.gz:3259`
links PATRIC 1033992.3 to this assembly, project and sample; its
culture-collection field is empty. Inspected GOLD identity fields at
`data/gold/organisms.jsonl.gz:11319`, `data/gold/projects.jsonl.gz:11182`
and `data/gold/analyses.jsonl.gz:16214` establish Go0012839 ->
Gp0012839 -> Ga0025359 -> IMG 2510065058 / GCA_000510765.1.
The analysis lacks a direct organism ID but supplies the explicit project
bridge. The old organism label matches NCBI's equivalent name and exact
taxon ID; its culture-collection field is empty. The
[primary JGI portal](https://genome.jgi.doe.gov/portal/PseoleOIL14HWK12_FD/PseoleOIL14HWK12_FD.info.html)
corroborates the target, sequencing project 404622, analysis project
1378120 and IMG 2510065058. Project and organism IDs remain related
records, not interchangeable genome identifiers.

The inspected publisher text of Gomila et al. (2015),
[Phylogenomics and systematics in Pseudomonas](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2015.00214/full),
DOI 10.3389/fmicb.2015.00214, specifically includes MOIL14HWK12.
Table 1 places it in the P. oryzihabitans group, with P. psychrotolerans
LMG 21977 as its closest type strain at 99.54% MLSA similarity.
The results also identify the MOIL14HWK12/L19 pair as evidence of
inconsistent species assignments. This supports preserving a taxonomic
conflict, not equating an entire species with this isolate. The PMC
reader presented a verification page; accessible publisher source text,
not the blocked page or search snippets, supports this observation.

## Completeness

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searches covered
`data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`,
excluding only `SOURCE.json`. ID, slug and MOIL14HWK12 separator variants
returned 38 contexts, all inspected. SAMEA1033992 belongs to an unrelated
Streptococcus sample. The suffixed isolates retain their own identities.
A second assembly/sample/project/WGS/IMG-identifier search returned 18
contexts, all inspected; longer WGS prefixes containing AZOB were
unrelated substring matches, not the exact target WGS accession.

The secondary search found exact BioSample SAMN02597181 at
`data/catalog/allthebacteria.tsv.xz:1033176`, with run SRR3944182,
META_FAIL and SYLPH_RESULTS_FAIL, and no ENA analysis. Its full TSV
row was inspected. A provided FASTA URL does not override the documented
eligibility filter. No eligible BacDive/StrainInfo deposit bridge was
found within these searches. Do not invent a culture identifier from a
bare strain designation or equate zero BacDive strains with no genome.

The consequential defect is species-to-strain identity promotion.
Optional nomenclature, phenotype and curator graph fields are not
required merely because native genome metadata exist. The YAML asserts
no ATB genome link, so ATB ineligibility is a future-enrichment caveat,
not a second current defect.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

1. Major: GTDB species-cluster membership is promoted to exact strain
   identity. YAML line 43 carries the closeMatch; line 46 introduces
   Chryseomonas oryzihabitans as an EXACT_SYNONYM; line 54 promotes
   the species xref; line 67 repeats the mapping predicate. The complete
   native cluster contains this target and many other isolates/genomes,
   including the two separately registered suffixed MOIL isolates.
   These data cannot support an exact strain synonym. The maintained
   upstream owner is kg-microbe's GTDB mapping transform, ingested by
   `src/taxonmech/extract.py:501`. `src/taxonmech/seed.py:451` treats
   every closeMatch as identity, and line 466 promotes a synonym/xref
   without a rank/scope guard. Fix those owners, not generated YAML.

## Recommended Edits

1. Correct maintained mapping semantics and guard GTDB identity promotion
   by rank/scope. Preserve the strain's classification/membership evidence,
   but remove the generated exact species synonym and identity xref through
   regeneration after the maintained fix. Do not blindly substitute
   broadMatch; first verify predicate direction and the upstream contract.
2. Add a regression in `tests/test_seed.py` for a strain within a
   multi-strain species cluster. Preserve the valid NCBI equivalent name,
   61-genome cluster count, one GOLD organism, three MADIN assertions,
   source units, NCBI-carried lineage and SEEDED status. Retain source
   taxonomy disagreements explicitly rather than choosing a convenient
   replacement species label.

## Follow-up Checks

After an authorized maintained-input change, rerun the exact GTDB cluster
comparison, regression tests, regeneration, focused schema/strict checks,
full `just verify-corpus` and relevant QC gates. Check valid same-scope
species mappings still work and no cluster-wide exact identity propagates
to a strain. Future strain/genome enrichment requires a whole eligible
deposit bridge and must retain the ATB exclusion and NCBI ANI caveat.
No blocker prevents reviewing other records while this issue remains open.

## Additional Notes

`data/taxa/PATHS.tsv:13869` fixes the target path;
`curation/seed_scope.tsv:26085` records scope addition on September 12,
2026. The September 13 seed event, its source list GOLD/GTDB/MADIN/
NCBITAXON and four-source reason agree. Different scope-addition and
seed dates are not an error. Ignored-inclusive searches found no prior
target report or history artifact before this report. iModulonDB is not
applicable: the YAML names no gene, regulator or expression module.
No paid research, outside contact, GitHub mutation, generator run,
record edit or status promotion occurred.
