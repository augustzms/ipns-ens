# Queries to get the events of contents hash changed.
# For more details, refer to https://dune.com/queries/1062715

SELECT evts.node, hash, evts.evt_block_time 
FROM ethereumnameservice."PublicResolver_evt_ContenthashChanged" evts
INNER JOIN
(
	SELECT max(evt_block_time) AS evt_block_time, node 
	FROM ethereumnameservice."PublicResolver_evt_ContenthashChanged" 
	WHERE length(hash) > 0
	GROUP BY node
) AS latest_evts 
ON evts.evt_block_time = latest_evts.evt_block_time AND evts.node = latest_evts.node;
