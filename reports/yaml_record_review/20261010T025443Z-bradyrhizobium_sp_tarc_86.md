# YAML Record Review: Bradyrhizobium sp. TARC 86

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bradyrhizobium_sp_tarc_86.yaml`
- Started UTC: 2026-10-10T02:52:06Z
- Finished UTC: 2026-10-10T02:54:43Z
- Verdict: pass

## Target

The entire 54-line generated `TaxonRecord` was read. `NCBITaxon:103741` denotes Bradyrhizobium sp. TARC 86, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2631580`, genetic code 11, grounding `EXACT` and mapping status `SEEDED`.

It contains ten ancestors, zero inventoried strains, one NCBITAXON name attestation and one seed event. It asserts no formal species name, synonym, GTDB mapping, culture deposit, genome, phenotype or causal graph. The space-separated TARC 86 designation is retained exactly as NCBI supplies it.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/bradyrhizobium_sp_tarc_86.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/bradyrhizobium_sp_tarc_86.yaml --out /private/tmp/taxonmech-tarc86-20261010-validation.tsv --workers 1`: one file, zero errors; output reread, header only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons verified identity, every ancestor, code, empty source synonyms, own source inventories, index/scope resolution, attestation and exact seed reason. Complete backbone scanning found no immediate child. Own type-material, merged-ID and dropped-record inventories had no rows.
- The complete native NCBI name row and relevant culture-inventory collision rows were read. Native candidate identities and all matching fields were inspected. Live NCBI taxonomy, nucleotide and PubMed responses were read, including complete marker annotations and a sequence-length/alphabet/hash check.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, source replay, rendering and publication gates. No graph is present for `just validate-products`. Focused agreement is not proof of full corpus reproduction.
- The taxonomy and nucleotide browser pages were unavailable through the web reader; structured NCBI APIs succeeded. Only the linked paper's abstract and bibliographic metadata were inspected, not its full strain-level tables.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18567`, [NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103741&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103741) agree on the exact label and species rank. EFetch confirms parent 2631580 and code 11. Datasets includes root 1.

The complete root-first lineage agrees with the backbone: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Alphaproteobacteria, Hyphomicrobiales, Nitrobacteraceae, Bradyrhizobium and unclassified Bradyrhizobium. The unclassified parent correctly has `NO_RANK`; no named species should be inserted beneath the genus without additional taxonomic evidence.

The full native row `data/catalog/ncbi_names-0000.jsonl.gz:38626` is the scientific name with an empty unique-name qualifier. The backbone synonym fields and live EFetch alternate-name surface supply no synonyms. NCBI species rank for this isolate-labelled entry does not establish a formally published species. `EXACT` means identity with this NCBI entry, not identity with B. japonicum or any other named species.

## Evidence

The live nucleotide query `txid103741[Organism:exp]` returned one record, UID 5881556. Its complete GenBank annotations resolve to [D85406.1](https://www.ncbi.nlm.nih.gov/nuccore/D85406.1), a 264-base partial 16S rRNA sequence. The source explicitly names TARC 86 and `taxon:103741`; the sequence is 264 bases of A/C/G/T. The rRNA feature is partial at both ends and carries a non-experimental inference note. This supports a bounded marker link, not a complete rRNA gene, whole genome or experimental phenotype.

The sequence record links [PMID 10528395](https://pubmed.ncbi.nlm.nih.gov/10528395/), DOI `10.1139/w99-061`, a 1999 study by Ando and Yokoyama. Its abstract describes RFLP and partial 16S comparisons between Thai soybean bradyrhizobia and USDA strains. It reports shared partial-marker sequences among several differently designated strains. That context does not make the strains identical or provide a current species reassignment for TARC 86. The inspected abstract does not enumerate TARC 86's individual experimental results, so no strain-specific nodulation or nitrogen-fixation assertion is inferred here.

The Datasets taxonomy response omits an assembly-count field. That is not an explicit zero-assembly result. The repository search established no eligible own genome join, and the YAML correctly does not turn the partial marker into one.

The one-NAME source attestation matches the 2026-09-13 NCBI snapshot. It is a name-coverage count, not a culture count, experimental result or assertion that only one sequence exists historically.

## Completeness

Ignored-inclusive, compressed-content-inclusive `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, using bounded taxon ID, full label, slug and TARC 86 variants. Forty-three source lines matched. The source-native candidates and projected-link matches were inspected for identity; numeric coincidences were excluded.

In particular, BacDive 103741 is Rhodococcus ST002191, taxon 194249, not NCBITaxon 103741. DSM 103741 is Methylorubrum rhodesianum, taxon 29427; CIP 103741 is Moraxella bovis, taxon 476. StrainInfo deposit 103741 belongs to Myxococcus fulvus, taxon 33. Their corresponding culture and projected-link rows preserve these different identities. Other matches include unrelated sequence-accession suffixes, numeric strain/isolate names and N50/N75/N90 values. None establishes a TARC 86 deposit or genome.

Complete structured scans found no own BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row. This is bounded repository coverage, not a global biological absence claim. Five independently enumerated SOURCE.json files were parsed; the BacDive metadata match refers to the unrelated BacDive identifier above. Ignored-independent filename scans found exactly the target YAML, no prior target report and no target-specific history filename.

`strain_count: 0` reflects the represented inventory, not proof that the isolate cannot be cultured. Optional nomenclature, culture deposits, genomic links and graphs need not be invented. iModulonDB is not applicable to the taxonomy/name assertion; the paper's mention of genes does not create a gene or expression-module assertion in this record.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected assertion scope. The record faithfully preserves the supported NCBI identity and unresolved named-species placement without importing evidence from numeric lookalikes.

## Recommended Edits

None required. Leave the generated YAML, seed status and history unchanged.

Any separately authorized marker enrichment belongs in a maintained source inventory or supported extraction/seeding extension before regeneration. Preserve `D85406.1`, its partial-sequence scope and explicit taxon/strain linkage. Do not merge strains because they share a short 16S sequence, or normalize culture/sequence numbers into taxon identifiers.

## Follow-up Checks

If a named-species reassignment, culture deposit, genome or phenotype is proposed, verify exact target linkage at its primary authority and inspect the relevant strain-level evidence. Read the full paper before importing an individual experimental outcome. Retain full culture identifiers and accession versions.

After maintained input changes, rerun the documented canary, schema/strict/history checks and full corpus reproduction/QC gates. No curator correction is needed for the current NCBI-only record.

## Additional Notes

- YAML SHA-256: `09c89ea049dee2e0101c33ad950992318674e451fc04c84e511ef35e2a2316e1`.
- D85406.1 lowercase sequence SHA-256: `6c136c342929709ae1f7d33e6f023cd8c3c1e52eee5c0e4ec77e803e0670fa6d`.
- `data/taxa/PATHS.tsv:15299` and `curation/seed_scope.tsv:144201` uniquely resolve the target. The seed event retains 2026-09-13T17:54:04Z and the exact NCBITAXON-only scope reason.
- Read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Only this new report was added for this target. No tracked record, input, schema, history, page, branch, worktree or GitHub state changed. No Eukaryota YAML was opened or review status promoted.
