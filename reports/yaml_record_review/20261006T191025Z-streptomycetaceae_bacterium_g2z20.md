# YAML Record Review: Streptomycetaceae bacterium G2Z20

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomycetaceae_bacterium_g2z20.yaml`
- Started UTC: 2026-10-06T19:08:32Z
- Finished UTC: 2026-10-06T19:10:25Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` was read: `NCBITaxon:1035269`, Streptomycetaceae bacterium G2Z20, species-rank Bacteria placeholder under `NCBITaxon:234292` (unclassified Streptomycetaceae). It has nine root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` lifecycle, zero BacDive strains, one name attestation and one seed event. No synonyms, nomenclature, mappings, deposits, genomes, traits or causal edges are asserted.

This is a species-rank placeholder classified only to family, not a family-rank corpus record. It therefore does not violate the species-and-below scope rule. Maintained scope, acquisition/extraction and `src/taxonmech/seed.py` own future corrections; generated YAML is read-only.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/streptomycetaceae_bacterium_g2z20.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/streptomycetaceae_bacterium_g2z20.yaml --out /private/tmp/gz20-strict.tsv`: exit 0, one record, zero errors. Actual TSV read: header only.
- Bounded manual comparisons matched complete pinned identity, lineage, path lock, scope, attestation and seed history. They are not a focused reproduction gate.
- Not run: full `just verify-corpus`, `just qc`, tests, rendering, provenance and corpus-wide history gates. The reproduction script has no target selector; `--max-diffs` limits output only.
- Not applicable: `just validate-products` for added graph nodes; none are stored. NCBITaxon references were checked at pinned and live authorities.
- Inline history passed target validation and matched scope. Ignored-inclusive content and history-filename checks found no target-specific external history entry.
- The local `kg-microbe-sources imodulondb datasets` adapter ran before web follow-up. All 28 rows were inspected. Named Streptomyces datasets do not identify G2Z20, so no target query was applicable. Absence is not negative evidence.

## Identity and Grounding

The full backbone `data/raw/ncbitaxon_taxa.tsv:221978`, scientific-name row `data/catalog/ncbi_names-0005.jsonl.gz:31446`, path lock `data/taxa/PATHS.tsv:14469` and scope `curation/seed_scope.tsv:322253` agree with the stored identity.

Live [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035269&retmode=xml) and [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035269) confirm the active species-rank placeholder, parent, genetic code and lineage. The root-first chain is root, cellular organisms, Bacteria, Bacillati, Actinomycetota, Actinomycetes, Kitasatosporales, Streptomycetaceae and unclassified Streptomycetaceae. All stored IDs, labels and ranks match the pinned source. No genus is supplied, and none should be inserted. Exact checks found no type-material, merged-ID or dropped row and no immediate child.

