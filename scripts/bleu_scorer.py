#!/usr/bin/env python3

import argparse
from sacrebleu.metrics import BLEU


def parse_input():
    parser = argparse.ArgumentParser("Evaluation of Speech Translation")
    parser.add_argument("--ref", help="root of ref-text, txt file")
    parser.add_argument("--hyp", help="root of hyp-text, txt file")
    args = parser.parse_args()
    return args 


def read_hyps(root):
    with open(root, 'r', encoding='utf8') as f:
        hyps = [x.strip() for x in f]
    return hyps


def read_refs(root):
    refs = []
    with open(root, 'r', encoding='utf8') as f:
        refss = [x.strip() for x in f]
        refs.append(refss)
    return refs


def result_blue(hyps,refs):
    bleu = BLEU()
    return bleu.corpus_score(hyps,refs)


def output_file(result):
    with open(root, 'w', encoding='utf8') as f:
        f.write(result)


def main():
    args = parse_input() 
    hyps = read_hyps(args.hyp)
    refs = read_refs(args.ref)
    result = result_blue(hyps,refs)
    print(result)


if __name__ == "__main__":
    main()