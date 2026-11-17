# YAML Record Review: uncultured marine bacterium D016

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_marine_bacterium_d016.yaml`
- Started UTC: 2026-10-09T10:38:10Z
- Finished UTC: 2026-10-09T10:41:09Z
- Verdict: pass

## Target

The complete 39-line generated `TaxonRecord` was read independently. It denotes `NCBITaxon:103669`, uncultured marine bacterium D016, at NCBI rank `SPECIES` in `BACTERIA`, under marine bacteria D ensemble (`NCBITaxon:150608`). It carries five root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` status, zero classified BacDive strains, one NCBITAXON name attestation, and one embedded seed event.

No synonyms, nomenclature, taxonomy mappings, equivalent xrefs, strain entries, literature evidence, causal graphs, or discussions are asserted. This is an environmental-clone-associated NCBI concept, not a formally named species or culture deposit. Only this record receives a verdict.

## Validation

Both documented focused validators passed:

```bash
UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/uncultured_marine_bacterium_d016.yaml
UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline python scripts/validate_strict.py data/taxa/bacteria/uncultured_marine_bacterium_d016.yaml --out /private/tmp/taxonmech-d016-review-strict.tsv
```

- LinkML exited 0 with `No issues found`.
- Closed-schema strict validation exited 0: one file scanned, zero error files, zero error rows. The temporary TSV is header-only.
- Read-only structured comparisons checked the complete own backbone row, all five ancestors, seven other raw source tables, PATHS, scope, attestation, and embedded seed-event wording. These checks do not establish full-corpus reproducibility.
- Live NCBI Taxonomy EFetch and Datasets were read for the target's identity. Exact-field scans checked children, type material, retired IDs, and dropped rows.
- `just validate-products` was not run: no curator-added graph nodes or edges occur in this target. No literature citation or graph reference is asserted in the YAML; the newly discovered marker citation was checked separately.
- `just validate-history` was not run: ignored-independent content/filename searches found no target-specific external history record. The embedded event was inspected and validated with the YAML; no history entry was written.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, provenance gates, generated-site drift, or corpus-wide history/product gates. No generator was run.

## Identity and Grounding

The own backbone row at `data/raw/ncbitaxon_taxa.tsv:18534` matches the identifier, label, rank, parent, genetic code, and snapshot date 2026-09-13. Synonym and retirement fields are empty. The complete native scientific-name row at `data/catalog/ncbi_names-0000.jsonl.gz:38550` agrees.

The live [NCBI taxonomy EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103669&retmode=xml) confirms D016, taxon 103669, species rank, parent 150608, and code 11. Its named ancestors agree with the pinned backbone. The [Datasets response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103669) supplies the root-inclusive IDs `1, 131567, 2, 48479, 150608`. The YAML's corresponding labels and ranks are root/NO_RANK, cellular organisms/CELLULAR_ROOT, Bacteria/DOMAIN, environmental samples/NO_RANK, and marine bacteria D ensemble/NO_RANK.

`EXACT` is defensible for the identifier-to-concept link. It does not establish a named-species equivalence, resolved phylogenetic placement, or experimental characterization. The environmental parent chain is carried from NCBI as required by repository policy; no placement is inferred from the paper's broader results.

The pinned backbone has no direct children. Exact target-ID scans found no own rows in `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv`, or `data/raw/dropped.tsv`. These observations are snapshot-scoped, not universal absence claims.

## Evidence

The complete own source row supports the identity and one NCBI name attestation. `data/taxa/PATHS.tsv:15102` associates the identifier with the target slug. `curation/seed_scope.tsv:144178` admits it on 2026-09-13 using the exact reason preserved in the seed event dated 2026-09-13T17:54:04Z.

Exact own-taxon scans returned no rows in `data/raw/bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv`, or `bactotraits_taxa.tsv`. Because there are no backbone children, the zero BacDive count does not omit descendant-classified strains. The single `NAME` assertion is a source count, not a biological measurement, culture count, or genome count.

The inspected generation owners are `src/taxonmech/seed.py:341` for identity/lineage/status, `src/taxonmech/seed.py:479` for code, `src/taxonmech/seed.py:543` for classified strains, `src/taxonmech/seed.py:549` for NCBI attestation, and `src/taxonmech/seed.py:630` for embedded seed history. Their behavior agrees with this record's maintained inputs.

