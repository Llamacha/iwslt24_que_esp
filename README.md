This repo contains the evaluation scripts needed to replicate the IWSLT 2023 speech translation tasks for Quechua to Spanish.

# IWSLT 2023 Dialectal and Low-Resource Speech Translation Task 

<a href="https://iwslt.org/2023/low-resource">IWSLT 2023 task homepage</a>


## Scripts for BLEU evaluation

We will use <a href="https://github.com/mjpost/sacrebleu">SacreBLEU</a> for evaluation of speech translation output. The following shows how we would compute (lowercased) BLEU on a detokenized example output (`example/example.st.unconstrained.contrastive1.aeb-eng.txt`):

```
pip install sacrebleu==2.0.0
cut -f 7- stm/st-aeb2eng.norm.test1.stm > example/test1.reference.eng
sacrebleu example/test1.reference.eng -i example/example.st.unconstrained.contrastive1.aeb-eng.txt -m bleu -lc
``` 

This should give:
```
{
 "name": "BLEU",
 "score": 19.1,
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

## Scripts for WER/CER evaluation

We'll compute WER and CER for ASR outputs as follows, using the SCLITE tool: 
```
python3 ./wer_cer.py example/smallset.reference.aeb example/smallset.asr.unconstrained.contrastive1.aeb.txt tmp ~/sctk/bin/sclite
```

This should give something like the following (Note this example may not be representative of actual WER/CER because it's just a small set of 100 utterances):
```
example/smallset.asr.unconstrained.contrastive1.aeb.txt 25/03/2022 22:49:38
WER on original hypothesis Error_Rate= 37.5 (#snt=100 #token=600 Corr=67.3 Sub=26.0 Del=6.7 Ins=4.8)
WER on additionally-normalized hypothesis Error_Rate= 31.7 (#snt=100 #token=600 Corr=73.2 Sub=20.2 Del=6.7 Ins=4.8)
CER on original hypothesis Error_Rate= 18.7 (#snt=100 #token=3116 Corr=88.1 Sub=4.7 Del=7.3 Ins=6.8)
CER on additionally-normalized hypothesis Error_Rate= 16.8 (#snt=100 #token=2921 Corr=89.3 Sub=3.7 Del=7.1 Ins=6.1)
```

The WER/CER on "original" refers to text like `asr-aeb.norm.stm` as provided by the setup_data.sh (not the `asr-aeb.raw.stm`). 
The WER/CER on "additionally-normalized" underwent additional normalization (not provided by setup_data.sh) and includes things like diacritic removal (see wer-cer.py for full set of additional normalization). Multiple versions are provided only as diagnostic. 

## Note for IWSLT'22 Evaluation (March 23, 2022)

It has come to our attention that 5 lines of the provided segments.txt file in the LDC package LDC2022E02 need to be removed from BLEU/WER evaluation. These are bad segments that correspond to zero duration or no speech:

The original file `LDC2022E02/data/segments.txt` contains 4293 lines.
Please use this new [`segments.4288lines.txt`](https://www.cs.jhu.edu/~kevinduh/t/iwslt22/segments.4288lines.txt) to decode.
Your submission of the transcript/translation file should be 4288 lines, corresponding to this new `segments.4288lines.txt` file. 

If you already decoded with the original segments file and generated transcriptions/translations with 4293 lines, please run the following script to filter out the 5 lines correspond to the bad segments:

```
python3 filter_bad_segment.py path/to/original/LDC2022E02/data/segments.txt your_file_to_filter resulting_file
```

The resulting_file should be correct with 4288 lines. The 5 lines that are filtered correspond to: 

```
'20170606_000110_13802_A_008209-008322 20170606_000110_13802_A 82.098 83.220'
'20170606_000110_13802_A_010606-010757 20170606_000110_13802_A 106.060 107.570'
'20170606_000110_13802_B_039745-039907 20170606_000110_13802_B 397.450 399.078'
'20170606_000110_13802_B_053041-053104 20170606_000110_13802_B 530.410 531.040'
'20170907_204736_16787_A_040194-040194 20170907_204736_16787_A 401.944 401.944'
```
