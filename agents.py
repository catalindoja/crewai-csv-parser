from crewai import Agent
from langchain_openai import ChatOpenAI
from tools.csv_parser_tools import CSVParserTools

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
            goal="""Print the results of the previous agents. You will need to take the output from the count_males agent and the output from the count_females agent and 
            print it in the format Line 1: Number of males, Line 2: Number of females.""",
            backstory="""You are a data analyst with a lot of experience in printing results. You have enough memory to remember the results from the previous agents.""",
            allow_delegation=False,
            verbose=True,
            llm=self.llm
        )