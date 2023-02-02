from bs4 import BeautifulSoup
import re

chunk = '''<div class="GameItemWrap">
    #some other div classes that i will need in the future
    <div class="SummonerName">
        <a href="//www.op.gg/summoner/userName=SANDBOX+Ghost" class="Link" target="_blank">SANDBOX Ghost</a>
    </div>
</div>'''
soup = BeautifulSoup(chunk, 'html5lib')
game_data = {}
duo_name = 'SANDBOX Ghost'
for chunks in soup.find_all('div', {'class': 'GameItemWrap'}):
    if chunks.find('a', string=duo_name):
        chunk_for_future = chunks
        a_tag = chunks.find('a', string=duo_name)
        game_data[a_tag.text] = a_tag['href']
print(game_data)

import pandas as pd


def remove_country_code(df, column_name):
    country_codes = ["+1", "+44", "+33", "+81", "+86"]
    df[column_name] = df[column_name].apply(lambda x: x[len(
        next((c for c in country_codes if x.startswith(c)), '')):] if any(
            x.startswith(code) for code in country_codes) else x)
    return df


# Example usage:
df = pd.DataFrame({
    "phone_number": [
        "+11234567890", "+441234567890", "01234567890", "+811234567890",
        "+861234567890"
    ]
})
df = remove_country_code(df, "phone_number")
