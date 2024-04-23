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
            verbose=True,
            tools=[
                CSVParserTools.parse_csv
            ],
            llm=self.llm
        )

    def csv_summarizer(self):
        return Agent(
            role='CSV Summarizer',
            goal="""Summarize the data in a CSV file and provide the summary of the data including the number of rows and columns, the data types of each column, and any other relevant information.""",
            backstory="""You are a data analyst with a lot of experience in summarizing data""",
            verbose=True,
            tools=[
                CSVParserTools.summarize_data
            ],
            llm=self.llm
        )
    
    def csv_analyzer(self):
        return Agent(
            role='CSV Analyzer',
            goal="""Analyze the data in a CSV file and if you find columns that are full of numbers, calculate the sum, average, and standard deviation of those columns. If you find columns that are full of text, calculate the word count, character count, and average word length of those columns. If you find columns that are full of dates, calculate the number of days between the earliest and latest dates in those columns.""",
            backstory="""You are a data analyst with a lot of experience in analyzing data""",
            verbose=True,
            tools=[
                CSVParserTools.analyze_data
            ],
            llm=self.llm
        )