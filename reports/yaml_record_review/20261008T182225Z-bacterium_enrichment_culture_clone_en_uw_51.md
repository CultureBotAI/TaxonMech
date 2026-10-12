# YAML Record Review: bacterium enrichment culture clone En_UW_51

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_51.yaml`
- Started UTC: 2026-10-08T18:18:27Z
- Finished UTC: 2026-10-08T18:22:25Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` was read for `NCBITaxon:1036437`, bacterium enrichment culture clone En_UW_51. It records rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:48479`, code 11, `EXACT` grounding, `SEEDED` mapping status and zero strains. Its only attestation is an NCBITAXON name assertion; its only embedded history event is the 2026-09-13 seed event. No synonyms, nomenclature, mappings, genomes, strains or causal graph are asserted.

The target was resolved independently through an ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history`: one target YAML and no pre-existing report for this stem. The review is read-only apart from this new report.

## Validation

Record validation used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `just validate data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_51.yaml`: passed with no issues.
- `just validate-strict data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_51.yaml --out /private/tmp/uw51-strict.tsv`: passed, one file scanned and zero error rows. The complete TSV was read and contained only its header.
- Structured comparisons against the entire pinned backbone, all ancestors, seven other raw inventories, scope, PATHS, type-material, merged-ID and dropped tables found no contradiction. Exact candidate name/backbone/scope rows were read in full.
- Full nucleotide/protein XML parsing confirmed declared lengths against sequences and exact agreement between the submitted CDS translation and its own protein record. This was an annotation-consistency check, not an independent translation or alignment.

Not checked: `just verify-corpus`, full-corpus schema validation, global provenance and history validation, `just qc`, full tests, vendored-file synchronization, site drift and publication builds. The individual comparisons do not replace corpus reproduction. The embedded seed event was checked manually; no separate target history artifact was found within the stated ignored-inclusive search. No graph nodes are present, so `just validate-products` is not applicable. No undocumented focused gate was substituted for a global check.

## Identity and Grounding

The full [NCBI Taxonomy EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036437&retmode=xml) agrees with the exact identifier, label, species rank, parent and code. Its named lineage is cellular organisms, Bacteria and environmental samples; the [NCBI Datasets response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036437) additionally includes root, confirming ancestor IDs 1, 131567, 2 and 48479. All four YAML labels and ranks agree with pinned ancestor rows.

NCBI's species rank for this environmental clone does not establish a named species, deposited strain or pure culture. `EXACT` refers to the taxonomic identifier match. The record makes no broader biological claim. Live EFetch supplies no other names, and pinned synonym fields are empty. Complete pinned scans found no exact type-material, merged-ID or dropped row and no backbone child for the target.

## Evidence

The inspected local source chain is:

