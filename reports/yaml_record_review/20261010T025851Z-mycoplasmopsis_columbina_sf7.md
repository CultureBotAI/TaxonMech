# YAML Record Review: Mycoplasmopsis columbina SF7

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/mycoplasmopsis_columbina_sf7.yaml`
- Started UTC: 2026-10-10T02:55:40Z
- Finished UTC: 2026-10-10T02:58:51Z
- Verdict: needs curation

## Target

The entire 89-line generated `TaxonRecord` was read. `NCBITaxon:1037410` denotes Mycoplasmopsis columbina SF7, rank `STRAIN`, domain `BACTERIA`, parent `NCBITaxon:114881`, genetic code 4, grounding `EXACT` and mapping status `SEEDED`.

It contains nine ancestors, one GTDB mapping with three genomes, four exact synonyms, a GTDB xref, zero inventoried strains, four source attestations and one seed event. It denotes SF7, not the whole species or the type strain. No individual genome, culture deposit, phenotype or causal graph is asserted in the YAML.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/mycoplasmopsis_columbina_sf7.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/mycoplasmopsis_columbina_sf7.yaml --out /private/tmp/taxonmech-sf7-20261010-validation.tsv --workers 1`: one file, zero errors; output reread, header only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons verified identity, all ancestors, code, NCBI synonyms, own source counts, index/scope resolution and exact seed reason. Complete backbone scanning found no immediate child. Own type-material, merged-ID and dropped-record inventories had no rows.
- Complete own native NCBI names, current/historical assemblies, GTDB genome, BV-BRC and GOLD rows were read. All three exact GTDB species-cluster rows were read in full. Other search candidates were inspected for identity and matching fields.
- Live NCBI EFetch/Datasets taxonomy, assembly reports, PubMed bibliographic metadata/abstract and the LPSN species page were inspected. The taxonomy and GTDB browser pages were unavailable through the web reader. PMC returned a browser-check page, so the full genome paper was not inspected.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, full provenance replay, rendering and publication gates. No graph is present for `just validate-products`. Structural success does not prove species-to-strain mapping correctness.
- An ignored-independent filename search of the configured kg-microbe `data` directory found no GTDB/Madin files or `edges.tsv`. Original transformed edges were unavailable for replay. Committed inventory counts and the native genome/organism evidence were checked; the individual Madin trait was not reconstructed.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222747`, [NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037410&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037410) agree on the strain label and rank. EFetch confirms parent 114881 and code 4. Datasets supplies root 1 and reports one assembly.

The complete root-first lineage agrees with the backbone: root, cellular organisms, Bacteria, Bacillati, Mycoplasmatota, Mycoplasmoidales, Metamycoplasmataceae, Mycoplasmopsis and Mycoplasmopsis columbina. No class is present in the NCBI chain. Do not insert Mollicutes merely because LPSN uses it, or replace the lineage with GTDB's Bacillota_I/Bacilli_A/Mycoplasmatales classification. These source-specific classification differences are not an error in the faithful NCBI lineage.

Native rows `data/catalog/ncbi_names-0005.jsonl.gz:32380` through `:32383` and EFetch support both Mycoplasma columbinum strain-qualified equivalent names and the synonym Mycoplasmopsis columbinum SF7. All three retain SF7 and refer to the same NCBI identity. The species-only GTDB synonym does not retain that scope.

[LPSN record 800274](https://lpsn.dsmz.de/species/mycoplasmopsis-columbina) recognizes Mycoplasmopsis columbina and its older Mycoplasma columbinum name. It identifies the type strain as ATCC 29257, MMP 1 and NCTC 10178, not SF7. That species-level nomenclature does not make SF7 the type strain or the species name an exact strain synonym. `EXACT` grounding to NCBI remains valid despite the separate GTDB defect.

## Evidence

`data/raw/gtdb_mappings.tsv:1490` supplies the copied `GTDB:s__Mycoplasmopsis_columbina` closeMatch and genome count three. Exact structured filtering across the ignored-inclusive compressed GTDB catalog found precisely three unique assemblies:

- `data/catalog/gtdb_genomes-0016.jsonl.gz:35679`: `RS_GCF_000222995.1`, strain SF7, taxon 1037410, species taxon 114881, not the representative.
- `data/catalog/gtdb_genomes-0012.jsonl.gz:30976`: `RS_GCF_000712175.1`, ATCC 29257, taxon 1408457, species taxon 114881, assembly from type material.
- `data/catalog/gtdb_genomes-0013.jsonl.gz:25579`: `RS_GCF_900660685.1`, NCTC10178, taxon 114881, assembly from type material and the GTDB representative.

The two type-deposit assemblies are not automatically two different biological strains, but they are not SF7 assemblies. Three is a supported species-cluster count; only one row is assigned to the SF7 taxon. The mapping and exact synonym must distinguish membership from identity.

The complete current GenBank and RefSeq rows, the historical GenBank row and [live NCBI assembly reports](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000222995.2,GCF_000222995.1/dataset_report) identify one current pair: `GCA_000222995.2` / `GCF_000222995.1`. It is a 748,210-base contig-level assembly with 15 contigs, BioSample `SAMN02469897`, sequencing project `PRJNA67465` and WGS master `AFXA00000000.1`. The corresponding historical `GCA_000222995.1` row is suppressed, with a not-live date of 2012-01-21; preserve these different version numbers rather than assuming the GenBank and RefSeq suffixes must match.

The native GTDB metadata points to the current GenBank .2 assembly despite using RefSeq .1. The native RefSeq inventory uses project `PRJNA224116`; live assembly-specific metadata and the GenBank inventory use `PRJNA67465`. Preserve this source context. Annotation counts differ by annotation provider/date and are not assertions in the YAML.

BV-BRC `1037410.3` explicitly links SF7, taxon 1037410, `GCA_000222995.2`, `SAMN02469897` and `PRJNA67465`. The complete GOLD chain is organism `Go0011534` to project `Gp0011534` to analysis `Ga0009502`, IMG 2512047065, and the unversioned `GCA_000222995` / `AFXA00000000` identifiers. Version resolution comes from the inspected NCBI evidence, not from inventing a version on the GOLD row.

The inventory-linked [PMID 23599295](https://pubmed.ncbi.nlm.nih.gov/23599295/) resolves to the 2013 SF7 genome announcement, DOI `10.1128/genomeA.00157-13`, PMCID `PMC3630406`. Its abstract establishes the intended SF7 genome report. Species-level biological statements in that abstract were not imported as individual SF7 phenotypes, and full-text methods were not reviewed.

`data/raw/gold_organisms.tsv:530` supports one `ORGANISM`; the native GOLD organism row corroborates this identity. `data/raw/madin_taxa.tsv:715` supports one `TRAIT_ASSERTION` inventory entry without specifying its biological meaning in the YAML. NCBITAXON's one-NAME count and snapshot note also agree. Counts with different units must not be summed or interpreted as experimental results.

## Completeness

Ignored-inclusive, compressed-content-inclusive `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, using the bounded taxon ID, full current/historical names, slug and SF7/SF-7 variants. Fifty-one source lines matched. All candidate identities and matching fields were inspected; the relevant own rows and all matched TSV rows were then read in full.

