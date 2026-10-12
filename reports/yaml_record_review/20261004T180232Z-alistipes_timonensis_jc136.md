# YAML Record Review: Alistipes timonensis JC136

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/alistipes_timonensis_jc136.yaml`
- Started UTC: 2026-10-04T17:55:50Z
- Finished UTC: 2026-10-04T18:02:32Z
- Verdict: needs curation

## Target

Reviewed the complete generated `TaxonRecord` for `NCBITaxon:1033731`, not the parent species `NCBITaxon:1465754` or another isolate named JC136. The record is a bacterial `STRAIN`, with genetic code 11, `grounding_status: EXACT`, `mapping_status: SEEDED`, one GTDB mapping, two synonyms, four source attestations, and `strain_count: 0`. Its single seed event is dated 2026-09-13T17:54:04Z. The parent species YAML was read for evidence-placement context, not assigned a separate review verdict.

The ignored-inclusive record-identifier search resolved exactly this target. An ignored-inclusive filename search found no previous report for its exact stem before this report was written.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/alistipes_timonensis_jc136.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/alistipes_timonensis_jc136.yaml`: passed; one file scanned, zero error rows. Both commands were rerun at the end of the review.
- Compared the full identity and lineage with the pinned NCBI inventory; compared all seven source-inventory categories, source-attestation counts and units, PATHS entry, scope entry, and seed text. These were bounded evidence comparisons, not a replacement corpus validator.
- Did not run full-corpus `just verify-corpus`, `just qc`, `just test`, provenance, site-drift, documentation-statistics, or vendored-file gates. This report does not certify corpus reproduction or global integrity.
- `just validate-products` was not run: this record contains no curator-added graph groundings. No external history artifact was created or validated; the review skill authorizes a new review report, not history or lifecycle mutations.
- Public NCBI taxonomy, assembly, and selected nucleotide evidence was inspected. GTDB's browser pages could not be retrieved; the mapping assessment instead uses the complete local source-native GTDB catalog and the maintained extraction/seeding code.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221297` supplies the exact identifier, label, rank, parent, genetic code, NCBI synonym, and 2026-09-13 snapshot. `data/taxa/PATHS.tsv:13750` and `curation/seed_scope.tsv:26083` identify this slug and its 2026-09-12 admission under the four-source attestation rule. No direct children were found in the complete backbone comparison. Exact searches of the type-material, merged-ID and dropped-record inventories returned no rows for this strain taxon; species-level type evidence was located separately.

The [NCBI Taxonomy EFetch record](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033731&retmode=xml) and [Datasets taxonomy response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033731) confirm the strain rank, parent 1465754, genetic code 11 and lineage. The twelve stored ancestors, root first, are 1, 131567, 2, 3379134, 1783270, 68336, 976, 200643, 171549, 171550, 239759 and 1465754. Their labels and ranks match the pinned backbone; Datasets also includes the root identifier.

The [legacy Taxonomy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1033731) still displays `no rank` and calls the older name a heterotypic synonym. Preserve this interface discrepancy: the pinned dump and both structured taxonomy APIs support `STRAIN`; do not change the YAML to match a differently rendered page. Native names at `data/catalog/ncbi_names-0005.jsonl.gz:30606` and `:30607` support the older NCBI synonym `Alistipes sp. JC136` and the current scientific name.

The NCBI grounding itself is supported. The GTDB-derived species synonym and equivalence xref are not supported at strain scope; see the major finding.

## Evidence

### Attestations and Source Scope

The NCBI attestation is one NAME. `data/raw/gtdb_mappings.tsv:1356` supplies the mapping to `GTDB:s__Alistipes_timonensis`, `skos:closeMatch`, and 15 GENOMEs; `data/raw/gtdb_species.tsv:7510` independently supplies the species-cluster count. `data/raw/gold_organisms.tsv:445` supplies one ORGANISM and `data/raw/madin_taxa.tsv:621` supplies four TRAIT_ASSERTIONs. All four counts and units reproduce the stored source inputs. They are not interchangeable biological counts.

The primary GOLD catalog contains two organism records carrying this strain taxon, whereas the KGX-derived taxon attestation counts one. That difference is not by itself an attestation defect: these are distinct input surfaces, as documented in `docs/HARMONIZATION.md`. No direct BacDive, LPSN, MediaDive or BactoTraits taxon-inventory rows were found for the target in the complete table comparisons.

### Type Strain and Literature

