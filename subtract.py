from typing import Union

def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int,float]:
    return abs(a - b)

if __name__ == "__main__":
    print(subtract(2,1))
    print(subtract(1,3))
    print(subtract(2.2,1))
    print(subtract(2,1.6))