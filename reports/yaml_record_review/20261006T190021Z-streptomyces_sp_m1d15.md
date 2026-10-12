# YAML Record Review: Streptomyces sp. M1D15

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_sp_m1d15.yaml`
- Started UTC: 2026-10-06T18:58:08Z
- Finished UTC: 2026-10-06T19:00:21Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` for `NCBITaxon:1035266`, Streptomyces sp. M1D15, was read. It is a species-rank Bacteria placeholder, parent `NCBITaxon:2593676`, genetic code 11, ten ancestors, `EXACT` grounding and `SEEDED` lifecycle. It has zero BacDive strains, one NCBITAXON name attestation and one seed event. Synonyms, nomenclature, taxonomy mappings, deposits, genomes, phenotype evidence and causal edges are not stored.

Future fixes belong in maintained scope, source acquisition/extraction or `src/taxonmech/seed.py`, not the generated YAML.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/streptomyces_sp_m1d15.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/streptomyces_sp_m1d15.yaml --out /private/tmp/m15-strict.tsv`: exit 0, one record, zero errors. The actual TSV was read and was header-only.
- Bounded manual comparisons matched complete pinned identity, lineage, scope, path lock, attestation and inline history; they are not a focused reproduction gate.
- Not run: full `just verify-corpus`, `just qc`, tests, rendering, provenance and corpus-wide history gates. Inspection of the reproduction script confirmed no target selector; `--max-diffs` only limits output.
- Not applicable: `just validate-products` for added graph nodes; none are present. NCBITaxon references were checked at pinned and live authorities.
- Inline history passed target validation and matched scope. Ignored-inclusive content and filename searches found no target-specific external history entry.
- The structured `kg-microbe-sources imodulondb datasets` adapter ran before web follow-up. All 28 rows were inspected. S. albidoflavus and S. coelicolor datasets do not establish M1D15 identity, so no query was applicable; this absence is not negative biological evidence.

## Identity and Grounding

The full pinned backbone `data/raw/ncbitaxon_taxa.tsv:221975`, scientific-name row `data/catalog/ncbi_names-0005.jsonl.gz:31443`, unique path lock `data/taxa/PATHS.tsv:14466` and scope `curation/seed_scope.tsv:322250` agree with this record.

Live [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035266&retmode=xml) and [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035266) confirm the active species-rank placeholder. Root-first lineage is root, cellular organisms, Bacteria, Bacillati, Actinomycetota, Actinomycetes, Kitasatosporales, Streptomycetaceae, Streptomyces and unclassified Streptomyces. All stored ancestor IDs, labels and ranks match the pinned source, and live Datasets includes root. Exact checks found no type-material, merged-ID or dropped row, and no immediate child.

The inspected nomenclatural section of [LPSN's Streptomyces genus page](https://lpsn.dsmz.de/genus/streptomyces) describes a validly published correct genus name with S. albus as type species. Whole-page M1D15 search found no match. It supplies no formal target binomial, type deposit or synonym. Genus-level risk and synonym annotations are not target assertions.

## Evidence

One `NCBITAXON` `NAME` attestation has the exact ID/label and snapshot date 2026-09-13. Its count is not a strain or genome count. The `seed_from_sources` `SEEDED_FROM_SOURCES` event at `2026-09-13T17:54:04Z` agrees with the one-source scope reason and remains unchanged.

Full metadata for [JF729484.1](https://www.ncbi.nlm.nih.gov/nuccore/JF729484.1), UID 334086860, identify a 1,412-nt partial 16S rRNA marker, strain M1D15, exact taxon 1035266 and seagrass isolation source. W. Chen submitted it on 25 March 2011; creation and update dates are 31 May and 3 June 2011. Its references are an unpublished comparative seagrass study and direct submission, without PMID or DOI. No culture deposit, BioSample, BioProject, assembly, host species or collection-country qualifier is supplied. Submission address is not collection locality, and genomic-DNA provenance is not an assembly. Sequence bases were not analyzed.

The nearby [Wu et al. paper, DOI:10.5897/AJMR11.981](https://academicjournals.org/journal/AJMR/article-full-text-pdf/2A88A4617354), was checked as a candidate, not assumed applicable. All eight extracted pages lacked M1D15 and JF729484. The accession list, Figures 1 and 2 and Table 2 were visually inspected; none identifies M1D15. Its host species, locality and PCR results cannot be transferred to this isolate.

Bounded exact label, designation and accession searches supplied no additional inspected publication, culture or genome bridge. Search snippets and unrelated short-code hits were not used as evidence.

## Completeness

Searches used `rg --no-ignore --hidden -n -z -i`, including hidden, ignored and compressed files, across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Identifier, label, slug and designation pattern `\bM1D[- _]?15\b` yielded ten rows: three target rows and seven false numeric matches. Every matched row was read in full native metadata or TSV form. Five source-level `SOURCE.json` files and history filenames were checked separately.

A second JF729484 search across those roots, plus metadata and history filenames, found no match. These are bounded local snapshot results, not worldwide absence claims.

Exact comparisons found no target row in `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`. With no pinned descendants, zero BacDive strains follows the own-plus-descendant seeder rule and does not deny the laboratory isolate.

Exact non-expanding NCBI searches returned zero Assembly records and one nucleotide record. Assembly reported the taxid phrase not found, which is bounded index evidence. The CAFI-backed normalizer returned no eligible culture key for M1D15, M1D-15 or M1D 15. Bare labels and neighboring sequence accessions cannot establish deposit/genome relationships.

No consequential required omission was established. Empty optional nomenclature, phenotype, deposit and genome fields are appropriate. The missing bridge to a candidate publication is an enrichment limit, not a defect in the stored seed assertions.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the stored assertions. This pass does not certify full-corpus reproducibility.

## Recommended Edits

None required. Preserve exact placeholder identity, the one-name attestation, zero BacDive count and seeded lifecycle. Do not infer M1D15's host species, collection site or PCR-screen phenotype from nearby isolates.

Future authorized enrichment belongs in maintained acquisition/extraction and `src/taxonmech/seed.py`. Any literature representation requires supported maintained inputs and tests; generated YAML must not be hand-edited.

## Follow-up Checks

For literature enrichment, require an explicit M1D15/JF729484 link in inspected source text or supplementary data before assigning experimental claims. For genome association, require a whole eligible deposit and explicit source-specific sequence relationship. Keep taxon, strain, deposit, marker, sample, project and assembly identities distinct.

After an authorized input change, regenerate through the validated writer and rerun target schema/strict checks and full `just verify-corpus` and `just qc`. No regeneration, history write or lifecycle promotion occurred.

## Additional Notes

The seven numeric false matches were:

- Four Parabacteroides distasonis assertions, taxid 823, RTP21277st1_H3_RTP21277_210401, SAMN41035266, GCA/GCF_040924505.1, BV-BRC 823.5228: `data/bvbrc/bvbrc-0027.jsonl.gz:26397`, `data/catalog/ncbi_genbank-0037.jsonl.gz:20829`, `data/catalog/ncbi_refseq-0006.jsonl.gz:19975`, `data/catalog/gtdb_genomes-0009.jsonl.gz:35389`.
- Two Mycobacterium tuberculosis assertions for ERR1035266: BV-BRC 1773.18290 at `data/bvbrc/bvbrc-0006.jsonl.gz:6081`; ATB SAMEA3558799, ERZ9334380 at `data/catalog/allthebacteria.tsv.xz:569736`. Available FASTA and passing filters do not overcome the organism mismatch.
- Campylobacter jejuni PNUSAC013517, GCA_010352665.1, SAMN13337904 at `data/catalog/ncbi_genbank-0009.jsonl.gz:6467`.

HEAD was `b6a6508faca1388b88feb5740b1095e9f64cfdb8` on `codex/record-review-extensimonas-20261003`. Ignored-inclusive filename checks found no prior report for this stem, and the entire YAML was reread byte-unchanged. This new report was the only repository write for this target. No record, history, lifecycle, site, Git or GitHub state changed; Eukaryota remained untouched.

