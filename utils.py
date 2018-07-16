from collections import OrderedDict

import pandas as pd

ALPHABET_TH = [chr(x) for x in list(range(0x0E01, 0x0E2E))]
TONE_TH = [chr(x) for x in list(range(0x0E47, 0x0E4B))]
VOWEL_TH_F = [chr(x) for x in list(range(0x0E40, 0x0E45))]
VOWEL_TH_B = [chr(x) for x in list(range(0x0E30, 0x0E3B)) + [0x0E45]]
SYMBOL = [chr(x) for x in list(range(0x0020, 0x0030)) + list(range(0x003A, 0x0041)) + list(range(0x005B, 0x0061)) + list(range(0x007B, 0x007F)) + [0] + [0x000A]]
ALPHABET_ENG_B = [chr(x) for x in list(range(0x0041, 0x005B))]
ALPHABET_ENG_S = [chr(x) for x in list(range(0x0061, 0x007B))]
NUM = [chr(x) for x in list(range(0x0030, 0x003A)) ]
NUM_TH = [chr(x) for x in list(range(0x0E50, 0x0E5A))]
SPECIAL_TH = [chr(x) for x in [0x0E2F,0x0E46,0x0E4C]]
SYMBOL_TH = [chr(x) for x in [0x0E3A,0x0E4D,0xE3F,0x04F,0xE4E,0x0E5A,0x0E5B]]

CHAR = ALPHABET_TH + TONE_TH + VOWEL_TH_F + VOWEL_TH_B + SPECIAL_TH + SYMBOL_TH + NUM_TH + ALPHABET_ENG_B + ALPHABET_ENG_S + NUM + SYMBOL

TYPE = ['ALPHABET_TH','TONE_TH','VOWEL_TH_F','VOWEL_TH_B',
             'SPECIAL_TH','SYMBOL_TH','NUM_TH','ALPHABET_ENG_B',
             'ALPHABET_ENG_S','NUM','SYMBOL']

# BASE ON ORCHID CORPUS FROM NECTEC
TAG = ['NPRP', 'NCNM','NONM','NLBL','NCMN','NTTL','PPRS','PDMN','PNTR','PREL','VACT','VSTA','VATT','XVBM',
        'XVAM''XVMM','XVBB','XVAE','DDAN','DDAC','DDBQ','DDAQ','DIAC','DIBQ','DIAQ','DCNM','DONM','ADVN',
        'ADVI','ADVP','ADVS','CNIT','CLTV','CMTR','CFQC','CVBL','JCRG','JCMP','JSBR','RPRE',
        'INT','FIXN','FIXV','EAFF','EITT','NEG','PUNC']

MAP_CHAR_TYPE = OrderedDict([(ch, 'ALPHABET_TH') for ch in ALPHABET_TH] + [(ch, 'TONE_TH') for ch in TONE_TH] \
                            + [(ch, 'VOWEL_TH_F') for ch in VOWEL_TH_F] + [(ch, 'VOWEL_TH_B') for ch in VOWEL_TH_B] \
                            + [(ch, 'SPECIAL_TH') for ch in SPECIAL_TH] + [(ch, 'SYMBOL_TH') for ch in SYMBOL_TH] \
                            + [(ch, 'ALPHABET_ENG_B') for ch in ALPHABET_ENG_B] + [(ch, 'ALPHABET_ENG_S') for ch in ALPHABET_ENG_S] \
                            + [(ch, 'NUM') for ch in NUM] + [(ch, 'NUM_TH') for ch in NUM_TH] + [(ch, 'SYMBOL') for ch in SYMBOL])

MAP_CHAR = OrderedDict([(v, k) for k, v in enumerate(CHAR)])
MAP_TYPE = OrderedDict([(v, k) for k, v in enumerate(TYPE)])
MAP_TAG = OrderedDict([(v, k) for k, v in enumerate(TAG)])
