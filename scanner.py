from selenium import webdriver
import time as t
import numpy as np
import pandas as pd
import pyautogui
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import string
from selenium.webdriver.common.keys import Keys

global failed

d = webdriver.Chrome()
output = pd.DataFrame(columns = ['Destination','Class','Best Cost','Best Time','Cheapest Cost','Cheapest Time','Fastest Cost','Fastest Time'])
eu = ['LHR', 'CDG', 'AMS', 'FRA', 'IST', 'MAD', 'BCN', 'LGW', 'MUC', 'FCO', 'SVO', 'SAW', 'DME', 'DUB', 'ZRH', 'CPH', 'PMI', 'MAN', 'OSL', 'LIS', 'ARN', 'AYT', 'STN', 'BRU', 'DUS', 'VIE', 'MXP', 'ATH', 'TXL', 'HEL', 'AGP', 'VKO', 'HAM', 'GVA', 'LED', 'ESB', 'LTN', 'WAW', 'PRG', 'ALC', 'EDI', 'NCE', 'BUD', 'LPA', 'BHX', 'SXF', 'ADB', 'OTP', 'CGN', 'BGY', 'TFS', 'STR', 'OPO', 'KBP', 'VCE', 'LYS', 'GLA', 'LIN', 'TLS', 'CTA', 'MRS', 'FAO', 'KEF', 'BLQ', 'NAP', 'BRS', 'IBZ', 'BSL', 'CRL', 'HER', 'ACE', 'GOT', 'VLC', 'SOF', 'SKG', 'BOD', 'BGO', 'RIX', 'FUE', 'MLA', 'CIA', 'HAJ', 'BFS', 'KRK', 'PMO', 'AER', 'EIN', 'ADA', 'NTE', 'NCL', 'BEG', 'RHO', 'PSA', 'SIP', 'SVQ', 'BIO', 'LPL', 'EMA']
sa = ['MEX', 'GRU', 'BOG', 'CUN', 'SCL', 'LIM', 'CGH', 'BSB', 'GIG', 'PTY', 'AEP', 'GDL', 'EZE', 'CNF', 'MTY', 'VCP', 'SDU', 'POA', 'REC', 'SSA', 'TIJ', 'CWB', 'FOR', 'HAV', 'SJO', 'MUN', 'FLN', 'BEL', 'CUZ', 'GYN', 'VIX', 'SAL', 'CGB', 'COR', 'MAO', 'GUA', 'NAT', 'IGU', 'MCZ', 'SXM', 'MDZ', 'BPS', 'AQP', 'SLZ', 'NVT', 'CGR', 'MGA', 'JPA', 'BRC', 'AJU', 'LIR', 'ASU', 'THE', 'UDI', 'SLA', 'IGR', 'IQT', 'NQN', 'LDB', 'BZE', 'SAP', 'RAO', 'PIU', 'USH', 'PVH', 'ROS', 'SJP', 'TGU', 'ACA', 'TPP', 'MGF', 'PMW', 'FTE', 'CRD', 'IOS', 'MCP', 'TRU', 'TUC', 'JDO', 'CIX', 'JOI', 'PCL', 'PNZ', 'JUL', 'STM', 'BHI', 'RTB', 'RBR', 'DAV', 'RES', 'IMP', 'REL', 'RGL', 'MDQ', 'BVB', 'MAB', 'MOC', 'JUJ', 'PPB']
na = ['ATL', 'LAX', 'ORD', 'DFW', 'DEN', 'JFK', 'SFO', 'LAS', 'YYZ', 'SEA', 'CLT', 'MCO', 'MIA', 'PHX', 'EWR', 'IAH', 'MSP', 'BOS', 'DTW', 'FLL', 'ORL', 'LGA', 'PHL', 'BWI', 'SLC', 'YVR', 'DCA', 'IAD', 'MDW', 'SAN', 'HNL', 'TPA', 'PDX', 'YUL', 'YYC', 'DAL', 'STL', 'BNA', 'AUS', 'HOU', 'OAK', 'SJC', 'MSY', 'RDU', 'MCI', 'SMF', 'SNA', 'CLE', 'SAT', 'PIT', 'RSW', 'IND', 'CVG', 'YEG', 'CMH', 'BDL', 'PBI', 'JAX', 'ANC', 'ABQ', 'YOW', 'BUF', 'OMA', 'YWG', 'ONT', 'YHZ', 'PVD', 'MKE', 'KOA', 'LGB', 'LIH', 'ELP', 'YTZ', 'SFB', 'ALB', 'BUR', 'PSP', 'SYR', 'YYJ', 'YLW', 'PWM', 'YQB', 'PNS', 'MHT', 'HPN', 'YXE', 'ITO', 'YQR', 'SRQ', 'ROC', 'BTV', 'PIE', 'ECP', 'FAT', 'MFE', 'TLH', 'AMA', 'SBA', 'ISP']
asia = ['PEK', 'DXB', 'HND', 'HKG', 'PVG', 'CAN', 'DEL', 'CGK', 'SIN', 'ICN', 'BKK', 'KUL', 'CTU', 'BOM', 'SZX', 'TPE', 'KMG', 'MNL', 'SHA', 'XIY', 'NRT', 'CKG', 'DMK', 'SGN', 'DOH', 'HGH', 'JED', 'CJU', 'KIX', 'NKG', 'GMP', 'BLR', 'RUH', 'XMN', 'CGO', 'CSX', 'AUH', 'FUK', 'TAO', 'WUH', 'HAN', 'CTS', 'DPS', 'HAK', 'SUB', 'URC', 'SYX', 'TLV', 'TSN', 'OKA', 'CCU', 'MAA', 'HRB', 'KWE', 'DLC', 'THR', 'SHE', 'HYD', 'HKT', 'PUS', 'ITM', 'TNA', 'NNG', 'TYN', 'LHW', 'FOC', 'KNO', 'CGQ', 'UPG', 'SHJ', 'KHN', 'HET', 'DAD', 'SJW', 'MHD', 'COK', 'CNX', 'NGO', 'CEB', 'HFE', 'ZUH', 'NGB', 'WNZ', 'IKA', 'JOG', 'INC', 'BKI', 'HLP', 'KWL', 'PNQ', 'BPN', 'AMD', 'PEN', 'LJG', 'GOI', 'WUX', 'YNT']
af = ['JNB', 'CAI', 'CPT', 'CMN', 'ADD', 'ALG', 'NBO', 'LOS', 'TUN', 'DUR', 'RAK', 'HRG', 'MIR', 'MRU', 'ABV', 'ACC', 'SSH', 'DAR', 'LAD', 'RUN', 'KRT', 'DKR', 'ABJ', 'ORN', 'HBE', 'PLZ', 'AGA', 'EBB', 'DLA', 'DJE', 'MBA', 'PHC', 'SID', 'TNG', 'ZNZ', 'JRO', 'FIH', 'HRE', 'TNR', 'COO', 'AAE', 'HME', 'MWZ', 'KAN', 'ENU', 'VFA', 'WIL', 'BJA', 'KIS', 'NSI', 'CBQ', 'NIM', 'ARK', 'TLM', 'WJR', 'EDL', 'BSK', 'AZR', 'BSO', 'BLJ', 'TMR', 'GHA', 'MYW', 'TKQ', 'BKZ', 'MFA', 'TGT', 'DOD', 'UPG', 'SHJ', 'KHN', 'HET', 'DAD', 'SJW', 'MHD', 'COK', 'CNX', 'NGO', 'CEB', 'HFE', 'ZUH', 'NGB', 'WNZ', 'IKA', 'JOG', 'INC', 'BKI', 'HLP', 'KWL', 'PNQ', 'BPN', 'AMD', 'PEN', 'LJG', 'GOI', 'WUX', 'YNT']
oce = ['SYD', 'MEL', 'BNE', 'AKL', 'PER', 'ADL', 'CHC', 'OOL', 'WLG', 'CNS', 'CBR', 'HBA', 'DRW', 'NAN', 'ZQN', 'TSV', 'LST', 'NTL', 'NSN', 'DUD', 'MKY', 'POM', 'MCY', 'KTA', 'NPE', 'ROK', 'PMR', 'ASP', 'HTI', 'PHE', 'GLT', 'BNK', 'NPL', 'BME', 'CFS', 'TRG', 'ZNE', 'HLZ', 'AYQ', 'BHE', 'IVC', 'PPP', 'ABX', 'ROT', 'EMD', 'KGI', 'PQQ', 'MQL', 'WGA', 'ISA', 'RMA', 'PLO', 'DBO', 'PBO', 'HVB', 'BDB', 'MOV', 'TMW', 'DPO', 'ARM', 'GET', 'HID', 'KNX', 'MGB', 'OLP']
world = ['ATL', 'PEK', 'DXB', 'LAX', 'ORD', 'LHR', 'HND', 'HKG', 'PVG', 'CDG', 'AMS', 'DFW', 'CAN', 'FRA', 'IST', 'DEL', 'CGK', 'SIN', 'ICN', 'DEN', 'BKK', 'JFK', 'KUL', 'SFO', 'MAD', 'CTU', 'LAS', 'BCN', 'BOM', 'YYZ', 'SEA', 'CLT', 'LGW', 'SZX', 'TPE', 'MEX', 'KMG', 'MUC', 'MCO', 'MIA', 'PHX', 'SYD', 'EWR', 'MNL', 'SHA', 'XIY', 'FCO', 'IAH', 'NRT', 'SVO', 'CKG', 'DMK', 'MSP', 'GRU', 'BOS', 'SGN', 'DOH', 'HGH', 'DTW', 'JED', 'MEL', 'FLL', 'ORL', 'SAW', 'BOG', 'DME', 'CJU', 'LGA', 'PHL', 'DUB', 'ZRH', 'CPH', 'KIX', 'PMI', 'MAN', 'OSL', 'LIS', 'ARN', 'BWI', 'AYT', 'STN', 'NKG', 'GMP', 'BLR', 'RUH', 'BRU', 'DUS', 'XMN', 'VIE', 'CGO', 'SLC', 'YVR', 'DCA', 'CSX', 'AUH', 'CUN', 'FUK', 'TAO', 'BNE', 'WUH']
all = sa + na + eu + asia + af + oce

