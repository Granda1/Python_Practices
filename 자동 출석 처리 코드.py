#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 필요한 라이브러리들 설치하시고, 여기서부터 아래까지 실행하시면 됩니다! 꼭 한 셀이 실행된 다음에 다음셀을 실행해주세요.

# 이 셀은 교수님의 메모장으로부터 데이터를 읽어오는 코드이에요.
import pandas as pd
from tqdm import tqdm
import time
from selenium.webdriver.common.alert import Alert

empty_list = []
with open('C:/Users/Daniel Hanjoo Rhee/Desktop/10월 5일 투자론 줌 출석 meeting_saved_chat.txt', 'rt', encoding='UTF8') as f:
    data = f.readlines()
    for line in data:
        line = line.strip()
        empty_list.append(line)
uncleaned_list = empty_list[1::2]


# In[3]:


# 여기는 읽어온 데이터에서 학번만을 추리고, 아래 함수에 넣지 못하는 데이터를 따로 보여주는 셀이에요.
import re

rep = '^\d{4}-\d{5}'
uncleaned_students = []
cleaned_list = []
for j in uncleaned_list:
    if re.match(rep,j) != None:
        cleaned_list.append(re.match(rep,j).group())
    else:
        uncleaned_students.append(j)

# student_id는 아래 코드들에 들어가서 자동으로 출석체크가 될 것이에요.
student_id = list(set(cleaned_list))

# 한편 must_click_by_hand는 데이터구조가 달라서 직접 손으로 출석체크를 해야하는 친구들이에요.
must_click_by_hand = list(set(uncleaned_students))


# In[ ]:





# In[8]:


from selenium                          import webdriver
from webdriver_manager.chrome          import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tqdm import tqdm
from selenium.webdriver.common.alert import Alert

# 크롬 드라이버를 생성한다.
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 원하는 url에에 접근한다.
URL = 'https://scard1.snu.ac.kr/snu/attended/faculty-main.do'

# 해당 URL을 연다.
browser.get(URL)

# => 아마 로그인하라는 창이 뜰 거에용.


# In[9]:


# 로그인 아이디 입력.
id_input = browser.find_element(By.XPATH,'//*[@id="ssoForm"]/fieldset/label[1]/input') # YOUR CODE HERE
id_input.send_keys('여기에 mysnu 아이디 입력!')


# In[10]:


# 로그인 비밀번호 입력.
password_input = browser.find_element(By.XPATH,'//*[@id="ssoForm"]/fieldset/label[2]/input') # YOUR CODE HERE
password_input.send_keys('여기에 mysnu 비밀번호 입력!')


# In[11]:


# 로그인 버튼 누르기.
from selenium.webdriver.common.keys import Keys
password_input.send_keys(Keys.RETURN)


# In[12]:


# 전자출결시스템 이동.
element = browser.find_element(By.XPATH,'//*[@id="header_box"]/div[2]/ul/li[2]/a') # YOUR CODE HERE
element.send_keys(Keys.RETURN)


# In[13]:


# 권한 변경을 하기 위해서는 iframe 안으로 들어가야 해요.
iframes = browser.find_element(By.CSS_SELECTOR,'#con_ifr')
browser.switch_to.frame(iframes)


# In[14]:


# 권한변경 이동.
authorization = browser.find_element(By.XPATH,'//*[@id="menu_div"]/ul/li[7]/a') # YOUR CODE HERE
authorization.send_keys(Keys.RETURN)


# In[15]:


# 권한변경에서 교원선택.
authorization_change = browser.find_element(By.XPATH,'//*[@id="authPopUp"]/div[1]/div[2]/div/a[2]') # YOUR CODE HERE
authorization_change.send_keys(Keys.RETURN)


# In[16]:


# 투자론 과목을 고릅시다.
choose_investment = browser.find_element(By.XPATH,'//*[@id="inner_container"]/div[2]/div[4]/table[2]/tbody/tr/td[4]/a') # YOUR CODE HERE
choose_investment.send_keys(Keys.RETURN)


# In[ ]:





# In[18]:


def student_auto_attendance(student_id):
    finished = {}

    for i in tqdm(student_id):
        # 수강생을 검색해봐요.
        time.sleep(1)
        search_student = browser.find_element(By.XPATH,'//*[@id="inner_container2"]/div[1]/div[2]/a') 
        search_student.send_keys(Keys.RETURN)

        # 학번을 넣어볼까용? 나중에 자동화할 때는 student_id[-2]를 for문으로 돌리면 되용.
        time.sleep(4)
        student_num_input = browser.find_element(By.XPATH,'//*[@id="txtHakbun2"]') 
        student_num_input.send_keys(i)

        # 이제 검색을 누릅시당
        time.sleep(1)
        search_enter = browser.find_element(By.XPATH,'//*[@id="pop7"]/div[1]/div[2]/div/a[2]') 
        search_enter.send_keys(Keys.RETURN)

        # 해당 학생을 눌러봐용. 사실 XPATH 찾는 과정에서 오류가 날 수 있어요.
        time.sleep(1)
        name_click = browser.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[2]/div[2]/div[7]/div[1]/table/tbody/tr/td[4]/a') 
        name_click.send_keys(Keys.RETURN)

        # 변경을 눌러볼까용. 이 친구는 해당주차에 맞게 XPATH를 업데이트 시켜야해요.
        time.sleep(1)
        attendance = browser.find_element(By.XPATH,'//*[@id="tr20221004"]/td[5]/a') 
        attendance.send_keys(Keys.RETURN)

        # 결석을 출석으로 바꿉시당
        time.sleep(1)
        attendance_change = browser.find_element(By.XPATH,'//*[@id="tdChgAtdcStatus"]/div/input[3]') 
        attendance_change.send_keys(Keys.RETURN)

        # 요친구는 왼쪽으로 두 칸 방향키를 누르라는 명령이에요.
        attendance_change.send_keys('\ue012'*2)

        # 다시 변경을 찾고 눌러줍시다!
        time.sleep(1)
        change_enter = browser.find_element(By.XPATH,'//*[@id="pop1"]/div[1]/div[2]/div[2]/a[2]') 
        change_enter.send_keys(Keys.RETURN)

        # scard1.snu.ac.kr 내용의 확인을 누르는 작업이당.
        time.sleep(2)
        alert = browser.switch_to.alert.dismiss()
        alert

        # 마지막으로 '확인'을 다시 누릅시당.
        time.sleep(1)
        final_click = browser.find_element(By.XPATH,'//*[@id="inner_container"]/div[2]/div[3]/a')
        final_click.send_keys(Keys.RETURN)

        #어떤 친구를 출석완료했는지를 알아야 하기에, 딕셔너리에 데이터를 넣었어요.
        finished[i] = 'done'

    return finished
print(student_auto_attendance(student_id))   


# In[ ]:





# In[19]:


browser.close()

