import json
import os
import re
from typing import Dict

import requests


def get_problems():
    response = requests.get(f"https://codeforces.com/api/problemset.problems")
    if response.status_code == 200:
        print("sucessfully fetched the data")
        # print(json.dumps(response.json(), indent=4))
        problems_response = response.json()
        problems_cache = cache_problems(problems_response["result"]["problems"])
        rename_files(problems_cache)
        # print(problems)
        # rename_files()
    else:
        print(f"Hello person, there's a {response.status_code} error with your request")


def get_problem_name():
    # print()
    pass


def cache_problems(problems):
    cache = {}
    for problem in problems:
        if "contestId" in problem and "index" in problem and "name" in problem:
            cache[f'{problem["contestId"]}{problem["index"]}'] = problem["name"]
    return cache


def rename_files(problems_cache: Dict[str, str]):
    problem_files_path = os.path.normpath(os.getcwd() + os.sep + os.pardir)
    problem_files = os.listdir(problem_files_path)
    file_pattern = "\d+[A-Z]"

    for file_name in problem_files:
        file_path = os.path.normpath(problem_files_path + os.sep + file_name)
        if (
                os.path.isfile(file_path) and
                file_name.endswith(".py") and
                re.match(file_pattern, file_name) and
                file_name.split(".")[0] in problems_cache
        ):
            file_name_without_extension = file_name[0: len(file_name) - 3]
            new_file_name = f'{file_name_without_extension} - {problems_cache[file_name_without_extension].strip()}.py'
            new_file_path = os.path.normpath(problem_files_path + os.sep + new_file_name)
            print(file_path, new_file_path)
            # os.rename(file_path, new_file_name)


get_problems()
