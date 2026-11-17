# YAML Record Review: Photobacterium sp. squidInt_03

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/photobacterium_sp_squidint_03.yaml`
- Started UTC: 2026-10-07T01:12:09Z
- Finished UTC: 2026-10-07T01:15:55Z
- Verdict: pass

## Target

Reviewed the entire generated `TaxonRecord` for `NCBITaxon:1035396`, label `Photobacterium sp. squidInt_03`, rank `SPECIES`, domain `BACTERIA`. The record has `grounding_status: EXACT`, `mapping_status: SEEDED`, genetic code 11, zero associated strain records, one NCBITAXON NAME attestation, and one seed event. It has no synonym, nomenclature, taxonomy-mapping, deposit, genome, literature, phenotype, or causal-graph assertions.

Generated YAML is read-only. Future identity or evidence corrections belong in the maintained source inventories, upstream transforms, or seeder; scope changes belong in `curation/seed_scope.tsv`. This review creates only this report.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/photobacterium_sp_squidint_03.yaml`: exit 0, no issues found.
- `python scripts/validate_strict.py data/taxa/bacteria/photobacterium_sp_squidint_03.yaml --out /private/tmp/psqi03-strict.tsv`: exit 0, one file scanned, zero ERROR rows. Read the actual TSV; it contains only its header.
- Read the complete target and compared its fields with its own backbone, scope, path-index, and source rows. All ten lineage entries agree with the pinned parent chain. These are bounded comparisons, not a reproduction gate.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, provenance hashes, generated-site drift, and the full test suite. Their results are not inferred from this individual review.
- Not checked: corpus-wide `just validate-products` and `just validate-history`. This target adds no curator-grounded graph nodes and no external history artifact matched the bounded search. The inline seed event was schema-checked and inspected; no history artifact or status promotion was created.

## Identity and Grounding

The full row at `data/raw/ncbitaxon_taxa.tsv:222058` agrees with the target's identifier, label, rank, parent `NCBITaxon:2628852`, genetic code, empty synonym sets, and 2026-09-13 taxonomy snapshot. `data/catalog/ncbi_names-0005.jsonl.gz:31538` independently retains the exact scientific-name row.

Inspected the complete current [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035396&retmode=xml) and [NCBI Datasets taxonomy response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035396). Both resolve this identifier to the exact label and species rank; the XML confirms parent 2628852 and code 11. The lineage agrees from root through cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Vibrionales, Vibrionaceae, Photobacterium, and unclassified Photobacterium. Datasets includes root explicitly.

The isolate designation does not justify changing NCBI's rank to strain or assigning this unidentified species a named-species synonym. EXACT denotes this identifier match, not formal nomenclatural standing or equivalence to another Photobacterium isolate. No alternate name or type-material assertion appears in the inspected taxonomy XML. Exact target lookups in the pinned type-material, merged-ID, and dropped inventories returned no rows.

## Evidence

