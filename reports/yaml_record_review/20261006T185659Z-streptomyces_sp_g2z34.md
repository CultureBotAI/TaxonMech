# YAML Record Review: Streptomyces sp. G2Z34

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_sp_g2z34.yaml`
- Started UTC: 2026-10-06T18:54:14Z
- Finished UTC: 2026-10-06T18:56:59Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` was read: `NCBITaxon:1035265`, Streptomyces sp. G2Z34, species-rank Bacteria placeholder, parent `NCBITaxon:2593676`, genetic code 11, ten root-first ancestors, `EXACT` grounding and `SEEDED` lifecycle. It stores zero BacDive strains, one NCBITAXON name attestation and one seed event, with no synonyms, nomenclature, mappings, deposits, genomes, traits or causal edges.

Maintained scope, acquisition/extraction and `src/taxonmech/seed.py` own future corrections. The generated YAML is not a curation input.

## Validation

Commands used the offline project runner with `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/streptomyces_sp_g2z34.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/streptomyces_sp_g2z34.yaml --out /private/tmp/g34-strict.tsv`: exit 0, one record, zero errors. Actual TSV read: header only.
- Full pinned lineage, identity, scope, path lock, attestation and inline history matched in bounded manual comparisons, not a focused reproduction validator.
- Not run: full `just verify-corpus`, `just qc`, tests, rendering, provenance and corpus-wide history gates. The reproduction script has no target selector; `--max-diffs` limits output only.
- Not applicable: `just validate-products` for added graph nodes; none are stored. NCBITaxon references were checked at pinned and live authorities.
- Inline history passed schema/strict checks. Ignored-inclusive content and filename searches found no target-specific external history entry.
- The structured `kg-microbe-sources imodulondb datasets` adapter initially failed DNS in the sandbox; an authorized read-only retry succeeded before web follow-up. All 28 rows were inspected. The covered S. albidoflavus and S. coelicolor datasets do not identify G2Z34, so no organism-specific query was applicable. Absence is not negative evidence.

## Identity and Grounding

The complete pinned backbone `data/raw/ncbitaxon_taxa.tsv:221974`, name `data/catalog/ncbi_names-0005.jsonl.gz:31442`, path lock `data/taxa/PATHS.tsv:14465` and scope `curation/seed_scope.tsv:322249` agree with the record.

Live [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035265&retmode=xml) and [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035265) confirm the active label, species rank and lineage. The root-first chain is root, cellular organisms, Bacteria, Bacillati, Actinomycetota, Actinomycetes, Kitasatosporales, Streptomycetaceae, Streptomyces and unclassified Streptomyces. All stored ancestor IDs, labels and ranks match the pinned source. Exact checks found no type-material, merged-ID or dropped row, and no child.

