# YAML Record Review: Curtobacterium sp. CtST3.3

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/curtobacterium_sp_ctst3_3.yaml`
- Started UTC: 2026-10-06T21:18:15Z
- Finished UTC: 2026-10-06T21:21:05Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` was read. `NCBITaxon:1035303` is Curtobacterium sp. CtST3.3, `SPECIES` in `BACTERIA`, parent `NCBITaxon:257496`. Ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` mapping status, zero inventoried strains, one NCBITAXON NAME attestation, and one seed event are asserted.

There are no synonym, nomenclature, taxonomy-mapping, strain-listing, genome, phenotype, citation, or causal-graph assertions. Generated fields remain read-only. Future corrections belong in maintained source transforms, inventory extraction, scope decisions, or `src/taxonmech/seed.py`, not this YAML or generated pages.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/curtobacterium_sp_ctst3_3.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/curtobacterium_sp_ctst3_3.yaml --out /private/tmp/cu33-strict.tsv`: exit 0, one file scanned, zero errors. The actual emitted TSV was read and is header-only.
- Structured comparisons inspected the full backbone row, every ancestor in order, direct children, seven non-NCBI inventories, PATHS, scope, attestation, and seed-event text. All compared fields agree.
- Exact checks of `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv`, and `data/raw/dropped.tsv` found no target entries.
- Ignored-inclusive searches, complete native candidate inspection, full SOURCE.json parsing, and history-filename checks completed.
- `uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets` ran with network access and exited 0. All 28 rows were inspected before external follow-ups. No Curtobacterium organism/dataset matches; iModulonDB is not applicable, not negative biological evidence.
- Live NCBI taxonomy XML, Datasets taxonomy JSON, exact-organism Assembly/nuccore searches, complete sequence metadata, and an independent Datasets genome query succeeded.
- Three unknown-labeled local ATB BioSamples were resolved by an accession-specific NCBI BioSample search and full XML fetch. All three matching records were read; they are not the target isolate.
- The exact-isolate Table II row in the primary paper was visually checked on printed page 886 using the existing PDFKit rendering. This is a bounded table inspection, not full-paper review.
- Not checked: full-corpus `just verify-corpus`, corpus-wide QC/history/provenance gates, full tests, page rendering, original-taxdump regeneration, or source-file hashes. Manual comparisons do not replace corpus-only gates.

## Identity and Grounding

The backbone `data/raw/ncbitaxon_taxa.tsv:222004`, scientific-name object `data/catalog/ncbi_names-0005.jsonl.gz:31480`, and live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035303&retmode=xml) agree on ID, exact label, species rank, parent, bacterial placement, and code 11. The [Datasets taxonomy response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035303) confirms every ancestor ID.

All ancestor IDs, labels, and normalized ranks agree: root; cellular organisms; Bacteria; Bacillati; Actinomycetota; Actinomycetes; Micrococcales; Microbacteriaceae; Curtobacterium; unclassified Curtobacterium. Family 85023, genus 2034, and parent 257496 agree. EFetch omits root from its displayed chain; Datasets includes ID 1.

Pinned synonym fields and live alternate-name content are empty; the pinned backbone has no direct children. NCBI's species rank does not establish a formal binomial or type strain. CtST3.3 is not ChST3.3 or the C. citreum isolate elsewhere in the paper.

## Evidence

