# ref: https://github.com/itzmestar/duneanalytics
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
        # https://duneanalytics.com/queries/3705/7192 => 3705
        # https://duneanalytics.com/queries/3751/7276 => 3751
        result_id = self.dune.query_result_id(query_id=query_id)
        data = self.dune.query_result(result_id)
        return data