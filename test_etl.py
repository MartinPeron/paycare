import etl
import pandas as pd

def test_extract():
  input_file = 'data/input_data.csv'
  data = etl.extract_data(input_file)
  assert data


def test_transform():
  data = pd.Dataframe({
    'salary': [50, None]
  })
  transformed_data = etl.transform_data(data)
  assert transformed_data == pd.Dataframe({
    'salary': [50],
    'tax': [5],
    'next_salary': [45],
  })
  
