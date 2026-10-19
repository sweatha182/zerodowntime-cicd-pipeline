
def migration_plan(old_schema_supported, new_schema_validated):
    """Plan a safe expand-contract database migration."""
    if not new_schema_validated:
        return {
            "phase": "expand",
            "action": "stop",
            "safe_to_continue": False,
        }

    if not old_schema_supported:
        return {
            "phase": "contract",
            "action": "remove_old_schema",
            "safe_to_continue": True,
        }

    return {
        "phase": "expand",
        "action": "add_new_schema_keep_old",
        "safe_to_continue": True,
    }


if __name__ == "__main__":
    print(migration_plan(True, True))
    print(migration_plan(False, True))
    print(migration_plan(True, False))
