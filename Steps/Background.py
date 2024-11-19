from pathlib import Path
from urllib.parse import urlencode
import requests
from behave import *
import pandas as pd
from io import BytesIO
from connection_to_database import execute_sql_query
from datetime import datetime


@given('Fetch the GetICOSReviewCalendarDates data from {get_icos_api}')
def icos_api(context,get_icos_api:str):
    context.get_icos_all_idices_api = get_icos_api

@given('Fetch the sql data from {all_indices_icos_query}')
def icos_query(context,all_indices_icos_query:str):
    context.all_indices_icos_query = all_indices_icos_query


@when('append the following params for icos_data')
def append_params(context):
    context.icos_api_with_params =f"{context.get_icos_all_idices_api}?{urlencode(dict(context.table))}"

@when('make the api request')
def api_request(context):
        context.icos_api_response = requests.get(context.icos_api_with_params,verify=True,timeout=10000)
        if context.icos_api_response.status_code!=200:
            raise ValueError(context.icos_api_response.text)        
        context.icos_api = context.icos_api_response.content

@when('save the data of icos api')
def save_data(context):
    context.icos_data_api = pd.read_csv(BytesIO(context.icos_api),na_filter=False)


@when('Fetch the icos data from sql at {indexSymbol} and {calendarYearMonth}')
def icos_data_query(context,indexSymbol:str,calendarYearMonth:str):
    with open(Path(context.all_indices_icos_query),'r') as fp:
        context.icos_query = fp.read().format(indexSymbol,datetime.strptime(calendarYearMonth,"%Y-%m").strftime("%Y%m"))
    context.icos_df = execute_sql_query("brutus1.bat.ci.dom","SIDDB",context.icos_query)