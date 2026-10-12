# YAML Record Review: gamma proteobacterium W08.001

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/gamma_proteobacterium_w08_001.yaml`
- Started UTC: 2026-10-10T05:57:56Z
- Finished UTC: 2026-10-10T06:02:29Z
- Verdict: pass

## Target

Reviewed the entire 45-line generated `TaxonRecord` for `NCBITaxon:1037582`, gamma proteobacterium W08.001. It is a species-ranked bacterial placeholder under unclassified Gammaproteobacteria (`NCBITaxon:33811`), with `EXACT` grounding, `SEEDED` mapping status, genetic code 11, zero inventoried strains, one NCBI name attestation, and one seed event. Maintained inventories and `curation/seed_scope.tsv`, interpreted by the extractor/seeder, own future changes. Generated YAML remains read-only.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/gamma_proteobacterium_w08_001.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/gamma_proteobacterium_w08_001.yaml --out /private/tmp/taxonmech-w08001-20261010-validation.tsv --workers 1`: one file, zero errors; output TSV inspected and contains only its header.
- `python scripts/validate_history.py history`: 17 valid history records, zero invalid links.
- Structured comparisons verified the entire parent chain, source synonyms, identity, genetic code, attestation, path-index entry, scope reason, and seed-event wording. This is not full corpus reproduction.
- `just validate-products`: not applicable; the record has no graph nodes or curator-added ontology claims. No separate focused term/reference validator is documented; taxon references were checked against the backbone and live authority.
- Not checked: `just qc`, full-corpus `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and site rendering. Those corpus-wide checks were not run for this read-only single-record review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222797` exactly matches the identifier, label, species rank, parent, code 11, and 2026-09-13 snapshot. Its synonym and retirement fields are empty. Every root-first lineage entry agrees with its individual source row: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Gammaproteobacteria 1236; unclassified Gammaproteobacteria 33811. Labels and ranks agree. Missing order, family, and genus are faithful to NCBI's unresolved placement, not a broken parent chain.

Live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037582&retmode=xml), [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037582), and the [Taxonomy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037582) agree with the record. EFetch omits root in its displayed ancestry; Datasets includes root, matching the YAML. The species rank denotes this placeholder, not Gammaproteobacteria as a whole. A strain-qualified sequence is compatible with that rank. No formally named species, type strain, or culture deposit is asserted. The Datasets response omits an assembly count; omission must not be interpreted as zero assemblies.

The full native scientific-name row, `data/catalog/ncbi_names-0005.jsonl.gz:32433`, agrees. Structured scans found no own children, type-material entries, merged IDs, or dropped IDs. `data/taxa/PATHS.tsv:15350` uniquely resolves this file. `curation/seed_scope.tsv:323012` contains the 2026-09-13 attested rule reproduced in the 2026-09-13T17:54:04Z seed event. The record does not claim human review sign-off.

## Evidence

The attestation correctly counts one NCBI `NAME` assertion, not a strain, assembly, experiment, or paper. Exact source comparisons found no own rows in the seven pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, and BactoTraits inventories. Empty optional strain/nomenclature/mapping sections are consistent with those inputs. `strain_count: 0` is not a claim that no cultured isolate exists.

