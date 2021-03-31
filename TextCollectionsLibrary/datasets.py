import pandas as pd
import os

def load():

  '''
  load all datasets and return a dictionary in which any key represent the dataset
  '''
  os.system('gdown --id 1-Q7VXXkdGGxIYmIDuotlN3sXNVy-RtYd') # CSTR
  os.system('gdown --id 1-PrzCH0m5pp6cAMepylDImfMMjHMOAh7') # Classic4
  os.system('gdown --id 1-TVrAJjWxYizbvzMgXE2LYjhEfOlm5qE')  # SiskillWebert
  os.system('gdown --id 1-Ss8VZNVqMe-_RqwZdDpVSZiuI6M_-xu')  # Webkb-parsed
  os.system('gdown --id 1-SR9H4S6RbUumRALpBRX2VbQURSuQbQp')  # Review_polarity
  os.system('gdown --id 1-TTx72T-l_nhdrQQYrjNqurOqwFgEco-')  # Re8
  os.system('gdown --id 1-N-jktqPoprXwFYHILcWzM96mQwQc7xC')  # NSF
  os.system('gdown --id 1-TUiP3uSyt4PU5uqQKWytfhr6GbhyMFc')  # indrustry Sector
  os.system('gdown --id 1-RbTMId6T9HJXyUMHH9YXP0pcVl35cmU')  # Dmoz-Sports
  os.system('gdown --id 1-Oou50qn2CKbDq0X7DRzM53OY-2zwysJ')  # Dmoz-Science
  os.system('gdown --id 1-QKNia6LYMQ8d5RmiS4wzEjj7bo__Hsc')  # Dmoz-Health
  os.system('gdown --id 1-QEkqxFTizvHaOlKp6UEmecC-8tboJMK')  # Dmoz-Computers

  bases = {
    'NSF' : pd.read_parquet('NSF.parquet'),
    'Dmoz-Science' : pd.read_parquet('Dmoz-Science.parquet'),
    'classic4' : pd.read_parquet('classic4.parquet'),
    'CSTR' : pd.read_parquet('CSTR.parquet'),
    'Dmoz-Computers' : pd.read_parquet('Dmoz-Computers.parquet'),
    'Dmoz-Health' : pd.read_parquet('Dmoz-Health.parquet'),
    'Dmoz-Sports' : pd.read_parquet('Dmoz-Sports.parquet'),
    'review_polarity' : pd.read_parquet('review_polarity.parquet'),
    'webkb-parsed' : pd.read_parquet('webkb-parsed.parquet'),
    're8' : pd.read_parquet('re8.parquet'),
    'Industry-Sector' : pd.read_parquet('Industry-Sector.parquet'),
    'SyskillWebert' : pd.read_parquet('SyskillWebert.parquet')
  }

  return bases