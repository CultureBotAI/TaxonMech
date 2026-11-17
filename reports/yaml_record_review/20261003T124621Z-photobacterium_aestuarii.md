# YAML Record Review: Photobacterium aestuarii

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/photobacterium_aestuarii.yaml`
- Started UTC: 2026-10-03T12:40:09Z
- Finished UTC: 2026-10-03T12:46:21Z
- Verdict: pass with minor issues

## Target

Generated `TaxonRecord` for `NCBITaxon:1028750`, Photobacterium aestuarii,
rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:657` (Photobacterium).
Grounding is `EXACT`; mapping status remains `SEEDED`.

Read the entire 222-line YAML. It includes one BacDive strain, six GOLD
organism assertions, two StrainInfo assertions and six source attestations.
No assembly, genome record or GTDB mapping is asserted. The related-record
count is not a count of distinct strains, organisms or genomes.

This is a read-only review. No source, generated record, history, status or
page was changed.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/photobacterium_aestuarii.yaml` | PASS; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/photobacterium_aestuarii.yaml` | PASS; one file, zero errors. |
| Complete lineage and BacDive subtree | PASS; all nine ancestor objects, complete strain membership and strain scalar fields match raw inventories. |
| Full raw and StrainInfo link equality | PASS; zero assembly, zero genome and eight related-record objects match the inventories, including complete nested evidence. |
| Native GOLD and StrainInfo checks | PASS; all six GOLD assertions and both StrainInfo assertions match native identifiers, taxids, matching fields and source values. |
| Native genome-source search | No matching assembly/genome row for the target identity and deposits in the inspected complete catalogs; ignored and compressed files included. |
| `just verify-corpus` | Not run: full-corpus reproduction check, not a focused record validator. Target comparisons do not replace it. |
| `just validate-history` | Not run: ignored-inclusive target search found no standalone history. Strict validation checked the embedded seed event. |
| Graph and generated products | Not run: no graph is asserted; generated pages and other products were outside this review. |

An initial ad hoc comparison failed because it had not converted the table's
`straininfo_evidence_json` field into the YAML's nested `straininfo_evidence`.
After applying the documented conversion, complete object equality passed.
This was a review-script error, not a record defect.

## Identity and Grounding

The inspected [NCBI Taxonomy page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1028750)
agrees on ID, current name, species rank, parent, genetic code 11 and lineage.
The complete raw subtree contains only this taxon. Native NCBI name rows
support the authority-bearing name and Photobacterium sp. YA11 as related
synonyms, not exact taxonomic equivalences.

