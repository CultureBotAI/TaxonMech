# YAML Record Review: Achromobacter sp. NS014

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/achromobacter_sp_ns014.yaml`
- Started UTC: 2026-10-07T22:55:44Z
- Finished UTC: 2026-10-07T23:00:04Z
- Verdict: pass

## Target

Generated `TaxonRecord` for `NCBITaxon:1036163`, Achromobacter sp. NS014, rank `SPECIES`, domain `BACTERIA`. The entire YAML was read independently. It has ten ancestors, genetic code 11, exact grounding, seeded status, one NCBI name attestation and `strain_count: 0`. It asserts no synonyms, nomenclature, mappings, strains, evidence objects, graph, discussion or dataset.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/achromobacter_sp_ns014.yaml`: exit 0, no issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/achromobacter_sp_ns014.yaml --out /private/tmp/ans014-strict.tsv`: exit 0, one file, zero errors. The diagnostic TSV was read and contains only its header.
- Structured comparisons passed for backbone identity, all ten ancestors, attestation, unique path and scope reason. Exact pinned type-material, merged-ID and dropped-ID searches returned no target rows; the backbone has no target children.
- Not checked: full-corpus `verify-corpus`, `provenance-check`, `qc`, `validate-all`, tests, render/docs and vendored gates. Bounded comparisons do not reproduce the corpus. No graph is asserted and the bounded search found no standalone target history record, so specialized graph/history checks had no target.

## Identity and Grounding

Live Taxonomy EFetch agrees on ID, label, species rank, bacterial division, genetic code 11 and parent `NCBITaxon:2626865`, unclassified Achromobacter. Datasets confirms all ten ancestor IDs including root. Labels and ranks agree through cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Betaproteobacteria, Burkholderiales, Alcaligenaceae and Achromobacter to the unclassified parent. [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1036163), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036163).

NS014 is a source strain designation, not a demonstrated registered culture deposit. Exact grounding identifies this NCBI node; species rank does not establish a formally published species name. Salmonella sp. NS014_S9_L001 is a distinct NCBI node, 3098509, not an alias. Matches within LRKNS014, ANS014, T_NS-014 or other longer source names cannot establish strain identity.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:222289` matches all seeded identity fields, empty synonyms, sole source and 2026-09-13 snapshot. Its complete native scientific-name object is `data/catalog/ncbi_names-0005.jsonl.gz:31807`.
- `data/taxa/PATHS.tsv:14793` uniquely maps the ID and slug; `curation/seed_scope.tsv:322543` matches the date and one-source reason.
- Exact-taxonomy Nucleotide search returned [JF826529.1](https://www.ncbi.nlm.nih.gov/nuccore/JF826529.1), a 1,310-base partial 16S rRNA sequence explicitly identifying NS014 and taxon 1036163. Complete non-sequence metadata describe petroleum sludge from former fuel-storage tank N8 at Oil Refinery Novi Sad, Serbia. Submission was 14 April 2011 by the study authors at IChTM, Belgrade; creation was 6 June 2011 and update 23 February 2012. No culture deposit, BioSample, BioProject, assembly or protein accession appears in those metadata. The marker is not a genome.
- GenBank explicitly cites PMID 21604191 and DOI `10.1007/s10532-011-9481-1`. Primary PubMed citation/full abstract and the publisher preview confirm the 2012 Biodegradation paper by Gojgic-Cvijovic and colleagues. Its degradation outcomes concern samples treated with a bacterial consortium, not an NS014-only assay. The subscription preview did not expose the full identification and strain-test tables. The linked supplementary text explicitly labels an Achromobacter sp. NS014 partial 16S sequence, strengthening the paper-to-strain association without resolving a species or deposit identity. [Primary study](https://link.springer.com/article/10.1007/s10532-011-9481-1), [PubMed](https://pubmed.ncbi.nlm.nih.gov/21604191/), [Publisher supplement](https://media.springernature.com/original/springer-static/esm/art%3A10.1007%2Fs10532-011-9481-1/MediaObjects/10532_2011_9481_MOESM1_ESM.txt).
- A university-hosted Newenviro 2012 poster, page 6 of its PDF, was read visually after local rendering. Its table explicitly names Achromobacter sp. NS014 and marks positive growth for several tested substrates, including diesel fuel and n-hexadecane; the footnote defines the positive mark using growth at a specified dilution. This is a strain-specific enrichment lead, not proof of mineralization, a mechanism or a quantitative degradation rate. The poster lacks an accession in that table and has limited assay detail; linkage and conditions should be checked against the full study before curation. Consortium/soil degradation rates elsewhere on the poster are not assigned to this strain. [University-hosted poster](https://www.chem.bg.ac.rs/~p43004/ref/2012_newenviro_vbeskoski1.pdf).
- Exact-taxonomy Assembly search returned zero with phrase-not-found/no-items warnings; this does not establish genome absence under all identifiers.
- The attestation counts one NCBI `NAME`, not a culture or genome. Seed event, inventory and scope reason agree. Timestamp `2026-09-13T17:54:04Z` matches the latest extracted-at value among the raw, ATB and StrainInfo manifests, selected by `src/taxonmech/seed.py:139`.

## Completeness

The exact BacDive comparison and lack of classified descendants support the inventory-specific zero strain count. It does not assert that NS014 was never cultured, and is not contradicted by its cultivation in the literature. Exact LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits comparisons returned no target rows. Optional slots are appropriately empty for this seeded identity record.

Resolution searched ignored files in `data/taxa`, `reports`, `curation` and `history`, separating the target from Salmonella. The source search used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, covering digit-bounded 1036163, NS014 label/slug variants and JF826529. All 32 candidate addresses were retained without truncation and all 27 JSON objects and five TSV rows were read completely. Five SOURCE.json files were parsed separately and history filenames checked independently.

Three candidates describe this target; 29 are matches to distinct organisms or substrings crossing a name/number boundary. No supported additional target culture/genome link, curation overlay or standalone history record was found in these bounded roots. No required representation was demonstrated missing. iModulonDB is not applicable: no gene, regulator, functional, transcriptomic or dataset claim is asserted.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found against the current YAML. Identity, lineage, source count and seeded provenance are supported. The YAML contains no unsupported phenotype, culture or genome assertion. Available strain-specific literature offers optional enrichment, not a missing required field.

## Recommended Edits

None required. Preserve the generated YAML and seed event. Optional sequence, isolation-context or phenotype enrichment belongs in maintained source/extractor inputs or a durable curator representation following `docs/CURATION.md`. Identity and harmonization corrections belong upstream or in `src/taxonmech/seed.py`, not in the generated YAML. Do not join by bare strain designation, use other organisms' genomes or assign consortium performance to NS014.

## Follow-up Checks

Before adding growth or degradation claims, inspect the original study's full identification, methods and strain tables, confirm the exact NS014/JF826529.1 linkage and preserve substrate, medium, endpoint and condition scope. Compare the supplement sequence to GenBank if sequence identity is material; no alignment was performed here. Resolve any proposed deposit through its own primary evidence. Regenerate future maintained-input changes through the documented pipeline and run focused schema/strict plus corpus/provenance gates.

## Additional Notes

- HEAD was `b6a6508faca1388b88feb5740b1095e9f64cfdb8`; the target YAML was byte-identical before report creation. Existing branches and worktrees were preserved.
- Complete collision objects identify Staphylococcus epidermidis LRKNS014 (taxon 1282, GCA/GCF_001622575.1, SAMN04542849; GOLD Go0502193/Gp0386455/Ga0353200), Paraclostridium bifermentans ANS014 (taxon 1490, GCA/GCF_024345245.1, SAMD00505432; GTDB calls that separate genome P. dentum), Salmonella T_NS-014 (taxon 611, GCA/GCF_002926455.1), ADRDL-NS 014, Enterococcus faecalis HC_NS0147, an Anaerolineae metagenomic bin and Serratia marcescens names ending in numeric 014 prefixes. Historical RefSeq suppression statuses belong to these other organisms.
- The Salmonella NS014_S9_L001 ATB row identifies SAMN38415687, SRR26954217 and ERZ26663253. Neither its name nor its available assembly supports an Achromobacter link.
- A later PCB-consortium study was discovered at DOI `10.2298/JSC211217113Z`; direct publisher and DOI reads failed. Its search-result accession mention remains a lead, not inspected strain-level evidence. Similarly, an uninspected mirror snippet suggesting a preliminary A. denitrificans identification was not used to replace NCBI's label. Any such identification requires the original methods and table context.
- Web PDF screenshot failed; the public university poster was downloaded and page 6 rendered with PDFKit for visual inspection. The other five PDF pages were not used as evidence. The original journal article remained a subscription preview; no access restriction was bypassed.
- No culture-availability assessment, taxonomic reassignment or outreach was performed. Only this new report was written for this review; no YAML, source inventory, history/lifecycle or GitHub state changed. Eukaryota remained untouched.

