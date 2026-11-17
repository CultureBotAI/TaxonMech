# YAML Record Review: Streptomyces sp. GZ23

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_sp_gz23.yaml`
- Started UTC: 2026-10-09T01:41:45Z
- Finished UTC: 2026-10-09T01:44:37Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1036519`: species rank, Bacteria domain, parent `NCBITaxon:2593676`, ten root-first ancestors, genetic code 11, `EXACT` grounding and `SEEDED` status. It has zero represented BacDive strains, one NCBITAXON name attestation and one seed event dated 2026-09-13T17:54:04Z. Optional synonyms, nomenclature, mappings, strain/genome links, evidence and graphs are unasserted.

Ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` found one target YAML and no earlier target report. The generated file is not the maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline just validate data/taxa/bacteria/streptomyces_sp_gz23.yaml`: passed, no issues.
- `uv run --offline just validate-strict data/taxa/bacteria/streptomyces_sp_gz23.yaml --out /private/tmp/streptomycesGZ23-strict.tsv`: passed, one file and zero errors; full TSV was header-only.
- Complete source-row comparisons matched identity, ancestor chain, attestation, PATHS, scope and seed-event wording. Seven supplementary inventories plus type-material, merged-ID and dropped tables were scanned for exact target identifiers.
- Own marker consistency passed: declared and actual length 1410; submitted rRNA transcription equals DNA; no non-ACGT symbols. This is not an independent alignment or species assignment.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Individual checks do not prove corpus reproduction. Embedded history was inspected, and ignored-inclusive history inventory found no separate target artifact. Graph-product validation is inapplicable without graph nodes.

## Identity and Grounding

Complete [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036519&retmode=xml) and [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036519) agree with the identifier, label, rank, parent, code and lineage. Datasets includes all ten root-first ancestor IDs; EFetch supplies matching ancestor labels/ranks while omitting root from its displayed chain.

The chain includes Bacillati, Actinomycetota, Actinomycetes, Kitasatosporales, Streptomycetaceae, Streptomyces and unclassified Streptomyces. Live EFetch has no other names and pinned synonym fields are empty. Exact pinned scans found no type-material, merged-ID or dropped row and no backbone children.

Species rank for an unnamed strain-associated taxon does not establish a formally described species. Exact grounding identifies this NCBI concept, not equivalence to a nearest named species or every strain containing GZ23 in its designation.

## Evidence

Complete own rows inspected:

