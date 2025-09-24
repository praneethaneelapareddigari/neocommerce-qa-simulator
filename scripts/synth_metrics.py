import csv, sys, random, datetime, math
def main(out_path):
    start = datetime.datetime.now() - datetime.timedelta(days=30)
    with open(out_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["timestamp","txn_accuracy","p95_latency_ms","defect_leakage"])
        acc, leak = 0.96, 0.08
        for h in range(30*24):
            t = start + datetime.timedelta(hours=h)
            acc = min(0.999, max(0.92, acc + random.uniform(-0.003,0.004)))
            leak = max(0.01, leak - 0.0005 + random.uniform(-0.002,0.002))
            p95 = int(240 + 40*math.sin(h/8.0) + random.uniform(-30,25))
            w.writerow([t.isoformat(timespec='seconds'), f"{acc:.3f}", p95, f"{leak:.3f}"])
    print(f"Wrote {out_path}")
if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv)>1 else "metrics.csv"
    main(path)
