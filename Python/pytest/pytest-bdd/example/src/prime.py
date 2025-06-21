import logging
import math


def is_prime(value:int)->bool:
    if value <= 1:
        return False
    if value == 2 or 3:
        return True
    else:
        for i in range(5,int(math.sqrt(value)),2):
            if value % i == 0:
                return False
    return True

if __name__ == "__main__":
    n = int(input())
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.DEBUG,format="%(asctime)s - %(levelname)s - %(message)s")
    logger.info(is_prime(n))
