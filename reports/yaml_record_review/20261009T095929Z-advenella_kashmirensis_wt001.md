# YAML Record Review: Advenella kashmirensis WT001

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/advenella_kashmirensis_wt001.yaml`
- Started UTC: 2026-10-09T09:47:31Z
- Finished UTC: 2026-10-09T09:59:29Z
- Verdict: needs curation

## Target

The complete generated `TaxonRecord` was read and uniquely resolved as `NCBITaxon:1036672`, Advenella kashmirensis WT001. It carries `STRAIN` rank, `BACTERIA` domain, parent species `NCBITaxon:310575`, genetic code 11, ten root-first ancestors, `EXACT` grounding and `SEEDED` mapping status. The record contains one GTDB mapping, four synonyms, one GTDB xref, zero listed strains and four source attestations. Its single embedded seed event is dated 2026-09-13T17:54:04Z.

This is a review of the WT001 taxon, not the parent species, a subspecies, W13003, a culture-collection deposit or a genome assembly. Related records were inspected only to resolve evidence placement. Their verdicts were neither assigned nor inherited. All target fields are generated; the YAML is not the maintained correction surface.

## Validation

The documented focused implementations ran successfully, including a repeat immediately before writing this report:

```bash
UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/advenella_kashmirensis_wt001.yaml
UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline python scripts/validate_strict.py data/taxa/bacteria/advenella_kashmirensis_wt001.yaml --out /private/tmp/taxonmech-advenella-wt001-review-strict.tsv
```

- LinkML: `No issues found`, exit 0.
- Strict: one file scanned, zero files with ERROR and zero ERROR rows, exit 0. The complete temporary TSV contained only its header.
- Structured source comparison verified identifier, label, rank, parent, code, all ancestors, NCBI synonyms, path mapping and scope/history text. All four attestations were separately compared with their inventory rows. Reproducing an upstream predicate is not proof that its biological scope is correct.
- Exact-field scans found no target rows in `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv` or `data/raw/dropped.tsv`, and no target children in the pinned backbone. Type-material rows for the parent species and subspecies were found and read separately.
- Seven complete GTDB catalog candidate rows were inspected; parsing their `gtdb_taxonomy` fields identified exactly two members of `s__Advenella kashmirensis`. The distinction between this field and `ncbi_taxonomy` matters.
- Not checked: full-corpus `just verify-corpus`, `just qc`, complete tests, all-record strict validation, full source-provenance checks, generated-page drift or full history validation. These corpus-wide gates were not replaced with an invented focused equivalent. The record has no curator-added graph-node groundings requiring the OAK product-label gate. No separate history entry was created or validated.
- The GTDB genome page and the NCBI assembly endpoint were inaccessible through the web tool. The NCBI endpoint subsequently returned a complete public JSON response through a direct read. GTDB identity/count evidence below comes from the inspected pinned native catalog, not a successfully refreshed GTDB website.
- The configured kg-microbe checkout lacks the four requested transformed GTDB/GOLD/Madin files. An ignored-independent `find` of that checkout's `data/` found only two NLP files. Thus original KGX assertions were not replayed; this does not claim that no other checkout or remote copy exists.

Target SHA-256 before and after research: `deec494bd12214457c3af78a14104b91fabde34ceba882637ad7570a0ef96650`.

## Identity and Grounding

Complete live [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036672&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036672) responses confirm the WT001 label and strain rank. EFetch supplies parent 310575, code 11, the Tetrathiobacter synonym and both `str.`/`strain` equivalent names. Together the structured responses support the carried chain: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Betaproteobacteria, Burkholderiales, Alcaligenaceae, Advenella and Advenella kashmirensis. The browser search lead displayed a `no rank` value; it was not preferred over the complete live structured responses, and the cause of that discrepancy was not resolved.

`EXACT` correctly identifies the NCBI strain concept, and `SEEDED` correctly preserves the workflow state. Neither establishes equivalence between a strain and a species cluster. The species-only GTDB synonym and equivalent xref do not have the same scope as this target.

The complete live [NCBI assembly report](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCF_000219915.2/dataset_report) independently joins WT001 and taxon 1036672 to current RefSeq `GCF_000219915.2`, paired GenBank `GCA_000219915.3`, assembly ASM21991v3 and BioSample `SAMN01940915`. Its BioSample attributes explicitly name WT001 as strain and isolate and identify type material. The assembly evidence supports this particular strain, not equivalence of all species members. The separate taxonomy response's count of one assembly is not the GTDB species genome count or the TaxonMech strain-list count.

## Evidence

Complete local rows supporting the seeded fields were read at:

| Address | Supported content |
| --- | --- |
| `data/raw/ncbitaxon_taxa.tsv:222575` | WT001 identity, parent, rank, code, three NCBI synonyms, four attesting sources and 2026-09-13 snapshot |
| `data/catalog/ncbi_names-0005.jsonl.gz:32119` through physical line 32122 | Two equivalent strain names, scientific name and Tetrathiobacter synonym |
| `data/raw/gtdb_mappings.tsv:1458` | Supplied species-to-WT001 `skos:closeMatch` and genome count 2; faithfully copied but semantically over-scoped |
| `data/raw/gtdb_species.tsv:5307` | GTDB species identifier, genus parent and species-wide genome count 2 |
| `data/raw/gold_organisms.tsv:499` | Legacy KGX direct-taxon organism count 1 |
| `data/raw/madin_taxa.tsv:690` | Legacy KGX direct-taxon trait-assertion count 3 |
| `data/taxa/PATHS.tsv:15093` | Exact identifier-to-slug mapping |
| `curation/seed_scope.tsv:26090` | Admission on 2026-09-12 and four-source reason carried into seed history |

The two exact GTDB species-cluster members in the native catalog are:

| Native row | Genome | Supplied identity |
| --- | --- | --- |
| `data/catalog/gtdb_genomes-0017.jsonl.gz:25052` | `RS_GCF_000219915.2` | Representative, WT001, NCBI taxon 1036672, species taxon 310575, BioSample SAMN01940915 |
| `data/catalog/gtdb_genomes-0012.jsonl.gz:34248` | `GB_GCA_002384805.1` | Non-representative metagenome assembly, isolate UBA4006, NCBI taxon 310575, BioSample SAMN06456267 |

Thus `genome_count: 2` is supported as a species-cluster count, not two WT001 genomes or its two replicons. W13003 (`RS_GCF_000506985.1`, native row `gtdb_genomes-0016.jsonl.gz:28646`) belongs to `s__Advenella kashmirensis_A`, not this exact cluster. Other complete candidates belonged to the suffixed B/C clusters or `sp003533245`/`sp023387815`. GTDB's class/family differ from the carried NCBI lineage; that source disagreement does not authorize rewriting NCBI ancestry.

The native WT001 assembly rows were fully inspected in `data/catalog/ncbi_genbank-0000.jsonl.gz:3753` and `ncbi_refseq-0000.jsonl.gz:3230`, with replaced versions in `ncbi_genbank_historical-0000.jsonl.gz:1103`, physical line 1104, and `ncbi_refseq_historical-0000.jsonl.gz:1076`. Current GenBank .3 and RefSeq .2 are explicitly paired; historical GenBank .1/.2 and RefSeq .1 are not extra current genomes. The live report gives PRJNA67337; the pinned RefSeq/GTDB rows carry PRJNA224116. Those supplied project contexts were preserved rather than treated as strain-identity disagreement.

[BacDive 383](https://bacdive.dsmz.de/strain/383), its complete native row `data/bacdive/records.jsonl.gz:382`, and `data/raw/bacdive_strains.tsv:383` identify WT001 and deposits DSM 17095, LMG 22965 and MTCC 7002. Its classification fields name species 310575 and subspecies 1914954, whereas its explicit genome block names taxon 1036672 and supplies unversioned GCA_000219915, IMG 2515154053 and BV-BRC/PATRIC 1036672.3. The 16S marker AJ864470 is a different identifier type and is classified at species scope. These are source assertions, not permission to merge all identifiers.

The corresponding whole assembly/genome crosswalk rows were read at `data/raw/strain_assemblies.tsv:123130`, physical line 123131, and `data/raw/strain_genome_records.tsv:99007` through physical line 99009. GOLD's eligible chain is Go0011867 -> Gp0011867 -> Ga0009814, matched through DSM 17095; the related rows also retain PRJNA67337. Its unversioned assembly accession must remain unversioned in that source assertion.

All six native GOLD rows for the two WT001 organism/project/analysis chains were read. The second chain, Go0396674 -> Gp0261116 -> Ga0226167, supplies versioned GCA_000219915.3 and IMG 2773858051 but no organism culture-collection identifier. A matching name/taxon or shared accession cannot invent a deposit match. Three further deposit-named GOLD organisms, Go0628456/Go0628457/Go0628458, are classified under species 310575; their complete rows and crosswalk rows were also read. Neither these modern native entries nor the two WT001 chains redefine the legacy direct KGX attestation count. `src/taxonmech/extract.py:676` and `docs/HARMONIZATION.md:44` explicitly define that count's different input.

The complete two BV-BRC native rows (`data/bvbrc/bvbrc-0000.jsonl.gz:3389` and physical line 3390) retain distinct identifiers 1036672.20 and 1036672.3 with differing genome-status metadata and a common assembly/BioSample. The BacDive assertion specifically supplies 1036672.3; no equivalent link to 1036672.20 was inferred. The complete AllTheBacteria row at `data/catalog/allthebacteria.tsv.xz:1014373` has sample SAMN01940915 but `asm_fasta_on_osf: 0`, `NOT_PROCESSED`, no assembly and no available FASTA. It does not support adding an ATB genome link.

There is a real deposit conflict to preserve before any future strain curation. [LPSN's species page](https://www.lpsn.dsmz.de/species/advenella-kashmirensis) lists LMG 22695 with DSM 17095, MTCC 7002 and WT001; [DSMZ's DSM 17095 entry](https://www.dsmz.de/collection/catalogue/details/culture/DSM-17095) instead lists LMG 22965 with WT001 and MTCC 7002. The native StrainInfo record (`data/straininfo/records.jsonl.gz:92118`, SI-ID135988, DOI 10.60712/SI-ID135988.3) contains both LMG deposits: LMG 22695 is typed to the kashmirensis taxon, while LMG 22965 carries Agrococcus sp. NA and is not marked type. Its grouping and BacDive cross-reference do not resolve that disagreement. The target YAML does not assert either deposit, so this is a contextual curation caution rather than a second finding against this record.

The complete PubMed abstracts and identifiers for [PMID 21914874](https://pubmed.ncbi.nlm.nih.gov/21914874/) / DOI 10.1128/JB.05781-11 and [PMID 23741407](https://pubmed.ncbi.nlm.nih.gov/23741407/) / DOI 10.1371/journal.pone.0064856 were read as genome-provenance context. The latter paper's inspected [genome-accession paragraph](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0064856) identifies chromosome CP003555 and plasmid CP003556. Neither paper is cited by the YAML; no physiology, virulence, biosafety or causal claim was imported. This was not a full scientific review of those studies.

## Completeness

The zero `strain_count` is consistent with the current classification-based listing contract. BacDive 383 is filed under species 310575 and subspecies 1914954, neither a descendant of WT001. The complete generated species and subspecies YAMLs were read and both already carry its deposit/genome evidence. `src/taxonmech/seed.py:487` gathers classified strains from the target and its descendants; a linked genome's `taxon_id` does not reclassify the strain. Zero here does not mean WT001 lacks a deposit or sequenced genome.

There is no missing required nomenclature entry: the inspected LPSN mapping concerns species 310575, not a separate strain-level name record. Optional discussions, causal graphs and record-level literature entries are empty without creating an automatic defect. iModulonDB is not applicable to this record's asserted content: it names no gene, locus, regulator, expression module or mechanistic claim to check.

The four attestations have the appropriate source/count/unit combinations against the committed inventories: NCBITAXON 1 NAME, GTDB 2 GENOME, GOLD 1 ORGANISM and MADIN 3 TRAIT_ASSERTION. They must not be summed as equivalent biological observations. The GTDB mapping scope remains defective despite the correct count. Madin's underlying three KGX assertions were not inspected because the configured transformed input was unavailable; inventory agreement is not an independent verification of their original experimental support.

Ignored-inclusive searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, with compressed-content searching enabled. The initial target-ID/WT001/slug search returned 41 candidate rows. The expanded assembly/BioSample/GTDB/deposit/GOLD/BacDive-ID search returned 57 candidates. All initial and newly encountered candidate rows were read in full, using complete parsed TSV/JSON rows or lossless common-field/delta output. A separate ignored-inclusive GTDB species-name search returned seven complete native rows, which were inspected before field-specific interpretation. These counts include overlapping results and are not biological counts.

All five discovered source `SOURCE.json` files were parsed; none matched the initial target terms. An ignored-independent filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved the target and found no earlier target-named report or separate target-named history artifact. These statements concern the searched local surfaces only, not the absence of biological evidence elsewhere.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

1. **Major: a GTDB species cluster is promoted to strain equivalence.** Target line 43 calls the GTDB species a `skos:closeMatch` to strain 1036672; line 46 supplies its species-only name as an `EXACT_SYNONYM`; line 60 puts the species identifier in equivalent `xrefs`; line 73 repeats the close-match predicate in the attestation. The schema at `src/taxonmech/schema/taxonmech.yaml:180` restricts xrefs to true equivalences, and its mapping description at line 429 defines closeMatch for the same species. Live NCBI separates WT001 from parent species 310575; the native GTDB cluster explicitly contains both WT001 and distinct metagenome UBA4006. The copied raw mapping therefore does not justify species/strain equivalence. The maintained local owner is `src/taxonmech/seed.py:451`, where closeMatch alone sets `identity`, followed by xref/exact-synonym promotion at line 467. The supplied predicate originates upstream in kg-microbe's GTDB mapping and is carried by `src/taxonmech/extract.py:501`; correct it at that source/transform boundary and protect local promotion with rank/scope-aware logic and tests. Do not hand-edit the generated YAML or raw inventory. This is one consolidated scope defect, not four independent findings.

No blocker was found in the target's NCBI identity or YAML shape. No minor finding is assigned. The deposit discrepancy and unavailable original KGX replay remain explicit limitations, not additional unsupported target verdicts.

## Recommended Edits

1. In `src/taxonmech/seed.py`, require scope-compatible identity evidence before turning a GTDB species mapping into an equivalent xref or exact synonym on an infraspecific record. For WT001, suppress the species-only exact synonym and equivalent xref unless an independently justified same-scope representation is supplied. Add a focused regression fixture in `tests/test_seed.py` covering this strain/species distinction while retaining valid species-level identity behavior.
2. Reevaluate the upstream kg-microbe GTDB mapping that produced `data/raw/gtdb_mappings.tsv:1458`; follow through `src/taxonmech/extract.py` during a separately authorized refresh. Preserve the original source assertion as provenance if needed, but distinguish it from an accepted identity assertion. Do not blindly replace closeMatch with broadMatch: the schema defines predicates from source to target, and broadMatch here means the TaxonMech record is broader than the source. WT001 is narrower than its source species. An appropriate rank-aware relation or explicit non-equivalence representation requires a deliberate source/schema decision.
3. Preserve species-wide `genome_count: 2` with an explicit species scope, the three supported NCBI synonyms, carried lineage and exact NCBI grounding. Keep classification-based strain placement unchanged unless a separate evidence-backed design change is authorized. Resolve the LMG deposit disagreement before using it for new joins; do not collapse 22695 and 22965 by spelling similarity.

These are future edits only. No generator, source refresh, history append or status promotion was performed by this review.

## Follow-up Checks

- After an authorized code change, run focused seeder regression tests and the documented single-target seed canary, inspect the resulting complete YAML, then rerun LinkML and strict validation on it. Retained source mappings must no longer imply unsupported equivalence through either xrefs or exact synonyms.
- Recheck WT001 and its species/subspecies context against NCBI, inspect the two exact GTDB cluster members, and confirm the mapping direction and count scope. A type or representative genome does not make its strain identifier synonymous with the whole cluster.
- When the configured source snapshots are available, replay the original GTDB mapping and GOLD/Madin direct counts, verifying the manifest pins. Do not substitute a modern native-catalog count for a legacy KGX count without an explicit input-contract change.
- For any newly authorized deposit work, compare the primary LMG collection records and StrainInfo deposit-specific provenance before joining sequences. Preserve supplied accession versions and the explicit organism/project/analysis chain.
- Before publishing a changed corpus, run `just verify-corpus` and the authoritative `just qc`, including provenance, tests, history, strict validation and generated-product gates. None is claimed green from this one-record review.

## Additional Notes

The initial content pattern was `\b1036672\b|\bWT[ _-]?001\b|advenella_kashmirensis_wt001\b`. The expanded pattern was:

```text
\bGTDB:s__Advenella_kashmirensis\b|\b(?:DSM[ _-]?17095|LMG[ _-]?(?:22695|22965)|MTCC[ _-]?7002)\b|\b(?:GCA|GCF)_000219915(?:\.[123])?\b|\b(?:SAMN01940915|Ga0009814|Gp0011867|Go0011867|Go0396674|Gp0261116|Ga0226167)\b|\bbacdive_383\b
```

Both used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` over the roots named above, with source metadata checked separately. The GTDB-only search initially used the underscored species spelling and found nothing; inspecting the native row revealed a space in its taxonomy value. The corrected `s__Advenella[ _]kashmirensis\b` search over `data/catalog` with `-g '*gtdb*'` found seven rows. Its matches included NCBI taxonomy fields, so complete rows and exact GTDB terminal taxa, not regex hits alone, established the two-member cluster.

One initial numeric hit, `data/catalog/ncbi_genbank-0066.jsonl.gz:36780`, was excluded after complete inspection: 1036672 was the genome size of a Rhodobiaceae bacterium assembly, not its taxon identifier. Source grouping, numeric coincidence and equal species labels were not used as identity evidence.

The configured upstream inventory check was `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data -type f`. Relevant manifest entries pin kg-microbe commit `30405b70ef762aa46c08278b2b3e06bffb0b34cd` and hashes for GTDB nodes/edges and GOLD/Madin edges; this review read those entries but did not rehash unavailable files.

This review added only this report. It did not change taxon YAML, source inventories, generated pages, scope, embedded or separate history, workflow status, Eukaryota records, branches or worktrees. It made no GitHub mutations or paid-research requests.
