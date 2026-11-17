# YAML Record Review: Streptomyces sp. M1X63

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_sp_m1x63.yaml`
- Started UTC: 2026-10-06T19:01:32Z
- Finished UTC: 2026-10-06T19:03:36Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` was read before judgement: `NCBITaxon:1035267`, Streptomyces sp. M1X63, species-rank Bacteria placeholder, parent `NCBITaxon:2593676`, genetic code 11 and ten root-first ancestors. It has `EXACT` grounding, `SEEDED` lifecycle, zero BacDive strains, one NCBITAXON name attestation and one seed event. There are no synonym, nomenclature, mapping, culture-deposit, genome, trait or causal-graph assertions.

Maintained scope, source acquisition/extraction and `src/taxonmech/seed.py` own future fixes. The generated record is not a curation input.

## Validation

Commands used the offline project runner with `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/streptomyces_sp_m1x63.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/streptomyces_sp_m1x63.yaml --out /private/tmp/mx63-strict.tsv`: exit 0, one record, zero errors. Actual diagnostic TSV read: header only.
- Bounded manual comparisons verified complete pinned identity, lineage, path lock, scope, attestation and inline history. These are not a focused reproduction validator.
- Not run: full `just verify-corpus`, `just qc`, tests, rendering, provenance and corpus-wide history gates. The reproduction script has no target selector; `--max-diffs` only limits output.
- Not applicable: `just validate-products` for curator-added graph nodes; none are present. NCBITaxon references were compared with pinned and live authorities.
- Inline history passed target validation and matched scope. Ignored-inclusive content and history-filename checks found no target-specific external history entry.
- The structured `kg-microbe-sources imodulondb datasets` adapter ran before web follow-up. All 28 rows were inspected. The S. albidoflavus and S. coelicolor datasets are not evidence for M1X63, so no target-specific query was applicable; absence is not negative biological evidence.

## Identity and Grounding

The full pinned backbone `data/raw/ncbitaxon_taxa.tsv:221976`, name row `data/catalog/ncbi_names-0005.jsonl.gz:31444`, unique path lock `data/taxa/PATHS.tsv:14467` and scope `curation/seed_scope.tsv:322251` agree.

Live [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035267&retmode=xml) and [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035267) confirm the active species-rank label, parent and lineage. The root-first chain is root, cellular organisms, Bacteria, Bacillati, Actinomycetota, Actinomycetes, Kitasatosporales, Streptomycetaceae, Streptomyces and unclassified Streptomyces. Every stored ancestor ID, label and rank matches the pinned source, and Datasets includes root. Exact checks found no type-material, merged-ID or dropped row, and no child.

