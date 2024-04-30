from langchain.tools import tool
import os
import csv
import json
import numpy as np


def males(file_path):
  with open("./" + file_path, 'r') as file:
    data = [line.strip().split(',') for line in file.readlines()]
  return len([row for row in data if row[5] == 'male'])


def females(file_path):
  with open("./" + file_path, 'r') as file:
    data = [line.strip().split(',') for line in file.readlines()]
  return len([row for row in data if row[5] == 'female'])

class CSVParserTools():

  @tool("Parse a CSV file")
  def parse_csv(csv_file):
    """Parse a CSV file and return the data in a list of lists"""
    with open(csv_file, 'r') as file:
      return [line.strip().split(',') for line in file.readlines()]

  @tool("Summarize the data")
  def summarize_data(data):
    """Summarize the data in a list of lists"""
    return {
      'num_rows': len(data),
      'num_columns': len(data[0]),
      'data': data
    }

  @tool("Analyze the data")
  def analyze_data(data):
    """Analyze the data in a list of lists"""
    return {
      'num_rows': len(data),
      'num_columns': len(data[0]),
      # the age is the column 3 of the file
      'average__age': sum([float(row[2]) for row in data]) / len(data),
      'median_age': sorted([float(row[2]) for row in data])[len(data) // 2] if len(data) % 2 == 1 else (sorted([float(row[2]) for row in data])[len(data) // 2 - 1] + sorted([float(row[2]) for row in data])[len(data) // 2]) / 2,
      'data': data
    }
  
  @tool("Count males from the provided file data")
  def count_males_from_titanic(file_path):
    """Count the number of people that are males in the data"""
    with open("./" + file_path, 'r') as file:
      data = [line.strip().split(',') for line in file.readlines()]
    return len([row for row in data if row[5] == 'male'])
  

  @tool("Count females from the provided file data")
  def count_females_from_titanic(file_path):
    """Count the number of people that are females in the data"""
    with open("./" + file_path, 'r') as file:
      data = [line.strip().split(',') for line in file.readlines()]
    return len([row for row in data if row[5] == 'female'])

  @tool("Count people from the provided file data")
  def count_people_from_titanic(file_path):
    """Count the number of people that are males and females in the data"""
    with open("./" + file_path, 'r') as file:
      data = [line.strip().split(',') for line in file.readlines()]
      nr_females = len([row for row in data if row[5] == 'female'])
      nr_males = len([row for row in data if row[5] == 'male'])
      output = f"The number of males is: {nr_males} and the number of females is: {nr_females}."
    return output

  @tool("Count people from the provided file data")
  def composed_tool(file_path):
    """Count the number of people that are males and females in the CSV file"""
    nr_males = males(file_path)
    nr_females = females(file_path)
    output = f"The number of males is: {nr_males} and the number of females is: {nr_females}."
    return output