The [LPSN page](https://lpsn.dsmz.de/species/photobacterium-aestuarii)
confirms record 791507, Lo et al. 2014 authorship and valid correct-name
status. Its type designations are DSM 28821, JCM 18592, KACC 16912 and YA11.
The existing DSM/JCM matches correctly support the true type flag despite M1.
The medical-use wording concerns the recommended name; it is not evidence
of therapeutic use or a species-level pathogenicity assertion.

## Evidence

**Raw provenance.** Identity traces to `data/raw/ncbitaxon_taxa.tsv:219200`,
nomenclature to `data/raw/lpsn_names.tsv:28351`, and the strain to
`data/raw/bacdive_strains.tsv:24216`. Culture crosswalks, the scope entry
and legacy-page path exist. The scope reason and embedded seed event agree
on six sources.

**Publications and marker.** The inspected
[original publisher page](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.056861-0)
confirms the original-description DOI, authors, February 2014 publication
metadata and abstract. Its type assignment explicitly connects YA11,
KACC 16912 and JCM 18592. DSM 28821 is supported by the collection sources,
not inferred from that abstract. The article's full body was not reassessed.

The inspected [publisher issue contents](https://www.microbiologyresearch.org/content/journal/ijsem/64/5)
associate DOI 10.1099/ijs.0.063446-0 with Oren and Garrity's notification
for volume 64, part 2. The direct notification page timed out; its full
species table was not inspected. LPSN independently associates this
notification with the name.

The raw LPSN row includes PMID 24158952. NCBI's inspected taxon reference
links its Lo et al. description to that PMID, supporting the association.
Independent PubMed access returned a browser check or footer-only text;
Europe PMC retrieval also failed. The PMID's full metadata was not independently
reassessed. No browser challenge was bypassed.

The complete native BacDive 24658 object and inspected
[BacDive page](https://bacdive.dsmz.de/strain/24658)
support YA11, all three collection deposits and the type designation.
Its native sequence section contains the partial 1,407-base YA11 16S marker
JF751050, also listed by LPSN. No genome-sequence object is present.
The live nucleotide page was unavailable; the sequence payload was not
reassessed. This marker is not an assembly or whole-genome accession.

**GOLD.** Read all four native organism objects for taxid 1028750:
Go0617984 (YA11), Go0617985 (KACC 16912), Go0617986 (JCM 18592) and
Go0617987 (DSM 28821), at `data/gold/organisms.jsonl.gz:448664` onward.
The three eligible collection deposits each match two independently
recorded source fields, yielding exactly six assertions. The whole-culture
parser accepts each deposited accession but rejects bare YA11. The fourth
organism remains valid taxon-level count evidence without becoming an
unsupported strain link. These are organism references, not genome objects.

Ignored-inclusive decompressed searches of all native GOLD organism,
project and analysis files found no project/analysis link for the three
eligible organism IDs. The count of four GOLD organisms is consistent with
the complete native set; it need not equal the six strain-link assertions.

**StrainInfo.** Read the complete native SI-ID 397496 object at
`data/straininfo/records.jsonl.gz:295385`. Its sole rich own-deposit object
is available DSM 28821, SI-DP 904128, explicitly type material with matching
NCBI/LPSN IDs. The collection is not deprecated and the corresponding
relation is not flagged erroneous. BacDive ID 24658 agrees.

Both assertions preserve the correct record ID/type, SI source ID, own-deposit
matching field, DSM accession and complete eight-field nested evidence.
The published strain status and DOI 10.60712/SI-ID397496.3 agree with the
native record and its archive's latest entry. This is a versioned strain-record
DOI, not a publication or genome identifier. Live StrainInfo and DOI retrieval
were unavailable, so independent current resolution remains unconfirmed.

JCM 18592, KACC 16912 and YA11 occur as relation designations, not additional
rich own-deposit objects. They do not authorize invented SI-DP links.
No native sequence array supplies an assembly or nucleotide assertion.
The served BacDive page was an older 2024 version with an older SI DOI;
that does not invalidate the newer native version-3 evidence in the YAML.

**Counts and media.** Inventories support one NCBI name, one LPSN name,
one BacDive strain, two MediaDive media, four GOLD organisms and one
BactoTraits trait assertion. The two medium IDs are mediadive.medium:514
and mediadive.medium:J118. These are taxon-level inventory attestations,
not two strain-specific recipe or growth assertions. Raw BacDive medium
count is zero; `src/taxonmech/seed.py:516` intentionally omits that zero
from the strain. Units are not summed or promoted to biological claims.

## Completeness

The complete BacDive subtree and all eight existing related-record
assertions are accounted for. M1 is the only confirmed record defect.
Optional phenotype, mechanism, graph and general evidence slots may remain
empty for this source-inventory seed.

Ignored-inclusive, case-insensitive decompressed searches covered native
GenBank/RefSeq current and historical catalogs, BV-BRC, GTDB, GOLD,
StrainInfo and ATB, plus raw links and overlays. Target taxid, normalized
name, included YA11 name and DSM/JCM/KACC deposit spellings yielded no
eligible genome row. Raw GTDB searches found no target mapping. This is
bounded snapshot evidence, not a claim that the species is unsequenced.

Live NCBI exposes two relevant BioSamples. The inspected
[SAMN07327676 record](https://www.ncbi.nlm.nih.gov/biosample/7327676)
explicitly identifies JCM 18592, alias CFSAN065505, and project PRJNA243331.
The inspected [SAMN09463004 record](https://www.ncbi.nlm.nih.gov/biosample/9463004)
identifies CAIM 1934T and project PRJNA451510. Neither inspected sample page
provides an assembly link. The multispecies projects' aggregate data counts
cannot establish an assembly for this target.

A further ignored-inclusive decompressed search across `data/catalog`,
`data/bvbrc`, `data/gold`, `data/straininfo`, `data/atb` and `data/raw`
found neither sample accession nor either newly observed strain alias.
These are bounded future source-coverage leads, not missing rows from the
currently supported seed inputs. CAIM equivalence needs its own collection
evidence before attaching that deposit. No ATB assembly is inferred from
a sample alone, and unlabelled samples elsewhere remain outside this audit.

Identifier/label/slug searches included ignored and hidden raw, curation,
history and prior-report files. No target-specific standalone history or
prior report was found. Compressed sources were explicitly decompressed.

## Findings

Counts: **0 blocker, 0 major, 1 minor**.

**M1 - Minor: the nomenclature type-deposit list omits KACC 16912.**
YAML lines 48-50 list DSM 28821 and JCM 18592 but omit KACC 16912.
The inspected LPSN page and original-description abstract support KACC;
`data/raw/ncbi_type_material.tsv:1460` also records it. YAML line 76 already
retains KACC in the strain's culture list, and line 77 correctly marks
the strain as type material. Identity is not broken.

The omission already exists in `data/raw/lpsn_names.tsv:28351`.
`src/taxonmech/seed.py:405` faithfully projects that list. The future fix
belongs to the maintained upstream KG-Microbe LPSN transform supplying
type-deposit edges consumed by `src/taxonmech/extract.py:461`. The precise
upstream loss stage was not established. Do not hand-patch generated YAML
or raw inventories to conceal it.

## Recommended Edits

1. In separate authorized curation, inspect the upstream LPSN source and
   transform for 791507 and preserve KACC 16912 alongside DSM 28821 and
   JCM 18592. Keep YA11 as a designation, not a culture-collection accession.
2. After fixing the maintained input, run `just extract-inventory` with the
   configured checkout, dry-run `just seed`, then regenerate this record
   with `just seed-canary NCBITaxon:1028750`.

## Follow-up Checks

- Add a regression at the maintained extraction boundary for all three
  collection type deposits; preserve the true type flag.
- Rerun both exact record validators and complete raw/native link comparisons.
  A deposit-list repair should not alter the eight supported link assertions.
- Run `just verify-corpus` before merging curation changes; it was skipped here.
- Retry PubMed metadata, nucleotide, notification and live SI DOI retrieval.
- Investigate the two BioSample leads only in a separately authorized source
  coverage change; require explicit deposit and assembly evidence as applicable.

## Additional Notes

iModulonDB was not applicable: no named gene, regulator, pathway or
transcriptomic relationship is asserted. No GTDB authority page was required
for an asserted mapping because the record has none; the bounded raw/native
searches above do not prove global absence.

This review does not certify the full corpus, archive sequence payloads or
published site. No source refresh, catalog rebuild, history event or review
status promotion was performed.
