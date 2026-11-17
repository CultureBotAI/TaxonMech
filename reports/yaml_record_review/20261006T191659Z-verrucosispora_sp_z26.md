# YAML Record Review: Verrucosispora sp. Z26

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/verrucosispora_sp_z26.yaml`
- Started UTC: 2026-10-06T19:11:45Z
- Finished UTC: 2026-10-06T19:16:59Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` was read: `NCBITaxon:1035270`, Verrucosispora sp. Z26, species-rank Bacteria placeholder under `NCBITaxon:2617518` (unclassified Micromonospora). It has ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` lifecycle, zero BacDive strains, one name attestation and one seed event. No synonyms, nomenclature, mappings, deposits, genomes, traits or causal edges are asserted.

Maintained scope, acquisition/extraction and `src/taxonmech/seed.py` own future corrections. Generated YAML is read-only. The retained Verrucosispora label with Micromonospora ancestry is addressed below, not silently rewritten.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/verrucosispora_sp_z26.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/verrucosispora_sp_z26.yaml --out /private/tmp/vz26-strict.tsv`: exit 0, one record, zero errors. Actual TSV read: header only.
- Bounded manual comparisons matched complete pinned identity, lineage, path lock, scope, attestation and inline seed history. These are not a focused reproduction validator.
- Not run: full `just verify-corpus`, `just qc`, tests, rendering, provenance and corpus-wide history gates. The reproduction script has no target selector; `--max-diffs` limits output only.
- Not applicable: `just validate-products` for added graph nodes; none are stored. NCBITaxon references were checked against pinned and live authorities.
- Ignored-inclusive content and history-filename searches found no target-specific external history entry in the bounded roots below.
- The local `kg-microbe-sources imodulondb datasets` adapter ran before web follow-up. All 28 rows were inspected; none covered Verrucosispora or Micromonospora. No target query was applicable. This is not negative biological evidence.

## Identity and Grounding

The full backbone `data/raw/ncbitaxon_taxa.tsv:221979`, scientific-name row `data/catalog/ncbi_names-0005.jsonl.gz:31447`, path lock `data/taxa/PATHS.tsv:14470` and scope `curation/seed_scope.tsv:322254` agree with the stored identity.

Live [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035270&retmode=xml) and [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035270) confirm the active species-rank placeholder, exact label, parent, genetic code and lineage. All ten stored ancestor IDs, labels and ranks match the pinned source: root, cellular organisms, Bacteria, Bacillati, Actinomycetota, Actinomycetes, Micromonosporales, Micromonosporaceae, Micromonospora and unclassified Micromonospora. Exact source checks found no type-material, merged-ID or dropped row and no immediate child.

