# YAML Record Review: Wolbachia endosymbiont of Liporrhopalum gibbosae

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_liporrhopalum_gibbosae.yaml`
- Started UTC: 2026-10-09T16:43:35Z
- Finished UTC: 2026-10-09T16:46:39Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` for `NCBITaxon:1036841` was read. It denotes Wolbachia endosymbiont of Liporrhopalum gibbosae, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2640676` (unclassified Wolbachia), code 11, grounding `EXACT` and status `SEEDED`. It contains zero inventoried strains, one NCBITAXON name attestation and one seeding event.

Ignored-inclusive filename search resolved this exact YAML and a distinct gibbosae-TIN sibling, but no prior own report. The target SHA-256 is `500b17883093074b3a55ebc53e00af8221deefe67cf27d9ba02a20825c0726d8`. Other records were inspected only for evidence disambiguation.

## Validation

Commands used the existing environment with `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/wolbachia_endosymbiont_of_liporrhopalum_gibbosae.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/wolbachia_endosymbiont_of_liporrhopalum_gibbosae.yaml --workers 1 --out /private/tmp/taxonmech-liporrhopalum-gibbosae-20261009-validation.tsv`: passed, one file and zero errors; inspected TSV is header-only.
- `uv run --offline python scripts/validate_history.py history`: passed earlier this turn, 17 valid records and zero invalid links; history was unchanged.
- Structured own-row comparisons passed for identity, all ancestors, source attestation, PATHS/scope entries and generated event wording.
- Live NCBI EFetch/Datasets taxonomy, exact and broader nucleotide searches, genome search and all seventeen returned GenBank entries were inspected. The own wsp record was read with its full annotations and references. The sixteen sibling markers were inspected using common/variant field grouping, including the output segment initially truncated by the display. Nucleotide lengths/alphabets were checked; sibling protein translations were reduced to length/hash checks. No protein-function or sequence-alignment validation is claimed.
- The own marker's DOI/PMID were verified through publisher text and PubMed EFetch. The PubMed website returned a browser challenge, so its API supplied the bibliographic metadata and abstract.
- Not checked: full-corpus reproduction, full-corpus schema/provenance/QC/tests and site drift. The documented `just verify-corpus` gate has no record selector; focused comparisons are not corpus reproduction.
- Not applicable: OAK curator-added graph and iModulonDB gene/component checks. The YAML has no graph, gene, regulator, pathway, trait or transcriptomics assertion; external marker context is not an added YAML claim.
- Not checked: independent BOLD resolution and supplementary specimen-to-result mapping for the linked publication. No study-wide phenotype, prevalence, supergroup or transmission mechanism is attributed to this taxon.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222635` and `data/catalog/ncbi_names-0005.jsonl.gz:32229` support the exact identifier, label, scientific-name status and 2026-09-13 snapshot. Rank, parent and code agree; exact, related and broad synonyms are empty.

Live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036841&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036841) agree. All eleven lineage entries match the local backbone. EFetch also matches the ten named ancestors after root, and Datasets includes root ID 1: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Alphaproteobacteria 28211; Rickettsiales 766; Anaplasmataceae 942; Wolbachieae 952; Wolbachia 953; unclassified Wolbachia 2640676.

The YAML denotes the bacterial endosymbiont, not its host. The separately indexed gibbosae-TIN concept is `NCBITaxon:1094257`, with local backbone row 235303, name row 47532 and scope row 333616. It has the separate YAML stem `wolbachia_endosymbiont_of_liporrhopalum_gibbosae_tin`. A shared label prefix or clone-name component does not establish a merger or synonym.

The broader nucleotide search translates the host-name component to Kradibia gibbosae in its query expansion. That search behavior does not authorize renaming the bacterial record: both live bacterial taxonomy endpoints retain the exact Liporrhopalum-based label.

## Evidence

The NCBITAXON attestation counts one name, not seventeen sequences, specimens or cultures. Its ID, label, count, unit and snapshot date match the own inventory. `strain_count: 0` describes classified BacDive coverage, not biological absence.

