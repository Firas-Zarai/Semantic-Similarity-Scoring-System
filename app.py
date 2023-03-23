
import argparse
from get_similar_products import get_similar_products
from input_cleaning import input_cleaning

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find similar products')
    parser.add_argument('product_name', type=str, help='Name of the product')
    parser.add_argument('num_similar', type=int, help='Number of similar products to retrieve')
    args = parser.parse_args()

    product_name = input_cleaning(args.product_name)
    num_similar = args.num_similar

    most_similar, least_similar = get_similar_products(product_name, num_similar)

    # Output the results
    print(f'The {num_similar} most similar products to "{product_name}" are:')
    print(most_similar)
    print()
    print(f'The {num_similar} least similar products to "{product_name}" are:')
    print(least_similar)
