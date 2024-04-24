from crewai import Task
from textwrap import dedent

class CSVParserTasks():
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"
    
    def parse_csv(self, agent, file):
        return Task(description=dedent(f"""
            Parse the CSV file {file} and then return the data so that other agents can use it.
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

    def count_males_from_titanic(self, agent, file_path):
        return Task(
            description=dedent(f"""
                Count the number of males that are present in the data of the CSV file {file_path}. 
                {self.__tip_section()}
            """),
            expected_output=dedent("""\
                The number of males in the data"""), 
            agent=agent
        )
    
    def count_females_from_titanic(self, agent, file_path):
        return Task(
            description=dedent(f"""
                Count the number of females that are present in the data of the CSV file {file_path}.
                {self.__tip_section()}
            """),
            expected_output=dedent("""\
                The number of females in the data"""),
            agent=agent
        )
    
    def print_results(self, agent):
        return Task(
            description=dedent(f"""
                Print the results from the previous tasks.
                {self.__tip_section()}
            """), 
            expected_output=dedent("""\
                Print the results in the format: first line print the number of males and in the second line print the number of females."""),
            agent=agent
        )