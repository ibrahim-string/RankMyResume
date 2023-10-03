import os
from pdfminer.high_level import extract_text
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd 
class RankMyResume:
    def rank(self,job_description,path):
        os.chdir(f'{path}')
        pdf=list()
        docx=list()
        doc=list()
        similarity_matrix=list()
        matrix=list()
        score=list()
        files=os.listdir()
        for file in files:
            if '.pdf' in file:
                pdf.append(file)
            if '.docx' in file:
                docx.append(file)
            if '.doc' in file:
                doc.append(file)
        text ={'pdf_name':[],'pdf_text':[]}
        for i in pdf:
            try:
                text['pdf_text'].append(extract_text(f'{i}'))
                text['pdf_name'].append(f'{i}')
            except:
                continue
        df=pd.DataFrame(text)
        cv = CountVectorizer()
        for i in df['pdf_text']:
            content=[job_description,i]
            matrix.append(cv.fit_transform(content))
        df['matrix']=matrix
        for i in matrix:
            similarity_matrix.append(cosine_similarity(i))
        for i in range(len(similarity_matrix)):
            score.append(similarity_matrix[i][1][0])
        df['score']=score
        for i in range(len(similarity_matrix)):
            score.append(similarity_matrix[i][1][0])
        df=df.drop(columns=['matrix'])
        df=df.drop(columns=['pdf_text'])
        df=df.sort_values(by='score',ascending=False)
        return df
    def rule_based_rank(self,job_description,path):
        os.chdir(f'{path}')
        pdf=list()
        docx=list()
        doc=list()
        similarity_matrix=list()
        matrix=list()
        score=list()
        files=os.listdir()
        rule1=input("Enter the rule as Country/City/Town/Pin-code:")
        for file in files:
            if '.pdf' in file:
                pdf.append(file)
            if '.docx' in file:
                docx.append(file)
            if '.doc' in file:
                doc.append(file)
        text ={'pdf_name':[],'pdf_text':[]}
        
        rule1=rule1.strip()
        for i in pdf:
            try:
                if rule1 in extract_text(f'{i}'):
                    text['pdf_text'].append(extract_text(f'{i}'))
                    text['pdf_name'].append(f'{i}')
            except:
                continue
        df=pd.DataFrame(text)
        cv = CountVectorizer()
        for i in df['pdf_text']:
            content=[job_description,i]
            matrix.append(cv.fit_transform(content))
        df['matrix']=matrix
        for i in matrix:
            similarity_matrix.append(cosine_similarity(i))
        for i in range(len(similarity_matrix)):
            score.append(similarity_matrix[i][1][0])
        df['score']=score
        for i in range(len(similarity_matrix)):
            score.append(similarity_matrix[i][1][0])
        df=df.drop(columns=['matrix'])
        df=df.drop(columns=['pdf_text'])
        df=df.sort_values(by='score',ascending=False)
        return df