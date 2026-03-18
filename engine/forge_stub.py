"""
Forge Stub

Takes a discovery hypothesis and turns it into a very small
build proposal. This is the first executable step of Akasha Forge.
"""

from pathlib import Path
import json


class ForgeStub:
    def __init__(self, output_dir: str = "build_outputs"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def build_proposal(self, hypothesis: dict) -> dict:
        target = hypothesis.get("target", "unknown_target")
        gap_score = hypothesis.get("gap_score", 0.0)
        proposal = hypothesis.get("proposal", "")
        suggestions = hypothesis.get("suggestions", [])

        build_plan = {
            "target": target,
            "source_gap_score": gap_score,
            "source_proposal": proposal,
            "recommended_action": f"Create exploratory module for '{target}'",
            "repo_candidate": f"akasha-{target.lower().replace(' ', '-').replace('_', '-')}",
            "files_to_create": [
                "README.md",
                "repo-manifest.yaml",
                "NOTES.md"
            ],
            "next_steps": suggestions
        }

        return build_plan

    def save_build_plan(self, build_plan: dict) -> str:
        safe_name = build_plan["target"].lower().replace(" ", "_").replace("-", "_")
        output_file = self.output_dir / f"{safe_name}_build_plan.json"

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(build_plan, f, indent=2)

        return str(output_file)


if __name__ == "__main__":
    sample_hypothesis = {
        "target": "time_crystal",
        "gap_score": 0.9,
        "proposal": "Explore missing connections for 'time_crystal'",
        "suggestions": [
            "Link 'time_crystal' to adjacent domains",
            "Search for analogous structures in other fields",
            "Generate tool or model to bridge domain gap"
        ]
    }

    forge = ForgeStub()
    plan = forge.build_proposal(sample_hypothesis)
    path = forge.save_build_plan(plan)

    print("Build plan saved to:", path)
    print(json.dumps(plan, indent=2))
