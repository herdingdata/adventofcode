import re


def sanitise_stream(stream):
    """
    strips all the garbage from a stream
    see also: https://xkcd.com/208/ and https://xkcd.com/1313/
              oh and this one https://xkcd.com/1171/

    :param stream: str
    :return: str:
    """
    exclamation_mark_pattern = re.compile('!.')
    sanitised_stream = re.sub(exclamation_mark_pattern, '', stream)
    garbage_group_pattern = re.compile('<[^>]*>')
    sanitised_stream = re.sub(garbage_group_pattern, '', sanitised_stream)
    return sanitised_stream


def score_groups(stream):
    """
    :param stream: str:
    :return: int:
    """
    stream = sanitise_stream(stream)
    current_level = 0
    running_score = 0
    for char in stream:
        if char == '{':
            current_level += 1
            running_score += current_level
        elif char == '}' and current_level >= 1:
            current_level -= 1
    return running_score



if __name__ == '__main__':
    stream = open('stream.txt').readlines()[0]
    print(score_groups(stream))
