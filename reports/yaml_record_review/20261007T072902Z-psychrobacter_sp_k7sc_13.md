# YAML Record Review: Psychrobacter sp. K7SC-13

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/psychrobacter_sp_k7sc_13.yaml`
- Started UTC: 2026-10-07T07:26:33Z
- Finished UTC: 2026-10-07T07:29:02Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord`: `NCBITaxon:1035612`, Psychrobacter sp. K7SC-13, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:196806`, ten root-first ancestors and genetic code 11. It carries `EXACT` grounding, `SEEDED` mapping status, `strain_count: 0`, one NCBI name attestation and one seed event.

No synonyms, nomenclature, taxonomy mappings, culture deposits, genomes, definition, literature evidence, discussions, datasets, replacement or causal graphs are asserted. The isolate designation is not a verified culture accession. Generated YAML is read-only. Maintained source/extraction inputs and `src/taxonmech/seed.py` own future fixes, with scope and slug ownership in `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv`.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and offline uv dependency resolution.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/psychrobacter_sp_k7sc_13.yaml` | Exit 0; No issues found. |
| `just validate-strict data/taxa/bacteria/psychrobacter_sp_k7sc_13.yaml --out /private/tmp/py13-strict.tsv` | Exit 0; one file, zero ERROR rows. |
| `cat /private/tmp/py13-strict.tsv` | Actual TSV read; header only. |
| Structured backbone, complete lineage, seven source inventories, path, scope and attestation comparisons | Bounded checks passed. |
| Exact type-material, merged-ID and dropped-record scans | No target row. |
| Live NCBI Taxonomy EFetch and Datasets | Exact identity and complete ancestry agree. |
| Exact-taxid Assembly and nuccore searches | Assembly 0 with phrase-not-found warning; nuccore 1, complete metadata inspected. |

Not checked: `just verify-corpus`, `just qc`, full-corpus schema validation, tests, provenance hashing, generated-page drift, documentation statistics and vendored checks. Bounded comparisons do not prove byte-for-byte corpus reproduction.

`just validate-products` was not run: configured OAK targets are curator-added graph nodes, absent here; NCBI taxonomy is excluded. There are no literature/internal evidence references in the YAML. The seed event was checked. `just validate-history` was not run because ignored-independent content/path searches found no target history artifact; none is created here.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:222140` agrees on ID, label, rank, parent, code, empty synonyms and snapshot `2026-09-13`. The full native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31619` agrees. Path and scope are unique at `data/taxa/PATHS.tsv:14642` and `curation/seed_scope.tsv:322410`.

All ten ancestors match the committed parent chain in identifier, label, rank and order. Live EFetch confirms species rank, parent 196806, code 11 and nine non-root ancestors; Datasets confirms the same chain including root. Moraxellales/Moraxellaceae/Psychrobacter and direct parent unclassified Psychrobacter agree. No retirement or replacement was found in the inspected lifecycle sources. [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035612&retmode=xml), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035612)

`EXACT` grounds the NCBI concept, not a formal species determination or equivalence to Psychrobacter nivimaris. The source's species rank does not imply that this provisional isolate name is a validly published binomial.

## Evidence

The sole `NCBITAXON` attestation agrees on ID, exact label, count 1, unit `NAME` and snapshot note. Unlike units are not summed. The complete backbone scan found no direct children. Exact scans found no target row in `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`.

Nuccore UID `334361527` resolves to `JF799968.1`, a 1,531-nt partial 16S rRNA marker. Complete GenBank metadata explicitly identifies the target organism, strain K7SC-13 and `taxon:1035612`, with soil isolation and India: Kafni Glacier. No culture-collection, assembly, BioSample or BioProject link is supplied. References are an unpublished Kafni study and direct submission, without DOI or PMID. Submission is dated 11 April 2011; creation/update are 6 June 2011. The rRNA feature is partial at both ends. This marker is not a genome. [GenBank JF799968.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799968.1)

The related primary paper is `PMID:21918795`, `DOI:10.1007/s00792-011-0398-8`, verified through PubMed earlier in this turn. Table 3 row 11 names Psychrobacter nivimaris 88/2-7T, AJ313425, as K7Sc-13's nearest neighbor at 99.3% 16S similarity. The column is not an isolate accession, deposit or species-equivalence assertion. The HTML extraction's enzyme signs are unreliable and are not interpreted. The paper also discusses an isolate-specific fatty-acid observation; that is outside this record's asserted content and does not warrant a taxonomic merge. [Primary article text](https://www.researchgate.net/publication/51644024_Comparison_of_bacterial_diversity_in_proglacial_soil_from_Kafni_Glacier_Himalayan_Mountain_ranges_India_with_the_bacterial_diversity_of_other_glaciers_in_the_world), [PubMed](https://pubmed.ncbi.nlm.nih.gov/21918795/)

The complete rendered Supplementary Fig. S3 on PDF page 4 was visually inspected for this target. It explicitly associates Psychrobacter isolate K7SC-13 with JF799968, agreeing with the exact-taxid sequence result. No genus conflict is established. [Publisher supplementary figures](https://media.springernature.com/original/springer-static/esm/art:10.1007%2Fs00792-011-0398-8/MediaObjects/792_2011_398_MOESM2_ESM.pdf)

Complete primary comparator metadata identifies `AJ313425.1` as a separate 1,498-nt partial 16S marker from Psychrobacter nivimaris type strain 88/2-7, taxon 281738, isolated from a seawater particle in Antarctica. Its linked `PMID:15368844` resolves to the 2004 species-description paper, `DOI:10.1078/0723202041438455`, whose abstract confirms the separate Southern Ocean isolate. Neither its type status nor its habitat/phenotypes transfers to K7SC-13. [GenBank AJ313425.1](https://www.ncbi.nlm.nih.gov/nuccore/AJ313425.1), [Comparator publication](https://pubmed.ncbi.nlm.nih.gov/15368844/)

Two additional local catalog hits were read in full and rejected as numeric collisions. `data/catalog/ncbi_genbank-0024.jsonl.gz:5273` has `genome_size: 1035612`; `data/catalog/gtdb_genomes-0000.jsonl.gz:28034` has `ncbi_total_length: 1035612`. Both concern assembly GCA_025994995.1 and taxid 2026775, a Pelagibacteraceae organism, not this taxon. They establish no genome link for K7SC-13.

The successful 28-dataset iModulonDB listing fully inspected in this turn includes no Psychrobacter target dataset; it was not re-fetched for this record. The YAML makes no gene, regulator or omics assertion. The adapter is not applicable, and its absence is not negative phenotype evidence.

## Completeness

Zero BacDive strains and the optional omissions agree with the inspected inventories. A marker's strain qualifier does not establish a missing BacDive deposit. Record-level literature evidence is optional for seeded records. No required gap was found.

Both local search stages included ignored/hidden files and compressed catalogs with `rg --no-ignore --hidden -n -z -i`. Roots were `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All five excluded `SOURCE.json` files were separately parsed in full per stage; history filenames were independently traversed.

The identity stage used taxid 1035612, exact label, slug and K7SC-13 case/separator variants. Five lines matched: the three target rows and two numeric collisions described above. The citation stage used JF799968 with optional version, PMID 21918795 and its DOI; no lines matched. Neither stage found matching metadata values or history paths. These negative findings include ignored files and are bounded to those roots and terms.

Web searches used the exact label and K7SC-13 with JF799968. No supported deposit/genome chain was established. The Assembly zero carries a phrase-not-found warning and does not exclude genomes indexed under another identity. The main article was read as HTML extraction rather than a visually verified PDF. Supplementary DOC tables were not inspected.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected scope. Identity, complete lineage, source provenance, counts and seed history agree. Neither the publication's nearest-neighbor comparison nor unrelated numeric catalog hits justify adding a species mapping, deposit or genome.

## Recommended Edits

None required. Do not patch generated YAML, import comparison-strain attributes, count the marker as a genome, or promote `SEEDED` to `REVIEWED`.

A later authorized source refresh belongs in `conf/ncbi_taxdump.yaml` and `scripts/extract_source_inventory.py`, followed by guarded seeding. Optional literature annotations require maintained-input support merged by `src/taxonmech/seed.py` with regression tests under `docs/CURATION.md`. Experimental traits and habitat assertions belong in the corresponding sibling corpora, with claim-specific evidence.

## Follow-up Checks

- Require an exact culture-deposit and genome-source chain before adding strain/genome identifiers; do not join numeric values across unrelated fields.
- Keep K7SC-13 and the P. nivimaris 88/2-7 comparison strain distinct in future curation.
- After an authorized maintained-input change, rerun both single-record validators, then `just verify-corpus` and `just qc`; validate any new history artifact. Full-corpus gates remain skipped here.

## Additional Notes

Primary taxonomy and nucleotide API reads succeeded. The supplement's web text lookup did not find the accession; the downloaded publisher PDF's rendered page supplied the readable exact-isolate evidence. That PDF was rendered earlier in this session using macOS PDFKit. Its page-1 caption has an unfinished final sentence; no missing methodology is reconstructed.

Seed wording agrees with scope and attestation. Timestamp `2026-09-13T17:54:04Z` is the newest raw/ATB/StrainInfo manifest timestamp selected by `src/taxonmech/seed.py:_seed_timestamp`, not a review date.

The whole target was reread unchanged before report creation. An ignored-independent filename search found no previous report for this stem. Only this new repository report is added; no record, inventory, page, old report, history, status, GitHub object or cross-repository artifact is changed. No paid research or outbound contact was used.
