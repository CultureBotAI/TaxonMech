# YAML Record Review: Paenibacillus mucilaginosus KNP414

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/paenibacillus_mucilaginosus_knp414.yaml`
- Started UTC: 2026-10-09T10:04:48Z
- Finished UTC: 2026-10-09T10:09:15Z
- Verdict: needs curation

## Target

The complete generated `TaxonRecord` was read and uniquely resolved as `NCBITaxon:1036673`, Paenibacillus mucilaginosus KNP414. It carries `STRAIN` rank, `BACTERIA` domain, parent species `NCBITaxon:61624`, ten root-first ancestors, genetic code 11, `EXACT` grounding and `SEEDED` mapping status. Its content comprises one GTDB mapping, three synonyms, one GTDB xref, zero listed strains, three attestations and one embedded seed event dated 2026-09-13T17:54:04Z.

This review independently evaluates KNP414, not the parent species, its type strain 1480D, or the other genomes in its GTDB species cluster. Related source rows were inspected as context, without assigning verdicts to their corresponding records. The target is generated, not a maintained hand-editing surface.

## Validation

The documented focused implementations were run:

```bash
UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/paenibacillus_mucilaginosus_knp414.yaml
UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline python scripts/validate_strict.py data/taxa/bacteria/paenibacillus_mucilaginosus_knp414.yaml --out /private/tmp/taxonmech-knp414-review-strict.tsv
```

- LinkML: `No issues found`, exit 0.
- Strict: one file scanned, zero files with ERROR and zero ERROR rows, exit 0. The complete temporary TSV contained only its header.
- Structured comparison verified target identity, rank, parent, genetic code, all ancestors, NCBI synonyms, PATHS mapping and scope/history text against the pinned inventories. All three source/count/unit combinations were inspected separately. The GTDB predicate matches the input row but fails the semantic scope check below.
- Exact-field scans of `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv` and `data/raw/dropped.tsv` found no target rows. The pinned backbone contains no children of this target. These are bounded local snapshot results, not global absence claims.
- Complete public taxonomy XML, taxonomy JSON, assembly JSON, two nucleotide summaries and the PubMed abstract/identifier response were read. No whole-chromosome sequence download, sequence alignment, ANI recalculation or independent gene annotation was performed.
- Not checked: full-corpus `just verify-corpus`, `just qc`, complete tests, all-record strict validation, source-provenance gates, generated-page drift and full history validation. No focused substitute for those corpus-wide gates is claimed. There are no curator-added graph-node groundings requiring the OAK product-label gate. No separate history record was written or validated.
- The attempted GTDB genome page returned an internal web-tool error. GTDB membership/count evidence comes from complete pinned native catalog rows, not a successfully refreshed GTDB page.
- An ignored-independent `find` of the configured kg-microbe checkout's `data/` found only two NLP files, not the required transformed GTDB/GOLD/Madin inputs. Original KGX predicates and trait assertions were therefore not replayed. Relevant manifest entries were read; unavailable source files were not rehashed. No claim is made about other checkouts or remote copies.

Target SHA-256 before and after research: `99bc6ddc577691e58a9eda635a88299eae5203142e180419da8bf5643775f86f`.

## Identity and Grounding

The complete live [NCBI Taxonomy EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036673&retmode=xml) and [NCBI Datasets taxonomy response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036673) confirm the KNP414 scientific name and strain rank. EFetch supplies parent 61624, code 11 and both `str.`/`strain` equivalent names. Together the responses support root, cellular organisms, Bacteria, Bacillati, Bacillota, Bacilli, Caryophanales, Paenibacillaceae, Paenibacillus and Paenibacillus mucilaginosus as the carried ancestor chain.

The browser search lead displayed `no rank`, whereas both complete live structured responses returned strain. The discrepancy's cause was not resolved; the search snippet was not used to override inspected primary structured data. Older native BV-BRC/GTDB NCBI-lineage labels include Bacillales for taxon 1385, whereas current structured taxonomy and the target carry Caryophanales. The YAML correctly follows the pinned/live backbone rather than an older source's label.

`EXACT` is justified NCBI identifier grounding and `SEEDED` accurately preserves workflow state. They do not justify treating a species cluster as this strain. GTDB's own order, family and suffixed genus differ from NCBI's carried lineage; preserving that source distinction is intentional.

The complete live [NCBI assembly report](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCF_000218915.1/dataset_report) explicitly associates KNP414 and taxon 1036673 with current RefSeq `GCF_000218915.1`, paired GenBank `GCA_000218915.1`, ASM21891v1 and BioSample `SAMN02603153`. The BioSample supplies strain KNP414; the assembly comments describe its laboratory holding, not a registered culture-collection deposit. The separate taxonomy response counts one assembly. That count is neither seven GTDB-cluster genomes nor a TaxonMech culture-strain count.

## Evidence

All target-supporting rows and newly encountered candidates were read in full, including complete structured rows represented losslessly as common fields plus row-specific values:

| Address | Supported content |
| --- | --- |
| `data/raw/ncbitaxon_taxa.tsv:222576` | Target identity, rank, parent, code, two equivalent names, three attesting sources and 2026-09-13 snapshot |
| `data/catalog/ncbi_names-0005.jsonl.gz:32123` through physical line 32125 | Scientific name and two equivalent strain names |
| `data/raw/gtdb_mappings.tsv:1459` | Supplied species-to-KNP414 closeMatch and species-wide count 7 |
| `data/raw/gtdb_species.tsv:133670` | GTDB species identifier, genus parent and seven-genome count |
| `data/raw/madin_taxa.tsv:691` | Three direct-taxon trait assertions in the transformed input inventory |
| `data/taxa/PATHS.tsv:15094` | Exact identifier-to-slug mapping |
| `curation/seed_scope.tsv:36175` | Admission on 2026-09-12 and three-source reason reproduced in the seed event |

Seven complete native GTDB genome rows share terminal taxon `s__Paenibacillus_G mucilaginosus`:

| Native catalog row | Genome | Supplied strain; NCBI taxon |
| --- | --- | --- |
| `data/catalog/gtdb_genomes-0011.jsonl.gz:44912` | `RS_GCF_000218915.1` | KNP414; 1036673 |
| `data/catalog/gtdb_genomes-0015.jsonl.gz:11687` | `RS_GCF_000258535.2` | K02; 997761 |
| `data/catalog/gtdb_genomes-0009.jsonl.gz:28965` | `RS_GCF_000250655.1` | 3016; 1116391; GTDB representative |
| `data/catalog/gtdb_genomes-0005.jsonl.gz:18893` | `RS_GCF_050433645.1` | CC578; 61624 |
| `data/catalog/gtdb_genomes-0008.jsonl.gz:11840` | `RS_GCF_028751605.1` | PM12; 61624 |
| `data/catalog/gtdb_genomes-0006.jsonl.gz:16694` | `RS_GCF_029542585.1` | KN-18; 61624 |
| `data/catalog/gtdb_genomes-0010.jsonl.gz:18037` | `RS_GCF_022343625.1` | G78; 61624 |

KNP414 is not the representative and is only one member of this cluster. The complete additional mapping rows at `data/raw/gtdb_mappings.tsv:4224`, physical lines 299774 and 322204 also close-match the same species to 3016, the parent species and K02. Those assertions show how the input is organized; they do not collapse the distinct strains into one biological identity. `genome_count: 7` is supported at cluster scope.

Complete native NCBI assembly rows at `data/catalog/ncbi_genbank-0000.jsonl.gz:3715` and `ncbi_refseq-0000.jsonl.gz:3204` identify the explicit assembly pair, same BioSample and one 8,663,821-base chromosome. Complete current [CP002869.1](https://www.ncbi.nlm.nih.gov/nuccore/CP002869.1) and [NC_015690.1](https://www.ncbi.nlm.nih.gov/nuccore/NC_015690.1) ESummary records confirm circular chromosome, length, code 11, taxon 1036673 and KNP414; the RefSeq summary explicitly points to CP002869.1. Their respective project contexts are PRJNA67335 and PRJNA224116. Distinct annotation dates and gene counts were retained as source/version context, not treated as additional assemblies.

The inspected [BioProject PRJNA67335 page](https://www.ncbi.nlm.nih.gov/bioproject/67335) names KNP414, its laboratory holding, GCA_000218915.1, SAMN02603153, the publication, GOLD Gp0011235 and IMG 650716070. The complete native BV-BRC row at `data/bvbrc/bvbrc-0000.jsonl.gz:3391` supplies genome 1036673.3, assembly GCA_000218915.1, the same BioSample/project, CP002869 and NC_015690.1, with source strain text `KNP414/soil`. That text is not a validated culture-collection accession.

The complete native GOLD rows at `data/gold/organisms.jsonl.gz:9863`, `projects.jsonl.gz:9727` and `analyses.jsonl.gz:19988` establish Go0011235 -> Gp0011235 -> Ga0029703. The analysis supplies GCA_000218915.1 and IMG 650716070. The organism's culture-collection field and the project's BioSample field are empty; the project-to-organism relationship is explicit. This supports source genome context but not an invented deposit match. There is no own-taxon row in the legacy `data/raw/gold_organisms.tsv`. Consequently the missing GOLD attestation matches the current legacy-KGX contract, not absence of GOLD data: `src/taxonmech/extract.py:676` counts that separate input, while `src/taxonmech/seed.py:613` emits its result. Native catalog coverage must not be described as absent.

[Lu et al.'s genome announcement](https://journals.asm.org/doi/10.1128/genomea.00881-13), PMID 24158556, PMCID PMC3813186 and DOI 10.1128/genomeA.00881-13, was checked through its complete PubMed abstract/identifiers and the publisher's article text. It reports KNP414's complete chromosome and accession CP002869 and distinguishes strains K02 and 3016. The paper is contextual genome provenance, not a citation already in the YAML. No nitrogen-fixation, nutrient-solubilization, growth-promotion or causal claims were imported from it.

[LPSN's species page](https://lpsn.dsmz.de/species/paenibacillus-mucilaginosus) identifies species record 788339 and type strain 1480D, including CIP 105815, DSM 24461 and KCTC 3870. Complete inventory row `data/raw/lpsn_names.tsv:25490` maps that name to species 61624, not KNP414. The inspected identity section of [BacDive 11505](https://bacdive.dsmz.de/strain/11505) likewise identifies 1480D and species 61624. Its appearance as a type-strain link from a taxonomy browser does not equate it with KNP414 or supply KNP414 with those deposits.

## Completeness

Zero `strain_count` agrees with the current classified-BacDive listing rule. The own-taxon inventory scan found no BacDive classification or descendant to gather, and ignored-inclusive searches for the target and its explicit genome/sample identifiers found no supporting culture-deposit crosswalk. NCBI, GTDB, GOLD and BV-BRC nonetheless preserve KNP414 genome context. A bare strain designation, species-level type link or shared taxon label cannot supply a registered-deposit join. This is not a claim that KNP414 has no laboratory culture or that no deposit exists anywhere.

No required strain-level LPSN nomenclature entry was identified. The two NCBI equivalent names are supported. Empty optional discussions, causal graphs and record-level literature entries do not create automatic completeness defects. iModulonDB is not applicable to the asserted YAML content, which contains no gene, regulator, transcriptomic module or mechanistic assertion requiring that adapter.

The attestations correctly reproduce NCBITAXON 1 NAME, GTDB 7 GENOME and MADIN 3 TRAIT_ASSERTION. Their units cannot be summed as equivalent observations. The GTDB predicate still fails scope review, and the original three Madin KGX assertions were not available for independent source-level inspection. No experimental phenotype support is claimed from an inventory count alone.

The initial ignored-inclusive content search returned 15 candidate rows. The expanded search returned 18, including ten new rows; all were fully read. The source-metadata scan parsed five `SOURCE.json` files and found no initial target-term match. Ignored-independent filename inventories found one target YAML and no earlier target-named report or separate target-named history artifact. Search terms, roots and limitations are recorded below.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

1. **Major: species-cluster membership is promoted to strain equivalence.** At target line 43, the species identifier `GTDB:s__Paenibacillus_G_mucilaginosus` is close-matched to KNP414; line 46 makes its rendered species name an exact synonym, line 57 places the species in equivalent xrefs, and line 70 repeats the closeMatch attestation. The seven complete native cluster rows contain several distinct strains, including K02 and 3016. Live NCBI distinguishes KNP414 from its parent species. The equivalence restriction at `src/taxonmech/schema/taxonmech.yaml:180` and source-to-target mapping definition at line 429 are therefore not satisfied by copying this predicate. The local maintained owner is `src/taxonmech/seed.py:451`, where closeMatch alone sets identity, followed by xref/exact-synonym promotion at line 467. The input predicate is owned upstream by kg-microbe's GTDB transform and carried through `src/taxonmech/extract.py:501`. The same promotion also replaces the meaningful genus suffix underscore with a space, yielding `Paenibacillus G mucilaginosus` instead of the native GTDB label `Paenibacillus_G mucilaginosus`. That malformed exact-name rendering is included in this consolidated mapping/synonym finding, not counted again.

No blocker was found in the target's NCBI identity or YAML shape, and no separate minor finding is assigned. The unavailable original KGX replay and the diagnostics described below remain limitations, not invented curation defects.

## Recommended Edits

1. Add scope-compatible identity checks to `src/taxonmech/seed.py` before promoting GTDB species mappings to equivalent xrefs or exact synonyms on infraspecific records. For KNP414, remove the unsupported species-level equivalence products through the generator, retain its two supported NCBI synonyms and add a regression fixture in `tests/test_seed.py`. Do not hand-edit generated YAML or inventories.
2. Reevaluate the upstream GTDB predicate that produced `data/raw/gtdb_mappings.tsv:1459`, then refresh through the maintained extractor only in a separately authorized curation change. Preserve original source assertions as provenance without presenting them as accepted same-scope identity. Do not mechanically substitute broadMatch: this schema's broadMatch means the record is broader than the source, the opposite of a strain versus its species cluster. An appropriate rank-aware relation or explicit non-equivalence representation needs a deliberate source/schema decision.
3. Keep the seven-genome count explicitly scoped to the GTDB species and preserve the native suffixed genus spelling wherever a legitimate GTDB name is displayed. Do not add species-type deposits, reclassify KNP414, alter its carried lineage or infer cross-database genome equivalence from names. Future source-coverage changes should distinguish native GOLD availability from legacy KGX attestations.

No recommended curation edit was made by this review.

## Follow-up Checks

- Run focused seeder regression tests after the authorized fix, covering KNP414's strain/species distinction, valid species-level mappings and preservation of GTDB suffix punctuation. Use the documented single-record seed canary, inspect the full resulting YAML, then rerun LinkML and strict validation.
- Recheck all seven pinned GTDB members and the four mapping targets against fresh authority data when accessible. Verify that species counts and source mapping provenance no longer imply strain equivalence.
- Replay the original GTDB and Madin KGX inputs when the configured snapshots are available; validate their manifest pins and maintain the distinct GOLD native-catalog versus KGX count contract.
- Require an explicit eligible culture-deposit assertion before adding KNP414 to a strain-genome crosswalk. A taxonomy browser's link to species type strain 1480D is insufficient.
- Before publishing changed generated products, run `just verify-corpus` and the authoritative `just qc`, including provenance, tests, history, strict-schema and generated-site checks. They were not run in this one-record review.

## Additional Notes

Both content scans used `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. The initial pattern was `\b1036673\b|\bKNP[ _-]?414\b|paenibacillus_mucilaginosus_knp414\b`. The expanded pattern was:

