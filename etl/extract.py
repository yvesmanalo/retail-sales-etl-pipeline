import pandas as pd

def extract(file_location,file_name):
  
  df = pd.read_csv(f"{file_location}/{file_name}")
  df_shape = df.shape
  print(
  f"""
  \n
  [Extract phase]
  Rows: {df_shape[0]} | Columns: {df_shape[1]}
  \n
  Preview:
  {df.head()}
  """
  )

  return df