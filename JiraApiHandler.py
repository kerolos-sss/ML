from jira.client import JIRA


class JiraApiHandler:



    def connect_to_jira_project(self, server_url):
        jira_options = {'server': server_url}
        return JIRA(options= jira_options)



    def connect_to_jira_project_with_credentials(self, server_url, username, password):
        jira_options = {'server': server_url}
        return JIRA(options=jira_options, basic_auth=(username, password))


    def connect_to_jira_project_with_oauth(self, server_url, oauth_dictionary):
        jira_options = {'server': server_url}
        return JIRA(options=jira_options, oauth= oauth_dictionary)

    def get_jira_projects(self, jira_client):
        return jira_client.projects()

    def get_jira_project_issues(self, jira_client, jira_project):
        return jira_client.search_issues('project=' + jira_project.key)

    def get_jira_issue_by_key(self, jira_client, issue_key):
        return jira_client.search_issues('key=' + issue_key)
