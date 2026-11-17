# YAML Record Review: Wolbachia endosymbiont of Ceratosolen cornutus

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_ceratosolen_cornutus.yaml`
- Started UTC: 2026-10-09T16:32:32Z
- Finished UTC: 2026-10-09T16:37:32Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` for `NCBITaxon:1036839` was read. Its label is Wolbachia endosymbiont of Ceratosolen cornutus; rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2640676` (unclassified Wolbachia), genetic code 11, grounding `EXACT`, status `SEEDED`. The record contains zero inventoried strains, one NCBITAXON name attestation and one seeding event.

Ignored-inclusive filename search resolved this exact YAML and a distinct cornutus-AUR sibling, but no prior own report. The target SHA-256 is `30153dee314f144de4431a75ec2be02e7191470ba0ba254ede127514acdaa4ed`. Other taxa were inspected only to disambiguate candidate evidence.

## Validation

Commands used the existing environment with `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/wolbachia_endosymbiont_of_ceratosolen_cornutus.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/wolbachia_endosymbiont_of_ceratosolen_cornutus.yaml --workers 1 --out /private/tmp/taxonmech-ceratosolen-cornutus-20261009-validation.tsv`: passed, one file and zero errors; inspected TSV is header-only.
- `uv run --offline python scripts/validate_history.py history`: passed this turn, 17 valid records and zero invalid links.
- Structured own-row comparisons passed for identity, all ancestors, attestation fields, PATHS/scope entries and generated event wording.
- Current NCBI dump identity and complete lineage comparison passed. Its download checksum matched the published checksum. Full `nodes.dmp`, `names.dmp`, `merged.dmp`, `delnodes.dmp` and `citations.dmp` member scans used the repository's `taxonmech.ncbi_taxdump.fields` parser; only exact target/sibling and required ancestor matches were evaluated.
- All sixteen broader nucleotide-search candidates were fetched. Complete source qualifiers, annotations and references were inspected through common/variant field grouping. Nucleotide lengths and alphabets were checked; amino-acid strings were reduced to length/hash checks, not interpreted as functional evidence.
- Not checked: full-corpus reproduction, full-corpus schema/provenance/QC/tests and site drift. The documented `just verify-corpus` gate has no record selector. Focused comparisons are not corpus reproduction.
- Not applicable: OAK curator-added graph and iModulonDB gene/component checks. The YAML contains no causal graph, gene, regulator, pathway, trait or transcriptomics assertion.
- Limitation: live browser/EFetch/Datasets responses conflict with positive ESummary, name-search and current-dump evidence; the responses are preserved below. BOLD references and sibling publication mappings were not independently resolved because they do not support target claims.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222633` and `data/catalog/ncbi_names-0005.jsonl.gz:32227` support the exact identifier, scientific name, species rank, parent, code and 2026-09-13 snapshot. All exact, related and broad synonym fields are empty.

All eleven root-first lineage entries match both the local backbone and the inspected 2026-10-09 primary NCBI dump: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Alphaproteobacteria 28211; Rickettsiales 766; Anaplasmataceae 942; Wolbachieae 952; Wolbachia 953; unclassified Wolbachia 2640676. Names, ranks and parent links agree. This is the bacterial endosymbiont, not its Ceratosolen host; species rank does not establish cultured type material or formal nomenclatural standing.

NCBI's live interfaces were inconsistent during review:

