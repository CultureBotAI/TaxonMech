# YAML Record Review: Photobacterium sp. squidInt_04

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/photobacterium_sp_squidint_04.yaml`
- Started UTC: 2026-10-07T01:17:50Z
- Finished UTC: 2026-10-07T01:20:45Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1035397`, `Photobacterium sp. squidInt_04`. It carries SPECIES rank, BACTERIA domain, parent 2628852, genetic code 11, EXACT grounding, SEEDED mapping status, zero associated strain records, one NCBITAXON NAME attestation, and one seed event. It makes no synonym, nomenclature, taxonomy-mapping, deposit, genome, literature, phenotype, or causal-graph assertion.

The generated YAML is read-only. Any future fix belongs in the maintained inventories, their upstream transforms, the seeder, or `curation/seed_scope.tsv`, according to ownership. This review adds only this report.

## Validation

The following commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/photobacterium_sp_squidint_04.yaml`: exit 0, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/photobacterium_sp_squidint_04.yaml --out /private/tmp/psqi04-strict.tsv`: exit 0, one file scanned and zero ERROR rows. Read the actual TSV; only its header is present.
- Read and compared the target's own backbone, source, scope, and index rows. Every lineage entry agrees with the pinned parent chain. These bounded comparisons are not a corpus reproduction check.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, source provenance hashes, generated-site drift, and the complete test suite. No focused substitute or corpus-wide result is claimed.
- Not checked: corpus-wide `just validate-products` and `just validate-history`. There are no curator-grounded graph nodes in this target; bounded history searches returned no target artifact. The inline event was schema-checked and inspected, without creating an external history entry or promoting status.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:222059` agrees with the identifier, exact label, SPECIES rank, parent `NCBITaxon:2628852`, genetic code 11, empty synonym fields, and 2026-09-13 snapshot. The complete native scientific-name row is at `data/catalog/ncbi_names-0005.jsonl.gz:31539`.

Inspected the full [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035397&retmode=xml) and [Datasets taxonomy response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035397). The exact name, rank, parent, bacterial domain, and genetic code agree. The root-first lineage is 1, 131567, 2, 3379134, 1224, 1236, 135623, 641, 657, 2628852, with the same labels and ranks as the YAML. Datasets explicitly includes root.

An isolate-style label does not authorize replacing NCBI's species rank with strain rank, assigning a named-species synonym, or asserting nomenclatural standing. EXACT is an identity match, not genome or deposit equivalence. The inspected taxonomy XML supplies no alternate name or type designation; exact target lookups in the pinned type-material, merged-ID, and dropped inventories returned no rows.

## Evidence

- `data/taxa/PATHS.tsv:14550` resolves the identifier to this slug. `curation/seed_scope.tsv:322330` records the 2026-09-13 scope addition and NCBI attestation reason copied into the event.
- The single attestation correctly retains count 1, unit NAME, exact source identifier and label, and snapshot. Exact-target rows in the BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, and BactoTraits inventories are empty. The pinned backbone contains no child taxon. A zero associated-strain count does not deny the isolate designation.
- Manifest timestamp fields read this turn are raw 2026-09-13T17:50:44Z, AllTheBacteria 2026-09-13T17:54:04Z, and StrainInfo 2026-09-13T17:29:00Z. Inspected `src/taxonmech/seed.py:139` and its maximum-timestamp rule; the seed event at 17:54:04Z is consistent. Manifest hashes were not recomputed.
- Exact `txid1035397[Organism:noexp]` searches returned zero Assembly records, including a phrase-not-found warning, and one nucleotide UID, 333798000. Read the full returned metadata, references, and features, excluding sequence bases. [JF792718.1](https://www.ncbi.nlm.nih.gov/nuccore/JF792718.1) is a 1,251-base partial 16S rRNA sequence explicitly assigned to squidInt_04 and taxon 1035397. It is not a genome or assembly.
- Sequence source qualifiers state host `Nototodarus gouldi` verbatim and locality `New Zealand: North Island, Auckland Fish Market`. They do not explicitly name an anatomical isolation site. No BioSample, BioProject, assembly, or culture-deposit accession appears in this sequence metadata. The research reference names Wollenberg, Rainey, and Ruby, is marked Unpublished, and supplies no DOI or PMID; the Wollenberg/Ruby direct submission is dated 07-APR-2011 at the University of Wisconsin, Madison. The research title alone does not establish bioluminescence measurements for this isolate.
- The independent [genome Datasets response](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035397/dataset_report) was an empty object. The checked sources supply no target assembly link; this is not a claim that no genome exists elsewhere under another identity.
- Before open-web discovery, ran `uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets`. The sandboxed attempt failed DNS resolution; a read-only network-authorized retry succeeded. Inspected all 28 dataset rows. No Photobacterium dataset is listed; Vibrio natriegens coverage is not transferable. iModulonDB is not applicable, not negative biological evidence.
- Web discovery used exact label/designation variants, JF792718, author/designation combinations, the sequence research title, and genome/strain terms. Taxonomy listings did not add biological assertions. A patent lead was inspected separately as described below; no inspected exact-isolate experimental publication justified a new phenotype assertion.

The primary patent text [US20180286520A1](https://patents.google.com/patent/US20180286520A1/en) names squidInt_04 in large microbiome-feature lists, including claims 23, 24, and 25 concerning mouth, nose, and skin features in a sleep-quality method. After the web reader rejected the oversized document, a read-only HTML parse searched the full text and inspected target-containing table rows, claim preambles, and target contexts. JF792718 was not found in the full parsed text. These passages do not establish that this exact isolate was recovered from those human sites, tested for a phenotype, or causally linked to sleep quality. Do not import such claims as demonstrated isolate biology. This was a bounded identity/evidence check, not a complete patent-family or statistical-method review.

## Completeness

A gitignore-independent search used `rg --no-ignore --hidden -n -z -i` for the target ID, label, slug, and designation variants in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. All three matching rows were read: backbone, scope, and native scientific name. All five SOURCE.json files were separately parsed in full and history filenames were checked without ignore filtering; no target match was found there.

A second search for JF792718 and its version over the same roots returned zero content matches; separate metadata and history-filename checks also returned none. These bounds do not include all external repositories or every downloadable source snapshot. The ignored-inclusive review-directory filename search found no earlier report for this target before this report was added.

Empty optional slots are consistent with the inspected sources. The marker and host/locality qualifiers could support future typed enrichment, but do not constitute missing required genome assertions. Do not infer an anatomical site from Int, alter host spelling without a separate authority check, or borrow another squid isolate's data. The patent name lists are not missing required phenotype evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within this individual review's bounds. The minimal record faithfully carries its supported identity, NCBI lineage, source count, attestation, and seed event. Pass does not certify full-corpus reproduction, patent claims, or globally exhaustive source coverage.

## Recommended Edits

None required. Leave generated YAML and SEEDED status unchanged.

Optional future JF792718.1 enrichment would need an owned upstream input and supported typed representation preserving nucleotide-marker identity and exact linkage, outside genome counts. Any phenotype enrichment requires inspected isolate-level evidence, not a study title or patent taxon list.

## Follow-up Checks

For future upstream changes, reverify the exact taxon and any deposit-to-sequence chain, rerun target schema and strict validation, and run documented full-corpus reproduction and QC gates before asserting corpus-wide correctness. Route fixes through the maintained source or seeder, with focused regression tests.

If the patent lead becomes a proposed biological assertion, inspect the underlying data, classification resolution, and claimed experiment first; the checked name-list contexts do not supply that support. No unresolved blocker was identified.

## Additional Notes

Branch `codex/record-review-extensimonas-20261003`, HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The other session is closed; this review retained the existing checkout. No YAML, inventory, prior report, generated product, history record, GitHub item, or Eukaryota record was changed. No paid research or external contact occurred.
