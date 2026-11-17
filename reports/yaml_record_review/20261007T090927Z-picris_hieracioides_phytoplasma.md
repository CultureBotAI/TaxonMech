# YAML Record Review: 'Picris hieracioides' phytoplasma

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/picris_hieracioides_phytoplasma.yaml`
- Started UTC: 2026-10-07T09:03:44Z
- Finished UTC: 2026-10-07T09:09:27Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord`: `NCBITaxon:1035632`, 'Picris hieracioides' phytoplasma, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:85621` (16SrII (Peanut WB group)), ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` mapping status and `strain_count: 0`. It has one NCBI name attestation and one seed event.

No synonyms, nomenclature, taxonomy mappings, deposits, genomes, definition, literature evidence, discussions, datasets, replacement or causal graphs are asserted. This phytoplasma is not the plant host or a verified culture deposit. Generated YAML is read-only; future fixes belong to maintained source/extraction inputs and `src/taxonmech/seed.py`, with scope and slug ownership in `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv`.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and offline uv dependency resolution.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/picris_hieracioides_phytoplasma.yaml` | Exit 0; No issues found. |
| `just validate-strict data/taxa/bacteria/picris_hieracioides_phytoplasma.yaml --out /private/tmp/picris-strict.tsv` | Exit 0; one file, zero ERROR rows. |
| `cat /private/tmp/picris-strict.tsv` | Actual TSV read; header only. |
| Structured backbone, full lineage, seven inventories, path, scope and attestations | Bounded checks passed. |
| Exact type-material, merged-ID and dropped-record scans | No target row. |
| Live NCBI Taxonomy EFetch and Datasets | Identity and complete ancestry agree. |
| Exact-taxid Assembly and nuccore searches | Assembly 0 with phrase-not-found warning; nuccore 1, complete metadata inspected. |
| Primary 2011 publisher paper | Both pages read in full and visually inspected; explicit target marker accession verified. |
| Related bushy-stunt identity | Complete native rows and JQ743509.1 metadata distinguish a separate NCBI concept. |

Not checked: `just verify-corpus`, `just qc`, full-corpus schema validation, tests, provenance hashing, generated-page drift, documentation statistics and vendored checks. Bounded comparisons are not byte-for-byte corpus reproduction.

`just validate-products` was not run: configured OAK targets are curator-added graph nodes, absent here; NCBI taxonomy is excluded. No literature/internal evidence references occur in the YAML. The seed event was checked. `just validate-history` was not run because ignored-independent content/path searches found no target history artifact.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:222160` agrees on ID, label, rank, parent, genetic code, empty synonyms and snapshot `2026-09-13`. The complete native scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31640` agrees. Unique path and scope rows are `data/taxa/PATHS.tsv:14660` and `curation/seed_scope.tsv:322427`.

All ten ancestors match the committed parent chain: root, cellular organisms, Bacteria, Bacillati, Mycoplasmatota, Mollicutes, Acholeplasmatales, Acholeplasmataceae, Candidatus Phytoplasma and 16SrII (Peanut WB group), with identical IDs, labels, ranks and order. Live EFetch confirms species rank, parent 85621, code 11, no alternate names and nine non-root ancestors; Datasets includes root. No retirement or replacement was found in inspected lifecycle sources. [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035632&retmode=xml), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035632)

The quoted host name is part of the bacterial scientific label. YAML's doubled single quotes correctly encode it. The record satisfies species-level scope without claiming a formally published binomial or a cultivated isolate. `EXACT` refers to the NCBI concept. Neither host identity nor inferred subgroup placement replaces the carried NCBI lineage.

## Evidence

The sole `NCBITAXON` attestation agrees on ID, label, count 1, unit `NAME` and snapshot note. A name count is not a strain or genome count. A complete backbone scan found no direct children. Exact scans found no target row in `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`.

Exact-taxid nuccore UID 333952451 resolves to `JF799094.1`, a 1,447-nt partial 16S rRNA marker. Organism and taxid match the YAML; isolate is 56Avg-07, host is Picris hieracioides and location is Serbia. The rRNA feature is partial at both ends. No DOI, PMID, culture-collection, BioSample, BioProject or assembly link is supplied. Submission was 11 April 2011; creation/update were 30 May 2011. [GenBank JF799094.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799094.1)

GenBank cites an unpublished study by Mitrovic and colleagues concerning a strain related to subgroup 16SrII-E, plus their direct submission. All metadata were inspected, excluding only sequence strings and translation/transcription payloads. The marker establishes source provenance, not a genome or a culture-collection strain count.

The 2011 Bulletin of Insectology paper by Mitrovic and colleagues explicitly reports JF799094 and its 1,447-bp length. In 38 plant samples collected in July 2010, six were PCR-positive; methods state that sampled plants lacked typical infection symptoms. Results and Figure 1 distinguish an MseI profile matching a 16SrII-D reference from sequence similarity to a 16SrII-E reference. These assay-specific observations support 16SrII context, not automatic assignment to either subgroup or identity with the reference isolates. Both pages, the gel and caption were inspected. GenBank's unpublished reference is therefore incomplete publication metadata, not proof that no publication exists or an error in this YAML. [Primary paper, S241-S242](https://archive.bulletinofinsectology.org/pdfarticles/vol64-2011-S241-S242mitrovic.pdf)

The expanded local search found a separate species-rank concept, `NCBITaxon:1240346`, 'Picris hieracioides' bushy stunt phytoplasma, under the same parent. Complete rows were read at `data/raw/ncbitaxon_taxa.tsv:284321`, `curation/seed_scope.tsv:373186` and `data/catalog/ncbi_names-0007.jsonl.gz:4843`. No synonym or retirement in those rows equates it with the target.

The publisher abstract of the 2012 study, DOI `10.1007/s10658-012-0044-z`, reports bushy-stunt-associated phytoplasma and vector-transmission work. A search lead to JQ743509 was checked at GenBank: `JQ743509.1` is a 1,084-nt rpl22/rps3 record for strain Ph with explicit `taxon:1240346`, and its reference names that 2012 article. This is a different source identity, not evidence to transfer genes, symptoms or vector claims to isolate 56Avg-07. Biological equivalence between the two concepts remains unestablished here. The 2012 full text and figures were not inspected. [Publisher abstract](https://link.springer.com/article/10.1007/s10658-012-0044-z), [GenBank JQ743509.1](https://www.ncbi.nlm.nih.gov/nuccore/JQ743509.1)

Two initial local search hits were unrelated accession-digit matches, read completely:

| Source address | Actual match and exclusion |
| --- | --- |
| `data/catalog/allthebacteria.tsv.xz:66277` | Staphylococcus aureus, SAMEA1035632, ERR083839 and ERZ3070822, with META_FAIL. Matching sample digits are not taxonomy; the filter also precludes an eligible link. |
| `data/catalog/allthebacteria.tsv.xz:551215` | Escherichia coli, SAMEA3375250, ERR1035632 and ERZ3259032. Digits occur in a run accession, not a taxon field. |

No gene, regulator, pathway, stress-response or transcriptomics assertion in the YAML requires iModulonDB. The rpl22/rps3 genes belong to the separately checked source concept and do not create target assertions.

## Completeness

Zero BacDive strains and optional omissions agree with inspected source scope. An isolate qualifier is not a culture deposit; a marker is not a genome. Optional literature context could cite the exact-accession 2011 paper, but seeded records need not populate those fields. No required gap was found. The relationship between isolate 56Avg-07 and strain Ph requires additional evidence before any consolidation.

Both local stages included ignored/hidden files and compressed catalogs using `rg --no-ignore --hidden -n -z -i`, across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All five excluded `SOURCE.json` files were separately parsed in full per stage; history filenames were independently traversed.

The initial search used taxid 1035632 as a complete digit run and label/slug variants; all five matches were read: three target rows and the two ATB exclusions. The expanded search used the host phrase followed within 40 characters by phytoplasma, isolate 56Avg-07, JF799094 with optional .1 and the exact 2012 DOI. Its six matches were the three target rows and the three bushy-stunt concept rows. No accession, isolate or DOI hit was found locally in that stage. Neither stage found matching metadata values or history paths. Negative local findings include ignored files and are bounded to these roots and terms.

Web queries used JF799094, 56Avg-07 and the host with phytoplasma/Serbia. Only inspected primary text supports the judgments above; plant-host pages and other phytoplasma studies were not used to infer target identity. No supported deposit/genome chain was established. Exhaustive literature retrieval, sequence similarity and independent subgroup reanalysis were not performed. The exact-taxid Assembly zero includes a phrase-not-found warning and does not exclude assemblies under another identity.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the YAML within the inspected scope. Identity, lineage, provenance, zero strain count and seed history agree. Publication metadata lag and unresolved cross-isolate relationships do not establish a generated-record error.

## Recommended Edits

None required. Do not patch generated YAML, merge the bushy-stunt taxon, assign its strain or genes to the target, equate a shared plant host with phytoplasma identity, infer subgroup placement from one assay, count JF799094.1 as a genome, or promote `SEEDED` to `REVIEWED`.

Optional marker/publication enrichment requires maintained-input support in `src/taxonmech/seed.py` with tests under `docs/CURATION.md`, preserving taxid, isolate and exact accession provenance. A publication update to the GenBank source belongs upstream. Taxonomy corrections would require upstream evidence and an authorized refresh through `conf/ncbi_taxdump.yaml`, `scripts/extract_source_inventory.py` and guarded seeding; none is supported here.

## Follow-up Checks

- Resolve isolate 56Avg-07 versus strain Ph using explicit primary evidence before aliasing concepts or transferring the 2012 vector and symptom results.
- Keep the 2011 restriction-pattern and sequence-comparison observations distinct; do not replace the carried NCBI parent without an upstream correction.
- After authorized maintained-input changes, rerun both single-record validators, `just verify-corpus` and `just qc`; validate any new history artifact. Full-corpus gates remain skipped here.

## Additional Notes

Primary NCBI reads succeeded. The 2011 PDF text was available through the web tool; screenshot delivery initially timed out and then returned no image payload. The publisher PDF was downloaded to scratch storage and both pages rendered through macOS PDFKit and inspected locally. No PDF authoring or repository artifact change was performed. The 2012 publisher supplied its abstract but marked the full article as subscription content; no purchase or author contact was attempted.

Seed wording agrees with scope and attestation. Timestamp `2026-09-13T17:54:04Z` is the newest raw/ATB/StrainInfo manifest timestamp selected by `src/taxonmech/seed.py:_seed_timestamp`, not a review date. Previously inspected guidance and maintained source state remain unchanged at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`.

The entire YAML was reread unchanged before this report. An ignored-independent filename search found no previous report for this stem. Only this new report is added; no record, inventory, page, old report, history, status, GitHub object or cross-repository artifact is changed. Eukaryota was not re-reviewed. No paid research or outbound contact was used.
