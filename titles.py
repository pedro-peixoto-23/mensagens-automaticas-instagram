from time import sleep


def tit(txt='Título', sim='~'):
    tam = len(txt) + 30
    print(sim * tam)
    print(txt.center(tam))
    print(sim * tam)
    print()
