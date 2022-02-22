# Education-ner-dataset

> EduNER is a Chinese named entity recognition dataset for education research.

```python
├── models
│   ├── BERT-CRF
│   ├── BERT-NER
│   ├── BiLSTM-CRF
│   ├── CLNER
│   ├── Flat-Lattice-Transformer
│   ├── Flert
│   ├── LEBERT
│   ├── LexiconAugmentedNER
│   ├── LGN
│   ├── LR-CNN
│   ├── MECT4CNER
│   ├── SLK-NER
│   └── TENER
└── sample_EduNER
```

## This full version dataset is coming soon...
- `sample_EduNER/` directory contains the sampleing version of our dataset.
- The related resource paper is currently under review and a sampled version of the dataset is currently released. After final proofing, the full version of the EduNER dataset will be publicly accessible.


## Models
- `models/` directory contains the recent SOTA models
- LexiconAugementedNER includes SoftLexicon+CNN/Transformer/LSTM models.
- CLNER includes the CL-KL and CL-L<sub>2</sub> models.

## Online Annotation Platform
- We provide a temporary account to test [the annotation tool](http://openaied.cn/) 
```markdown
username: edu
password: edu123
```
- A beta educational tool (EDUNERScore) based on our dataset can be accessed. The tool is based on NER technology and allows for the analysis of unstructured educational texts in real time. Due to limited computing resources, it is currently possible to view the cached results. Unfortunately, it is now only available in Chinese.
- Operation see the following picture:
