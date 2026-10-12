# YAML Record Review: Wolbachia endosymbiont of Pyralidae sp.

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_pyralidae_sp.yaml`
- Started UTC: 2026-10-09T09:36:25Z
- Finished UTC: 2026-10-09T09:42:58Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` was read and uniquely resolved as `NCBITaxon:1036671`, Wolbachia endosymbiont of Pyralidae sp. It asserts `SPECIES` rank, `BACTERIA` domain, parent `NCBITaxon:2640676`, genetic code 11 and eleven root-first ancestors. Its status is `EXACT`/`SEEDED`, with zero linked strains and one NCBITAXON attestation counting one NAME in the 2026-09-13 snapshot. The single embedded event records source seeding on 2026-09-13T17:54:04Z.

This review concerns the bacterial taxon, not the eukaryotic host-family record. It is based on this record's own sources and evidence, not adjacent-record verdicts. The YAML is generated and is not a maintained correction surface.

## Validation

The focused documented implementations ran successfully:

```bash
UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/wolbachia_endosymbiont_of_pyralidae_sp.yaml
UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline python scripts/validate_strict.py data/taxa/bacteria/wolbachia_endosymbiont_of_pyralidae_sp.yaml --out /private/tmp/taxonmech-wolbachia-pyral-review-strict.tsv
```

- LinkML: `No issues found`, exit 0.
- Strict: one file scanned, zero files with ERROR and zero ERROR rows, exit 0. The complete temporary output TSV contained only its header.
- Structured comparison against the pinned taxonomy checked identifier, label, rank, parent, code, every ancestor, synonym fields, all attestations, path mapping and scope/history text. All compared values agreed. This was not a full corpus-reproduction check.
- Exact-field scans of `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv` and `data/raw/dropped.tsv` returned no target rows. The inspected backbone had no children of this taxon. These are bounded local snapshot results.
- JF902228.1 and JF902229.1 each declare and contain 657 bases; JN674157.1 declares and contains 618. All three have only A/C/G/T sequence characters, and their complete source, gene and CDS annotations were read. No independent translation verification, alignment or phylogenetic reconstruction was performed.
- A read-only structured comparison matched 27 supplementary specimen rows to complete current NCBI summaries by exact voucher, BOLD process identifier, sequence length and the two already supplied accessions. It found 26 assigned to taxon 1084952 and one to 1084953. Metadata correspondence is not taxon equivalence.
- Not checked: full-corpus `just verify-corpus`, `just qc`, complete test suite, all-record strict validation, source-provenance gates, generated-page drift or full history validation. There are no curator-added graph-node groundings requiring the OAK product-label gate here. No separate history entry was created or validated; this review does not authorize history mutation.

Target SHA-256 before and after research: `1f11bce2f40760f020e033061795d11e0346a0d5ef0b3d2a2e8cedc0e7dedd60`.

## Identity and Grounding

The complete live [NCBI Taxonomy EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036671&retmode=xml) and [NCBI Datasets response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036671) confirm the exact target label and species rank. EFetch verifies parent 2640676 and genetic code 11. Together the responses support all carried ancestors, including root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Alphaproteobacteria, Rickettsiales, Anaplasmataceae, Wolbachieae, Wolbachia and unclassified Wolbachia. No alternative name or replacement was supplied for this target.

`EXACT` is appropriate identifier grounding, not proof that all Wolbachia from a pyralid host are interchangeable. The authority's species rank on this host-associated label does not imply a formally published binomial, culture deposit or isolated genome. `SEEDED` correctly preserves the workflow state.

The closest specimen leads resolve separately as [taxon 1084952](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1084952&retmode=xml), Wolbachia endosymbiont of pyralJanzen01 Janzen01, and [taxon 1084953](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1084953&retmode=xml), Wolbachia endosymbiont of pyralJanzen01 Janzen15. Both complete EFetch/Datasets response pairs were read. Each retains its own identifier and Wolbachia sp. synonym under the same unclassified-Wolbachia parent. Neither response equates it with 1036671.

## Evidence

Complete source rows supporting the target were inspected at:

| Address | Supported content |
| --- | --- |
| `data/raw/ncbitaxon_taxa.tsv:222574` | Identity, rank, parent, code, source, snapshot and empty supplied synonym fields |
| `data/catalog/ncbi_names-0005.jsonl.gz:32118` | Exact scientific name and identifier |
| `curation/seed_scope.tsv:322821` | Admission date and one-source NCBI reason reproduced by seed history |
| `data/taxa/PATHS.tsv:15092` | Identifier-to-slug mapping |

