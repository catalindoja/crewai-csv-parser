from crewai import Task
from textwrap import dedent

class CSVParserTasks():
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"
    
    def parse_csv(self, agent, file):
        return Task(description=dedent(f"""
            Parse the CSV file {file} and provide the concise data.
            Your final answer must include the data but also, 
            include the number of rows and columns, the data types
            of each column, and any other relevant information.
            Make sure to use the most recent data as possible.
        """), agent=agent)

    def summarize_csv(self, agent, file):
        return Task(description=dedent(f"""
            Summarize the data in the CSV file {file}.
            Your final answer must include a summary of the data.
            Make sure to use the most recent data as possible.
        """), agent=agent)

    def analyze_csv(self, agent, file):
        return Task(description=dedent(f"""
            Analyze the data in the CSV file {file} and provide insights.
            Your final answer must include an analysis of the data
            including any trends, outliers, mean, deviations, correlations, or other
            patterns you observe in the data.
            Make sure to use the most recent data as possible.
        """), agent=agent)

