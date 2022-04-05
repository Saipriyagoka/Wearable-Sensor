
import random
import pandas as pd
from os.path import exists
from flask_api import status
from collections import defaultdict
from datetime import datetime, timedelta

def generate_values(input_data):
    '''
    genrating Heart rate (60 - 100),
    Respiration Rate (12 - 25),
    Activity (1-5) using python library called random
    and generating 1 hour data based on input timestamp 
    '''
    try:
        generated_data = []
        user_id = input_data.get('user_id', '')
        timestamp = input_data.get('timestamp', '')
        till_timestamp = timestamp + 3600

        file_name = 'patients_data.csv'
        if not exists(file_name):
            df = pd.DataFrame([input_data])
            df.to_csv(file_name)

        for every_second in range(timestamp+1, till_timestamp+1):
            data = {
                'user_id': user_id,
                'timestamp': every_second,
                'heart_rate': random.randint(60, 100),
                'respiration_rate': random.randint(12, 25),
                'activity': random.randint(1, 5),
            }
            # update the DF with new data
            process_values(data)
            generated_data.append(data)

        # caluclates aggragate data based on segments
        caluclate_aggregate_data(user_id)

        return 'Generated Succesfully'
    except Exception as e:
        print(e)
        return 'Failed generating the values'

def process_values(data):
    '''
    Takes the input and update the df for every second
    '''
    try:
        file_name = 'patients_data.csv'
        df = pd.DataFrame([data])
        with open(file_name, 'a') as f:
            df.to_csv(f, header=False)
        return df
    except Exception as e:
        print(e)
        return {}

def caluclate_aggregate_data(user_id, segments=15):
    try:
        file_name = 'patients_data.csv'
        if exists(file_name):
            df = pd.read_csv(file_name)
        else:
            return "Patient Records not found", status.HTTP_404_NOT_FOUND

        segment_wise_data = []
        patient_df = df[df['user_id'] == user_id]
        start = patient_df.head(1).get('timestamp', '')
        end = patient_df.tail(1).get('timestamp', '')
        step_size = int(segments) *60
        for segment in range(int(start), int(end), step_size):
            seg_start = segment
            seg_end = segment + (step_size)
            mask = (patient_df['timestamp'] >= seg_start) & (patient_df['timestamp'] <= seg_end)
            df2 = patient_df.loc[mask]
            if df2.empty:
                break
            
            segment_wise_data.append({
                'user_id': user_id,
                'seg_start': seg_start,
                'seg_end': seg_end,
                'max_hr': df2['heart_rate'].max(),
                'min_hr': df2['heart_rate'].min(),
                'avg_hr': df2['heart_rate'].mean(),
                'max_rr': df2['respiration_rate'].max(),
                'min_rr': df2['respiration_rate'].min(),
                'avg_rr': df2['respiration_rate'].mean(),    
            })

        aggregate_file_name = 'aggragated_data.csv'
        aggragate_df = pd.DataFrame(segment_wise_data, )
        aggragate_df.to_csv(aggregate_file_name)

        return aggragate_df.to_dict()

    except Exception as e:
        print(e)
        return 'Not Processed values'