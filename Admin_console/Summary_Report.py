import time
import unittest
from Data.parameters import Data
from get_dir import pwd
from reuse_func import GetData


class Test_summaryreport(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.p = pwd()
        self.driver = self.data.get_driver()
        self.data.open_cqube_appln(self.driver)
        self.data.page_loading(self.driver)
        self.data.login_to_adminconsole(self.driver)

    def test_summary_icon(self):
        count = 0
        self.data.page_loading(self.driver)
        self.driver.find_element_by_xpath("//*[@id='summary']/img").click()
        self.data.page_loading(self.driver)
        if 'summary-statistics' in self.driver.current_url:
            print("Summmary statistics report page is present ")
        else:
            print('Summary report page is not displayed')
            count = count + 1
        self.assertEqual(0,count,msg='Summary report page is not working')
        self.driver.find_element_by_id('homeBtn').click()
        self.data.page_loading(self.driver)

    def test_dashboard_summary(self):
        count = 0
        self.driver.find_element_by_id(Data.Dashboard).click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='summary']/div/td[2]").click()
        self.data.page_loading(self.driver)
        if 'summary-statistics' in self.driver.current_url:
            print("Summmary statistics report page is present ")
        else:
            print('Summary report page is not displayed')
            count = count + 1
        self.assertEqual(0,count,msg='Summary report page is not working')
        self.driver.find_element_by_id('homeBtn').click()
        self.data.page_loading(self.driver)

    def test_check_summary(self):
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Dashboard).click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='summary']/div/td[2]").click()
        self.data.page_loading(self.driver)
        reports =self.driver.find_elements_by_tag_name('h2')
        count = len(reports)
        for i in range(len(reports)):
            print(reports[i].text)
        self.assertNotEqual(0,count,msg='All summary reports are not present')
        # if count > 6:
        #     print("summary report of all files to be updated")
        if "Diksha data Summary:" in self.driver.page_source:
            print('Diksha data Summary: statistics present')
        else:
            print('Diksha data Summary: is not present')

        if "Student Attendance Summary:" in self.driver.page_source:
            print('Student Attendance Summary: present')
        else:
            print('Student Attendance summmary is not present')

        if "CRC Report Summary:" in self.driver.page_source:
            print('CRC Report Summary: statistics present')
        else:
            print('CRC Report Summary: is not present')

        if "Semester Report Summary:" in self.driver.page_source:
            print(' Semester Report Summary: statistics present')
        else:
            print(' Semester Report Summary: is not present')

        if "Infra Report Summary:" in self.driver.page_source:
           print(' Infra Report Summary: statistics present')
        else:
            print(' Infra Report Summary: is not present')

        if "Inspection Report Summary:" in self.driver.page_source:
           print(' Inspection Report Summary: statistics present')
        else:
            print(' Inspection Report Summary: is not present')

        if "Static district file Summary:" in self.driver.page_source:
            print(' Static district file Summary: statistics present')
        else:
            print(' Static district file Summary: is not present')

        if "Static block file Summary:" in self.driver.page_source:
            print(' Static block file Summary: statistics present')
        else:
            print(' Static block file Summary: is not present')

        if "Static cluster file Summary:" in self.driver.page_source:
            print(' Static cluster file Summary: statistics present')
        else:
            print(' Static cluster file Summary: is not present')

        if "Static school file Summary:" in self.driver.page_source:
            print("Static school file Summary: is present ")
        else:
            print("Static school file Summary: is not present ")


        self.data.page_loading(self.driver)
        self.driver.find_element_by_id('homeBtn').click()
        self.data.page_loading(self.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()