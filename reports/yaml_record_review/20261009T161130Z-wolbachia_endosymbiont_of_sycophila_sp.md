# YAML Record Review: Wolbachia endosymbiont of Sycophila sp.

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_sycophila_sp.yaml`
- Started UTC: 2026-10-09T16:08:20Z
- Finished UTC: 2026-10-09T16:11:30Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` for `NCBITaxon:1036835` was read. It denotes Wolbachia endosymbiont of Sycophila sp., rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2640676` (unclassified Wolbachia), genetic code 11, grounding `EXACT` and status `SEEDED`. It has zero inventoried strains, one NCBITAXON name attestation and one seeding event.

The ignored-inclusive filename inventory also found `wolbachia_endosymbiont_of_sycophila_sp_2.yaml`. Its distinct source identity is taxon 1248012, labeled Wolbachia endosymbiont of Sycophila sp. 2. The exact identifier and PATHS row uniquely resolve the present target; that other record was not reviewed. No prior report for this target was found. Target SHA-256: `dbe15602aa57ef4722242a5bceb8cf6089e2f8acbca890ce0913cad19d82a80d`.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1` with the existing environment.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/wolbachia_endosymbiont_of_sycophila_sp.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/wolbachia_endosymbiont_of_sycophila_sp.yaml --workers 1 --out /private/tmp/taxonmech-sycophila-20261009-validation.tsv`: passed, one file and zero errors; the inspected output TSV contains only its header.
- `uv run --offline python scripts/validate_history.py history`: passed, 17 valid records and zero invalid links.
- Structured own-row checks passed for identity, every ancestor, source attestation, PATHS/scope entries and generated event wording.
- Not checked: full-corpus reproduction, full-corpus schema/provenance/QC/tests and site drift were not rerun for this individual review. The documented `just verify-corpus` gate has no record selector. Focused comparisons do not certify corpus reproduction.
- Not applicable: OAK curator-added graph checks and iModulonDB gene/component checks. The YAML contains no causal graph, gene, regulator, pathway, trait or transcriptomics assertion. External marker records inspected for identity do not add such claims to the YAML.
- The NCBI Taxonomy browser was inaccessible through the web tool; live EFetch and Datasets responses supplied authority evidence. PMC returned a browser-check page for the contextual paper; its publisher's full text and PubMed were inspected instead.
- Not checked: the contextual paper's supplementary Table S2 specimen mapping. Its legacy XLS format has no `xlrd` reader in the existing environment; no dependency was installed. Direct GenBank qualifiers, rather than an uninspected supplementary table, support the specimen details below.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222629` and `data/catalog/ncbi_names-0005.jsonl.gz:32223` support the exact identifier, label and scientific-name status. The backbone also supports species rank, direct parent, genetic code, NCBI-only attestation and the 2026-09-13 snapshot. It supplies no exact, related or broad synonyms.

Live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036835&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036835) agree. All eleven lineage entries match the local backbone and live authority: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Alphaproteobacteria 28211; Rickettsiales 766; Anaplasmataceae 942; Wolbachieae 952; Wolbachia 953; unclassified Wolbachia 2640676. Labels and ranks are consistent.

This is the bacterial endosymbiont concept, not its Sycophila host. NCBI's species rank does not establish a formally named species or cultured type strain. The carried unclassified-Wolbachia placement is not replaced by an inferred supergroup or a host classification.

## Evidence

The source attestation counts one NCBI name, not three specimens or three bacterial strains. Source ID, label, count, unit and snapshot date match the inventory. `strain_count: 0` means no inventoried BacDive strain under the taxon, not no biological occurrence.

The exact non-expanded query `txid1036835[Organism:noexp]` returned three nucleotide IDs: 334360642, 334360644 and 334360646. Complete GenBank metadata, features, references and sequence-length checks were inspected for each:

| Accession | Specimen voucher | BOLD cross-reference | Marker |
|---|---|---|---|
| [JF902514.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902514.1) | `BIOUG<CAN>:YLCFW120-08.w` | ASWFW002-10.COI-5P | partial COI, 642 bases |
| [JF902515.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902515.1) | `BIOUG<CAN>:YLCFW121-08.w` | ASWFW003-10.COI-5P | partial COI, 642 bases |
| [JF902516.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902516.1) | `BIOUG<CAN>:YLCFW122-08.w` | ASWFW004-10.COI-5P | partial COI, 642 bases |

