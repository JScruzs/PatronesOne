# Este patron permite crear objetos los cuales ya se habian
# idealizado con anterioridad y el codigo no tendra que depender
# de sus clases.

import copy
class Prot:
     pass

def main():
    proto = Prot()
    proto_copy = copy.deepcopy(proto)

if __name__ == "__main__":
    main()