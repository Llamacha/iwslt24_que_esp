#!/usr/bin/env python3

from evaluate import load
import argparse

hyp = ["hello world", "good night moon"]
ref = ["hello world", "good night moon"]


def parse_input():
    parser = argparse.ArgumentParser("Evaluation of Speech Translation")
    parser.add_argument("--ref", help="root of ref-text, txt file")
    parser.add_argument("--hyp", help="root of hyp-text, txt file")
    args = parser.parse_args()
    return args


def read_file(root):
    with open(root, 'r', encoding='utf8') as f:
        list_txt = [x.strip() for x in f]
    return list_txt


def get_evaluation_result(hyp,ref,metric):
    if metric == "cer":
        eva = load("cer")
    else:
        eva = load("wer")
    cer_score = eva.compute(predictions=hyp, references=ref)
    return cer_score


def main():
    args = parse_input()
    hyp = read_file(args.hyp)
    ref = read_file(args.ref)
    cer_result = get_evaluation_result(hyp,ref,"cer")
    print("CER on original hypothesis Error_Rate= "+str(cer_result))
    wer_result = get_evaluation_result(hyp,ref,"wer")
    print("WER on original hypothesis Error_Rate= "+str(wer_result))


if __name__ == "__main__":
    main()