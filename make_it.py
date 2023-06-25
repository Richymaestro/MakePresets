import time
from dataclasses import dataclass
from dataclasses_json import dataclass_json

from roless.roles_v1 import ScopeAllowFunction

@dataclass_json
@dataclass
class Transaction:
    to: str
    data: list
    value: str = "0"

    def create_transactions(self) -> list[dict]:
        transactions = [{'to': self.to, 'data': d, 'value': self.value} for d in self.data]
        return transactions

@dataclass_json
@dataclass
class Meta:
    name: str = "kpk"
    description: str = "karpatkey test"
    txBuilderVersion: str = "1.8.0"

@dataclass_json
@dataclass
class Root:
    chainId: str
    meta: Meta
    transactions: list[Transaction]
    version: str = "1.0"
    createdAt: int = int(time.time() * 1000)

CHAINID = 100
META = Meta()
TO = "0xB6CeDb9603e7992A5d42ea2246B3ba0a21342503"
DATA = [ScopeAllowFunction(1,"0xae7ab96520DE3A18E5e111B5EaAb095312D7fE84","0xa1903eab",0).data
        ]
TRANSACTIONS = Transaction(TO,DATA).create_transactions()

# Create an instance of the Root class with the provided values
root = Root(
    chainId=CHAINID,
    meta=META,
    transactions=TRANSACTIONS
)

# Convert the dataclass instance to JSON
json_data = root.to_json()

# Save the JSON data to a file
with open("output.json", "w") as file:
    file.write(json_data)

print("JSON data saved to output.json")
