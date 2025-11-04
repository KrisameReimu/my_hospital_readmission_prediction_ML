"""
Fetch the Diabetes 130-US Hospitals dataset from UCI ML Repository.

This script downloads the dataset and saves it to data/raw/ for reproducibility.
Dataset ID: 296
Source: UCI Machine Learning Repository
"""
import os
import sys
from pathlib import Path

try:
    from ucimlrepo import fetch_ucirepo
except ImportError:
    print("ERROR: ucimlrepo package not found.")
    print("Please install it with: pip install ucimlrepo")
    sys.exit(1)

import pandas as pd


def fetch_and_save_data(output_dir: str = "data/raw"):
    """
    Fetch diabetes hospital readmission dataset and save to CSV.
    
    Args:
        output_dir: Directory to save the dataset
    
    Returns:
        Path to saved CSV file
    """
    print("Fetching Diabetes 130-US Hospitals dataset from UCI ML Repository...")
    print("Dataset ID: 296")
    
    # Fetch dataset
    diabetes_data = fetch_ucirepo(id=296)
    
    # Extract features and target
    X = diabetes_data.data.features
    y = diabetes_data.data.targets
    
    # Combine into single dataframe
    df = pd.concat([X, y], axis=1)
    
    # Create output directory if it doesn't exist
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Save to CSV
    output_file = output_path / "diabetic_data.csv"
    df.to_csv(output_file, index=False)
    
    print(f"\n✓ Dataset saved to: {output_file}")
    print(f"  Shape: {df.shape[0]:,} rows × {df.shape[1]} columns")
    print(f"  Memory usage: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
    
    # Display basic info
    print("\n--- Dataset Preview ---")
    print(df.head(3))
    print("\n--- Target Variable Distribution ---")
    if 'readmitted' in df.columns:
        print(df['readmitted'].value_counts())
    
    print("\n--- Metadata ---")
    print(diabetes_data.metadata)
    
    print("\n--- Variable Information ---")
    print(diabetes_data.variables)
    
    return output_file


if __name__ == "__main__":
    # Get project root (assuming script is in src/data/)
    project_root = Path(__file__).parent.parent.parent
    output_dir = project_root / "data" / "raw"
    
    fetch_and_save_data(str(output_dir))
