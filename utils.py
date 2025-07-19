import pandas as pd

def load_draws(file_path_or_buffer):
    df = pd.read_csv(file_path_or_buffer)
    draws = df[[col for col in df.columns if col.lower().startswith("draw")]].values.tolist()
    return draws, df
