# YAML Record Review: Gleimia coleocanis

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/gleimia_coleocanis.yaml`
- Started UTC: 2026-10-08T02:14:04Z
- Finished UTC: 2026-10-08T02:31:08Z
- Verdict: pass

## Target

The entire 702-line generated `TaxonRecord` was read. It denotes `NCBITaxon:103618`, Gleimia coleocanis, rank SPECIES, domain BACTERIA, parent `NCBITaxon:2692113` (Gleimia). Its nine ancestors, EXACT grounding, SEEDED state, nomenclature, five source-qualified synonym entries, two xrefs, genetic code 11, one listed type strain, genome/related links, five attestations and seed history were reviewed.

The identifier resolves the species record, not the separately indexed DSM 15436 descendant. That descendant was used to verify classification and aggregation, not given an additional YAML verdict.

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/gleimia_coleocanis.yaml` | Passed; no LinkML issues. |
| `just validate-strict data/taxa/bacteria/gleimia_coleocanis.yaml --out /private/tmp/gcoleo-strict.tsv` | Passed; one file, zero errors; TSV header only. |
| Structured backbone comparison | Identity, parent, code, all nine lineage entries, NCBI names, scope and seed event agree. |
| Source and overlay comparison | All fields of 10 assembly, 7 genome-record and 31 related-record assertions match the raw inventories plus validated StrainInfo overlay. No ATB genome entry is eligible. |
| Status/type-material checks | Eight target type-material rows agree with the named deposits/designation. No exact merged-ID or dropped-ID row. |
| Current authorities | NCBI taxonomy, LPSN current/basonym pages, BacDive, assembly/BioSample, nucleotide and publication metadata checked. |

Not run: whole-corpus `just verify-corpus`, QC, provenance, product-label, rendering and documentation gates. The bounded comparison does not prove full-corpus reproduction. There is no curator-added causal graph. Ignored-inclusive searches found no separate target history artifact; inline history shape is covered by schema validation.

Live GTDB and GOLD pages were inaccessible; their pinned primary-source projections were inspected. The StrainInfo landing page/DOI redirect failed, but DOI registration metadata and the complete pinned native strain/deposit object were inspected. IMG's current service state was not independently checked; its identifier is supported by the inspected GOLD chain and BacDive entry.

## Identity and Grounding

NCBI EFetch and Datasets agree on species identity, rank, code, parent, complete carried lineage and sole child `NCBITaxon:525245`, Gleimia coleocanis DSM 15436. The older Actinomyces name is a synonym; authority strings and the CCUG includes-name are not incorrectly promoted to exact synonyms. [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=103618)