The complete inspected [LPSN Streptomycetaceae page](https://lpsn.dsmz.de/family/streptomycetaceae), record 1348, concerns a validly published correct family name with Streptomyces as type genus. Whole-page G2Z20 search found no match. The family's type genus does not identify every family member or provide this isolate's nomenclature, synonyms or deposits.

## Evidence

The single `NCBITAXON` `NAME` attestation has the exact ID/label and snapshot date 2026-09-13. Its count is not a biological strain or genome count. The `seed_from_sources` `SEEDED_FROM_SOURCES` event at `2026-09-13T17:54:04Z` matches the one-source scope explanation.

Full metadata for [JF729482.1](https://www.ncbi.nlm.nih.gov/nuccore/JF729482.1), UID 334086858, identify a 1,397-nt partial 16S rRNA marker, strain G2Z20, exact taxon 1035269 and seagrass isolation source. The sequence also uses the Streptomycetaceae bacterium label. W. Chen submitted it on 25 March 2011; creation and update dates are 31 May and 3 June 2011. The unpublished-study and direct-submission references carry no PMID or DOI. Metadata supply no culture deposit, BioSample, BioProject, assembly, host species or collection-country qualifier. Institutional address is not collection locality; genomic DNA is not an assembly. Sequence bases were not analyzed.

[Wu et al., DOI:10.5897/AJMR11.981](https://academicjournals.org/journal/AJMR/article-full-text-pdf/2A88A4617354), page 88, explicitly links G2Z20/JF729482. Figure 2 places G2Z20 within its Streptomyces grouping. Table 2 compares it with S. varsoviensis at 97.70%, with PKS-I negative, PKS-II positive and NRPS positive. The discussion calls it a possible novel species. The relevant text, figure and table were inspected.

The publication's genus-level treatment differs from NCBI's unresolved genus. This difference is retained here, not silently reconciled. Under TaxonMech's carried-lineage policy the stored NCBI placement is correct. Neither the publication's grouping nor marker similarity establishes formal synonymy, deposit identity, a whole genome, complete biosynthetic clusters or antimicrobial activity.

Exact designation and accession web searches supplied no additional inspected deposit or genome bridge. Unrelated short-code matches were not evidence.

## Completeness

Searches used `rg --no-ignore --hidden -n -z -i`, including ignored, hidden and compressed files, across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Identifier, label, slug, candidate Streptomyces label and designation pattern `\bG2Z[- _]?20\b` yielded ten rows: three target rows and seven false numeric matches, all read in full native metadata or TSV form. Five source-level `SOURCE.json` files and history filenames were checked separately.

A second JF729482 search across those roots, plus metadata/history filenames, found no match. These are bounded local snapshot results, not worldwide absence claims.

Exact comparisons found no target row in `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`. No pinned descendants contribute BacDive entries. Zero strains agrees with the own-plus-descendant seeder rule without denying the isolate.

Live non-expanding NCBI searches returned zero Assembly records and one nucleotide record. Assembly reported the taxid phrase not found, a bounded index result. The CAFI-backed normalizer returned no eligible culture key for G2Z20, G2Z-20 or G2Z 20. No deposit/genome chain was established.

No consequential required omission was found. Empty optional slots are appropriate. A missing genus is not a local omission when NCBI supplies none; source-specific literature context would be optional enrichment.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the assertions stored. The classification difference above is a source-scope caveat, not a generated-record defect. This pass does not certify full-corpus reproducibility.

## Recommended Edits

None required. Preserve the family-classified species placeholder, nine-entry lineage, one-name attestation, zero BacDive count and seeded lifecycle. Do not insert Streptomyces or rename the target S. varsoviensis from the publication.

Any authorized classification reconciliation belongs upstream; this repository carries NCBI lineage rather than inferring it. Other source enrichment belongs in maintained acquisition/extraction and `src/taxonmech/seed.py`, with supported inputs and tests. Do not hand-edit generated YAML.

## Follow-up Checks

If future evidence changes classification, verify the authority's exact taxon and parent before refreshing the pinned source. Literature claims need the explicit isolate/accession relation and assay scope. Genome associations require a whole eligible deposit plus an explicit source-specific sequence chain; keep taxon, strain, deposit, marker, sample, project and assembly identities distinct.

After an authorized input change, regenerate through the validated writer and rerun target schema/strict checks and full `just verify-corpus` and `just qc`. No regeneration, contact, history write or lifecycle promotion occurred.

## Additional Notes

The seven false numeric matches were:

- Four Parabacteroides merdae assertions, taxid 46503, RTP21230st1_B11_RTP21230_210325, SAMN41035269, GCA/GCF_040924445.1, BV-BRC 46503.3053: `data/bvbrc/bvbrc-0020.jsonl.gz:25656`, `data/catalog/ncbi_genbank-0037.jsonl.gz:20826`, `data/catalog/ncbi_refseq-0006.jsonl.gz:19972`, `data/catalog/gtdb_genomes-0002.jsonl.gz:48683`.
- Two Mycobacterium tuberculosis assertions for ERR1035269: BV-BRC 1773.18294 at `data/bvbrc/bvbrc-0006.jsonl.gz:6085`; ATB SAMEA3558802, ERZ9334385 at `data/catalog/allthebacteria.tsv.xz:569739`. Available FASTA and passing filters do not establish target identity.
- Salmonella enterica 1035269001, GCA_020044905.1, SAMN21475428 at `data/catalog/ncbi_genbank-0018.jsonl.gz:21516`.

HEAD was `b6a6508faca1388b88feb5740b1095e9f64cfdb8` on `codex/record-review-extensimonas-20261003`. Ignored-inclusive filename checks found no prior report for this stem. The full YAML was reread byte-unchanged. Only this new report was written for this target. No record, history, lifecycle, site, Git or GitHub state changed, and Eukaryota remained untouched.

