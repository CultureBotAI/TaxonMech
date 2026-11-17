# YAML Record Review: uncultured marine bacterium D030

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_marine_bacterium_d030.yaml`
- Started UTC: 2026-10-09T14:20:13Z
- Finished UTC: 2026-10-09T14:22:34Z
- Verdict: pass

## Target

The entire 39-line generated `TaxonRecord` was read. It identifies `NCBITaxon:103677`, uncultured marine bacterium D030, with rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:150608`, genetic code 11, `EXACT` grounding and `SEEDED` lifecycle. It carries five ancestors, one NCBI name attestation, zero inventoried strains and one seed event. No synonyms, nomenclature, mappings, genome links or mechanism assertions are emitted.

This is the NCBI environmental clone concept, not culture accession 103677. The unique filename is pinned by `data/taxa/PATHS.tsv:15144`; `curation/seed_scope.tsv:144186` records admission on 2026-09-13. The YAML remains generated, read-only output.

## Validation

The following commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1`:

- `just validate data/taxa/bacteria/uncultured_marine_bacterium_d030.yaml`: exit 0; no issues.
- `just validate-strict data/taxa/bacteria/uncultured_marine_bacterium_d030.yaml --out /private/tmp/taxonmech-d030-20261009-validation.tsv`: exit 0; one file, zero errors. The complete TSV was read and contains only the header.

Structured source comparisons verified the full carried ancestor chain, parent, rank, label, genetic code, exact source-name attestation, filename, scope reason and seed-event text. Own-taxon scans returned no child, merged ID, dropped row or type-material row.

Not checked: `just verify-corpus`, `just qc`, the full test suite, corpus-wide schema validation, provenance hashes and rendered products. The inspected reproduction command has no record selector; `--max-diffs` limits output, not work. The bounded comparisons above are not a substitute for that gate. `just validate-products` is inapplicable to this record: there are no curator-grounded graph nodes, and NCBITaxon identity is excluded from its OAK targets. No separate target history file was found for `just validate-history`; the embedded event passed schema validation. No new history event or status promotion was made.

## Identity and Grounding

The full backbone row at `data/raw/ncbitaxon_taxa.tsv:18542` and native scientific-name entry at `data/catalog/ncbi_names-0000.jsonl.gz:38558` support the exact ID and label. Their synonym fields are empty. Fresh [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103677&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103677) confirm the species rank, parent, code and identity. The root-first chain is root, cellular organisms, Bacteria, environmental samples, marine bacteria D ensemble. Datasets supplies the root-inclusive IDs; taxonomy XML supplies the remaining names and ranks.

`EXACT` is appropriate for identification with that NCBI concept. It does not establish a cultivated organism, validly published species name or equivalence to a cultured sequence neighbor. The environmental placement is faithfully carried from the authority and is not a TaxonMech inference to repair.

## Evidence

The sole emitted attestation is correct in both identity and unit: `NCBITAXON`, source ID `NCBITaxon:103677`, D030's full label, one `NAME`, snapshot 2026-09-13. It is not a genome or phenotype count.

An independent exact-taxon nucleotide query, `txid103677[Organism:noexp]`, returned one sequence, UID 5882279. Its complete [GenBank XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=5882279&rettype=gb&retmode=xml), including all features and sequence, identifies **AF177564.1**, a 559-base partial 16S rRNA record. Its own source feature names clone D030, `taxon:103677`, an environmental sample and surface-associated marine context. The actual sequence has 559 A/C/G/T bases, matching the declared length and submitted transcription after case normalization. This checks source annotation consistency, not an independently inferred phylogeny. A partial marker is not an assembly or culture deposit.

The sequence's PMID 10653705 was freshly resolved via PubMed's complete abstract and identifiers to DOI 10.1128/AEM.66.2.467-475.2000 and PMC91850. The primary Table 1 gives D030 clone-library frequencies of PVA-24 1.9%, PVA-72 5.3%, BR-72 1.8%, PEG-S-24 1.5% and PU-24 2.0%. These are ARDRA-pattern frequencies within libraries, not direct abundance or evidence of a cultured isolate's polymer degradation. [Primary study and table](https://journals.asm.org/doi/10.1128/aem.66.2.467-475.2000).

## Completeness

An ignored-inclusive search used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. The terms covered bounded taxon digits, full label, slug and bounded D030. All 42 candidate rows were then read in full with structured TSV/JSON readers, including compressed native records. A second search for AF177564 and bounded UID 5882279 returned no rows within the same roots. All five source metadata JSON files were parsed separately; filename and history inventories also included ignored files.

No own-taxon BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row, eligible genome/deposit chain, SeqCode identity or separate target history was found in that bounded local search. The following collisions were explicitly resolved:

- BacDive 103677 is Rhodococcus sp. ST000628, taxon 194249 (`data/bacdive/records.jsonl.gz:27798`). The BacDive integer does not identify this NCBI taxon.
- CIP 103677 belongs to the Aeromonas trota/enteropelogenes source group, taxon 29489, BacDive 249, StrainInfo 7843/deposit 148468. The complete BacDive and StrainInfo rows, including every sequence/deposit attribution, were read. Their nomenclatural and type-status differences remain source context for that other taxon, not D030 evidence.
- NBRC 103677 belongs to Methylomicrobium/Methylotuvimicrobium japanense, taxon 81932, BacDive 134303, strain NI, GOLD Go0025289 (`data/gold/organisms.jsonl.gz:21502`). Neither its type material nor GOLD organism association transfers to D030.
- StrainInfo deposit 103677 is ATCC 25136, Mycobacterium xenopi, taxon 1789, SI-ID 38374. The separate yeast row SI-ID 64505 matches through accession KY103677, with CBS 2685 and taxon 36907. Reading that native collision did not reopen the completed Eukaryota record review.
- CP103677 is a Klebsiella pneumoniae 2946 sequence associated with GCA_024918095.1, SAMN28174011, BV-BRC 573.50478/573.50851 and GOLD Ga0608820. It is not a taxonomy identifier.
- Pseudomonas GCA/GCF_001036775.1 has assembly name ASM103677v1, taxon 287 and strain Pae_CF67.12q. MGBC103677 is the Duncaniella metagenome GCA_948860845.1, taxon 2768039. MarMAG_103677 is GCA_977592725.1, taxon 77133. Complete source records distinguish all three from this clone.
- Salmonella PNUSAS103677 has GCA_008804295.1 and taxon 28901; E. coli isolate 103677 has GCA_012478775.1 and taxon 562. ATB DRR103677 belongs to E. coli sample SAMD00076020; the remaining ATB hits are sequence-hash substrings on other samples.

The absence of own/descendant BacDive support supports the zero strain count; no cap was hiding strains. Optional definition, literature, datasets, discussions and causal graphs need not be fabricated to fill empty slots. AF177564.1 is useful potential clone evidence, not a missing required genome link. iModulonDB is not applicable to the taxonomy-only record, which asserts no gene, regulator, trait or expression module. The searches do not prove global absence of additional biological evidence.

## Findings

None found in the record's current claims.

Counts: 0 blocker, 0 major, 0 minor.

## Recommended Edits

No corrective edit is required. Preserve the exact NCBI identity, source-carried lineage, zero inventoried strain count and `SEEDED` status.

Optional future enrichment could retain AF177564.1 as a partial-marker reference with the exact clone and taxon qualifiers. That would require maintained importer/overlay and seeder support with a focused test, not a hand edit to this YAML or an inferred culture link. NCBI identity projection is maintained in `src/taxonmech/ncbi_taxdump.py`; emission is maintained in `src/taxonmech/seed.py`.

## Follow-up Checks

For any later authorized enrichment, resolve AF177564.1 at NCBI, preserve its version and marker scope, and reject the unrelated numbered deposits and accession substrings listed above. Rerun both focused validators. An actual generator change also requires an inspected canary and the full `just verify-corpus` and `just qc` gates. No regeneration or corpus-wide success is claimed by this review.

## Additional Notes

Record SHA-256 at start: `57dd6714fb1b63a8f22181a640a918ca8c189f633bb97f398caa19c4637898c4`. HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The embedded event's 2026-09-13T17:54:04Z timestamp agrees with the newest source manifest chosen by the inspected `src/taxonmech/seed.py:_seed_timestamp`, specifically ATB. The event's action, curator and source/scope text are consistent; it does not claim human review.

This independent D030 review used its own complete YAML, live taxonomy, primary sequence and candidate-source reads, not another record's verdict. Only this new report was written. No record, history, scope, source, page, lifecycle status, GitHub state, branch or worktree was changed; Eukaryota records remained untouched.
