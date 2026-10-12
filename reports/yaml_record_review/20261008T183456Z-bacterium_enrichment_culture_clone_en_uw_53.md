# YAML Record Review: bacterium enrichment culture clone En_UW_53

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_53.yaml`
- Started UTC: 2026-10-08T18:31:10Z
- Finished UTC: 2026-10-08T18:34:56Z
- Verdict: pass

## Target

Reviewed the entire generated `TaxonRecord` for `NCBITaxon:1036439`, bacterium enrichment culture clone En_UW_53. The YAML specifies species rank, bacterial domain, parent `NCBITaxon:48479`, code 11, `EXACT` grounding, `SEEDED` mapping status and zero strains. Its sole source attestation is one NCBITAXON `NAME`; its sole history event is the seed operation. Optional synonyms, nomenclature, taxonomy mappings, strain/genome links and causal graphs are not present.

An ignored-inclusive filename search of `data/taxa`, `reports/yaml_record_review` and `history` resolved one target YAML and no prior report for its stem. Generated YAML is not the maintained location for a future correction.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `just validate data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_53.yaml`: passed, no issues.
- `just validate-strict data/taxa/bacteria/bacterium_enrichment_culture_clone_en_uw_53.yaml --out /private/tmp/uw53-strict.tsv`: passed, one file, zero errors. The full TSV was read and contained only its header.
- Structured comparisons scanned the complete pinned backbone, all four ancestors, seven supplementary raw inventories, scope, PATHS, type-material, merged-ID and dropped tables. All stored identity, lineage, attestation and seed-event values agree with the relevant input rows.
- Complete nucleotide/protein XML parsing verified actual lengths against declared lengths and compared the submitted CDS translation with its linked protein sequence. These checks passed; they do not independently translate or align the sequence or measure function.

Not checked: `just verify-corpus`, full-corpus schema validation, global provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Bounded source checks do not establish corpus reproduction. The embedded seed event was inspected; searches below found no separate target history artifact. `just validate-products` is not applicable because no graph nodes are present. No undocumented single-record substitute was used for a corpus-wide gate.

## Identity and Grounding

The full [NCBI taxonomy EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036439&retmode=xml) confirms the exact label, species rank, parent 48479 and code 11. The [NCBI Datasets response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036439) confirms lineage IDs 1, 131567, 2 and 48479. Pinned ancestor rows agree with the YAML's root-first labels and ranks: root, cellular organisms, Bacteria and environmental samples. EFetch's displayed lineage omits root while Datasets includes it; that does not contradict the record.

This is NCBI's environmental clone taxon, not a demonstrated pure isolate or a formally named species. `EXACT` appropriately denotes identifier grounding, not experimental characterization. Live EFetch supplies no other names, and pinned synonym fields are empty. Complete pinned scans found no target type-material, merged-ID or dropped row and no backbone children.

## Evidence

The source rows were read completely:

- `data/raw/ncbitaxon_taxa.tsv:222441`: exact identity, rank, parent, code, empty synonyms, NCBI attestation and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:31985`: the target scientific-name object with an empty unique-name field.
- `data/taxa/PATHS.tsv:14948`: exact ID and slug.
- `curation/seed_scope.tsv:322688`: admission date and one-source reason agreeing with the embedded seed-event wording.

The attestation's unit is `NAME`, not organism count, assembly or experiment. Exact-target scans of complete BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits raw inventories returned no rows. Zero represented strains and no extra source attestations are consistent with those inputs.

Two additional catalog candidates were read in full and rejected as numeric collisions:

- `data/catalog/ncbi_genbank-0002.jsonl.gz:7482` is `GCA_002714375.1`, Flammeovirgaceae bacterium isolate SAT1302, with taxid and species taxid 2026740. The target number occurs in `genome_size` and `genome_size_ungapped`, both 1036439. This does not link its assembly, BioSample `SAMN07618935`, project `PRJNA391943` or listed PMID 29337314 to En_UW_53.
- `data/catalog/gtdb_genomes-0000.jsonl.gz:46855` is `GB_GCA_041330455.1`, Parabacteroides distasonis isolate D5064bin9, with NCBI taxid and species taxid 823. The number 1036439 is `ncbi_contig_n50`; total and ungapped genome lengths are 5119024. Its classification and assembly/sample/project identifiers do not supply a target GTDB mapping or genome link.