LPSN record 798106 supports the current combination, authority, valid publication, correct-name status, three collection deposits and marker AJ249326. Record 772770 identifies Actinomyces coleocanis as the homotypic basonym/synonym. Their separate source-qualified synonym entries need not be collapsed. [Current name](https://lpsn.dsmz.de/species/gleimia-coleocanis), [Basonym](https://lpsn.dsmz.de/species/actinomyces-coleocanis)

The GTDB species xref comes from the LPSN inventory, not a species-level GTDB mapping row. The inspected native genome RS_GCF_000159015.1 is a representative of s__Gleimia coleocanis and names species taxon 103618, strain taxon 525245 and DSM 15436. The YAML does not turn the strain into a species synonym or claim an unsupported mapping predicate/genome count.

## Evidence

Pinned identity: `data/raw/ncbitaxon_taxa.tsv:18520`; child classification: line 119823. Nomenclature: `data/raw/lpsn_names.tsv:33251`, with the older name at line 14987. GTDB species inventory: `data/raw/gtdb_species.tsv:70429`; native representative: `data/catalog/gtdb_genomes-0004.jsonl.gz:46126`.

The cited PMID 30186281 resolves to DOI 10.3389/fmicb.2018.02007. The primary paper's Gleimia coleocanis section explicitly gives the new combination, basonym, M343/98/2, CCUG 41708, CIP 106873, DSM 15436 and SAMN00001853. Its sample accession is not an assembly accession. The other cited DOI, 10.1099/ijsem.0.003071, resolves to the publisher's validation-list article; article metadata and LPSN's association were checked, but its full validation table was unavailable. [Reclassification paper](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2018.02007/full), [Validation-list article](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijsem.0.003071)

BacDive 179 supports M343/98/2, the three deposits, type status and classification under 525245. Its genome annotation reference 66792 is automated DiASPora evidence, not an experimental phenotype citation. Native object: `data/bacdive/records.jsonl.gz:178`; raw strain: `data/raw/bacdive_strains.tsv:179`. The live page confirms the linked assembly, BV-BRC and IMG identifiers. [BacDive 179](https://bacdive.dsmz.de/strain/179)

Current NCBI explicitly pairs GCA_000159015.1 with GCF_000159015.1, identifies DSM 15436/type material and reports scaffold-level ASM15901v1, 35 scaffolds, 40 contigs and 1,723,843 bases. SAMN00001853 supplies culture collection DSM:15436 and project PRJNA31427. PRJNA224116 is the multispecies RefSeq annotation project, not another isolate. [Assembly](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_000159015.1/), [BioSample](https://www.ncbi.nlm.nih.gov/biosample/SAMN00001853), [RefSeq project](https://www.ncbi.nlm.nih.gov/bioproject/PRJNA224116)

The native BV-BRC object at `data/bvbrc/bvbrc-0021.jsonl.gz:30355` independently preserves genome 525245.3, DSM 15436, the versioned GenBank assembly, sample and sequencing project. The native GOLD chain is Go0003591 to Gp0003591 to Ga0027353; its single referenced project resolves the otherwise blank analysis organism field. It explicitly supplies GCA_000159015 and IMG 643886017. Go0626693 and Go0626694 link the CIP and CCUG deposits without being counted as genomes. Go0626692 has only the bare M343/98/2 designation and correctly does not become a culture-identifier join.

StrainInfo 87815.3 has three own available deposits: 278195/CCUG 41708, 301771/CIP 106873 and 301773/DSM 15436. Its complete native object at `data/straininfo/records.jsonl.gz:67635` assigns AJ249326 specifically to 278195 and GCA_000159015 specifically to 301773. Those exact sequence-deposit relationships, DOI version and statuses are preserved. DataCite registration identifies the same species, dataset version and three deposits. [StrainInfo DOI](https://doi.org/10.60712/SI-ID87815.3)

AJ249326 resolves to AJ249326.1, a 1,437-base partial 16S sequence from CCUG 41708, type material of the older species name, taxon 103618. Its reference is PMID 12148628, the original description. The supplied unversioned accession is correctly preserved, and the marker remains outside genome counts. [Marker](https://www.ncbi.nlm.nih.gov/nuccore/AJ249326.1), [Original description](https://pubmed.ncbi.nlm.nih.gov/12148628/)

Source conflict retained: BioSample describes a human host, whereas the original description and BacDive report canine origin. No host assertion occurs in the YAML. The conflict does not negate the explicit deposit/assembly relationship, but must be resolved before importing host or isolation metadata.

Attestations match their distinct units: NCBI one NAME, LPSN one NAME, BacDive one descendant STRAIN, GOLD three direct ORGANISMs and Madin three direct TRAIT_ASSERTIONs. Direct counts are not inflated with descendant records. No biological phenotype or causal edge is asserted. iModulonDB was not applicable to this identity, nomenclature and identifier-link record.

## Completeness

The strain listing is complete for the pinned BacDive inventory. The sole child accounts for its one entry; `classified_as` preserves the narrower identity. Ten assembly assertions are source-specific evidence, not ten different assemblies; similarly, repeated typed genome/related IDs retain distinct source fields. Unversioned source accessions are not silently changed to `.1`.

AllTheBacteria retains SAMN00001853 as NOT_PROCESSED with no FASTA, matching `data/atb/assemblies.tsv:1912` and exclusion `data/atb/exclusions.tsv:1194` (assembly_unavailable). Its omission from eligible genome links is correct. Catalog samples SAMEA5390791 and SAMEA5390793 carry the DSM 15436 name but a conflicting Pauljensenia assignment and no established same-sample/deposit bridge; name matching alone cannot attach them.

Ignored-inclusive compressed-input searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Initial taxon, species, deposit and linked-accession terms produced 162 candidate addresses. Their identity/matching fields were screened; relevant native objects and the non-catalog TSV rows were read in full. Expanded WGS/sample/GOLD terms added 12 objects, all read in full, for 174 candidate addresses total. The additional hits were longer WGS accessions of unrelated organisms, not the target ACFG project.

Other excluded matches include BacDive ID 103618, CIP 103618, DSM 103618, numeric assembly statistics and accession substrings. Database namespaces and whole accessions were kept distinct. Resolution additionally covered `data/taxa` and `reports`, including ignored files, with no prior species review report. All five source metadata JSON files and history filenames were checked. Negative findings are bounded to these roots, not an exhaustive claim about all external resources.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the record's assertions or supported identifier links. The external host conflict and unavailable live source pages remain documented limitations, not silently reconciled facts.

## Recommended Edits

None required. Preserve the generated YAML, source-qualified links and SEEDED state.

Any later authorized enrichment belongs in the maintained source adapter/overlay, `src/taxonmech/extract.py` or `src/taxonmech/seed.py`, not this generated record. Source host corrections belong at the contributing authority. Do not add name-only ATB links or manufacture sequence versions.

## Follow-up Checks

Before importing new host assertions, resolve the BioSample-versus-original-isolation conflict. Before adding either SAMEA sample, require explicit deposit/sample evidence and assess the classification conflict. Recheck inaccessible source pages during an authorized source refresh.

For approved input or generator changes, run the seed dry-run and `just seed-canary NCBITaxon:103618`, inspect the biological diff and repeat both focused validators. Shared changes require full-corpus reproduction, QC, provenance, product-label, rendering and documentation gates. No regeneration was performed here.

## Additional Notes

Scope: `curation/seed_scope.tsv:23617`, added 2026-09-12. Slug: `data/taxa/PATHS.tsv:14811`. Seed event remains `2026-09-13T17:54:04Z`. The scope reason counts original direct sources; the current descendant BacDive aggregation explains the additional attestation.

The publisher's large reclassification HTML exceeded the web reader limit; a structured HTML text read recovered the exact species section. PMC returned a browser challenge. Large BioProject output was truncated; only inspected project identity/description/scope fields are relied on, not its exhaustive secondary-ID or locus lists. Sequence metadata review excluded bases and non-source feature annotations.

Reviewed HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Unchanged target SHA256: `6599caba252c3df7a233a696110e5dbdb2c7f10eaa69438027e7063119b7111d`. Only this new Markdown report was added. No YAML, source inventory, lifecycle, history, GitHub or worktree changes occurred. Eukaryota was not re-reviewed.
