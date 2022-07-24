import requests

def _query(q, subgraph):
    BASE_URL = "https://api.thegraph.com"
    r = requests.post(
        f"{BASE_URL}/subgraphs/name/{subgraph}",
        json={"query": q},
    )
    r.raise_for_status()
    resp = r.json()
    # if "errors" in resp:
        # raise TheGraphQueryError(resp["errors"])
    return resp["data"]

def query_ens_by_id(id, subgraph="ensdomains/ens"):
    q = f"""
    {{
      domains(where: {{id: "{id}"}}) {{
        name
      }}
    }}
    """
    try:
        data = _query(q, subgraph)
    except:
        print("error")
    else:
        if domains := data["domains"]:
            return domains[0]["name"]
        return None
