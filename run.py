from sim import simulate, safety_case_tests
import csv, statistics, json
SEEDS = [11, 12, 13]  # Task 5 and Task 9 specify the same three seeds.
EXTRA_SEEDS = [14, 15]  # Included as supplementary checks from the fixed-settings table.

rows = []
for seed in SEEDS:
    rows.append(simulate(seed, "baseline"))
    rows.append(simulate(seed, "model"))
    rows.append(simulate(seed, "harbour_master", harbour_master=True))

with open("results.csv", "w", newline="", encoding="utf-8") as f:
    fields = ["seed","policy","cargo_delivered","storm_knockouts","invalid_outputs","fallback_uses","ships_arrived"]
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    for r in rows:
        writer.writerow({k:r[k] for k in fields})

print("PRIMARY RESULTS (seeds 11, 12, 13)")
for policy in ["baseline", "model", "harbour_master"]:
    subset = [r for r in rows if r["policy"] == policy]
    print(policy, {
        "average_cargo": round(statistics.mean(r["cargo_delivered"] for r in subset), 2),
        "average_knockouts": round(statistics.mean(r["storm_knockouts"] for r in subset), 2),
        "average_invalid": round(statistics.mean(r["invalid_outputs"] for r in subset), 2),
        "average_fallback": round(statistics.mean(r["fallback_uses"] for r in subset), 2)
    })

print("SUPPLEMENTARY SEEDS 14-15")
for seed in EXTRA_SEEDS:
    for policy in ["baseline", "model", "harbour_master"]:
        r = simulate(seed, policy if policy != "harbour_master" else "harbour_master",
                     harbour_master=(policy == "harbour_master"))
        print(seed, policy, r["cargo_delivered"], r["storm_knockouts"],
              r["invalid_outputs"], r["fallback_uses"])

print("SAFETY CASE TESTS")
print(json.dumps(safety_case_tests(), indent=2))
