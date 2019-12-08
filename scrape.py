from selenium import webdriver

def main():

    driver = webdriver.Chrome("F:/Downloads/chromedriver_win32/chromedriver.exe") # change this to whereever your driver is

    # select division one button, since that's all we care about, will stay persistent
    driver.get("http://web1.ncaa.org/stats/StatsSrv/rankings?sportCode=MBB")
    div1 = driver.find_element_by_xpath("/html/body/form/table[3]/tbody/tr[2]/td/select/option[2]").click()
    week_base = "/html/body/form/table[3]/tbody/tr[5]/td/select/option[{}]" # base string for selecting week
    stats_base = "/html/body/form/table[3]/tbody/tr[10]/td/select/option[{}]" # base for stats

    for i in range(2, 142):
        driver.find_element_by_xpath(week_base.format(i)).click()
        for j in range(3, 33):
            driver.find_element_by_xpath(stats_base.format(j)).click()
            driver.find_element_by_xpath("/html/body/form/table[3]/tbody/tr[13]/td/input[4]").click()

if __name__ == "__main__":
    main()