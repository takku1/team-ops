import hashlib, json, sys
sys.path.insert(0, "Z:/SkillWren/src")
from skillwren.review import validate_review
d = sys.argv[1]
spec = json.load(open(f"{d}/review-spec.json", encoding="utf-8"))
orig = open(f"{d}/original.md", "rb").read(); cand = open(f"{d}/SKILL.md", "rb").read()
h = lambda b: hashlib.sha256(b).hexdigest()
review = {"original_sha256": h(orig), "logic_sha256": h(cand),
          "review": "Manual conversion review (prose v2 -> SkillWren 0.5). Anchors check bookkeeping, not semantic parity.",
          "requirements": [{"id": i, "original_lines": s, "logic_contains": a} for i, s, a in spec]}
text = cand.decode("utf-8-sig")
bad = [(i, x) for i, s, a in spec for x in a if x not in text]
if bad: print("MISSING ANCHORS:", bad); sys.exit(1)
print(validate_review({"original.md": orig}, cand, cand, review))
json.dump(review, open(f"{d}/review.json", "w", encoding="utf-8"), indent=1)
