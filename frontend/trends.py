from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US', tz=360)
pytrends.build_payload(kw_list=['recycling', 'garbage'], timeframe=['2022-09-10 2023-08-10', '2022-09-10 2023-08-10'])
wow = pytrends.multirange_interest_over_time()
print(wow)