Other SF7 candidates denote Erythrobacter fulvus, Shewanella algae, a Shigella isolate, Marinobacter, Burkholderia, a swine fecal bacterium or an environmental community. In particular, BacDive 175915 and its KACC 22865 / TBRC 16611 deposits belong to Erythrobacter fulvus, taxon 2987523. The matching type-material rows also belong to that different taxon. These must not be joined to SF7 merely by designation.

Complete structured scans found no own BacDive, LPSN, MediaDive or BactoTraits inventory row. Five independently enumerated SOURCE.json files were parsed without a target match. Ignored-independent filename scans found exactly one target YAML, no prior target report and no target-specific history filename. These are bounded repository findings, not proof that no other biological evidence exists.

Zero inventoried strains does not mean SF7 lacks a genome or cannot be cultured. The checked genome/organism resources provide evidence for SF7 without establishing a culture-collection deposit eligible for the current strain list. Optional individual genome links, nomenclature and causal graphs need not be invented. iModulonDB is not applicable to the taxonomy and source-count assertions.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

**Major: a GTDB species identity is promoted onto the SF7 strain.** YAML line 40 uses closeMatch from the species mapping; lines 49-52 call the species-only name an `EXACT_SYNONYM` of SF7; line 57 promotes the species to the identity xrefs. Lines 67-72 repeat that close mapping and the unqualified three-genome cluster count. The native cluster contains SF7 plus two type-deposit assemblies, while NCBI explicitly distinguishes strain taxon 1037410 from species taxon 114881. The species-only exact synonym erases the defining strain scope. Three is valid at species-cluster scope, not as the number of SF7 assemblies.

