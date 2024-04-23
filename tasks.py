from crewai import Task
from textwrap import dedent

class CSVParserTasks():
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"
    
    def parse_csv(self, agent, file):
        return Task(description=dedent(f"""
            Parse the CSV file {file} and provide the concise data.
            {self.__tip_section()}
        """), agent=agent)

    def summarize_csv(self, agent):
        return Task(description=dedent(f"""
            Take the input from the parse_csv task and summarize the data.
            Your final answer must include the number of rows and columns,
            the data types of each column, and any other relevant information.
            {self.__tip_section()}
        """), agent=agent)

    def analyze_csv(self, agent):
        return Task(description=dedent(f"""
            Analyze the data provided by the parse_csv task.
            Your final answer must include an analysis of the data
            including how many names are in the data, the range of ages,
            the average age of the people, and any other relevant information.
        """), agent=agent)

