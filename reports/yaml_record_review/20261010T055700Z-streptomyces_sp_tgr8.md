# YAML Record Review: Streptomyces sp. TGR8

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_sp_tgr8.yaml`
- Started UTC: 2026-10-10T05:54:50Z
- Finished UTC: 2026-10-10T05:57:00Z
- Verdict: pass

## Target

Read the entire 54-line generated `TaxonRecord`, `NCBITaxon:1037522`, Streptomyces sp. TGR8. The record is a species-ranked bacterial placeholder, parent `NCBITaxon:2593676`, with `EXACT` grounding, `SEEDED` mapping status, code 11, zero inventoried strains, one NCBI name attestation, and one seed event. Maintained inventories and `curation/seed_scope.tsv`, interpreted by the extractor/seeder, own future changes; the generated YAML is not manually editable.

## Validation

Commands ran with `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/streptomyces_sp_tgr8.yaml`: passed, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/streptomyces_sp_tgr8.yaml --out /private/tmp/taxonmech-tgr8-20261010-validation.tsv --workers 1`: one file, zero errors. The TSV was read and contains only the header.
- `python scripts/validate_history.py history`: 17 valid history records, zero invalid links.
- Structured source comparisons passed for identity, all lineage entries, synonyms, genetic code, name attestation, path index, scope reason, and seed-event wording. These checks are not corpus reproduction.
- `just validate-products`: not applicable; no graph nodes or curator-added ontology claims. No separately documented focused term/reference validator applies; source identifiers were checked directly.
- Not checked: `just qc`, full-corpus `validate-all`, `verify-corpus`, provenance/vendored gates, tests, documentation statistics, and site rendering. Full-corpus checks were not run for this read-only record review.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222794` agrees with the complete identity, parent, rank, genetic code, and 2026-09-13 snapshot. Its synonym and retirement fields are empty. The root-first lineage matches the individual inventory rows: root 1; cellular organisms 131567; Bacteria 2; Bacillati 1783272; Actinomycetota 201174; Actinomycetes 1760; Kitasatosporales 85011; Streptomycetaceae 2062; Streptomyces 1883; unclassified Streptomyces 2593676. All labels/ranks agree; no hierarchy was inferred or reconciled to another source.

Live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037522&retmode=xml), [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037522), and [Taxonomy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1037522) agree. EFetch omits the root from displayed ancestry; Datasets includes it, matching the YAML. The species rank is compatible with a source sequence bearing strain TGR8; it does not establish a formally named species or culture deposit. The Datasets response omits an assembly count; that omission does not prove zero assemblies. The broad BLAST group is not strain-level phenotype evidence.

The full native name row `data/catalog/ncbi_names-0005.jsonl.gz:32432` matches the scientific name. No own child, type-material, merged-ID, or dropped-ID rows were found by structured source scans. `data/taxa/PATHS.tsv:15347` resolves this identifier uniquely. `curation/seed_scope.tsv:323011` supplies the attested scope reason exactly reproduced in the 2026-09-13T17:54:04Z seed event. There is no assertion of human review sign-off.

## Evidence

The attestation accurately counts one NCBI `NAME`, not a strain, genome, publication, or experiment. No own rows were present in the seven pinned BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, and BactoTraits inventories checked. The empty optional strain/nomenclature/mapping sections therefore agree with those inputs. Zero listed strains is an inventory count, not an absence-of-isolates or unculturability claim.

The exact NCBI Nucleotide query `txid1037522[Organism:exp]` returned one UID, `334361468`. The complete [GenBank annotation for JF799836.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799836.1) explicitly joins the organism name, strain TGR8, and `taxon:1037522`. It is a 781-base partial 16S rRNA gene, incomplete at both ends, from wetland soil. Declared and retrieved lengths agree and the sequence alphabet is A/C/G/T; lowercase-sequence SHA-256 is `e3aae79f4e02bab97ceb43af488b01b8bea33c67f03e632349efcc86a3c9b955`. The genomic-DNA source qualifier does not make this marker a genome assembly.

Its single reference is a direct submission by Li, Liu, Shao, and Sun dated 10 April 2011, through Hebei University. No DOI/PMID, collection country, sampling date, coordinates, or culture-collection accession is supplied. The submitter's Baoding address and submission date must not become collection metadata. The wetland-soil qualifier is narrowly supported source context, not a measured phenotype or genus-wide ecological claim; its absence from this seeded taxonomy/name record is not a required-field defect.

Eighteen lines matched the broad ignored-inclusive repository search, including three own rows and 15 non-target rows, all of which were read in full:

- Burkholderia sp. PTGR-8 (`NCBITaxon:1395895`) appears in backbone line 343020, scope line 422434, and `data/catalog/ncbi_names-0008.jsonl.gz:18256`. The extra P and different taxon are not aliases of this target.
- Solirubrobacter phytolaccae (`NCBITaxon:1404360`) has the related name Solirubrobacter sp. GTGR-8 in backbone line 346306 and native name line 21756 of that same name shard. `data/raw/ncbi_type_material.tsv:28959` and 28960 refer to its GTGR-8 type strain. `data/bacdive/records.jsonl.gz:86178` is BacDive 163943 for this other species, with JCM 31078/CCTCC AB 2013011/KCTC 29190, marker KF459924, and genome GCA_027587195. None supplies a target deposit, synonym, or genome.
- Six native rows contain BioSample `SAMN10375220` for Bacillus subtilis BH5 (`taxid 1423`): BV-BRC `1423.662` at `data/bvbrc/bvbrc-0003.jsonl.gz:11687`; GenBank `GCA_003833255.1` at `data/catalog/ncbi_genbank-0003.jsonl.gz:654`; suppressed RefSeq `GCF_003833255.1` at `data/catalog/ncbi_refseq_historical-0000.jsonl.gz:18728`; GTDB at `data/catalog/gtdb_genomes-0013.jsonl.gz:32232`; GOLD project `Gp0389936` at `data/gold/projects.jsonl.gz:277384`; and AllTheBacteria `ERZ25501856` at `data/catalog/allthebacteria.tsv.xz:1506365`. The GTDB/Sylph Bacillus cabrialesii assignments concern that unrelated strain, not TGR8.
- `data/catalog/ncbi_genbank-0033.jsonl.gz:35306` is Streptococcus pneumoniae (`taxid 1313`), isolate 404, `GCA_036048235.1`, assembly name `PDT001037522.1`, `SAMN11121240`, `PRJNA514245`. Its PMID 30286803 is not target evidence. Numeric substrings are not identity links.

A previously identified same-designation lead was checked against primary full text: Hunter et al. (2005), [Bacillus subtilis is a Potential Degrader of Pyrene and Benzo[a]pyrene](https://pmc.ncbi.nlm.nih.gov/articles/PMC3810630/), DOI `10.3390/ijerph2005020010`, PMID `16705827`. Bibliographic front matter, abstract, all Tgr-relevant paragraphs, and complete Table 1 were read. Table 1 lists Tgr 8 as a Gram-positive rod; the identification paragraph does not identify it as Streptomyces. Detailed PAH transformation experiments concern Tgr3. The target's complete name, accession JF799836, and taxon ID are absent from the downloaded XML. The similar designation provides no demonstrated identity bridge: no phenotype, morphology, growth condition, or Southern Maryland locality was transferred to TGR8.

## Completeness

Ran `rg --no-ignore --hidden -n -z -i -g '!SOURCE.json'` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Initial patterns included the numeric taxon ID, full label, exact slug, and `TGR[ _-]?8`; the expanded pass added `JF799836`. Both returned the same 18 lines, including ignored and compressed files. No additional target-linked strain, genome, attestation, or history record was established on these searched surfaces, not universally.

Independently enumerated and fully parsed all five `SOURCE.json` metadata files under the source directories; no target/accession matches. Ignored-independent filename scans found this target and the distinct Burkholderia PTGR-8 filename, with no matching pre-existing report or target history filename. No Eukaryota YAML content was opened.

Web searches used the complete name, designation with soil/bacterial terms, and `JF799836`. Broad designation queries yielded unrelated leads; none was treated as identity or phenotype evidence from a snippet. No experimental publication specifically linked to this target was established by the bounded search and primary-text inspection. This does not prove that none exists. iModulonDB was not applicable because the record has no gene, regulator, module, stress-response, or transcriptomic claim.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The record accurately retains its taxonomy/name-only source scope. No unsupported strain, genome, phenotype, or literature assertions are present. Near-name records and numeric collisions are not omitted target evidence.

## Recommended Edits

None required. Do not hand-edit generated YAML, add a history event, or promote review status. Future confirmed enrichment belongs in maintained inventories or an explicitly designed curation input. Extraction/seeding changes belong in `scripts/extract_source_inventory.py`, `scripts/seed_from_sources.py`, and their implementation modules; scope changes belong in `curation/seed_scope.tsv`. Do not use TGR8 alone as a global strain identifier or upgrade a partial marker to a genome link.

## Follow-up Checks

Any later strain/genome association must demonstrate the exact source chain and full deposit accession; any proposed phenotype must resolve the experimental isolate to this target. After an authorized maintained-input change, re-run focused schema/strict/history checks and the documented dry run, seed canary, corpus reproduction, and full quality gates. Review-status promotion requires separate human sign-off.

## Additional Notes

The web reader failed to open NCBI's browser page; a direct fetch succeeded and all 74 parsed text lines were read, alongside complete EFetch/Datasets responses. The Hunter article XML was 56,488 bytes, SHA-256 `f8622f20dc4cd738b7f09c5e7e684a607c066e2ddea6edde3237ced7ccecade1`. Its table uses the spaced spelling Tgr 8, so a literal zero count for unspaced Tgr8 is not an absence finding; the table itself was inspected.

YAML SHA-256 at review: `d1538003f2f04561843e08c964071ef67a8cf49ee9d7b05b1890d707a6769e1b`. Only this new report was written; generated records, maintained sources, history, site, schemas, GitHub state, Eukaryota, and existing worktrees were left unchanged.
