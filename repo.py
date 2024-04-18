from langchain_anthropic import ChatAnthropic
from crewai import Crew, Process, Agent
from dotenv import load_dotenv
import os
os.environ["ANTHROPIC_API_KEY"] ="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"
Nutritionist = Agent(
    role='Nutritionist',
    goal=f'prescribe healthy meal plan',
    backstory=f""" you are an expert nutritonist""",
    verbose=False,
    allow_delegation=True,
    max_rpm=5,
    llm=ChatAnthropic(model="claude-3-sonnet-20240229", max_tokens=4069)
)



from crewai import Task

# Install duckduckgo-search for this example:
# !pip install -U duckduckgo-search

from langchain_community.tools import DuckDuckGoSearchRun
search_tool = DuckDuckGoSearchRun()


diet_task = Task(
    description=f"""a balanced diet meal plan """,
    expected_output=f"""  300 words maximum, a healthy meal plan""",
    output_file='diet_report4.docx',
)


from crewai import Crew, Process, Agent


project_crew = Crew(
    tasks=[diet_task], # Tasks that that manager will figure out how to complete
    agents=[Nutritionist], # Agents that will be assigned to complete the tasks
    manager_llm=ChatAnthropic(temperature=1, model="claude-3-sonnet-20240229", max_tokens=4069 ), # The manager's LLM that will be used internally
    max_rpm=4,  # The maximum RPM for the project
    process=Process.hierarchical  # Designating the hierarchical approach
)

result = project_crew.kickoff()
print(result)
