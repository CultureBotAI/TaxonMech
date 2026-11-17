# YAML Record Review: Bradyrhizobium japonicum USDA 6

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bradyrhizobium_japonicum_usda_6.yaml`
- Started UTC: 2026-10-10T02:43:45Z
- Finished UTC: 2026-10-10T02:49:28Z
- Verdict: needs curation

## Target

The entire 84-line generated `TaxonRecord` was read. `NCBITaxon:1037409` denotes Bradyrhizobium japonicum USDA 6, rank `STRAIN`, domain `BACTERIA`, parent `NCBITaxon:375`, genetic code 11, grounding `EXACT` and mapping status `SEEDED`.

It contains ten ancestors, one GTDB mapping with 81 genomes, three exact synonyms, one GTDB xref, zero inventoried strains, NCBITAXON/GTDB/MADIN attestations and one seed event. It is the named strain, not the whole species. No phenotype, causal graph or individual genome link is asserted in the YAML.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/bradyrhizobium_japonicum_usda_6.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/bradyrhizobium_japonicum_usda_6.yaml --out /private/tmp/taxonmech-usda6-20261010-validation.tsv --workers 1`: one file, zero errors; output reread, header only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured source comparisons verified identity, every ancestor, code, NCBI synonyms, own source counts, index/scope resolution and exact seed reason. Complete backbone scanning found no immediate child. Own type-material, merged-ID and dropped-record inventories had no rows; the USDA 6 type-material row is instead filed at parent taxon 375.
- Complete native own rows were read from the NCBI names and assembly catalogs, GTDB, BacDive, StrainInfo, BV-BRC, GOLD and AllTheBacteria. An exact parsed GTDB species census independently counted 81 unique assemblies, including two with taxon 1037409. This is a source cross-check, not an invented replacement for a documented validator.
- Live NCBI taxonomy, assembly and PubMed API responses and the LPSN species page were inspected. The GTDB genome page was unavailable through the web reader; the pinned native GTDB rows supplied the mapping evidence.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, full provenance replay, rendering and publication gates. No graph is present for `just validate-products`. Passing structural checks does not establish semantic mapping correctness.
- The configured kg-microbe checkout lacked the referenced GTDB and Madin transformed edge files. A gitignore-independent filename search across its `data` directory also found no matching GTDB/Madin files or `edges.tsv`. The extraction manifest and committed inventories were inspected, but the original six Madin assertions and transformed GTDB edges were not replayed.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222746`, [NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037409&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037409) agree on the named strain and its placement. EFetch explicitly gives rank strain, parent 375 and code 11; Datasets includes root 1 and reports two assemblies.

The complete root-first chain agrees with the backbone: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Alphaproteobacteria, Hyphomicrobiales, Nitrobacteraceae, Bradyrhizobium and Bradyrhizobium japonicum. Preserve this NCBI lineage. The alternate GTDB order/family labels Rhizobiales/Xanthobacteraceae in the genome catalog do not authorize overwriting it.

The complete native name rows `data/catalog/ncbi_names-0005.jsonl.gz:32377`, `:32378` and `:32379` establish the two strain-qualified equivalent names and scientific name. Both NCBI exact synonyms are supported. The species-only GTDB exact synonym is not, as detailed below.

The cached legacy [NCBI browser page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037409) displayed no rank, unlike both directly fetched APIs, which returned strain. This source-display discrepancy is retained rather than silently treating the cached page as the current rank authority. `EXACT` grounding to the NCBI strain remains sound; it does not validate the separate GTDB equivalence claim.

## Evidence

`data/raw/gtdb_mappings.tsv:1489` supplies `GTDB:s__Bradyrhizobium_japonicum`, `skos:closeMatch` and 81. The generated YAML faithfully copies that row, but copying it is not sufficient evidence of species-to-strain identity.

Exact parsing of `gtdb_taxonomy` across the ignored-inclusive compressed GTDB catalog found 81 distinct assemblies in this species cluster. Their NCBI taxon distribution was 68 at 375, two each at 1037409, 1079467 and 476282, and one each at 1128255, 1128256, 136996, 208389, 29448, 3082951 and 3240368. These are catalog assignments, not a claim that the named NCBI taxa are all taxonomic synonyms. The cluster includes strains such as USDA 38, SEMIA 5079 and CCBAU 15618, so its full membership cannot denote USDA 6 alone.

The complete native USDA 6 rows are `data/catalog/gtdb_genomes-0004.jsonl.gz:37357` and `data/catalog/gtdb_genomes-0005.jsonl.gz:47111`. Both distinguish `ncbi_taxid: 1037409` from `ncbi_species_taxid: 375`. The first, `RS_GCF_000284375.1`, is the GTDB representative; the second, `RS_GCF_000472985.1`, is not. Representative status does not make a strain coextensive with the species cluster. The number 81 is correct at cluster scope; it is not 81 assemblies assigned to the USDA 6 taxon.

The full GenBank and RefSeq catalog rows and [live NCBI assembly reports](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCF_000284375.1,GCF_000472985.1/dataset_report) corroborate two current assembly pairs:

- `GCA_000284375.1` / `GCF_000284375.1`, complete genome, 9,207,384 bases, BioSample `SAMD00060992`, project `PRJDA67463`, chromosome `AP012206.1` in the BV-BRC record.
- `GCA_000472985.1` / `GCF_000472985.1`, scaffold assembly, 9,131,141 total bases, 9,129,831 ungapped bases, 87 scaffolds and 89 contigs, BioSample `SAMN02441114`, project `PRJNA163001`, WGS master `AXAV00000000.1`.

These pairs are not four separate biological strains. Native RefSeq summary project `PRJNA224116` is retained as source context rather than substituted for the assembly-specific sequencing projects. BV-BRC entries `1037409.3` and `1037409.40` support the first assembly; `1037409.18` supports the second. One BV-BRC assembly field has trailing whitespace, not a different accession.

GOLD preserves the same provenance through organism `Go0009853`: project `Gp0013271` leads to analysis `Ga0009468`, IMG 2511231207 and `GCA_000284375.1`; project `Gp0009853` leads to `Ga0025170`, IMG 2513237097 and `GCA_000472985.1`. Project `Gp0067902` names `PRJNA175444`, but the inspected rows do not establish an additional assembly for it. The Clostridium USDA_6 candidates are unrelated and were excluded.

The assembly inventory's [PMID 24710291](https://pubmed.ncbi.nlm.nih.gov/24710291/) resolves to the 2011 primary genome paper, DOI `10.3390/genes2040763`, PMCID `PMC3927601`. Its abstract reports one circular 9,207,384-base chromosome for USDA6T. It supports that specific genome, not equivalence between all GTDB cluster genomes and USDA 6. No physiological assertions were imported from the publication or BioSample metadata.

`data/raw/madin_taxa.tsv:714` supports six `TRAIT_ASSERTION` inventory records. Their individual biological content was not replayed, and the YAML does not assert six particular phenotypes. The NCBITAXON one-NAME attestation and 2026-09-13 snapshot note agree with the inventory. Units are not combined across sources.

## Completeness

Ignored-inclusive, compressed-content-inclusive `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, using bounded taxon ID, full strain name, slug and USDA 6 variants. Thirty-one source lines matched; all native candidate identities and matching fields were inspected, and the relevant own records were subsequently read in full. The separate GTDB cluster census used exact structured taxonomy filtering, not the broader name search alone.

