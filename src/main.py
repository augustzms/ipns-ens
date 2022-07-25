import argparse
import content_hash
import sys
import thegraph

from dune import Dune

def run(username, password):
	dune = Dune(username, password)
	data = dune.query_result(1062715)['data']['get_result_by_result_id']

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
					print(name)
		except Exception as e:
			print(e)
	f.close()



if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Dune analysis account info.')
	parser.add_argument('--username', metavar='username', required=True,
                        help='Dune analysis account user name')
	parser.add_argument('--password', metavar='password', required=True,
                        help='Dune analysis account password')
	args = parser.parse_args()
	run(username=args.username, password=args.password)
