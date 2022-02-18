# 项目描述
- api 接口自动化项目

# 环境准备
- python 3.6
- pytest 5.4.3
- 其它依赖包

> pip install -r requirements.txt # 安装依赖包
> pip freeze >requirements.txt # 导出依赖包

# 执行pytest用例 
- Terminal 切换目录到该项目根路径 cd/api_object
- pytest 执行所有用例
- pytest -m smoke 执行标记为smoke的用例

# HTML测试报告
- pytest --html=./report/report.html --self-contained-html
- 配置信息写到 pytest.ini文件中执行pytest自己去读取配置文件内容

# 安装pytest-base_url
- pip install pytest-base-url --index-url https://pypi.douban.com/simple

# allure测试报告
- pytest -m smoke --alluredir ./report/allure_raw --clean-alluredir
- allure serve report/allure_raw -p 9909
