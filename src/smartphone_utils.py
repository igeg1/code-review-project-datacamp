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
print(cleaned_data.head())


def column_to_label(column_name):
    """
    Converts a column name in a pandas DataFrame to a string that can be
    used as a label in a plot.
    
    :param column_name: string containing original column name.
    :return: string that is ready to be presented on a plot.
    """

    """
    Convert a snake_case column name into a title-cased plotting label.

    :param column_name: String containing the original column name (e.g., from a DataFrame).
    :return: A string formatted with spaces instead of underscores and title casing.
    :raises TypeError/Exception: If the input provided is not a string.

    >>> column_to_label("price")
    'Price'
    >>> column_to_label("processor_speed")
    'Processor Speed'
    """
    
    # Validate that column_name is a string
    if isinstance(column_name, str):
        return " ".join(column_name.split("_")).title()
    
    # If the value provided is not a string, raise an Exception
    else:
        raise Exception("Please makes sure to pass a value of type 'str'.")


print(column_to_label("processor_speed"))

def visualize_versus_price(clean_data, x):
    """
    Visualize the relationship between a specified column and price.
    
    Uses a seaborn scatterplot to plot the 'x' variable against 'price',
    colored by the operating system ('os').
    
    :param clean_data: A pandas DataFrame containing cleaned smartphone data.
    :param x: The name of the column to be plotted on the x-axis.
    :return: None
    """
    
    # Create x-label
    x_label = column_to_label(x)

    # Create the scatterplot
    sns.scatterplot(x=x, y="price", data=clean_data, hue="os")
    
    # Add x and y labels
    plt.xlabel(x_label)
    plt.ylabel("Price ($)")
    
    # Add a title to the plot
    plt.title(f"{x_label} vs. Price")

    # Show the plot
    plt.show()
    
    
# Call the visualize_versus_price function
visualize_versus_price(cleaned_data, "processor_speed")