def out(airports):
    output.to_excel('C:\\Users\\WilliamWilson\\Desktop\\Flights not feelings\\flights_' + airports[0] + '.xlsx')


def try_clickid(id):
    try:
        clk = d.find_element_by_id(id)
        clk.click()
    except NoSuchElementException:
        t.sleep(5)
        print("1")
        try:
            clk = d.find_element_by_id(id)
            clk.click()
        except NoSuchElementException:
            print(id)
            t.sleep(5)


def clickcss(css):
  clk = d.find_element_by_css_selector(css)
  clk.click()
def clickid(id):
  clk = d.find_element_by_id(id)
  clk.click()
def sendid(keys,id):
  snd = d.find_element_by_id(id)
  snd.send_keys(keys)
def sendcss(keys,css):
  snd = d.find_element_by_css_selector(css)
  snd.send_keys(keys)
def to_value(val):
  val1 = val.text
  val2 = val1.replace(',', '')
  value = float(val2.strip('$'))
  return(value)

def check_exists_by_css(css):
    try:
        d.find_element_by_css_selector(css)
    except NoSuchElementException:
        return False
    return True
failed = []
twait = 0
ttries = 0
def get_data(code,d,fareType):
  global failed
  global ttries
  global twait
  
  global output
  tries = 0
  
  wait = 0
  print("Waiting for ",code,' ',fareType)
  while check_exists_by_css('#react-view > div.MainViewstyled__Container-sc-17vqwtc-0.goiDuA > div.SearchViewstyled__Container-sc-fgecmz-0.OuSZu > div > div > div > div > div > div.ResultListstyled__ResultList-sc-3646jl-0.kTLSJj > div.Box__StyledBox-sc-19rtrat-0.LxhTl > div.LoadingLinestyled__LoadingLineWrapper-sc-bibgil-0.jxPMsw') and wait < 300:
    
    wait = wait+1
    t.sleep(1)
  print("Waited for ", wait," seconds")
  t.sleep(2)
  while tries < 3:
    try:
      best_cost = to_value(d.find_element_by_css_selector('#react-view > div.MainViewstyled__Container-sc-17vqwtc-0.goiDuA > div.SearchViewstyled__Container-sc-fgecmz-0.OuSZu > div > div > div > div > div > div.ResultListstyled__ResultList-sc-3646jl-0.kTLSJj > div > div.ResultListstyled__ResultListHeader-sc-h8yvgy-2.lnGztr > div > div > div.SortingPanelstyled__StyledPanelItem-sc-a0wlfp-3.gPGcUu > div.SortingPanelstyled__DataContainer-sc-a0wlfp-2.htwhbG > span'))
      best_time = d.find_element_by_css_selector('#react-view > div.MainViewstyled__Container-sc-17vqwtc-0.goiDuA > div.SearchViewstyled__Container-sc-fgecmz-0.OuSZu > div > div > div > div > div > div.ResultListstyled__ResultList-sc-3646jl-0.kTLSJj > div > div.ResultListstyled__ResultListHeader-sc-h8yvgy-2.lnGztr > div > div > div.SortingPanelstyled__StyledPanelItem-sc-a0wlfp-3.gPGcUu > div.SortingPanelstyled__DataContainer-sc-a0wlfp-2.htwhbG > time').text
      cheapest_cost = to_value(d.find_element_by_css_selector('#react-view > div.MainViewstyled__Container-sc-17vqwtc-0.goiDuA > div.SearchViewstyled__Container-sc-fgecmz-0.OuSZu > div > div > div > div > div > div.ResultListstyled__ResultList-sc-3646jl-0.kTLSJj > div > div.ResultListstyled__ResultListHeader-sc-h8yvgy-2.lnGztr > div > div > div:nth-child(2) > div.SortingPanelstyled__DataContainer-sc-a0wlfp-2.htwhbG > span'))
      cheapest_time = d.find_element_by_css_selector('#react-view > div.MainViewstyled__Container-sc-17vqwtc-0.goiDuA > div.SearchViewstyled__Container-sc-fgecmz-0.OuSZu > div > div > div > div > div > div.ResultListstyled__ResultList-sc-3646jl-0.kTLSJj > div > div.ResultListstyled__ResultListHeader-sc-h8yvgy-2.lnGztr > div > div > div:nth-child(2) > div.SortingPanelstyled__DataContainer-sc-a0wlfp-2.htwhbG > time').text
      fastest_cost = to_value(d.find_element_by_css_selector('#react-view > div.MainViewstyled__Container-sc-17vqwtc-0.goiDuA > div.SearchViewstyled__Container-sc-fgecmz-0.OuSZu > div > div > div > div > div > div.ResultListstyled__ResultList-sc-3646jl-0.kTLSJj > div > div.ResultListstyled__ResultListHeader-sc-h8yvgy-2.lnGztr > div > div > div:nth-child(3) > div.SortingPanelstyled__DataContainer-sc-a0wlfp-2.htwhbG > span'))
      fastest_time = d.find_element_by_css_selector('#react-view > div.MainViewstyled__Container-sc-17vqwtc-0.goiDuA > div.SearchViewstyled__Container-sc-fgecmz-0.OuSZu > div > div > div > div > div > div.ResultListstyled__ResultList-sc-3646jl-0.kTLSJj > div > div.ResultListstyled__ResultListHeader-sc-h8yvgy-2.lnGztr > div > div > div:nth-child(3) > div.SortingPanelstyled__DataContainer-sc-a0wlfp-2.htwhbG > time').text
      print(code,fareType,best_cost,best_time,cheapest_cost,cheapest_time,fastest_cost,fastest_time)
      output = output.append({'Destination':code,'Class':fareType,'Best Cost': best_cost,'Best Time':best_time,'Cheapest Cost':cheapest_cost,'Cheapest Time':cheapest_time,'Fastest Cost':fastest_cost,'Fastest Time':fastest_time}, ignore_index = True)
      break
    except:
      t.sleep(5)
      tries = tries+1
      
    else:
      
      break
  
  ttries = ttries + tries
  twait = twait + wait
  
  
  if tries > 1:
    failed.append(code)
    output = output.append({'Destination':code,'Class':"failed"}, ignore_index = True)
  #'Best Cost','Best Time','Cheapest Cost','Cheapest Time','Fastest Cost','Fastest Time'
  
