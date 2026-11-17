# YAML Record Review: Lactiplantibacillus plantarum subsp. plantarum NC8

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/lactiplantibacillus_plantarum_subsp_plantarum_nc8.yaml`
- Started UTC: 2026-10-08T01:37:08Z
- Finished UTC: 2026-10-08T01:46:37Z
- Verdict: needs curation

## Target

The entire 98-line generated `TaxonRecord` was read. It denotes `NCBITaxon:1036177`, Lactiplantibacillus plantarum subsp. plantarum NC8, rank STRAIN, domain BACTERIA, parent `NCBITaxon:337330`. The 11 root-first ancestors, EXACT grounding, SEEDED status, GTDB mapping and synonym, four NCBI synonyms, GTDB xref, code 11, zero listed strains, four attestations and seed event were inspected.

Identifier, label and slug resolve one target. Other organisms called NC8 or 36E were source-search candidates, not additional YAML reviews.

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/lactiplantibacillus_plantarum_subsp_plantarum_nc8.yaml` | Passed; no LinkML issues. |
| `just validate-strict data/taxa/bacteria/lactiplantibacillus_plantarum_subsp_plantarum_nc8.yaml --out /private/tmp/nc8-strict.tsv` | Passed; one file, zero errors; TSV header only. |
| Structured pinned-source comparison | Identity, rank, parent, code, all ancestors, NCBI synonyms, source counts, slug, scope and inline provenance match. GTDB values reproduce their input but have a semantic scope defect. |
| Exact status/inventory checks | No child, type-material, merged-ID or dropped-ID row for 1036177. |
| Public NCBI Taxonomy EFetch and Datasets | Current identity, rank, parent, lineage and four NCBI aliases agree. |
| Public NCBI assembly report | Current version, explicit GenBank/RefSeq pairing, BioSample, BioProject and culture-collection attribute verified. |
| Candidate source inspection | All 113 initial and expanded search-hit addresses read in full, including compressed native objects. |
| Live authority pages | CCUG and BacDive inspected. GTDB pages unavailable; StrainInfo HTML supplied only its application shell and its DOI page was inaccessible. Native StrainInfo data were inspected. |

Not run: whole-corpus `just verify-corpus`, QC, provenance, product-label, rendering and documentation gates. Focused comparisons do not replace those gates. No curator-added ontology graph occurs. Ignored-inclusive bounded searches found no separate target history artifact; inline history shape was covered by schema validation.

## Identity and Grounding

Current NCBI supports this strain concept and its subspecies parent, not equivalence with the entire species. All 11 ancestor identifiers, labels and ranks agree. NCBI supplies two synonym and two equivalent-name entries, all retaining NC8 or CCUG 61730; their exact-synonym treatment preserves strain scope. EXACT describes NCBI grounding, not a GTDB species-equivalence claim. [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1036177)

