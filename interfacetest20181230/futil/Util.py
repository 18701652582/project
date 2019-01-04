# coding=utf-8
"""高亮显示元素"""
def highLight(driver,element):
        js = '''
            element = arguments[0];
            element.setAttribute('style','border: 3px solid red;')
            '''
        driver.execute_script(js,element)