- The NCBITAXON attestation correctly represents one NAME at snapshot 2026-09-13. `data/taxa/PATHS.tsv:14495` maps the identifier to this stem. `curation/seed_scope.tsv:322278` supplies the exact scope reason in the seed event.
- Raw, ATB, and StrainInfo extraction timestamps were read as 2026-09-13T17:50:44Z, 2026-09-13T17:54:04Z, and 2026-09-13T17:29:00Z. Their maximum equals the seed-event timestamp under the inspected seeder rule. This is source-seeding provenance, not human sign-off.
- Exact nuccore searching returned one record, UID 334899365, [JF935080.1](https://www.ncbi.nlm.nih.gov/nuccore/JF935080.1). Complete metadata excluding nucleotide bases describes a 1315 bp partial 16S rRNA sequence, strain CtST3.3, taxon cross-reference 1035303, female back, host Sturnira lilium, Venezuela, and collection date 13-Feb-2010. Direct submission was on 12-Apr-2011 by Gonzalez and Fermin at Universidad de Los Andes. A marker is not an assembly or culture-deposit accession.
- The cited [Interciencia paper, 39(12):882-889 (2014)](https://www.redalyc.org/pdf/339/33932786009.pdf), Table II on page 886, pairs JF935080 with CtST3.3, Curtobacterium sp., female S. lilium, and back, agreeing with GenBank. No DOI or PMID occurs in the inspected sequence reference metadata.
- Exact-organism Assembly searching returned count 0 with a no-items/phrase warning. The independent [Datasets genome query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035303/dataset_report) returned an empty object. These bounded results do not establish global genome absence.
- The full [BioSample XML for the three numeric candidates](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=biosample&id=10353039%2C10353038%2C10353037&retmode=xml) describes SAMN10353037/FC1591, SAMN10353038/FCLT, and SAMN10353039/FC1321 as human-associated samples from China, collected 2018-07-11, taxon 1869227 (bacterium), project PRJNA503135. Their source context differs from CtST3.3; none names this isolate or its taxon. The ATB unknown labels were not treated as sufficient proof of unrelatedness without this authority check.

## Completeness

The seeded identity is complete enough. Optional host, culture, or sequence details are not missing required fields. `strain_count: 0` counts inventoried BacDive-backed entries, not every biological isolate. A GenBank strain qualifier cannot supply a registered culture deposit.

The source search used `rg --no-ignore --hidden -n -z -i` with `1035303|CtST[-_ ]?3[._ -]?3\b|curtobacterium_sp_ctst3_3` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Ignored, hidden, and compressed data were included. Five source-native SOURCE.json files were parsed completely; history filenames were searched independently.

All nine candidate lines were inspected in full native form: one JSON object and eight TSV rows. Lossless structured displays retained every value and asserted reconstruction. Three are exact backbone, scientific-name, and scope records. Six ATB candidates do not supply target links:

| Candidates | Why excluded |
| --- | --- |
| One M. tuberculosis row | Run ERR1035303, SAMEA3558836, ERZ9334445. Matching run digits are not a taxon identifier. |
| Three unknown-labeled rows | SAMN10353037, SAMN10353038, SAMN10353039 are NOT_PROCESSED, without an available FASTA, run, or assembly accession. The live BioSample records resolve them to the distinct 2018 human-associated samples described above. |
| One E. coli row | SAMN25146432, SRR17779390, ERZ26077722. The target digits occur within the SeqKit sum, not in a taxonomic assertion. |
| One C. coli row | SAMN31685103, SRR22257350, ERZ26248087. The computational label is Campylobacter_D coli. The matching digits occur within the SeqKit sum. |

A separate ignored-inclusive `JF935080` search returned zero lines across the ten roots and no matches in parsed SOURCE.json metadata or history filenames. No exact target rows occur in the inspected raw BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. These negatives are bounded to the inspected sources and snapshots.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in current assertions. Identity, lineage, grounding, count, attestation, and seed event agree with inspected sources. Unknown-labeled numeric candidates were investigated without inventing target links.

## Recommended Edits

None required.

Separately authorized enrichment must preserve exact accession identity and source scope in maintained inputs or a deliberately designed representation. Necessary seeder changes belong in `src/taxonmech/seed.py` with focused tests. Do not hand-edit this YAML, infer culture deposits, count a marker as a genome, or promote `SEEDED` from this report.

## Follow-up Checks

After an authorized upstream change, use the documented extraction/seeding workflow and `just verify-corpus`, then schema and single-target strict validation. Inspect the emitted TSV, source rows, and regenerated fields.

Require explicit authority-backed identity bridges for new genome/deposit links and directly relevant evidence for functional or causal claims. Isolation context alone does not establish an effect. Do not reuse numeric BioSample or checksum matches as identity evidence. Full-corpus reproduction and QC remain unrun.

## Additional Notes

The review skill, curator boundaries, checklist, repository guidance, relevant schema, and history documentation were read at unchanged HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The source PDF/rendering remained in scratch space; no other isolate's verdict was reused.

The target was byte-compared with its initial full read and remains unchanged. This new report is the sole repository artifact of the target review. No YAML, inventories, generated products, histories, prior reports, or Git/GitHub objects were modified. Eukaryota was not reopened.