The [exact non-expanded nucleotide search](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=nuccore&term=txid1036841%5BOrganism%3Anoexp%5D&retmode=json&retmax=100) returned one entry: [JQ342228.1](https://www.ncbi.nlm.nih.gov/nuccore/JQ342228.1), clone Ligi-F-TIN-HN-16-WSP. It carries the exact organism and `taxon:1036841`, host Liporrhopalum gibbosae and isolation source female. It annotates a partial wsp gene/CDS and outer surface protein, code 11, protein accession AFX95996.1. Declared and actual nucleotide lengths are 492 bases with an A/C/G/T-only alphabet. Its Sanger/Bioedit assembly-method comment describes sequence processing, not a complete-genome assembly or culture accession.

GenBank directly links [Yang et al. 2012, DOI 10.1371/journal.pone.0048882](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0048882), and [PMID 23145008](https://pubmed.ncbi.nlm.nih.gov/23145008/). Publisher and PubMed metadata agree on the study. The inspected article describes wsp screening and sequence analyses in a Ficus benjamina-associated community, and its submitted-accession range includes JQ342228. It does not, in the inspected main-text material, establish a particular phenotype, transmission event or recombinant assignment for this exact clone. Main-text name searches did not find Liporrhopalum or gibbosae; supplementary specimen mapping was not checked. The accession's direct source qualifier is the narrow support for host association, and community-wide conclusions are not generalized to this record.

The [broader host-name plus Wolbachia query](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=nuccore&term=%22Liporrhopalum%20gibbosae%22%5BAll%20Fields%5D%20AND%20Wolbachia%5BAll%20Fields%5D&retmode=json&retmax=100) returned seventeen entries: the own wsp accession plus all sixteen accessions from [JF902464.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902464.1) through [JF902479.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902479.1), inclusive. Every one of those sixteen COI entries carries gibbosae-TIN and `taxon:1094257`, not the target ID.

The sibling entries contain partial COI annotations, code 11, BIOUG specimen vouchers YLCFX471-08.w through YLCFX486-08.w and BOLD cross-references ASWFW073-10.COI-5P through ASWFW088-10.COI-5P. They describe two Hainan collection sets, 09-Nov-2006 and 05-Apr-2007. Their declared/actual lengths agree, ranging from 611 to 642 bases; all include N ambiguity. They retain an unpublished Smith reference and a 01-May-2011 submission. These source-specific specimens and references are not transferred to the target. The own wsp clone's TIN component alone does not override the different explicit taxonomy assignments.

The [NCBI genome dataset query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1036841/dataset_report) returned an empty object. That supplies no positive assembly evidence, not proof that no genome exists anywhere. Neither wsp nor COI markers establish eligible culture-to-genome links.

## Completeness

Gitignore-independent searches covered hidden and compressed files under `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, using bounded ID 1036841 and label/slug-compatible spelling. All eight candidates were read in full: four native JSON and four TSV rows. All five source `SOURCE.json` files were parsed without a target match. A follow-up ignored-inclusive compressed search for JQ342228, its clone name, PMID and DOI found no match in those roots. These negative findings are limited to the inspected snapshots and search terms.

Two native rows are unrelated Stenotrophomonas maltophilia ZSL2493, taxon 40324, connected to BioProject PRJNA1036841: BV-BRC 40324.3724 and NCBI GCA_047782825.1/GCF_047782825.1, BioSample SAMN38153187, replicons CP180589 through CP180591. The shared numeric suffix is a project identifier, not a taxonomic or culture link to this Wolbachia record. The remaining six candidates are own/sibling name, backbone and scope rows.

Complete own-ID inventory scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits assertion, type-material row, merged-ID row, dropped row or child. No inspected source supplies an eligible own culture-to-genome chain. Optional synonyms, nomenclature, mappings, xrefs, strain/genome lists, experimental evidence and causal graphs are appropriately empty. Marker/literature context can support later authorized enrichment but does not demonstrate a missing required field in this seeded concept.

`data/taxa/PATHS.tsv:15167` agrees with the filename. `curation/seed_scope.tsv:322868` records the 2026-09-13 one-source inclusion. The sole event at 2026-09-13T17:54:04Z matches the generated source/scope wording. Ignored-inclusive history filename/content searches found no target-specific external history entry. No human-reviewed mapping status is asserted.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the complete YAML and inspected evidence. The publication-mapping limitation does not leave an asserted YAML claim unsupported, because the record contains no experimental trait or study-derived mechanism claim.

## Recommended Edits

None required. Preserve the exact bacterial taxonomy, distinguish the gibbosae-TIN sibling and keep markers, clones and vouchers outside genome/culture counts. Do not transfer the unrelated Stenotrophomonas genome through a project-number suffix.

Any later authorized correction belongs in maintained upstream extraction inputs, `scripts/seed_from_sources.py` or `curation/seed_scope.tsv`, followed by regeneration. Do not hand-edit this generated YAML. A later literature enrichment needs a claim-specific evidence placement and independently resolved specimen-to-result mapping, not a study-wide inference.

## Follow-up Checks

No defect-specific repair is required. Before using Yang et al. for a taxon-specific experimental claim, inspect the relevant supplementary/figure mappings and distinguish the own wsp clone from sibling COI vouchers. Independently resolve BOLD references before making current BOLD claims. New strain/genome associations require explicit eligible culture-deposit source chains. Before authorized regeneration, run the documented corpus reproduction, provenance, strict-schema, tests and publication gates.

## Additional Notes

This new independent report is the only repository write for the target. No record, source, scope/history entry, generated page, branch, worktree or GitHub item changed. The host, sibling and other source organisms were disambiguation context only; no Eukaryota record was reviewed. No paid research was performed.