The exact non-expanded Nuccore query `txid1036439[Organism:noexp]` returned one record, UID 336092422. The complete [HQ630177.1 nucleotide record](https://www.ncbi.nlm.nih.gov/nuccore/HQ630177.1) assigns a 340-base partial `nosZ` CDS to taxon 1036439 and clone En_UW_53. It identifies an anode-biofilm source, environmental-sample status and H2S-supplemented mineral medium. Both CDS ends are partial, codon start is 3 and translation table is 11. No strain, collection deposit or geographic qualifier is supplied.

The complete linked [AEI00835.1 protein record](https://www.ncbi.nlm.nih.gov/protein/AEI00835.1) reciprocally names HQ630177.1 and the same taxon/clone. Its 112-residue conceptual translation has a PRK02888/CDD:235082 region through residue 112. Declared and actual nucleotide/protein lengths match, the submitted translation exactly equals its own protein sequence, and no non-ACGT DNA symbols or ambiguous amino-acid symbols were found. This supports a consistent submitted fragment annotation, not measured nitrous-oxide reduction or an organism-level pathway.

Both sequence records reference an unpublished enrichment study and a direct submission dated 17-NOV-2010, without a PMID or DOI for that unpublished reference. An enrichment condition or a partial gene annotation does not demonstrate isolate purity or measured whole-organism physiology.

The [2015 Vilar Sanz dissertation](https://dugi-doc.udg.edu/bitstream/handle/10256/12459/tavs1de1.pdf?sequence=5), printed page 54, identifies HQ630075-HQ630210 as enrichment-derived nosZ accessions; HQ630177 falls in that range. Page 92 warns that one DGGE band is insufficient to establish purity. Both pages were read completely. Searching all 164 pages of extractable text for the exact accession/clone returned no match. This is study context, not a clone-specific species assignment; raster and supplementary content were not exhaustively searched.

Exact accession and protein web queries returned no results; the clone-label query excluding the already checked NCBI Taxonomy site also returned none. Exact accession/clone finds in the [PLOS article main HTML](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0063460) found no matching text. No community-level experimental result was transferred to this clone. These bounded discovery checks do not establish literature absence.

## Completeness

Complete enough for the supported taxonomy seed. Empty optional mappings, nomenclature, deposits, genomes, synonyms and graphs are appropriate without a supported identity chain. The external partial gene is not a genome assembly and is not a mandatory taxonomy-record field.

Expanded searches used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, including ignored and compressed files. Patterns included taxid, slug, clone-label variants, own nucleotide/protein accessions, unpublished study title and PLOS DOI. Five rows matched: backbone, native name, scope and the two rejected metric collisions. Each was read completely. Five source `SOURCE.json` files were separately parsed in full without a target identity match, and history filenames were separately searched. Negative results are bounded to these roots and expressions.

An exact non-expanded Assembly query returned zero with a phrase-not-found warning. This establishes no hit under that exact taxid query, not universal genome absence. No independent UniProt or pure-isolate identity was established. iModulonDB was not run: the record makes no gene, regulator or transcriptomics claim, and no covered strain/dataset was identified. That is not evidence of absence from the database.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Both metric collisions were excluded, and the external fragment's limited biological characterization does not contradict the stored taxonomy claims.

## Recommended Edits

None required. Preserve the generated YAML and its `SEEDED` state. Do not import either unrelated genome, its classification, sample/project links or literature. Do not infer a phenotype or isolate identity from neighboring clone names, medium or study membership.

Any future taxonomy correction belongs first at NCBI and then in the pinned input governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. A demonstrated projection defect belongs in `src/taxonmech/seed.py` with a focused regression test; a scope decision belongs in `curation/seed_scope.tsv`. Optional sequence provenance requires supported maintained input and model/seeder handling, not direct YAML edits.

## Follow-up Checks

No corrective follow-up is required. Before optional genome or trait enrichment, establish explicit primary evidence connecting this exact clone to the asserted entity or experiment. Use typed identifiers, not genome lengths or contig statistics, for catalog joins.

After an authorized input/seeder correction, run the focused regression test, `just seed-canary NCBITaxon:1036439`, inspect the emitted YAML, rerun both record validators and `just verify-corpus`, then use the full publication QC gates. No regeneration was performed for this review.

## Additional Notes

The single-record skill, local field checklist, write boundaries and documented validators governed this review. Its own evidence was inspected rather than inferred from adjacent accessions. Before/after YAML SHA-256 was `0998cd36ea5ddb51ca11092ab0fed8d1f360394d704b9b2599b473ee3e28849f`.

Only this new timestamped report was written for this target. No record, inventory, history, status, generated page or GitHub object was changed. Existing worktrees and the fully covered Eukaryota corpus remained untouched.
