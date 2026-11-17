# YAML Record Review: Nocardiopsis sp. VL18

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/nocardiopsis_sp_vl18.yaml`
- Started UTC: 2026-10-04T17:41:07Z
- Finished UTC: 2026-10-04T17:45:29Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord`, NCBITaxon:1033688, Nocardiopsis sp. VL18. This is a species-ranked BACTERIA placeholder with EXACT grounding, SEEDED status, genetic code 11, zero inventoried BacDive strains, one NCBITAXON NAME attestation and a 2026-09-13T17:54:04Z seed event. No generated field was changed.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/nocardiopsis_sp_vl18.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/nocardiopsis_sp_vl18.yaml`: passed, one file, zero errors.
- Ignored-inclusive exact-identifier search across `data/taxa` completed with only this YAML. Ignored-inclusive exact-stem report search found no prior report.
- Structured comparisons matched backbone, complete lineage, children, seven source inventories, PATHS, scope, attestation and seed text. Exact type-material, merged-ID and dropped-row scans completed separately.
- Not run: full-corpus `just qc`, `just verify-corpus`, tests, provenance, render and documentation checks. Global term/reference and history gates were skipped; no curator-added graph terms, literature references or separate history artifacts are asserted here. Strict validation checked embedded history shape. Focused source comparisons are not corpus reproduction.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221294` and the complete native name object at `data/catalog/ncbi_names-0005.jsonl.gz:30602` agree with the YAML. `data/taxa/PATHS.tsv:13747` pins the identifier and slug; `curation/seed_scope.tsv:321646` supports the attested-rule inclusion dated 2026-09-13.

Live [NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033688&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033688) confirm canonical identity, species rank, parent 2649073 and code 11. No OtherNames were returned. The entire root-first lineage agrees: root 1 (NO_RANK), cellular organisms 131567 (CELLULAR_ROOT), Bacteria 2 (DOMAIN), Bacillati 1783272 (KINGDOM), Actinomycetota 201174 (PHYLUM), Actinomycetes 1760 (CLASS), Streptosporangiales 85012 (ORDER), Nocardiopsidaceae 83676 (FAMILY), Nocardiopsis 2013 (GENUS), unclassified Nocardiopsis 2649073 (NO_RANK). Datasets explicitly includes root 1. The taxonomy browser was unavailable, but both structured authority responses succeeded.

Species rank is the authority's classification, not proof of a formally named species. The placeholder is distinct from VL24 and from unrelated strains sharing part of its designation.

## Evidence

The one NCBITAXON NAME attestation accurately records snapshot 2026-09-13. Exact scans found no direct BacDive, LPSN, GTDB mapping, GOLD, MediaDive, Madin or BactoTraits inventory rows and no child taxa. Type-material, merged-ID and dropped inventories had no target row. Zero strains means zero inventoried BacDive entries, not that VL18 was never cultured.

