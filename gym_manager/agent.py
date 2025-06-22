from google.adk.agents import Agent

from .config import MODEL
from .prompt import MANAGER_PROMPT
from .sub_agents.nutrition_agent.agent import nutrition_agent 
from .sub_agents.train_agent.agent import train_agent 

root_agent = Agent(
    name="gym_manager",
    model=MODEL,
    description="Managet Agent",
    instruction=MANAGER_PROMPT,
    sub_agents=[nutrition_agent, train_agent]
)
