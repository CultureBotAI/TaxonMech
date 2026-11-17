# YAML Record Review: Cardinium endosymbiont of Nitocra spinipes

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/cardinium_endosymbiont_of_nitocra_spinipes.yaml`
- Started UTC: 2026-10-10T01:29:07Z
- Finished UTC: 2026-10-10T01:31:42Z
- Verdict: pass

## Target

The complete 60-line generated `TaxonRecord` was read. `NCBITaxon:1037369` denotes Cardinium endosymbiont of Nitocra spinipes, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2641185` (unclassified Candidatus Cardinium), genetic code 11, grounding `EXACT`, status `SEEDED`.

It carries twelve ancestors, no synonym list, zero inventoried BacDive strains, one NCBITAXON name attestation and one seed event. The concept denotes the bacterium, not its eukaryotic host or every Cardinium-associated host population. No host YAML was opened.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/cardinium_endosymbiont_of_nitocra_spinipes.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/cardinium_endosymbiont_of_nitocra_spinipes.yaml --out /private/tmp/taxonmech-nitocra-20261010-validation.tsv --workers 1`: one file, zero errors; output reread, header only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links, run earlier this turn; history was not changed.
- Structured comparisons verified own identity, every ancestor, code, empty synonym columns, attestation, index/scope entries and seed reason. Complete backbone scanning found no direct child. Exact own-ID type-material, merged-ID and dropped scans found none.
- The native name row, complete live taxonomy responses and metadata of all seven exact-taxonomy nucleotide hits were inspected. The original study's PubMed abstract and identifiers and relevant publisher methods, results and discussion were read.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, original-source replay, rendering and publication gates. No causal graph is asserted, so `just validate-products` has no applicable nodes. Focused source agreement is not corpus reproduction.
- No independent sequence alignment, vector-trimming audit, phylogenetic reconstruction, experimental reanalysis or genome comparison was performed. Figure images, supplemental chemical-analysis methods and later cross-host literature were not independently audited; the report relies on inspected primary text and sequence annotations.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222735`, [NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037369&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037369) agree on exact scientific name, species rank, parent and code.

The root-first lineage is root, cellular organisms, Bacteria, Pseudomonadati, FCB group, Bacteroidota/Chlorobiota group, Bacteroidota, Cytophagia, Cytophagales, Amoebophilaceae, Candidatus Cardinium and unclassified Candidatus Cardinium. Every stored ancestor ID, label and rank matches the pinned backbone. EFetch confirms the chain below root; Datasets includes root 1. FCB group and Bacteroidota/Chlorobiota group retain their authority `CLADE` ranks.

`data/catalog/ncbi_names-0005.jsonl.gz:32354` is the exact own scientific-name row. Pinned synonym columns are empty and live EFetch supplies no synonym. `EXACT` concerns this NCBI concept, not valid publication of a species name or equivalence to Candidatus Cardinium hertigii. The genus's Candidatus wording does not authorize changing the target label or assigning another species.

## Evidence

The sole NCBITAXON attestation has exact own ID/label, count 1, unit `NAME`, snapshot 2026-09-13. It counts a name assertion, not host individuals, molecular clones, genomes or culture deposits.

A live exact nucleotide query, `txid1037369[Organism:exp]`, returned seven entries. All inspected annotations explicitly name this organism, `taxon:1037369` and host Nitocra spinipes. All are partial 16S rRNA markers with partial feature endpoints:

