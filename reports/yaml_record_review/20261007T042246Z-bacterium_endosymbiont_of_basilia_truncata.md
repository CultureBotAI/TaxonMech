# YAML Record Review: bacterium endosymbiont of Basilia truncata

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacterium_endosymbiont_of_basilia_truncata.yaml`
- Started UTC: 2026-10-07T04:18:58Z
- Finished UTC: 2026-10-07T04:22:46Z
- Verdict: pass

## Target

Read the entire generated TaxonRecord for `NCBITaxon:1035577`, `bacterium endosymbiont of Basilia truncata`: FORMA_SPECIALIS in BACTERIA, parent `NCBITaxon:1485666`, code 11, EXACT grounding, SEEDED status, strain_count 0, one NCBITAXON NAME attestation and one seed event. No synonyms, nomenclature, mappings, strains, genomes, literature, discussions or causal graphs are asserted.

This is the Basilia-associated bacterial node beneath Candidatus Aschnera chinzeii, not the host fly, host bat, parent species or another host-associated symbiont. Generated YAML is read-only; maintained inventories, `curation/seed_scope.tsv` and `src/taxonmech/seed.py` own future fixes.

## Validation

Environment prefix: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline`.

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/bacterium_endosymbiont_of_basilia_truncata.yaml`: exit 0, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/bacterium_endosymbiont_of_basilia_truncata.yaml --out /private/tmp/basilia-strict.tsv`: exit 0, one file, zero errors. Read the actual header-only TSV.
- Complete backbone, lineage, seven-inventory, path/scope, status and attestation comparisons passed. These are bounded source checks, not corpus reproduction.
- Live taxonomy XML/Datasets, browser, exact Assembly/nuccore searches, independent genome Datasets and all 21 nucleotide metadata records were inspected. Bases and translations were excluded; all other metadata were read losslessly.
- Not checked: full-corpus `just verify-corpus`, `just qc`, `just test`, `just validate-all`, provenance/hash, rendering, publication-size and docs-drift gates.
- No graph node requires `just validate-products`. Full history validation was not run; no external target history reference or lifecycle promotion applies.

## Identity and Grounding

Complete backbone row `data/raw/ncbitaxon_taxa.tsv:222105` matches ID, label, rank, parent, code and snapshot 2026-09-13. Synonym and retirement fields are empty. Native scientific-name row `data/catalog/ncbi_names-0005.jsonl.gz:31584` matches and has empty unique_name.

All ten ancestors match in order, ID, label and rank: root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Gammaproteobacteria 1236; Enterobacterales 91347; Enterobacteriaceae 543; Candidatus Aschnera 1485663; Candidatus Aschnera chinzeii 1485666.

Live [taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035577&retmode=xml) and [taxonomy Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035577) agree with FORMA_SPECIALIS, parent, lineage and identity. XML confirms code 11, creation 24 May 2011 and update 9 April 2014. No OtherNames or type-material assertion appears. Exact pinned type-material, merged-ID and dropped scans found no target row.

