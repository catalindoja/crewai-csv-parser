from crewai import Agent
from langchain_openai import ChatOpenAI
from tools.csv_parser_tools import CSVParserTools
from crewai_tools import FileReadTool


file_read_tool = FileReadTool(file_path='./titanic.csv')

class CSVParserAgents():
    def __init__(self):
        self.llm = ChatOpenAI(
            model="crewai-mistral",
            base_url="http://localhost:11434/v1",
            api_key="NA"
        )

    def csv_parser(self):
        return Agent(
            role='CSV Parser',
            goal="""Parse a CSV file and provide the data""",
            backstory="""You are a data analyst with a lot of experience in parsing CSV files and providing the data in a concise manner""",
            allow_delegation=False,
            verbose=True,
            llm=self.llm,
            tools=[
                CSVParserTools.parse_csv
            ]
        )

    def csv_summarizer(self):
        return Agent(
            role='CSV Summarizer',
            #goal="""Summarize the data in a CSV file and provide the summary of the data including the number of rows and columns, the data types of each column, and any other relevant information.""",
            goal = """Summarize the data in a CSV file and provide the summary of the data using the summarize_data tool.""",
            backstory="""You are a data analyst with a lot of experience in summarizing data""",
            allow_delegation=False,
            verbose=True,
            llm=self.llm,
            tools=[
                CSVParserTools.summarize_data
            ]
        )
    
    def csv_analyzer(self):
        return Agent(
            role='CSV Analyzer',
            goal="""Analyze the data in a CSV file and if you find columns that are full of numbers, calculate the sum, average, and standard deviation of those columns. If you find columns that are full of text, calculate the word count, character count, and average word length of those columns. If you find columns that are full of dates, calculate the number of days between the earliest and latest dates in those columns.""",
            backstory="""You are a data analyst with a lot of experience in analyzing data""",
            allow_delegation=False,
            verbose=True,
            llm=self.llm,
            tools=[
                CSVParserTools.analyze_data
            ]
        )
    
    def count_males(self):
        return Agent(
            role='Male counter',
            goal="""Count the number of males in the data.""",
            tools=[
                CSVParserTools.count_males_from_titanic
            ],
            backstory="""You are a data analyst with a lot of experience in counting people.""",
            allow_delegation=False,
            verbose=True,
            llm=self.llm
        )
    
    def count_females(self):
        return Agent(
            role='Female counter',
            goal="""Count the number of females in the data.""",
            tools=[
                CSVParserTools.count_females_from_titanic
            ],
            backstory="""You are a data analyst with a lot of experience in counting people.""",
            allow_delegation=False,
            verbose=True,
            llm=self.llm
        )

    def results_printer(self):
        return Agent(
            role='Results Printer',
            goal="""Print the results of the analysis. More explicitly, the number of males in one line and then the number of females in the next line.""",
            backstory="""You are a data analyst with a lot of experience in printing results.""",
            allow_delegation=False,
            verbose=True,
            llm=self.llm
        )

    def people_counter(self):
        return Agent(
            role='People counter',
            goal="""Count the number of people in the data and then return the result.""",
            tools=[
                #CSVParserTools.count_people_from_titanic
                CSVParserTools.composed_tool
            ],
            backstory="""You are a data analyst with a lot of experience in counting people.""",
            allow_delegation=False,
            verbose=True,
            llm=self.llm
        )


    def composed_agent(self):
        return Agent(
            role='Composed Agent',
            goal="""Count the number of people in the data and then return the result.""",
            tools=[
                file_read_tool,
                CSVParserTools.count_males_from_titanic,
                CSVParserTools.count_females_from_titanic
            ],
            backstory="""You are a data analyst with a lot of experience in counting people.""",
            allow_delegation=False,
            verbose=True,
            llm=self.llm
        )