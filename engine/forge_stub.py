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
        gap_type = hypothesis.get("gap_type", "unknown")
        reason   = hypothesis.get("reason", "")
        proposal = hypothesis.get("proposal", "")
        suggestions = hypothesis.get("suggestions", [])

        # Only structural_sink defaults to repo creation.
        # isolated = needs human review before action.
        # sparse = observe, don't build yet.
        action_map = {
            "structural_sink": "propose_extension",
            "isolated":        "flag_for_review",
            "sparse":          "observe",
        }
        action = action_map.get(gap_type, "flag_for_review")

        build_plan = {
            "target": target,
            "gap_type": gap_type,
            "reason": reason,
            "gap_score": gap_score,
            "action": action,
            "source_proposal": proposal,
            "recommended_action": f"Create exploratory module for '{target}'" if action == "propose_extension" else f"Review '{target}' before materializing",
            "repo_candidate": f"akasha-{target.lower().replace(' ', '-').replace('_', '-')}" if action == "propose_extension" else None,
            "files_to_create": ["README.md", "repo-manifest.yaml", "NOTES.md"] if action == "propose_extension" else [],
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
