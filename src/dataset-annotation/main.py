# -*- coding: utf-8 -*-
import argparse
import sys
import logging as log
import cfg
import os




# BEGIN MAIN

def main():
    parser = argparse.ArgumentParser(description='Ferramenta de anotação do PhySketch Dataset')
    parser.add_argument("-i", "--input", help="Pasta contendo estrutura /Dataset", required=True)
    parser.add_argument("-s", "--startAt", help="Pula -s imagens",default=0,type=int)
    #parser.add_argument("-o", "--output", help="Pasta de destino", required=True)
    parser.add_argument("-v", "--verbose", help="Verbose", action='store_true')
    args = parser.parse_args()

    cfg.INPUT_DIR = os.path.join(args.input, "raw")
    cfg.OUTPUT_DIR = os.path.join(args.input, "annotated")
    cfg.OUTPUT_CROP_DIR = os.path.join(args.input, "cropped")
    cfg.START_AT = args.startAt

    if args.verbose:
        log.basicConfig(format="%(levelname)s: %(message)s", level=log.DEBUG)
        log.info("Verbose output.")
    else:
        log.basicConfig(format="%(levelname)s: %(message)s")

    import anotacao as an
    ant = an.Annotator()

    ant.run()



if __name__ == '__main__':
    main()


# END MAIN
