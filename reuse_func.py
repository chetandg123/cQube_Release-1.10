import configparser
import os
import time
import logging
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

from Data.parameters import Data
from get_dir import pwd


class GetData():
    def __init__(self):
        self.p = pwd()


    # def put_log(self,received_msg):
    #     logging.basicConfig(filename=self.p.get_log_dir(),filemode='w',format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',level=logging.INFO)
    #     logging.info(received_msg)

    def get_smoke_log(self):
        logging.basicConfig(filename=self.p.get_smoke_testing_log_dir(), filemode='w', format='%(asctime)s  %(levelname)s  %(message)s',
                            datefmt='%d-%m-%Y %I:%M:%S %p', level=logging.INFO)
        logger = logging.getLogger()
        return logger

    def get_functional_log(self):
        logging.basicConfig(filename=self.p.get_functional_testing_log_dir(), filemode='w', format='%(asctime)s  %(levelname)s  %(message)s',
                            datefmt='%d-%m-%Y %I:%M:%S %p', level=logging.INFO)
        logger = logging.getLogger()
        return logger

    def get_sanity_log(self):
        logging.basicConfig(filename=self.p.get_sanity_testing_log_dir(), filemode='w', format='%(asctime)s  %(levelname)s  %(message)s',
                            datefmt='%d-%m-%Y %I:%M:%S %p', level=logging.INFO)
        logger = logging.getLogger()
        return logger

    def get_regression_log(self):
        logging.basicConfig(filename=self.p.get_regression_testing_log_dir(), filemode='w', format='%(asctime)s  %(levelname)s  %(message)s',
                            datefmt='%d-%m-%Y %I:%M:%S %p', level=logging.INFO)
        logger = logging.getLogger()
        return logger

    def get_domain_name(self):
        config = configparser.ConfigParser()
        config.read(self.p.get_config_ini_path())
        return config['config']['domain']

    def get_username(self):
        config = configparser.ConfigParser()
        config.read(self.p.get_config_ini_path())
        return config['config']['username']

    def get_password(self):
        config = configparser.ConfigParser()
        config.read(self.p.get_config_ini_path())
        return config['config']['password']

    def get_driver(self):
        options = webdriver.ChromeOptions()
        prefs = {'download.default_directory': self.p.get_download_dir()}
        options.add_experimental_option('prefs', prefs)
        options.add_argument('--headless')
        self.driver=webdriver.Chrome(options=options,executable_path=self.p.get_driver_path())
        return self.driver

    def open_cqube_appln(self,driver):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.get(self.get_domain_name())
        self.driver.implicitly_wait(30)

    def login_cqube(self,driver):
        self.driver = driver
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id(Data.email).send_keys(self.get_username())
        self.driver.find_element_by_id(Data.passwd).send_keys(self.get_password())
        self.driver.find_element_by_id(Data.login).click()
        cal = GetData()
        cal.page_loading(self.driver)

    def page_loading(self,driver):
        try:
            driver.implicitly_wait(2)
            self.driver = driver
            for x in range(1, 10):
                elem = self.driver.find_element_by_id('loader').text
                if str(elem) == "Loading…":
                    time.sleep(1)
                if str(elem) != "Loading…":
                    time.sleep(1)
                    break
        except NoSuchElementException:
            pass

    def click_on_state(self, driver):
        self.driver = driver
        self.driver.find_element_by_css_selector(Data.sar_hyper_link).click()
        cal = GetData()
        cal.page_loading(self.driver)

    def get_data_status(self):
        errMsg = self.driver.find_element_by_css_selector('p#errMsg')
        return errMsg

    def navigate_passwordchange(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id(Data.Dashboard).click()
        cal = GetData()
        cal.page_loading(self.driver)
        self.driver.find_element_by_xpath(Data.user_options).click()
        cal.page_loading(self.driver)


    def navigate_to_student_report(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id(Data.Dashboard).click()
        cal = GetData()
        cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.SAR).click()
        cal.page_loading(self.driver)
        # self.driver.find_element_by_xpath("//*[@id='SAR']")
    def navigate_to_school_infrastructure(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id(Data.Dashboard).click()
        cal = GetData()
        cal.page_loading(self.driver)
        self.driver.find_element_by_xpath(Data.School_infra).click()
        cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Report).click()

    def navigate_to_school_infrastructure_map(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id(Data.Dashboard).click()
        cal = GetData()
        cal.page_loading(self.driver)
        self.driver.find_element_by_xpath(Data.School_infra).click()
        cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Reportmap).click()

    def select_month_year(self,y,m):
        year = Select(self.driver.find_element_by_name(Data.select_year))
        month = Select(self.driver.find_element_by_name(Data.select_month))
        time.sleep(2)
        year.select_by_visible_text(y)
        time.sleep(2)
        month.select_by_visible_text(m)
        time.sleep(2)

    def navigate_to_semester_report(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id(Data.Dashboard).click()
        cal = GetData()
        cal.page_loading(self.driver)
        # self.driver.find_element_by_xpath("//a[@id='sr']/div/td[2]").click()
        self.driver.find_element_by_xpath("//*[@id='sr']").click()
        cal.page_loading(self.driver)


    def navigate_to_crc_report(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id(Data.Dashboard).click()
        cal = GetData()
        cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.CRC).click()

    def Details_text(self):
        Details = self.driver.find_elements_by_xpath(Data.details)
        cal = GetData()
        cal.page_loading(self.driver)
        for i in range(len(Details)):
           print(Details[i].text)

    def Click_HomeButton(self):
            self.driver.find_element_by_id(Data.homeicon).click()
            cal = GetData()
            cal.page_loading(self.driver)

    def CRC_footers(self):
        footer = self.driver.find_elements_by_xpath(Data.footer)
        for i in range(len(footer)):
            print(footer[i].text)
            #time.sleep(5)

    def test_Distnames(self):
        dnames = self.driver.find_elements_by_xpath(Data.SAR_Dnames)
        for i in range(len(dnames)):
            print(dnames[i].text)
            #time.sleep(2)

    def dots_dist(self):
        distnames = self.driver.find_elements_by_xpath(Data.SAR_Dnames)
        for i in range(len(distnames)):
            distnames[i].click()
            cal = GetData()
            cal.page_loading(self.driver)
            lists = self.driver.find_elements_by_class_name(Data.dots)
            count = len(lists) - 1
            print(distnames[i].text, ":", count)

    def X_Yaxis(self):
        x_axis = self.driver.find_elements_by_xpath(Data.xaxis)
        #time.sleep(2)
        print("X axis menu list...")
        for i in range(len(x_axis)):
            print(x_axis[i].text)
        print("Y axis menu list...")
        #time.sleep(2)
        y_axis = self.driver.find_elements_by_xpath(Data.yaxis)
        for i in range(len(y_axis)):
            print(y_axis[i].text)

    def crcclusters_click(self):
        clu = self.driver.find_elements_by_xpath(Data.clusterlist)
        for i in range(len(clu)):
            clu[i].click()
            cal = GetData()
            cal.page_loading(self.driver)

    def clusters_text(self):
        cluster = self.driver.find_elements_by_xpath(Data.clusterlist)
        for i in range(len(cluster)):
            cluster[i].click()
            cal = GetData()
            cal.page_loading(self.driver)
            print(cluster[i].text)
            # time.sleep(5)

    def X_axis(self):
        xvalues = self.driver.find_elements_by_xpath(Data.xaxis)
        for i in range(len(xvalues)):
            xvalues[i].click()
            cal = GetData()
            cal.page_loading(self.driver)

    def get_driver_path(self):
        os.chdir('../cQube_Components/')
        executable_path = os.path.join(os.getcwd(), 'Driver/chromedriver1')
        return executable_path

    def crc_downloadwise(self):
        self.driver.find_element_by_xpath("//*[@id='select']/select/option[2]").click()
        cal = GetData()
        cal.page_loading(self.driver)
        self.driver.find_element_by_xpath("//*[@id='select']/select/option[3]").click()
        cal.page_loading(self.driver)
        self.driver.find_element_by_xpath("//*[@id='select']/select/option[4]").click()
        cal.page_loading(self.driver)
        self.driver.find_element_by_xpath("//*[@id='select']/select/option[5]").click()
        cal.page_loading(self.driver)
    def crc_table_value(self):
        rows = self.driver.find_elements_by_xpath(Data.distrows)
        for j in range(len(rows)):
            print(rows[j].text)
            # time.sleep(2)
    #SAR_2
    def blocks_names(self):
        self.driver.find_element_by_xpath(Data.SAR_Bnames).click()
        cal = GetData()
        cal.page_loading(self.driver)
        print("Block details..")
        infob = self.driver.find_elements_by_xpath(Data.details)
        for i in range(len(infob)):
            print(infob[i].text)

    def clusters_names(self):
        self.driver.find_element_by_xpath(Data.SAR_cnames).click()
        cal = GetData()
        cal.page_loading(self.driver)
        print("Cluster details..")
        infoc = self.driver.find_elements_by_xpath(Data.details)
        for i in range(len(infoc)):
            print(infoc[i].text)

    def schools_test(self):
        self.driver.find_element_by_xpath(Data.SAR_Schools_btn).click()
        print("for schools details...")
        cal = GetData()
        cal.page_loading(self.driver)
        infos = self.driver.find_elements_by_xpath(Data.details)
        for i in range(len(infos)):
            print(infos[i].text)

    def Total_details(self):
        details = self.driver.find_elements_by_xpath(Data.SAR_Details)
        for i in range(len(details)):
            print(details[i].text)


    def test_mouse_over(self):
        self.driver.implicitly_wait(20)
        lists = self.driver.find_elements_by_class_name(Data.dots)
        count = len(lists)-1
        # time.sleep(5)
        def mouseover(i):
            action = ActionChains(self.driver)
            action.move_to_element(lists[i]).perform()
            #time.sleep(3)
            del action

        i = 0
        while i < len(lists):
            mouseover(i)
            i = i + 1
        return count
    def Table_data(self):
        tabledata = self.driver.find_elements_by_xpath(Data.distrows)
        for i in range(len(tabledata)):
            print(tabledata[i].text)
        footer = self.driver.find_elements_by_xpath(Data.footer)
        for i in range(len(footer)):
            print(footer[i].text)
            # time.sleep(5)


    def x_yaxis(self):
        xaxis_lists = self.driver.find_elements_by_xpath(Data.xaxis)
        yaxis_lists = self.driver.find_elements_by_xpath(Data.yaxis)
        for i in range(len(xaxis_lists)):
            xaxis_lists[i].click()
            cal = GetData()
            cal.page_loading(self.driver)
            print(xaxis_lists[i].text)
            for j in range(len(yaxis_lists)):
                yaxis_lists[i].click()
                cal = GetData()
                cal.page_loading(self.driver)
                print(yaxis_lists[j].text)

    def CRC_dist_Clicks(self):
        dist = self.driver.find_elements_by_xpath(Data.CRC_Districts)
        for i in range(len(dist)):
            dist[i].click()
            time.sleep(3)
            driver = cqube(self.driver)
            driver.CRC_footers()
