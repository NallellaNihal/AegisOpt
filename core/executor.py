import time

class Executor:
    def run(self, code):
        start = time.time()
        exec(code, {"__builtins__": {"print": print}})
        end = time.time()

        return {
            "execution_time": end - start
        }