The two complete primary marker records [JF902228.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902228.1) and [JF902229.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902229.1) both explicitly identify taxon 1084952 and host Pyralidae sp. They concern separate Costa Rican specimens:

| Accession | Voucher suffix | BOLD process | Source detail |
| --- | --- | --- | --- |
| JF902228.1 | MHMXF258-07.w | ASLEP066-10 | GenBank supplies Costa Rica but no collection-date qualifier |
| JF902229.1 | MHMYE110-09.w | ASLEP093-10 | 3 July 2009, Sector San Cristobal, Rio Areno, Alajuela |

Both are partial COI CDSs with code 11 and codon start 1, not genome assemblies. Their source vouchers carry the `BIOUG<CAN>:` prefix. The full records include Smith's barcoding study as unpublished and a 1 May 2011 direct submission. No target YAML assertion relies on either marker.

The published [Smith et al. study](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0036514), PMID 22567162 and DOI 10.1371/journal.pone.0036514, was checked through the complete PubMed abstract, selected publisher methods/discussion and primary Table S2. Its methods distinguish bacterial COI and specimen-associated codes from insect barcodes. The `Wolbachia CO1` sheet explicitly joins the two markers to their vouchers at rows 225 and 252. It also supplies the 26 July 2006 collection date for MHMXF258-07.w, which is absent from the GenBank qualifier; this is supplementary context, not a contradictory date.

All four workbook sheets were searched for Pyralidae, pyralJanzen01 and exact initial marker/specimen identifiers. Every matching row was read in full. Thirty-nine rows matched on the COI sheet; 27 concern the pyralJanzen01 specimens, including 25 entries that still had pending accession placeholders. The remaining 12 rows have different specimen or host labels and were not individually resolved to current accessions. This was not an exhaustive reanalysis of the study.

The current pyralJanzen01 index query returned 27 complete summaries: JF902228.1, JF902229.1 and JN674133.1 through JN674157.1. All 27 specimen/process/length links agreed with the inspected supplementary rows. The 25 pending entries are thus resolved at current-summary level, not treated as missing sequences. Twenty-six summaries identify 1084952; only JN674157.1 identifies 1084953. None identifies the target 1036671.

