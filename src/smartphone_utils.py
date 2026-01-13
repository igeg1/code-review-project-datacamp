import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def prepare_smartphone_data(file_path):
    """
    Prepare smartphone data for visualization.

    Reads a CSV file, cleans missing values in specific columns, 
    and converts the price to a standard dollar format.

    :param file_path: The path to the raw smartphone CSV data.
    :return: A cleaned pandas DataFrame.
    """
    
    # Check if file exists
    if os.path.exists(file_path):
        raw_data = pd.read_csv(file_path)  
    else:
        raise Exception(f"File containing smartphone data not found at path {file_path}")

    # Define and filter columns
    columns_to_keep = [
        "brand_name",
        "os",
        "price",
        "avg_rating",
        "processor_speed",
        "battery_capacity",
        "screen_size"
    ]
    trimmed_data = raw_data[columns_to_keep]
    
    # Remove records without a battery_capacity or os value
    reduced_data = trimmed_data.dropna(subset = ["battery_capacity", "os"]).copy()
    
    # Transform price from cents to dollars 
    reduced_data["price"] = reduced_data["price"] / 100

    return reduced_data


# Call the function
cleaned_data = prepare_smartphone_data("./data/smartphones.csv")


def column_to_label(column_name):
    """
    Converts a column name in a pandas DataFrame to a string that can be
    used as a label in a plot.
    
    :param column_name: string containing original column name
    :return: string that is ready to be presented on a plot
    """
    
    # Validate that column_name is a string
    if isinstance(column_name, str):
        return " ".join(column_name.split("_")).title()
    
    # If the value provided is not a string, raise an Exception
    else:
        raise Exception("Please makes sure to pass a value of type 'str'.")


def visualize_versus_price(clean_data, x):
    """
    Use seaborn and matplotlib to identify a pattern between avg_rating and 
    battery_capacity.
    
    :param clean_data: a pandas DataFrame containing cleaned smartphone data
    :param x: variable to be plotted on the x-axis
    :return: None
    """
    
    # Create the scatterplot
    sns.scatterplot(x=x, y="price", data=clean_data, hue="os")
    
    # Add x and y labels
    plt.xlabel(" ".join(x.split("_")).title())
    plt.ylabel("Price ($)")
    
    # Add a title to the plot
    plt.title(f"{' '.join(x.split('_')).title()} vs. Price")

    # Show the plot
    plt.show()
    
    
# Call the visualize_versus_price function
visualize_versus_price(cleaned_data, "processor_speed")
