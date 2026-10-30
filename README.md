# Stormwatch Harbour — CGD-460 Assignment 2

## Requirements
- Python 3.10 or newer
- No third-party packages are required to run the simulation.

## Run
From this folder:
```bash
python run.py
```
Run one policy for one seed:
```bash
python sim.py --seed 11 --policy baseline
python sim.py --seed 11 --policy model
python sim.py --seed 11 --policy harbour_master
```

## Implementation notes
- Grid: 24 columns × 16 rows; warehouse at (0, 15); berths B1–B4 at (3,0), (9,0), (15,0), (21,0).
- Ten dockworkers, eight cargo units per ship, three 15-tick storms, 600 ticks per run.
- All simulation randomness is derived from the run seed. Storm timing uses a separate deterministic stream derived from that seed.
- Baseline workers choose the nearest ship without remembering storm warnings. Model-based workers remember Lookout warnings and avoid B1/B4 from warning time through the end of the storm.
- Harbour Master uses an offline deterministic mock advisory so the assignment can be run without an API key. Its output is validated against the strict action allow-list. Invalid output is rejected and the model-based policy is used for that tick.
- `run.py` evaluates seeds 11–13 as explicitly requested in Tasks 5 and 9, and additionally prints seeds 14–15 because the fixed-settings table lists 11–15.
- `safety_case_tests()` tests manifest prompt injection and an unauthorised harbour-closure request. Cases 3 and 4 are discussed in the report as additional required safe behaviours.
