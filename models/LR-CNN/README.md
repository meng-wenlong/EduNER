# LR-CNN

Source codes for paper:
CNN-Based Chinese NER with Lexicon Rethinking  

Requirement:
======
Python 3.6
Pytorch 0.4.1  

Input format:
======
CoNLL format, with each character and its label splited by a whitespace in a line. The "BMES" tag scheme is prefered.

	别 O  
	错 O  
	过 O  
	邻 O  
	近 O  
	大 B-LOC  
	鹏 M-LOC  
	湾 E-LOC  
	的 O  
	湿 O  
	地 O  

Pretrain embedding:
======
The pretrained embeddings(word embedding, char embedding) are the same with Lattice LSTM(https://github.com/jiesutd/LatticeLSTM)  

Run the code:
======
1. Download the character embeddings and word embeddings and put them in the `data` folder.
2. To train/test the demo: `sh train.sh` / `sh test.sh`
3. To train/test your own data: modify the 'train.sh' or 'test.sh' file with your file path, and run the shell file.
