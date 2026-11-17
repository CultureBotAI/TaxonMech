# YAML Record Review: Streptomyces sp. THGR27

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_sp_thgr27.yaml`
- Started UTC: 2026-10-10T05:51:38Z
- Finished UTC: 2026-10-10T05:53:47Z
- Verdict: pass

## Target

Reviewed the complete 54-line generated `TaxonRecord` for `NCBITaxon:1037521`, Streptomyces sp. THGR27. It is a species-ranked bacterial placeholder under unclassified Streptomyces (`NCBITaxon:2593676`), with `EXACT` grounding, `SEEDED` mapping status, genetic code 11, zero inventoried strains, one NCBI name attestation, and one seed event. Generated YAML is read-only; the maintained inputs are the pinned inventories and `curation/seed_scope.tsv`, interpreted by the extractor and seeder.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/streptomyces_sp_thgr27.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/streptomyces_sp_thgr27.yaml --out /private/tmp/taxonmech-thgr27-20261010-validation.tsv --workers 1`: one file, zero errors; output TSV inspected and contains only its header.
- `python scripts/validate_history.py history`: 17 history records valid, zero invalid links.
- Structured comparisons verified the complete source parent chain, synonyms, code, attestation, unique path-index entry, scope reason, and seed-event wording. This is not full corpus reproduction.
- `just validate-products`: not applicable; no curator-added graph nodes or ontology-grounded graph claims.
- Not checked: `just qc`, full-corpus `validate-all`, `verify-corpus`, provenance and vendored gates, test suite, documentation statistics, and rendering. These full-corpus checks were not run for this read-only single-record review. No separate focused term/reference gate is documented; referenced taxon identifiers were checked against the backbone and live NCBI.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222793` exactly matches the record's identifier, name, species rank, parent, code 11, and 2026-09-13 snapshot. Its synonym and retirement fields are empty. The complete root-first chain matches the individual backbone rows: root 1; cellular organisms 131567; Bacteria 2; Bacillati 1783272; Actinomycetota 201174; Actinomycetes 1760; Kitasatosporales 85011; Streptomycetaceae 2062; Streptomyces 1883; unclassified Streptomyces 2593676. Labels and ranks agree, with no inferred reconciliation to another taxonomy.

The live [NCBI taxonomy EFetch record](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037521&retmode=xml), [Datasets taxonomy response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037521), and [Taxonomy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037521) agree with that identity and lineage. EFetch omits root from its displayed ancestry; Datasets includes root, agreeing with the YAML. The species rank and the sequence's THGR27 strain qualifier are compatible: neither establishes a formally named species or a collection deposit. The Datasets response omits an assembly count; omission is not evidence of zero assemblies. Its broad BLAST group label is not a phenotype measurement.

`data/catalog/ncbi_names-0005.jsonl.gz:32431` was read in full and supplies the same scientific name. Exact structured searches found no own type-material, merged-ID, dropped-ID, or child rows. `data/taxa/PATHS.tsv:15346` uniquely resolves the identifier to this file. `curation/seed_scope.tsv:323010` supplies the 2026-09-13 attested scope reason reproduced in the 2026-09-13T17:54:04Z seed event. No human review promotion is asserted or warranted by this report.

## Evidence

The sole attestation is correctly one `NAME` assertion from `NCBITAXON`, not a genome, strain, experiment, or literature count. Structured checks found no own rows in `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv`, or `bactotraits_taxa.tsv`. Thus the empty optional nomenclature, mapping, and strain sections agree with these pinned inventories. A zero strain inventory does not mean that no isolate exists or that the organism is unculturable.

Live NCBI Nucleotide search for `txid1037521[Organism:exp]` returned exactly one UID, `334361429`. Its complete [GenBank annotation, JF799797.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799797.1), explicitly links Streptomyces sp. THGR27, strain THGR27, and `taxon:1037521`. It describes a 761-base partial 16S rRNA gene, incomplete at both ends, from wetland soil, with geographic qualifier `China: Inner Mongolia Hetao`. The source is genomic DNA, but this marker is not a genome assembly. Declared and retrieved lengths agree, using only A/C/G/T; lowercase-sequence SHA-256 is `f11d51b4a75dc490c1ce51ec99734dd33079d30b5d33ece59a1e33341b095618`.

The annotation's single reference is a direct submission by Liu, Shao, Li, and Sun dated 10 April 2011, through Hebei University. It supplies no DOI or PMID, collection date, coordinates, or culture-collection accession. Here the collection locality is explicitly annotated; it is not inferred from the submitter's Baoding address. The submission date is not a sampling date. The marker supports this bounded source context, not a genus-wide habitat claim, metabolic phenotype, or causal mechanism. Optional enrichment is not a missing required representation in the present taxonomy/name record.

The ignored-inclusive catalog search returned 58 lines: the backbone, scope, and own scientific-name rows plus 55 unrelated native rows. All native candidate rows were read completely, using lossless common-field/delta presentation where helpful. Of the 55 unrelated rows, 54 contain BioSamples `SAMN10375210` through `SAMN10375219`: 10 BV-BRC, 10 GenBank, eight current RefSeq, one historical RefSeq, nine GTDB, 10 AllTheBacteria, and six GOLD project rows. They concern Salmonella enterica, Bacillus subtilis, Bacillus velezensis, Priestia endophytica, or Paenibacillus xylanexedens, not THGR27. Different GTDB/Sylph labels on some of these unrelated records do not create a target mapping.

Examples are BV-BRC `135735.35`/`GCA_003833305.1`/`SAMN10375214`, strain FH5, and `1423.660`/`GCA_003833195.1`/`SAMN10375211`, strain BH6. Full AllTheBacteria rows are `data/catalog/allthebacteria.tsv.xz:1506355` through 1506364; GOLD project rows are `data/gold/projects.jsonl.gz:277378` through 277383. The remaining unrelated hit, `data/catalog/ncbi_genbank-0033.jsonl.gz:35305`, is `GCA_036048215.1`, assembly name `PDT001037521.1`, Streptococcus pneumoniae (`taxid 1313`), isolate 401, `SAMN11121237`, `PRJNA514245`. Its PMID 30286803 belongs to that excluded record and is not a THGR27 citation. Digits embedded in these identifiers are not a taxon identity bridge.

## Completeness

Before absence judgments, ran `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` over `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Patterns included `1037521`, the complete label, exact slug, and `THGR[ _-]?27`; a second pass added `JF799797`. Both returned the same 58 lines. Compressed and ignored files were included. No target-linked genome, deposit, supplemental attestation, or history artifact was established on those surfaces; this is not a universal absence claim.

