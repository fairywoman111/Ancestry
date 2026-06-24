# Data Sources

Sources are organized in **tiers** that match the phases in `ROADMAP.md`. Tier 1 is the
most readily available and structured; later tiers require more effort and carry more
interpretation. Track **license + citation** for every source as it is brought in.

---

## Tier 1 — Census / demographic *(free, structured)*

The macro baseline. Used in Phase 1.

| Source | What it provides | Notes |
| --- | --- | --- |
| **US Census Bureau** (data.census.gov) | Decennial census + American Community Survey (ACS): race, ethnicity, ancestry, language, income, geography | Free public **API** available |
| **IPUMS** (Univ. of Minnesota) | Historical US census **microdata** back to 1790; IPUMS International for other countries | Free; registration required |
| **Pew Research Center** | Religion and demographic reports/surveys | Free reports |
| **ARDA** (Association of Religion Data Archives) | Religious adherence by geography | Free |
| **CDC / NCHS** | Vital statistics — births, deaths | Free |

## Tier 2 — Modern population genetics *(free, public)*

Overlaying genetics onto census groups. Used in Phase 2.

| Source | What it provides | Notes |
| --- | --- | --- |
| **1000 Genomes Project** | Reference genomes across world populations | Open access |
| **HGDP** (Human Genome Diversity Project) | Worldwide population reference panel | Open access |
| **gnomAD** | Allele frequencies across large, diverse cohorts | Open access |
| **ALFRED** | Allele frequency database by population | Open access |
| 23andMe / AncestryDNA | (Proprietary datasets) | Use their **published papers**, not raw data |

## Tier 3 — Historical / origins

The documentary "where they came from" arc. Used in Phase 3.

| Source | What it provides | Notes |
| --- | --- | --- |
| **SlaveVoyages.org** | Trans-Atlantic & Intra-American slave trade databases | Key for the West-African origins arc |
| **IPUMS historical** + immigration/naturalization records | Settlement and immigration history (e.g. Ellis Island) | Free / archival |
| **Maddison Project Database** | Historical population & GDP over centuries | The economics thread |
| **UN DESA International Migrant Stock** | Modern international migration flows | Free |

## Tier 4 — Ancient / deep-time genetics

Reaching back toward common descent and dispersal. Used in Phase 4.

| Source | What it provides | Notes |
| --- | --- | --- |
| **Allen Ancient DNA Resource (AADR)** | Harvard / Reich Lab; the large public ancient-DNA dataset | Free download |
| **Max Planck** genomes | Neanderthal & Denisovan genomes (archaic admixture) | Public |
| **ISOGG** Y-DNA tree | Y-chromosome haplogroup phylogeny | Free |
| **PhyloTree** | mtDNA haplogroup phylogeny | Free |
| **YFull** (YTree) | Y-DNA tree with age estimates | Free / freemium |

---

## Conventions

- **Cite everything.** Record source, access date, version, and license per dataset.
- **Respect licensing.** Census / IPUMS / AADR are openly usable; some require registration
  or specific citation language — capture those requirements alongside the data.
- **Mark interpretation.** Where a figure is derived or inferred rather than reported,
  label it as such (see the honesty note in `ROADMAP.md`).
