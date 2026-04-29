class SecurityAgent:
    def scan(self, code):
        issues = []

        if "eval(" in code:
            issues.append("Use of eval() is unsafe.")

        if "exec(" in code:
            issues.append("Use of exec() is unsafe.")

        if "pickle.load" in code:
            issues.append("Untrusted pickle deserialization risk.")

        return issues