- `data/raw/ncbitaxon_taxa.tsv:222439`: target identity, parent, rank, genetic code, empty synonyms, NCBI attestation and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:31983`: the exact scientific name for this taxon, with an empty unique-name field.
- `data/taxa/PATHS.tsv:14946`: exact identifier and slug.
- `curation/seed_scope.tsv:322686`: admission date and one-source reason, matching the embedded seed-event wording.

The count of one has unit `NAME`, not strain, assembly or experiment. Complete exact-target scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories returned no rows. The absence of represented strains or extra source attestations is consistent with those inputs, not a biological assertion that no strain could exist elsewhere.

An exact non-expanded Nuccore query, `txid1036437[Organism:noexp]`, returned one result, UID 336092418. The full [HQ630175.1 record](https://www.ncbi.nlm.nih.gov/nuccore/HQ630175.1), including sequence and all qualifiers, assigns this 340-base partial `nosZ` CDS to taxon 1036437 and clone En_UW_51. It specifies an anode-biofilm source, environmental-sample status and H2S-supplemented mineral medium. The CDS is partial at both ends, uses codon start 3 and genetic code 11, and links protein AEI00833.1. No strain, collection deposit or geographic qualifier is supplied.

The full [AEI00833.1 protein record](https://www.ncbi.nlm.nih.gov/protein/AEI00833.1) reciprocally references HQ630175.1 and the same taxon/clone. Its 112-residue conceptual translation has a PRK02888/CDD:235082 region through residue 112. Actual sequence lengths equal the declared 340 bases and 112 residues; the submitted translation exactly matches the protein. No non-ACGT DNA symbols or ambiguous amino-acid symbols were found. This supports annotation consistency, not experimentally demonstrated enzyme activity or whole-organism physiology.

Both sequence records cite an unpublished enrichment study and a 17-NOV-2010 direct submission. They supply neither a PMID nor a DOI for that study. Sequence annotation and enrichment conditions cannot establish isolate purity, species assignment, a complete pathway or measured denitrification for this clone.

The [2015 Vilar Sanz dissertation](https://dugi-doc.udg.edu/bitstream/handle/10256/12459/tavs1de1.pdf?sequence=5) lists enrichment-derived nosZ accessions HQ630075-HQ630210 on printed page 54; HQ630175 lies within that range. Printed page 92 cautions that a single DGGE band does not prove purity. Both pages were read completely. An exact accession/clone search across the extractable text of all 164 pages returned no hit; this was not an exhaustive raster or supplement audit. The study context therefore does not supply a clone-specific species identification.

Exact web searches for HQ630175 and AEI00833 returned no results. A clone-label query excluding the already checked NCBI Taxonomy site also returned none. Exact clone/accession finds in the [PLOS article main HTML](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0063460) found no matching text. These bounded results do not establish literature absence or authorize transfer of community-level results.

## Completeness

Complete enough for the supported taxonomy seed. The external gene fragment is not an assembly and is not a required field for this record. Optional synonyms, nomenclature, taxonomy mappings, deposit links, genomes and causal graphs should remain empty without an explicit supporting identity chain.

Ignored-inclusive compressed-content searches used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. The expanded expression covered the taxid, slug, clone-label variants, own accession and protein, unpublished study title and PLOS DOI. Only the backbone, native name and scope rows above matched, and each was read completely. The five source `SOURCE.json` files were separately parsed in full without a target identity match; history filenames were separately searched. Absence claims apply only to these roots and patterns, with ignored files included.

An exact non-expanded Assembly query returned zero and a phrase-not-found warning. It demonstrates no result under that exact taxid query, not universal genome absence. No independent UniProt or pure-isolate linkage was established. iModulonDB was not run: there is no stored gene, regulator or transcriptomics claim and no identified covered strain/dataset. This is not evidence that the database lacks relevant data.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The limited biological characterization of an environmental fragment is not a defect in this correctly grounded taxonomy-only record.

## Recommended Edits

None required. Preserve the generated YAML and its `SEEDED` status. Do not import a sibling clone's accessions, conditions, species assignment or phenotype.

If later authority evidence changes, taxonomy corrections belong first at NCBI and then in the pinned source governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. A demonstrated projection defect belongs in `src/taxonmech/seed.py` with a regression test; scope changes belong in `curation/seed_scope.tsv`. Optional sequence provenance requires supported maintained input and appropriate model/seeder handling, not a hand edit to `data/taxa/`.

## Follow-up Checks

No corrective follow-up is required. Before optional strain, genome or trait enrichment, inspect primary evidence explicitly connecting this exact clone to the asserted entity or experiment. Shared medium, study membership, gene annotation or a similar fragment is insufficient.

For an authorized future input/seeder correction, run the focused regression test, `just seed-canary NCBITaxon:1036437`, inspect the emitted YAML, rerun both record validators and `just verify-corpus`, then use the full publication QC gates. No regeneration was performed for this review.

## Additional Notes

The review followed the local skill, field checklist, ownership guidance and documented validators. Its individual accession and sequence checks were performed for this target, not inferred from numerical neighbors. Before/after YAML SHA-256 was `ad99ebcc1038834f1ab47a424eac42a6aff99f478c3825758ae05a1457957691`.

Only this new review report was written for this target. No source, YAML, history event, status, generated page or GitHub object was changed. Existing worktrees and the fully covered Eukaryota corpus were untouched.
