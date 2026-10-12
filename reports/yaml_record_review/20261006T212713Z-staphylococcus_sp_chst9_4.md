# YAML Record Review: Staphylococcus sp. ChST9.4

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/staphylococcus_sp_chst9_4.yaml`
- Started UTC: 2026-10-06T21:22:14Z
- Finished UTC: 2026-10-06T21:27:13Z
- Verdict: pass

## Target

The entire generated `TaxonRecord` was read. `NCBITaxon:1035304` is Staphylococcus sp. ChST9.4, `SPECIES` in `BACTERIA`, parent `NCBITaxon:91994`. Ten root-first ancestors, code 11, `EXACT` grounding, `SEEDED` mapping status, zero inventoried strains, one NCBITAXON NAME attestation, and one seed event are asserted.

No synonyms, nomenclature, taxonomy mappings, strain listings, genomes, phenotypes, citations, or causal graphs are asserted. Generated fields remain read-only. Any future correction belongs in maintained source transforms, inventory extraction, scope decisions, or `src/taxonmech/seed.py`, not this YAML or generated pages.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/staphylococcus_sp_chst9_4.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/staphylococcus_sp_chst9_4.yaml --out /private/tmp/s94-strict.tsv`: exit 0, one file scanned, zero errors. The actual emitted TSV was read and is header-only.
- Structured comparisons inspected the full backbone row, every ancestor in order, direct children, seven non-NCBI inventories, PATHS, scope, attestation, and seed-event text. All compared fields agree.
- Exact checks of `data/raw/ncbi_type_material.tsv`, `data/raw/ncbi_merged_ids.tsv`, and `data/raw/dropped.tsv` found no target entries.
- Ignored-inclusive searches, complete native candidate inspection, full SOURCE.json parsing, and history-filename checks completed.
- `uv run --offline --project ../../culturebotai-claw kg-microbe-sources imodulondb datasets`: exit 0 with network access; all 28 rows inspected before external follow-ups. The keys `s_aureus/staph_precise108` and `s_aureus/staph_precise165` cover S. aureus, not this unnamed isolate. No exact organism/dataset match; iModulonDB is not applicable, not negative biological evidence.
- Live NCBI taxonomy XML, Datasets taxonomy JSON, exact-organism Assembly/nuccore searches, complete sequence metadata, and an independent Datasets genome query succeeded.
- Accession-specific BioSample searching returned all ten unknown-labeled ATB candidates. Their full XML records were read before excluding them.
- The exact-isolate Table II row on printed page 886 of the primary paper was visually checked using the existing PDFKit rendering. This is a bounded table inspection, not full-paper review.
- Not checked: full-corpus `just verify-corpus`, corpus-wide QC/history/provenance gates, full tests, page rendering, original-taxdump regeneration, or source-file hashes. Manual comparisons do not replace corpus-only gates.

## Identity and Grounding

The backbone `data/raw/ncbitaxon_taxa.tsv:222005`, scientific-name object `data/catalog/ncbi_names-0005.jsonl.gz:31481`, and live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035304&retmode=xml) agree on ID, exact label, rank, parent, bacterial placement, and code 11. The [Datasets taxonomy response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035304) confirms all ancestor IDs.

Every ancestor ID, label, and normalized rank agrees: root; cellular organisms; Bacteria; Bacillati; Bacillota; Bacilli; Caryophanales; Staphylococcaceae; Staphylococcus; unclassified Staphylococcus. Family 90964, genus 1279, and parent 91994 agree. EFetch omits root from its displayed chain; Datasets includes ID 1.

Pinned synonym fields and live alternate-name content are empty; the pinned backbone has no direct children. NCBI's species rank does not establish a formally named species, a type strain, or equivalence with S. aureus. ChST9.4 must remain distinct from CtST9.4 and from the unrelated numerical isolate 1035304.

## Evidence

