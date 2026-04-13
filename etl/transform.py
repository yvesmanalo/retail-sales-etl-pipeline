import pandas as pd

def transform(raw_data, new_column_name):

  transformed_data = raw_data
  transformed_data[new_column_name] = transformed_data["price"] * transformed_data["quantity"]

  if(transformed_data.duplicated().any()):
    transformed_data.drop_duplicates()

  transformed_data = transformed_data.loc[:,["order_id","order_date","region","total_sales"]]
  transformed_data["region"] = transformed_data["region"].apply(lambda region: region.upper())
  transformed_data["order_date"] = pd.to_datetime(transformed_data["order_date"], format="%Y-%m-%d")
  transformed_data = transformed_data.sort_values(by="order_date")

  print(
  f"""
  \n
  [Transform phase]
  New column added: {new_column_name}
  \n
  Preview:
  {transformed_data.head()}
  """
  )
  return transformed_data