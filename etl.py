import pandas as pd

def extract_data(file_path):
    """Extract data from CSV file."""
    return pd.read_csv(file_path)

def transform_data(df):
    """Transform data: Filter ages > 25, increase salary by 10%, and add a new column."""
    df = df[df['age'] > 25]  # Filter
    df['salary'] = df['salary'] * 1.10  # Increase salary
    df['bonus'] = df['salary'] * 0.05  # Add bonus column
    return df

def load_data(df, output_path):
    """Load transformed data to a new CSV file."""
    df.to_csv(output_path, index=False)
    print(f"Data loaded to {output_path}")

if __name__ == "__main__":
    input_file = 'input_data.csv'
    output_file = 'output_data.csv'
    
    data = extract_data(input_file)
    transformed = transform_data(data)
    load_data(transformed, output_file)