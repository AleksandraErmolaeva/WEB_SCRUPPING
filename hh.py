
# <h3 data-qa="bloko-header-3" class="bloko-header-section-3"><span data-page-analytics-event="vacancy_search_suitable_item"><a class="serp-item__title" data-qa="serp-item__title" target="_blank" href="https://adsrv.hh.ru/click?b=558034&amp;c=30&amp;place=35&amp;meta=Zs1_KntWVkuCnfzX6gCUzEZPuilNKie5veYZJBIC2BVt82Y4dpAxqF-NthGw_jeGai3eu4afc64Ej-RBuZZvZ1QXlcI9FLcC-KWjqO1Wlihku3hS0QRg8HayL264FxRu6mJo-1pORjBC-lKEmalzWNAxthsPa-CFJ7y94VjhUgqXtlpPxYpuZoMVwgxhrK6XGPOKZlNwjtWeanwJr37pDNspSTNW7VFBo8Oas-uGVaPbQ36BrYTd-P2zjSHJrYn8GnDqx8AkDge6nnASj4x8Tj7j6zDeIcs3rdnbHP_agPUIh0bA_6dvRDEbShw64xUbdlA0xjAo0OA-CWFHXPyhu8LJQkMUBT6DyQm4uzqgrazYy66x_bby0owVtegoPWQ3JSYOqcl4B3rf9jmnyoQUmCcodsYNmvI6k6cF8SLRB9KB_NW_iMFEJH3sFgEZMBwCCsXqxKhtd3hF1T2vlfOiNBy1ADyX4k1KGGtGF48QRla_Qsvvn4CqTp504DxkbPKZNrlftZ940f4jPhfhp2kcIA%3D%3D&amp;clickType=link_to_vacancy&amp;requestId=1693411710622ed52b4a7afe765b8be3&amp;totalVacancies=7620&amp;query=python&amp;position=0&amp;source=vacancies">Преподаватель IT-дисциплин C++, Python (Комендантский проспект, Новочеркасская)</a></span></h3>


import requests
import bs4
import fake_headers
import json

for page_num in range(0,9):
    url = f'https://spb.hh.ru/search/vacancy?no_magic=true&L_save_area=true&text=python+django+flask&excluded_text=&area=2&area=1&salary=&currency_code=RUR&experience=doesNotMatter&order_by=relevance&search_period=0&items_on_page=20&page={page_num}'

    headers_gen = fake_headers.Headers(browser='firefox', os='win')
    response = requests.get (url, headers=headers_gen.generate())
    page_html = response.text
    page_soup = bs4.BeautifulSoup(page_html, 'lxml')


    a_vacancy_list_tag = page_soup.findAll('a', class_ = 'serp-item__title')
    vacancy_information = []
    for vacancy_tag in a_vacancy_list_tag:
        vacancy_link = vacancy_tag['href']
        response_vacancy = requests.get(vacancy_link, headers=headers_gen.generate())
        response_vacancy_html = response_vacancy.text
        vacancy_soup = bs4.BeautifulSoup(response_vacancy_html, 'lxml')
        vacancy_name = vacancy_soup.find('h1',class_ = 'bloko-header-section-1')
        name = vacancy_name.text
        company_name_soup = vacancy_soup.find('span', class_ = 'vacancy-company-name')
        company_name = company_name_soup.text
        salary_soup = vacancy_soup.find(attrs ={'data-qa':'vacancy-salary-compensation-type-net'})
        if salary_soup is None:
            salary = 'Не указано'
        else:
            salary = salary_soup.text
        city_soup = vacancy_soup.find(attrs= {'data-qa':'vacancy-serp__vacancy-address'})
        city = city_soup.text.split(',')[0]
        vacancy_information.append({
            'vacancy_name': name,
            'link': vacancy_link,
            'company_name': company_name,
            'salary': salary,
            'city': city


        })
        # print(city)
    
    print(f'Добавлена информация с {page_num+1} страницы')
   
   
# with open ('vacancy_info.json', 'w') as file:
#     json.dump(vacancy_information, encure_ascii=False)




