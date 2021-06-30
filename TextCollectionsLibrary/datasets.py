import pandas as pd
import os
from pathlib import Path

def load(path_files='', without_little_datasets = False, only_download = False):

  '''
  this function can download and load all datasets, and return a dictionary in which any key represent the dataset
  
  if the files already exist, to load them, pass the path where the files are through the path_files parameter
  
  when without_little_datasets parameter is True, the function don't download and load CSTR and SyskillWebert
  
  when only_download parameter is True, the function don't load the datasets (only download) 
  '''
  
  bases = {}
  
  if not without_little_datasets:
    if not Path(path_files +'CSTR.parquet').is_file():
      cmd = 'gdown --id 1-Q7VXXkdGGxIYmIDuotlN3sXNVy-RtYd -O ' + path_files + 'CSTR.parquet'
      os.system(cmd) # CSTR
      
    if not only_download:
      bases['CSTR'] = pd.read_parquet(path_files + 'CSTR.parquet')
    
    if not Path(path_files +'SyskillWebert.parquet').is_file():
      cmd = 'gdown --id 1-TVrAJjWxYizbvzMgXE2LYjhEfOlm5qE -O ' + path_files + 'SyskillWebert.parquet'
      os.system(cmd)  # SiskillWebert
     
    if not only_download:
      bases['SyskillWebert'] = pd.read_parquet(path_files + 'SyskillWebert.parquet')
 
  if not Path(path_files +'classic4.parquet').is_file():
    cmd = 'gdown --id 1-PrzCH0m5pp6cAMepylDImfMMjHMOAh7 -O ' + path_files + 'classic4.parquet'
    os.system(cmd) # Classic4
    
  if not only_download:
    bases['classic4'] = pd.read_parquet(path_files + 'classic4.parquet')
 
  if not Path(path_files +'webkb-parsed.parquet').is_file():
    cmd = 'gdown --id 1-Ss8VZNVqMe-_RqwZdDpVSZiuI6M_-xu -O ' + path_files + 'webkb-parsed.parquet'
    os.system(cmd)  # Webkb-parsed
    
  if not only_download:
    bases['webkb-parsed'] = pd.read_parquet(path_files + 'webkb-parsed.parquet')
  
  if not Path(path_files +'review_polarity.parquet').is_file():
    cmd = 'gdown --id 1-SR9H4S6RbUumRALpBRX2VbQURSuQbQp -O ' + path_files + 'review_polarity.parquet'
    os.system(cmd)  # Review_polarity
  
  if not only_download:
    bases['review_polarity'] = pd.read_parquet(path_files + 'review_polarity.parquet')
  
  if not Path(path_files +'re8.parquet').is_file():
    cmd ='gdown --id 1-TTx72T-l_nhdrQQYrjNqurOqwFgEco- -O ' + path_files + 're8.parquet'
    os.system(cmd)  # Re8
    
  if not only_download:
    bases['re8'] = pd.read_parquet(path_files + 're8.parquet')
  
  if not Path(path_files +'NSF.parquet').is_file():
    cmd = 'gdown --id 1-N-jktqPoprXwFYHILcWzM96mQwQc7xC -O ' + path_files + 'NSF.parquet'
    os.system(cmd)  # NSF
    
  if not only_download:
    bases['NSF'] = pd.read_parquet(path_files + 'NSF.parquet')
  
  if not Path(path_files +'Industry-Sector.parquet').is_file():
    cmd = 'gdown --id 1-TUiP3uSyt4PU5uqQKWytfhr6GbhyMFc -O ' + path_files + 'Industry-Sector.parquet'
    os.system(cmd)  # indrustry Sector
    
  if not only_download:
    bases['Industry-Sector'] = pd.read_parquet(path_files + 'Industry-Sector.parquet')
  
  if not Path(path_files +'Dmoz-Sports.parquet').is_file():
    cmd = 'gdown --id 1-RbTMId6T9HJXyUMHH9YXP0pcVl35cmU -O ' + path_files + 'Dmoz-Sports.parquet'
    os.system(cmd)  # Dmoz-Sports
  
  if not only_download:
    bases['Dmoz-Sports'] = pd.read_parquet(path_files + 'Dmoz-Sports.parquet')
  
  if not Path(path_files +'Dmoz-Science.parquet').is_file():
    cmd = 'gdown --id 1-Oou50qn2CKbDq0X7DRzM53OY-2zwysJ -O ' + path_files + 'Dmoz-Science.parquet'
    os.system(cmd)  # Dmoz-Science
  
  if not only_download:
    bases['Dmoz-Science'] = pd.read_parquet(path_files + 'Dmoz-Science.parquet')
 
  if not Path(path_files +'Dmoz-Health.parquet').is_file():
    cmd = 'gdown --id 1-QKNia6LYMQ8d5RmiS4wzEjj7bo__Hsc -O ' + path_files + 'Dmoz-Health.parquet'
    os.system(cmd)  # Dmoz-Health
  
  if not only_download:
    bases['Dmoz-Health'] = pd.read_parquet(path_files + 'Dmoz-Health.parquet')
  
  if not Path(path_files +'Dmoz-Computers.parquet').is_file():
    cmd = 'gdown --id 1-QEkqxFTizvHaOlKp6UEmecC-8tboJMK -O ' + path_files + 'Dmoz-Computers.parquet'
    os.system(cmd)  # Dmoz-Computers

  if not only_download:
    bases['Dmoz-Computers'] = pd.read_parquet(path_files + 'Dmoz-Computers.parquet')
  
  if not only_download:
    return bases