```text
\bs__Paenibacillus_G[ _]mucilaginosus\b|\b(?:GCA|GCF)_000218915(?:\.1)?\b|\b(?:SAMN02603153|PRJNA67335|CP002869(?:\.1)?|NC_015690(?:\.1)?|Go0011235|Gp0011235|Ga0029703|650716070)\b
```

Search counts overlap and are not biological counts. Complete rows, not regex hits alone, established cluster membership and source-chain scope. The separate LPSN species-label search was also ignored-inclusive; its whole matching row was parsed with the TSV header. These searches establish only bounded local findings, not an exhaustive census of every remote synonym or literature reference.

The live assembly report's ANI diagnostic is `Inconclusive`, with no submitted-species type assembly and a below-threshold best type match to Paenibacillus caseinilyticus. This is not authority to rename KNP414 or change its lineage. No independent taxonomic reassessment was performed. Historical paper and current annotation counts likewise do not prove biological identity changes.

The configured upstream check was `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data -type f`. It included ignored files and located no transformed inputs in that specific data directory. The GTDB website limitation and the missing local inputs do not erase the inspected native catalog or make this a blocked review.

Only this timestamped report was added. This review did not modify record YAML, source data, scope, generated pages, either history surface, mapping status, Eukaryota, branches or worktrees. It made no GitHub mutation, provider-credit expenditure or external contact.