Independently enumerated and fully parsed the five `SOURCE.json` files in BV-BRC, StrainInfo, BacDive, GOLD, and SeqCode, with no target/accession matches. Ignored-independent filename walks found only the exact target YAML and no pre-existing report or target history filename. These walks did not read Eukaryota YAML contents.

Web searches for the quoted organism/designation and `JF799797`, including wetland/soil variants, returned no results. No direct experimental publication was established by those bounded searches; they do not prove that none exists. No search snippet was used as evidence. iModulonDB is not applicable: the record asserts no gene function, regulator, transcriptomic module, phenotype, or stress-response dataset requiring that adapter.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, source count and unit, and seed status are consistent with the inspected source evidence. Unrelated numeric catalog hits are correctly not represented as target genomes or strains. Optional marker-associated habitat and locality metadata do not invalidate this seeded name record.

## Recommended Edits

None required. Do not hand-edit `data/taxa/bacteria/streptomyces_sp_thgr27.yaml`, promote status, or append a curation/history event from this review. Future verified source enrichment belongs in maintained inventories or an explicitly designed curation input; transformation defects belong in `scripts/extract_source_inventory.py` or `scripts/seed_from_sources.py` and their implementation modules. Scope changes belong in `curation/seed_scope.tsv`. Marker evidence must retain strain and provenance scope and remain outside genome counts.

## Follow-up Checks

For future enrichment, independently verify the exact accession/taxon/strain chain and any full culture-deposit identifier before joining a genome. Preserve the explicit geographic qualifier without substituting an institutional address. Re-run focused schema, strict, and history validation after an authorized maintained-input change; use the documented dry run, seed canary, corpus reproduction, and full quality gates before publishing regenerated data. Human approval is separately required for review-status promotion.

## Additional Notes

The web tool could not open the Taxonomy browser. A direct read succeeded and all 74 parsed text lines were inspected, alongside complete live EFetch and Datasets responses. This tool limitation is not a record defect. YAML SHA-256 at review: `b89488e01c7f629385cb949b72ada8dfca97fcdab56ac4f1eb6d9baf9e41ec70`.

Only this new timestamped report was written. No source inventory, generated record, schema, history, site, GitHub state, or Eukaryota record was modified. Existing worktrees were preserved.
