class OptimizerAgent:
    def suggest(self, profile):
        suggestions = []

        if profile["loops"] > 2:
            suggestions.append("Consider reducing nested loops or using vectorization.")

        if profile["functions"] == 0:
            suggestions.append("Break code into reusable functions.")

        return suggestions