[LPSN 791422](https://lpsn.dsmz.de/species/alistipes-timonensis) treats Alistipes timonensis Lagier et al. 2014 as a validly published correct species name. Its type designations include AK5, CSUR P148, DSM 25383 and JC136; its marker is JF824799. This names the parent species and its nomenclatural type, not an equivalence between the species and the strain taxon. The local LPSN row is `data/raw/lpsn_names.tsv:28273`, mapped to 1465754.

[BacDive 24536](https://bacdive.dsmz.de/strain/24536) identifies type strain JC136 and deposits DSM 25383, CSUR P148 and JCM 32780. Its native object, `data/bacdive/records.jsonl.gz:24100`, classifies the strain at species taxon 1465754 while its sequence entries carry 1033731. The raw strain row is `data/raw/bacdive_strains.tsv:24101`. The [JCM 32780 catalog](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_number?JCM=32780) independently gives the deposit succession from DSM 25383 and JC136, the Senegal fecal source, assembly 900107675 and WGS projects CAEG and FNRI.

The inspected introduction, classification and genome-project sections of [Lagier et al. 2012, DOI:10.4056/sigs.2685971, PMID:23408657](https://pmc.ncbi.nlm.nih.gov/articles/PMC3558960/) explicitly identify JC136 = CSUR P148 = DSM 25383. The authors describe a human fecal specimen from Senegal, cultured in Marseille, and project CAEG00000000. Their project table calls the sequence a high-quality draft and describes 23 contigs, despite complete-genome wording elsewhere. The paper's 3,497,779-bp description must not silently replace the current catalog's assembly statistics. No phenotype or clinical assertion was added to this record.

[JF824799.1](https://www.ncbi.nlm.nih.gov/nuccore/JF824799.1) was read as GenBank XML: a 1,423-bp partial 16S sequence, source strain JC136, taxon 1033731 and explicit type-material annotation. Its references include the species-description paper, the culturomics article DOI:10.1111/1469-0691.12023 / PMID:23033984, and a direct submission dated 2011-04-18. The latter date precedes the paper's stated June 2011 isolation; retain source-specific dates rather than manufacture a reconciled chronology. The secondary article was not used as independently inspected experimental evidence. A nucleotide search reported 642 records; the initial 100-ID retrieval failed its completeness assertion. Only the selected marker was then fetched. This is not an audit of all 642 nucleotide records, nor a genome count.

### Assemblies and Deposit Links

The live exact-taxid Assembly search returned four records, and all four summaries were inspected. [NCBI Datasets for GCA_900107675.1](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_900107675.1/dataset_report) supplies the full current assembly and BioSample metadata.

- GCA/GCF_900107675.1 is the DSM 25383 assembly: SAMN05444145, GenBank project PRJEB16631, WGS FNRI00000000.1, 22 contigs in 21 scaffolds, 3,488,964 total bases, and 3,488,593 ungapped bases. It is current, reference, and from type material. The ANI response explicitly says no match is expected for the type assembly; its below-threshold best match to another species is not a reason to reidentify JC136.
- GCA/GCF_000285455.1 is the P148 assembly: SAMEA2272181, PRJEA68303, CAEG00000000.1, 38 contigs and 3,489,612 bases in the pinned native catalogs. Live summaries retain both paired accessions. These two isolate assembly pairs must not be collapsed merely because they refer to the same named strain.
- GCA_949463495.1 is isolate `extra-SRR5927705.101_1677798347`, SAMEA112727367; GCA_949738895.1 is isolate `iMGMC-396_1678881645`, SAMEA112815852. Both belong to PRJEB32890 and are excluded from RefSeq as metagenome-derived assemblies failing its MAG annotation-completeness check. Source-native GTDB metadata identifies their isolation source as mouse gut metagenome. Their shared NCBI taxid does not establish a culture-deposit link to JC136.

Full native GenBank objects were read at shards 0000:6560, 0056:39450 and 0061:25272/:34318; the two RefSeq objects are 0000:5599 and 0009:27187. BacDive directly supplies unversioned GCA_000285455 and GCA_900107675, IMG 2547132133/2693429854 and PATRIC 1033731.3/.11. Full BV-BRC objects at `data/bvbrc/bvbrc-0000.jsonl.gz:3186` through `:3189` preserve those isolate links separately from the mouse-MAG entries 1033731.18/.19.

The inspected GOLD DSM chain is Go0143333 -> Gp0148865 -> Ga0131249 -> GCA_900107675.1 / IMG 2693429854, with DSM 25383 matched in explicit strain and collection fields and SAMN05444145 on the project. Native objects are organisms:82548, projects:94294 and analyses:77476. A separate CSUR P148 chain, Go0016398 -> Gp0016398 -> Ga0019631, points to GCA_000285455.1 / IMG 2547132133 and SAMEA2272181; those full native objects are organisms:13948, projects:13493 and analyses:11780. Go0614574, organisms:445298, is the JCM 32780 organism classified at the parent species. Organism and project IDs are not genome IDs, and these chains do not justify transferring arbitrary species-associated assemblies to a deposit.

StrainInfo's full native object at `data/straininfo/records.jsonl.gz:300186` is SI-ID 402297, DOI:10.60712/SI-ID402297.3. Its own available DSM 25383 deposit is SI-DP 909294. The genome sequence explicitly names that same deposit and supplies unversioned GCA_900107675. The parent YAML preserves this evidence; no `.1` was invented, and the JCM/CSUR aliases were not used to transfer another deposit's sequences.

ATB's eligible entry is `atb.assembly:202505.SAMN05444145`, catalog row 1174281 and overlap row 4777. It retains SRR4237016, ERZ26860584, SeqKit sum `seqkit.v0.1_DLS_k0_b631299cb9cf55ef2fc3470b74ff4b87`, available FASTA, assembly/HQ PASS, batch 95, OSF archive and mutable sample-based AWS URL. Seven BioSample evidence assertions from BV-BRC, GOLD, GTDB and NCBI are preserved in the parent strain entry and `data/atb/strain_links.tsv:3810`. Genome crosslinks at rows 16576-16580 are explicitly `shares_biosample`, not assembly equivalence. No FASTA or archive was downloaded or sequence-verified.

## Completeness

Zero listed BacDive strains on this strain taxon is consistent with the current classification-based contract, not evidence that JC136 lacks a deposit or genome. BacDive classifies its strain under parent 1465754. The parent YAML already contains BacDive 24536, its deposits, supported NCBI/GTDB/BV-BRC/IMG links, ATB evidence and StrainInfo assertions. Gathering a parent's strains into each child would violate the documented descendant-only rule.

Absence and collision checks included ignored and hidden files and compressed catalogs: `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. The target-id/name/designation search completed with 85 matching lines; the expanded deposit, marker, sample and GOLD-chain search completed with 73. The source-manifest query was also checked separately. These searches establish the stated local boundaries, not universal absence from external resources.

Excluded collisions include Erythrobacter sp. JC136 (`NCBITaxon:1183082`), an unrelated uncultured-bacterium assembly GCA_982661435.1 whose genome size happens to be 1033731, and ATB rows containing SAMEA1033731 (Streptococcus pneumoniae) or SRR1033731 (Acinetobacter baumannii 730795). Identifiers were compared whole and by type, not joined by numeric substrings. Optional narrative definitions, causal graphs, phenotype assertions and literature slots are not missing required fields. iModulonDB was not applicable to the taxonomic claims being reviewed.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

1. **Major: a species-cluster mapping is promoted to strain-level equivalence.** Target line 49 stores a GTDB species `skos:closeMatch`; line 55 makes the bare species name an `EXACT_SYNONYM` of JC136, and line 60 makes the GTDB species a true-equivalence xref. The GTDB attestation repeats the predicate at line 73. A type strain is not the species it typifies. A complete scan of all 901,341 native GTDB catalog rows found 15 unique accessions in this species cluster: four under NCBI 1033731, ten under parent 1465754 and one under 538949. The four target-taxid rows include the two mouse-gut MAGs above. The cluster count is supported as source-cluster volume, not as 15 JC136 isolates or biological genomes. `data/raw/gtdb_mappings.tsv:1356` supplies the inherited predicate; parent mapping row 31606 is separate. `src/taxonmech/extract.py:501` reads upstream GTDB edges, while `src/taxonmech/seed.py:451` treats every closeMatch as identity and lines 467-469 promote it to xrefs and exact synonyms without checking taxonomic rank. This is a semantic mapping/identity-promotion defect despite passing schema validation.

## Recommended Edits

No generated files were changed. A future correction belongs in kg-microbe's maintained GTDB mapping transform, with a rank-aware defensive rule in TaxonMech's `src/taxonmech/seed.py` and focused regression tests. Keep the species association and assembly classifications as source evidence without declaring species/strain identity. Remove the inappropriate exact synonym and equivalence xref through regeneration after the maintained rule is corrected.

Do not blindly substitute `skos:broadMatch`: the schema defines that predicate from the source taxon's side, for an NCBI target broader than the source, the opposite of this species-to-strain situation. Do not silently rewrite the supported source-cluster count of 15 to the four target-taxid accessions or to two isolate assemblies. Preserve the NCBI identifier, lineage and old NCBI synonym, and preserve the parent species' independently supported nomenclature and strain evidence.

## Follow-up Checks

After an authorized upstream change, re-extract the inventories, run a seed dry-run and the documented JC136 seed canary, inspect its actual YAML, and rerun both record validators. Regression coverage should include species-to-strain closeMatch, a genuine species identity, a non-equivalent pooled mapping, count semantics, and unchanged culture-deposit genome placement. Run `just verify-corpus` and `just qc` before claiming a corpus-wide correction. The mouse-MAG classifications warrant upstream source review if their strain-taxid assignment is to be corrected; they do not authorize TaxonMech to infer a new placement.

## Additional Notes

This was an individual read-only review, resumed across a status-check interruption. Only this timestamped report was added, plus the validator's normal report artifact. No record, maintained inventory, scope, old review report, page, external history, GitHub item or lifecycle status was edited. `SEEDED` was not promoted to human `REVIEWED`. Eukaryota was not re-reviewed. The corpus-wide review goal remains incomplete.
