# test_forge_stub.py

from forge_stub import ForgeStub

hypothesis = {
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
plan = forge.build_proposal(hypothesis)
path = forge.save_build_plan(plan)

print(path)
print(plan)
