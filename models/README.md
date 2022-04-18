# Model Testing

## Flat + BERT

### Requirement

```bash
Python: 3.7.3
PyTorch: 1.2.0
FastNLP: 0.5.0
Numpy: 1.16.4
```

### Run

```
cd Flat-Lattice-Transformer
```

1. Download the character embeddings and word embeddings.

   Character and Bigram embeddings (gigaword_chn.all.a2b.{'uni' or 'bi'}.ite50.vec) : [Google Drive](https://drive.google.com/file/d/1_Zlf0OAZKVdydk7loUpkzD2KPEotUE8u/view?usp=sharing) or [Baidu Pan](https://pan.baidu.com/s/1pLO6T9D)

   Word(Lattice) embeddings:

   yj, (ctb.50d.vec) : [Google Drive](https://drive.google.com/file/d/1K_lG3FlXTgOOf8aQ4brR9g3R40qi1Chv/view?usp=sharing) or [Baidu Pan](https://pan.baidu.com/s/1pLO6T9D)

   ls, (sgns.merge.word.bz2) : [Baidu Pan](https://pan.baidu.com/s/1luy-GlTdqqvJ3j-A4FcIOw)

2. Modify the `paths.py` to add the pretrained embedding and the dataset

3. Run following commands

   ```bash
   python preprocess.py
   cd V1
   python flat_main.py --dataset edu
   ```

## MECT4CNER

### Requirement

```bash
torch==1.5.1
numpy==1.18.5
FastNLP==0.5.0
fitlog==0.3.2
```

### Run

```
cd MECT4CNER
```

1. Download the pretrained character embeddings and word embeddings and put them in the data folder.

   - Character embeddings (gigaword_chn.all.a2b.uni.ite50.vec): [Google Drive](https://drive.google.com/file/d/1_Zlf0OAZKVdydk7loUpkzD2KPEotUE8u/view?usp=sharing) or [Baidu Pan](https://pan.baidu.com/s/1pLO6T9D)
   - Bi-gram embeddings (gigaword_chn.all.a2b.bi.ite50.vec): [Baidu Pan](https://pan.baidu.com/s/1pLO6T9D)
   - Word(Lattice) embeddings (ctb.50d.vec): [Baidu Pan](https://pan.baidu.com/s/1pLO6T9D)

2. Modify the `Utils/paths.py` to add the pretrained embedding and the dataset

3. Run following commands

   ```bash
   python Utils/preprocess.py
   python main.py --dataset edu
   ```

## SLK-NER

### Requirement

```bash
python == 3.6.10 
torch == 1.3.1 
numpy == 1.17.4 
seqeval == 0.0.12 
tqdm == 4.40.0 
```

### Run

```bash
cd SLK-NER
```

1. Download the character embeddings and word embeddings.

   Character embeddings: [chinese_L-12_H-768_A-12](https://storage.googleapis.com/bert_models/2018_11_03/chinese_L-12_H-768_A-12.zip)
   Word embeddings: [ctb.50d.vec](https://drive.google.com/file/d/1K_lG3FlXTgOOf8aQ4brR9g3R40qi1Chv/view?usp=sharing)

2. Modify DATA_DIR and OUTPUT_DIR in `run_ner.sh`

3. Run the following commands

   ```bash
   bash run_ner.sh
   ```

## LEBERT

### Requirement

```bash
Python 3.7.0
Transformer 3.4.0
Numpy 1.18.5
Packaging 17.1
skicit-learn 0.23.2
torch 1.6.0
tqdm 4.50.2
multiprocess 0.70.10
tensorflow 2.3.1
tensorboardX 2.1
seqeval 1.2.1
```

### Run

```
cd LEBERT
```

1. Copy EduNER dataset to `data/NER/`
2. Convert .char.bmes file to .json file, `python to_json.py`
3. run the shell, `bash run_edu.sh`

## FLERT

### Requirement

PyTorch 1.5+ and Python 3.6+

Install [flair](https://github.com/flairNLP/flair)

### Run

```bash
cd Flert
# revise data_folder in train.py
python train.py
```

## CLNER

### Requirement

```bash
python==3.6
gensim==3.8.1
h5py==2.8.0
PyYAML==5.2
scikit-learn==0.24.2
scipy==1.5.4
torch==1.4.0
tqdm==4.62.3
transformers==3.0.0
```

### Run

```bash
cd CLNER
```

1. Revise data_folder in `config/eduner_doc_cl_kl.yaml` and `config/eduner_doc_cl_l2.yaml`

2. Run:

   ```bash
   CUDA_VISIBLE_DEVICES=0 python train.py --config config/eduner_doc_cl_kl.yaml
   CUDA_VISIBLE_DEVICES=0 python train.py --config config/eduner_doc_cl_l2.yaml
   ```

   