The complete [JN674157.1 GenBank XML](https://www.ncbi.nlm.nih.gov/nuccore/JN674157.1) additionally verifies voucher MHMYF1533-10.w, process ASWLP042-11, Costa Rica, the Janzen15 host string and a partial COI CDS using code 11 and codon start 2. Its 13 September 2011 direct submission is distinct from the earlier JF records. No culture-deposit or assembly identity was inferred from it.

The original broader Pyralidae sequence query also returned nine fbpA markers assigned to Wolbachia pipientis, taxon 955: KX843653.1, KX843569.1, KX843446.1, KX843445.1, KX843444.1, KX843443.1, KX843442.1, KX843428.1 and KX843039.1. All complete summaries were read. They describe distinct French Polynesian specimens, not an explicit link to this target. Across the two queries, 36 unique complete summaries were inspected; full GenBank XML was read for the three COI records detailed above, not all 36 sequences.

The quoted-name PubMed query rejected the exact phrase and returned [Chai et al. 2011](https://pubmed.ncbi.nlm.nih.gov/22233324/), DOI 10.1673/031.011.12301. Its complete abstract describes Chinese Cnaphalocrocis medinalis populations and Wolbachia typing. It does not identify the reviewed taxon. Its infection frequencies, inferred transmission and supergroup assignment were not transferred to the YAML; the full paper was not reviewed.

Local expanded candidates comprised three target rows, eight rows for the two separately identified taxa, and one numeric collision. The sibling rows are `data/raw/ncbitaxon_taxa.tsv:233140`, `data/raw/ncbitaxon_taxa.tsv:233141`, `curation/seed_scope.tsv:331686`, `curation/seed_scope.tsv:331687`, and scientific-name/synonym rows 44957, 44958, 44959 and 44960 of `data/catalog/ncbi_names-0005.jsonl.gz`. All were read in full. In `data/catalog/gtdb_genomes-0016.jsonl.gz:26145`, 1084952 is scaffold N90 for RS_GCF_030513645.1, a Mycobacteroides abscessus record under NCBI taxon 1185650; it is not a Wolbachia taxon link.

No unsupported assertion, evidence-placement problem or citation mismatch was found in the target. iModulonDB was not applicable: the YAML asserts no gene, regulator, expression module, transcriptomic observation or phenotype.

## Completeness

The record is complete enough for its NCBI-attested generated scope. Optional nomenclature, synonyms, taxonomy mappings, strains, deposits, genome links and causal graphs are correctly unasserted. `strain_count: 0` is an upstream linked-record count, not a biological assertion that no sequence, infection or strain exists. Related marker accessions and specimen vouchers do not establish a required culture-deposit or genome listing.

All local absence checks included ignored files. The content searches used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. The initial expression was:

```text
\b1036671\b|wolbachia[ _]endosymbiont[ _]of[ _]pyralidae\b
```

The next pass added 1084952, pyralJanzen01, JF902228/JF902229, their sequence UIDs, MHMXF258-07/MHMYE110-09 and ASLEP066-10/ASLEP093-10. The final pass additionally searched 1084953, the JN674133-JN674159 accession range, the process-code pattern `ASWLP0(?:39|4[0-35789]|5[0-9]|6[0-4])[ _-]11` and all 25 resolved pending-entry voucher strings, permitting space/underscore/hyphen separators. That process-code pattern does not include ASWLP046-11, but its exact specimen MHMYH1412-10 was independently included in the voucher search. The wider accession expression covered two extra numeric suffixes beyond the 25 resolved markers.

The initial pass returned three target rows. Both expanded passes returned the same 12 source rows, all completely inspected. No additional target association was established. Five discovered `SOURCE.json` files were parsed completely in all passes, with no matching keys or values. Filename inventories included `data/taxa`, `reports/yaml_record_review` and `history`; they found the unique target YAML but no previous target report or target-named separate history file. These statements cover the named roots and terms, not all possible spellings or remote sources.

Exact target scans of the seven raw supplementary inventories for BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits found no target rows. The live Nuccore and Assembly taxon queries returned zero with phrase-not-found warnings; this is only an index result, not evidence that a directly resolving taxon is invalid or has no possible sequence. The family query's host-family expansion and PubMed's rejected exact phrase were explicitly retained as search limitations.

No consequential required omission was demonstrated. The biological relationship between this broad host-associated label and the more specific specimen taxa is not established by the inspected evidence, and the YAML does not falsely assert one.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within this record-level review. Identity, carried lineage, source units/counts, grounding and seed provenance agree. This pass does not certify the entire related-host literature, all external sequence records, full-corpus reproducibility or unperformed strain typing.

## Recommended Edits

None required. Preserve the YAML, `SEEDED` status and embedded history. Do not move sibling COI sequences or W. pipientis fbpA markers into this record based only on their host family.

A future authority-backed taxonomy correction belongs in the pinned intake through `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`; a demonstrated projection defect belongs in `src/taxonmech/seed.py` with a focused regression test. Admission changes belong in `curation/seed_scope.tsv`. Never patch generated YAML or pages to force agreement.

## Follow-up Checks

No immediate blocker remains. Before an equivalence or sequence link is added, require explicit source evidence for the target identifier and specimen, preserve the separate taxon identities and recheck authority merge status. After an authorized source/projection fix, run a focused regression test, `just seed-canary NCBITaxon:1036671`, inspect the emitted record, repeat both focused validators, then run `just verify-corpus` and authoritative `just qc`. None of these regeneration operations was performed here.

## Additional Notes

Work used branch `codex/record-review-extensimonas-20261003` at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. This report is the sole repository artifact created for this target. This review did not change records, source inventories, generated pages, curation histories, statuses, GitHub objects or worktrees, did not contact people and did not use paid research. Eukaryota records and reports were left untouched.

The primary supplement was read from `/private/tmp/taxonmech-wolbachia-noto-table-s2.xls`, downloaded from the publisher during this turn and byte-compared with the existing cached copy. SHA-256: `8df12e221a835a4504e4ce0a30e5aed17a4e906c9bc2e1bffcd4113adf0f0a1e`. The publisher calls the file Table S2 although its internal header says Table S1. Actual sheet names and physical row addresses identify the evidence used. BOLD was not independently revalidated, the Smith paper was not read in its entirety, and neither population-wide host effects nor taxon equivalence was inferred from its contextual examples.
