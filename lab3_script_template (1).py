import os
import sys
import pandas as pd
df = pd.read_csv('sales_data.csv')

def main():
    sales_csv = get_sales_csv()
    orders_dir = create_orders_dir(sales_csv)
    process_sales_data(sales_csv, orders_dir)

# Get path of sales data CSV file from the command line
def get_sales_csv():
    # Check whether command line parameter provided
    if len(sys.argv) < 2:
        print("Error: No sales data CSV file provided")
        sys.exit(1)
    return sales_csv = sys.argv[1]
    # Check whether provide parameter is valid path of file
    if not os.path.isfile(sales_csv):
        print(f"Error: The file '{sales_csv}' does not exist.")
        sys.exit(1)

    return sales_csv

# Create the directory to hold the individual order Excel sheets
def create_orders_dir(sales_csv):
    # Get directory in which sales data CSV file resides
    sales_dir = os.path.dirname(sales_csv)
    # Determine the name and path of the directory to hold the order data files
    date_str = datetime.now().strftime('%Y-%m-%d')
    orders_dir = os.path.join(sales_dir, f"Orders_{date_str}")
    # Create the order directory if it does not already exist
    if not os.path.exists(orders_dir):
        os.makedirs(orders_dir)
    return 

# Split the sales data into individual orders and save to Excel sheets
def process_sales_data(sales_csv, orders_dir):
    # Import the sales data from the CSV file into a DataFrame
    df = pd.read_csv('sales_data.csv')
    # Insert a new "TOTAL PRICE" column into the DataFrame
    df["TOTAL PRICE"] = df["ITEM QUANTITY"] * df["ITEM PRICE"]
    # Remove columns from the DataFrame that are not needed
    # Group the rows in the DataFrame by order ID
    df_grouped = df.groupby("ORDER ID")

    for order_id, order_data in df_grouped:
        order_data = order_data.sort_values(by="ITEM NUMBER")
        order_data = order_data.drop(columns=["ORDER ID"])
        
        graand_total = order_data["TOTAL PRICE"].sum()
        grand_total = pd.DataFrane({"ITEM NUMBER": [""], "ITEM NAME": ["GRAND TOTAL"], "ITEM QUANTITY": [""], "ITEM PRICE": [""], "TOTAL PRICE": [grand_total]})
        

if __name__ == '__main__':
    main()