import sys
import pandas as pd

sys.path.append("..")
from master_stat import filter_dataframe


def test_filter_all_dataframe():
    data = {
    "identifier": [1, 2, 3],
    "identifier_second": [4, 5, 6]
    }
    df = pd.DataFrame(data)
    df_new = filter_dataframe(df, "identifier", [1,2,3])
    assert(df.equals(df_new) == True)