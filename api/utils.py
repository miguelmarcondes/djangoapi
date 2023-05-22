import requests
import json
import pandas as pd

class fbiRequest():
    def fetch_data_from_fbi_api():
        page = 1
        df_full = pd.DataFrame()
    
        while True:
            response = requests.get('https://api.fbi.gov/wanted/v1/list', params={'page': page})
    
            if response.status_code == 200:
                data = json.loads(response.content)
    
                if 'items' in data:
                    df = pd.DataFrame.from_dict(data['items'])
                    df_full = pd.concat([df_full, df], ignore_index=True)
                    page += 1
                else:
                    break
            else:
                break
            
        df_clean = df_full[['title', 'race', 'sex', 'nationality', 'dates_of_birth_used', 'place_of_birth', 'description']]
        df_clean.loc[:, 'dates_of_birth_used'] = df_clean['dates_of_birth_used'].str[0]
        df_clean.rename(columns={"sex": "gender", "dates_of_birth_used": "date_of_birth", "description": "description"})
    
        return df_clean
