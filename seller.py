import time
import json
import random
from dotenv import load_dotenv
from virtuals_acp.client import VirtualsACP
from virtuals_acp.env import EnvSettings

load_dotenv()
env = EnvSettings()

def flip_coin(choice: str) -> dict:
    result = random.choice(["heads", "tails"])
    won = result == choice.lower()
    return {
        "result": result,
        "your_choice": choice,
        "outcome": "WIN" if won else "LOSE"
    }

def on_new_task(job):
    print(f"[JOB] Incoming: {job.id}")
    acp.respond_job(job.id, job.memo_id, accept=True, reason="Flip incoming!")

acp = VirtualsACP(
    wallet_private_key=env.WHITELISTED_WALLET_PRIVATE_KEY,
    agent_wallet_address=env.SELLER_AGENT_WALLET_ADDRESS,
    on_new_task=on_new_task
)

print("[COINFLIP] Agent running...")

while True:
    jobs = acp.get_active_jobs()
    for job in jobs:
        req = job.service_requirement
        # req schema: {"choice": "heads"} atau {"choice": "tails"}
        choice = req.get("choice", "heads")
        result = flip_coin(choice)
        acp.deliver_job(job.id, deliverable=json.dumps(result))
        print(f"[DONE] {result}")
    time.sleep(10)
