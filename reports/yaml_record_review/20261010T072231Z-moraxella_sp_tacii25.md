# YAML Record Review: Moraxella sp. TACII25

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/moraxella_sp_tacii25.yaml`
- Started UTC: 2026-10-10T07:16:00Z
- Finished UTC: 2026-10-10T07:22:31Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord` for `NCBITaxon:103760`, Moraxella sp. TACII25. This species-ranked bacterial placeholder has parent `NCBITaxon:2685852`, `EXACT` grounding, `SEEDED` status, genetic code 11, zero inventoried strains, one NCBI name attestation, and one seed event. Maintained inventories and `curation/seed_scope.tsv`, interpreted by extraction/seeding code, own future changes. Generated taxon YAML must not be hand-edited.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/moraxella_sp_tacii25.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/moraxella_sp_tacii25.yaml --out /private/tmp/taxonmech-tacii25-20261010-validation.tsv --workers 1`: one file, zero errors; inspected output TSV contains only its header.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid history links.
- Structured comparisons passed for identifier, exact label, full lineage labels/ranks, synonyms, genetic code, attestation, unique ID/slug, scope reason, and seed-event wording. These are not full corpus reproduction.
- `just validate-products`: not applicable; no curator-added graph or causal assertions. Taxon references were checked directly; no separate documented focused term/reference validator applies.
- Not checked: `just qc`, corpus-wide `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and rendering. Full-corpus gates were not run for this individual read-only review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18568` agrees on ID, exact label, rank, parent, code, and 2026-09-13 snapshot. Exact/related/broad synonym and retirement fields are empty. Individual backbone rows support every label/rank in the full root-first chain: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Gammaproteobacteria 1236; Moraxellales 2887326; Moraxellaceae 468; Moraxella 475; unclassified Moraxella 2685852.

Full live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103760&retmode=xml), [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103760), and [Taxonomy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=103760) agree. All 67 parsed browser text lines were read. EFetch omits root while Datasets includes it. Datasets omits an assembly count; this is not evidence of zero assemblies. The browser exposes taxonomy without a nucleotide link.

The complete native scientific-name row at `data/catalog/ncbi_names-0000.jsonl.gz:38627` agrees. Exact structured scans found no own child, type-material, merged-ID, or dropped-ID rows. `data/taxa/PATHS.tsv:15368` uniquely resolves this identifier/slug. `curation/seed_scope.tsv:144202` supplies the reason reproduced in the 2026-09-13T17:54:04Z seed event.

The historical sequence-attribution conflict below does not invalidate faithful grounding to the still-maintained NCBI identifier. `EXACT` describes that identifier mapping, not independently demonstrated equivalence of TACII25 and TAC125, formal nomenclatural validity, or acceptance of an updated biological classification.

## Evidence

The sole attestation counts one NCBI `NAME`, not a strain, genome, paper, or assay. Structured scans found no own rows in the pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. Empty strain, nomenclature, and mapping sections match those inputs. Zero inventoried strains does not mean no biological isolate exists.

Exact Nucleotide search `txid103760[Organism:exp]` returned zero hits with a phrases-not-found warning. It is not evidence of no historical sequences: explicitly versioned primary records below name the target.

Complete [PubMed metadata and abstract, PMID 11112539](https://pubmed.ncbi.nlm.nih.gov/11112539/) identify Masullo, Arcari, de Paola, Parmeggiani, and Bocchini's 2000 paper, Biochemistry 39(50):15531-15539, DOI [10.1021/bi0018133](https://doi.org/10.1021/bi0018133), on elongation factor Tu from Antarctic Moraxella sp. Tac II 25. Associated data link AJ249258. The abstract describes purified EF-Tu biochemistry and cloning of its encoding gene. This is protein-level evidence, not a whole-cell susceptibility, thermal-tolerance, or species-wide phenotype result. Article full text was not read.

Complete annotations for all three nucleotide versions were inspected:

| Version | Explicit source identity | Sequence/protein annotation | Version history |
| --- | --- | --- | --- |
| [AJ249258.1](https://www.ncbi.nlm.nih.gov/nuccore/AJ249258.1) | Moraxella sp. TACII25, strain TAC II 25, `taxon:103760` | 1,179 bases; tufA/CDS 1..1179; CAB65285.1, 392 aa | Created 7 January 2000; replaced by .2 on 8 May 2001 |
| [AJ249258.2](https://www.ncbi.nlm.nih.gov/nuccore/AJ249258.2) | Moraxella sp. TACII25, strain TAC II 25, `taxon:103760` | 1,413 bases; tufA gene 104..1301, CDS 120..1301; CAB65285.2, 393 aa; PMID 11112539 | Revised submission 4 May 2001; replaced by .3 on 27 June 2003 |
| [AJ249258.3](https://www.ncbi.nlm.nih.gov/nuccore/AJ249258.3) | Current source: Pseudoalteromonas translucida TAC125, strain TAC125, `taxon:326442`; definition still says Pseudoalteromonas haloplanktis | 3,540 bases; rps7/fus/tufA region; tufA gene 2231..3428, CDS 2247..3428; same CAB65285.2 and PMID 11112539 | Revised submission 25 June 2003; replaces .2 on 27 June 2003; record update 15 April 2005 |

Actual lengths agree with declarations and all three nucleotide sequences contain A/C/G/T only. Versions .2 and .3 retain the same 393-aa CAB65285.2 translation, verified by SHA-256. The accession-version chain establishes changed sequence attribution; it does not establish formal synonymy, a taxon merge, entire-strain equivalence, or a genome-assembly relationship. These are gene-region fragments, not assemblies. Submission dates and the Naples laboratory address are not collection dates or locations.

A bounded comparison of full live [taxonomy EFetch for 326442](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=326442&retmode=xml) and [Datasets taxonomy for 326442](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/326442) confirms a distinct retained strain node, Pseudoalteromonas translucida TAC125, parent 166935, code 11. Alternative names include Pseudoalteromonas haloplanktis TAC125 and its str./strain variants, not TACII25. Its ancestry is through Alteromonadales/Pseudoalteromonadaceae/Pseudoalteromonas, not the target's Moraxella lineage. Local backbone `data/raw/ncbitaxon_taxa.tsv:66726`, index `data/taxa/PATHS.tsv:440472`, and scope `curation/seed_scope.tsv:32336` likewise keep 326442 separate. No second taxon YAML was reviewed and no identifiers or genome links were transferred.

All 22 unrelated native-row matches from the bounded local search were read completely:

- Eight GTDB rows match the numeric value 103760 in assembly length statistics, not taxonomy: `data/catalog/gtdb_genomes-0000.jsonl.gz:31851` (GCA_963610365.1, Eubacterium ventriosum); `0005:44770` (GCA_948875445.1, uncultured Oscillospiraceae); `0006:37698` (GCA_017430265.1, Paludibacteraceae bacterium); `0007:32467` (GCA_948826105.1, uncultured Oscillospiraceae); `0010:22005` (GCF_040096225.1, Hominiventricola aquisgranensis); `0011:18534` (GCF_016760635.1, Escherichia coli); `0014:14309` (GCF_021124445.1, Enterococcus faecium); and `0016:36513` (GCF_005043465.1, Escherichia coli). Abbreviated shard addresses use the same `data/catalog/gtdb_genomes-` prefix and `.jsonl.gz` suffix. NCBI organism names are used here; GTDB classifications can differ.
- Eleven rows concern culture deposit CIP 103760 for Wolinella succinogenes, not NCBITaxon:103760: `data/bacdive/records.jsonl.gz:6001`; `data/raw/bacdive_strains.tsv:6002`; `data/raw/culture_collection_strains.tsv:44080`; `data/raw/lpsn_names.tsv:21225` and `:21286`; `data/raw/ncbi_type_material.tsv:267635` and `:267636`; `data/straininfo/records.jsonl.gz:13878`; `data/straininfo/related_records.tsv.gz:234529` and `:234541`; and `data/straininfo/strain_links.tsv:95476`. The native BacDive ID is 6116, species taxid 844/strain taxid 273121; LPSN distinguishes deprecated Vibrio succinogenes from current Wolinella succinogenes. StrainInfo SI-ID13878/DOI 10.60712/SI-ID13878.3 has 11 deposits, including CIP 103760 (deposit 156242, origin LMG 7608), and eight sequence entries. Those sequences explicitly name ATCC, DSM, or NCTC deposits, not CIP; GCA_000196135.1 and GCA_900637325.1 do not establish a Moraxella genome link.
- `data/bacdive/records.jsonl.gz:27880` and `data/raw/bacdive_strains.tsv:27881` identify BacDive ID 103760 as Rhodococcus sp., taxid 194249, ST020721 (HKI)/BI10043, not type material, with no sequence information.
- `data/straininfo/records.jsonl.gz:135232` is SI-ID183272/DOI 10.60712/SI-ID183272.1, published offline, culture IMI 103760, deposit 461761, available and non-type. It supplies no taxon or sequence. Collection identity alone cannot establish an organism match.

None of these numeric collisions supports another target attestation, deposit, genome, or synonym.

## Completeness

Used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. The ID was word-bounded to avoid prefix collisions; other patterns covered the exact slug and Moraxella/TACII25 designation variants. The expanded pass added TAC II 25 variants, AJ249258, CAB65285, PMID 11112539, and bi0018133. Both passes returned 25 lines: own backbone, scope, scientific name, and the 22 unrelated rows above. Ignored and compressed files were included. No further target-linked assertion or local history artifact was established on these bounded surfaces.

All five source `SOURCE.json` files were independently enumerated and fully parsed. BacDive metadata contains 103760 in `responses/279/requested_ids/79` and its batch-fetch URL, referring to the unrelated BacDive/Rhodococcus ID above; the other four files had no match. Ignored-independent filename checks found the exact target YAML and no pre-existing target report or history filename. Eukaryota YAML contents were not opened.

There is a consequential unresolved historical identity question for future enrichment, but no unsupported biological assertion in this taxonomy/name-only YAML. Absence of optional sequence or literature enrichment is not itself a schema or curation defect. iModulonDB is not applicable to the record's assertions: it names no gene, regulator, expression module, or transcriptomics dataset. External tufA accession history was checked for provenance, not as expression-module evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the recorded assertions. The YAML faithfully preserves active NCBI 103760 and its pinned name attestation. The observed AJ249258 attribution change is a bounded source-history conflict, not sufficient evidence to merge records, overwrite the target name/lineage, or attach TAC125 genomes. A pass here does not resolve that historical biological identity question.

## Recommended Edits

None required for the present assertions. Do not hand-edit generated YAML, add an unsupported TAC125 synonym, transfer genomes, append history, or promote status. If later authorized curation resolves the historical attribution, preserve exact accession versions and the distinction between source taxonomy and biological identity. Verified enrichment belongs in maintained source inputs or an explicitly supported overlay. Extraction/seeding defects belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and their implementation modules; scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

Before enriching or reconciling these identities, obtain the primary article and documented taxonomic/strain reassignment evidence, explain the AJ249258.2-to-.3 change, and verify whether an authority explicitly equates TAC II 25 with TAC125. Recheck both live taxon IDs and any merger/retirement records. Require an explicit assembly/deposit source chain; shared protein accession is insufficient. After authorized maintained-input edits, rerun focused schema/strict/history validation, extraction dry run, seed canary, corpus reproduction, and full quality gates. Review-status promotion requires separate human sign-off.

## Additional Notes

Complete taxonomy API responses, browser text, PubMed bibliographic/abstract data, and all three GenBank versions were inspected. No search snippet supports a scientific claim. The [Naples deposit](https://www.iris.unina.it/handle/11588/159844) agrees with PubMed's volume 39 and pages; a [duplicate deposit](https://www.iris.unina.it/handle/11588/130199) instead lists volume 59. This is an external bibliographic discrepancy, not a YAML defect. The [Parthenope deposit](https://ricerca.uniparthenope.it/handle/11367/18056) supplies the abstract and a restricted PhTu.pdf link; opening the file redirected to institutional-login HTML, not PDF. The ACS article endpoint returned 403. No login, copy request, payment, or article full-text reading occurred.

Sequence audit SHA-256 values, for lowercase nucleotide strings: AJ249258.1 `e508871be071438f504f6f0e60eb7bc2a212d01a67d1f22e7dc66802ca9f7cc3`; AJ249258.2 `6c36ffe02306a6168e20c6db0d838c1d6f524426840778e9fa18cc52bc217f76`; AJ249258.3 `54787ef821a3d30031e8b72fcd22968206eb65f71c71fb9d2e16b2936ce5e4b8`. Protein translation hashes: CAB65285.1 `c585249a40ead37895e84bba8bdd6a24d21c6f0077ff5198a3fb3df70a28af2d`; CAB65285.2 in both .2 and .3 `95edfd52b8fd65fef55da66acca0bca70a021aba67881e807b4ae2013f66e677`.

YAML SHA-256: `d348c02c56fa0a953b9eadb0deae19d53021fb83041055db52bdcc9a8c2504b9`. Only this new report was written for the target. Maintained inputs, generated data, schema, history, pages, GitHub state, Eukaryota, and existing worktrees were unchanged.