- [Taxonomy ESummary](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=taxonomy&id=1036839&retmode=json) reports taxon 1036839 as active, with the exact scientific name, species rank and bacterial GenBank division. [Exact scientific-name search](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=taxonomy&term=%22Wolbachia%20endosymbiont%20of%20Ceratosolen%20cornutus%22%5BScientific%20Name%5D&retmode=json&retmax=100) returns this one ID.
- [EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036839&retmode=xml) returned an empty TaxaSet, including a reordered-parameter retry. [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036839) reported an unrecognized identifier, including a complete-content retry. The directly inspected [legacy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1036839&mode=Info) reported no result.
- The [primary taxonomy dump](https://ftp.ncbi.nlm.nih.gov/pub/taxonomy/taxdump.tar.gz), listed by NCBI as modified 2026-10-09, independently contains the exact active node and scientific name: `nodes.dmp:835857`, `names.dmp:1634205`. No own or cornutus-AUR row occurs in its merged/deleted member scans. The exact own label, rank, parent, code and complete lineage match the YAML.

The primary dump and positive live responses support the record despite the conflicting service responses. The cause of that interface discrepancy remains unknown; no retirement, merger or replacement ID is inferred.

The similarly named cornutus-AUR concept is `NCBITaxon:1094253`, not the target. Its local backbone/name rows are 235299 and 47528; the current dump separately contains it at `nodes.dmp:886624` and `names.dmp:1714245`. It has its own YAML stem `wolbachia_endosymbiont_of_ceratosolen_cornutus_aur`. No synonym or merge evidence joins the two IDs.

## Evidence

The sole NCBITAXON attestation counts one name, not nucleotide sequences, specimens or strains. Source ID, label, count, unit and snapshot date agree with the own inventory. `strain_count: 0` concerns classified BacDive coverage, not biological absence.

The [exact non-expanded nucleotide query](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=nuccore&term=txid1036839%5BOrganism%3Anoexp%5D&retmode=json&retmax=100) returned zero IDs with a phrase-not-found diagnostic. That is a bounded query result, not proof of universal sequence absence.

The [broader host-name plus Wolbachia query](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=nuccore&term=%22Ceratosolen%20cornutus%22%5BAll%20Fields%5D%20AND%20Wolbachia%5BAll%20Fields%5D&retmode=json&retmax=100) returned sixteen entries. All were inspected: every accession from [JF902387.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902387.1) through [JF902402.1](https://www.ncbi.nlm.nih.gov/nuccore/JF902402.1), inclusive. Every entry names cornutus-AUR and carries `taxon:1094253`. They are not exact-target evidence.

These sibling-specific records annotate partial COI gene/CDS markers with code 11, specimen vouchers YLCFX195-08.w through YLCFX210-08.w and BOLD cross-references ASWFW036-10.COI-5P through ASWFW051-10.COI-5P. Source qualifiers specify Limushan, Hainan, China, 12-Apr-2007. All declared and actual nucleotide lengths are 642 bases; the final two accessions include N ambiguity. Their unpublished Smith reference and 01-May-2011 direct submission are not reassigned to the target. Marker vouchers are not culture deposits and these sequences are not assemblies.

The [NCBI genome dataset query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1036839/dataset_report) returned an empty object. With the taxonomy interface limitations above, this supplies no positive assembly evidence and is not interpreted as proof of genome absence.

## Completeness

Gitignore-independent searches covered hidden and compressed files under `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, using bounded ID 1036839 and label/slug-compatible spelling. All sixteen candidates were read in full: twelve native JSON and four TSV rows. All five source `SOURCE.json` files were parsed without a target match. These are snapshot-scoped findings, not claims about all external data.

The non-target numeric matches were explicitly excluded:

- Four Staphylococcus aureus strains, taxon 1280, share BioProject PRJNA1036839: 17CS1042/GCA_033798685.1, V482/GCA_033798745.1, V315/GCA_033798765.1 and 15V8707/GCA_033798785.1. Four NCBI catalog rows, four BV-BRC rows and the V482 GTDB row refer to those organisms. Their BioSamples, available RefSeq pairs and V482 annotation exclusion flag are source context, not Wolbachia evidence.
- Helicobacter pylori Hp P-74, taxon 992091, GCA_000274345.1/GCF_000274345.1, has GTDB contig N50 1036839. That metric is not an NCBI taxonomy association.
- The remaining six rows describe the own and cornutus-AUR name, backbone and scope entries; the sibling is not an alias.

Complete own-ID scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits assertion, local type-material row, merged-ID row, dropped row or child. No inspected source supplies an eligible own culture-to-genome chain. Optional synonyms, nomenclature, mappings, xrefs, strain/genome lists, experimental evidence and causal graphs are appropriately empty.

`data/taxa/PATHS.tsv:15165` agrees with the filename. `curation/seed_scope.tsv:322866` records the 2026-09-13 one-source inclusion; the sole event at 2026-09-13T17:54:04Z matches the generated source/scope wording. Ignored-inclusive history filename/content searches found no target-specific external history entry. The YAML does not claim human review.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the complete record and inspected evidence. The inconsistent live services remain a documented external limitation, not evidence of a wrong or retired taxon: the verified current primary dump supports all asserted taxonomy fields.

## Recommended Edits

None required. Do not merge cornutus with cornutus-AUR, copy sibling markers or link unrelated genomes using numeric substring matches.

Any future authorized taxonomy correction belongs in the snapshot pinned by `conf/ncbi_taxdump.yaml`, its extraction through `src/taxonmech/ncbi_taxdump.py` and maintained inventory-generation code, or the seeding/scope inputs as appropriate, followed by regeneration. Do not hand-edit this generated YAML or replace the pinned snapshot with the diagnostic download during a review.

## Follow-up Checks

Recheck the conflicting NCBI browser/EFetch/Datasets interfaces before relying on their responses for a later refresh. Retain dated dump checksums and compare nodes, names, merged and deleted entries before asserting a retirement or replacement. Future strain/genome enrichment needs an explicit eligible culture-deposit source chain. Before authorized regeneration, run the documented corpus reproduction, provenance, schema, tests and publication gates.

## Additional Notes

The temporary primary dump is `/private/tmp/taxonmech-ncbi-taxdump-20261009.tar.gz`, 79,794,570 bytes. Its MD5 `8fa90f979abdf24614da0f4e2ac39dfb` matches the [published checksum](https://ftp.ncbi.nlm.nih.gov/pub/taxonomy/taxdump.tar.gz.md5); SHA-256 is `26505b54d0cffe428eb70aecea005c18bce0ac5d7a51fa55fb7cf805e1fa2290`. Archive members were streamed without extraction into the repository. This diagnostic current standard dump is distinct from the configured 2026-09-13 extended source snapshot. The current dump's target/sibling citation-member scan had no match.

This new report is the only repository write for the target. No record, source, history/scope entry, generated page, branch, worktree or GitHub item changed. Other organisms were disambiguation context only; no Eukaryota record was reviewed. No paid research was performed.
