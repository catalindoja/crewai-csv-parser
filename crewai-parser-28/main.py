from crewai import Crew
from textwrap import dedent

from agents import CSVParserAgents
from tasks import CSVParserTasks
from dotenv import load_dotenv

import os

load_dotenv()


class CSVParserCrew:
    def __init__(self, file_path):
        self.file_path = file_path

    def run(self):
        agents = CSVParserAgents()
        tasks = CSVParserTasks()

        #csv_parser_agent = agents.csv_parser()
        #summarize_data_agent = agents.csv_summarizer()
        #analyze_data_agent = agents.csv_analyzer()
        #count_males_agent = agents.count_males()
        #count_females_agent = agents.count_females()
        #print_results_agent = agents.results_printer()
        people_counter_agent = agents.composed_agent()
        ()

        #parse_csv_task = tasks.parse_csv(csv_parser_agent, self.file_path)
        #summarize_data_task = tasks.summarize_csv(summarize_data_agent)
        #analyze_data_task = tasks.analyze_csv(analyze_data_agent)
        #count_males_task = tasks.count_males_from_titanic(count_males_agent, self.file_path)
        #count_females_task = tasks.count_females_from_titanic(count_females_agent, self.file_path)
        #print_results_task = tasks.print_results(print_results_agent)
        #ount_people_task = tasks.count_people(people_counter_agent, self.file_path)
        composed_task = tasks.composed_task(people_counter_agent, self.file_path)

        crew = Crew(
            agents=[
                #csv_parser_agent,
                #summarize_data_agent,
                #analyze_data_agent
                #count_males_agent,
                #count_females_agent,
                #print_results_agent
                people_counter_agent
            ],
            tasks=[
                #parse_csv_task,
                #summarize_data_task,
                #analyze_data_task
                #count_males_task,
                #count_females_task,
                #print_results_task
                #count_people_task
                composed_task
            ],
            verbose=True
        )

        result = crew.kickoff()
        return result
    
if __name__ == "__main__":
    print("## Welcome to CSV Parser Crew")
    print('-------------------------------')
    print("## Let's start the process")
    path_str = "./titanic.csv"
    path = os.path.normpath(path_str)
    csv_parser_crew = CSVParserCrew(path)
    result = csv_parser_crew.run()
    print("\n\n########################")
    print("## Here is the Report")
    print("########################\n")
    print(result)