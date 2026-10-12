# YAML Record Review: uncultured marine bacterium D029

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_marine_bacterium_d029.yaml`
- Started UTC: 2026-10-09T14:14:35Z
- Finished UTC: 2026-10-09T14:17:02Z
- Verdict: pass

## Target

Read the entire 39-line generated `TaxonRecord` for `NCBITaxon:103676`, uncultured marine bacterium D029. It carries rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:150608`, genetic code 11, `EXACT` grounding and `SEEDED` lifecycle. Five ancestor entries and one source-name attestation are present; synonyms, nomenclature, mappings, strains and mechanism claims are not asserted. The strain count is zero.

This report reviews the NCBI environmental clone concept, not a similarly numbered collection deposit or a cultured organism inferred from a sequence neighbor. `data/taxa/PATHS.tsv:15143` uniquely pins this slug; `curation/seed_scope.tsv:144185` admits the record on 2026-09-13. The YAML is generated and remains read-only.

## Validation

Commands used the existing environment with `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1`:

- `just validate data/taxa/bacteria/uncultured_marine_bacterium_d029.yaml`: passed, exit 0, no issues.
- `just validate-strict data/taxa/bacteria/uncultured_marine_bacterium_d029.yaml --out /private/tmp/taxonmech-d029-20261009-validation.tsv`: passed, exit 0, one file and no error rows. The complete TSV was read; only its header is present.

Additional structured reads compared all carried ancestors, the parent/rank/code/label, own source rows, PATHS, scope, attestation and embedded event text. Exact own-taxon checks returned no child, type-material, merged-ID or dropped row. These bounded source checks do not establish byte-for-byte corpus reproduction.

Not checked: `just verify-corpus`, `just qc`, the full test suite, all-record validation, provenance hashing and rendered-site drift. The reproduction script has no single-record selector; `--max-diffs` only bounds diagnostic output. No focused replacement was invented. The configured `just validate-products` gate targets curator-added graph grounding, absent here, and excludes NCBITaxon IDs from OAK resolution. `just validate-history` has no separate target history artifact to validate; the existing embedded seed event was schema-checked. No history or lifecycle update was made.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:18541` and native scientific-name row at `data/catalog/ncbi_names-0000.jsonl.gz:38557` match the YAML. Fresh [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103676&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103676) confirm the exact clone name and ID, species rank, code 11 and parent 150608. The root-first chain is root, cellular organisms, Bacteria, environmental samples, marine bacteria D ensemble. Datasets explicitly includes the root and the taxonomy XML provides the remaining ancestor names and ranks.

The generic environmental lineage is faithfully carried from NCBI. A historical sequence-based affiliation does not authorize TaxonMech to infer a more specific hierarchy. `EXACT` identifies the NCBI concept; it is not evidence of species circumscription, nomenclatural validity, culture availability or an exact match to any named species.

## Evidence

The emitted source evidence is narrow and correct: one `NCBITAXON` assertion, source ID `NCBITaxon:103676`, the full D029 label, unit `NAME`, and snapshot date 2026-09-13. The source contains no synonym or additional own-taxon attestation that the YAML omitted.

An independently issued NCBI nucleotide query for `txid103676[Organism:noexp]` returned exactly UID 5882278. Its complete [GenBank record](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=5882278&rettype=gb&retmode=xml), including features, references and sequence, identifies **AF177563.1**, a 585-base partial 16S rRNA sequence. The source feature explicitly gives clone D029, `taxon:103676`, environmental-sample status and surface-associated marine context. It is not an assembly, culture deposit or direct phenotype assay.

Sequence-length and annotation checks agree at 585 bases, and the submitted transcription equals the DNA after case normalization. Position 516 contains the source's ambiguous `s`; all other bases are A/C/G/T. Preserve that ambiguity in any future sequence work. It is not a record defect: the YAML makes no sequence or base-quality assertion. No alignment, assembly download or inferred taxonomic reassignment was performed.

The sequence's PMID 10653705 was freshly resolved through the complete PubMed abstract and identifiers to DOI 10.1128/AEM.66.2.467-475.2000, PMC91850. The inspected primary article places D029 in the Alteromonas-associated gamma-proteobacterial group. Table 1 reports 24-hour library frequencies of 3.9% on PVA, 1.5% on PEG-S and 2.0% on PU. These observations are clone-library results, not cultured-isolate phenotypes. [Primary study](https://journals.asm.org/doi/10.1128/aem.66.2.467-475.2000).

## Completeness

The source search included ignored and hidden files and decompressed supported archives: `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Terms included bounded taxon digits, the full label, slug and bounded D029. All 44 candidate rows were then read completely using structured readers; an expansion for AF177563 and UID 5882278 yielded two further complete native rows. All five source metadata JSON files were separately parsed. Filename/history searches were also gitignore-independent. Absence statements here apply to these retained local sources, not to all possible publications or databases.

