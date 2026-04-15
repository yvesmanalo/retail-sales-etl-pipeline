from etl.extract import extract
from etl.transform import transform
from etl.load import load

file_location = "data/raw"
file_name = "sales_data.csv"
new_column_name = "total_sales"
processed_data_file_location = "./data/processed"
processed_data_file_name = "cleaned_sales_data.csv"

raw_data = extract(file_location=file_location,file_name=file_name)
transformed_data = transform(raw_data=raw_data, new_column_name=new_column_name)
cleaned_sales_data = load(transformed_data=transformed_data,processed_filename=processed_data_file_name,processed_file_location=processed_data_file_location)