The exact nuccore query `txid103669[Organism:noexp]` returned one entry, UID 5882271. Its complete [GenBank XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=5882271&rettype=gb&retmode=xml) identifies [AF177556.1](https://www.ncbi.nlm.nih.gov/nuccore/AF177556.1), a 559-base partial 16S rRNA marker. The source feature explicitly links `taxon:103669` to clone D016, flags an environmental sample, and describes a surface-associated marine source. Both rRNA ends are partial. All 559 DNA bases are A/C/G/T and match the supplied transcription ignoring case. This is an annotation-consistency check, not an independent alignment or species identification.

The sequence cites Dang and Lovell, PMID 10653705, and their direct submission of 13-Aug-1999. The exact assembly query returned zero entries with NCBI's `phrasesnotfound`/`No items found` diagnostics. No genome was identified; this does not prove that every related organism lacks an assembly. The marker is not a genome or culture accession.

The complete PubMed abstract and bibliographic identifiers for [Dang and Lovell (2000)](https://pubmed.ncbi.nlm.nih.gov/10653705/) were freshly read through EFetch. PMID 10653705 resolves to DOI `10.1128/AEM.66.2.467-475.2000`, Applied and Environmental Microbiology 66:467-475. The study used cultivation-independent ribosomal-marker analysis to examine colonization of test surfaces in a salt-marsh estuary. Those study-wide results do not establish D016-specific substrate preference, physiology, causal mechanism, or named-species equivalence. The D016-to-paper association is supported by D016's own GenBank reference.

Full paper text, tables, and figures were not inspected for this review. The PMC route had returned a browser-verification page during the preceding D015 review; it was not re-requested or bypassed. The web-rendered PubMed response here yielded no text, but the separate EFetch abstract/identifier request succeeded. No clone-specific table value is inferred from search snippets or another clone's report.

All 30 initial source-search candidate rows were read completely, including compressed native records. Important exclusions are:

- `data/raw/ncbitaxon_taxa.tsv:634248`, `data/catalog/ncbi_names-0015.jsonl.gz:14210`, and `curation/seed_scope.tsv:611026` identify Borreliella sp. D016 as taxon 3448912 under parent 2645750, not the target environmental concept.
- BacDive 135331, StrainInfo SI-ID 65561, and GOLD Go0266782 describe Pseudoalteromonas atlantica, taxon 288, with CIP 103669. Their native rows are `data/bacdive/records.jsonl.gz:57636`, `data/straininfo/records.jsonl.gz:52887`, and `data/gold/organisms.jsonl.gz:204831`. Their explicit organism fields exclude a join to D016.
- BacDive 140416 and StrainInfo SI-ID 397331 associate DSM 103669 with Clostridium merdae, taxon 1958780, not 103669: `data/bacdive/records.jsonl.gz:62700` and `data/straininfo/records.jsonl.gz:295220`. Raw type-material rows 74703-74704 name that other taxon. Its marker and genome links are not transferred to this record.
- `data/straininfo/records.jsonl.gz:26763` uses 103669 as an SI-DP for ATCC 25123 within SI-ID 38367, Mycobacterium intracellulare, taxon 1767.
- `data/straininfo/records.jsonl.gz:72175` contains designation FP 103669-S within SI-ID 106369, with KCTC 6666 and ATCC 14793 deposits. The native row supplies no taxon field or explicit D016 link. A numeric substring without identity evidence is not an association; its organism is not guessed.
- `data/catalog/gtdb_genomes-0009.jsonl.gz:10152`, `data/catalog/gtdb_genomes-0007.jsonl.gz:23863`, and `data/catalog/gtdb_genomes-0000.jsonl.gz:49740` use 103669 as contig N50, with one also using it as scaffold N50. All carry Escherichia coli species taxon 562; the third has organism taxon 83334. These numeric assembly statistics are not target taxonomy identifiers.

The corresponding raw BacDive/culture/related-record rows and StrainInfo link/related-record rows were also read in full. They preserve those explicit other-taxon classifications. No verdict is assigned here to another TaxonMech record, and collateral differences in other sources' type flags are not used to alter this target.

## Completeness

Complete enough for its supported seeded scope. Optional nomenclature, synonyms, mappings, xrefs, literature, definitions, strain entries, and graphs need not be filled merely because the concept exists. The explicit AF177556.1 linkage could support future optional provenance enrichment, but it is not a missing required genome or strain entry.

The initial case-insensitive pattern was `\b103669\b|\bD[ _-]?016\b|uncultured_marine_bacterium_d016\b`. After reading the marker, it was repeated with `|\bAF177556(?:\.1)?\b`. Both searches used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Ignored and compressed files were included. Both returned the same 30 content rows, all fully read; the accession expansion added no match in those roots.

All five `SOURCE.json` files discovered under `data`, `curation`, and `history` with ignored-inclusive discovery were separately parsed completely. Neither target search pattern matched a metadata value. Ignored-independent filename searches under `data/taxa`, `reports/yaml_record_review`, and `history` found only the target YAML before this report was written, with no earlier target report or target-specific history filename. These are bounded repository searches, not an assertion that every external culture, assembly, or paper was examined.

iModulonDB was not applicable: no target gene, regulator, expression dataset, module, or transcriptomic claim is present. No mechanism, phenotype, or phylogenetic placement was borrowed from an adjacent clone or higher taxon.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the record's asserted scope. Identity, lineage, code, source count/unit, strain count, admission, and seed history agree with the inspected evidence. Limited paper access does not invalidate the source-backed NCBI-only YAML.

## Recommended Edits

None required. Retain `mapping_status: SEEDED`; this report is not human curation sign-off. Do not hand-edit generated YAML or pages.

Any later enrichment must preserve the explicit AF177556.1-to-103669 relationship through a maintained, validated input path, keep partial markers outside genome counts, and distinguish clone D016 from Borreliella sp. D016 and similarly numbered deposits. A supported backbone change belongs in the NCBI inventory/source transform and seeder. No scope change is supported.

## Follow-up Checks

- Inspect an authorized accessible full text before adding D016-specific experimental or phylogenetic statements. Abstract-level context is insufficient for clone-level table values.
- Require an explicit taxon/sample/deposit/accession relationship before adding any culture or genome association; a shared D016 label or 103669 number is insufficient.
- After any later authorized maintained-input change, rerun both focused validators, inspect the generated canary, and run the documented full `just verify-corpus` and `just qc` gates. History should accompany that later authorized curation change, not this review.

## Additional Notes

This independent review followed the local one-record review skill and field checklist. D016's own source rows, taxonomy, marker, and citation were inspected; no D015 finding or verdict was inherited.

Target SHA-256 remained `f513aa41cf7ee1323d328e54840349e1c0d4196ea95d27528b5c5fbe233eb989` before and after inspection. This review wrote only this new repository report and did not change YAML, inventories, scope, pages, history, review status, GitHub state, branches, or existing worktrees. Eukaryota remained untouched.
