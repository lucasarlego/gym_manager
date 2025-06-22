from google.adk.agents import Agent

from ...config import MODEL 
from ...prompt import TRAIN_PROMPT

train_agent = Agent(
    name="train_agent",
    model=MODEL,
    description="Train Agent",
    instruction=TRAIN_PROMPT,
    #tools=[]
)