- `data/raw/ncbitaxon_taxa.tsv:222519`: identity, parent, rank, code, empty synonyms and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:32063`: scientific-name object with empty unique name.
- `data/taxa/PATHS.tsv:15026`: identifier/slug.
- `curation/seed_scope.tsv:322766`: admission date/reason matching the event.

The attestation counts one `NAME`, not a genome or experiment. Exact raw scans returned no target BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row. Schema semantics make `strain_count: 0` a represented BacDive count, not a denial of the strain designation.

Exact Nuccore query `txid1036519[Organism:noexp]` and genus-constrained alias query `"GZ23"[All Fields] AND Streptomyces[Organism]` each returned only UID 334361407. Complete [JF806662.1](https://www.ncbi.nlm.nih.gov/nuccore/JF806662.1) XML, including both references, all features and sequence, was read. This 1410-base 16S marker is partial at both ends. Its source qualifiers explicitly name Streptomyces sp. GZ23, genomic DNA, strain GZ23 and taxon 1036519. They supply no host, isolation-source, geographic, culture-deposit or assembly qualifier. Only source and rRNA features occur.

The accession names Chen, Wu and Li, an unpublished seagrass-associated study and a direct submission on 13-APR-2011 from the South China Sea Institute of Oceanology. No DOI or PMID is supplied. A marker is not a genome or phenotype assay, and missing qualifiers cannot be inherited from adjacent records.

Inspected [Wu et al. (2012) Table 2](https://www.researchgate.net/publication/267963976_Culture-dependent_diversity_of_Actinobacteria_associated_with_seagrass_Thalassia_hemprichii) compares GZ23 with Streptomyces griseoplanus, 99.71%, with positive PKS-I, PKS-II and NRPS PCR screens. The asterisk denotes tree inclusion. This is not synonymy or demonstrated antimicrobial activity. [Publisher metadata](https://academicjournals.org/journal/AJMR/article-abstract/2A88A4617354) verifies DOI 10.5897/AJMR11.981. The strain/study connection is plausible, not an explicit GenBank citation link.

The inspected [KR101601089B1 description](https://patents.google.com/patent/KR101601089B1/en) uses GZ23 and 13CM4 as sequence comparisons for CKDBD 1100. Its reported greater-than-99% similarity does not identify CKDBD 1100 as GZ23 or transfer the patent strain's daptomycin-production claim. The translated description supports this bounded distinction; no legal-status judgment or patent experimental replication was attempted.

The extra local candidate, `data/catalog/ncbi_genbank-0045.jsonl.gz:7037`, was read in full. It is Escherichia coli Ec-gz23, taxid 562, GCA_048936575.1, SAMN41222820 and PRJNA1108026, not the target. Its strain designation explains the regex match; its genome and project are excluded.

## Completeness

Complete enough for the supported taxonomy-seed claims. Optional nomenclature, deposits, genome links and graphs are appropriately unasserted without explicit evidence chains. The external marker does not require an invented BacDive strain. Potential literature enrichment needs a maintained model/input and claim-level identity linkage.

Gitignore-independent `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Initial terms were word-bounded taxid 1036519, word-bounded GZ23 and slug; expansion added JF806662 and word-bounded UID 334361407. Both returned the same four fully inspected rows: three own taxonomy/name/scope rows and the excluded E. coli assembly. Five SOURCE.json files were fully parsed separately with initial and expanded terms without a match; history filenames were independently inventoried. Absence claims are bounded to these roots and terms.

Exact non-expanded Assembly search returned zero with phrase-not-found/no-items diagnostics. PubMed queries for GZ23 with Streptomyces and for JF806662 returned zero; the accession query had a quoted-phrase warning. Accession web search returned no result. Strain web searches supplied the primary study, patent and other name-collision leads; snippets were not used as biological evidence. The genus-constrained Nuccore result is not an audit of all 43 unfiltered GZ23 hits. These indexed misses do not establish universal literature or genome absence.

iModulonDB was not run: no gene, regulator or expression claim is asserted and no applicable strain/dataset was identified. This is not negative database evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in stored claims. Identity, lineage, scope and provenance agree with pinned and live authorities. No unsupported species reassignment, genome or phenotype is asserted.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Future authoritative taxonomy corrections belong first at NCBI, then pinned inputs governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection fixes belong in `src/taxonmech/seed.py` with regression tests; scope changes belong in `curation/seed_scope.tsv`. Do not hand-edit generated output to add unlinked literature or collisions.

## Follow-up Checks

No corrective follow-up for present claims. Before literature enrichment, verify an explicit strain/accession/deposit chain and inspect original paper visuals. The author-hosted Table 2 text, headings and footnote were inspected; original PDF/figure visual verification was not completed. Patent text was inspected for the comparator role, not its figures, sequence listing or biological performance claims.

After any authorized input/seeder change, run focused tests, `just seed-canary NCBITaxon:1036519`, inspect output, rerun both individual validators and `just verify-corpus`, then full publication QC. No regeneration ran.

## Additional Notes

The local review skill and field checklist governed this independent review. Its own complete YAML, source candidates, live taxonomy, marker and primary-source contexts were inspected; no neighboring accession or verdict was inherited.

Before/after YAML SHA-256: `63fb761029db98c091ce37faeb4d8b32da497a8f9aafe59d23d32838256df0d6`. Only this new report was written for the target. YAML, sources, history, mapping status, pages, GitHub objects, Eukaryota and existing worktrees remained unchanged.
