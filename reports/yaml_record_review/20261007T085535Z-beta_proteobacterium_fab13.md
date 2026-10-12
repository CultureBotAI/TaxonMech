# YAML Record Review: beta proteobacterium FAB13

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/beta_proteobacterium_fab13.yaml`
- Started UTC: 2026-10-07T08:49:57Z
- Finished UTC: 2026-10-07T08:55:35Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord`: `NCBITaxon:1035630`, beta proteobacterium FAB13, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:33809` (unclassified Betaproteobacteria), seven root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` mapping status and `strain_count: 0`. It has one NCBI name attestation and one seed event.

No synonyms, nomenclature, taxonomy mappings, culture deposits, genomes, definition, literature evidence, discussions, datasets, replacement or causal graphs are asserted. The label is not a verified culture accession. Generated records remain read-only. Maintained source/extraction inputs and `src/taxonmech/seed.py` own future fixes; scope and slug ownership are `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv`.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and offline uv dependency resolution.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/beta_proteobacterium_fab13.yaml` | Exit 0; No issues found. |
| `just validate-strict data/taxa/bacteria/beta_proteobacterium_fab13.yaml --out /private/tmp/fab13-strict.tsv` | Exit 0; one file, zero ERROR rows. |
| `cat /private/tmp/fab13-strict.tsv` | Actual TSV read; header only. |
| Structured backbone, full lineage, seven inventories, path, scope and attestations | Bounded checks passed. |
| Exact type-material, merged-ID and dropped-record scans | No target row. |
| Live NCBI Taxonomy EFetch and Datasets | Identity and complete ancestry agree. |
| Exact-taxid Assembly and nuccore searches | Assembly 0 with phrase-not-found warning; nuccore 1, complete metadata inspected. |

Not checked: `just verify-corpus`, `just qc`, full-corpus schema validation, tests, provenance hashing, generated-page drift, documentation statistics and vendored checks. Bounded comparisons are not byte-for-byte corpus reproduction.

`just validate-products` was not run: configured OAK targets are curator-added graph nodes, absent here; NCBI taxonomy is excluded. No literature/internal evidence references occur in the YAML. The seed event was checked. `just validate-history` was not run because ignored-independent content/path searches found no target history artifact.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:222158` agrees on ID, label, rank, parent, genetic code, empty synonyms and snapshot `2026-09-13`. The complete native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31638` agrees. Unique path and scope rows are `data/taxa/PATHS.tsv:14658` and `curation/seed_scope.tsv:322425`.

All seven ancestors match the committed parent chain: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Betaproteobacteria and unclassified Betaproteobacteria, with identical IDs, labels, ranks and order. Live EFetch confirms species rank, parent 33809, code 11, no alternate names and the six non-root ancestors; Datasets includes root. No retirement or replacement was found in inspected lifecycle sources. [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035630&retmode=xml), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035630)

This species-rank placeholder satisfies record scope without claiming a validly published species binomial. Its unclassified placement does not authorize inventing an order, family or genus. `EXACT` applies to the NCBI concept, not a culture deposit or sequence-based reidentification.

## Evidence

The sole `NCBITAXON` attestation agrees on ID, label, count 1, unit `NAME` and snapshot note. It does not count strains or genomes. A complete backbone scan found no direct children. Exact scans found no target row in `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`.

Exact-taxid nuccore UID 333952292 resolves to `JF799919.1`, a 1,405-nt partial 16S rRNA marker. Its organism is beta proteobacterium FAB13, its strain qualifier is FAB13 and its explicit cross-reference is `taxon:1035630`. The rRNA feature is partial at both ends. [GenBank JF799919.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799919.1)

The marker describes active-layer permafrost in China/Qinghai-Tibet. It cites an unpublished permafrost bacterial-diversity study and a direct submission by Li, Xu and Zhang. Submission was 11 April 2011; creation/update were 30 May 2011. No DOI, PMID, culture-collection, BioSample, BioProject or assembly link is supplied. All metadata were inspected, excluding only sequence strings and translation/transcription payloads. This is submission provenance, not independent published species confirmation. A marker is not a genome, and locality alone does not establish cold-growth or another phenotype.

All six non-target local matches were read completely:

| Native source address | Actual match and exclusion |
| --- | --- |
| `data/bvbrc/bvbrc-0022.jsonl.gz:24500` | BV-BRC 562.161718, Escherichia coli TATVAM-FAB13, taxid 562, PRJNA1026516, SAMN38138625 and JAXUAQ000000000. Not the permafrost taxon. |
| `data/catalog/ncbi_genbank-0042.jsonl.gz:43541` | GCA_046537495.1, E. coli TATVAM-FAB13, taxid/species taxid 562, PRJNA1026516, SAMN38138625 and JAXUAQ000000000.1. |
| `data/catalog/ncbi_refseq-0007.jsonl.gz:2025` | GCF_046537495.1, the same E. coli source identity, SAMN38138625, PRJNA224116 and JAXUAQ000000000.1. |
| `data/catalog/gtdb_genomes-0016.jsonl.gz:48917` | RS_GCF_046537495.1, the same NCBI E. coli TATVAM-FAB13 identity. GTDB assigns ECMA0423 sp047199055 within Gammaproteobacteria/Enterobacterales/Enterobacteriaceae. Preserve that source disagreement on the unrelated genome; neither classification belongs to this target. |
| `data/catalog/allthebacteria.tsv.xz:66275` | Staphylococcus aureus, SAMEA1035630, ERR083835 and ERZ3070818, with META_FAIL. The matching sample digits are not a taxonomy identifier. |
| `data/catalog/allthebacteria.tsv.xz:551213` | Escherichia coli, SAMEA3375248, ERR1035630 and ERZ3259030. The matching digits occur in a run accession, not a taxon field. |

The author-uploaded full text of Hijam et al. (Indian Journal of Biotechnology 19, 2020, pp. 192-205) describes FAB1-FAB19 from gut samples collected in Manipur, India. Its results compare Enterobacter sp. FAB8 morphologically with FAB13; its FAB accession range is KX242115-KX242133. These inspected methods/results support a different provenance, not an identity link to the 2011 Chinese permafrost marker. No cellulase observation is transferred. This is an identity exclusion based on source context, not a sequence comparison. [Author-uploaded article](https://www.researchgate.net/publication/350122694_Identification_and_determination_of_cellulase_activity_of_cellulose_degrading_microorganisms_from_earthworm_species_of_different_habitats_of_North_East_India)

No gene, regulator, pathway, stress-response or transcriptomics assertion in the YAML requires iModulonDB. A marker accession found during review does not create such an assertion.

## Completeness

Zero BacDive strains and optional omissions agree with inspected source scope. A marker strain qualifier is not a culture deposit. Seeded records do not require literature annotations or an inferred genus. No required gap was found.

Both local stages included ignored/hidden files and compressed catalogs using `rg --no-ignore --hidden -n -z -i`, across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All five excluded `SOURCE.json` files were separately parsed in full per stage; history filenames were independently traversed.

The initial stage used taxid 1035630 as a complete digit run, exact label/slug and FAB13 with case/separator variants. Numeric boundaries exclude substrings within longer numbers; returned rows were checked structurally. All nine matched lines were read: three target rows and the six excluded lines above. The accession stage searched JF799919 with optional .1 and found zero lines. Neither stage found matching metadata values or history paths. Negative local findings include ignored files and are bounded to these roots and terms.

Web queries used proteobacterium with FAB13, FAB13 with bacteria, and JF799919. The standalone accession search returned no results. Only inspected source text supports the distinctions above; antibody, conference-code and industrial search hits were not used as evidence. No inspected exact-target publication or supported culture-deposit/genome chain was established. Exhaustive literature retrieval and sequence similarity were not performed. The exact-taxid Assembly zero includes a phrase-not-found warning and does not exclude assemblies filed under another identity.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the YAML within the inspected scope. Identity, full lineage, source provenance, zero strain count and seed history agree. Shared short labels do not establish strain equivalence.

## Recommended Edits

None required. Do not patch generated YAML, import TATVAM-FAB13 genomes or the unrelated article's phenotype observations, count JF799919.1 as a genome, or promote `SEEDED` to `REVIEWED`.

Optional marker enrichment requires maintained-input support in `src/taxonmech/seed.py` with tests under `docs/CURATION.md`, preserving the exact organism, taxid, strain qualifier and accession with provenance. A taxonomy-source correction would belong upstream and in an authorized refresh through `conf/ncbi_taxdump.yaml`, `scripts/extract_source_inventory.py` and guarded seeding. No such correction is supported here.

## Follow-up Checks

- Require an exact culture-deposit and genome-source chain; keep markers, taxon labels, sample/run accessions and genome identifiers separate.
- Before importing literature phenotypes, establish the exact isolate using source provenance and stable identifiers rather than the bare FAB13 alias.
- After authorized maintained-input changes, rerun both single-record validators, `just verify-corpus` and `just qc`; validate any new history artifact. Full-corpus gates remain skipped here.

## Additional Notes

Primary NCBI taxonomy, Datasets, sequence-index and nucleotide reads succeeded. Publisher handle/PDF web retrieval timed out. The publisher PDF was downloaded successfully to scratch storage, but not parsed or visually inspected: Poppler commands and tested Python PDF parsers were unavailable. The author-uploaded full text supplied the inspected methods and results. Figure 7 labels and individual KX accession identities were not verified and are not relied on. No access failure was treated as negative biological evidence.

Seed wording agrees with scope and attestation. Timestamp `2026-09-13T17:54:04Z` is the newest raw/ATB/StrainInfo manifest timestamp selected by `src/taxonmech/seed.py:_seed_timestamp`, not a review date; code and all three timestamps were inspected this turn.

The entire YAML was reread unchanged before this report. An ignored-independent filename search found no previous report for this stem. Only this new report is added; no record, inventory, page, old report, history, status, GitHub object or cross-repository artifact is changed. No paid research or outbound contact was used.
