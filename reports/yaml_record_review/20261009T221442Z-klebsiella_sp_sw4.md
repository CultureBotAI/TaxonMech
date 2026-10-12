# YAML Record Review: Klebsiella sp. SW4

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/klebsiella_sp_sw4.yaml`
- Started UTC: 2026-10-09T22:11:42Z
- Finished UTC: 2026-10-09T22:14:42Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read. `NCBITaxon:1037240` denotes NCBI's species-ranked placeholder Klebsiella sp. SW4, domain `BACTERIA`, parent `NCBITaxon:2608929`, genetic code 11, grounding `EXACT`, status `SEEDED`. Ten ancestors, one NCBITAXON attestation and the complete seed event were inspected. Zero represented BacDive strains measures source coverage, not biological absence. No synonyms, nomenclature, mappings, strains, definition, evidence or graph are asserted.

HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. YAML SHA-256: `c61f773b0585fd7454157c2ea61982c5d0661c8c63a00fbf2a980c3ac91881ed`. Ignored-inclusive filename resolution found one target and no prior report for this stem.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1`:

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/klebsiella_sp_sw4.yaml`: passed.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/klebsiella_sp_sw4.yaml --out /private/tmp/taxonmech-klebs-sw4-20261009-validation.tsv --workers 1`: one file, zero errors; output TSV read and header-only.
- `uv run --offline python scripts/validate_history.py history`: reused this turn's 17 valid records and zero invalid links after a fresh empty diff for history, schema and validator.
- Complete own-row, lineage, attestation, scope and slug comparisons passed; these bounded checks do not certify corpus reproduction.
- Public NCBI structured reads succeeded. The taxonomy browser failed; complete API responses were inspected instead. PubMed and targeted publisher full-text passages were read. The supplementary-document browser link failed and PMC displayed a browser challenge; no supplement or experimental reanalysis was completed.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, raw-provenance hash replay, rendering and publication-size gates. `just validate-products` has no applicable graph nodes.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:222706`, native name `data/catalog/ncbi_names-0005.jsonl.gz:32305`, slug `data/taxa/PATHS.tsv:15242` and scope `curation/seed_scope.tsv:322939` agree. The full backbone row supports identity, rank, parent, code, empty synonyms and the 2026-09-13 snapshot.

All ancestor IDs, labels and ranks match the pinned chain: root; cellular organisms; Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria; Enterobacterales; Enterobacteriaceae; Klebsiella; unclassified Klebsiella. [NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037240&retmode=xml) confirms target, parent, code and named ancestors; [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037240) confirms all ancestor IDs including root. Neither returned an alias or successor.

Complete type-material, merged-ID and dropped tables have no own exact-ID row; the complete backbone has no child of this node. `EXACT` grounds the NCBI node, not formal species nomenclature or equivalence of physical cultures sharing SW4.

## Evidence

The sole NCBITAXON attestation correctly counts one `NAME`. Complete own-ID inventory scans found no BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row. Source set, snapshot and full scope sentence agree; no descendant supplies BacDive coverage. This turn's inspected `src/taxonmech/seed.py:_seed_timestamp` and raw/ATB/StrainInfo manifests support the latest extraction timestamp `2026-09-13T17:54:04Z`; a fresh diff confirmed these inputs unchanged. The event records generation, not human review.

The exact non-expanded [nucleotide query](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=nuccore&term=txid1037240%5BOrganism%3Anoexp%5D&retmode=json&retmax=100) returned two records; complete annotations and bibliography were inspected:

- [JF815403.1](https://www.ncbi.nlm.nih.gov/nuccore/JF815403.1), GI 334725016: 1,489-nt partial 16S rRNA gene, strain SW4, organism Klebsiella sp. SW4, `taxon:1037240`. The submission describes Gracilaria-associated material collected in India on 2008-07-15, submitted in 2011. It contains only a direct-submission reference. Sequence SHA-256: `a950a8db0f1df803857d5bb83678adccf61e51734284e18777e75c1b1d147824`.
- [AB924601.1](https://www.ncbi.nlm.nih.gov/nuccore/AB924601.1), GI 943491755: 27,316-nt capsule-synthesis region, strain SW4, serotype K65, same organism and taxon cross-reference, submitted in 2014 and published in 2015. The annotations include 21 CDSs, not a complete genome. Sequence SHA-256: `0ad84c9bb5732d31d6ed40b677e9c09a6a07c7d39c412babcc1b6b748e46137f`.

Both lengths match the actual lowercase `acgt` sequences. CDS translations were checked by length and hash, not functionally validated. No phenotype, gene function, capsule chemistry or equivalence between these submissions is asserted by this review.

The capsule reference resolves to [PubMed 26493302](https://pubmed.ncbi.nlm.nih.gov/26493302/), Pan et al. (2015), `DOI:10.1038/srep15573`, `PMC4616057`. The [primary paper](https://www.nature.com/articles/srep15573) describes a comparative capsule-locus study and states that its 77 reference strains were purchased from Statens Serum Institute. The inspected K65 discussion distinguishes gene-content observations from unavailable capsule-structure knowledge. These passages do not establish that the Indian algal isolate and K65 reference material are the same physical culture. Preserve this unresolved provenance boundary before enrichment; shared SW4 and taxon metadata alone are insufficient.

The [genome endpoint](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1037240/dataset_report?page_size=100) returned `{}`: no positive assembly evidence in that response, not global absence. Neither a partial marker nor a capsule locus establishes a culture deposit or whole-genome relationship.

## Completeness

`rg --no-ignore --hidden -n -z -i` searched numeric ID, scientific name and slug across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, including ignored, hidden and compressed contents. All twenty matching rows were read completely: three own rows and seventeen unrelated matches.

Native false matches: `data/catalog/ncbi_genbank-0009.jsonl.gz:7429` is Salmonella Saintpaul taxon 90105, strain 2013K-1790, assembly `GCA_010372405.1`, sample `SAMN02947391`. `data/catalog/gtdb_genomes-0016.jsonl.gz:43650` and `data/catalog/ncbi_genbank-0062.jsonl.gz:44872` concern Holophagaceae bacterium taxon 2052165, isolate MsH-30apr19-148, assembly `GCA_963970135.1`, sample `SAMEA115347382`; GTDB calls it Acidiparvus lacustris. `data/catalog/gtdb_genomes-0009.jsonl.gz:43909` and `data/catalog/ncbi_genbank-0026.jsonl.gz:5876` concern Aquiluna sp. taxon 2053504, isolate AM-384-N17, assembly `GCA_028095925.1`, sample `SAMN29376216`. The latter four matches are genome lengths equal to 1037240, not taxon links.

Ten `data/catalog/allthebacteria.tsv.xz` rows describe Campylobacter coli, runs ERR10372400-09. Read row/run/assembly triples: 170827 / ERR10372401 / ERZ25134929; 170832 / ERR10372408 / ERZ25134976; 170849 / ERR10372402 / ERZ25135147; 170893 / ERR10372404 / ERZ25135592; 170895 / ERR10372407 / ERZ25135611; 170905 / ERR10372409 / ERZ25135693; 170909 / ERR10372403 / ERZ25135728; 170965 / ERR10372400 / ERZ25136207; 170997 / ERR10372406 / ERZ25136470; 171011 / ERR10372405 / ERZ25136599. Row 170827 has unknown current/previous Sylph labels and failed Sylph/HQ flags; row 170893 fails CheckM2 contamination. Other eight have passing flags; nine rows have Campylobacter_D coli current/previous classifications. Row 1777094 is Shigella sonnei with Sylph Escherichia coli, assembly `ERZ25715957`, sample `SAMN14055951`, run `SRR11037240`. Row 2262772 is Salmonella enterica, assembly `ERZ26105254`, sample `SAMN26507247`, run `SRR18256796`; the hit is inside its SeqKit checksum. The latter two have passing flags. None links SW4.

Five `SOURCE.json` files were separately parsed. The only match, `data/straininfo/SOURCE.json` response index 663, is inside SHA-256 `d1f10372401024bddd5f587777c4c28a73d8db0d567bd2b09ec1f789720124d8`. Its complete metadata object describes `responses/records-0657.json.gz`, requested SI records 78772-78871, not a Klebsiella taxon relationship. No own history entry appeared in searched contents or filenames.

Accession/PMID/DOI search returned only `data/catalog/allthebacteria.tsv.xz:2597110`, fully read: Salmonella enterica assembly `ERZ26493302`, sample `SAMN34999263`, run `SRR24466572`, passing flags. Its analysis accession happens to contain the PubMed digits; it is not a citation or SW4 relationship.

No missing required representation, supported synonym, LPSN/GTDB mapping, successor or eligible whole-deposit/genome chain was established. Optional evidence, definitions and graphs may remain absent. iModulonDB is inapplicable to this YAML, which asserts no gene, regulator, pathway, functional trait or transcriptomic dataset; external sequence annotations were not promoted into such claims. Absence conclusions are bounded to inspected roots, snapshots and responses.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the YAML. Identity, Enterobacteriaceae lineage, provenance, lifecycle and represented coverage agree. The unresolved identity relationship between the two external submissions limits enrichment, not the existing NCBI-node representation.

## Recommended Edits

None required. Preserve NCBI identity and `SEEDED` status. Before adding origin, serotype, strain or genome claims, resolve the submission provenance using source-specific deposit or sample evidence; do not combine the two culture histories merely through SW4 or this taxon ID. Future supported enrichment belongs in maintained source transforms or `src/taxonmech/seed.py`, with tests and regeneration. Taxonomy corrections belong upstream, not in hand-edited generated YAML or an assumed overlay.

## Follow-up Checks

No corrective validation is required by a finding. A future identity investigation should inspect the capsule study's strain table and explicit submitter/deposit chains, preserving conflicting origins until resolved. Before regenerated publication run `just verify-corpus` and `just qc`; use eligible whole culture accessions and explicit source chains for genome links.

## Additional Notes

Only `NCBITaxon:1037240` is judged. Eukaryota was not reopened; neighboring verdicts were not transferred. No YAML, source, scope, history, status, branch, worktree or GitHub item changed. This new report is the only repository write for the target. No paid research was used.