| Accession | Source designation | Length |
| --- | --- | --- |
| [JQ364959.1](https://www.ncbi.nlm.nih.gov/nuccore/JQ364959.1) | isolate EG1-6 | 795 bases |
| [FR878031.1](https://www.ncbi.nlm.nih.gov/nuccore/FR878031.1) | clone 29 | 911 bases |
| [FR878030.1](https://www.ncbi.nlm.nih.gov/nuccore/FR878030.1) | clone 27 | 911 bases |
| [FR878029.1](https://www.ncbi.nlm.nih.gov/nuccore/FR878029.1) | clone 26 | 846 bases |
| [FR878028.1](https://www.ncbi.nlm.nih.gov/nuccore/FR878028.1) | clone 25 | 846 bases |
| [FR871411.1](https://www.ncbi.nlm.nih.gov/nuccore/FR871411.1) | Nitocra_clone_2 | 842 bases |
| [FR871410.1](https://www.ncbi.nlm.nih.gov/nuccore/FR871410.1) | Nitocra_clone_1 | 842 bases |

Declared and actual lengths agree. JQ364959 contains ambiguous R/Y bases; the six FR entries use A/C/G/T. FR878028-FR878031 carry an environmental-sample qualifier and specify DNA extracted from the host in laboratory culture; FR871410-FR871411 specify total copepod extracts. Host laboratory culture does not establish an axenic bacterial culture or a culture-collection deposit. Matching sequence hashes within FR878030/FR878031 and FR878028/FR878029 do not establish strain or genome equivalence. The seven-hit query is not a global sequence census.

JQ364959 explicitly cites [Edlund et al., PMID 22427962](https://pubmed.ncbi.nlm.nih.gov/22427962/), DOI 10.1371/journal.pone.0033107, PLoS ONE 7(3):e33107 (2012). The [primary study](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0033107) lists the FR accession ranges and JQ364959 in its methods. It reports Cardinium-associated ribotypes from N. spinipes and proposes phylogenetic group D. Specific PCR detected Cardinium in controls as well as antibiotic treatments. The discussion states that absolute bacterial abundance and sex ratios were not measured and does not resolve causal contributions to host responses. Thus increased relative representation is not proof of absolute proliferation or a target-specific susceptibility phenotype, and reproductive manipulation remains unproven in this host.

The six FR entries retain unpublished-reference metadata with older working titles; those titles are not experimental evidence of reproductive effects. The published connection is supported by the article's accession ranges and JQ364959's explicit bibliography, not by silently relabeling every old reference.

The YAML asserts taxonomy and provenance only. Its authority name is retained without adding a mechanistic localization, antibiotic-resistance, reproductive-manipulation or causal-graph claim.

## Completeness

An ignored-inclusive, compressed-content-inclusive `rg --no-ignore --hidden -n -z -i` search covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Terms included bounded 1037369, Cardinium near Nitocra, Nitocra spinipes with separators, and the target slug. All three matching lines were inspected: own backbone, native name and scope rows.

A follow-up ignored/compressed-inclusive search for all seven marker accessions over the same roots returned no matches. Five SOURCE.json files were separately parsed without a target match. Gitignore-independent filename enumeration under the taxon corpus and report directory for the target ID/slug found only this bacterial YAML and no prior report. History filename inspection found no target-specific filename. These are bounded repository checks, not global absence claims or a review of the host corpus.

Complete structured own-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row. No immediate backbone child supplies descendant inventory. Zero correctly counts inventoried BacDive strains, not molecular clones or the existence of associated bacteria. No source-supported culture-deposit/genome chain was established. Partial 16S entries do not indicate omitted genomes.

Optional definitions, nomenclature, mappings, record-level evidence and causal graphs need not be invented. iModulonDB was not applicable to this taxonomy-only record: marker-based detection and ecological experiments do not create a record gene or transcriptomics assertion. No adapter run or global dataset absence is claimed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected record and bounded source scope. Identity, rank, lineage, provenance, source-count semantics and seeded status are supported. The molecular host association is supported without inflating it into an unmeasured causal mechanism. Skipped corpus checks and the explicitly unaudited analyses remain limitations.

## Recommended Edits

None required. Preserve the bacterial concept, authority label/rank, unclassified Candidatus Cardinium placement and zero BacDive count. Do not turn molecular clone labels into culture deposits, 16S sequences into genomes, or study hypotheses into demonstrated reproductive or antibiotic phenotypes.

Future authorized corrections belong in maintained source/harmonization inputs, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` or `curation/seed_scope.tsv`, according to ownership, followed by documented extraction/seeding. No supported defect requires a change here; generated YAML must not be hand-edited.

## Follow-up Checks

Any future mechanistic enrichment needs target-host-specific experiments and evidence for the precise claimed effect. Preserve the distinction between host association, cellular localization, relative abundance, susceptibility and reproductive causation. New deposit/genome links require an explicit source-supported identity chain and whole culture accessions, without borrowing assemblies from Cardinium in other hosts.

After an authorized source refresh, rerun schema/strict/history validation and documented full-corpus reproduction/QC gates. Focused matching does not replace those checks.

## Additional Notes

- YAML SHA-256: `cc9c2409f34418107f46de57ec8a4ce519f0b2be6c522c87f8bc0bf9f343dab1`.
- `data/taxa/PATHS.tsv:15283` and `curation/seed_scope.tsv:322960` uniquely resolve the target. The seed retains 2026-09-13T17:54:04Z and the exact one-source scope reason.
- Read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Only this new report was added for this target. No record, maintained input, schema, history, page, branch, worktree or GitHub state was changed. No review status was promoted and no Eukaryota YAML was opened.