Each identifies the exact organism and `taxon:1036835`, translation table 11, collection date 26-May-2007 and Hainan, China. Actual and declared lengths agree. JF902514 contains A/C/G/T only; the other two include ambiguous N bases. The BOLD IDs are GenBank-supplied cross-references, not independently verified current BOLD pages. Specimen vouchers and partial markers do not establish eligible culture deposits or genome assemblies.

GenBank retains an unpublished Smith reference titled "Wolbachia and Barcoding Insects: Patterns, Potential and Problems." The related published study, [Smith et al. 2012, DOI 10.1371/journal.pone.0036514](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0036514), was checked at the publisher and through [PubMed 22567162](https://pubmed.ncbi.nlm.nih.gov/22567162/). Its methods explain bacterial COI recovery from host extracts and the .w specimen convention. This is contextual support; the uninspected supplementary accession mapping is not claimed as verified. Study-wide prevalence, supergroup and reproductive effects are not assigned to this taxon.

The live [NCBI genome dataset query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1036835/dataset_report) returned an empty object. It supplies no positive assembly evidence through that query, not proof of universal absence.

## Completeness

Gitignore-independent searches included hidden and compressed files under `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Searches used the bounded numeric identifier and label/slug-compatible spelling. All 23 candidates were read in full: 19 native JSON rows and four TSV rows. All five source `SOURCE.json` files were parsed and had no target match. A follow-up ignored-inclusive compressed-source search for JF902514/JF902515/JF902516 and their voucher/BOLD identifiers found no match in those roots. These absence findings concern the inspected snapshot only.

Non-target candidates were resolved explicitly:

- Taxon 1248012 has the separately named Sycophila sp. 2 endosymbiont concept in its backbone, scientific-name and scope rows. A shared host genus and parent do not make the concepts synonymous.
- Eight NCBI assembly rows and eight BV-BRC rows concern Enterococcus faecium, taxon 1352, BioProject PRJNA1036835. The project-number suffix collides with this NCBI taxon ID. The assemblies are GCA_033657225.1, GCA_033657245.1, GCA_033657365.1, GCA_033657405.1, GCA_033657445.1, GCA_033657465.1, GCA_033657525.1 and GCA_033678185.1; their paired RefSeq accessions, Efm designations, BioSamples and BV-BRC 1352.17150 through 1352.17157 are not Wolbachia evidence.
- GCA_977267155.1, MarMAG_029232, is an uncultured bacterium, taxon 77133. Its ungapped genome size is 1036835; this numeric statistic is not a taxonomic association.

Complete own-ID inventory scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits assertion, type-material row, merged-ID row, dropped row or child. No inspected source supports an eligible own culture-to-genome chain. Optional synonyms, nomenclature, mappings, xrefs, strain/genome lists, experimental evidence and causal graphs are appropriately empty. External marker evidence does not demonstrate a missing required genome relationship.

`data/taxa/PATHS.tsv:15161` agrees with the filename. `curation/seed_scope.tsv:322862` records the 2026-09-13 one-source inclusion. The sole event at 2026-09-13T17:54:04Z matches the source/scope-generated wording. Ignored-inclusive history filename and content searches found no target-specific external history entry. No human-reviewed status is asserted.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the complete record and inspected evidence. The supplementary literature check remains bounded as stated above; it does not leave an asserted YAML claim unsupported.

## Recommended Edits

None required. Keep host, bacterial taxon, specimen voucher, marker and genome identity separate. Do not join the unrelated BioProject or similarly named endosymbiont on a partial identifier or label.

Any later authorized correction belongs in maintained upstream extraction inputs, `scripts/seed_from_sources.py` or `curation/seed_scope.tsv`, followed by regeneration, not a hand edit to this generated YAML.

## Follow-up Checks

No defect-specific repair is required. A later literature-enrichment task should inspect Table S2 before asserting its specimen-level accession mapping, and resolve BOLD identifiers at BOLD before making a current-database claim. Any additional strain/genome relationship needs an explicit eligible source chain. Before authorized regeneration, run the documented corpus reproduction, provenance, strict-schema, tests and publication gates.

## Additional Notes

This independent report is the only repository write for the target. No record, source, scope/history entry, generated page, branch, worktree or GitHub item was changed. Source comparisons did not review the host or any Eukaryota record. No paid research was performed.
