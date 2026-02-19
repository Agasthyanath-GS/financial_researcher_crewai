from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from crewai_tools import SerperDevTool


@CrewBase
class research_crew():
    """FinancialResearcher crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def financial_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['financial_researcher'], 
            verbose=True, tools = [SerperDevTool()]
        )

    @agent
    def financial_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['financial_analyst'],
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(config=self.tasks_config['research_task'])

    @task
    def analysis_task(self) -> Task:
        return Task(config=self.tasks_config['analysis_task'])

    @crew
    def crew(self) -> Crew:
        """Creates the FinancialResearcher crew"""

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
