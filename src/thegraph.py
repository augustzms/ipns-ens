import constants
import requests

from exceptions import ENSLookupError, TheGraphQueryError

def _query(q, subgraph):
    BASE_URL = constants.BASE_URL
    r = requests.post(
        f"{BASE_URL}/subgraphs/name/{subgraph}",
        json={"query": q},
    )
    r.raise_for_status()
    resp = r.json()
    if "errors" in resp:
        raise TheGraphQueryError(resp["errors"])
    return resp["data"]

def query_ens_by_id(id, subgraph=constants.ENS):
    q = f"""
    {{
      domains(where: {{id: "{id}"}}) {{
        name
      }}
    }}
    """
    try:
        data = _query(q, subgraph)
    except TheGraphQueryError as e:
        raise ENSLookupError(e)
    else:
        if domains := data["domains"]:
            return domains[0]["name"]
        return None