Exact-taxid NCBI searches returned zero Assembly results with no-items/phrase warnings and one Nuccore record. [JF732910.1](https://www.ncbi.nlm.nih.gov/nuccore/JF732910.1), UID 333360403, is a 1,382-base partial 16S sequence. Inspected GenBank XML explicitly links genomic DNA, strain VL18 and taxon 1033688 to Lonar lake sediment, India, January 2010, coordinates 19.9681 N 76.5022 E, collector Kiran R. Marathe, identifier N. D. Dandi and PCR primers 27F/1517R. This is marker evidence, not a genome assembly or a culture-collection accession.

Both sequence references were read: an unpublished isolate study and direct submission on 2011-03-26 by Marathe, Maheshwari, Chaudhari, Kadam and Dandi from North Maharashtra University. Neither reference supplies a DOI or PMID. The unpublished study title alone does not prove a physiological phenotype.

The author abstract of a [2015 screening article](https://openurl.ebsco.com/contentitem/gcd%3A110194460), inspected through EBSCO, names VL18 among five Lonar-lake actinomycete isolates with protease-inhibitor activity. The author's [institutional publication list, page 7](https://nmu.ac.in/Portals/13/Profile/CV_-Prof.V.%20L.%20Maheshwari.pdf) independently lists the paper in Advances in Pharmacology and Toxicology 16(2), 39-47. Shared designation, site and authors make this a plausible enrichment lead, but the accessible abstract does not give JF732910 or the taxid. The paper body was not available in these checks. No experimental values or finer identity are transferred to this YAML without an explicit isolate/accession link and claim-level primary-text review.

Complete native GenBank objects were inspected for all five candidate matches:

- `data/catalog/ncbi_genbank-0065.jsonl.gz:11995`: GCA_977633765.1, uncultured bacterium taxon 77133, isolate MarMAG_121274, SAMEA120736108, PRJEB104710, WGS CDVABI000000000.1. The scaffold assembly has 100 contigs, 93 scaffolds and total length 1,034,118. Only ungapped length 1,033,688 matches the target taxid digits.
- `data/catalog/ncbi_genbank-0024.jsonl.gz:13743`: GCA_026171045.1, Salmonella enterica taxon 28901, strain VL-18-24, SAMN31019079, WGS DAJWOL000000000.1.
- The same shard, line 13770: GCA_026171565.1, Salmonella enterica taxon 28901, strain VL-18-18, SAMN31019078, WGS DAJWOV000000000.1.
- The same shard, line 13803: GCA_026172195.1, Salmonella enterica taxon 28901, strain VL-18-16, SAMN31019077, WGS DAJWPI000000000.1.
- The same shard, line 13807: GCA_026172275.1, Salmonella enterica taxon 28901, strain VL-18-26, SAMN31019080, WGS DAJWPJ000000000.1.

The four Salmonella objects belong to PRJNA514245 and have no paired RefSeq assembly. Neither a strain-prefix match nor an unrelated genome-length value establishes a taxonomic join. Their source-reported exclusion reasons are not the basis for rejecting the identity match.

The complete ATB row at `data/catalog/allthebacteria.tsv.xz:65050` is SAMEA1033688, runs ERR064661/ERR085920, analysis ERZ3069132. Its scientific and both Sylph labels are Streptococcus pneumoniae. Available FASTA, assembly/Sylph/HQ PASS and prior HQ T do not overcome the unrelated identity. Only the BioSample/download-path suffix matches the taxid digits. The SeqKit sum, batch-600 OSF archive and mutable AWS URL remain unrelated source context, not VL18 genome evidence.

## Completeness

Ignored-inclusive compressed searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, using bounded taxid, VL18 separator variants and name/slug forms. Nine lines were returned: backbone, scope, native name, five unrelated GenBank objects and one unrelated ATB row. Structured SOURCE.json searches in the source roots found no matching manifest evidence.

No missing required representation was found. Optional strains, mappings, nomenclature, datasets, literature evidence, discussion and causal graphs may remain absent. This bounded review found no supported genome link; zero exact-taxid Assembly results do not prove global absence under other identifiers. Literature access limits leave optional enrichment unresolved, not the record's asserted taxonomy.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the asserted fields. The literature lead is not treated as either a verified strain equivalence or a missing required citation.

## Recommended Edits

None required. Future supported source additions belong in the configured upstream resource, `scripts/extract_source_inventory.py`, or a tested `src/taxonmech/seed.py` rule. Do not hand-edit generated YAML, add a genome by numerical or strain-prefix coincidence, or infer a BacDive/deposit identity.

## Follow-up Checks

Before literature enrichment, inspect the complete screening article for an explicit VL18-to-JF732910 identity link and the exact supporting experiment. Later maintained-source changes require the seed dry-run, single-record canary, emitted-file inspection, open/strict validation and full reproduction/QC. No seed mutation was performed here.

## Additional Notes

iModulonDB was not applicable: no gene, locus, regulator, pathway or expression-module claim is asserted. No paid research, contact, GitHub mutation, history write or status promotion occurred. Only a new report was written. The other Codex session is closed; the original worktree remains in use. Eukaryota was not revisited.