The inspected nomenclatural section of [LPSN's Streptomyces genus page](https://lpsn.dsmz.de/genus/streptomyces) identifies a validly published correct genus name with S. albus as type species. Whole-page search found no G2Z34. Genus synonymy, risk annotations and neighboring species' deposits do not supply target-specific nomenclature or equivalence.

## Evidence

The single `NCBITAXON` `NAME` assertion has the exact ID and label, snapshot 2026-09-13. Its count is not a strain or genome count. The `seed_from_sources` `SEEDED_FROM_SOURCES` event at `2026-09-13T17:54:04Z` matches the one-source scope explanation.

Full metadata for [JF729480.1](https://www.ncbi.nlm.nih.gov/nuccore/JF729480.1), UID 334086856, identify a 1,398-nt partial 16S rRNA marker, strain G2Z34, exact taxon 1035265 and seagrass isolation source. W. Chen submitted it on 25 March 2011; creation and update dates are 31 May and 3 June 2011. The unpublished study and direct-submission references carry no PMID or DOI. Metadata supply no culture deposit, BioSample, BioProject, assembly, host species or collection-country qualifier. Institutional address is not collection locality; genomic DNA is not whole-genome evidence. Sequence bases were not analyzed.

[Wu et al., DOI:10.5897/AJMR11.981](https://academicjournals.org/journal/AJMR/article-full-text-pdf/2A88A4617354), printed page 88, explicitly links G2Z34/JF729480. Visually inspected Figure 2 separates G2Z34 from S. nanshensis EU589334. Table 2 reports 98.91% similarity and PCR screens PKS-I negative, PKS-II positive, NRPS positive. These results do not establish species identity, assembled biosynthetic clusters or antimicrobial activity.

Exact designation and accession web searches supplied no additional inspected deposit or genome bridge. A mirror of the same primary paper was a search lead; the publisher PDF was the evidence inspected.

## Completeness

Ignored-independent searches used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, covering hidden, ignored and compressed inputs. The identifier, label, slug and designation pattern `\bG2Z[- _]?34\b` produced twelve rows: three target rows and nine false numeric matches, all read in complete native form. All five source-level `SOURCE.json` files and history filenames were checked separately.

A second JF729480 search across those roots, plus metadata/history filenames, returned no match. These are bounded snapshot results, not worldwide absence claims.

Exact comparisons found no target row in `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`. With no pinned descendants, zero BacDive strains agrees with the seeder's own-plus-descendant rule; it does not deny the laboratory isolate.

Live non-expanding NCBI searches returned zero Assembly records and one nucleotide record. Assembly marked the taxid phrase not found, a bounded index result. The CAFI-backed normalizer returned no eligible culture key for G2Z34, G2Z-34 or G2Z 34. No valid strain/deposit/genome chain was established.

No consequential required omission was found. Optional literature context need not be stored in this source-attested seed; unsupported nomenclature, deposits, genomes and phenotypes should remain empty.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the stored assertions. The pass is record-specific, not a corpus reproducibility certificate.

## Recommended Edits

None required. Preserve the NCBI placeholder, one-name count, zero BacDive strains and seeded lifecycle. Do not equate G2Z34 with S. nanshensis or assign it another Streptomyces dataset.

Future authorized enrichment belongs in maintained acquisition/extraction and `src/taxonmech/seed.py`, with supported inputs and tests for any new literature representation. Do not hand-edit generated YAML.

## Follow-up Checks

Any literature enrichment must retain the exact G2Z34/JF729480 relationship and PCR-screen scope. Genome associations require an eligible whole culture accession and explicit source-specific chain; marker, taxon, sample, project, strain and assembly identities remain distinct.

After authorized upstream changes, regenerate through the validated writer and rerun target schema/strict checks, full `just verify-corpus` and `just qc`. No regeneration or lifecycle promotion occurred.

## Additional Notes

The nine numeric false matches were:

- Four Parabacteroides distasonis assertions, taxid 823, RTP21277st1_D4_RTP21277_210401, SAMN41035265, GCA/GCF_040924525.1, BV-BRC 823.5229: `data/catalog/ncbi_genbank-0037.jsonl.gz:20830`, `data/bvbrc/bvbrc-0027.jsonl.gz:26398`, `data/catalog/gtdb_genomes-0016.jsonl.gz:28483`, `data/catalog/ncbi_refseq-0006.jsonl.gz:19976`.
- Two Mycobacterium tuberculosis assertions for ERR1035265: BV-BRC 1773.18288 at `data/bvbrc/bvbrc-0006.jsonl.gz:6078`; ATB SAMEA3558798, ERZ9334374 at `data/catalog/allthebacteria.tsv.xz:569735`.
- Klebsiella pneumoniae zj02015, GCA_041035265.1, SAMN37542636 at `data/catalog/ncbi_genbank-0037.jsonl.gz:25651`.
- Enterobacter hormaechei PP98, GCA_021035265.1, SAMEA8581607 at `data/catalog/ncbi_genbank-0019.jsonl.gz:18995`.
- Salmonella enterica, SAMN14247367, ERZ25728530, SRR11233949, whose SeqKit sum contains the digits, at `data/catalog/allthebacteria.tsv.xz:1794203`. Both ATB rows have available FASTAs and passing filters, but neither organism is this target.

HEAD was `b6a6508faca1388b88feb5740b1095e9f64cfdb8` on `codex/record-review-extensimonas-20261003`. Ignored-inclusive filename searches found no prior report for this stem. The full YAML was reread byte-unchanged. Only this new report was written for this target; temporary validation output and existing publisher-PDF renderings were used. No record, history, lifecycle, site, Git or GitHub state changed; Eukaryota was not reopened.

