#!/usr/bin/env python3

import argparse
import numpy as np
from typing import List, Tuple, Dict
from collections import defaultdict


def find_unique_pairs_with_equal_sum(arr: np.ndarray) -> None:
    """
    Print all unique pairs in the unsorted numpy array that have equal sums.

    Args:
        arr (np.ndarray): The input array of integers.

    Returns:
        None: The function prints the unique pairs with equal sums.
    """
    pair_sum_map: Dict[int, List[Tuple[int, int]]] = defaultdict(list)

    n = arr.size

    # Iterate through all unique pairs
    for num_one in range(arr.size):
        for num_two in range(num_one + 1, n):
            pair_sum = arr[num_one] + arr[num_two]
            pair_sum_map[pair_sum].append((arr[num_one], arr[num_two]))

    # Print pairs that share the same sum
    for pair_sum, pairs in pair_sum_map.items():
        if len(pairs) > 1:  # we only care about sums with multiple pairs
            pairs_output = " ".join(f"( {pair[0]}, {pair[1]} )" for pair in pairs)
            print(f"Pairs : {pairs_output} have sum : {pair_sum}")


def parse_arguments() -> np.ndarray:
    """
    Parse command-line arguments to get the list of integers and convert them to a numpy array.

    Returns:
        np.ndarray: The numpy array of integers provided as input.
    """
    parser = argparse.ArgumentParser(
        description="Find unique pairs with equal sums in a numpy array."
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
    input_array = np.array(args.numbers)
    print("Input: A[] =", input_array.tolist())
    find_unique_pairs_with_equal_sum(input_array)