- The NCBITAXON attestation represents one NAME at snapshot 2026-09-13. `data/taxa/PATHS.tsv:14496` maps the identifier to this stem; `curation/seed_scope.tsv:322279` supplies the exact scope reason in the event.
- Raw, ATB, and StrainInfo MANIFEST.yaml extraction times were read as 2026-09-13T17:50:44Z, 2026-09-13T17:54:04Z, and 2026-09-13T17:29:00Z. Their maximum matches the seed timestamp under the inspected seeder rule. This is seeding provenance, not human sign-off.
- Exact nuccore searching returned one record, UID 334899389, [JF935104.1](https://www.ncbi.nlm.nih.gov/nuccore/JF935104.1). Complete metadata excluding nucleotide bases describes an 889 bp partial 16S rRNA sequence, strain ChST9.4, taxon cross-reference 1035304, female shoulders, host Sturnira lilium, Venezuela, collection date 16-Feb-2010. Direct submission was 12-Apr-2011 by Gonzalez and Fermin at Universidad de Los Andes. This marker is neither an assembly nor a culture-deposit accession.
- The cited [Interciencia paper, 39(12):882-889 (2014)](https://www.redalyc.org/pdf/339/33932786009.pdf), Table II, page 886, pairs JF935104 with ChST9.4, Staphylococcus sp., female S. lilium, and shoulders, agreeing with GenBank. No DOI or PMID occurs in the inspected sequence reference metadata.
- Exact-organism Assembly searching returned count 0 with a no-items/phrase warning. An independent [Datasets genome query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1035304/dataset_report) returned an empty object. These bounded results do not establish global genome absence.
- Full [BioSample XML for the ten ambiguous candidates](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=biosample&id=10353049%2C10353048%2C10353047%2C10353046%2C10353045%2C10353044%2C10353043%2C10353042%2C10353041%2C10353040&retmode=xml) identifies SAMN10353040 through SAMN10353049 as human-associated samples from China, collected 2018-07-11, taxon 1869227 (bacterium), project PRJNA503135. Their sample names, in accession order, are FC2225, X2181, FC1984, FC2813, FC2305, FC1914, FC1942, FC1355, FC1843, and FC1451. None names ChST9.4 or its taxon. Their different source context resolves the numeric candidates without interpreting ATB's unknown labels as proof of identity or unrelatedness.

## Completeness

The seeded identity is complete enough. Optional host, culture, and marker details are not required slots. `strain_count: 0` counts inventoried BacDive-backed entries, not every biological isolate. A GenBank strain qualifier is not a registered culture deposit.

The source search used `rg --no-ignore --hidden -n -z -i` with `1035304|ChST[-_ ]?9[._ -]?4\b|staphylococcus_sp_chst9_4` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Ignored, hidden, and compressed files were included. Five source-native SOURCE.json files were parsed completely; history filenames were checked independently.

All 24 candidate lines were inspected in full native form: ten JSON objects and fourteen TSV rows. Lossless structured displays retained every value and asserted reconstruction. Three are exact backbone, scientific-name, and scope entries. The other 21 do not support a target link:

| Candidates | Why excluded |
| --- | --- |
| Five Solibacillus entries | BV-BRC 412383.3, GOLD Go0552181/Gp0504480, GenBank GCA_900168685.1, RefSeq GCF_900168685.1, and GTDB RS_GCF_900168685.1 all concern S. isronensis Marseille-P3605, taxon 412383. Their matching BioSample substring is SAMEA103530418; the assembly project is PRJEB19810, with RefSeq project PRJNA224116. |
| Three M. tuberculosis entries | BV-BRC 1773.18320 and ATB SAMEA3558837/ERZ9334446 share run ERR1035304, not the target TaxID. A separate ATB SAMEA112910661/ERR11252620/ERZ26335095 row matches within its SeqKit sum. |
| One C. jejuni assembly | GCA_010353045.1, taxon 197, strain PNUSAC014828, SAMN13750677, PRJNA239251. Matching assembly digits are not target grounding. |
| One S. aureus assembly | GCA_031876735.1, taxon 1280, isolate 1035304, SAMEA113541662, PRJNA514245. Its numerical isolate name must not be confused with NCBITaxon:1035304. |
| One Methylophilaceae assembly | GCA_984331695.1, taxon 2030816, isolate TARA_SAMEA4397034_MAG_00000014, SAMEA122620682, PRJEB103742. The matching number is ungapped genome length 1035304. |
| Ten unknown-labeled ATB rows | SAMN10353040 through SAMN10353049 are NOT_PROCESSED, without FASTA, run, or assembly accessions. Live BioSample authority records resolve them to the distinct samples described above. |

A separate ignored-inclusive `JF935104` search returned zero lines across those ten roots and no matches in parsed SOURCE.json metadata or history filenames. No exact target rows occur in the inspected raw BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, or BactoTraits inventories. All negatives are bounded to the inspected sources and snapshots.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in current assertions. Identity, lineage, grounding, count, attestation, and seed event agree with inspected sources. Numerical isolate, accession, and length collisions were excluded without promoting unrelated evidence.

## Recommended Edits

None required.

Separately authorized enrichment must preserve exact accession identity and source scope in maintained inputs or a deliberately designed representation. Necessary seeder changes belong in `src/taxonmech/seed.py` with focused tests. Do not hand-edit this YAML, infer a culture deposit, count a marker as a genome, identify the isolate as S. aureus, or promote `SEEDED` from this report.

## Follow-up Checks

After an authorized upstream change, use the documented extraction/seeding workflow and `just verify-corpus`, then schema and exact-target strict validation. Inspect the emitted TSV, source rows, and regenerated fields.

Require explicit authority-backed identity bridges for any genome or deposit link and direct evidence for functional or causal claims. Isolation context alone does not establish an effect. Numerical matching is insufficient even when an adjacent source uses the digits as an isolate name. Full-corpus reproduction and QC remain unrun.

## Additional Notes

The review skill, curator boundaries, checklist, repository guidance, relevant schema, and history documentation were read at unchanged HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The source PDF/rendering remained in scratch space; no other isolate's verdict was reused.

A web-rendered nuccore request was inaccessible; direct NCBI EUtils metadata retrieval succeeded and supplies the inspected sequence evidence. An initial lookup used incorrect SOURCE.json paths for raw/ATB manifests; an ignored-inclusive filename search located their MANIFEST.yaml files, which were then parsed successfully.

The target was byte-compared with its initial full read and remains unchanged. This new report is the sole repository artifact of this target review. No YAML, inventories, generated products, histories, prior reports, or Git/GitHub objects were modified. Eukaryota was not reopened.
