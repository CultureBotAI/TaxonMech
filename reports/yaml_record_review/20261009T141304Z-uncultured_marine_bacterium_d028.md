# YAML Record Review: uncultured marine bacterium D028

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_marine_bacterium_d028.yaml`
- Started UTC: 2026-10-09T14:09:29Z
- Finished UTC: 2026-10-09T14:13:04Z
- Verdict: pass

## Target

The complete 39-line generated `TaxonRecord` denotes `NCBITaxon:103675`, uncultured marine bacterium D028. Its NCBI rank is `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:150608`, genetic code 11, grounding `EXACT` and lifecycle `SEEDED`. It has five lineage entries, no synonyms or cross-source mappings, zero inventoried strains, one NCBI name attestation and one seed event. This is an environmental clone taxon, not a cultured strain or a formally established species name.

`data/taxa/PATHS.tsv:15142` pins the filename; `curation/seed_scope.tsv:144184` admits the taxon on 2026-09-13. The record is read-only generated output. Any future source or emission correction belongs in the maintained extraction/seeding implementation, not this YAML.

## Validation

Both commands ran with `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1`:

- `just validate data/taxa/bacteria/uncultured_marine_bacterium_d028.yaml`: exit 0, no issues.
- `just validate-strict data/taxa/bacteria/uncultured_marine_bacterium_d028.yaml --out /private/tmp/taxonmech-d028-20261009-validation.tsv`: exit 0, one file, zero errors. The output TSV was read and contains only its header.

Structured, read-only comparisons independently checked the complete ancestor chain, parent, rank, label, genetic code, source-name attestation, scope reason, filename and seed-event text against the actual inventories. Own-taxon searches found no children, type-material rows, merged IDs or dropped rows. These checks are not the corpus reproduction gate.

Not checked: `just verify-corpus`, `just qc`, all-record schema/tests, provenance hashes and rendered products. The inspected `scripts/verify_corpus.py` exposes no record selector; `--max-diffs` limits display, not verification scope. This individual review does not claim a full-corpus result. `just validate-products` is inapplicable: the record has no curator-grounded graph nodes and the configured OAK gate excludes NCBITaxon identities. There is no target history file to pass to `just validate-history`; the embedded event passed schema validation. No history entry was created.

## Identity and Grounding

The complete source backbone row at `data/raw/ncbitaxon_taxa.tsv:18540` and source-native scientific-name row at `data/catalog/ncbi_names-0000.jsonl.gz:38556` agree with the YAML. The source has no synonym for this taxon. Fresh [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103675&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103675) independently confirm the label, species rank, parent, code and lineage. Datasets includes the root; XML names the intervening ancestors explicitly. The YAML correctly carries root, cellular organisms, Bacteria, environmental samples and marine bacteria D ensemble in that order.

`EXACT` means that this record identifies the NCBI concept. It does not turn the environmental clone into a cultivated type strain or a validly published name. The broad environmental placement is NCBI's, not a missing TaxonMech inference.

## Evidence

The NCBI attestation is supported exactly: source ID `NCBITaxon:103675`, the same label, one `NAME`, and the 2026-09-13 taxonomy snapshot. No trait, medium, culture or genome claim is emitted.

A fresh exact-taxon nucleotide query, `txid103675[Organism:noexp]`, returned one sequence, UID 5882277. Its complete [GenBank XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=5882277&rettype=gb&retmode=xml) identifies **AF177562.1**, a 559-base partial 16S rRNA sequence, with clone D028, `taxon:103675`, an environmental-sample flag and surface-associated marine context. The complete sequence contains 559 A/C/G/T bases and equals the submitted rRNA transcription after case normalization; this is annotation consistency, not an independent phylogenetic analysis. The record is a marker sequence, not a genome assembly.

The sequence cites PMID 10653705. Fresh PubMed metadata and its complete abstract resolve that citation to DOI 10.1128/AEM.66.2.467-475.2000 and PMC91850. The primary publisher's abstract, methods, accession statement, Table 1 and relevant results were inspected. D028 has reported clone-library frequencies of 5.5% for BR-72, 4.6% for PEG-S-24, 1.9% for PEG-M-24, 1.8% for PEG-M-72 and 2.0% for PU-24. These are ARDRA-pattern frequencies within the respective libraries, not direct organism abundance, an isolate assay or proof of polymer degradation. The deposited accession lies within the study's stated sequence series. This supports the clone context without replacing NCBI's carried lineage. [Dang and Lovell, primary study](https://journals.asm.org/doi/10.1128/aem.66.2.467-475.2000).

## Completeness

An ignored-inclusive, compressed-file-aware `rg --no-ignore --hidden -n -z -i` search covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, using the exact taxon number with numeric boundaries, full label, slug and bounded clone label. All 60 candidate rows were subsequently read in full with structured TSV/JSON readers. An accession/UID expansion found three additional rows, also fully read. Source metadata were separately parsed from all five `SOURCE.json` files; history and target/report filename inventories included ignored files. These are bounded searches of local retained evidence, not a claim that no other evidence exists worldwide.

No own-taxon LPSN, GTDB, BacDive, GOLD, MediaDive, Madin or BactoTraits inventory row, eligible strain/genome chain, SeqCode identity or separate target history was found. Important rejected collisions were:

- BacDive 103675 is Rhodococcus sp. ST000623, taxon 194249 (`data/bacdive/records.jsonl.gz:27796`), not NCBITaxon 103675.
- CIP 103675 belongs to Enterococcus columbae, species 1355 and strain 1121865, BacDive 5328, StrainInfo 2245/deposit 150567. Complete native strain, deposits and sequence provenance were read; none links to the marine clone. Its LPSN name and type-material entries are not D028 nomenclature.
- NBRC 103675 belongs to the Methanosaeta/Methanothrix source group, species 2223 and strain 990316, BacDive 23083, StrainInfo 47744/deposit 802484 and GOLD Go0198679. Source naming/type-status differences within that unrelated group were retained as context, not resolved or imported here.
- StrainInfo deposit 103675 is ATCC 25133, Mycobacterium avium subsp. avium, taxon 44454 and SI-ID 38372 (`data/straininfo/records.jsonl.gz:26768`). A deposit number is not a taxonomy identifier.
- Flavobacteriales endosymbiont of Aoinidomytilus ceanothi D028 is taxon 404064, independently retained in the backbone and native names. E. coli d028-11/d028-33 assemblies GCA_014079245.1/GCA_014080505.1 and the UUID-bearing Marinobacter assembly GCA_965212585.1 likewise have different identities.
- Other hits are GTDB assembly statistics, the MGBC103675 metagenome, Salmonella PNUSAS103675, Enterobacter sequence CP103675, ATB run DRR103675 or hash substrings. Full native records establish the different taxon/sample/accession namespaces.
- The expanded UID search finds Staphylococcus aureus sample SAMEA5882277 and its ATB entry, plus a Klebsiella assembly with genome length 5882277. Neither is the nucleotide UID 5882277. No local AF177562 accession entry was found within the stated search roots.

Zero inventoried strains is therefore supported, not a listing cap. Empty optional definitions, literature, genomes and causal graphs do not constitute defects under the seeded-record contract. AF177562.1 is a useful future evidence lead, but an unrequested marker-sequence import is not a missing required genome link. iModulonDB is not applicable to the current taxonomy-only claims; there is no gene/regulator/module assertion to check.

## Findings

None found in the reviewed record's current claims.

Counts: 0 blocker, 0 major, 0 minor.

## Recommended Edits

No corrective edit is required. Preserve the identifier, source-carried lineage, zero strain count and `SEEDED` status. Do not join numeric or clone-label collisions.

Optional future enrichment could preserve AF177562.1 and its primary citation as explicitly scoped clone/marker evidence. It must be implemented through a maintained source importer or supported curator overlay and seeder, with a test; never hand-edit this generated YAML or create a fictitious culture deposit. The current source identity is owned by `src/taxonmech/ncbi_taxdump.py`, with emission in `src/taxonmech/seed.py`.

## Follow-up Checks

For any later authorized source change, verify the exact `taxon:103675` and clone D028 qualifiers at NCBI, retain the accession version, distinguish partial 16S evidence from an assembly, and exclude the unrelated numbered deposits and D028 labels above. Rerun both focused validators. A future emission change requires an inspected canary followed by the repository's full reproduction and QC gates; none was run or substituted here.

## Additional Notes

Record SHA-256 at review start: `d2ab6fd80bcdaaa5b78c1a9e2689b5e2501cea2ff5540fbd1d25d2b7e17f6d04`. Worktree HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The seed timestamp 2026-09-13T17:54:04Z agrees with the newest of the three manifests read by `src/taxonmech/seed.py:_seed_timestamp`, specifically the ATB manifest; it is not the date of this review. The event text agrees with the scope and sole NCBI source.

This report was independently authored for D028 after reading its own record, primary sequence and source collisions. No neighboring report supplied its verdict. Only this new report was added; no records, history, scope, sources, pages, lifecycle status, GitHub state, branches or worktrees were changed. Eukaryota was not reviewed or modified.