Owner: the kg-microbe GTDB mapping consumed through `conf/sources.yaml` and `src/taxonmech/extract.py:501`, together with `src/taxonmech/seed.py:439` identity promotion and `src/taxonmech/seed.py:574` attestation generation. The current seeder treats closeMatch as identity without rank compatibility. This is one grouped semantic defect; the supported NCBI identity itself is not a blocker.

## Recommended Edits

1. Correct species-versus-strain handling in the maintained upstream mapping and TaxonMech seeder. A species membership relationship must not create a species-only exact strain synonym or identity xref merely because the input says closeMatch. Verify source-edge direction and actual cluster extent before selecting a replacement predicate.
2. Retain three only with explicit species-cluster scope where that context can be represented. If a strain-specific assembly count is desired, derive it independently from taxon/strain-qualified evidence. Do not relabel the cluster's three as one while leaving its source semantics unchanged.
3. Add rank-aware regression tests, then regenerate through maintained inputs in an authorized curation branch. Preserve the valid NCBI synonyms, genetic code 4, source-specific lineage and versioned assembly evidence. Do not hand-edit the generated YAML or extracted TSV row.

Optional culture/genome enrichment is separate work. No record status promotion, curation event or history append is authorized by this review.

## Follow-up Checks

Restore the pinned upstream inputs in `data/raw/MANIFEST.yaml` before replaying the source transforms. Test that a strain retains supported GTDB membership without a species-only exact synonym, and that a single mapping still receives explicit cluster-count scope. Include rank-compatible species mappings as positive controls.

For an authorized fix, run `just seed`, the documented `just seed-canary NCBITaxon:1037410`, schema/strict/history checks, full `just verify-corpus`, tests and QC. The canary writes the record and was not run in this read-only review. Manually inspect predicates, synonym scope, xrefs and attestation notes; structural validators alone cannot prove the correction.

Any future genomic enrichment must retain current `GCA_000222995.2`, paired `GCF_000222995.1`, and historical .1 suppression context. Do not count paired accessions or suppressed versions as additional current SF7 genomes.

## Additional Notes

- YAML SHA-256 remained `6dacfbff33f690c345b42e399a0bd551053e9d3bfb05505e95e1de4dbbc233d0`.
- `data/taxa/PATHS.tsv:15300` and `curation/seed_scope.tsv:26092` uniquely resolve the target. The 2026-09-13T17:54:04Z seed event exactly matches the GOLD/GTDB/MADIN/NCBITAXON scope reason.
- Complete native assembly rows: `data/catalog/ncbi_genbank-0000.jsonl.gz:3875`, `data/catalog/ncbi_genbank_historical-0000.jsonl.gz:1187` and `data/catalog/ncbi_refseq-0000.jsonl.gz:3332`. Own BV-BRC is line 3451; GOLD organism/project/analysis lines are 10132, 9986 and 4283 respectively.
- Read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Only this new report was added for this target. No tracked record, input, schema, history, page, branch, worktree or GitHub state changed. No Eukaryota YAML was opened or review status promoted.
