from duneanalytics import DuneAnalytics

class Dune:
    def __init__(self, username, password):
        self.dune = DuneAnalytics(username, password)
        self.dune.login()
        self.dune.fetch_auth_token()

    def query_result(self, query_id):
        # Fetch query result id using query id
        # Query id for any query can be found from the url of the query:
        # For example:
        # https://duneanalytics.com/queries/4494/8769 => 4494
        result_id = self.dune.query_result_id(query_id=query_id)
        data = self.dune.query_result(result_id)
        return data