- `data/taxa/PATHS.tsv:14549` identifies the target slug; `curation/seed_scope.tsv:322329` supplies the 2026-09-13 addition and NCBI attestation reason reproduced by the seed event.
- The single NCBITAXON attestation has the correct source identifier, exact label, count 1, unit NAME, and snapshot. Exact-target rows in the BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, and BactoTraits inventories are empty. No child taxon was found in the pinned backbone. Zero associated strain records is not a claim that the isolate lacks a biological strain designation.
- Inspected the manifest timestamp fields and `src/taxonmech/seed.py:139` through its timestamp-selection logic. The seed event's 2026-09-13T17:54:04Z agrees with the maximum source timestamp: raw 17:50:44Z, AllTheBacteria 17:54:04Z, and StrainInfo 17:29:00Z. Manifest hashes were not recomputed.
- Exact NCBI `txid1035396[Organism:noexp]` searches returned zero Assembly records, with a phrase-not-found warning, and one nucleotide record, UID 333797999. Inspected all returned nucleotide metadata, references, and features, excluding sequence bases. [JF792717.1](https://www.ncbi.nlm.nih.gov/nuccore/JF792717.1) is a 1,251-base partial 16S rRNA sequence explicitly assigned to taxon 1035396 and strain squidInt_03. It is not a genome or assembly. Its source qualifiers give host `Nototodarus gouldi` verbatim and locality `New Zealand: North Island, Auckland Fish Market`; they do not explicitly identify an anatomical isolation site. No BioSample, BioProject, assembly, or culture-deposit identifier is present in this sequence metadata.
- The sequence's research reference names Wollenberg, Rainey, and Ruby and is marked Unpublished; it supplies no DOI or PMID. Its separate Wollenberg/Ruby direct-submission entry is dated 07-APR-2011 at the University of Wisconsin, Madison. A bioluminescence-related study title is not an isolate-level phenotype measurement or experimental result.
- The independent [NCBI genome Datasets response](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035396/dataset_report) was an empty object. Together with the bounded inventory and exact-taxonomy checks, this supplies no supported target assembly to add; it does not prove no genome exists anywhere under another identity.
- Rejected an apparent catalog hit after reading its entire row at `data/catalog/ncbi_genbank-0015.jsonl.gz:14812`: `GCA_016782545.1` is a Candidatus Microgenomates bacterium assembly for taxon 2093373, isolate BS750m-G73. The value 1035396 occurs in genome-size fields, not its taxon identifier. Its BioSample and BioProject cannot be transferred to this target.
- Before open-web discovery, successfully ran `uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets` and inspected all 28 dataset rows. None covers Photobacterium. The Vibrio natriegens datasets are not transferable; iModulonDB is not applicable and its absence is not negative biological evidence.
- Bounded web discovery covered the exact label, hyphenated and space-separated designations, accession JF792717, author/designation combinations, the sequence research title, and genome/strain terms. Results were taxonomy listings or unrelated leads; no inspected exact-isolate publication supplied a missing experimental assertion. This is not an exhaustive literature census.

## Completeness

Gitignore-independent, hidden-file-inclusive, compressed-content searches used `rg --no-ignore --hidden -n -z -i` for the target ID, label, slug, and squidInt designation variants within `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. All four matching rows were read: backbone, scope, native scientific name, and the rejected genome-length collision. Separate structured reads covered all five SOURCE.json metadata files; history filenames were also checked without ignore filtering.

A second search over the same bounded roots for JF792717 and its version returned zero matching content lines. Separate SOURCE.json and history-filename checks likewise returned no accession match. These bounds do not include all external repositories, every downloadable source snapshot, or arbitrary differently named evidence.

An ignored-inclusive review-directory filename search found no earlier report for this target before this report was added. Empty optional nomenclature, mapping, strain/deposit, genome, and graph slots are consistent with the inspected sources. The partial marker sequence and source qualifiers are possible future typed enrichment, not missing required genome or phenotype assertions. Do not infer intestine from the designation, normalize the host spelling without a separate authority check, or borrow the neighboring squid isolates' evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the individual review's evidence bounds. The minimal seed record accurately represents its supported identity, NCBI lineage, count, source attestation, and seed event. Passing this review does not certify full-corpus reproducibility or complete global source coverage.

## Recommended Edits

None required. Leave the generated YAML and SEEDED lifecycle status unchanged.

Optional future enrichment of JF792717.1 would require a maintained upstream input and supported typed representation that preserves its nucleotide-marker identity and exact source linkage. It must not populate genome counts, manufacture culture-deposit equivalence, or derive an experimental phenotype from a title. No such implementation is authorized by this review.

## Follow-up Checks

If a maintained source input changes, verify the exact taxon and any strain/deposit-to-sequence chain at its authority, rerun schema and strict validation for this target, and run the documented full-corpus reproduction and QC gates before claiming corpus-wide correctness. Route any generator or identity-mapping correction through its owning upstream input or seeder, with focused regression tests.

For future phenotype or habitat enrichment, inspect an actual isolate-specific primary source and retain its measured scope, conditions, source qualifiers, and publication status. Unresolved coverage remains bounded by the local roots and live queries described above, not an identified blocker.

## Additional Notes

Review performed on branch `codex/record-review-extensimonas-20261003`, HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The other session is closed; the existing checkout was retained without creating another worktree. No record, inventory, prior report, generated page, history artifact, GitHub item, or Eukaryota record was changed. No paid research or external contact occurred.