The primary collection lists NC8 and 36E for CCUG 61730. It uses the broader species label and notes its former subspecies listing; this does not establish that the current NCBI strain identifier is wrong. [CCUG 61730](https://www.ccug.se/strain?id=61730)

The species-only GTDB synonym at YAML lines 49-52 does not preserve that scope. The mapping, xref and attestation expose the same species concept without explaining that NC8 is a member, not its equivalent.

## Evidence

Pinned backbone row `data/raw/ncbitaxon_taxa.tsv:222303` and five native name objects at `data/catalog/ncbi_names-0005.jsonl.gz:31826` onward support the NCBI identity and aliases. The NCBITAXON attestation correctly records one NAME from snapshot 2026-09-13.

`data/raw/gtdb_mappings.tsv:1453` supplies closeMatch and 1,506. `extract_gtdb` in `src/taxonmech/extract.py:501` counts assemblies at the GTDB species node; the mapping projection at line 755 carries that species total to each mapping. It is not a target-strain genome count. `data/catalog/gtdb_genomes-0002.jsonl.gz:45299` instead identifies the individual NC8 genome, `RS_GCF_000247735.1`, as a nonrepresentative member of the species. Its NCBI taxon is 1036177 and its NCBI species taxon is 1590. Live GTDB genome/tree pages were attempted but unavailable; the current public species total was not independently verified.

GOLD count 1 is supported by `data/raw/gold_organisms.tsv:493` and the native Go0012110 organism, Gp0012110 project and Ga0012298 analysis chain. These connect NC8 to PRJNA67175, SAMN02470702, AGRI00000000 and IMG 2521172735. BVBRC genome 1036177.3 independently carries that accession chain. The Madin count 1 at `data/raw/madin_taxa.tsv:683` is an upstream TRAIT_ASSERTION count; the YAML asserts no particular phenotype. Counts with different units were not summed.

The live assembly response identifies current GCA_000247735.2 and explicitly paired current GCF_000247735.1, a 3,207,224-base, ten-contig assembly. Its BioSample SAMN02470702 links strain NC8 to `culture_collection=CCUG:61730`, grass silage and Sweden; PRJNA67175 is the sequencing project. This is an explicit accession-to-deposit bridge, not a short-designation join. The BioSample's free-text organism field says Lacticaseibacillus, conflicting with the current top-level Lactiplantibacillus taxonomy. Preserve that source-field discrepancy; it does not justify renaming the YAML. [NCBI assembly report](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000247735.2/dataset_report)

Native GenBank and RefSeq records corroborate the pair. Historical GCA_000247735.1 is suppressed and must not be represented as the current version. RefSeq's PRJNA224116 is not evidence that it is a different NC8 sample.

PubMed PMID 22493200 resolves DOI 10.1128/JB.00141-12 and PMC3347089. Its inspected title explicitly pairs NC8 with CCUG 61730; its abstract concerns sequencing this strain. Full text was not inspected: PMC presented a browser challenge, Europe PMC HTML was unavailable and the XML endpoint returned HTTP 500. No mechanistic or gene-level claim was inferred from the abstract. [Primary genome publication record](https://pubmed.ncbi.nlm.nih.gov/22493200/)

The YAML contains no publication citation, quoted snippet, gene, protein, mechanism or causal edge. iModulonDB was not applicable; absence from an expression resource was not treated as negative evidence.

## Completeness

BacDive 156438 and native StrainInfo SI-ID 411107 / SI-DP 919051 identify CCUG 61730 under the broader NCBI species taxon 1590. The StrainInfo object supplies NC8 and 36E, DOI 10.60712/SI-ID411107.2, and an exact CCUG deposit match to BacDive. The inspected native records do not mark it as type material. BacDive's live page corroborates the deposit and species taxon but has no sequence-information entries. [BacDive 156438](https://bacdive.dsmz.de/strain/156438)

Relevant local rows include `data/bacdive/records.jsonl.gz:78677`, `data/raw/bacdive_strains.tsv:78678`, `data/raw/culture_collection_strains.tsv:34186`, `data/straininfo/records.jsonl.gz:308994`, `data/straininfo/strain_links.tsv:54445` and the two SI strain/deposit rows in `data/straininfo/related_records.tsv.gz:128793` onward.

Thus `strain_count: 0` is consistent with the current exact-taxon-plus-descendants seeder, not a claim that NC8 lacks a deposit. The deposit is filed at an ancestor, outside this record's subtree. As documented in `docs/STRAININFO.md`, the overlay neither creates BacDive strains nor changes their classification. GTDB metadata gives only bare NC8; GOLD's culture field is empty. Neither satisfies the whole culture-collection-token join required by `docs/STRAIN_GENOMES.md`. Do not copy every parent-species strain into this record or silently retaxon the source deposit.

The verified BioSample collection attribute provides a concrete future enrichment route. A maintained, evidence-preserving source adapter and explicit same-deposit policy would be needed to publish that relationship here. This optional model extension is separate from the existing GTDB identity error; an empty optional genome slot is not itself a second finding.

Ignored-inclusive compressed-input searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Search terms included bounded taxon 1036177, NC8, CCUG 61730, the slug, 36E, the assembly/sample/project/WGS and GOLD/IMG identifiers, and candidate deposit/database IDs. All 113 matching addresses were fully inspected. Other NC8 genera, unrelated 36E isolates, accession-prefix collisions and equal numbers in different namespaces were rejected. The three AllTheBacteria hits concern Streptococcus pneumoniae, Staphylococcus aureus and Salmonella, not NC8.

Resolution searches additionally covered `data/taxa` and `reports`, including ignored files, with no prior target report. All five source metadata JSON files and history filenames were checked. No exact-target LPSN, BacDive, MediaDive or BactoTraits raw taxon row was found. These are bounded source findings, not assertions of global biological or literature absence.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

**Major: a GTDB species identity is promoted to an exact strain identity.** YAML lines 49-52 make Lactiplantibacillus plantarum an EXACT_SYNONYM of NC8. Lines 42-47, 65-66 and 76-81 accompany this with an unqualified species mapping/xref and the species-wide genome count. Native genome metadata and NCBI distinguish the strain from the species. Faithful reproduction of a source closeMatch does not justify that identity expansion.

The maintained owner is `src/taxonmech/seed.py:451`, whose identity decision accepts closeMatch without rank compatibility, followed by the xref/exact-synonym branch at lines 466-469. The source-count scope originates in `src/taxonmech/extract.py:501` and line 755. The primary taxon identity remains correct, so this is major rather than blocker.

## Recommended Edits

1. Make the maintained GTDB identity handling rank-aware. Prevent a GTDB species name from becoming an exact synonym or equivalence-style xref of a strain merely because the input says closeMatch. Preserve the four strain-scoped NCBI aliases.
2. Preserve the upstream GTDB assertion as provenance or explicitly labelled species membership, with its species-wide count identified as such. Do not silently relabel 1,506 as NC8 assemblies or automatically replace closeMatch with broadMatch: `docs/HARMONIZATION.md` defines the latter as an upstream pooling signal, not a generic rank-containment correction.
3. Add focused tests for this strain/species case and regenerate only through the authorized source/seed workflow. If representation requires a schema change, use the maintained non-vendored schema process. Do not patch the generated YAML or raw projection by hand.

Optional separate enrichment: use the accession-to-CCUG BioSample evidence in a maintained input adapter with a narrowly tested same-deposit rule. Preserve BacDive's source classification and the conflicting BioSample label as provenance. No such change was made in this review.

## Follow-up Checks

Test that NC8 remains a STRAIN under 337330, all NCBI aliases retain their scope, the species-only exact synonym disappears, and the GTDB count cannot be interpreted as strain-specific. Include species-level identity and pooled-mapping controls so a shared fix preserves valid existing behavior.

Run the documented seed dry-run and `just seed-canary NCBITaxon:1036177`, inspect the biological diff, and repeat both focused validators. Shared seed/extract changes require full corpus, QC, provenance, product-label, rendering and documentation gates. For any deposit enrichment, test exact CCUG matching, source classification preservation, historical/current assembly distinctions and rejection of other NC8/36E organisms.

Retry the live GTDB authority pages before claiming a current release count. Retrieve the primary full paper before adding any paper-derived experiment or mechanism. Neither unavailable check prevents the scope finding already supported by inspected source objects.

## Additional Notes

Scope: `curation/seed_scope.tsv:26089`, added 2026-09-12. Slug: `data/taxa/PATHS.tsv:14808`. Legacy path: `curation/legacy_page_paths.tsv:885`. Seed event remains `2026-09-13T17:54:04Z`.

Reviewed HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Unchanged target SHA256: `b37a134d14a21744996a73e2d5ab25009f4896741da621e54200dfc4fd09b795`. Only this new Markdown report was added for this individual review. No YAML, history, lifecycle, source snapshot, GitHub or worktree mutation occurred. Eukaryota was not re-reviewed.
