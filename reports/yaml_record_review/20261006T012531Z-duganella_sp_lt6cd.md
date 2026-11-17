# YAML Record Review: Duganella sp. LT6CD

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/duganella_sp_lt6cd.yaml`
- Started UTC: 2026-10-06T01:23:18Z
- Finished UTC: 2026-10-06T01:25:31Z
- Verdict: pass

## Target

Read the entire 56-line generated `TaxonRecord` for `NCBITaxon:1034915`, Duganella sp. LT6CD. It carries rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2636909` (unclassified Duganella), eleven root-first lineage entries, genetic code 11, `EXACT` grounding and `SEEDED` mapping status. It has zero represented strains, one NCBITAXON NAME assertion at snapshot `2026-09-13`, and one inline `SEEDED_FROM_SOURCES` event dated `2026-09-13T17:54:04Z`. Optional synonyms, nomenclature, mappings, strain entries, evidence, discussions and causal graph are unpopulated.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/duganella_sp_lt6cd.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/duganella_sp_lt6cd.yaml --out /private/tmp/lt6cd-validation.tsv`: exit 0, one file scanned, zero ERROR rows. Read the complete header-only TSV.
- Structured comparisons read the full target backbone and scope rows and checked every ancestor ID/label/rank, unique PATHS mapping, attestation and inline seed-event description. The backbone scan returned no children. These are bounded comparisons, not full-corpus reproduction.
- Exact-ID scans of the complete `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv` and `data/raw/dropped.tsv` found no target row. Seven supplementary source inventories also returned no exact target-ID match.
- Complete live NCBI Taxonomy EFetch and Datasets responses, exact non-expanding Assembly/Nuccore search results, and the sole nucleotide hit's full metadata, references and feature annotations were inspected. Sequence bases were not reanalyzed.
- Not checked: full-corpus `just verify-corpus`, `just qc`, `just test`, `just validate-all`, full history validation, provenance hashes, rendered-site drift, README statistics, publication-size budget or vendored synchronization. This bounded report-only review does not claim those gates. Inline-event inspection is not history-schema validation.
- `just validate-products` and iModulonDB were not applicable: no curator-added graph grounding, gene, regulator, expression module or transcriptomic claim is asserted. No target LPSN/GTDB assertion required an authority-page check.

## Identity and Grounding

The full backbone row at `data/raw/ncbitaxon_taxa.tsv:221743` agrees with the YAML. Live [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034915&retmode=xml) confirms ID, exact label, species rank, parent, bacterial division and code 11. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034915) confirms the target and all eleven ordered ancestor IDs, including root.

The chain is root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Betaproteobacteria, Burkholderiales, Oxalobacteraceae, Telluria group, Duganella and unclassified Duganella. Labels and ranks agree with the pinned inventory and inspected taxonomy evidence. Telluria group (`NCBITaxon:2895353`) is a no-rank ancestor, not a synonym or alternate genus assignment. GenBank's abbreviated lineage omits the unclassified intermediate, which the dedicated taxonomy endpoints explicitly retain.

`data/taxa/PATHS.tsv:14213` uniquely assigns `duganella_sp_lt6cd` to this ID. `curation/seed_scope.tsv:322045` records the one-source NCBI inclusion rule. The complete native scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:31146` identifies the same taxon. No alternate target name is supplied by the inspected taxonomy evidence. Species rank for this provisional isolate-labelled NCBI entity does not establish formal nomenclatural validity or equivalence with another LT-labelled isolate.

## Evidence

The target's assertion is source-backed NCBI identity and carried lineage, not physiology, nomenclature or a genome. The source ID, label, snapshot, NAME unit and count of one agree with the inventory. Name assertions are not strain or genome counts. No unsupported phenotype, medium, causal mechanism or type-strain claim is present.

