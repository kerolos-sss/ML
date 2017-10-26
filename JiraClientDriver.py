from JiraApiHandler import JiraApiHandler

class JiraClientDriver:

    def main(self):
        server_url = 'https://carolearmia.atlassian.net'
        user_name = 'carolinemarkoc@gmail.com'
        password = 'C@roline'

        api_handler = JiraApiHandler()

        # create a jira client with username and password
        print('Connecting to jira server at, ' + server_url)
        jira = api_handler.connect_to_jira_project_with_credentials(server_url= server_url, password= password, username= user_name)

        #list jira client projects
        print('Show projects for this server')

        projects = api_handler.get_jira_projects(jira_client= jira)
        print(projects)

        print('Show issues for each project for this server')

        for project in projects:
            print(project.key + '\n')
            print(api_handler.get_jira_project_issues(jira_project= project, jira_client= jira))
            print('\n\n')



