def load(transformed_data,processed_filename,processed_file_location):
  transformed_data.to_csv(f"{processed_file_location}/{processed_filename}", sep= "|", index = False)
  print(
  f"""
  \n
  [Load phase]
  File saved successfully:
  {processed_file_location}/{processed_filename}
  \n
  """
  )
