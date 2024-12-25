from typing import Union

def add(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    return x + y

if __name__ == "__main__":
    print(add(2,1))
    print(add(2.1,1.1))
    print(add(2.1,1))
    print(add(2,1.1))
