import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from backend import run_travel_agent

user_input = input("Enter travel request: ")

respone = run_travel_agent(
    user_input=user_input,
    thread_id="test_user"
)

print("\n\nFINAL RESPONSE:\n")
print(respone["answer"])