Complete own-taxonomy inventory scans found no BacDive, LPSN, GOLD, MediaDive or BactoTraits attestation row. This is a bounded inventory result, not a claim that the strain lacks culture, nomenclatural or genome evidence. Five independently enumerated SOURCE.json files were parsed without a target match. Ignored-independent filename scans found the one target YAML and no prior target report or target-specific history filename.

[LPSN record 774164](https://lpsn.dsmz.de/species/bradyrhizobium-japonicum) explicitly includes USDA 6 among the type-strain designations for the species. `data/raw/ncbi_type_material.tsv:198190` files USDA 6 under taxon 375. Native BacDive 1805 and StrainInfo SI-ID 1344 likewise use species taxon 375, with DSM 30131, ATCC 10324, LMG 6138, NBRC 14783 and other deposits. StrainInfo includes USDA 6 as a designation. These establish useful type-strain context, but the documented seeder gathers exact-taxonomy and descendant BacDive strains, not ancestor entries. Thus `strain_count: 0` follows the current inventory policy and is not evidence of unculturability.

Do not transfer every sequence in that broad StrainInfo group onto the USDA 6 label. Its genome `GCA_006539645` is explicitly attached to NBRC 14783, SI-DP 489393; its other sequence entries retain their own deposit provenance. The BacDive genome field also names NBRC 14783. Preserve deposit-specific evidence and resolve versioned accessions before any separately authorized enrichment.

The full AllTheBacteria rows name USDA 6 for `SAMD00079864` / `ERZ2886089` and `SAMN02441114` / `ERZ4057247`. The former is HQ PASS; the latter has `SYLPH_RESULTS_FAIL`. They are candidate sample/assembly context, not automatically interchangeable with the BacDive culture record or proof of an additional qualified genome claim.

Optional nomenclature, deposited-strain entries, individual genomes and graphs need not be invented to pass this checklist. Their absence is not counted separately. iModulonDB is not applicable to the record's taxonomy and source-count assertions; no gene, regulator or expression-module claim requires it.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

**Major: GTDB species identity is promoted onto a single strain.** At YAML line 43 the species mapping is `skos:closeMatch`; lines 46-49 call the species-only name an `EXACT_SYNONYM` of USDA 6; line 57 promotes the species into the identity xrefs. The GTDB attestation repeats the close mapping and the unqualified species-wide 81-genome count at lines 67-72. Native taxonomy separates species 375 from strain 1037409, and only two of the 81 cluster assemblies carry the target strain taxon. The exact synonym erases the defining strain scope. The count itself is supported at species-cluster scope, not as a strain-level assembly count.

Owner: the upstream kg-microbe GTDB mapping consumed through `conf/sources.yaml` and extracted by `src/taxonmech/extract.py:501`, plus the identity-promotion logic in `src/taxonmech/seed.py:439` and primary-attestation logic at `src/taxonmech/seed.py:574`. The seeder currently accepts every closeMatch as identity without checking rank compatibility. This is one grouped mapping/synonym/count-scope defect, not three independent findings. The NCBI identity itself is correct, so no blocker is assigned.

## Recommended Edits

1. In the maintained upstream mapping and TaxonMech seeder, distinguish species identity from strain membership. Prevent a GTDB species label from becoming an exact strain synonym or identity xref solely because the source emitted closeMatch. Review the mapping's direction and actual cluster extent before choosing a replacement predicate; do not mechanically substitute broadMatch or assume GTDB and NCBI species boundaries are identical.
2. Keep 81 only with explicit GTDB species-cluster scope where the representation supports that context. If a strain-specific assembly count is desired, derive it from taxon/strain-qualified assembly evidence and clearly distinguish it from the cluster count. Do not simply change the source's 81 to two while continuing to label it the species total.
3. Add rank-aware regression coverage around seeding and attestation generation. Regenerate through maintained inputs after a separately authorized fix; do not hand-edit this generated YAML or its extracted inventory row. Preserve the two valid NCBI synonyms, NCBI lineage, grounding and seed provenance.

No curation event, status promotion or history append is authorized by this review. Optional culture/genome enrichment is separate work and must preserve complete deposit and source-chain identifiers.

## Follow-up Checks

Restore the pinned upstream inputs identified by `data/raw/MANIFEST.yaml` before replaying extraction. Its source revision is `kg-microbe@30405b70ef762aa46c08278b2b3e06bffb0b34cd`; the extraction time is 2026-09-13T17:50:44Z. Verify provenance rather than substituting an undated current transform.

For a future fix, test that a strain can retain supported GTDB membership without acquiring a species-only exact synonym, that rank-compatible species mappings still work, and that cluster counts remain scoped even when only one GTDB mapping is present. Use `just seed` followed by the documented `just seed-canary NCBITaxon:1037409` in the authorized curation branch, then schema/strict/history checks, full `just verify-corpus`, tests and QC. Canary execution writes the record and was intentionally not run here.

Inspect the resulting source predicates, xrefs, synonyms and attestation notes manually. Structural validation alone will not prove the scientific scope correction. Any future culture join must verify its exact deposit and sequence linkage, including versions and the AllTheBacteria qualification flags.

## Additional Notes

- YAML SHA-256 remained `ab9cf25ffacae79aa5167fbd34afb0d8e44d39e9d66c67fff33c2396cb74b9f7`.
- `data/taxa/PATHS.tsv:15298` and `curation/seed_scope.tsv:36185` uniquely resolve the target. The scope reason and 2026-09-13T17:54:04Z seed event agree on GTDB, MADIN and NCBITAXON.
- Assembly native rows: `data/catalog/ncbi_genbank-0000.jsonl.gz` lines 6508 and 14985, and `data/catalog/ncbi_refseq-0000.jsonl.gz` lines 5559 and 12616. These were read in full, as were BacDive line 1800, StrainInfo line 1344, BV-BRC lines 3448-3450 and the own GOLD source chains.
- Read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Only this new report was added for this target. No tracked record, input, schema, history, page, branch, worktree or GitHub state changed. Existing worktrees were preserved. No Eukaryota YAML was opened.
