import time
from dotenv import load_dotenv
from virtuals_acp.client import VirtualsACP
from virtuals_acp.env import EnvSettings

load_dotenv()
env = EnvSettings()

acp = VirtualsACP(
    wallet_private_key=env.WHITELISTED_WALLET_PRIVATE_KEY,
    agent_wallet_address=env.BUYER_AGENT_WALLET_ADDRESS
)

agents = acp.browse_agents(keyword="CoinflipAgent", rerank=True, top_k=1)
seller = agents[0]
offering = seller.offerings[0]

job_id = offering.initiate_job(
    service_requirement={"choice": "heads"},
    expired_at=int(time.time()) + 3600,
    evaluator_address=env.BUYER_AGENT_WALLET_ADDRESS
)
print(f"Job initiated: {job_id}")