The inspected nomenclatural section of [LPSN's Streptomyces page](https://lpsn.dsmz.de/genus/streptomyces) concerns a validly published correct genus name with S. albus as type species. Whole-page search found no M1X63. It supplies no target-specific formal name, type deposit or synonym; genus risk and synonymy must not be inherited.

## Evidence

The sole `NCBITAXON` `NAME` attestation carries the exact ID/label and snapshot 2026-09-13. Its count is not a genome or biological strain count. The `seed_from_sources` `SEEDED_FROM_SOURCES` event at `2026-09-13T17:54:04Z` agrees with the one-source scope reason.

Full metadata for [JF729483.1](https://www.ncbi.nlm.nih.gov/nuccore/JF729483.1), UID 334086859, identify a 1,426-nt partial 16S rRNA marker, strain M1X63, exact taxon 1035267 and seagrass isolation source. W. Chen submitted it on 25 March 2011; creation and update dates are 31 May and 3 June 2011. Its references are an unpublished comparative seagrass study and direct submission, with no PMID or DOI. No culture deposit, BioSample, BioProject, assembly, host species or collection-country qualifier is supplied. Institutional address is not collection-locality evidence, and genomic DNA is not an assembly. Sequence bases were not analyzed.

The nearby [Wu et al. paper, DOI:10.5897/AJMR11.981](https://academicjournals.org/journal/AJMR/article-full-text-pdf/2A88A4617354), had no M1X63 or JF729483 match across all eight extracted pages. Visual inspection of its accession list, Figures 1 and 2 and Table 2 likewise supplied no target link. Its experimental claims cannot be transferred here.

Exact label, designation and accession web searches supplied no further inspected publication, deposit or genome bridge. Search snippets and unrelated short-code matches were not treated as evidence.

## Completeness

Searches used `rg --no-ignore --hidden -n -z -i`, covering ignored, hidden and compressed inputs across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Identifier, label, slug and bounded designation pattern `\bM1X[- _]?63\b` yielded ten rows: three target rows and seven false numeric matches, all read in complete source-native metadata or TSV form. Five source-level `SOURCE.json` files and history filenames were checked separately.

A second JF729483 search across those roots, plus metadata and history filenames, returned no match. These are bounded snapshot findings, not worldwide absence claims.

Exact comparisons found no target rows in `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`. No pinned descendants can contribute BacDive strains. Zero agrees with the seeder's own-plus-descendant rule without denying the laboratory isolate.

Live non-expanding NCBI searches returned zero Assembly records and one nucleotide record. Assembly also reported the taxid phrase not found, a bounded index result. The CAFI-backed normalizer returned no eligible culture key for M1X63, M1X-63 or M1X 63. No valid deposit/genome chain was established.

No consequential required omission was found. Optional nomenclature, phenotype, deposit and genome fields are correctly empty pending appropriate source evidence. The unresolved literature bridge limits enrichment, not the validity of the current seed assertions.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the stored assertions. This is not a full-corpus reproducibility certificate.

## Recommended Edits

None required. Preserve the NCBI placeholder, one-name attestation, zero BacDive count and seeded lifecycle. Do not import neighboring isolates' species identities, host/locality claims or PCR results.

Future authorized enrichment belongs in maintained acquisition/extraction and `src/taxonmech/seed.py`, with supported inputs and tests for any literature representation. Do not hand-edit generated YAML.

## Follow-up Checks

A literature claim requires inspected evidence explicitly linking M1X63/JF729483 to the experiment. Genome association requires an eligible whole culture accession and explicit source-specific deposit/sequence chain. Keep taxon, strain, deposit, marker, sample, project and assembly identities distinct.

After authorized upstream changes, regenerate through the validated writer and rerun target schema/strict checks and full `just verify-corpus` and `just qc`. No regeneration or lifecycle promotion occurred.

## Additional Notes

The seven numeric false matches were:

- Four Parabacteroides merdae assertions, taxid 46503, RTP21002st1_C6_RTP21002_201210, SAMN41035267, GCA/GCF_040924485.1, BV-BRC 46503.3055: `data/bvbrc/bvbrc-0020.jsonl.gz:25658`, `data/catalog/ncbi_genbank-0037.jsonl.gz:20828`, `data/catalog/ncbi_refseq-0006.jsonl.gz:19974`, `data/catalog/gtdb_genomes-0014.jsonl.gz:35972`.
- Two Mycobacterium tuberculosis assertions for ERR1035267: BV-BRC 1773.18297 at `data/bvbrc/bvbrc-0006.jsonl.gz:6088`; ATB SAMEA3558800, ERZ9334384 at `data/catalog/allthebacteria.tsv.xz:569737`. Passing filters and available FASTA do not establish target identity.
- Campylobacter jejuni PNUSAC013518, GCA_010352675.1, SAMN13337901 at `data/catalog/ncbi_genbank-0009.jsonl.gz:6468`.

HEAD remained `b6a6508faca1388b88feb5740b1095e9f64cfdb8` on `codex/record-review-extensimonas-20261003`. Ignored-inclusive filename searches found no prior report for this stem. The complete YAML was reread byte-unchanged. This report was the only repository write for this target; temporary diagnostics and existing publisher-PDF renderings were used. No record, history, lifecycle, site, Git or GitHub state changed; Eukaryota was not reopened.