Live NCBI Nucleotide search `txid1037582[Organism:exp]` returned one UID, `334562411`. Its complete [GenBank annotation, JF813790.1](https://www.ncbi.nlm.nih.gov/nuccore/JF813790.1), explicitly links strain W08.001, the record's organism name, and `taxon:1037582`. This is a 1,460-base partial 16S rRNA gene with incomplete ends, annotated from the gut of Bombus terrestris. Declared/retrieved lengths agree, alphabet A/C/G/T; lowercase-sequence SHA-256 is `37d72edfee5646288c37f6dc1fd99f90aa8aa3c941003e10e66aa7db66edfdcb`. A genomic-DNA source qualifier does not make this marker a genome assembly. The annotation describes submitter chimera screening and primers 27f/1492r; these are provenance/method statements, not independent phenotype validation. It provides no collection country, sampling date, coordinates, or culture-deposit accession. The ETH Zurich address and 18 April 2011 submission date are not collection metadata.

The sequence cites Koch and Schmid-Hempel (2011), [Socially transmitted gut microbiota protect bumble bees against an intestinal parasite](https://www.pnas.org/doi/10.1073/pnas.1110474108), DOI `10.1073/pnas.1110474108`, PMID [22084077](https://pubmed.ncbi.nlm.nih.gov/22084077/), PMCID `PMC3228419`. PubMed links JF813790, and the paper's data-deposition statement confirms the accession. The main paper's results, methods, and relevant figures were inspected. Fecal microbiota transfer reduced Crithidia load; the cultured-gammaproteobacteria group did not differ from the control in parasite load (P = 0.77). Its characteristic bacterial signal was detected in only one individual at the endpoint. Figure 1 gives n = 12 for bacteria-fed, 16 control, and 15 feces-fed workers; a separate antibiotic group is not an equivalent concurrent control. These results do not establish that this single isolate protects its host, nor that it can never do so. The detailed culture protocol and designation in the supplement remain unchecked because the supplement could not be retrieved. Do not infer a mechanistic edge or revised genus from the article title or a related phylogenetic cluster.

All nine non-target native catalog hits from the repository search were read in full:

- `data/catalog/gtdb_genomes-0005.jsonl.gz:31893`: Chlamydia trachomatis (`taxid 813`), R32100IMS, `RS_GCF_001317825.1`, `SAMEA1398340`; the numeric match is contig N50 `1037582`, not taxonomy.
- `data/catalog/ncbi_genbank-0009.jsonl.gz:7600`: Francisella tularensis subsp. holarctica (`taxid 119857`, species 263), strain 14T0098, `GCA_010375825.1`, `SAMN12576348`, `PRJNA560345`; the assembly name is `ASM1037582v1`.
- `data/catalog/ncbi_genbank-0014.jsonl.gz:11667`: Salmonella enterica serovar Typhi (`taxid 90370`, species 28901), strain `1037582`, `GCA_015694905.1`, `SAMN16952256`, `PRJNA248792`. The numeral is a different organism's strain designation.
- `data/catalog/allthebacteria.tsv.xz:65324`: Streptococcus pneumoniae, `SAMEA1033953`, `ERZ3069511`, `ERR068092`; the numeral occurs inside a SeqKit checksum, not an identity field.
- AllTheBacteria lines 1716812 through 1716816: Escherichia coli samples `SAMN13162585` through `SAMN13162589`, with runs `SRR10375821`, `SRR10375822`, `SRR10375823`, `SRR10375824`, and `SRR10375826`. Their ENA analysis IDs are `ERZ25667898`, `ERZ25667910`, `ERZ25667921`, `ERZ25667932`, and `ERZ25667942`. Run-accession substrings are not taxon links.

None supplies a W08.001 strain, genome, mapping, or attestation. Catalog numbers in different identifier namespaces must remain distinct.

## Completeness

Ran ignored-inclusive compressed searches with `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. After the initial ID/designation search, expanded patterns explicitly covered the dotted label, exact slug, `W08[._ -]?001`, accession `JF813790`, PMID `22084077`, and DOI suffix `1110474108`. The final search returned 12 lines: backbone, scope, own name, and the nine unrelated rows above. No additional target-linked deposit, assembly, attestation, or history artifact was established on these surfaces; this is not a universal absence claim.

Independently enumerated and fully parsed the five source `SOURCE.json` files, finding no target/accession/citation matches. Ignored-independent filename walks found only this target YAML and no pre-existing target report/history filename. No Eukaryota YAML contents were read.

Web searches used the exact label, designation, accession, cited PMID, and author/designation combinations. Taxonomy-tree listings, similarity-table leads, and secondary comments about related bacterial clusters were not used as phenotype or identity evidence. The directly linked primary paper was inspected as above. Host/source and literature information could support optional future enrichment with explicit evidence scope; the local checklist does not require populating every optional field or inventing a causal graph. No required representation was found missing. iModulonDB is not applicable to this taxonomy/name-only record.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, unresolved lineage, source unit/count, strain inventory count, and seeded status agree with inspected authority and maintained inputs. The record makes no unsupported protective-function claim. The inaccessible supplement limits optional enrichment, not the validity of existing assertions.

## Recommended Edits

None required. Do not manually edit this generated record, promote its status, or append a curation/history event. Optional literature/host enrichment should be designed in maintained inputs or a supported curation overlay, retaining isolate and experiment scope. Transformation changes belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and their implementation modules; scope changes belong in `curation/seed_scope.tsv`. Do not turn source markers, checksum matches, or a community-level study title into genome or mechanistic assertions.

## Follow-up Checks

Before any optional culture/phenotype enrichment, obtain the linked supplement and verify the exact experimental isolate, culture conditions, and evidence placement. A later genus assignment needs explicit authoritative identity support, not tree proximity. Any new deposit/genome association requires a full source chain. After authorized input changes, rerun schema/strict/history validation, documented dry run and seed canary, corpus reproduction, and full quality gates. Human sign-off remains separate from this review.

## Additional Notes

The web reader could not open the NCBI browser, but a direct fetch succeeded; all 71 parsed text lines and complete EFetch/Datasets responses were inspected. Europe PMC full-text XML returned HTTP 500 twice; the PMC API supplied front matter only and explicitly disallowed full-text XML. The browser encountered a PMC verification page and publisher cookie errors. A public copy of the original five-page paper was retrieved from BeanBeetle and inspected; relevant pages 2 and 4 were also rendered and visually checked using cached PyMuPDF because Poppler was unavailable. Paper SHA-256: `562de1c081f274357593e84a1297e37995f4559ba0efe9827f47da2ae5c36e68`. The publisher's linked supplement returned 403; an attempted public PMC supplement path returned 404. No supplement contents are claimed read.

YAML SHA-256 at review: `745631b85c064c6738f0325a5a57cb704426859ce6f007ecb73184d6fa3ad67f`. Only this new report was written in the repository. Source inventories, generated YAML, schema, history, site, GitHub state, Eukaryota, and existing worktrees were unchanged.
