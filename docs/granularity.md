# Granularity Strategy

The project moves macro → micro, but the trap is picking one fixed resolution: too coarse
and the data is mush, too fine and it's noise before we can read it. So we don't pick one
resolution — we pick a **default altitude** and a **rule for drilling down**.

## Default altitude: state → metro → county-on-demand

1. **State (50 + DC)** — the baseline skeleton (Phase 1). Coarse enough to stay macro, but
   it shows the big regional structure immediately (the South, the Southwest, the industrial
   Midwest, etc.). Start here.
2. **Metro area (CBSA, ~390)** — the natural second cut, and the sweet spot for this
   project. Populations concentrate in metros, and so do culture and economics — distinct
   communities (Irish Boston, German Midwest, Cuban Miami) show up at metro level, not state
   level.
3. **County (~3,100)** — held in reserve. At county level, small populations hit Census
   suppression and large margins of error; going county-wide drowns the signal in noise.

## The rule: drill down only where it naturally breaks apart

Stay at state/metro by default. Drop to **county only for the specific communities that
prove interesting** — let the data show where to zoom rather than pre-committing to maximum
granularity everywhere. This is the practical form of *reading the macro through the micro*:
surgical drill-downs, not a uniform high-resolution grid.

## Why this avoids both failure modes

- Never **so general it's useless** — state+metro already exposes real structure.
- Never **so granular it's noise** — county detail is added only where there's a question
  that needs it and enough population to answer it reliably.
