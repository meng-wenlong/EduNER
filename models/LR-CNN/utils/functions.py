# -*- coding: utf-8 -*-

import sys
import numpy as np
from utils.alphabet import Alphabet

NULLKEY = "-null-"


def normalize_word(word):
    new_word = ""
    for char in word:
        if char.isdigit():
            new_word += '0'
        else:
            new_word += char
    return new_word


def read_instance_with_gaz(num_layer,
                           input_file,
                           gaz,
                           word_alphabet,
                           biword_alphabet,
                           char_alphabet,
                           gaz_alphabet,
                           label_alphabet,
                           number_normalized,
                           max_sent_length,
                           char_padding_size=-1,
                           char_padding_symbol='</pad>'):
    in_lines = open(input_file, 'r', encoding="utf-8").readlines()
    instence_texts = []
    instence_Ids = []
    words = []
    biwords = []
    chars = []
    labels = []
    word_Ids = []
    biword_Ids = []
    char_Ids = []
    label_Ids = []
    for idx in range(len(in_lines)):
        line = in_lines[idx]
        if len(line) > 2:
            pairs = line.strip().split()
            word = pairs[0]
            if number_normalized:
                word = normalize_word(word)
            label = pairs[-1]
            if idx < len(in_lines) - 1 and len(in_lines[idx + 1]) > 2:
                biword = word + in_lines[idx + 1].strip().split()[0]
            else:
                biword = word + NULLKEY
            biwords.append(biword)
            words.append(word)
            labels.append(label)
            word_Ids.append(word_alphabet.get_index(word))
            biword_Ids.append(biword_alphabet.get_index(biword))
            label_Ids.append(label_alphabet.get_index(label))
            char_list = []
            char_Id = []
            for char in word:
                char_list.append(char)
            if char_padding_size > 0:
                char_number = len(char_list)
                if char_number < char_padding_size:
                    char_list = char_list + [char_padding_symbol] * (
                        char_padding_size - char_number)
                assert (len(char_list) == char_padding_size)
            else:
                ### not padding
                pass
            for char in char_list:
                char_Id.append(char_alphabet.get_index(char))
            chars.append(char_list)
            char_Ids.append(char_Id)

        else:
            if ((max_sent_length < 0) or
                (len(words) < max_sent_length)) and (len(words) > 0):
                gazs = []
                gaz_Ids = []
                layergazs = []
                layergazmasks = []
                w_length = len(words)

                for idx in range(w_length):
                    matched_list = gaz.enumerateMatchList(words[idx:])
                    matched_length = [len(a) for a in matched_list]
                    matched_Id = [
                        gaz_alphabet.get_index(entity)
                        for entity in matched_list
                    ]

                    layergaz = []
                    gaz_mask = []
                    for layer in range(num_layer):

                        if layer + 2 in matched_length:
                            index = matched_length.index(layer + 2)
                            layergaz.append(matched_Id[index])
                            gaz_mask.append(0)
                        else:
                            layergaz.append(0)
                            gaz_mask.append(1)
                    layergazs.append(layergaz)
                    layergazmasks.append(gaz_mask)

                    gazs.append(matched_list)
                    matched_Id = [
                        gaz_alphabet.get_index(entity)
                        for entity in matched_list
                    ]
                    if matched_Id:
                        gaz_Ids.append([matched_Id, matched_length])
                    else:
                        gaz_Ids.append([])

                instence_texts.append([words, biwords, chars, gazs, labels])
                instence_Ids.append([
                    word_Ids, biword_Ids, char_Ids, gaz_Ids, label_Ids,
                    layergazs, layergazmasks
                ])
            words = []
            biwords = []
            chars = []
            labels = []
            word_Ids = []
            biword_Ids = []
            char_Ids = []
            label_Ids = []
            gazs = []
            gaz_Ids = []
    return instence_texts, instence_Ids


def build_pretrain_embedding(embedding_path,
                             word_alphabet,
                             embedd_dim=100,
                             norm=True):
    embedd_dict = dict()
    if embedding_path != None:
        embedd_dict, embedd_dim = load_pretrain_emb(embedding_path)

    scale = np.sqrt(3.0 / embedd_dim)
    pretrain_emb = np.empty([word_alphabet.size(), embedd_dim])
    perfect_match = 0
    case_match = 0
    not_match = 0
    pretrain_emb[0, :] = np.random.uniform(-scale, scale, [1, embedd_dim])
    for word, index in word_alphabet.instance2index.items():
        if word in embedd_dict:
            if norm:
                pretrain_emb[index, :] = norm2one(embedd_dict[word])
            else:
                pretrain_emb[index, :] = embedd_dict[word]
            perfect_match += 1
        elif word.lower() in embedd_dict:
            if norm:
                pretrain_emb[index, :] = norm2one(embedd_dict[word.lower()])
            else:
                pretrain_emb[index, :] = embedd_dict[word.lower()]
            case_match += 1
        else:
            pretrain_emb[index, :] = np.random.uniform(-scale, scale,
                                                       [1, embedd_dim])
            not_match += 1
    pretrained_size = len(embedd_dict)
    print(
        "Embedding:\n     pretrain word:%s, prefect match:%s, case_match:%s, oov:%s, oov%%:%s"
        % (pretrained_size, perfect_match, case_match, not_match,
           (not_match + 0.) / word_alphabet.size()))
    return pretrain_emb, embedd_dim


def norm2one(vec):
    root_sum_square = np.sqrt(np.sum(np.square(vec)))
    return vec / root_sum_square


def load_pretrain_emb(embedding_path):
    """
    该函数是从预训练的embedding中，提取每个token对应的embedding；
    返回{token: embedding}, embedding_dimension
    """
    embedd_dim = -1
    embedd_dict = dict()
    with open(embedding_path, 'r', encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if len(line) == 0:
                continue
            tokens = line.split()
            if embedd_dim < 0:
                embedd_dim = len(tokens) - 1
            else:
                assert (embedd_dim + 1 == len(tokens))
            embedd = np.empty([1, embedd_dim])
            embedd[:] = tokens[1:]
            embedd_dict[tokens[0]] = embedd
    return embedd_dict, embedd_dim
