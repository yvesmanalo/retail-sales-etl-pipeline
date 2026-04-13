from etl.extract import extract
from etl.transform import transform

file_location = "data/raw"
file_name = "sales_data.csv"
new_column_name = "total_sales"

raw_data = extract(file_location=file_location,file_name=file_name)
transformed_data = transform(raw_data=raw_data, new_column_name=new_column_name)