The inspected [NCBI browser](https://ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=1035577&lvl=3&mode=node) instead displays "no rank". This unresolved authority-surface discrepancy is preserved, not silently harmonized. The pinned inventory and both live machine-readable services support the YAML; the browser alone does not establish a generated-record defect. `src/taxonmech/seed.py:73` explicitly permits FORMA_SPECIALIS; an unranked node below this species would also be within scope.

## Evidence

`data/taxa/PATHS.tsv:14606` and `curation/seed_scope.tsv:322375` uniquely agree on identifier, stem and reason. The NCBITAXON attestation correctly counts one NAME.

The complete pinned backbone has no direct children. Exact BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventory scans found no target row. Strain_count 0 accurately describes inventory coverage, not an assertion that the named specimens or their markers do not exist.

All three source manifests were parsed in full: raw extracted_at 2026-09-13T17:50:44Z, ATB 17:54:04Z and StrainInfo 17:29:00Z. The newest-manifest rule at `src/taxonmech/seed.py:139` explains the seed timestamp. The event source list and scope reason match. Hashes were not recomputed.

Exact nuccore search returned 21 records. All metadata from the [GenBank retrieval](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=383212447,383212445,383212443,383212441,383212439,383212437,383212365,383212363,383212361,383212359,383212357,383212355,383212353,383212351,383212315,383212314,383212313,383212312,383212311,383212310,383212309) explicitly identify taxon:1035577 and host Basilia truncata. They cover eight isolate labels, BaTr1 through BaTr8, with unequal locus coverage:

| Locus | Exact accessions, all version .1 | Count | Length | Isolate labels |
|---|---|---|---|---|
| 16S rRNA, partial | AB632404 through AB632410 | 7 | 1472 bases each | BaTr1 through BaTr7 |
| gyrB, partial CDS | AB632446 through AB632453 | 8 | 964 bases each | BaTr1 through BaTr8 |
| groEL, partial CDS | AB632489 through AB632494 | 6 | 1601 bases each | BaTr1, BaTr3, BaTr4, BaTr5, BaTr6, BaTr7 |

BaTr1-3 are from Menashi-gun, BaTr4 from Shari-gun, BaTr5-6 from Shibetsu-gun, BaTr7 from Souya-gun and BaTr8 from Abashiri-gun, all Hokkaido, Japan. These are supplied geographic qualifiers, not inferred culture deposits. None supplies a culture_collection, BioSample, BioProject or assembly link. The CDS qualifiers retain code 11; annotations do not prove a physiological function.

The records were created/updated 3 April 2012 and cite a 19 May 2011 submission and an unpublished-title reference by Hosokawa and colleagues. That reference is not a formal PMID link. The inspected [related primary study](https://pmc.ncbi.nlm.nih.gov/articles/PMC3280136/), DOI:10.1038/ismej.2011.125, PMID:21938025, describes 16S/gyrB/groEL sampling of nycteribiid symbionts and proposes the parent candidate name. Its localization experiments and 0.76-Mb genome-size estimate concern other specified hosts, notably Penicillidia jenynsii, not a demonstrated Basilia result. Its supplementary specimen table was not successfully retrieved; the exact accession-to-publication table join remains unverified and is not invented from a similar title.

The inspected [2024 genome study](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2023.1336919/full) explicitly sequenced Aschnera from P. jenynsii. Neither that assembly nor its inferred vitamin provisioning establishes a Basilia-specific genome or phenotype.

The inspected [LPSN parent-species page](https://lpsn.dsmz.de/species/aschnera-chinzeii) names type NyAl1 and 16S accession AB632412. Those are not BaTr target records. Parent nomenclature and type identity must not be copied into this descendant as an equivalence.

Exact Assembly search returned zero with a phrase-not-found warning; independent [genome Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035577/dataset_report) returned an empty object. These are bounded checks, not global genome-absence proof. Twenty-one markers are not 21 genomes.

Before web search, all 28 fresh `kg-microbe-sources imodulondb datasets` rows were read through `uv run --offline --project ../../culturebotai-claw`. No organism matches; no module/gene is asserted by the YAML. Component queries are inapplicable, and noncoverage is not negative biological evidence.

## Completeness

No missing required representation was established. Definitions, record-level citations, nomenclature, mappings and graphs are optional for this seeded record. Marker/host context is useful optional enrichment; specimen labels alone do not justify BacDive strain entries.

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searched numeric-boundary 1035577, exact label, stem and Basilia truncata variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, including compressed contents. All five matches were fully read: three applicable identity/scope rows and two unrelated numeric collisions.

A second scan for all 21 accessions/version forms and boundary-delimited BaTr1-8 variants found zero rows in those roots. Both stages independently parsed all five SOURCE.json files and searched history filenames without ignore filtering, with no target metadata/history match. Ignored-inclusive corpus/report filename search resolved one target YAML and no prior target report. Absence findings are bounded to these roots.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the current record. The NCBI browser/API rank discrepancy and unverified supplementary table join are retained as follow-up limitations, not unsupported claims added to the YAML.

## Recommended Edits

None required. Preserve generated YAML and SEEDED lifecycle.

Optional marker/host enrichment belongs in maintained source/extractor inputs and inventories or tested `src/taxonmech/seed.py` behavior; scope fixes belong in `curation/seed_scope.tsv`. Do not import a parent type, another host's genome, or speculative metabolic mechanism. Resolve any taxonomy rank change upstream before refreshing pinned inputs.

## Follow-up Checks

For authorized enrichment, inspect the original supplementary specimen/accession table and preserve host/sample/locus specificity. Recheck NCBI browser, EFetch, Datasets and the pinned dump together before changing rank. Rerun target schema/strict checks and then documented corpus reproduction/provenance gates. No unresolved record blocker requires curation now.

## Additional Notes

The two local collisions, read with every native field/column, are:

- `data/catalog/ncbi_genbank-0049.jsonl.gz:23007`: Candidatus Woesearchaeota archaeon ATWRK4-1F_367, taxon 2026803, GCA_053530835.1, SAMN21437590. The match is genome_size/genome_size_ungapped 1035577, not target taxonomy.
- `data/catalog/allthebacteria.tsv.xz:66222`: Staphylococcus aureus, SAMEA1035577, ERR083851, ERZ3070738. Both assembly and HQ filters are META_FAIL despite an available FASTA; neither the sample-number match nor file availability supplies a target association.

The supplementary S1 URL returned an HTML preparation page, confirmed by `file`, rather than the linked Word table. Publisher alternatives failed. No table contents or specimen-to-paper join are claimed from that response. The primary article body and direct GenBank metadata remain independently inspected.

The long nucleotide output was reread in bounded chunks after an outer display truncation; the underlying retrieval was terminal and not restarted.

Only this new report was written for this target. No record YAML, inventory, generated page, earlier report, history or lifecycle state changed. Eukaryota remains untouched. No paid research, external contact or GitHub mutation occurred.
