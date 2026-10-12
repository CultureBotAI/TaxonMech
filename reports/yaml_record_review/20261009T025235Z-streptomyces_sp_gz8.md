# YAML Record Review: Streptomyces sp. GZ8

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_sp_gz8.yaml`
- Started UTC: 2026-10-09T02:40:50Z
- Finished UTC: 2026-10-09T02:52:35Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1036530`: species rank, Bacteria, parent `NCBITaxon:2593676`, ten root-first ancestors, genetic code 11, `EXACT` grounding and `SEEDED` status. It has zero represented BacDive strains, one NCBITAXON name attestation and one seed event dated 2026-09-13T17:54:04Z. Synonyms, nomenclature, mappings, strain/genome links, evidence and graphs are unasserted optional fields.

Ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved one target YAML and no prior target report. Generated YAML is not the maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/streptomyces_sp_gz8.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/streptomyces_sp_gz8.yaml --out /private/tmp/taxonmech-gz8-review-strict.tsv`: passed, one file and zero errors; the complete TSV was header-only.
- Structured comparisons matched backbone, complete lineage, attestation, PATHS, scope and seed wording. Seven supplementary raw inventories plus type-material, merged-ID and dropped tables were scanned for exact target identifiers.
- Own marker consistency passed: declared/actual length 1390, submitted rRNA transcription equals DNA and no non-ACGT symbols. This is annotation consistency, not independent alignment or species assignment.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Individual checks do not prove corpus reproduction. Embedded history was inspected; ignored-inclusive searches found no separate target history artifact. Graph-product validation is inapplicable without nodes.

## Identity and Grounding

Complete [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036530&retmode=xml) and [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036530) agree with identifier, label, rank, parent, code and lineage. Datasets confirms all ten root-first ancestor IDs; EFetch supplies matching labels/ranks while omitting root from its displayed chain.

The chain includes Bacillati, Actinomycetota, Actinomycetes, Kitasatosporales, Streptomycetaceae, Streptomyces and unclassified Streptomyces. EFetch supplies no other names; pinned synonym fields are empty. Exact pinned scans found no type-material, merged-ID or dropped row and no backbone children. Species rank for an unnamed strain-associated taxon is not a formal species description. Exact grounding identifies this NCBI concept, not every strain spelled GZ8, GZ-8 or GZ_8.

## Evidence

Complete own rows inspected:

- `data/raw/ncbitaxon_taxa.tsv:222530`: identity, parent, rank, code, empty synonyms and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:32074`: scientific-name object with empty unique name.
- `data/taxa/PATHS.tsv:15037`: identifier/slug.
- `curation/seed_scope.tsv:322777`: admission date/reason matching the seed event.

One `NAME` attestation counts a name, not a genome or experiment. Exact raw scans returned no target BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row. `strain_count: 0` counts represented BacDive entries, not all externally named isolates.

