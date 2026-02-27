import json

class Writer:
    def __init__(self, output, verbose=False):
        self.output = output
        self.data = []
        self.verbose = verbose

    def add(self, record):
        self.data.append(record)

        if self.verbose:
            print(f"[RECORDED] {record['url']}")

    def save(self):
        with open(self.output, "w") as f:
            json.dump(self.data, f, indent=2)

        print(f"\n[✓] Results saved to {self.output}")
