# YAML Record Review: Saccharomonospora sp. M8Z39

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/saccharomonospora_sp_m8z39.yaml`
- Started UTC: 2026-10-06T18:47:23Z
- Finished UTC: 2026-10-06T18:52:08Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` for `NCBITaxon:1035264`, Saccharomonospora sp. M8Z39, was read before judgement. It is a species-rank Bacteria placeholder, parent `NCBITaxon:2634184`, genetic code 11, with ten root-first ancestors, `EXACT` grounding, `SEEDED` lifecycle, zero BacDive strains, one NCBITAXON name attestation and one seed event. It contains no synonym, nomenclature, mapping, deposit, genome, trait or causal-graph assertions.

Future corrections belong in maintained scope, source acquisition/extraction or `src/taxonmech/seed.py`, not in this generated YAML.

## Validation

The offline project runner used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/saccharomonospora_sp_m8z39.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/saccharomonospora_sp_m8z39.yaml --out /private/tmp/sm39-strict.tsv`: exit 0, one record and zero errors. The actual diagnostic TSV was read and was header-only.
- Bounded manual comparisons verified the complete pinned backbone, lineage, path lock, scope, source attestation and seed explanation. This is not a focused reproduction validator.
- Not run: full `just verify-corpus`, `just qc`, tests, rendering, provenance and corpus-wide history gates. The reproduction script has no target selector; `--max-diffs` only limits diagnostic output. No full-corpus success is claimed.
- Not applicable: `just validate-products` for curator-added graph nodes, since none are present. NCBITaxon references were compared with pinned and live authorities.
- Inline history passed schema/strict checks and matched scope. Ignored-inclusive content and history-filename checks found no target-specific external history entry.
- The local `culturebotai-claw` runner executed `kg-microbe-sources imodulondb datasets` before web follow-up. All 28 rows were inspected; none covers Saccharomonospora. No further transcriptomic query was applicable, and absence is not negative biological evidence.

## Identity and Grounding

The full pinned backbone at `data/raw/ncbitaxon_taxa.tsv:221973` and scientific-name row at `data/catalog/ncbi_names-0005.jsonl.gz:31441` agree with the record. Its unique path lock is `data/taxa/PATHS.tsv:14464`; `curation/seed_scope.tsv:322248` supplies the one-source inclusion reason.

Live [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035264&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035264) confirm the identifier, active species-rank label, parent and lineage. The stored chain is root, cellular organisms, Bacteria, Bacillati, Actinomycetota, Actinomycetes, Pseudonocardiales, Pseudonocardiaceae, Saccharomonospora and unclassified Saccharomonospora. Every ancestor ID, label and rank matches the pinned source; live Datasets also includes root. Exact pinned checks found no type-material, merged-ID or dropped row, and no immediate child.

The complete inspected [LPSN Saccharomonospora genus page](https://lpsn.dsmz.de/genus/saccharomonospora), record 516525, concerns a validly published genus with S. viridis as type species. A whole-page M8Z39 search found no match. The genus page supplies no formal target species name, type deposit or synonym; its risk annotation and neighboring species' deposits must not be inherited.

## Evidence

The sole attestation is one `NCBITAXON` `NAME` assertion with exact ID and label, snapshot 2026-09-13. This count is not a strain or genome count. The `seed_from_sources` `SEEDED_FROM_SOURCES` event at `2026-09-13T17:54:04Z` matches scope. This review does not promote the lifecycle.

Full metadata for [JF729481.1](https://www.ncbi.nlm.nih.gov/nuccore/JF729481.1), UID 334086857, describe a 1,399-nt partial 16S rRNA sequence with strain M8Z39, taxon 1035264 and seagrass isolation source. W. Chen submitted it on 25 March 2011; creation and update dates are 31 May and 3 June 2011. References comprise an unpublished comparative seagrass study and direct submission, without PMID or DOI. There is no culture deposit, BioSample, BioProject, assembly, source-country qualifier or host species in this metadata. Institutional address is not collection-locality evidence. Genomic-DNA provenance does not turn the marker into a whole-genome assembly; sequence bases were not analyzed.

[Wu et al., DOI:10.5897/AJMR11.981](https://academicjournals.org/journal/AJMR/article-full-text-pdf/2A88A4617354), printed page 88, explicitly links M8Z39/JF729481 and describes Thalassia hemprichii sampling at Nancun Port, China, in October 2010. Visually inspected Figure 1 separates M8Z39 from S. xinjiangensis AJ306300. Table 2 reports 98.49% similarity to S. xinjiangensis and positive PKS-I, PKS-II and NRPS PCR screens. These observations do not establish species equivalence, a complete biosynthetic cluster or demonstrated antimicrobial activity.

A [primary author's university abstract for the 2013 antibacterial study](https://bu.edu.eg/staff/hassanemara7-publications/29004) describes a different Saccharomonospora isolate from a Saudi mangrove rhizosphere. Its sequence is compared with M8Z39 at 98% similarity. M8Z39 is the comparator, not the tested isolate. The page provides neither a full paper nor a tested-isolate accession; its antibacterial results and isolation locality cannot be assigned to this record.

## Completeness

The searches used `rg --no-ignore --hidden -n -z -i`, including ignored, hidden and compressed files. Identifier, exact label, slug and bounded designation pattern `\bM8Z[- _]?39\b` were searched across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All ten matching rows were read in full native metadata or TSV form: three target rows and seven numeric false matches. Five source-level `SOURCE.json` files and ignored-inclusive history filenames were checked separately.

A second compressed search for JF729481 across the same ten roots, plus separate metadata and history-filename checks, returned no match. These are bounded snapshot checks, not worldwide absence claims or a census of every ignored directory.

Exact checks of `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` and `bactotraits_taxa.tsv` found no target rows. There are no pinned descendants to contribute BacDive entries. Zero strains agrees with the seeder's own-plus-descendant rule; it does not deny the laboratory isolate.

Exact, non-expanding live NCBI searches returned zero Assembly records and one nucleotide record. Assembly also reported the taxid phrase as not found; this is bounded index evidence. The existing CAFI-backed normalizer yielded no eligible culture key for M8Z39, M8Z-39 or M8Z 39. Bare designations and marker similarity do not establish a deposit/genome chain.

No consequential required omission was established. Optional literature enrichment is not mandatory for this source-attested seed. Empty nomenclature, phenotype, deposit and genome slots are appropriate until claim-specific evidence supports them.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the stored assertions. This is a bounded record-level pass, not a full-corpus reproducibility certificate.

## Recommended Edits

None required. Preserve the exact NCBI placeholder, one-name attestation, zero BacDive count and seeded lifecycle. Do not rename M8Z39 to its nearest published comparator or transfer another study isolate's antibacterial phenotype.

Future authorized source enrichment belongs in maintained acquisition/extraction and `src/taxonmech/seed.py`. Any literature overlay needs supported maintained inputs and tests. Do not hand-edit generated YAML.

## Follow-up Checks

For proposed enrichment, retain the exact M8Z39/JF729481 relationship and PCR-screen scope. A claimed antibacterial phenotype would need inspected evidence explicitly naming the tested M8Z39 isolate, which the 2013 abstract does not provide. Require a whole eligible culture accession and explicit source-specific deposit/sequence relationship before genome association.

After an authorized upstream change, regenerate through the validated writer, rerun target schema/strict checks and full `just verify-corpus` and `just qc`. No regeneration or lifecycle promotion occurred here.

## Additional Notes

The seven numeric false matches are distinct source assertions:

- Four Parabacteroides distasonis assertions, taxid 823, strain RTP21277st1_C1_RTP21277_210401, SAMN41035264, GCA/GCF_040924545.1 and BV-BRC 823.5230: `data/catalog/ncbi_genbank-0037.jsonl.gz:20831`, `data/bvbrc/bvbrc-0027.jsonl.gz:26399`, `data/catalog/ncbi_refseq-0006.jsonl.gz:19977`, `data/catalog/gtdb_genomes-0011.jsonl.gz:35007`.
- Two Mycobacterium tuberculosis assertions for ERR1035264: BV-BRC 1773.18289 at `data/bvbrc/bvbrc-0006.jsonl.gz:6079`; ATB SAMEA3558797, ERZ9334372 at `data/catalog/allthebacteria.tsv.xz:569734`. Its FASTA availability and passing filters do not establish target identity.
- Campylobacter jejuni, taxid 197, PNUSAC014944, GCA_010352645.1 and SAMN13825590 at `data/catalog/ncbi_genbank-0009.jsonl.gz:6466`.

HEAD remained `b6a6508faca1388b88feb5740b1095e9f64cfdb8` on `codex/record-review-extensimonas-20261003`. Ignored-inclusive prior-report filename searches found no report for this stem. The complete YAML was reread byte-unchanged. The only repository write for this target was this new report; diagnostics and publisher-PDF renderings used temporary storage. No record, history, lifecycle, site, Git or GitHub state changed, and no Eukaryota record was reopened.
