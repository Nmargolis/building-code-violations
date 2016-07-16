import csv
from datetime import date, datetime



# Your program should calculate the number of violations in each category
# and the earliest and latest violation date for each category. 
# You can use your preferred programming language, and decide on the presentation format of the resulting data.



def process_csv(input_file):
    """Takes csv file name as string, returns dictionary with data for each cateogry

    Expected fields in csv file are:
    violation_id,inspection_id,violation_category,violation_date,violation_date_closed,violation_type

    """ 
    # Dictionary of categories that will take the format of
    categories = {}

    with open(input_file) as csv_source_file:

        # Initialize reader
        reader = csv.DictReader(csv_source_file)

        for row in reader:
            category = row['violation_category']

            date_str = row['violation_date']

            # Convert date to datetime object
            violation_date = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')

            # If category not in categories dict, add it
            if not categories.get(category):
                # Initialize count and dates
                categories[category] = {
                    'count': 1,
                    'earliest': violation_date,
                    'latest': violation_date
                }
            else:
                # Increment the count
                categories[category]['count'] += 1

                # Check if date is earlier than earliest
                if violation_date < categories[category]['earliest']:
                    categories[category]['earliest'] = violation_date
                # Check if date is later than latest
                if violation_date > categories[category]['latest']:
                    categories[category]['latest'] = violation_date

    print_results(categories)

    return categories


def print_results(categories):

    for category in categories:
        category_data = categories[category]
        # print category_data
        print 'Category: {}'.format(category)
        print '         Count: {}'.format(category_data['count'])
        print '         Earliest: {}'.format(category_data['earliest'].strftime('%Y-%m-%d %H:%M:%S'))
        print '         Latest: {}'.format(category_data['latest'].strftime('%Y-%m-%d %H:%M:%S'))


if __name__ == "__main__":

    process_csv('Violations-2012.csv')

          