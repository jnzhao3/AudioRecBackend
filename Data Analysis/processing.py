import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from collections import Counter
from nltk.corpus import stopwords

class processing:
    def __init__(self, file_path):
        stop_words = set(stopwords.words('english'))

        df = pd.read_csv(file_path)
        df = df.drop(['Id', 'Confidence', 'SpeakerConfidence'], axis=1)

        total_row = df.copy()
        total_row.loc['Total'] = total_row[total_row.columns[3:]].sum()
        sorted_totals = total_row.sort_values('Total', axis=1, ascending=False)
        tags = list(sorted_totals.columns[:5])
        
        flattened = df[df.columns[3:]].idxmax(axis=1)
        text_total = df.copy()
        text_total['Emotion'] = flattened
        
        by_emotion = text_total.copy()
        by_emotion = by_emotion[['Emotion', 'Text']]

        by_emotion = by_emotion.groupby('Emotion', as_index = True).agg({'Text': ' '.join})
        
        fig, axs = plt.subplots(5, figsize=(15, 30))

        for i in range(5):
            word_frequencies = Counter(str(by_emotion.loc[tags[i]]['Text']).split()).most_common()
            word_frequencies = [s for s in word_frequencies if not s[0].lower() in stop_words]
            word_frequencies.sort(key=lambda x: x[1], reverse=True)

            labels, values = zip(*word_frequencies[:20])
            axs[i].bar(labels, values)
            axs[i].set_title(f"Words Associated with {tags[i]}")

        
        fig.savefig(file_path + "_Analysis.png", dpi='figure')
        

