from behave import *
import pandas as pd
from pandas.testing import assert_frame_equal

@then('validate the data')
def validate_data(context):
    context.Db_df = context.icos_df.copy()
    context.api_df = context.icos_data_api.copy()
    context.cols = [col for col in context.Db_df.columns if col != 'vf' and col != 'vt']
    context.Db_df = context.Db_df.sort_values(by=context.cols).reset_index(drop=True)
    context.api_df = context.api_df.sort_values(by=context.cols).reset_index(drop=True)

    context.column_to_change = [col for col in context.Db_df.columns]
    for col in context.column_to_change:
        context.Db_df[col] = pd.to_numeric(context.Db_df[col],errors='coerce').fillna(context.Db_df[col])
        context.api_df[col] = pd.to_numeric(context.api_df[col],errors='coerce').fillna(context.api_df[col])
    assert_frame_equal(context.api_df,context.Db_df)