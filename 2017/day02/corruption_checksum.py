def get_checksum(spreadsheet):
    """
    :param spreadsheet: list: of lists of numbers
    :return: sum of the differences between max & min in each row
    """
    cumulative_checksum = 0
    for row in spreadsheet:
        diff = max(row) - min(row)
        cumulative_checksum += diff
    return cumulative_checksum


if __name__ == '__main__':
    raw_spreadsheet = open('raw_spreadsheet.txt').readlines()
    spreadsheet = []
    for row in raw_spreadsheet:
        spreadsheet.append([int(v) for v in row.split('	')])
    print('checksum: ' + str(get_checksum(spreadsheet)))
