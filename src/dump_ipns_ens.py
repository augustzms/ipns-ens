import content_hash
from dune import Dune
import sys
import thegraph

def run():
	# Please input the username and password.
	dune = Dune('simplessssss', '8224074zms')
	# For more details, please check dune_query.sql. 
	data = dune.query_result(1062715)['data']['get_result_by_result_id']

	for idx in range(len(data)):
		# namehash is the hash from the ens name.
		# For more details, refer to: https://docs.ens.domains/terminology
		# All results in the dune are formatted as \x for hexadecimal.
		namehash = data[idx]['data']['node'].replace('\\', '0')
		contenthash = data[idx]['data']['hash'].replace('\\', '0')
		if len(namehash) == 0 or len(contenthash) == 0:
			continue

		# Verify the codec of the contenthash, if it's from ipns, at this moment,
		# We will dump the result.
		try:
			codec = content_hash.get_codec(contenthash)
			if "ipns-ns" in codec:
				name = thegraph.query_ens_by_id(namehash)
				if name is not None:
					print(name)
		except:
			continue



if __name__ == '__main__':
    run()
