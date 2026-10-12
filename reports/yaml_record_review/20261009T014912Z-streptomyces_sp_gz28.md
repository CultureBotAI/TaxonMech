# YAML Record Review: Streptomyces sp. GZ28

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_sp_gz28.yaml`
- Started UTC: 2026-10-09T01:45:57Z
- Finished UTC: 2026-10-09T01:49:12Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1036520`: species rank, Bacteria domain, parent `NCBITaxon:2593676`, ten root-first ancestors, genetic code 11, `EXACT` grounding and `SEEDED` status. It contains zero represented BacDive strains, one NCBITAXON name attestation and one seed event dated 2026-09-13T17:54:04Z. Optional synonyms, nomenclature, mappings, strain/genome links, evidence and graphs are unasserted.

Ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved one target YAML and no prior target report. This generated file is not the maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline just validate data/taxa/bacteria/streptomyces_sp_gz28.yaml`: passed, no issues.
- `uv run --offline just validate-strict data/taxa/bacteria/streptomyces_sp_gz28.yaml --out /private/tmp/streptomycesGZ28-strict.tsv`: passed, one file and zero errors; complete TSV was header-only.
- Structured comparisons matched complete backbone/ancestor rows, lineage, attestation, PATHS, scope and seed-event wording. Seven supplementary raw inventories plus type-material, merged-ID and dropped tables were checked for exact target identifiers.
- Own marker consistency passed: declared and actual length 1413, submitted rRNA transcription equals DNA, no non-ACGT symbols. This checks submitted annotation, not independent alignment or species identity.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Individual checks do not establish corpus reproduction. Embedded history was inspected; ignored-inclusive inventory found no separate target history artifact. Graph-product validation is inapplicable without graph nodes.

## Identity and Grounding

Complete [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036520&retmode=xml) and [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036520) agree with identifier, label, rank, parent, code and lineage. Datasets confirms all ten root-first ancestor IDs; EFetch supplies matching ancestor labels/ranks while omitting root from its displayed chain.

The chain includes Bacillati, Actinomycetota, Actinomycetes, Kitasatosporales, Streptomycetaceae, Streptomyces and unclassified Streptomyces. Live EFetch has no other names, and pinned synonym fields are empty. Exact pinned scans found no type-material, merged-ID or dropped row and no backbone children.

Species rank for an unnamed strain-associated taxon does not establish a formally described species. Exact grounding identifies this NCBI concept, not equivalence to a nearest named species or a later isolate with a similar marker.

## Evidence

Complete own rows inspected:

- `data/raw/ncbitaxon_taxa.tsv:222520`: identity, rank, parent, code, empty synonyms and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:32064`: scientific-name object with empty unique name.
- `data/taxa/PATHS.tsv:15027`: identifier/slug.
- `curation/seed_scope.tsv:322767`: admission date/reason matching the event.

The attestation counts one `NAME`, not a genome or experiment. Exact raw scans returned no target BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row. Schema semantics make `strain_count: 0` a represented BacDive count, not a denial of the strain designation.