def select(fareType,d):
  select = Select(d.find_element_by_css_selector('body > div:nth-child(75) > div.ContentWrapper__StyledPopoverParent-sc-15796ki-2.gOSbAp > div > div.ContentWrapper__StyledContentWrapper-sc-15796ki-0.cCNSqq > div > div'))
  select.select_by_value(fareType)
def start():
  d.get("https://www.kiwi.com/en/search/tiles/austin-texas-united-states/anywhere/anytime/anytime?cabinClass=ECONOMY-false")
  t.sleep(2)
  clickcss("#cookies_accept > div > div")

def get_flights(code,d):
    
    global output
    
    d.get("https://www.kiwi.com/en/search/tiles/austin-texas-united-states/anywhere/anytime/anytime?cabinClass=ECONOMY-false")
    #t.sleep(2)
       #react-view > div.MainViewstyled__Container-sc-17vqwtc-0.goiDuA > div.SearchFormstyled__StyledSearchForm-sc-1j6aexc-0.eCkXSl.SearchForm > div > div > div.FormWrapperstyled__StyledSearchFormWrapper-sc-i1a9yv-0.kdEAwE > div.FormWrapperstyled__SearchFormContainer-sc-i1a9yv-1.FtKzv > div:nth-child(2) > div > div > div > div.SearchFieldstyled__SearchFieldInputWrapper-sc-1f3jsso-3.eOBVBy > div > input
    #clickcss("#cookies_accept > div > div")
    clickcss("#react-view > div.MainViewstyled__Container-sc-17vqwtc-0.goiDuA > div.SearchFormstyled__StyledSearchForm-sc-1j6aexc-0.eCkXSl.SearchForm > div > div > div.FormWrapperstyled__StyledSearchFormWrapper-sc-i1a9yv-0.kdEAwE > div.FormWrapperstyled__SearchFormContainer-sc-i1a9yv-1.FtKzv > div:nth-child(2) > div > div > div > div.SearchFieldstyled__SearchFieldInputWrapper-sc-1f3jsso-3.eOBVBy > div > div.PlacePickerInputPlacestyled__StyledPlacePickerInputPlace-sc-esw2vf-0.gilAsG")
    t.sleep(3)
    clickcss("#react-view > div.MainViewstyled__Container-sc-17vqwtc-0.goiDuA > div.SearchFormstyled__StyledSearchForm-sc-1j6aexc-0.eCkXSl.SearchForm > div > div > div.FormWrapperstyled__StyledSearchFormWrapper-sc-i1a9yv-0.kdEAwE > div.FormWrapperstyled__SearchFormContainer-sc-i1a9yv-1.FtKzv > div:nth-child(2) > div > div.SearchFieldstyled__SearchFieldWrapper-sc-1f3jsso-1.bwYDRu > div > div.SearchFieldstyled__SearchFieldInputWrapper-sc-1f3jsso-3.eOBVBy > div > input")
    
    sendcss(code,"#react-view > div.MainViewstyled__Container-sc-17vqwtc-0.goiDuA > div.SearchFormstyled__StyledSearchForm-sc-1j6aexc-0.eCkXSl.SearchForm > div > div > div.FormWrapperstyled__StyledSearchFormWrapper-sc-i1a9yv-0.kdEAwE > div.FormWrapperstyled__SearchFormContainer-sc-i1a9yv-1.FtKzv > div:nth-child(2) > div > div.SearchFieldstyled__SearchFieldWrapper-sc-1f3jsso-1.bwYDRu > div > div.SearchFieldstyled__SearchFieldInputWrapper-sc-1f3jsso-3.eOBVBy > div > input")
    t.sleep(5)
    sendcss(Keys.RETURN,"#react-view > div.MainViewstyled__Container-sc-17vqwtc-0.goiDuA > div.SearchFormstyled__StyledSearchForm-sc-1j6aexc-0.eCkXSl.SearchForm > div > div > div.FormWrapperstyled__StyledSearchFormWrapper-sc-i1a9yv-0.kdEAwE > div.FormWrapperstyled__SearchFormContainer-sc-i1a9yv-1.FtKzv > div:nth-child(2) > div > div.SearchFieldstyled__SearchFieldWrapper-sc-1f3jsso-1.bwYDRu > div > div.SearchFieldstyled__SearchFieldInputWrapper-sc-1f3jsso-3.eOBVBy > div > input")
    t.sleep(3)
    sendcss(Keys.ESCAPE,"#react-view > div.MainViewstyled__Container-sc-17vqwtc-0.goiDuA > div.SearchFormstyled__StyledSearchForm-sc-1j6aexc-0.eCkXSl.SearchForm > div > div > div.FormWrapperstyled__StyledSearchFormWrapper-sc-i1a9yv-0.kdEAwE > div.FormWrapperstyled__SearchFormContainer-sc-i1a9yv-1.FtKzv > div:nth-child(2) > div > div.SearchFieldstyled__SearchFieldWrapper-sc-1f3jsso-1.bwYDRu > div > div.SearchFieldstyled__SearchFieldInputWrapper-sc-1f3jsso-3.eOBVBy > div > input")
    t.sleep(3)
    get_data(code,d,"Economy Class")
    current_url = d.current_url
    new_url = current_url.replace("ECONOMY","BUSINESS")
    d.get(new_url)
    get_data(code,d,"Business Class")
    new_url = current_url.replace("ECONOMY","FIRST_CLASS")
    d.get(new_url)
    get_data(code,d,"First Class")
    
def run(airports):
  global output
  try:
    start()
  except:
    t.sleep(10)
    try:
      start()
    except:
      print("start failed twice")  
  for i,c in enumerate(airports):
    print("Total Wait: ",twait," Seconds, Total Tries: ",ttries)
    print(len(failed),"Have Failed: ", failed)
    print('Starting ',c,", number ",i, " of ",len(airports))
    print(output.tail())
    try:
      get_flights(c,d)
    except:
      print(c,' failed!')
      failed.append(c)
      output = output.append({'Destination':c,'Class':"failed"}, ignore_index = True)
    if i % 3 == 0:
      out(airports)
  out(airports)
run(eu)
run(failed)
