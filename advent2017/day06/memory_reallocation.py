import math
from itertools import cycle


def redistribute_memory_blocks(memory_bank):
    """
    :param memory_bank: list of ints, where each int is a memory block
    :return: list of ints, distributed
    """
    new_memory_bank = list(memory_bank)
    num_blocks_in_bank = len(memory_bank)
    index_of_max_val = new_memory_bank.index(max(new_memory_bank))
    blocks_to_distribute = int(new_memory_bank[index_of_max_val])
    new_memory_bank[index_of_max_val] = 0
    # need to know which order to increment our indices
    indices_to_increment = [x for x in range(index_of_max_val + 1, num_blocks_in_bank)] + \
                           [x for x in range(0, index_of_max_val + 1)]
    index_generator = cycle(indices_to_increment)

    while blocks_to_distribute > 0:
        index = next(index_generator)
        new_memory_bank[index] += 1
        blocks_to_distribute -= 1
    print('redistributed from [{}] to [{}])'
          ''.format(','.join([str(x) for x in memory_bank]),
                    ','.join([str(x) for x in new_memory_bank])))
    return new_memory_bank


def how_many_redistributions_until_repeat(input_memory_bank):
    """
    :param input_memory_bank: list: of ints where each int is a memory block
    :return: int: how many times can reallocate_memory_bank be called
                  until a pattern reoccurs
    """
    detected_patterns = []
    redistribution_count = 0
    repeat_detected = False
    mem_bank = input_memory_bank
    while repeat_detected is False:
        detected_patterns.append(list(mem_bank))
        mem_bank = redistribute_memory_blocks(mem_bank)
        redistribution_count += 1
        if mem_bank in detected_patterns:
            repeat_detected = True
    return redistribution_count


if __name__ == '__main__':
    mem_bank = [2, 8, 8, 5, 4, 2, 3, 1, 5, 5, 1, 2, 15, 13, 5, 14]
    print('result: ' +
          str(how_many_redistributions_until_repeat(mem_bank)))