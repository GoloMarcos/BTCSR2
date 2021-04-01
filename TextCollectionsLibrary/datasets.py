import pandas as pd
import os
from pathlib import Path

def load(path_files=''):

  '''
  this function download and load all datasets and return a dictionary in which any key represent the dataset
  
  if the files already exist, to load them, pass the path where the files are through the path_files parameter
  
  this function changes the current directory, remember to go back to the directory you were in
  '''

  os.chdir(path_files)

  if not Path('CSTR.parquet').is_file():
    os.system('gdown --id 1-Q7VXXkdGGxIYmIDuotlN3sXNVy-RtYd') # CSTR

  if not Path('classic4.parquet').is_file():
    os.system('gdown --id 1-PrzCH0m5pp6cAMepylDImfMMjHMOAh7') # Classic4
  
  if not Path('SyskillWebert.parquet').is_file():
    os.system('gdown --id 1-TVrAJjWxYizbvzMgXE2LYjhEfOlm5qE')  # SiskillWebert
  
  if not Path('webkb-parsed.parquet').is_file():
    os.system('gdown --id 1-Ss8VZNVqMe-_RqwZdDpVSZiuI6M_-xu')  # Webkb-parsed
  
  if not Path('review_polarity.parquet').is_file():
    os.system('gdown --id 1-SR9H4S6RbUumRALpBRX2VbQURSuQbQp')  # Review_polarity
  
  if not Path('re8.parquet').is_file():
    os.system('gdown --id 1-TTx72T-l_nhdrQQYrjNqurOqwFgEco-')  # Re8
  
  if not Path('NSF.parquet').is_file():
    os.system('gdown --id 1-N-jktqPoprXwFYHILcWzM96mQwQc7xC')  # NSF
  
  if not Path('Industry-Sector.parquet').is_file():
    os.system('gdown --id 1-TUiP3uSyt4PU5uqQKWytfhr6GbhyMFc')  # indrustry Sector
  
  if not Path('Dmoz-Sports.parquet').is_file():
    os.system('gdown --id 1-RbTMId6T9HJXyUMHH9YXP0pcVl35cmU')  # Dmoz-Sports
  
  if not Path('Dmoz-Science.parquet').is_file():
    os.system('gdown --id 1-Oou50qn2CKbDq0X7DRzM53OY-2zwysJ')  # Dmoz-Science
  
  if not Path('Dmoz-Health.parquet').is_file():
    os.system('gdown --id 1-QKNia6LYMQ8d5RmiS4wzEjj7bo__Hsc')  # Dmoz-Health
  
  if not Path('Dmoz-Computers.parquet').is_file():
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
