This repo contains the evaluation scripts needed to replicate the IWSLT 2023 speech translation tasks for Quechua to Spanish.

# IWSLT 2023 Dialectal and Low-Resource Speech Translation Task 

<a href="https://iwslt.org/2023/low-resource">IWSLT 2023 task homepage</a>


## Requirements
```
pip install -r requirements.txt
``` 

## Scripts for BLEU and CHRF evaluation

We will use <a href="https://github.com/mjpost/sacrebleu">SacreBLEU</a> for evaluation of speech translation output. The following shows how we would compute (lowercased) BLEU on a detokenized example output:

```
python scripts/bleu_scorer.py --hyp files/hyps.txt --ref files/refs.txt
``` 

This should give:
```
{
 "name": "BLEU",
 "score": 34.1,
 "signature": "nrefs:1|case:lc|eff:no|tok:13a|smooth:exp|version:2.0.0",
 "verbose_score": "50.8/26.0/13.9/7.7 (BP = 0.985 ratio = 0.985 hyp_len = 41561 ref_len = 42181)",
 "nrefs": "1",
 "case": "lc",
 "eff": "no",
 "tok": "13a",
 "smooth": "exp",
 "version": "2.0.0"
}
```


