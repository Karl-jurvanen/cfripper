from cfripper.config.filter import Filter
from cfripper.model.enums import RuleMode

FILTERS = [
    Filter(
        rule_mode=RuleMode.WHITELISTED,
        eval={
            "and": [
                {"eq": [{"ref": "config.stack_name"}, "mockstack"]},
                {"eq": [{"ref": "logical_id"}, "RootRoleOne"]},
            ]
        },
        rules={"CrossAccountTrustRule"},
    )
]
