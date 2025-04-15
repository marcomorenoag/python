import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(funcName)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)

def main():
    data = [1,2,3,4,5,6,7,8,9]
    first, *others, last = data

    logging.debug(f'first: {first}')
    logging.debug(f'others: {others}')
    logging.debug(f'last: {last}')

if __name__ == '__main__':
    main()