No own-taxon BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row was found, and no eligible culture-to-genome chain or SeqCode identity was found. Notable rejected matches explain why the clone must remain separate:

- BacDive 103676 identifies Rhodococcus sp. ST000624, taxon 194249, in `data/bacdive/records.jsonl.gz:27797`. The matching integer is in another namespace.
- CIP 103676 is an Enterococcus cecorum deposit, represented by BacDive 5321, species 44008, strain 1121864 and StrainInfo 10169/deposit 150566. Its full deposits and per-sequence deposit links were read at `data/straininfo/records.jsonl.gz:10169`. Associated LPSN Enterococcus/Streptococcus names, type material and marker/genome identifiers are evidence for that unrelated group, not D029.
- StrainInfo deposit 103676 is ATCC 25134, Mycobacterium intracellulare, taxon 1767, SI-ID 38373 (`data/straininfo/records.jsonl.gz:26769`). It is not NCBI taxon 103676.
- E. coli strain d029-11 has GCA_014080545.1 and SAMN11319324; E. coli strain 103676 has GCA_049978545.1 and SAMN14127139. Both native assembly records classify their source organisms as taxon 562, not this marine clone.
- CP103676 belongs to Klebsiella pneumoniae 2946, with GCA_024918095.1, SAMN28174011, BV-BRC 573.50478/573.50851 and GOLD Ga0608820. Those complete source rows supply no D029 identity.
- MGBC103676 is the distinct metagenome GCA_948830875.1, SAMeA source spelling `SAMEA112377617`, taxon 91750; Salmonella PNUSAS103676 is GCA_008804315.1, taxon 28901. Pseudomonas GCA/GCF_001036765.1 uses the assembly name ASM103676v1. Other GTDB hits are contig/scaffold statistics, and ATB DRR103676 belongs to E. coli sample SAMD00076019.
- The expanded sequence-UID search hit Klebsiella GCA_054541635.1 with genome length 5882278 and E. coli GCA_058822785.1 with assembly name ASM5882278v1. Neither denotes nucleotide UID 5882278. AF177563 was not found in the searched local source roots.

Zero inventoried strains agrees with the absence of own/descendant BacDive support; it is not a truncated list. Optional evidence, definition, causal graphs, discussions and datasets may remain absent in a seeded taxonomy-only record. The directly linked partial 16S is a potential enrichment lead, not a mandatory missing genome. There are no gene, regulator, trait or expression-module claims requiring an iModulonDB adapter; it is not applicable.

## Findings

None found in the record as emitted. The source's sequence ambiguity and external phylogenetic context do not contradict its limited taxonomic claims.

Counts: 0 blocker, 0 major, 0 minor.

## Recommended Edits

No corrective edit is needed. Keep the NCBI identity and lineage, zero source-backed strain count, and `SEEDED` lifecycle.

Optional enrichment could cite AF177563.1 as partial-marker evidence with the ambiguous base preserved. It would require a maintained source-import/overlay design and seeder support, not a hand edit or transfer from CIP 103676. NCBI identity projection belongs to `src/taxonmech/ncbi_taxdump.py`; generated-record emission belongs to `src/taxonmech/seed.py`. Any future change should include a focused regression test for its own identifier and provenance semantics.

## Follow-up Checks

For later authorized enrichment, recheck the exact clone and `taxon:103676` qualifiers, accession version and sequence length at NCBI, and retain the distinction between a marker, culture deposit and genome. Reject all source-namespace collisions above. Rerun the two focused validators; after a genuine generator change, inspect a canary and run `just verify-corpus` and `just qc`. This report neither ran those bulk gates nor uses its narrow pass to imply a corpus-wide pass.

## Additional Notes

Record SHA-256 before review: `e62334ad7d35d8b5013c809e1f3a9afffa8da3aef2071ba676e4ff7d1e011564`. HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The embedded 2026-09-13T17:54:04Z seed time is the maximum source-manifest time selected by `src/taxonmech/seed.py:_seed_timestamp`, not this review time. Its curator, action, sources and scope reason are internally consistent. No separate target history artifact was found in the ignored-inclusive search.

Only this new independent report was written for D029. No neighboring verdict was reused. The record, source inventories, history, scope, pages and statuses remain unchanged; no GitHub operation, branch or worktree mutation occurred. Eukaryota remained untouched.
