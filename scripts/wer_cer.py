#!/usr/bin/env python3

from evaluate import load
import argparse


def parse_input():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser("Evaluation of Speech Translation")
    parser.add_argument("--ref", help="path to reference text file", required=True)
    parser.add_argument("--hyp", help="path to hypothesis text file", required=True)
    return parser.parse_args()


def read_file(path):
    """Read text file and return list of strings, one for each line."""
    with open(path, 'r', encoding='utf8') as f:
        lines = [line.strip() for line in f]
    return lines


def compute_error_rate(hypotheses, references, metric):
    """
    Compute Character Error Rate (CER) or Word Error Rate (WER) between
    a list of hypotheses and references.

    Args:
        hypotheses (List[str]): List of hypotheses, where each hypothesis is a string.
        references (List[str]): List of references, where each reference is a string.
        metric (str): Evaluation metric to use, either 'cer' for CER or 'wer' for WER.

    Returns:
        float: Error rate score between 0 and 1, where lower scores are better.
    """
    evaluator = load(metric)
    return evaluator.compute(predictions=hypotheses, references=references)


def main():
    args = parse_input()
    hypotheses = read_file(args.hyp)
    references = read_file(args.ref)

    # Compute CER and WER and print results
    cer_score = compute_error_rate(hypotheses, references, "cer")
    print(f"CER on hypotheses: {cer_score:.4f}")

    wer_score = compute_error_rate(hypotheses, references, "wer")
    print(f"WER on hypotheses: {wer_score:.4f}")


if __name__ == "__main__":
    main()
