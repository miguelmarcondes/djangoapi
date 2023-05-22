import requests
import json
import pandas as pd

class fbiRequest:

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
            
        df_clean = df_full[['title', 'race', 'sex', 'nationality', 'dates_of_birth_used', 'place_of_birth', 'description']].copy()
        df_clean.loc[:, 'dates_of_birth_used'] = df_clean['dates_of_birth_used'].str[0]
        df_clean.rename(columns={"sex": "gender", "dates_of_birth_used": "date_of_birth", "description": "description"}, inplace=True)
        df_clean.to_csv('csv.zip', index=False)
  
class interpolRequest:
    
    def fetch_data_from_interpol_api(self):
        df_entity = self.fetch_notice_id_from_interpol_api()
        list_entity = df_entity.to_list()

        data_list = []
        for notice in list_entity:
            url = f"https://ws-public.interpol.int/notices/v1/red/{notice}"
            response = requests.get(url)
            print(f"Parsing JSON for notice: {notice}")
            if response.status_code == 200:
                try:
                    data = response.json()
                    data_list.append(data)
                except ValueError:
                    print(f"Failed to parse JSON for notice: {notice}")
                    continue
                
        df_full = pd.json_normalize(data_list)
        df_clean = df_full.copy()
        df_clean['forename'] = df_clean['forename'].astype(str)+" "+df_clean['name']
        df_clean = df_clean[['forename', 'nationalities', 'sex_id', 'nationalities', 'date_of_birth', 'place_of_birth', 'arrest_warrants']]
        df_clean.to_csv('csv.zip')

    def fetch_notice_id_from_interpol_api(self):
        page = 1
        df_full = pd.DataFrame()
        next_page = True

        while next_page:
            response = requests.get('https://ws-public.interpol.int/notices/v1/red?resultPerPage=160',
                                    params={'page': page})
            
            if page > 20:
                next_page = False

            if response.status_code == 200:
                data = json.loads(response.content)
    
                if '_embedded' in data:
                    df = pd.DataFrame.from_dict(data['_embedded']['notices'])
                    df_full = pd.concat([df_full, df], ignore_index=True)
                    page += 1
                else:
                    break
            else:
                break


        
        df_entity = df_full['entity_id']
        df_entity = df_entity.str.replace('/', '-')
        return df_entity



