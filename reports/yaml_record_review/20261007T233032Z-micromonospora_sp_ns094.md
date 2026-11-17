# YAML Record Review: Micromonospora sp. NS094

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/micromonospora_sp_ns094.yaml`
- Started UTC: 2026-10-07T23:20:36Z
- Finished UTC: 2026-10-07T23:30:32Z
- Verdict: pass

## Target

Generated `TaxonRecord` for `NCBITaxon:1036166`, Micromonospora sp. NS094, rank `SPECIES`, domain `BACTERIA`. The entire YAML was read. It carries ten ancestors, genetic code 11, exact grounding, seeded status, one NCBI name attestation and `strain_count: 0`. It asserts no synonyms, nomenclature, taxonomy mappings, strains, evidence objects, graph, discussion or dataset.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/micromonospora_sp_ns094.yaml`: exit 0, no issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/micromonospora_sp_ns094.yaml --out /private/tmp/mns094-strict.tsv`: exit 0, one file, zero errors. The diagnostic TSV was read and is header-only.
- Structured comparisons passed for backbone identity, all ten ancestors, attestation, unique path and scope reason. Exact pinned type-material, merged-ID and dropped-ID searches returned no target rows. The backbone has no target children.
- Not checked: full-corpus `verify-corpus`, `provenance-check`, `qc`, `validate-all`, tests, render/docs and vendored gates. Bounded source comparisons do not prove corpus reproduction. No graph is asserted and the ignored-inclusive bounded search found no standalone target history record, so specialized graph/history checks had no target.

## Identity and Grounding

Live Taxonomy EFetch agrees on ID, name, species rank, bacterial division, genetic code 11 and parent `NCBITaxon:2617518`, unclassified Micromonospora. Datasets confirms all ten ancestor IDs including root. Labels and ranks agree through cellular organisms, Bacteria, Bacillati, Actinomycetota, Actinomycetes, Micromonosporales, Micromonosporaceae and Micromonospora to the unclassified parent. [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1036166), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036166).

Exact grounding identifies the NCBI node; species rank does not establish a formally named species or a culture deposit. NS094 is a source strain designation. Salmonella sp. NS094_S89_L001, taxon 3098579, and Enterococcus faecium HC_NS0940, taxon 1352, are different organisms, not additional evidence for this taxon.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:222292` matches every seeded identity field, empty synonyms, sole source and the 2026-09-13 snapshot. The complete native scientific-name object is `data/catalog/ncbi_names-0005.jsonl.gz:31810`.
- `data/taxa/PATHS.tsv:14796` uniquely maps the ID and slug; `curation/seed_scope.tsv:322546` agrees on date and the one-source inclusion reason.
- Exact-taxonomy Nucleotide search returned [JF826530.1](https://www.ncbi.nlm.nih.gov/nuccore/JF826530.1), a 1,314-base partial 16S rRNA sequence explicitly identifying NS094 and taxon 1036166. Complete non-sequence metadata describe petroleum sludge from former fuel-storage tank N8 at Oil Refinery Novi Sad, Serbia. Submission was 14 April 2011 at IChTM, Belgrade; creation was 6 June 2011 and update 23 February 2012. No culture deposit, BioSample, BioProject, assembly or protein accession occurs in those metadata. The marker is not a genome.
- GenBank explicitly cites PMID 21604191 and DOI `10.1007/s10532-011-9481-1`. The previously fetched primary PubMed citation and full abstract were reread, and the publisher preview inspected again. Accessible results concern samples and a bacterial consortium, not NS094-only degradation rates. Full identification and strain-test tables remained behind the subscription preview. The publisher-linked supplementary text explicitly labels Micromonospora sp. NS094 partial 16S sequence, supporting the paper-to-strain association without establishing a deposit or formal species. [Primary study](https://link.springer.com/article/10.1007/s10532-011-9481-1), [PubMed](https://pubmed.ncbi.nlm.nih.gov/21604191/), [Publisher supplement](https://media.springernature.com/original/springer-static/esm/art%3A10.1007%2Fs10532-011-9481-1/MediaObjects/10532_2011_9481_MOESM1_ESM.txt).
- Page 6 of the university-hosted 2014 poster was read as text and visually inspected. It explicitly links Micromonospora sp. NS094 to JF826530 and reports fatty-acid, carbon-source, metal-tolerance and API ZYM testing. Its Table 2 marks phenanthrene, sodium benzoate and diesel-fuel growth positive for NS094, while other NS094 cells use an unexplained slash. Broad prose claiming all strains used additional substrates is not unambiguously supported by those cells. Table 4 supports the named NS094 enzyme-test results, but those tests do not identify genes or establish a mechanism. Chromium prose uses Cr3+ while Methods/Table 1 name potassium dichromate; preserve this source discrepancy before curating chemical-specific tolerance. These are optional strain-scoped leads, not required TaxonMech identity fields. [Primary 2014 poster](https://www.chem.bg.ac.rs/~p43004/ref/2014/2014_turska_mljesevic.pdf).
- The older Newenviro 2012 poster's page 6 was visually reread. Its Micromonospora column says NS096, not NS094, and gives no accession. The designation difference is unresolved; neither a typo nor strain equivalence is assumed, and its growth column is not assigned to NS094. [Primary 2012 poster](https://www.chem.bg.ac.rs/~p43004/ref/2012_newenviro_vbeskoski1.pdf).
- Exact-taxonomy Assembly search returned zero with phrase-not-found/no-items warnings. This bounded result does not establish genome absence under all identifiers.
- The sole attestation counts one NCBI `NAME`, not a culture or genome. Seed event and scope reason agree. Timestamp `2026-09-13T17:54:04Z` equals the latest extracted-at value in the raw, ATB and StrainInfo manifests, consistent with `src/taxonmech/seed.py:139`.

## Completeness

The exact BacDive comparison and lack of classified descendants support the inventory-specific zero strain count. It does not mean NS094 was never cultured. Exact LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits comparisons returned no target rows. Optional slots are appropriately empty for this seeded identity record. Phenotype, medium and isolation-context claims belong to the relevant sibling repositories under `docs/CURATION.md`.

Resolution searched ignored files in `data/taxa`, `reports`, `curation` and `history`. Source discovery used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, covering digit-bounded 1036166, NS094 label/slug variants and JF826530. All nine candidate addresses were retained without truncation, and all four JSON objects and five TSV rows were read completely. Five SOURCE.json files were separately parsed and history filenames independently checked.

Three candidates describe NS094; six concern the distinct Enterococcus and Salmonella organisms. No supported additional target culture/genome link, curation overlay or standalone history record was found in these bounded roots. No required representation was demonstrated missing. iModulonDB is not applicable: no gene, regulator, functional, transcriptomic or dataset claim is asserted.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found against the current YAML. Identity, lineage, source count and seeded provenance are supported. The source-level phenotype and designation caveats are retained explicitly; the YAML does not import those uncertain claims. Optional literature enrichment is not a missing required field.

## Recommended Edits

None required. Preserve the generated YAML and seed event. Any supported taxonomic correction belongs upstream at NCBI; any harmonization defect belongs in `src/taxonmech/seed.py` with a test. Future source extraction changes belong in maintained source/extractor inputs, including `scripts/extract_source_inventory.py`, rather than generated YAML. Durable curator overlays require the implementation described in `docs/CURATION.md` before they can survive regeneration. Phenotype, media and habitat enrichment belongs to the appropriate sibling repository and was not performed here.

## Follow-up Checks

Before optional enrichment, verify assay-specific methods, endpoint, strain/accession and source qualifications. Resolve the poster caveats rather than merging conflicting statements. Do not infer a culture deposit, genome link or species-level identification from a bare strain designation or partial 16S alone. No sequence alignment was performed; compare supplement and GenBank sequences if exact sequence identity becomes material. Regenerate future maintained-input changes through the documented pipeline and run focused schema/strict plus corpus/provenance gates.

## Additional Notes

- HEAD was `b6a6508faca1388b88feb5740b1095e9f64cfdb8`; the YAML was byte-identical before report creation. Existing branches and worktrees were preserved.
- Complete Enterococcus collision objects identify HC_NS0940, taxon 1352, GCA_013325605.1, SAMN14000087, PRJNA604849 and BV-BRC 1352.20813. They are not Micromonospora links.
- Salmonella NS094_S89_L001 has separate native-name, backbone and scope rows. Its ATB row identifies SAMN38415757, SRR26954139 and ERZ26663866; none supplies a genome for Micromonospora NS094.
- The web screenshot request for the 2014 poster timed out. The public PDF was downloaded to a temporary file and page 6 rendered with PDFKit for visual review. Other PDF pages were not used as evidence. The earlier poster rendering was reused only after visually rereading the relevant page. Search snippets and uninspected mirrors were discovery leads, not verdict evidence.
- The original article remained a subscription preview; no access restriction was bypassed. No culture-availability assessment, taxonomic reassignment or outreach was performed.
- Only this new report was written for this review. No YAML, source inventory, history/lifecycle or GitHub state changed. Eukaryota remained untouched.
