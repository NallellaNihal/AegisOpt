class Coordinator:
    def decide(self, profile, optimizations, security_issues):
        decision = {
            "safe": len(security_issues) == 0,
            "optimize": len(optimizations) > 0,
            "action": None
        }

        if not decision["safe"]:
            decision["action"] = "Fix security issues first"
        elif decision["optimize"]:
            decision["action"] = "Apply optimizations"
        else:
            decision["action"] = "Code is good"

        return decision