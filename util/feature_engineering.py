import pandas as pd
from scipy import stats
from feature_engine.outliers import Winsorizer,OutlierTrimmer


@staticmethod
def if_normal(data,tail):
    if tail == 'left':
        result = data[stats.zscore(data,nan_policy='omit') <-3].count()
    if tail == 'right':
        result = data[stats.zscore(data,nan_policy='omit') > 3].count()

    return result


@staticmethod
def if_skew(data,tail):
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    if tail == 'left':
        result = data[data <(Q1-1.5*IQR)].count()
    if tail == 'right':
        result = data[data >(Q3+1.5*IQR)].count()

    return result

class detect_outlier:
    
    def __init__(self,data):
        self.data = data
        self.outlier_df = None

    def detect_outlier(self):
        outlier_df = pd.DataFrame(columns=['feature','skewness','distribution','left_tail','right_tail','total_outlier','percentage'])

        outlier_df['feature'] = self.data.columns
        outlier_df['skewness'] = outlier_df['feature'].apply(lambda x : self.data[x].skew())
        outlier_df['distribution'] = outlier_df['skewness'].apply(lambda x: 'normal' if x > -0.5 and x < 0.5 else 'skew')
        outlier_df['left_tail'] = outlier_df.apply(lambda x: if_normal(self.data[x['feature']],'left') if x['distribution'] == 'normal' else if_skew(self.data[x['feature']],'left') ,axis=1)
        outlier_df['right_tail'] = outlier_df.apply(lambda x: if_normal(self.data[x['feature']],'right') if x['distribution'] == 'normal' else if_skew(self.data[x['feature']],'right') ,axis=1)
        outlier_df['total_outlier'] = outlier_df['left_tail'] + outlier_df['right_tail']
        outlier_df['percentage'] = outlier_df['total_outlier'] / len(self.data) * 100
        
        return outlier_df