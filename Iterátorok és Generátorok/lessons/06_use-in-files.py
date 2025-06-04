import csv

file_path = 'survey_results_public.csv'


def read_csv_from_generator_fn_1(file):
    with open(file, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        return [row for row in reader]


result_1 = read_csv_from_generator_fn_1(file_path)
# print(len(result_1))
print(result_1[0])

# No MemoryError


def read_csv_from_generator_fn_2(file):
    with open(file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            yield row


# result_2 = [row for row in read_csv_from_generator_fn_2(file_path)]
# print(len(result_2))
result_2 = read_csv_from_generator_fn_2(file_path)
print(next(result_2))
