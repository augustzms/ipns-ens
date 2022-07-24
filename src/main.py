#!/usr/bin/python -tt
import content_hash
from dune import Dune
import sys
import thegraph

def run():
	dune = Dune('simplessssss', '8224074zms')
	data = dune.query_result(1062715)['data']['get_result_by_result_id']
    f = open('../results/ens.txt', 'w')

	for idx in range(len(data)):
		# Namehash is the hash from the ens name.
		# For more details, refer to: https://docs.ens.domains/terminology
		# All results in the dune are formatted as \x for hexadecimal.
		namehash = data[idx]['data']['node'].replace('\\', '0')
		contenthash = data[idx]['data']['hash'].replace('\\', '0')
		if len(namehash) == 0 or len(contenthash) == 0:
			continue

		try:
			codec = content_hash.get_codec(contenthash)
			if "ipns-ns" in codec or "ipfs-ns" in codec:
				name = thegraph.query_ens_by_id(namehash)
				if name is not None:
					f.write("%s\n" % name)
		except:
			continue

    f.close()



if __name__ == '__main__':
    run()