Exact Nuccore query `txid1036520[Organism:noexp]` and genus-constrained alias query `"GZ28"[All Fields] AND Streptomyces[Organism]` each returned only UID 334361406. Complete [JF806661.1](https://www.ncbi.nlm.nih.gov/nuccore/JF806661.1) XML, including both references, all features and sequence, was read. This 1413-base 16S marker is partial at both ends. Source qualifiers explicitly name Streptomyces sp. GZ28, genomic DNA, strain GZ28 and taxon 1036520. They supply no host, isolation-source, geographic, culture-deposit or assembly qualifier. Only source and rRNA features occur.

The accession names Chen, Wu and Li, an unpublished seagrass-associated study and direct submission on 13-APR-2011 from the South China Sea Institute of Oceanology. No DOI or PMID is supplied. This marker is not a genome or phenotype assay; missing qualifiers cannot be inherited from neighboring accessions.

Inspected [Wu et al. (2012) Table 2](https://www.researchgate.net/publication/267963976_Culture-dependent_diversity_of_Actinobacteria_associated_with_seagrass_Thalassia_hemprichii) compares GZ28 with Streptomyces glauciniger, 99.86%, with PKS-I negative and PKS-II/NRPS positive PCR screens. GZ28 has no asterisk. These results establish neither synonymy nor antimicrobial activity. [Publisher metadata](https://academicjournals.org/journal/AJMR/article-abstract/2A88A4617354) verifies DOI 10.5897/AJMR11.981. The strain/study connection is plausible, not an explicit GenBank citation link.

The accession search also found [Passari et al. (2015), Table 3](https://pmc.ncbi.nlm.nih.gov/articles/PMC4388002/), DOI 10.3389/fmicb.2015.00273, PMID 25904906. The full BPSAC32 row and column headings identify KJ584874 as that isolate's accession and JF806661 as a closest-sequence comparator, with 99% similarity. BPSAC32's Table 2 assays do not concern GZ28. Neither its medicinal-plant context nor assay findings can be transferred to this target. Bibliographic metadata, relevant table text and sequence-analysis context were inspected, not merely search snippets.

Both extra local candidates were read in full: `data/catalog/gtdb_genomes-0014.jsonl.gz:13949` and `data/catalog/ncbi_genbank-0001.jsonl.gz:19557`. They concern Candidatus Uhrbacteria bacterium RIFOXYC2_FULL_47_19, taxid 1802424, assembly GCA_001791745.1, BioSample SAMN04314601 and project PRJNA288027. Their ungapped genome length is 1036520, explaining the numeric match. No strain, genome, environmental context or cited publication from these rows belongs to the target on this evidence.

## Completeness

Complete enough for the supported taxonomy-seed claims. Optional nomenclature, deposits, genome links and graphs are appropriately unasserted without explicit evidence chains. The external marker does not require an invented BacDive strain. Prospective enrichment needs an appropriate maintained model/input and claim-level identity linkage.

Gitignore-independent `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Initial terms were word-bounded taxid 1036520, word-bounded GZ28 and slug; expansion added JF806661 and word-bounded UID 334361406. Both returned the same five fully inspected rows: three own taxonomy/name/scope rows and two excluded metagenome rows. Numeric boundaries prevent substring matches but not a coincidentally equal genome length. Five SOURCE.json files were fully parsed separately with initial and expanded terms without a match; history filenames were independently inventoried. Absence claims are bounded to these roots and terms.

Exact non-expanded Assembly search returned zero with phrase-not-found/no-items diagnostics. PubMed queries for GZ28 with Streptomyces and for JF806661 returned zero with quoted-phrase warnings; the accession web search nevertheless recovered the inspected 2015 comparator paper. The genus-constrained Nuccore result is not an audit of all 34 unfiltered GZ28 hits. These indexed misses do not prove universal genome or literature absence.

iModulonDB was not run: no gene, regulator or expression claim is asserted and no applicable strain/dataset was identified. This is not negative database evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in stored claims. Identity, lineage, scope and provenance agree with pinned and live authorities. No unsupported species reassignment, genome or phenotype is asserted.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Future authoritative taxonomy corrections belong first at NCBI, then pinned inputs governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection fixes belong in `src/taxonmech/seed.py` with regression tests; scope changes belong in `curation/seed_scope.tsv`. Do not hand-edit generated output to add unlinked assays or false genome matches.

## Follow-up Checks

No corrective follow-up is needed for current claims. Before literature enrichment, verify an explicit strain/accession/deposit chain and inspect original paper visuals. The 2012 author-hosted table text, headings and footnote were inspected; its original PDF/figure was not visually verified. The 2015 PMC article became readable after an initial browser-check response; relevant HTML table text was inspected, not PDF figures or an independent phylogenetic reconstruction.

After any authorized input/seeder change, run focused tests, `just seed-canary NCBITaxon:1036520`, inspect output, rerun both individual validators and `just verify-corpus`, then full publication QC. No regeneration ran.

## Additional Notes

The local review skill and field checklist governed this independent review. Its own complete YAML, source candidates, live taxonomy, marker and literature contexts were inspected; no neighboring accession or verdict was inherited.

Before/after YAML SHA-256: `e11b76171baf19db68d7706fdb7e85929957e33268ea380195be1541035a5929`. Only this new report was written for the target. YAML, sources, history, mapping status, pages, GitHub objects, Eukaryota and existing worktrees remained unchanged.
