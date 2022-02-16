export CUDA_VISIBLE_DEVICES=0
python run_ner.py \
    --data_dir ./data/discipline/ \
    --model_type bert \
    --model_name_or_path bert-base-chinese \
    --output_dir /data2/lx/baseline_ner_bk/discipline_slk_model/ \
    --cache_dir ./TEMP_transformers \
    --max_seq_length 256 \
    --do_train \
    --do_predict \
    --evaluate_during_training \
    --per_gpu_train_batch_size 32 \
    --per_gpu_eval_batch_size 32 \
    --learning_rate 5e-5 \
    --num_train_epochs 30 \
    --logging_steps 10



