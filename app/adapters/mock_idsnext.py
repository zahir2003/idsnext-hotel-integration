import json
from pathlib import Path

from app.adapters.base import PMSAdapter

DATA_FILE = Path(__file__).resolve().parents[2] / "data" / "sample_data.json"


class MockIDSNextAdapter(PMSAdapter):

    def get_data(self, resource: str):
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        if resource not in data:
            raise ValueError(f"Unknown resource: {resource}")

        return data[resource]
