# YAML Record Review: Duganella sp. LT12CD

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/duganella_sp_lt12cd.yaml`
- Started UTC: 2026-10-06T01:07:54Z
- Finished UTC: 2026-10-06T01:11:52Z
- Verdict: pass

## Target

Read the entire 56-line generated `TaxonRecord`: `NCBITaxon:1034911`, Duganella sp. LT12CD, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2636909` (unclassified Duganella). It carries eleven root-first lineage entries, genetic code 11, `EXACT` grounding, `SEEDED` mapping status, zero represented strains, one NCBITAXON NAME attestation, and one seed event dated `2026-09-13T17:54:04Z`. Optional synonym, nomenclature, mapping, strain, evidence, discussion and graph sections are not populated. This is a read-only review, not a human status promotion.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/duganella_sp_lt12cd.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/duganella_sp_lt12cd.yaml --out /private/tmp/lt12cd-validation.tsv`: exit 0, one file scanned, zero ERROR rows. Read the complete header-only TSV.
- Structured comparisons read the complete matching backbone and scope rows, checked every lineage ID/label/rank, resolved the unique identifier/slug pair, and compared every source attestation and the seed-event scope description. These bounded checks passed; they are not corpus regeneration.
- Exact-ID scans of `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv` and `data/raw/dropped.tsv` found no matching rows. Seven supplementary source inventories likewise contained no exact taxon-ID row; see Completeness for search scope.
- Live NCBI Taxonomy EFetch and Datasets responses were read completely. Exact, non-expanding Assembly and Nuccore queries were checked, and the one returned nucleotide record's complete metadata, references and feature annotations were inspected. Sequence bases were not reanalyzed.
- Not checked: full-corpus `just verify-corpus`, `just qc`, `just test`, `just validate-all`, full history validation, provenance hashes, rendered-site drift, README statistics, publication-size budget and vendored synchronization. This bounded report-only review does not establish those gates. The inline seed event was inspected, but that is not a history-schema run.
- `just validate-products` and iModulonDB were not applicable: no curator-added causal graph, gene, regulator, expression module or transcriptomic claim is present. No LPSN or GTDB assertion on this record required an authority-page check.

## Identity and Grounding

The ID, label, species rank, domain, parent and genetic code agree between the YAML, `data/raw/ncbitaxon_taxa.tsv:221739`, and the [NCBI Taxonomy EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034911&retmode=xml). The [NCBI Datasets response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034911) independently supplies the same ordered eleven ancestor IDs, including root.

The complete pinned chain is root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Betaproteobacteria, Burkholderiales, Oxalobacteraceae, Telluria group, Duganella and unclassified Duganella. All labels and ranks agree with the inspected taxonomy responses. Telluria group is a carried no-rank ancestor (`NCBITaxon:2895353`), not a synonym of this strain or a reason to replace its parent. GenBank's abbreviated organism lineage omits the unclassified intermediate; the dedicated taxonomy endpoints confirm it.

`data/taxa/PATHS.tsv:14209` uniquely associates this ID with `duganella_sp_lt12cd`; `curation/seed_scope.tsv:322041` gives the one-source NCBI attestation rule. The complete native name object at `data/catalog/ncbi_names-0005.jsonl.gz:31142` is a scientific-name entry for this same taxon. No alternate name was supplied in the inspected target name/taxonomy evidence. Species rank here is NCBI's rank for the provisional isolate-labelled taxon, not evidence of a formally named or validly published species.

## Evidence

The record's actual assertion is the NCBI name and taxonomy at the pinned `2026-09-13` snapshot. Its single NAME unit, source ID, label and snapshot note agree with the inventory; the count does not represent genomes or biological strain abundance. No unsupported phenotype, medium, ecological mechanism or type-strain assertion appears in the YAML.

The exact Nuccore query returned one record, [JF778662.1](https://www.ncbi.nlm.nih.gov/nuccore/JF778662.1): an 875-base partial 16S rRNA gene from Duganella sp. LT12CD, explicitly annotated with strain LT12CD, freshwater-lake isolation source and `taxon:1034911`. Both ends of the rRNA feature are partial. Its only reference is a 23 March 2011 direct submission by Huang, Swain, Thacker, Ravindra, Andersen and Bej. The submitted chimera-screening comment is not an independent analysis performed by this review. The complete metadata contain no culture-collection qualifier, BioSample, BioProject, assembly link, DOI or PMID. This is a marker accession, not a genome identifier or proof of a deposited culture.

The inspected primary article, [Huang et al., Aquatic Biosystems 9:4, DOI 10.1186/2046-9063-9-4](https://link.springer.com/article/10.1186/2046-9063-9-4), explicitly includes JF778662 in its submitted range JF778652-JF778667. Together with the matching submission authors, this supports a study-context association with Lake Tawani(P), East Antarctica. The main text describes a culture workflow using R2A at 15 C for ten days, alongside culture-independent methods. Those study methods and community results are not target-specific growth optima, psychrophily, metabolic traits, culture-deposit identity or genome evidence. Supplements and figure images were not inspected; no claims depend on them.

The exact Assembly search returned zero, with NCBI's phrase-not-found warning for `txid1034911[Organism:noexp]`. This describes that query's result, not proof that a genome could not exist under another taxon or identifier.

## Completeness

Ignored-inclusive, hidden-file and compressed-file searches used `rg --no-ignore --hidden -n -z -i`, excluding `SOURCE.json` manifests, across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. The taxon ID, full label and slug candidate scan produced 19 lines. The backbone and scope rows were read structurally; all remaining four native JSON objects and thirteen header-aware AllTheBacteria rows were read in full. Address reconciliation found no unread candidate.

Three lines identify the target: backbone, scope and the native NCBI scientific name. Sixteen are numeric substring collisions, not links:

- GenBank and GTDB entries for Rhodocyclaceae bacterium PROT-12, `NCBITaxon:1898103`, assembly `GCA_048499035.1`, BioSample `SAMN31034911` and project `PRJNA884640`. GTDB calls that different organism Desulfobacillus denitrificans; neither the classification nor the genome transfers to LT12CD.
- A GenBank Staphylococcus aureus 8-275-247 assembly (`GCA_027163245.1`, taxon 1280) and its AllTheBacteria sample match `SAMEA1034911`. The accession's numeric suffix is not this taxon ID.
- Ten AllTheBacteria Shigella sonnei rows with sample IDs `SAMEA110349110` through `SAMEA110349119`.
- One AllTheBacteria Neisseria meningitidis row, `SAMEA12303263`, where the numeric string occurs in a SeqKit sum.
- One AllTheBacteria Mycobacterium tuberculosis row, `SAMEA3558444`, run `ERR1034911`.

A separate ignored-inclusive scan of those same ten roots for `JF778662|LT[ -]?12[ -]?CD` returned only the same three target rows. Exact-ID comparisons in the BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories found no matching taxon row. Within these bounded retained sources, there is no supported missing deposit/genome association. The zero represented-strain count is consistent with the inventories and does not deny the existence of the named LT12CD isolate.

Ignored-inclusive ID/name/slug searches of prior reports and history found no existing target review/history match before this report; a filesystem filename search also found no prior target report. Optional nomenclature, mappings, synonyms and evidence slots need not be invented. A literature-context enrichment could be considered later, but the current taxonomy-only record does not require it to pass.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the reviewed record's asserted scope. Neither the marker accession, a bare strain designation, the genus-level paper discussion nor any numeric substring collision establishes a missing eligible culture/genome record. No observed conflict requires a local taxonomy change.

## Recommended Edits

None. Leave the generated YAML and `SEEDED` status unchanged.

Future primary taxonomy corrections belong at NCBI and then the pinned refresh in `conf/ncbi_taxdump.yaml` and extraction through `scripts/extract_source_inventory.py`; supported harmonization changes belong in `src/taxonmech/seed.py`, invoked by `scripts/seed_from_sources.py`. Scope policy belongs in `curation/seed_scope.tsv`. Any optional study-context enrichment first needs an explicitly maintained source representation with target-specific evidence. Do not hand-edit this generated record or use a partial 16S sequence as a genome.

## Follow-up Checks

No blocking follow-up remains for this verdict. If future evidence adds a deposit, assembly or identifier crosslink, inspect its full source-native object and prove the explicit target/deposit/source relationship before regeneration. For an authorized implementation, rerun the focused schema and strict validators, then the documented reproduction, provenance, history and relevant corpus gates. Recheck live taxonomy if the pinned dump is refreshed. An independent sequence-based placement assessment would require analyses not performed here.

## Additional Notes

Review performed on branch `codex/record-review-extensimonas-20261003`, HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. One existing worktree was listed; the user reported the other session closed. No additional worktree was created. Existing reports were preserved. Only this new report was added; validation diagnostics were directed to `/private/tmp`. No records, inventories, scope, prior reports, history, lifecycle statuses or generated pages were edited, and no commits, GitHub mutations, external contacts or paid research were performed. Eukaryota was left untouched.
