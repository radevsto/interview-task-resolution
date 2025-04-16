#!/usr/bin/env python3

import argparse
from typing import List, Tuple, Dict
from collections import defaultdict


def find_unique_pairs_with_equal_sum(arr: List[int]) -> None:
    """
    Print all unique pairs in the unsorted array that have equal sums using a hash map.

    Args:
        arr (List[int]): The input array of integers.

    Returns:
        None: The function prints the unique pairs with equal sums.
    """
    pair_sum_map: Dict[int, List[Tuple[int, int]]] = defaultdict(list)

    n = len(arr)

    # Iterate through all unique pairs
    for num_one in range(n):
        for num_two in range(num_one + 1, n):
            pair_sum = arr[num_one] + arr[num_two]
            pair_sum_map[pair_sum].append((arr[num_one], arr[num_two]))

    # Print pairs that share the same sum
    for pair_sum, pairs in pair_sum_map.items():
        if len(pairs) > 1:  # only care about sums with multiple pairs
            pairs_output = " ".join(f"( {pair[0]}, {pair[1]} )" for pair in pairs)
            print(f"Pairs : {pairs_output} have sum : {pair_sum}")


def parse_arguments() -> List[int]:
    """
    Parse command-line arguments to get the list of integers.

    Returns:
        List[int]: The list of integers provided as input.
    """
    parser = argparse.ArgumentParser(
        description="Find unique pairs with equal sums in an array."
    )
    parser.add_argument(
        "numbers",
        nargs="+",
        type=int,
        help="List of integers in the array, separated by spaces",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    print("Input: A[] =", args.numbers)
    find_unique_pairs_with_equal_sum(args.numbers)
