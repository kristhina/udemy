projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']
dates = ['2016-06-23', '2016-08-29', '1994-01-01']

projects_leaders = zip(projects, leaders)
for project, leader in projects_leaders:
    print("The leader of {} is {}".format(project, leader))

projects_leaders_dates = zip(projects, leaders, dates)
for project, leader, date in projects_leaders_dates:
    print("The leader of {}, started {} is {}".format(project, date, leader))

new_list = enumerate(zip(projects, leaders, dates))
for number, (project, leader, date) in new_list:
    print("{}. The leader of {}, started {} is {}".format(number, project, date, leader))