Exact Nuccore query `txid1036530[Organism:noexp]` returned only UID 334361409. Complete [JF806664.1](https://www.ncbi.nlm.nih.gov/nuccore/JF806664.1) XML was read, including references, all features and sequence. This 1390-base 16S marker is partial at both ends. Its four source qualifiers identify Streptomyces sp. GZ8, genomic DNA, strain GZ8 and taxon 1036530. Only source and rRNA features occur; no host, isolation-source, geography, culture-deposit or assembly qualifier is supplied.

The marker references Chen, Wu and Li, an unpublished seagrass-associated study and a 13-APR-2011 direct submission from the South China Sea Institute of Oceanology, without DOI or PMID. It is neither a genome nor a phenotype assay.

[Wu et al. (2012), Table 2](https://www.researchgate.net/publication/267963976_Culture-dependent_diversity_of_Actinobacteria_associated_with_seagrass_Thalassia_hemprichii), compares GZ8 with Streptomyces althioticus at 98.26%, with PKS-I negative and PKS-II/NRPS positive; this row has no tree-inclusion asterisk. The methods include JF806664 within their deposited accession range. [Publisher metadata](https://academicjournals.org/journal/AJMR/article-abstract/2A88A4617354) verifies DOI 10.5897/AJMR11.981, absent from the GenBank citation. These comparisons do not establish synonymy or metabolite production.

Spelling-variant Nuccore search also returned UID 1398331524. Complete [MH458737.1](https://www.ncbi.nlm.nih.gov/nuccore/MH458737.1) XML identifies a 1489-base partial 16S marker for generic Streptomyces sp., taxon 1931, strain GZ-8. Zhang submitted it on 08-JUN-2018 from Hainan University. It supplies no direct relationship to taxon 1036530 or JF806664. Shared spelling alone cannot transfer this marker to the target.

The complete PubMed record and author abstract for [PMID 32653809](https://pubmed.ncbi.nlm.nih.gov/32653809/), DOI 10.1016/j.micres.2020.126548, concern Streptomyces badius gz-8 and dinactin-related antifungal work. An inspected [2017 primary paper](https://html.rhhz.net/nyxxb/20170607.htm), DOI 10.16801/j.issn.1008-7303.2017.0097, identifies gz-8 as a Linyi, Shandong soil isolate. The accessible text supplies no explicit identity chain to this seagrass-associated target. The 2020 full-text fetch failed; its full methods were not checked. No species reassignment, dinactin production or antifungal phenotype is attributed to the reviewed record. Similar author/strain context suggests a relationship between the later paper and the 2018 marker, but that is not a verified accession link.

All 21 additional local candidate rows were read in full and excluded from target identity:

- Enterococcus faecium GZ8, taxid 1352: GCA/GCF_007923945.2 with SAMN11180681, PRJNA528381, BV-BRC 1352.16062 and CP038163/CP038162; separately GCA/GCF_050446565.1 with SAMN18794688, PRJNA722835, BV-BRC 1352.23115 and JAGSZQ000000000.1. RefSeq rows use PRJNA224116. Native addresses: `data/bvbrc/bvbrc-0002.jsonl.gz:33534`, `data/bvbrc/bvbrc-0002.jsonl.gz:35974`, `data/catalog/ncbi_genbank-0006.jsonl.gz:42686`, `data/catalog/ncbi_refseq-0002.jsonl.gz:28265`, `data/catalog/ncbi_genbank-0046.jsonl.gz:28508`, `data/catalog/ncbi_refseq-0007.jsonl.gz:27778`, `data/catalog/gtdb_genomes-0003.jsonl.gz:13175` and `data/catalog/gtdb_genomes-0006.jsonl.gz:36582`.
- Clostridioides difficile GZ8, taxid 1496: GCA/GCF_003324025.1, SAMN09536779, PRJNA479396, QOVP00000000.1, BV-BRC 1496.3032 and the GOLD chain Go0489324 to Gp0373146 to Ga0340661. Native addresses: `data/bvbrc/bvbrc-0003.jsonl.gz:28212`, `data/gold/organisms.jsonl.gz:338763`, `data/gold/projects.jsonl.gz:260743`, `data/gold/analyses.jsonl.gz:200613`, `data/catalog/ncbi_genbank-0002.jsonl.gz:31196`, `data/catalog/ncbi_refseq-0001.jsonl.gz:47161` and `data/catalog/gtdb_genomes-0006.jsonl.gz:7288`. RefSeq uses PRJNA224116. The explicit GOLD organism/project chain is off-target despite its shared strain name.
- Bacillus velezensis GZ8-6, taxid 492670: GCA/GCF_051940895.1, SAMN50187270 and PRJNA1295821, with RefSeq project PRJNA224116. Native addresses: `data/catalog/ncbi_genbank-0047.jsonl.gz:47699`, `data/catalog/ncbi_refseq-0007.jsonl.gz:42264` and `data/catalog/gtdb_genomes-0004.jsonl.gz:27037`. GZ8 is only a prefix of its strain designation.
- Klebsiella pneumoniae GZ_8, taxid 573: GCA_053068625.1, SAMN50316559, PRJNA1299801 and JBROXV000000000.1 at `data/catalog/ncbi_genbank-0049.jsonl.gz:533`.
- Microvirga puerhi W GZ8, taxid 2876078: BacDive 170705, JCM 35317 and CGMCC 1.19171 at `data/bacdive/records.jsonl.gz:92937` and `data/raw/bacdive_strains.tsv:92938`. Its sequence section describes Microvirga sp. WGZ8/OK147892 under another Microvirga taxid, not this Streptomyces. A word-boundary match inside W GZ8 does not identify this target.

## Completeness

Complete enough for current taxonomy-seed claims. Optional nomenclature, deposits, genome links and graphs are appropriately unasserted without explicit evidence chains. An external marker does not require inventing a BacDive strain.

Gitignore-independent `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Initial terms included word-bounded taxid 1036530, label/slug and GZ8 with optional hyphen, space or underscore. Expansion added JF806664, MH458737 and both word-bounded sequence UIDs. Both scans returned the same 24 fully inspected rows: three target rows and 21 excluded candidates. Five SOURCE.json files were fully parsed separately for both term sets without matches; history filenames were independently inventoried. Absence statements are bounded to these roots and terms.

`GZ8[All Fields] AND Streptomyces[Organism]` returned only the own marker, not an audit of all 644 unfiltered GZ8 hits. The genus-constrained GZ-8/GZ 8 variant query returned the separate 2018 marker, not an audit of 21 unfiltered variant hits. Exact non-expanded Assembly query returned zero with missing-phrase/no-items diagnostics. The label/genus PubMed query returned the one inspected 2020 paper; accession PubMed query `JF806664[All Fields]` returned zero with missing-phrase diagnostics. Exact-accession web search yielded no target result. Indexed misses are not universal literature or genome absence.

An attempted Google Patents full-text open for search lead CN116536179A failed; no patent-based claim is used. Local native metadata independently establish the off-target Bacillus GZ8-6 identity. Secondary thesis/catalog search results were not treated as evidence for this target.

iModulonDB was not run: no gene, regulator or expression claim is asserted and no applicable strain/dataset was identified. This is not negative database evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in stored claims. Identity, lineage, scope and provenance agree with pinned and live authorities. Unresolved links to similarly named external strains are not asserted by the YAML and do not constitute a current record defect.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Future taxonomy corrections belong first at NCBI, then pinned inputs governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection fixes belong in `src/taxonmech/seed.py` with tests; scope changes belong in `curation/seed_scope.tsv`. Do not hand-edit output or join unrelated GZ8 strains by designation alone.

## Follow-up Checks

No corrective follow-up is needed for current claims. Optional enrichment requires an explicit target/accession/deposit chain; obtain the 2020 methods and exact strain provenance before making any link to the later gz-8 studies. Relevant seagrass table text, headings, methods and footnote were inspected, but original PDF figures were not visually verified. No complete experimental audit or independent sequence alignment is claimed.

After an authorized input/seeder change, run focused tests, `just seed-canary NCBITaxon:1036530`, inspect output, rerun both individual validators and `just verify-corpus`, then full publication QC. No regeneration ran.

## Additional Notes

The local review skill and checklist governed this independent review. Complete YAML, own rows, all local candidates, live taxonomy, both full marker records, PubMed record and relevant primary text were inspected. No neighboring accession or verdict was inherited.

Before/after YAML SHA-256: `d1a03e3ccfa423345762c4f255a2e94f6b3b4b53cb1e99e812505f0c99e0f89f`. Only this new report was written for the target. YAML, sources, history, status, pages, GitHub objects, Eukaryota and existing worktrees remained unchanged.