The complete [LPSN Verrucosispora page](https://lpsn.dsmz.de/genus/verrucosispora), record 516898, treats this validly published genus as a synonym, with Micromonospora as correct name and V. gifhornensis as type species. It also notes the alternative treatment as a separate genus. No Z26 entry was found on that page. This is genus-level context, not a formal name, synonym or deposit determination for this isolate.

The label/lineage difference mirrors NCBI, so it is not a local generation defect. TaxonMech carries the authority's lineage; it should not invent a Micromonospora species name or inherit a named species' type material.

## Evidence

The single `NCBITAXON` `NAME` attestation has the exact ID/label and snapshot date 2026-09-13. Its count is not a biological strain or genome count. The `seed_from_sources` `SEEDED_FROM_SOURCES` event at `2026-09-13T17:54:04Z` agrees with the one-source scope explanation.

Full metadata for [JF729479.1](https://www.ncbi.nlm.nih.gov/nuccore/JF729479.1), UID 334086855, identify a 1,384-nt partial 16S rRNA marker, strain Z26, exact taxon 1035270 and seagrass isolation source. W. Chen submitted it on 25 March 2011; creation and update dates are 31 May and 3 June 2011. Its unpublished-study and direct-submission references carry no DOI or PMID. No culture deposit, BioSample, BioProject, assembly, host species or collection-country qualifier is supplied. Institutional address is not collection locality; genomic DNA is not an assembly. Sequence bases were not analyzed.

[Wu et al., DOI:10.5897/AJMR11.981](https://academicjournals.org/journal/AJMR/article-full-text-pdf/2A88A4617354), page 88, explicitly associates M8Z26 with JF729479. Figure 1 separates it from V. sediminis EU870859. Table 2 reports 99.21% similarity, PKS-I negative, PKS-II positive and NRPS positive. Relevant text, figure and table were inspected.

The shared accession, not the short designation alone, supports this literature connection. Similarity and PCR results do not establish formal synonymy, type-strain identity, whole-genome availability, complete biosynthetic clusters or antimicrobial activity. None of those claims is inserted into the record.

A [PLaBA-db](https://plabase.cs.uni-tuebingen.de/pb/plaba_db.php) search lead was inspected in the fetched page source. Its Z26 option is `PAB_0000000930`, Streptomyces sp. Z26, while the Verrucosispora option is sp. ts21. Neither identifies this target. No analysis job was submitted. Exact designation/accession searches supplied no additional inspected deposit or genome bridge.

## Completeness

Searches used `rg --no-ignore --hidden -n -z -i`, including ignored, hidden and compressed files, across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Identifier, label, slug and designation patterns `\bZ[- _]?26\b` and `\bM8Z[- _]?26\b` yielded 54 rows: three exact target rows and 51 unrelated short-code or numeric matches. All 54 were read in full native metadata or TSV form. Five source-level `SOURCE.json` files and history filenames were checked separately.

A second JF729479 search across these roots, metadata and history filenames found no match. These are bounded local snapshot results, not worldwide absence claims.

Exact comparisons found no target row in `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`. There are no pinned descendants contributing BacDive entries. Zero strains agrees with the own-plus-descendant seeder rule without denying the isolate.

Live non-expanding NCBI searches returned zero Assembly records and one nucleotide record. Assembly reported the taxid phrase not found, a bounded index result. The CAFI-backed normalizer returned no eligible culture key for Z26, Z-26, Z 26, M8Z26, M8Z-26 or M8Z 26. No target deposit/genome chain was established.

No consequential required omission was found. Empty optional slots are appropriate; the literature connection is optional enrichment, not a reason to invent a deposit, genome, taxonomic synonym or reviewed lifecycle.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the assertions stored. The retained label/lineage difference and source-specific isolate designation are documented caveats, not local defects. This pass does not certify full-corpus reproducibility.

## Recommended Edits

None required. Preserve the exact NCBI label, Micromonospora lineage, one-name attestation, zero BacDive count and seeded lifecycle. Do not rename the target V. sediminis or join it to Streptomyces sp. Z26.

Any authorized classification reconciliation belongs upstream. Other evidence enrichment belongs in maintained acquisition/extraction and `src/taxonmech/seed.py`, with supported inputs and tests. Do not hand-edit generated YAML.

## Follow-up Checks

If a future source changes classification, verify the exact authority taxon and parent before refreshing pinned input. Literature claims need the explicit accession relationship and assay scope. Genome associations require a whole eligible deposit plus an explicit source-specific sequence chain. Keep taxon, strain, deposit, marker, sample, project and assembly identities distinct.

After an authorized input change, regenerate through the validated writer and rerun target schema/strict checks plus full `just verify-corpus` and `just qc`. No regeneration, contact, history write or lifecycle promotion occurred.

## Additional Notes

The 51 rejected rows include:

- Twenty-one backbone, scope and scientific-name rows for seven different short-code taxa: 202511, 448299, 1116758, 1144863, 1351393, 2500177 and 3722082.
- Eight further Streptomyces Z26 assertions: BV-BRC 1150371.3; GOLD Go0533233, Gp0480131 and Ga0437180; GCA/GCF_003665095.1 and its GTDB row; ATB SAMN10141549, ERZ9075744. Sources differ between Streptomyces phytohabitans and Streptomyces sp. Z26, but none supplies target 1035270 or JF729479. A bare Z26 is insufficient even when a complete project/assembly chain exists for a different organism.
- Four Parabacteroides merdae assertions linked by SAMN41035270 and GCA/GCF_040924425.1, and two Mycobacterium tuberculosis rows linked by ERR1035270, SAMEA3558803 and ERZ9334386. These are numeric collisions.
- Five Vibrio vulnificus assembly/BV-BRC rows, three Klebsiella pneumoniae assembly rows including a suppressed RefSeq record, two Streptococcus pyogenes assemblies, and two Bacillus sp. z26 assemblies. Shared Z26 fragments do not establish identity.
- Four remaining collisions: GOLD Gp0152574, Campylobacter jejuni GCA_010352705.1, a Gammaproteobacteria genome whose length is 1035270, and Salmonella SAMN61035270. None denotes the target.

HEAD was `b6a6508faca1388b88feb5740b1095e9f64cfdb8` on `codex/record-review-extensimonas-20261003`. Ignored-inclusive filename checks found no prior report for this stem. The complete YAML was reread byte-unchanged. Only this new report was written for this target. No record, history, lifecycle, site, Git or GitHub state changed, and Eukaryota remained untouched.