The exact Nuccore query returned UID 333496488. The complete [JF778657.1 record](https://www.ncbi.nlm.nih.gov/nuccore/JF778657.1) is a 941-base partial 16S rRNA gene, partial at both ends, explicitly annotated with Duganella sp. LT6CD, strain LT6CD, freshwater-lake isolation source and `taxon:1034915`. Its only reference is a 23 March 2011 direct submission by Huang, Swain, Thacker, Ravindra, Andersen and Bej. The submitter's Bellerophon-screening comment was not independently tested here. The full metadata contain no culture-collection qualifier, BioSample, BioProject, assembly, DOI or PMID. The marker and bare strain name do not establish a culture-deposit/genome relationship.

The inspected main text of [Huang et al., Aquatic Biosystems 9:4](https://link.springer.com/article/10.1186/2046-9063-9-4) includes JF778657 within JF778652-JF778667. That accession range and matching authors support a Lake Tawani(P), East Antarctica study association. Community results and study conditions are not LT6CD-specific phenotype, growth-optimum or deposit evidence. Supplements and figure images were not inspected.

The exact Assembly query returned zero with a phrase-not-found warning for `txid1034915[Organism:noexp]`. This is a bounded result, not proof of genome absence under every other identifier or taxon.

## Completeness

Ignored-inclusive searches used `rg --no-ignore --hidden -n -z -i`, including hidden/compressed files and excluding `SOURCE.json` manifests, across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Searching the ID digits, full label and slug yielded 26 lines. Backbone and scope were read structurally; all other twelve native JSON objects and twelve complete header-aware AllTheBacteria rows were read. Reconciliation found no unread or truncated candidate.

Three rows identify the target: backbone, scope and NCBI scientific name. The remaining 23 are numeric collisions with unrelated organisms:

- Five objects concern Pseudomonas aeruginosa Pae_CF67.08c, taxon 287: GOLD analysis `Ga0158526` naming project `Gp0189757` and assembly `GCA_001034915.1`; BV-BRC `287.1597`; paired GenBank/RefSeq `GCA_001034915.1`/`GCF_001034915.1`; and GTDB `RS_GCF_001034915.1`. The assembly objects explicitly identify that different organism and sample `SAMN03566367`. GOLD's organism-ID field is empty. None supplies an LT6CD identity chain; an assembly accession's numeric substring is not an NCBI taxon link.
- Three GenBank objects are Klebsiella pneumoniae isolate 1922711, taxon 573, sample `SAMN34998340`: replaced `GCA_031034915.1` and `.2`, and latest `.3`. Assembly version history does not turn this different isolate into LT6CD.
- GenBank `GCA_061034915.1` is Blautia fusiformis isolate 1755_1755L_C_7, taxon 2881264, sample `SAMN60702909`, project `PRJNA1464738`, derived from a metagenome.
- BV-BRC `1773.20369` is Mycobacterium tuberculosis ERR1034915, taxon 1773; the AllTheBacteria row for run `ERR1034915` is Mycobacterium tuberculosis sample `SAMEA3558448`, analysis `ERZ3501196`.
- GenBank `GCA_027162245.1` is Staphylococcus aureus 8-326-146, taxon 1280, sample `SAMEA1034915`, project `PRJNA514245`; the AllTheBacteria sample row is also Staphylococcus aureus, analysis `ERZ3070313`, run `ERR086095`.
- Ten AllTheBacteria rows identify Shigella sonnei samples `SAMEA110349150` through `SAMEA110349159`.

A second ignored-inclusive search over the same ten roots for `JF778657|LT[ -]?6[ -]?CD` returned only the same three target rows. Exact-ID structured scans of the BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories returned no target row. Within those bounded retained sources, no eligible missing strain/deposit/genome association is supported. Zero represented strains does not deny that the named LT6CD isolate exists.

Ignored-inclusive ID/name/slug searches of `reports` and `history`, plus a filesystem review-filename search, found no prior target report/history match before this report. No required missing synonym, nomenclature, mapping, graph or evidence object was established. Optional study-context enrichment is not required for this taxonomy-only record to pass.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The asserted identity, lineage, provenance, count semantics and seeded status are supported. Unrelated GOLD/GTDB/genome records and marker evidence do not justify adding an LT6CD genome relationship.

## Recommended Edits

None. Keep the generated YAML and `SEEDED` status unchanged.

Future taxonomy corrections belong at NCBI, followed by the pinned refresh in `conf/ncbi_taxdump.yaml` and extraction through `scripts/extract_source_inventory.py`. Harmonization belongs in `src/taxonmech/seed.py`, invoked by `scripts/seed_from_sources.py`; scope policy belongs in `curation/seed_scope.tsv`. A future study-context extension requires a maintained input and explicit target-specific support. Do not hand-edit generated records or count the partial marker as a genome.

## Follow-up Checks

No blocking follow-up remains. Any new deposit or genome candidate needs full source-native identity and linkage verification before authorized regeneration. Then rerun focused schema/strict validation and the documented reproduction, provenance, history and relevant full-corpus gates. Recheck live taxonomy when refreshing the pinned dump. Independent sequence placement and chimera analysis were outside this review.

## Additional Notes

Branch `codex/record-review-extensimonas-20261003`, HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`; tracked guidance and relevant code had no baseline diff. One existing worktree was listed, with the other session reported closed; no additional worktree was created. This target review adds only this report, with diagnostics under `/private/tmp`. Records, inventories, scope, history, statuses, prior reports and generated pages were preserved. No commits, GitHub mutations, external contacts or paid research occurred. Eukaryota was left untouched.
