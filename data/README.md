# Data

Datasets are organized into **tiers** that match the phases in [`../ROADMAP.md`](../ROADMAP.md)
and the source catalog in [`../DATA_SOURCES.md`](../DATA_SOURCES.md).

| Folder | Tier | Used in | Contents |
| --- | --- | --- | --- |
| `tier1_census/` | 1 — Census / demographic | Phase 1 | Census, ACS, IPUMS, Pew, ARDA, CDC |
| `tier2_genetics/` | 2 — Modern population genetics | Phase 2 | 1000 Genomes, HGDP, gnomAD, ALFRED |
| `tier3_historical/` | 3 — Historical / origins | Phase 3 | SlaveVoyages, immigration records, Maddison, UN migration |
| `tier4_ancient/` | 4 — Ancient / deep-time genetics | Phase 4 | AADR, archaic genomes, ISOGG / PhyloTree / YFull |

## Conventions

- **Do not commit large raw datasets.** Keep raw downloads out of git (see `.gitignore`);
  commit small, derived/processed extracts and the scripts/notebooks that produce them.
- **Every dataset gets a citation entry** in [`../CITATIONS.md`](../CITATIONS.md) — source,
  access date, version, and license.
- **Mark interpretation.** Derived or inferred figures are labeled as such, never presented
  as reported fact (see the honesty note in `../ROADMAP.md`).
