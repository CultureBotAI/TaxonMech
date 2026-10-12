# YAML Record Review: Actinomycetospora sp. G2Z35

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/actinomycetospora_sp_g2z35.yaml`
- Started UTC: 2026-10-09T00:40:40Z
- Finished UTC: 2026-10-09T00:47:32Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1036510`: species rank, Bacteria domain, parent `NCBITaxon:2636769`, ten root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` status, zero BacDive records, one NCBITAXON name attestation and one seed event. Synonyms, nomenclature, other mappings, genome links and graphs are unasserted.

Ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved one YAML and no prior report for this stem. Generated YAML is not a maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline just validate data/taxa/bacteria/actinomycetospora_sp_g2z35.yaml`: passed, no issues.
- `uv run --offline just validate-strict data/taxa/bacteria/actinomycetospora_sp_g2z35.yaml --out /private/tmp/actinomycetosporaG2Z35-strict.tsv`: passed, one file and zero errors; complete TSV was header-only.
- Structured comparisons checked complete backbone/ancestor rows, lineage, attestation, PATHS, scope and exact seed-event wording. Seven supplementary raw inventories and full type-material, merged-ID and dropped tables were scanned.
- Own nucleotide XML consistency check: declared and actual length 1415, submitted rRNA transcription equals DNA, no non-ACGT symbols. This is annotation consistency, not independent alignment or species assignment.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Individual checks do not establish corpus reproduction. The embedded event was read; stated ignored-inclusive searches found no separate target history artifact. Graph-product validation is inapplicable without graph nodes. No focused substitute for a corpus gate was invented.

## Identity and Grounding

Full [NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036510&retmode=xml) agrees with identifier, label, rank, parent, genetic code and live ancestor labels/ranks. [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036510) confirms all ten root-first ancestor IDs. The chain runs through Bacillati, Actinomycetota, Actinomycetes, Pseudonocardiales, Pseudonocardiaceae, Actinomycetospora and unclassified Actinomycetospora. EFetch omits root from its displayed lineage while Datasets includes it; this is not a conflict.

NCBI species rank for this unnamed strain-associated taxon does not establish a formally described species or synonymy with a congener. Exact grounding denotes this NCBI identity. Live EFetch has no other names; pinned synonyms are empty. Complete pinned scans found no target type-material, merged-ID or dropped row and no backbone children. The literature naming difference below does not establish that this identifier should be replaced by an A. lutea identifier.

## Evidence

Complete target rows were inspected:

