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

## EduNER：the full version dataset is coming soon...
- `sample_EduNER/` directory contains the sampling version of our dataset.
- The related <em>resource paper ✨</em> is currently under review and a sampled version of the dataset is currently released. After final proofing, the full version of the EduNER dataset will be publicly accessible.
- A snapshot of schema<img src="https://github.com/xuli19/EduNER/blob/main/img/EDUNER_schema.png" alt="EduNER schema" style="zoom:50%;" />


## Models
- `models/` directory contains the recent SOTA models.
- LexiconAugementedNER includes SoftLexicon+CNN/Transformer/LSTM models.
- CLNER includes the CL-KL and CL-L<sub>2</sub> models.

## Online Annotation Platform
- We provide a temporary account to test [the annotation tool](http://openaied.cn/) 
```markdown
username: edu
password: edu123
```
##  Beta application 

- A beta educational tool ( [EDUNERScore](http://openaied.cn/ents) ) based on our dataset can be accessed. The tool is based on NER technology and allows for the analysis of unstructured educational texts in real time. Specifically, the tool can extract the discipline entity from a large-scale unstructured texts, e.g., discouse content, online forums, writing documents etc. It will help the stakeholder to better understand the learning or teaching activity. 
- Due to limited computing resources, only cached results can be viewed at current. In addition, only the Chinese version is now available.
- User instruction, ![operation](https://github.com/xuli19/EduNER/blob/main/img/sample.gif)
