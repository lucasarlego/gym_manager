from google.adk.agents import Agent

from ...config import MODEL 
from ...prompt import NUTRITION_PROMPT
from .tools.imc_calculator import imc_calculator
from .tools.water_per_day import water_per_day
from .tools.creatine_calculator import creatine_calculator
from .tools.tmb_calculator import tmb_calculator
from .tools.protein_calculator import protein_calculator

nutrition_agent = Agent(
    name="nutrition_agent",
    model=MODEL,
    description="Nutrition Agent",
    instruction=NUTRITION_PROMPT,
    tools=[imc_calculator, water_per_day, creatine_calculator, tmb_calculator, protein_calculator]
)