# YAML Record Review: Glycomyces sp. HCZ4

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/glycomyces_sp_hcz4.yaml`
- Started UTC: 2026-10-06T18:17:08Z
- Finished UTC: 2026-10-06T18:22:25Z
- Verdict: pass

## Target

One complete generated `TaxonRecord`, `NCBITaxon:1035258`, was read and reviewed. The record represents the NCBI species-rank placeholder Glycomyces sp. HCZ4, not the genus, a formally named neighboring species, a culture deposit, or a genome. Its bacterial domain, parent `NCBITaxon:2637084`, genetic code 11, `EXACT` grounding, `SEEDED` lifecycle, zero BacDive strain count, sole NCBITAXON name attestation and seed event were checked. There are no additional synonym, nomenclature, mapping, genome, evidence, definition or causal-graph claims in the YAML.

The maintained scope is `curation/seed_scope.tsv`; pinned evidence is in `data/raw/` and the native catalogs. Generation is owned by `src/taxonmech/seed.py`. The YAML is not a curator-editable input.

## Validation

Commands used the offline project environment with `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/glycomyces_sp_hcz4.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/glycomyces_sp_hcz4.yaml --out /private/tmp/ghcz-strict.tsv`: exit 0; one file, zero errors. The actual TSV was read and contained only its header.
- A bounded, read-only structured comparison checked the full pinned parent chain, identity, code, NCBI attestation, source tables, path lock and scope-derived seed-event text. All comparisons passed. This was a manual evidence check, not a new focused reproduction validator.
- `just verify-corpus` was not run: its documented CLI exposes only the full-corpus reproduction gate, with no target selector. Full `just qc`, provenance, rendering, tests and corpus-wide history validation were not run for this read-only target review; no full-corpus green result is claimed.
- `just validate-products` was not run: `conf/id_label_targets.yaml` targets curator-added ontology graph nodes, and this record has none. Taxonomic IDs were checked against the pinned backbone and live NCBI instead.
- The only inline history entry is the generated seed event. Its shape passed strict validation and its scope text matched. Ignored-inclusive history content and filename searches found no target-specific external history record to validate.
- Before literature follow-up, the structured `kg-microbe-sources imodulondb datasets` adapter was run through the local `culturebotai-claw` checkout. Its 28 returned datasets contained no Glycomyces organism. It is not applicable, not negative evidence.

## Identity and Grounding

The exact pinned row is `data/raw/ncbitaxon_taxa.tsv:221967`; the sole native scientific-name row is `data/catalog/ncbi_names-0005.jsonl.gz:31435`. They agree with the complete YAML. The path lock is `data/taxa/PATHS.tsv:14458` and the unique scope entry is `curation/seed_scope.tsv:322242`.

Live [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035258&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035258) agree on the active name, species rank, parent and lineage. The ten root-first ancestors are root, cellular organisms, Bacteria, Bacillati, Actinomycetota, Actinomycetes, Glycomycetales, Glycomycetaceae, Glycomyces and unclassified Glycomyces. Every stored ancestor ID, label and rank matches the pinned chain; Datasets includes root explicitly. Exact checks of the pinned type-material, merged-ID and dropped tables returned no target row. No immediate child occurs in the pinned backbone.

The [LPSN Glycomyces genus page](https://lpsn.dsmz.de/genus/glycomyces), record 515715, describes a validly published, correct genus whose type species is G. harbinensis. It does not establish HCZ4 as a named species or type strain. Its displayed children and whole-page HCZ search supplied no HCZ4 entry. Genus nomenclature and neighboring species' deposits must not be inherited by this placeholder.

## Evidence

The source attestation is exactly one `NCBITAXON` assertion with unit `NAME`, dated to the 2026-09-13 taxonomy snapshot. It is not a strain or genome count. The seed event timestamp is `2026-09-13T17:54:04Z`, curator `seed_from_sources`, action `SEEDED_FROM_SOURCES`; its one-source scope explanation matches the maintained scope row.

The complete metadata for [JF729475.1](https://www.ncbi.nlm.nih.gov/nuccore/JF729475.1), UID 334086851, identify a 1,395-nt partial 16S rRNA sequence with strain HCZ4 and exact taxon 1035258. The isolation source is seagrass. W. Chen submitted it on 25 March 2011; the record was created 31 May and updated 3 June 2011. Its references comprise an unpublished study and the direct submission, without a PMID or DOI. There is no culture-deposit, BioSample, BioProject, assembly or geographic source qualifier. The submitter's Chinese institution alone is not a sampling-locality assertion. Sequence bases were not reanalyzed.

The [publisher PDF of Wu et al., DOI:10.5897/AJMR11.981](https://academicjournals.org/journal/AJMR/article-full-text-pdf/2A88A4617354) was inspected, including rendered pages 88, 90 and 92. Methods explicitly pair HCZ4 with JF729475 and describe Thalassia hemprichii collected at Nancun Port, China, in October 2010. Figure 1 separates HCZ4 from the G. arizonensis comparator. Table 2 reports 96.88% identity to that closest named species, with PKS-I screening negative and PKS-II/NRPS screening positive; its footnote defines these as PCR outcomes. The authors regard HCZ4 as a possible novel species. This supports retaining the unresolved species label, not adding G. arizonensis as an equivalent name. PCR screening does not establish a complete genome, expressed pathway, identified natural product or measured antimicrobial effect.

A separate [Sweet and Bythell study](https://doi.org/10.1111/j.1462-2920.2012.02746.x), PMID 22507379, was inspected through its [public Europe PMC XML](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3465780/fullTextXML). Figure 2 uses JF729475 as a closest BLAST reference for a coral-associated band; the text discusses its own Glycomyces-related sequence JN406287. That is not an HCZ4 strain-identity bridge. The authors explicitly limit causal interpretation of their culture-independent observations. No coral isolation or pathogenicity claim transfers to this record.

## Completeness

The ignored-inclusive, compressed-file search used `rg --no-ignore --hidden -n -z -i` for taxid, full label, slug and the bounded designation pattern `\bHCZ[- _]?4\b` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All ten matching rows were inspected in their full native metadata or TSV form: three target rows and seven unrelated numeric-substring hits. Five source-level `SOURCE.json` files were parsed separately; none added a target match. A separate compressed, ignored-inclusive JF729475 search over those same ten roots returned no match. This is a bounded snapshot search, not a claim about every external database or every ignored directory.

Exact taxon lookups in `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` and `bactotraits_taxa.tsv` all returned no row. With no backbone descendants, the zero BacDive count is consistent with the seeder's own-plus-descendant gathering rule.

The live NCBI exact, non-expanding taxid query returned zero Assembly results and one nucleotide result. Assembly reported the taxid phrase as not found; this is a bounded index result, not proof that a genome cannot exist elsewhere. HCZ4, HCZ-4 and HCZ 4 all normalize to no eligible culture identifier in the existing CAFI-backed matcher. Neither a bare strain designation nor this marker accession supplies a deposit-to-genome link.

Optional literature evidence could preserve the exact marker and paper relationship in a future supported curation model. Its absence is not a required-field defect under `docs/CURATION.md`. Source attestation already supplies provenance for this seeded record. No consequential omission or unsupported populated assertion was established.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the checked record and evidence scope. The pass does not certify all external biology or full-corpus reproducibility. The literature scope restrictions above are safeguards for future enrichment, not defects presently asserted in the YAML.

## Recommended Edits

None required. Retain the identity, seeded lifecycle, NCBI name unit and zero BacDive count. Do not hand-edit this generated record or promote it to human-reviewed status.

Any later marker/literature enrichment must be implemented through a maintained input or supported overlay and `src/taxonmech/seed.py`, with tests and schema support where needed. Do not invent a BacDive strain or use a marker as an assembly. Habitat, culture and phenotype claims belong in the appropriate sibling corpus with exact strain-scoped evidence.

## Follow-up Checks

For any future source refresh, repeat exact NCBI identity and status checks, the native designation/accession search, and deposit-specific genome joins before changing the record. Preserve the marker/publication association without converting nearest-neighbor similarity or PCR screening into equivalence or phenotype claims.

After an authorized maintained-input change, regenerate through the validated writer, run this target's schema and strict validators, then the documented full `just verify-corpus` and `just qc` gates. This review itself performed no regeneration.

## Additional Notes

The seven rejected search hits were:
- Four Odoribacter splanchnicus assertions, taxid 28118, strain 2201st1_F12_2201SCRN_220225, sample SAMN41035258, GCA/GCF_040924655.1 and BV-BRC 28118.2183: `data/bvbrc/bvbrc-0015.jsonl.gz:45158`, `data/catalog/ncbi_genbank-0037.jsonl.gz:20837`, `data/catalog/ncbi_refseq-0006.jsonl.gz:19983`, and `data/catalog/gtdb_genomes-0011.jsonl.gz:13433`.
- Two Mycobacterium tuberculosis assertions matching run ERR1035258, not taxid 1035258: BV-BRC 1773.18280 at `data/bvbrc/bvbrc-0006.jsonl.gz:6070`; ATB sample SAMEA3558791, analysis ERZ9334363 at `data/catalog/allthebacteria.tsv.xz:569728`. Available FASTA and passing ATB filters do not connect that sample to HCZ4.
- Campylobacter jejuni taxid 197, strain PNUSAC014938, GCA_010352585.1 and SAMN13825582 at `data/catalog/ncbi_genbank-0009.jsonl.gz:6463`.

Some web fetches failed: the first publisher abstract request and Wiley page returned 403, the PMC HTML follow-up showed a browser check, the institution page timed out, and CiteSeer/ResearchGate download leads failed. The public publisher article route and its declared PDF link ultimately returned 200; Europe PMC's public XML supplied the coral-study text. No access control was bypassed. An initial HTML-link extraction attempt lacked BeautifulSoup; the standard-library HTML parser succeeded without changing dependencies. PDF text extraction used cached PyMuPDF; rendered methods, Figure 1 and Table 2 were inspected to verify column and row alignment. No supplements or new sequence analyses were performed.

At review time HEAD was `b6a6508faca1388b88feb5740b1095e9f64cfdb8` on `codex/record-review-extensimonas-20261003`. An ignored-inclusive prior-report filename search found no HCZ4 report before this write. The complete target was reread byte-identical to its initial contents. Only this new report was written in the repository; scratch diagnostics and downloaded source material used temporary storage. No YAML, history, lifecycle, generated pages, Git or GitHub state was changed. No Eukaryota TaxonRecord was reopened.