- `data/raw/ncbitaxon_taxa.tsv:222510`: identity, rank, parent, code, empty synonyms and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:32054`: exact scientific-name object.
- `data/taxa/PATHS.tsv:15017`: identifier/slug.
- `curation/seed_scope.tsv:322757`: date and admission reason matching the seed event.

The attestation counts one `NAME`, not a genome or experiment. Exact-target scans of BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits raw inventories returned no rows. Under the schema/seeder contract, `strain_count: 0` counts represented BacDive records, not whether a strain designation exists.

Exact Nuccore query `txid1036510[Organism:noexp]` returned UID 334361411. Complete [JF806666.1](https://www.ncbi.nlm.nih.gov/nuccore/JF806666.1) XML, including both references, all source/rRNA features and sequence, explicitly names this taxon and strain G2Z35. It is a 1415-base partial 16S marker, partial at both ends. The source feature supplies organism, genomic DNA, strain and taxon cross-reference, but no host, isolation-source, country, culture-deposit or assembly qualifier. Its feature table has source and rRNA, not CDS.

The references name Chen, Wu and Li, an unpublished seagrass-associated actinobacteria study and direct submission on 13-APR-2011 from the South China Sea Institute of Oceanology. No DOI or PMID is supplied in the nucleotide record. The study title alone does not establish a trait, and absent source qualifiers must not be reconstructed from neighboring accessions.

All seven additional local candidates were fully read and excluded:

- `data/bvbrc/bvbrc-0007.jsonl.gz:15030`: Polaromonas sp., taxid 1869339, strain Bin2_6, genome 1869339.6, assembly GCA_010365105.1, sample SAMN12810504, project PRJNA573403 and WGS JAAFGZ000000000.
- `data/catalog/ncbi_genbank-0009.jsonl.gz:7079` and `data/catalog/ncbi_refseq-0002.jsonl.gz:41248`: the same Polaromonas isolate, paired GCA_010365105.1/GCF_010365105.1, ASM1036510v1, SAMN12810504 and WGS JAAFGZ000000000.1. These are metagenome-derived records; paired assemblies are marked identical, with different annotation dates/counts and projects PRJNA573403/PRJNA224116. The assembly-name digits are not this target taxid.
- `data/catalog/gtdb_genomes-0009.jsonl.gz:41685`: representative RS_GCF_010365105.1 of Polaromonas sp010365105, Bin2_6. Its H2-incubated subglacial sediment and Antarctica metadata do not concern G2Z35.
- `data/catalog/gtdb_genomes-0010.jsonl.gz:48620`: nonrepresentative GB_GCA_039930905.1 in that GTDB cluster, NCBI taxid 1869339, isolate cluster3_bin.283, sample SAMN38393020, project PRJNA746701 and WGS JBDTSY000000000.1. Its country and isolation source are unspecified; Bin2_6 metadata must not be transferred to this genome either.
- `data/raw/gtdb_species.tsv:142190` and `data/raw/gtdb_mappings.tsv:68824`: Polaromonas sp010365105, two genomes, mapping to NCBITaxon:1869339 with `skos:broadMatch`. This mapping is neither an equivalence nor evidence for G2Z35.

Literature searches found a genuine primary study, [Wu et al. (2012), DOI 10.5897/AJMR11.981](https://academicjournals.org/journal/AJMR/article-abstract/2A88A4617354), African Journal of Microbiology Research 6(1):87-94. The publisher abstract and [author-uploaded full text](https://www.researchgate.net/publication/267963976_Culture-dependent_diversity_of_Actinobacteria_associated_with_seagrass_Thalassia_hemprichii) were inspected. The latter describes seawater-washed, homogenized Thalassia hemprichii collected at Nancun Port, China. Its deposited accession range includes JF806666; NCBI supplies the exact strain/accession link. Table 2 identifies A. lutea as G2Z35's most similar published species at 99.22%, not as a demonstrated taxonomic synonym. It reports PCR screening PKS-I negative, PKS-II positive and NRPS positive; the footnote defines the signs as PCR results. These are not measured antimicrobial activity, identified products or proof of complete biosynthetic pathways. G2Z35 is also among the isolates described as slow-growing. Full methods, relevant results/discussion and Table 2 including its footnote were read as HTML text; PDF layout and figure labels could not be visually verified.

A [2018 review's Table 1](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2018.01767/full) instead uses the label Actinomycetospora lutea G2Z35 and cites Wu et al. The naming difference is preserved here as external source scope, not silently adopted. The primary similarity result is insufficient to replace the current NCBI identity or establish an exact synonym. The secondary table's endophyte framing also must not replace the primary study's more limited association evidence.

## Completeness

Complete enough for supported taxonomy-seed claims. Optional nomenclature, mappings, deposits, genomes and graphs should remain empty without explicit identity chains. The external marker and literature context do not require an invented BacDive entry or genome link. Potential biological enrichment is separate from validating this generated seed.

Initial and expanded `rg --no-ignore --hidden -n -z -i` searches covered ignored/compressed files in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Expressions covered taxid, slug and G2Z35, then JF806666 and both literature DOIs. Both returned the same ten rows: three own taxonomy/name/scope rows and seven unrelated candidates. All were read fully. Five `SOURCE.json` files were separately parsed without a target identity match, and history filenames were independently inventoried. Absence statements are bounded to these roots and expressions.

Exact non-expanded Assembly search returned zero with a phrase-not-found warning. PubMed queries for G2Z35/JF806666/JF806666.1 and separately the primary DOI returned zero with quoted-phrase warnings. They demonstrably do not establish literature absence: the primary paper was inspected through another route. Web searches also covered exact strain, accession and DOI expressions; snippets were only leads.

iModulonDB was not run: the YAML asserts no gene, regulator or expression claim and no covered strain/dataset was identified. External PCR screening does not establish expression-module coverage. This is not negative database evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in stored claims. The later literature label is not an authoritative reassignment, and the primary comparison preserves the distinction between an isolate and its closest named species. The YAML agrees with pinned and live NCBI taxonomy.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Do not join on accession substrings, convert nearest-neighbor similarity into synonymy, infer genomes from a marker or promote PCR screening to a demonstrated phenotype.

Future taxonomy corrections belong first at NCBI, then in pinned inputs governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection fixes belong in `src/taxonmech/seed.py` with regression coverage; scope changes belong in `curation/seed_scope.tsv`. Optional marker/literature enrichment requires maintained inputs and model/seeder support, not generated-YAML edits.

## Follow-up Checks

No corrective follow-up required for the current record. Before any biological enrichment, obtain a readable original PDF and visually check Table 2 and Figure 1; preserve the exact strain/accession chain, source scope and screening limitations described above. A formal species reassignment would require independent taxonomic support beyond this comparison.

After an authorized input/seeder change, run a focused regression test, `just seed-canary NCBITaxon:1036510`, inspect its output, rerun both individual validators and `just verify-corpus`, then full publication QC. No generation command ran during this review.

## Additional Notes

Publisher PDF retrieval returned HTTP 403, the CiteSeer copy failed through web and curl routes, and the author-page PDF link failed. The accessible author-uploaded HTML full text was therefore used, with no claim of PDF visual verification. The publisher's main article page dates publication 9 January 2012, consistent with the author copy; another publisher entry for the same DOI displays 31 January. No exact publication date is asserted in the YAML.

Local single-record review, checklist and ownership guidance governed this review. Before/after YAML SHA-256 was `06b52088586a792d4e96c62454678d486b2d0e6716aa98906119bd8166eef890`.

Only this new timestamped report was written for the target. No YAML, source, history, status, generated page or GitHub object changed. Existing worktrees and Eukaryota remained untouched.
