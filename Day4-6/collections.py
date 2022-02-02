from collections import namedtuple, deque, defaultdict
import urllib.request
import os
import csv

finan_data = 'https://www.stats.govt.nz/assets/Uploads/Annual-enterprise-survey/Annual-enterprise-survey-2020-financial-year-provisional/Download-data/annual-enterprise-survey-2020-financial-year-provisional-csv.csv'
finan_csv = 'finan.csv'
FinData = namedtuple("FinData","variable_name unit category value")

def get_csvdata():
    base = os.path.abspath(os.path.dirname(__file__))
    finan_csv_path = os.path.join(base, finan_csv)
    if not os.path.exists(finan_csv_path):
        urllib.request.urlretrieve(finan_data, finan_csv_path)
    return finan_csv_path

def create_industry_data(data):
    industries = defaultdict(list)
    with open(data) as f:
        for line in csv.DictReader(f):
            try:
                name = line['Industry_name_NZSIOC']
                dollar_unit = line['Units']
                vname = line['Variable_name']
                category = line['Variable_category']
                value = line['Value']
            except ValueError:
                continue

            int_value = value.replace(",", "")
            data_point = FinData(vname, dollar_unit, category, int_value)
            industries[name].append(data_point)

    return industries

def gross_sum_of_industry(industries, industry_name):
    sum = 0
    for values in industries[industry_name]:
        if values.value == 'C' or values.category != "Financial performance":
            continue
        if "millions" in values.unit:
            sum += (int(values.value) * 1000000)
        else:
            sum += int(values.value)
    print(f'The gross sum made by this industry was ${sum}')

def main():
    path = get_csvdata()
    industries = create_industry_data(path)
    industry_name = input("What industry would you like info of: ")
    if(industry_name in industries):
        gross_sum_of_industry(industries, industry_name)
    else:
        print("Invalid industry, please enter a valid one from list below:")
        for key in industries.keys():
            print(key)

if __name__ == "__main__":
    main()
