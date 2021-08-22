import pandas as pd


def value_counts(heart_failure: pd.DataFrame, column: str, head: int = 5, verbose: bool = True):
    dtype = heart_failure[column].dtype

    counts = heart_failure[column].value_counts()
    counts_perc = counts / len(heart_failure) * 100

    counts_df = pd.DataFrame({"count": counts, "%": counts_perc})

    counts_df = counts_df.reset_index()
    counts_df = counts_df.rename(columns={'index': column})

    head_df: pd.DataFrame = counts_df.iloc[:head]

    if len(counts_df) != len(head_df):
        others_s = counts_df.iloc[head:].sum()
        others_s[column] = 'others'
        head_df = head_df.append(others_s, ignore_index=True)

    vmin = heart_failure[column].min()
    vmax = heart_failure[column].max()
    nunique = heart_failure[column].nunique()

    if verbose:
        print(head_df)
        print(f'{dtype} min: {vmin} max: {vmax} nunique: {nunique}')

    return head_df, dtype, vmin, vmax, nunique
