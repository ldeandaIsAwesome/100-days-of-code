from collections import namedtuple, deque, defaultdict
import urllib.request
import os

def get_csvdata():
    finan_data = 'https://www.stats.govt.nz/assets/Uploads/Annual-enterprise-survey/Annual-enterprise-survey-2020-financial-year-provisional/Download-data/annual-enterprise-survey-2020-financial-year-provisional-csv.csv'
    finan_csv = 'finan.csv'

    directory_name = os.path.dirname(__file__)
    finan_csv_path = os.path.join(directory_name, finan_csv)

    urllib.request.urlretrieve(finan_data, finan_csv_path)

def getValue_by_industry(data=finan_csv):
    industries = defaultdict(list)
    with open(data) as f:
        try:
            name = line['Industry_name_NZSIOC']

        except:


def main():
    get_csvdata()


if __name__ == "__main__":
    main()
