# from comapny_details import DataStore

# company_id = '9548'
# # company_id = '10137'
# return_data = DataStore("http://www.technopark.org/company-details?id="+str(company_id), company_id)
# return_data.add_data()

from second import job_details
link = "http://www.technopark.org/job-detail?cmpid=10086&vacancy_id=14349"
job_details(link)