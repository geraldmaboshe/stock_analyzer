from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
import tools

@CrewBase
class StockAnalyzerCrew():
    """Stock analysis crew"""

    # Agent definitions
    @agent
    def web_scraper(self) ->Agent:
        return Agent(config=self.agents_config['web_scraper'], tools=[tools
            .web_scrape], verbose=True)
    
    @agent
    def stock_analyzer(self) -> Agent:
        return Agent(
            config=self.agents_config['stock_analyzer'],
            tools=[],
            verbose=True,
        )

    # Task definitions
    @task
    def scrape_site(self) ->Task:
        return Task(config=self.tasks_config['scrape_site'])
        
    @task
    def analyze_stocks(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_stocks'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Stock Analysis crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )