from private._config import *


def get_json(path=PATH) -> list:
    """
    Gets json from the given 'path'
    :param path: string
    :return: list of dicts
    """
    with open(path, "r", encoding="utf-8") as file:
        return load(file)


data = get_json()
message = f"Candidates total - {len(data)}"


def get_candidate(name, data=data) -> list:
    """
    Gets candidate with given 'name' from 'data' list of dicts
    :param name: string
    :param data: list of dicts
    :return: list of dicts
    """
    candidates = [i for i in data if name.lower().replace('_', ' ') in i['name'].lower()]
    return candidates


def find_candidates(data=data) -> tuple:
    """
    Searches candidates with matching name or skill in the 'data' list of dicts
    :param data: list of dicts
    :return: list of dicts
    """
    skill = request.args.get('skill', default=1, type=str)
    name = request.args.get('name', default=1, type=str)

    if skill != 1:
        candidates = [i for i in data if skill.lower() in i['skills'].lower()]
        message = f"Candidates with skill matching < {skill} > - {len(candidates)}"
        return candidates, message

    if name != 1:
        candidates = [i for i in data if name.lower().replace('+', ' ') in i['name'].lower()]
        message = f"Candidates found - {len(candidates)}"
        return candidates, message