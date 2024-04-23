from crewai import Crew
from textwrap import dedent

from agents import CSVParserAgents
from tasks import CSVParserTasks
from dotenv import load_dotenv

load_dotenv()


class CSVParserCrew:
    def __init__(self, file_path):
        self.file_path = file_path

    def run(self):
        agents = CSVParserAgents()
        tasks = CSVParserTasks()

        csv_parser_agent = agents.csv_parser()
        summarize_data_agent = agents.csv_summarizer()
        #analyze_data_agent = agents.csv_analyzer()

        parse_csv_task = tasks.parse_csv(csv_parser_agent, self.file_path)
        summarize_data_task = tasks.summarize_csv(summarize_data_agent)
        #analyze_data_task = tasks.analyze_csv(analyze_data_agent)

        crew = Crew(
            agents=[
                csv_parser_agent,
                summarize_data_agent,
                #analyze_data_agent
            ],
            tasks=[
                parse_csv_task,
                summarize_data_task,
                #analyze_data_task
            ],
            verbose=True
        )

        result = crew.kickoff()
        return result
    
if __name__ == "__main__":
    print("## Welcome to CSV Parser Crew")
    print('-------------------------------')
    print("## Let's start the process")
    csv_parser_crew = CSVParserCrew("./example.csv")
    result = csv_parser_crew.run()
    print("\n\n########################")
    print("## Here is the Report")
    print("########################\n")
    print(result)