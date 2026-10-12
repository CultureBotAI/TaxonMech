# YAML Record Review: Staphylococcus lugdunensis N920143

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/staphylococcus_lugdunensis_n920143.yaml`
- Started UTC: 2026-10-05T21:07:04Z
- Finished UTC: 2026-10-05T21:11:56Z
- Verdict: needs curation

## Target

The complete 84-line generated `TaxonRecord` was read before judgment. It denotes `NCBITaxon:1034809`, Staphylococcus lugdunensis N920143, rank `STRAIN`, domain `BACTERIA`, parent `NCBITaxon:28035`, grounding `EXACT`, and lifecycle `SEEDED`. It carries ten ancestors, genetic code 11, one GTDB species mapping, three exact synonyms, a GTDB xref, `strain_count: 0`, and NCBI, GTDB, and Madin attestations.

Resolution is unique at `data/taxa/PATHS.tsv:14163`, `curation/seed_scope.tsv:36163`, and `curation/legacy_page_paths.tsv:845`. N920143 is not the species-level taxon or the species type strain N860297 / DSM 4804. Parent/type information below is contextual evidence, not an additional completed review.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/staphylococcus_lugdunensis_n920143.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/staphylococcus_lugdunensis_n920143.yaml --out /private/tmp/sln-strict-20261005.tsv`: exit 0, one file, zero error rows; the TSV was read and contains only its header.
- Structured comparisons checked the complete backbone/ancestor chain, children, seven taxon-level source inventories, pinned path, scope reason, NCBI snapshot note, and seed-event wording. The generated values reproduce those bounded inputs; this does not prove biological correctness or full corpus reproducibility.
- An ignored-inclusive native GTDB scan parsed and counted all unique genome accessions assigned to the exact species, including their NCBI taxon classifications. The target genome and representative genome objects were read in full; this was not a manual review of all 181 genome records.
- Live NCBI Taxonomy EFetch/Datasets, Assembly Datasets, exact-taxid Assembly/Nuccore searches, four nucleotide records' source metadata, and PubMed citation/abstract metadata were inspected.
- Read-only execution of `normalize_culture_identifier('N920143')` returns no culture-deposit join key.
- `just validate-products` is not applicable: the target has no curator-added causal graph. Source identifiers were checked directly; no undocumented single-record reference validator was invented.
- Not run: `just verify-corpus`, `just qc`, full tests, full-corpus strict validation, provenance hashes, full history validation, generated-site drift, documentation statistics, publication-size budget, and vendored synchronization.

## Identity and Grounding

The backbone at `data/raw/ncbitaxon_taxa.tsv:221693` agrees with live [NCBI taxonomy 1034809](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1034809): strain N920143 under species 28035, bacterial domain, genetic code 11. The complete root-first lineage is:

`1 > 131567 > 2 > 1783272 > 1239 > 91061 > 1385 > 90964 > 1279 > 28035`.

All pinned ancestor labels and ranks match the YAML; live Datasets supplies the same ancestor IDs. Older BV-BRC/GTDB NCBI metadata say Bacillales, while the current pinned backbone and live NCBI chain say Caryophanales. GTDB's own hierarchy uses Staphylococcales. These source hierarchies should remain distinct; neither is grounds for rewriting the NCBI lineage by hand.

The two NCBI-derived strain-qualified synonyms agree with live equivalent-name entries and `data/catalog/ncbi_names-0005.jsonl.gz:31094` and line 31095. The scientific-name row is line 31093. The GTDB-derived bare species synonym has broader scope and is finding F1.

The inspected [LPSN species page, record 781202](https://lpsn.dsmz.de/species/staphylococcus-lugdunensis), identifies the species type as N860297 and deposits including DSM 4804, ATCC 43809, and NCTC 12217, not N920143. The complete local row at `data/raw/lpsn_names.tsv:20010` maps to species 28035. Omitting a species-level nomenclature block and type-deposit claims from this strain is appropriate. No target descendants, retired status, exact-target merged-ID entry, or exact-target type-material row was found in the inspected inventories.

## Evidence

`data/raw/gtdb_species.tsv:168235` supplies the species-wide count of 181, and `data/raw/gtdb_mappings.tsv:1400` supplies this target's closeMatch. The independent ignored-inclusive native scan also found 181 unique members of the exact GTDB species. Only one carries NCBI taxon 1034809; 139 carry species taxon 28035, and the remaining 41 carry other taxon IDs.

The full target object at `data/catalog/gtdb_genomes-0001.jsonl.gz:10178` is `RS_GCF_000270465.1`, strain N920143, with GenBank partner GCA_000270465.1 and BioSample SAMEA2272235. It is not the GTDB representative and has no type-material designation. In contrast, the full representative object at `data/catalog/gtdb_genomes-0005.jsonl.gz:24946` is `RS_GCF_050882105.1`, DSM 4804, species taxon 28035, and explicitly type material. Thus species membership is supported, but species/strain equivalence is not. The valid number 181 must not be relabeled as 181 N920143 genomes.

Live [NCBI assembly GCA_000270465.1](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_000270465.1/) and its explicitly paired GCF_000270465.1 are current and name N920143 with exact taxon 1034809. They contain one chromosome of 2,595,888 bases. The full native GenBank and RefSeq rows are `data/catalog/ncbi_genbank-0000.jsonl.gz:5882` and `ncbi_refseq-0000.jsonl.gz:5001`. Both explicitly supply the partner accession and identical sequence comparison.

The exact-taxid search returned one Assembly result and four Nuccore records. Inspected source metadata identifies chromosome FR870271.1 and RefSeq NC_017353.1, both circular and 2,595,888 bases; RefSeq explicitly states its identity to FR870271.1. The two other records, HG782463.1 and HG520602.1, are 362-base tmRNA transcript/gene records, not additional genomes. Their source taxon and primary-sequence references were read; a specialist label containing HKU090 is not used to equate N920143 with another strain.

The complete native BV-BRC object at `data/bvbrc/bvbrc-0000.jsonl.gz:3286` is `1034809.4`, with the same NCBI assembly, chromosome accessions, and BioSample. It supplies only the bare strain designation N920143, not a recognized culture-deposit identifier.

GOLD retains the explicit native chain `Go0011124 > Gp0011124 > Ga0030443`, inspected in full at `data/gold/organisms.jsonl.gz:9771`, `projects.jsonl.gz:9635`, and `analyses.jsonl.gz:20625`. Its analysis names GCA_000270465.1, FR870271, and IMG 651053071. The organism's culture-collection field and project's BioSample field are empty. These are retained native genome candidates, not sufficient deposit-join evidence. The Go/Gp/Ga identifiers are not themselves genome identifiers.

Project spellings remain source-specific: native GenBank/GOLD and live Assembly metadata use PRJEA67127, BV-BRC uses PRJNA67127, and native RefSeq/GTDB metadata use PRJNA224116. No equivalence among those project identifiers is inferred. Live BioSample SAMEA2272235 supplies strain N920143 and SRA sample ERS379681 but no culture_collection attribute.

[The primary genome publication](https://academic.oup.com/femsle/article/322/1/60/599023), DOI 10.1111/j.1574-6968.2011.02339.x / PMID 21682763, explicitly concerns N920143. Publisher metadata/abstract and the PubMed record were read, and both chromosome records cite this paper. Full-text experimental details were not available and are not used for the verdict; no phenotype or functional claim is added.

Madin's five TRAIT_ASSERTIONs match `data/raw/madin_taxa.tsv:654`. They are an upstream assertion count, not five independently reviewed phenotypes. The configured original Madin KGX input was unavailable, so the individual trait assertions could not be independently recounted. NCBI's one NAME assertion, 2026-09-13 snapshot note, and the three-source seed-event wording match their inventories.

## Completeness

Identifier/strain-name and subsequent assembly/chromosome/BioSample/GOLD-ID searches used `rg --no-ignore --hidden -n -z` over `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`, excluding per-file `SOURCE.json` manifests. All 17 initial candidate rows were read in full as decoded native JSON or header-aware TSV. The follow-up identifier search returned seven of those same rows and no additional row.

Within those bounded searches, no target-specific BacDive, StrainInfo, or ATB association was found. The two initial ATB numeric hits were rejected from their full rows: SAMEA1034809 belongs to Streptococcus dysgalactiae subsp. equisimilis, and ERR1034809 belongs to a Mycobacterium tuberculosis sample. Neither is SAMEA2272235. This is not a claim that N920143 has no genome: its complete assembly is directly supported above.

The zero BacDive strain count agrees with the exact-taxid inventory and absence of descendants. The `src/taxonmech/seed.py:483` rule gathers BacDive records filed at the target or descendants, not arbitrary same-species cultures. No eligible deposit-backed row was found to have been dropped by the writer. The parent-species YAML also returned no match for the target, its assembly/sample, or its GOLD/IMG identifiers in an ignored-inclusive search.

The absence of published strain-genome links here remains an enrichment opportunity for a sequenced strain without a demonstrated deposit join. It is not evidence that the established culture matcher should accept a bare alias. A future non-deposit strain-to-genome representation would require an explicit maintained model/importer design and provenance, not copying DSM 4804 links or inventing a BacDive entry.

The native GOLD organism does not automatically require a taxon-level GOLD attestation: that attestation is generated from the separate KGX inventory, which has no exact-target row. Optional definitions, record-level evidence, discussions, phenotypes, and causal graphs are not blanket requirements. iModulonDB is not applicable to the target's claims.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

1. **Major F1: a GTDB species is promoted to exact identity with strain N920143.** Target lines 39-49 retain a species closeMatch and emit the bare species as EXACT_SYNONYM; lines 56-57 expose its identifier as an equivalent xref, and lines 67-72 repeat the relationship in the GTDB attestation. The complete target and representative genome objects, plus the 181-member native census, show that this is membership in a larger species cluster. The source mapping belongs to upstream kg-microbe's GTDB transform, imported by `src/taxonmech/extract.py:501`. The local amplification is the rank-unaware closeMatch identity branch at `src/taxonmech/seed.py:454`. Core NCBI identity remains correct, so this is major rather than a blocker.

## Recommended Edits

1. Correct the maintained upstream GTDB species-to-strain relationship or represent it explicitly as membership rather than identity. Preserve species-cluster metadata at species scope.
2. Add rank-aware protection to `src/taxonmech/seed.py` so this input cannot generate a bare-species exact synonym or equivalent xref on a strain. Preserve both valid NCBI strain synonyms, genetic code 11, and the supplied NCBI lineage. Do not change 181 to one as a substitute for correcting scope.
3. Keep the native NCBI, GTDB, BV-BRC, and GOLD genome evidence available for a separately authorized enrichment design. Any culture-based link still needs an explicit source-supported deposit; do not relax `src/taxonmech/genome_sources.py` into a name matcher.
4. Following an authorized maintained-input/code fix, re-extract and re-seed through the validated writer. Do not hand-edit generated YAML, source snapshots, or pages.

## Follow-up Checks

Extend `tests/test_seed.py` with a strain target receiving a GTDB species closeMatch. Verify that membership cannot produce exact identity, while the parent species retains the valid species-level relationship and 181-member count. Include the distinct DSM 4804 representative so representative status cannot be confused with target identity.

After an authorized fix, run relevant tests, the documented extraction and seed dry runs, `just seed-canary NCBITaxon:1034809`, focused schema/strict validation, corpus reproduction, and full QC. Reinspect the generated target and species context.

For optional genome enrichment, require explicit provenance for any deposit or new non-deposit linkage mechanism. Preserve assembly versions, distinguish chromosome and tmRNA identifiers, keep BioSamples/projects/GOLD records outside genome counts, and verify project aliases at their own authority before merging them.

## Additional Notes

- HEAD remained `b6a6508faca1388b88feb5740b1095e9f64cfdb8` on the existing review branch. Previously read review guidance and ownership documents were checked for working-tree changes and remained unchanged.
- The seed timestamp 2026-09-13T17:54:04Z equals the newest raw/ATB/StrainInfo manifest timestamp. It is not a claim of human review.
- GTDB species/genome web pages were inaccessible. GOLD's analysis page returned an application error. Those database statements above are explicitly based on inspected pinned native metadata, not a claimed current web census.
- The PMC page returned a browser check; the accessible publisher abstract and PubMed metadata were used without bypassing access controls or purchasing anything.
- The configured Madin edge path did not exist, and an ignored-inclusive filename search of the configured kg-microbe checkout found no Madin-named file. No claim is made about every other checkout.
- An ignored-inclusive target search of reports and history found no prior match before creation. This new report does not overwrite an earlier review, append a history event, or promote lifecycle status.
- Only this report was written. No taxon YAML, source inventory, scope, history, generated product, or Eukaryota record was changed. No contacts, provider credits, GitHub mutations, commits, or new worktrees were used.
